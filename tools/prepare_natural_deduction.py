"""Prepare the cumulative Gujarati reader through natural deduction.

This adapter launches no TeX process. It extends the sequent-calculus reader
with the complete classical first-order natural-deduction chapter, selects the
frozen source's FOL and natural-deduction profile, and records the translated
chapter driver as a covered source unit.
"""
from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_sequent_calculus.py"))
body = (BUILD / "sequent-calculus-body.tex").read_text(encoding="utf-8")
receipts = json.loads((BUILD / "sequent-calculus-input-hashes.json").read_text(encoding="utf-8"))

names = [
    "rules-and-proofs",
    "propositional-rules",
    "quantifier-rules",
    "derivations",
    "proving-things",
    "proving-things-quant",
    "proof-theoretic-notions",
    "provability-consistency",
    "provability-propositional",
    "provability-quantifiers",
    "soundness",
    "identity",
    "soundness-identity",
]

tokens = {
    "constant": ("અચળ", "અચળો"),
    "derivability": ("નિષ્પન્નક્ષમતા", "નિષ્પન્નક્ષમતાઓ"),
    "derivable": ("નિષ્પન્ન કરી શકાય એવું", "નિષ્પન્ન કરી શકાય એવાં"),
    "derivation": ("નિષ્પત્તિ", "નિષ્પત્તિઓ"),
    "derive": ("નિષ્પન્ન", "નિષ્પન્ન"),
    "discharge": ("નિવૃત્ત", "નિવૃત્ત"),
    "discharged": ("નિવૃત્ત", "નિવૃત્ત"),
    "formula": ("સૂત્ર", "સૂત્રો"),
    "identity": ("તાદાત્મ્ય", "તાદાત્મ્યો"),
    "main operator": ("મુખ્ય કારક", "મુખ્ય કારકો"),
    "nonderivability": ("અનિષ્પન્નક્ષમતા", "અનિષ્પન્નક્ષમતાઓ"),
    "operator": ("કારક", "કારકો"),
    "sentence": ("વાક્ય", "વાક્યો"),
    "structure": ("સંરચના", "સંરચનાઓ"),
    "undischarged": ("અનિવૃત્ત", "અનિવૃત્ત"),
    "valuation": ("સત્યમૂલ્ય-નિયુક્તિ", "સત્યમૂલ્ય-નિયુક્તિઓ"),
    "variable": ("ચલ", "ચલો"),
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


resolver_globals = scope["resolve_tags"].__globals__
active_tags = resolver_globals["active_tags"]
active_tags.discard("PL")
active_tags.discard("prfLK")
active_tags.update({"FOL", "prfND", "prvAll", "prvEx"})
resolve_tags = scope["resolve_tags"]
replace_command = resolver_globals["replace_command"]
tag_enabled = resolver_globals["tag_enabled"]
formula_letters = scope["formula_letters"]


def resolve_tagged_problems(text: str) -> str:
    pattern = re.compile(
        r"\\tagprob(?:\[([^]]+)\])?\{([^}]+)\}([\s\S]*?)\\tagendprob"
    )
    while match := pattern.search(text):
        gate = match[1] or "tagTrue"
        tags = match[2]
        keep = (gate == "tagTrue" or tag_enabled(gate)) and tag_enabled(tags)
        replacement = match[3] if keep else ""
        text = text[:match.start()] + replacement + text[match.end():]
    assert not re.search(r"\\(?:tagprob|tagendprob)(?![A-Za-z])", text)
    return text


def resolve_tagged_enumerations(text: str) -> str:
    pattern = re.compile(
        r"\\begin\{tagenumerate\}\{([^}]+)\}([\s\S]*?)\\end\{tagenumerate\}"
    )
    while match := pattern.search(text):
        replacement = (
            r"\begin{enumerate}" + match[2] + r"\end{enumerate}"
            if tag_enabled(match[1])
            else ""
        )
        text = text[:match.start()] + replacement + text[match.end():]
    assert "tagenumerate" not in text
    return text


def prepare_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8").split(r"\begin{document}", 1)[1].rsplit(r"\end{document}", 1)[0]
    # TeX comments may legally sit between the braced arguments of \iftag;
    # remove them before the structural resolver walks those arguments.
    text = re.sub(r"(?m)(?<!\\)%.*$", "", text)
    text = resolve_tagged_problems(text)
    text = resolve_tagged_enumerations(text)
    text = resolve_tags(text)
    text = expand_tokens(text)
    text = re.sub(r"!([ABCDEFGHKLORST])", lambda match: formula_letters[match[1]], text)
    return text


chapter_root = ROOT / "gu" / "content" / "first-order-logic" / "natural-deduction"
driver = chapter_root / "natural-deduction.tex"
driver_text = prepare_text(driver)
driver_text = replace_command(
    driver_text,
    "olchapter",
    3,
    lambda _part, _chapter, title: r"\part{" + title + "}",
)
driver_text = replace_command(driver_text, "olimport", 1, lambda _name: "")
driver_text = driver_text.replace(r"\OLEndChapterHook", "")
assert r"\olimport" not in driver_text and r"\olchapter" not in driver_text
body += "\n" + driver_text + "\n"

for name in names:
    path = chapter_root / f"{name}.tex"
    body += prepare_text(path) + "\n"
    receipts.append({
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    })

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

(BUILD / "natural-deduction-body.tex").write_text(body, encoding="utf-8", newline="\n")
(BUILD / "natural-deduction-available-labels.tex").write_text(
    "\n".join(
        r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}"
        for key in sorted(keys)
    ) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "natural-deduction-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "natural-deduction-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)

assert len(receipts) == 90, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 83, sections
assert not re.search(
    r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])",
    body,
)
print(json.dumps({
    "rendered_sections": sections,
    "source_units_covered": 94,
    "input_receipts": len(receipts),
    "labels": len(keys),
    "logic_profile": "classical_first_order_natural_deduction",
    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
}))
