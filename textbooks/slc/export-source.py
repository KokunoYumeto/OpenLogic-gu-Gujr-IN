"""Export just the recorded local inputs and the required licence/build files."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

PROJECT = Path(__file__).resolve().parent
BOOK = Path("locale/gu/courses/sets-logic-computation")


def archive_source(tree, output):
    book = tree / BOOK
    recorder = (book / "slc-screen.fls").read_text(encoding="utf-8").splitlines()
    resolve = lambda prefix: {(book / row[len(prefix):]).resolve()
                              for row in recorder if row.startswith(prefix)}
    consumed = {p for p in resolve("INPUT ") - resolve("OUTPUT ")
                if p.is_relative_to(tree) and p.is_file()}
    excluded = {".aux", ".bbl", ".bcf", ".blg", ".fls", ".glo", ".glg",
                ".gls", ".idx", ".ist", ".log", ".out", ".pcr", ".prb", ".toc", ".xmpi"}
    consumed = {p for p in consumed if p.suffix.lower() not in excluded}
    # BibTeX reads the database separately; it is not in LuaLaTeX's recorder.
    biblog = (book / "slc-screen.blg").read_text(encoding="utf-8", errors="replace")
    assert "open-logic.bib" in biblog and "natbib-oup.bst" in biblog, biblog
    consumed.update({tree / "bib/open-logic.bib", tree / "bib/natbib-oup.bst"})
    # LuaHBTeX's HarfBuzz font loader records these font paths in the final
    # engine log, but the Lua file access does not appear in MiKTeX's .fls.
    texlog = (book / "slc-screen.log").read_text(encoding="utf-8", errors="replace")
    font_paths = tuple(tree / "fonts" / name for name in
                       ("NotoSansGujarati-Regular.ttf", "NotoSansGujarati-Bold.ttf"))
    unwrapped_log = "".join(texlog.splitlines())
    if any(font.name not in unwrapped_log for font in font_paths):
        raise ValueError("Final LuaHBTeX log is missing a staged Gujarati font.")
    consumed.update(font_paths)
    for path in ("LICENSE.md", "assets/photos/README.md", "assets/portraits/LICENSE.md", "fonts/OFL.txt"):
        consumed.add(tree / path)
    members = {("source/" + p.relative_to(tree).as_posix()): p.read_bytes() for p in consumed}
    companion = ["LICENSE-SLC.md", "BUILD.md", "build.ps1", "WindowsTeXJob.cs",
                 "check-build.py", "MANIFEST.json", "locale/scope.txt", "slc-screen-gu.tex"]
    members.update({name: (PROJECT / name).read_bytes() for name in companion})
    members.update({("licenses/nowidow/" + p.name): p.read_bytes()
                    for p in (PROJECT / "assets" / "tex").iterdir() if p.name != "nowidow.sty"})
    assert sum(name.startswith("source/locale/gu/content/") and name.endswith(".tex")
               for name in members) == 176
    members["SOURCE-SHA256SUMS.txt"] = "".join(
        f"{sha256(data).hexdigest()}  {name}\n" for name, data in sorted(members.items())
    ).encode("ascii")
    temporary = output.with_suffix(".tmp")
    with ZipFile(temporary, "w", compression=ZIP_DEFLATED, compresslevel=6) as z:
        for name, data in sorted(members.items()):
            assert not {"..", ".git", "build", ".build"}.intersection(Path(name).parts)
            info = ZipInfo(name, (2026, 11, 13, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    with ZipFile(temporary) as z:
        assert sorted(z.namelist()) == sorted(members) and z.testzip() is None
    temporary.replace(output)
    print(json.dumps({"members": len(members), "sha256": sha256(output.read_bytes()).hexdigest()}))


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("tree", type=Path)
    args = cli.parse_args()
    archive_source(args.tree.resolve(), PROJECT / "slc-source-gu.zip")


if __name__ == "__main__":
    main()
