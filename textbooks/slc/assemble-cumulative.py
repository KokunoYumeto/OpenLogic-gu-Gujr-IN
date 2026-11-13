"""Produce an editable cumulative TeX driver without flattening the textbook.

The cumulative driver embeds complete, unexpanded module sources in
filecontents blocks. On a build it writes short-named module files into the
temporary book directory and uses the same subfile groups, conditions,
sectioning modes and identifiers as the modular driver.
"""
from pathlib import Path, PurePosixPath
from hashlib import sha256
import argparse
import json
import re


PROJECT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("source", type=Path, help="Staged Open Logic tree from prepare.py")
args = parser.parse_args()
ROOT = args.source.resolve()
LOCALE = ROOT / "locale/gu"
BOOK = LOCALE / "courses/sets-logic-computation"
IMPORT = re.compile(r"\\olimport(\*)?\s*(?:\[([^][]*)\]\s*)?\{([^{}]*(?:\\[^{}\s]+)?)\}(?:\[([^][]*)\])?")
SLC_NUMBERS = (1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 14, 15)


def read(p):
    return p.read_text(encoding="utf-8")


paths = (PROJECT / "locale" / "scope.txt").read_text(encoding="utf-8").splitlines()
files = {path: f"slc-module-{index:03d}.tex" for index, path in enumerate(paths, 1)}
dispatched = []
unresolved = []


def imports(text, relative=""):
    def convert(match):
        star, directory, name, sectioning = match.groups()
        if name == r"\olpath/locale/\ollangid/content/open-logic-about":
            target = "content/open-logic-about.tex"
        elif any("\\" in part for part in (directory or "", name)):
            raise ValueError((relative, match[0]))
        else:
            start = PurePosixPath("content") if star and directory else PurePosixPath(relative).parent
            target = (start / (directory or "") / name).as_posix()
            if not target.endswith(".tex"):
                target += ".tex"
        if target not in files:
            # These are only legal when a pinned textbook tag suppresses the call;
            # execute a hard error if the branch unexpectedly becomes active.
            unresolved.append((relative, target))
            return r"\slcMissingImport{" + target + "}"
        dispatched.append((relative, target))
        return r"\slcEmbeddedImport{" + files[target] + "}" + ("[" + sectioning + "]" if sectioning else "")

    return "\n".join(
        IMPORT.sub(convert, parts[0]) + (("%" + parts[1]) if len(parts) > 1 else "")
        for line in text.split("\n")
        for parts in [re.split(r"(?<!\\)%", line, maxsplit=1)]
    )


def embed(name, text):
    assert "\\end{filecontents" not in text and not Path(name).is_absolute()
    return f"\\begin{{filecontents*}}[overwrite]{{{name}}}\n" + text.rstrip("\n") + "\n\\end{filecontents*}\n"


sections = [r"""% ગણો, તર્ક, સંગણન — સંપૂર્ણ સંપાદનીય ગુજરાતી LaTeX.
% સ્રોત ZIPમાં આપેલા BUILD.md મુજબ build.ps1 -Cumulative ચલાવો.
% Richard Zach અને Open Logic Project. લખાણ CC BY 4.0 હેઠળ.
% કૃત્રિમ બુદ્ધિથી તૈયાર થયેલો અનુવાદ. પુસ્તક-વિશિષ્ટ પાઠ: GPT-6.1 Sol (Ultra).
"""]
for relative, filename in files.items():
    sections.append("% " + relative + "\n" + embed(filename, imports(read(LOCALE / relative), relative)))
for title in ("preface", "glossary", *(f"summary-{n}" for n in SLC_NUMBERS)):
    sections.append(embed(f"slc-embedded-{title}.tex", read(BOOK / f"include/{title}.tex")))
slc = imports(read(BOOK / "slc.tex")).replace("include/preface", "slc-embedded-preface").replace(
    r"include/summary-\thechapter", r"slc-embedded-summary-\thechapter")
sections.append(embed("slc-embedded-book.tex", slc))
driver = read(BOOK / "slc-screen.tex").replace(r"\loadglsentries{include/glossary}",
                                                r"\loadglsentries{slc-embedded-glossary}")
driver = driver.replace(r"\input{slc}", r"\input{slc-embedded-book}")
anchor = r"\begin{document}"
assert driver.count(anchor) == 1
dispatch = r"""\makeatletter
\NewDocumentCommand \slcEmbeddedImport {m O{section}}{%
  \begingroup
  \def\ol@sectioncs{#2}%
  \def\olfilename{#1}%
  \subfile{#1}%
  \endgroup}
\NewDocumentCommand \slcMissingImport {m}{\PackageError{slc-gu}{Unexpected active import #1}{}}
\makeatother
"""
sections.append(driver.replace(anchor, dispatch + anchor))
payload = "\n".join(sections).encode("utf-8")
(PROJECT / "slc-screen-gu.tex").write_bytes(payload)
print(json.dumps({"modules": len(files), "dispatched_import_calls": len(dispatched),
                  "guarded_inactive_paths": len(unresolved), "sha256": sha256(payload).hexdigest()}))
