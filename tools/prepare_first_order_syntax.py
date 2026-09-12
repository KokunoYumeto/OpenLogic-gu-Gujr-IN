"""Prepare the cumulative Gujarati reader through first-order syntax.

This adapter launches no TeX process. It extends the accepted cumulative
first-order introduction body with the complete syntax chapter and resolves
the frozen source's classical first-order/default-connective profile.
"""
from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_first_order_introduction.py"))
body = (BUILD / "first-order-introduction-body.tex").read_text(encoding="utf-8")
receipts = json.loads(
    (BUILD / "first-order-introduction-input-hashes.json").read_text(encoding="utf-8")
)

tokens = scope["prepare_text"].__globals__["tokens"]
tokens.update({
    "biconditional": ("દ્વિમુખી પ્રેરણ", "દ્વિમુખી પ્રેરણો"),
    "conditional": ("પ્રેરણ", "પ્રેરણો"),
    "falsity": ("અસત્યતા", "અસત્યતાઓ"),
    "free for": ("મુક્તપણે પ્રતિસ્થાપનીય", "મુક્તપણે પ્રતિસ્થાપનીય"),
    "main operator": ("મુખ્ય કારક", "મુખ્ય કારકો"),
    "operator": ("કારક", "કારકો"),
    "subformula": ("ઉપસૂત્ર", "ઉપસૂત્રો"),
    "truth": ("સત્ય", "સત્યો"),
})

prepare_text = scope["prepare_text"]
replace_command = scope["replace_command"]
chapter_root = ROOT / "gu" / "content" / "first-order-logic" / "syntax-and-semantics"
chapter_driver = chapter_root / "syntax.tex"
names = [
    "intro-syntax",
    "first-order-languages",
    "terms-formulas",
    "unique-readability",
    "main-operator",
    "subformulas",
    "formation-sequences",
    "free-vars-sentences",
    "substitution",
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

(BUILD / "first-order-syntax-body.tex").write_text(
    body, encoding="utf-8", newline="\n"
)
(BUILD / "first-order-syntax-available-labels.tex").write_text(
    "\n".join(
        r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}"
        for key in sorted(keys)
    ) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "first-order-syntax-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "first-order-syntax-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)

assert len(receipts) == 151, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 138, sections
assert not re.search(
    r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])",
    body.replace(r"\string\iftag", ""),
)
print(json.dumps({
    "rendered_sections": sections,
    "source_units_covered": 155,
    "input_receipts": len(receipts),
    "labels": len(keys),
    "logic_profile": "classical_first_order_syntax_after_introduction",
    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
}))
