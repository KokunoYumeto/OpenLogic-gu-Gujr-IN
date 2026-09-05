"""Prepare the cumulative Gujarati reader through the proof-systems overview.

This adapter launches no TeX process. It adds the five rendered overview
sections and records the chapter driver as a covered source unit. The frozen
source's propositional profile is selected because these overview sections are
shared by first-order and propositional logic.
"""
from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_propositional.py"))
body = (BUILD / "propositional-body.tex").read_text(encoding="utf-8")
receipts = json.loads((BUILD / "propositional-input-hashes.json").read_text(encoding="utf-8"))

names = [
    "introduction",
    "sequent-calculus",
    "natural-deduction",
    "tableaux",
    "axiomatic-deduction",
]

tokens = {
    "derivation": ("નિષ્પત્તિ", "નિષ્પત્તિઓ"),
    "sentence": ("વાક્ય", "વાક્યો"),
    "formula": ("સૂત્ર", "સૂત્રો"),
    "derivable": ("નિષ્પન્ન કરી શકાય એવું", "નિષ્પન્ન કરી શકાય એવાં"),
    "derivability": ("નિષ્પન્નક્ષમતા", "નિષ્પન્નક્ષમતાઓ"),
    "derive": ("નિષ્પન્ન", "નિષ્પન્ન"),
    "discharge": ("નિવૃત્ત", "નિવૃત્ત"),
    "discharged": ("નિવૃત્ત", "નિવૃત્ત"),
    "undischarged": ("અનિવૃત્ત", "અનિવૃત્ત"),
    "signed formula": ("ચિહ્નિત સૂત્ર", "ચિહ્નિત સૂત્રો"),
    "tableau": ("ટેબ્લો", "ટેબ્લો"),
    "structure": ("સંરચના", "સંરચનાઓ"),
    "element": ("ઘટક", "ઘટકો"),
}


def expand_tokens(text: str) -> str:
    def replacement(match: re.Match[str]) -> str:
        key = " ".join(match[1].split())
        suffix = match[2]
        assert key in tokens, key
        assert suffix in {"", "s", "d"}, (key, suffix)
        if suffix == "d":
            assert key == "derive"
            return tokens[key][0]
        return tokens[key][suffix == "s"]

    text = re.sub(r"!!\^?a?\{([^}]+)\}([A-Za-z]*)", replacement, text)
    assert "!!" not in text
    return text


scope["active_tags"].add("PL")
resolve_tags = scope["resolve_tags"]
formula_letters = scope["formula_letters"]

body += "\n\\part{નિષ્પત્તિ તંત્રો}\n"
chapter_root = ROOT / "gu" / "content" / "first-order-logic" / "proof-systems"
for name in names:
    path = chapter_root / f"{name}.tex"
    text = path.read_text(encoding="utf-8").split(r"\begin{document}", 1)[1].rsplit(r"\end{document}", 1)[0]
    text = resolve_tags(text)
    text = expand_tokens(text)
    text = re.sub(r"!([ABCDEFGHKLORST])", lambda match: formula_letters[match[1]], text)
    body += text + "\n"
    receipts.append({
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    })

driver = chapter_root / "proof-systems.tex"
receipts.append({
    "path": driver.relative_to(ROOT).as_posix(),
    "sha256": hashlib.sha256(driver.read_bytes()).hexdigest(),
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

(BUILD / "proof-systems-body.tex").write_text(body, encoding="utf-8", newline="\n")
(BUILD / "proof-systems-available-labels.tex").write_text(
    "\n".join(
        r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}"
        for key in sorted(keys)
    ) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "proof-systems-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "proof-systems-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)

assert len(receipts) == 61, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 56, sections
assert not re.search(r"!!|\\(?:iftag|tagitem|startycommalist|ycomma)(?![A-Za-z])", body)
print(json.dumps({
    "rendered_sections": sections,
    "source_units_covered": 65,
    "input_receipts": len(receipts),
    "labels": len(keys),
    "logic_profile": "propositional_shared_overview",
    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
}))
