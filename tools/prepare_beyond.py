"""Prepare the cumulative Gujarati reader through Beyond First-order Logic.

This adapter launches no TeX process. It extends the accepted cumulative
models-and-theories body with the complete Beyond First-order Logic chapter
under the frozen source's classical first-order/default-connective profile.
"""

from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_first_order_models_theories.py"))
body = (BUILD / "first-order-models-theories-body.tex").read_text(encoding="utf-8")
receipts = json.loads(
    (BUILD / "first-order-models-theories-input-hashes.json").read_text(encoding="utf-8")
)

prepare_text = scope["prepare_text"]
replace_command = scope["replace_command"]
tokens = prepare_text.__globals__["tokens"]
tokens.update({
    "surjective": ("વ્યાપ્ત", "વ્યાપ્ત"),
    "bijection": ("એક-એક વ્યાપ્ત વિધેય", "એક-એક વ્યાપ્ત વિધેયો"),
})
chapter_root = ROOT / "gu" / "content" / "first-order-logic" / "beyond"
chapter_driver = chapter_root / "beyond.tex"
names = [
    "introduction",
    "many-sorted-logic",
    "second-order-logic",
    "higher-order-logic",
    "intuitionistic-logic",
    "modal-logics",
    "other-logics",
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

(BUILD / "beyond-body.tex").write_text(body, encoding="utf-8", newline="\n")
(BUILD / "beyond-available-labels.tex").write_text(
    "\n".join(
        r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}"
        for key in sorted(keys)
    )
    + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "beyond-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n", encoding="utf-8", newline="\n"
)
(BUILD / "beyond-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)

assert len(receipts) == 174, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 158, sections
assert not re.search(
    r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])",
    body.replace(r"\string\iftag", ""),
)
print(json.dumps({
    "rendered_sections": sections,
    "source_units_covered": 178,
    "input_receipts": len(receipts),
    "labels": len(keys),
    "logic_profile": "classical_first_order_beyond_after_models_theories",
    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
}))
