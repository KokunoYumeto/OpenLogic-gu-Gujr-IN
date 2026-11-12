"""Check the actual TeX import, summary, and glossary inventories."""

import json
from pathlib import Path
import re
import sys


project = Path(__file__).resolve().parent
book = Path(sys.argv[1]).resolve()
locale = book.parent.parent
manifest = json.loads((project / "MANIFEST.json").read_bytes())
expected = set((project / "locale" / "scope.txt").read_text(encoding="utf-8").splitlines())
content = locale / "content"
imports = set()
for record in (book / "slc-screen.fls").read_text(encoding="utf-8").splitlines():
    if record.startswith("INPUT "):
        path = (book / record[6:]).resolve()
        if path.is_relative_to(content) and path.suffix == ".tex":
            imports.add(path.relative_to(locale).as_posix())
if imports != expected:
    missing = sorted(expected - imports)
    extra = sorted(imports - expected)
    raise SystemExit(f"Textbook import mismatch. Missing {missing}, extra {extra}")

glossary = (book / "include" / "glossary.tex").read_text(encoding="utf-8")
sort_keys = dict(re.findall(r"(?m)^\\slcterm(?:\[.*?\])?\{([^}]+)\}\{([^}]+)\}", glossary))
gls = (book / "slc-screen.gls").read_text(encoding="utf-8")
rendered = re.findall(r"(?m)^\\glossentry\{([^}]+)\}", gls)
if len(rendered) != manifest["screen"]["glossary_entries"] or set(rendered) != set(sort_keys):
    raise SystemExit("The built glossary does not have the full entry inventory.")
order = [sort_keys[key] for key in rendered]
if order != sorted(order):
    raise SystemExit("The built glossary is out of order.")

summary_paths = {
    int(name) for name in re.findall(r"(?m)^INPUT .*include[/\\]summary-(\d+)\.tex$",
                                    (book / "slc-screen.fls").read_text(encoding="utf-8"))
}
if summary_paths != set(manifest["screen"]["chapter_summaries"]):
    raise SystemExit(f"Summary import mismatch. Observed {sorted(summary_paths)}.")
print(json.dumps({"imported_modules": len(imports), "glossary_entries": len(rendered),
                  "glossary_sorted": True, "chapter_summaries": sorted(summary_paths)}))
