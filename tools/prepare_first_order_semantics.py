"""Prepare the cumulative Gujarati reader through first-order semantics.

This adapter launches no TeX process. It extends the accepted cumulative
first-order syntax body with the complete semantics chapter and resolves the
frozen source's classical first-order/default-connective profile.
"""
from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_first_order_syntax.py"))
body = (BUILD / "first-order-syntax-body.tex").read_text(encoding="utf-8")
receipts = json.loads((BUILD / "first-order-syntax-input-hashes.json").read_text(encoding="utf-8"))

prepare_text = scope["prepare_text"]
replace_command = scope["replace_command"]
chapter_root = ROOT / "gu" / "content" / "first-order-logic" / "syntax-and-semantics"
chapter_driver = chapter_root / "semantics.tex"
names = [
    "intro-semantics",
    "structures",
    "covered-structures",
    "satisfaction",
    "assignments",
    "extensionality",
    "semantic-notions",
]

chapter_driver_text = prepare_text(chapter_driver)
chapter_driver_text = replace_command(
    chapter_driver_text,
    "olchapter",
    3,
    lambda _part, _chapter, title: r"\part{" + title + "}",
)
chapter_driver_text = replace_command(chapter_driver_text, "olimport", 1, lambda _name: "")
chapter_driver_text = chapter_driver_text.replace(r"\OLEndChapterHook", "")
assert r"\olimport" not in chapter_driver_text
assert r"\olchapter" not in chapter_driver_text
body += "\n" + chapter_driver_text + "\n"

for name in names:
    path = chapter_root / f"{name}.tex"
    prepared = prepare_text(path)
    if name == "satisfaction":
        # The frozen default treats both quantifiers as primitive, so the
        # alternative defEx/defAll teaching branches are intentionally absent
        # from this reader profile. Their repairs remain in the complete
        # translated source. Repeat only the three omitted disclosure notes at
        # the end of the rendered section so every keyed repair is public.
        wanted = ["OLSEM-004", "OLSEM-005", "OLSEM-006"]
        captured = {}

        def capture_correction(identifier: str, note: str) -> str:
            if identifier in wanted:
                captured[identifier] = (
                    r"\sourcecorrection{" + identifier + "}{" + note + "}"
                )
            return ""

        replace_command(
            path.read_text(encoding="utf-8"),
            "sourcecorrection",
            2,
            capture_correction,
        )
        assert list(captured) == wanted, captured
        assert all(identifier not in prepared for identifier in wanted)
        prepared += (
            "\n\\subsection*{વૈકલ્પિક પરિમાણક-સમજૂતીના સ્રોત-સુધારા}\n"
            "આ આવૃત્તિ પરિમાણકોને આદિમ માને છે; તેથી પરિમાણકોને અન્ય "
            "સંયોજકો વડે સમજાવતી નીચે સુધારેલી ત્રણ વૈકલ્પિક ચર્ચાઓ મુખ્ય "
            "પાઠમાં દેખાતી નથી. સંપૂર્ણ અનુવાદિત સ્રોતમાં તે ચર્ચાઓ અને "
            "સુધારા છે; પારદર્શિતા માટે સુધારાની નોંધો અહીં પણ આપેલી છે.\n"
            + "\n".join(captured[identifier] for identifier in wanted)
            + "\n"
        )
    body += prepared + "\n"
    receipts.append({
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    })

receipts.append({
    "path": chapter_driver.relative_to(ROOT).as_posix(),
    "sha256": hashlib.sha256(chapter_driver.read_bytes()).hexdigest(),
    "role": "chapter_driver_expanded",
})

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

(BUILD / "first-order-semantics-body.tex").write_text(body, encoding="utf-8", newline="\n")
(BUILD / "first-order-semantics-available-labels.tex").write_text(
    "\n".join(r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}" for key in sorted(keys)) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "first-order-semantics-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n", encoding="utf-8", newline="\n"
)
(BUILD / "first-order-semantics-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
)

assert len(receipts) == 159, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 145, sections
assert not re.search(
    r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])",
    body.replace(r"\string\iftag", ""),
)
print(json.dumps({
    "rendered_sections": sections,
    "source_units_covered": 163,
    "input_receipts": len(receipts),
    "labels": len(keys),
    "logic_profile": "classical_first_order_semantics_after_syntax",
    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
}))
