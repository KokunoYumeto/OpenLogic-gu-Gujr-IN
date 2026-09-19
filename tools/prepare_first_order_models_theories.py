"""Prepare the cumulative Gujarati reader through models and theories.

This adapter launches no TeX process. It extends the accepted cumulative
first-order semantics body with the complete models-and-theories chapter and
resolves the frozen source's classical first-order/default-connective profile.
"""

from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_first_order_semantics.py"))
body = (BUILD / "first-order-semantics-body.tex").read_text(encoding="utf-8")
receipts = json.loads(
    (BUILD / "first-order-semantics-input-hashes.json").read_text(encoding="utf-8")
)

tokens = scope["prepare_text"].__globals__["tokens"]
tokens.update({"injective": ("એક-એક", "એક-એક")})

prepare_text = scope["prepare_text"]
replace_command = scope["replace_command"]
chapter_root = ROOT / "gu" / "content" / "first-order-logic" / "models-theories"
chapter_driver = chapter_root / "models-theories.tex"
names = [
    "introduction",
    "expressing-props-of-structures",
    "theories",
    "expressing-relations",
    "set-theory",
    "size-of-structures",
]

chapter_driver_text = prepare_text(chapter_driver)
chapter_driver_text = replace_command(
    chapter_driver_text,
    "olchapter",
    3,
    lambda _part, _chapter, title: r"\part{" + title + "}",
)
chapter_driver_text = replace_command(
    chapter_driver_text, "olimport", 1, lambda _name: ""
)
chapter_driver_text = chapter_driver_text.replace(r"\OLEndChapterHook", "")
assert r"\olimport" not in chapter_driver_text
assert r"\olchapter" not in chapter_driver_text
body += "\n" + chapter_driver_text + "\n"

for name in names:
    path = chapter_root / f"{name}.tex"
    prepared = prepare_text(path)
    body += prepared + "\n"
    receipts.append(
        {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
    )

receipts.append(
    {
        "path": chapter_driver.relative_to(ROOT).as_posix(),
        "sha256": hashlib.sha256(chapter_driver.read_bytes()).hexdigest(),
        "role": "chapter_driver_expanded",
    }
)

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

(BUILD / "first-order-models-theories-body.tex").write_text(
    body, encoding="utf-8", newline="\n"
)
(BUILD / "first-order-models-theories-available-labels.tex").write_text(
    "\n".join(
        r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}"
        for key in sorted(keys)
    )
    + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "first-order-models-theories-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n", encoding="utf-8", newline="\n"
)
(BUILD / "first-order-models-theories-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)

assert len(receipts) == 166, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 151, sections
assert not re.search(
    r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])",
    body.replace(r"\string\iftag", ""),
)
print(
    json.dumps(
        {
            "rendered_sections": sections,
            "source_units_covered": 170,
            "input_receipts": len(receipts),
            "labels": len(keys),
            "logic_profile": "classical_first_order_models_theories_after_semantics",
            "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        }
    )
)
