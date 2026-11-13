"""Stage the pinned Gujarati OLP corpus under the textbook's locale hook."""
from hashlib import sha256
import json
from pathlib import Path
import re
from shutil import copy2, copytree
from tempfile import mkdtemp

PROJECT = Path(__file__).resolve().parent
REPO = PROJECT.parents[1]


def load(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def replace_once(path, before, after):
    text = path.read_text(encoding="utf-8")
    if text.count(before) != 1:
        raise ValueError(f"Expected one occurrence of {before!r} in {path.name}")
    write(path, text.replace(before, after))


def stage_sources():
    manifest = load(PROJECT / "MANIFEST.json")
    provenance = load(REPO / "SOURCE_PROVENANCE.json")
    records = provenance["units"]
    expected = manifest["sources"]["gujarati_open_logic"]["locale_input_units"]
    if len(records) != expected or len({row["path"] for row in records}) != expected:
        raise ValueError("The Gujarati source inventory differs from the manifest")
    if provenance["source_revision"] != manifest["sources"]["open_logic"]["commit"]:
        raise ValueError("The Gujarati source manifest names a different OLP revision")

    build = PROJECT / ".build"
    build.mkdir(exist_ok=True)
    stage = Path(mkdtemp(prefix="screen-", dir=build))
    olp = stage / "olp"
    locale = olp / "locale" / "gu"
    copytree(REPO / "upstream", olp)
    for group in ("logos", "portraits"):
        copytree(PROJECT / "assets" / group, olp / "assets" / group)
    fonts = olp / "fonts"
    fonts.mkdir()
    for name in ("NotoSansGujarati-Regular.ttf", "NotoSansGujarati-Bold.ttf", "OFL.txt"):
        copy2(REPO / "fonts" / name, fonts)
    copytree(PROJECT / "locale" / "photocredits", locale / "photocredits")
    copy2(PROJECT / "locale" / "open-logic-locale.sty", locale)
    copy2(PROJECT / "locale" / "open-logic-config.sty", locale)

    marked = 0
    for row in records:
        relative = row["path"]
        data = (REPO / "gu" / relative).read_bytes()
        original = (REPO / "upstream" / relative).read_bytes()
        if sha256(data).hexdigest() != row["gujarati_sha256"]:
            raise ValueError(f"Gujarati unit differs from the sealed edition: {relative}")
        if sha256(original).hexdigest() != row["english_sha256"]:
            raise ValueError(f"English unit differs from the pinned edition: {relative}")
        lines = []
        for line in data.decode("utf-8").splitlines(keepends=True):
            code, separator, comment = line.partition("%")
            code, count = re.subn(
                r"(\\ol(?:file|chapter|part)id)(?=[ \t]*\{)", r"\1[gu]", code
            )
            marked += count
            lines.append(code + separator + comment)
        write(locale / relative, "".join(lines))

    for patch in load(PROJECT / "locale" / "patches.json"):
        replace_once(locale / patch["path"], patch["before"], patch["after"])

    # The edition's full-reader settings supply the established Gujarati tokens.
    # Its captions were registered against English in the standalone driver.
    base = (REPO / "reader" / "full-reader-config.sty").read_text(encoding="utf-8")
    write(locale / "gu-reader-tokens.sty", base.replace("{english}", "{gujarati}"))

    # The upstream babel option is still Gujarati. cleveref only accepts its
    # own supported language list, and the Gujarati names are registered locally.
    replace_once(
        olp / "sty" / "open-logic.sty",
        r"\RequirePackage[capitalize,nameinlink,english,\ollanguage]{cleveref}",
        r"\RequirePackage[capitalize,nameinlink,english]{cleveref}",
    )
    book_class = olp / "sty" / "open-logic-book.cls"
    replace_once(book_class, "      pdfdisplaydoctitle,\n", "")
    replace_once(book_class, r"\RequirePackage[a-1b]{pdfx}", r"\RequirePackage[a-2b]{pdfx}")
    replace_once(book_class, r"\usepackage[osf]{Baskervaldx}", "")
    replace_once(book_class, r"\usepackage[scaled=.92]{helvet}", "")
    replace_once(book_class, r"\OLPbookformat{8in}{5in}{.6in}{1}",
                 r"\OLPbookformat{9.5in}{7in}{.7in}{1}")
    replace_once(book_class, r"\settypeblocksize{*}{300pt}{1.62}",
                 r"\settypeblocksize{*}{435pt}{1.32}")
    replace_once(book_class, r"(0in,3.5in)", r"(0in,.435\stockheight)")
    replace_once(book_class, r"\vbox to 4.5in", r"\vbox to .565\stockheight")
    replace_once(book_class, r"\textsc{\OLPbookversion}", r"\textbf{\OLPbookversion}")
    replace_once(olp / "open-logic-config.sty", "is atomic: ", "પરમાણુક છે: ")
    replace_once(olp / "open-logic-config.sty", "{exercise.}", "{સ્વાધ્યાય.}")
    replace_once(
        olp / "bib" / "natbib-oup.bst",
        'FUNCTION {bbl.and}\n{ "and"}',
        'FUNCTION {bbl.and}\n{ "અને"}',
    )

    envs = olp / "sty" / "open-logic-book-envs.sty"
    replace_once(envs, r"\begin{mdframed}[style=defishstyle]",
                 r"\begin{mdframed}[style=defishstyle,nobreak=true]")

    replace_once(
        olp / "sty" / "open-logic.sty",
        r"\begin{adjustbox}{max width=\textwidth}",
        r"\begin{adjustbox}{max width=\dimexpr\linewidth-1pt\relax}",
    )

    # Bound the two unbreakable objects reported by the screen proof.
    for path, first, last, occurrence in (
        ("first-order-logic/syntax-and-semantics/formation-sequences.tex",
         r"\tuple{", "}", 1),
        ("turing-machines/machines-computations/representing-tms.tex",
         r"\begin{tikzpicture}", r"\end{tikzpicture}", 3),
    ):
        unit = locale / "content" / path
        text = unit.read_text(encoding="utf-8")
        opening = "\\[\n" + first
        closing = "\n" + last + "\n\\]"
        hits = [match.start() for match in re.finditer(re.escape(opening), text)]
        start = hits[occurrence - 1]
        stop = text.index(closing, start) + len(closing)
        body = text[start + 3:stop - 2]
        replacement = "\\begin{maxwidth}\n$\\displaystyle\n" + body + "$\n\\end{maxwidth}"
        write(unit, text[:start] + replacement + text[stop:])

    book = locale / "courses" / "sets-logic-computation"
    copytree(PROJECT / "book", book)
    copy2(book / "slc-config.gu.sty", book / "slc-config.sty")
    copy2(PROJECT / "assets" / "tex" / "nowidow.sty", book)
    return {
        "book": str(book),
        "olp": str(olp),
        "stage": str(stage),
        "source_units": len(records),
        "localized_ids": marked,
    }


if __name__ == "__main__":
    print(json.dumps(stage_sources()))
