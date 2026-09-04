"""Prepare the cumulative reader through Arithmetization; no TeX process is launched."""
from pathlib import Path
import hashlib
import json
import re
import runpy

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
runpy.run_path(str(ROOT / "tools" / "prepare_size.py"))
body = (BUILD / "size-body.tex").read_text(encoding="utf-8")
receipts = json.loads((BUILD / "size-input-hashes.json").read_text(encoding="utf-8"))
names = ["integers", "rationals", "reals", "cuts", "reflections", "checking-details", "cauchy"]
tokens = {
    "element": ("ઘટક", "ઘટકો"),
    "surjective": ("વ્યાપ્ત", "વ્યાપ્ત"),
    "surjection": ("વ્યાપ્ત વિધેય", "વ્યાપ્ત વિધેયો"),
    "injective": ("એક-એક", "એક-એક"),
    "injection": ("એક-એક વિધેય", "એક-એક વિધેયો"),
    "bijective": ("એક-એક અને વ્યાપ્ત", "એક-એક અને વ્યાપ્ત"),
    "bijection": ("એક-એક વ્યાપ્ત વિધેય", "એક-એક વ્યાપ્ત વિધેયો"),
    "enumerable": ("ગણનીય", "ગણનીય"),
    "nonenumerable": ("અગણનીય", "અગણનીય"),
}
body += "\n\\part{અંકગણિતીકરણ}\n"
for name in names:
    path = ROOT / "gu" / "content" / "sets-functions-relations" / "arithmetization" / f"{name}.tex"
    text = path.read_text(encoding="utf-8").split(r"\begin{document}", 1)[1].rsplit(r"\end{document}", 1)[0]
    text = re.sub(r"!!\^?a?\{([^}]+)\}(s?)", lambda match: tokens[match[1]][bool(match[2])], text)
    assert "!!" not in text
    body += text + "\n"
    receipts.append({"path": path.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})

# The chapter driver is an aligned source unit even though the adapter expands
# its imports into one cumulative part rather than embedding the subfiles wrapper.
driver = ROOT / "gu" / "content" / "sets-functions-relations" / "arithmetization" / "arithmetization.tex"
receipts.append({"path": driver.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(driver.read_bytes()).hexdigest(), "role": "chapter_driver_expanded"})

keys = set()
for block in re.split(r"(?=\\olfileid)", body):
    match = re.search(r"\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}", block)
    if not match:
        continue
    prefix = ":".join(match.groups())
    keys.add(prefix + ":sec")
    for label in re.findall(r"\\ollabel\{([^}]+)\}", block):
        keys.add(prefix + ":" + label)
    for label in re.findall(r"\\label\{([^}]+)\}", block):
        keys.add(label)

(BUILD / "arithmetization-body.tex").write_text(body, encoding="utf-8")
(BUILD / "arithmetization-available-labels.tex").write_text(
    "\n".join(r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}" for key in sorted(keys)) + "\n",
    encoding="utf-8",
)
(BUILD / "arithmetization-available-labels.json").write_text(json.dumps(sorted(keys), indent=2) + "\n", encoding="utf-8")
(BUILD / "arithmetization-input-hashes.json").write_text(json.dumps(receipts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
assert len(receipts) == 41, len(receipts)
print(json.dumps({
    "rendered_sections": 40,
    "source_units_covered": 45,
    "input_receipts": len(receipts),
    "labels": len(keys),
    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
}))
