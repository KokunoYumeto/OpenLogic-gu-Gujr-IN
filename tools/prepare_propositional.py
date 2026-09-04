"""Prepare the cumulative reader through propositional syntax and semantics.

This adapter launches no TeX process.  It expands Open Logic text tokens and
resolves the connective switches with the frozen source revision's default
profile: both truth constants and all five connectives are primitive, while
the alternative defined-connective clauses remain in the aligned source.
"""
from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
runpy.run_path(str(ROOT / "tools" / "prepare_infinite.py"))
body = (BUILD / "infinite-body.tex").read_text(encoding="utf-8")
receipts = json.loads((BUILD / "infinite-input-hashes.json").read_text(encoding="utf-8"))

names = [
    "introduction",
    "formulas",
    "preliminaries",
    "formation-sequences",
    "valuations-sat",
    "semantic-notions",
]

tokens = {
    "biconditional": ("દ્વિમુખી પ્રેરણ", "દ્વિમુખી પ્રેરણો"),
    "conditional": ("પ્રેરણ", "પ્રેરણો"),
    "denumerable": ("ગણનીય", "ગણનીય"),
    "falsity": ("અસત્યતા", "અસત્યતાઓ"),
    "formula": ("સૂત્ર", "સૂત્રો"),
    "operator": ("કારક", "કારકો"),
    "propositional variable": ("વિધાનચલ", "વિધાનચલો"),
    "structure": ("સંરચના", "સંરચનાઓ"),
    "truth": ("સત્ય", "સત્યો"),
    "valuation": ("સત્યમૂલ્ય-નિયુક્તિ", "સત્યમૂલ્ય-નિયુક્તિઓ"),
}

# Defaults in upstream/open-logic-config.sty at the frozen revision.
active_tags = {
    "limitClause",
    "prvAnd",
    "prvFalse",
    "prvIf",
    "prvIff",
    "prvNot",
    "prvOr",
    "prvTrue",
}


def argument(text: str, index: int) -> tuple[str, int]:
    while index < len(text) and text[index].isspace():
        index += 1
    assert index < len(text) and text[index] == "{", (text[index:index + 40], index)
    depth = 1
    cursor = index + 1
    while depth:
        assert cursor < len(text), text[index:index + 120]
        slash_count = 0
        back = cursor - 1
        while back >= 0 and text[back] == "\\":
            slash_count += 1
            back -= 1
        escaped = slash_count % 2 == 1
        if text[cursor] == "{" and not escaped:
            depth += 1
        elif text[cursor] == "}" and not escaped:
            depth -= 1
        cursor += 1
    return text[index + 1:cursor - 1], cursor


def replace_command(text: str, name: str, count: int, callback) -> str:
    pattern = re.compile(r"\\" + name + r"(?![A-Za-z])")
    position = 0
    while match := pattern.search(text, position):
        values = []
        cursor = match.end()
        for _ in range(count):
            value, cursor = argument(text, cursor)
            values.append(value)
        replacement = callback(*values)
        text = text[:match.start()] + replacement + text[cursor:]
        position = match.start() + len(replacement)
    return text


def tag_enabled(tag_list: str) -> bool:
    return any(tag.strip() in active_tags for tag in tag_list.split(","))


def resolve_tagblocks(text: str) -> str:
    pattern = re.compile(r"\\begin\{tagblock\}\{([^}]*)\}([\s\S]*?)\\end\{tagblock\}")
    while match := pattern.search(text):
        replacement = match[2] if tag_enabled(match[1]) else ""
        text = text[:match.start()] + replacement + text[match.end():]
    return text


def resolve_tags(text: str) -> str:
    text = resolve_tagblocks(text)
    # Innermost commands are naturally resolved first because argument()
    # returns complete balanced arguments and the loop revisits replacements.
    previous = None
    while previous != text:
        previous = text
        text = replace_command(text, "iftag", 3, lambda tags, yes, no: yes if tag_enabled(tags) else no)
        text = replace_command(
            text,
            "tagitem",
            3,
            lambda tags, yes, no: (r"\item " + yes) if tag_enabled(tags) and yes.strip()
            else ((r"\item " + no) if (not tag_enabled(tags) and no.strip()) else ""),
        )
    # The only tagenumerate in this chapter is inside the inactive block, but
    # reject an unexpected survivor rather than silently changing list shape.
    assert r"\begin{tagenumerate}" not in text and r"\end{tagenumerate}" not in text
    comma_lists = text.count(r"\startycommalist")
    assert comma_lists in {0, 1}, comma_lists
    if comma_lists:
        text = text.replace(r"\startycommalist", "", 1)
        assert r"\ycomma" in text
        text = text.replace(r"\ycomma", "", 1)
        text = text.replace(r"\ycomma", ", ")
    assert not re.search(r"\\(?:iftag|tagitem|startycommalist|ycomma)(?![A-Za-z])", text)
    return text


def expand_tokens(text: str) -> str:
    def replacement(match: re.Match[str]) -> str:
        key = " ".join(match[1].split())
        assert key in tokens, key
        return tokens[key][bool(match[2])]

    text = re.sub(r"!!\^?a?\{([^}]+)\}(s?)", replacement, text)
    assert "!!" not in text
    return text


# Open Logic's default configuration renders !A, !B, ... as Greek formula
# metavariables.  Converting the source marker here also makes Pandoc's MathML
# path deterministic without relying on an active math character.
formula_letters = {
    "A": r"\varphi",
    "B": r"\psi",
    "C": r"\chi",
    "D": r"\theta",
    "E": r"\alpha",
    "F": r"\beta",
    "G": r"\gamma",
    "H": r"\delta",
    "K": r"\xi",
    "L": r"\zeta",
    "O": r"\omega",
    "R": r"\rho",
    "S": r"\sigma",
    "T": r"\tau",
}


body += "\n\\part{વિધાનાત્મક તર્કશાસ્ત્ર}\n"
logic_root = ROOT / "gu" / "content" / "propositional-logic"
section_root = logic_root / "syntax-and-semantics"
for name in names:
    path = section_root / f"{name}.tex"
    text = path.read_text(encoding="utf-8").split(r"\begin{document}", 1)[1].rsplit(r"\end{document}", 1)[0]
    text = expand_tokens(text)
    text = resolve_tags(text)
    text = re.sub(r"!([ABCDEFGHKLORST])", lambda match: formula_letters[match[1]], text)
    body += text + "\n"
    receipts.append({"path": path.relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})

for driver, role in (
    (logic_root / "propositional-logic.tex", "part_driver_expanded"),
    (section_root / "syntax-and-semantics.tex", "chapter_driver_expanded"),
):
    receipts.append({
        "path": driver.relative_to(ROOT).as_posix(),
        "sha256": hashlib.sha256(driver.read_bytes()).hexdigest(),
        "role": role,
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

(BUILD / "propositional-body.tex").write_text(body, encoding="utf-8", newline="\n")
(BUILD / "propositional-available-labels.tex").write_text(
    "\n".join(r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}" for key in sorted(keys)) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "propositional-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n", encoding="utf-8", newline="\n"
)
(BUILD / "propositional-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
)

assert len(receipts) == 55, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 51, sections
assert not re.search(r"!!|\\(?:iftag|tagitem|startycommalist|ycomma)(?![A-Za-z])", body)
print(json.dumps({
    "rendered_sections": sections,
    "source_units_covered": 59,
    "input_receipts": len(receipts),
    "labels": len(keys),
    "connective_profile": "upstream_default_all_primitives",
    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
}))
