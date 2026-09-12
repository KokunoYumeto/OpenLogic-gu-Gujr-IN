"""Prepare the cumulative Gujarati reader through the FOL introduction.

This adapter launches no TeX process. It extends the axiomatic-deduction
reader through completeness with the first-order part driver and complete
introduction chapter. It resolves the frozen source's FOL/default-connective
profile and records both translated drivers as covered source units.
"""
from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_completeness.py"))
body = (BUILD / "completeness-body.tex").read_text(encoding="utf-8")
receipts = json.loads(
    (BUILD / "completeness-input-hashes.json").read_text(encoding="utf-8")
)

names = [
    "first-order-logic",
    "syntax",
    "formulas",
    "satisfaction",
    "sentences",
    "semantic-notions",
    "substitution",
    "models-theories",
    "soundness-completeness",
]

tokens = {
    "complete": ("પૂર્ણ", "પૂર્ણ"),
    "constant": ("અચળ", "અચળો"),
    "denumerable": ("ગણનીય", "ગણનીય"),
    "derivability": ("નિષ્પન્નક્ષમતા", "નિષ્પન્નક્ષમતાઓ"),
    "derivation": ("નિષ્પત્તિ", "નિષ્પત્તિઓ"),
    "derive": ("નિષ્પન્ન", "નિષ્પન્ન"),
    "domain": ("વ્યાપકક્ષેત્ર", "વ્યાપકક્ષેત્રો"),
    "element": ("ઘટક", "ઘટકો"),
    "enumerable": ("ગણનીય", "ગણનીય"),
    "formula": ("સૂત્ર", "સૂત્રો"),
    "function": ("વિધેય", "વિધેયો"),
    "identity": ("તાદાત્મ્ય", "તાદાત્મ્યો"),
    "language": ("ભાષા", "ભાષાઓ"),
    "nonenumerable": ("અગણનીય", "અગણનીય"),
    "predicate": ("વિધેય", "વિધેયો"),
    "propositional variable": ("વિધાનચલ", "વિધાનચલો"),
    "sentence": ("વાક્ય", "વાક્યો"),
    "structure": ("સંરચના", "સંરચનાઓ"),
    "valuation": ("સત્યમૂલ્ય-નિયુક્તિ", "સત્યમૂલ્ય-નિયુક્તિઓ"),
    "value": ("મૂલ્ય", "મૂલ્યો"),
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
active_tags.discard("prfND")
active_tags.discard("prfTab")
active_tags.update({"FOL", "prfAx", "prvAll", "prvEx"})
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


def resolve_tagged_references(text: str) -> str:
    """Choose the active proof-system reference from ``\tagrefs`` lists.

    The completeness chapter cites the same fact in several proof systems.
    Its frozen source uses ``\tagrefs{tag/label,...}``, but the standalone
    Gujarati preamble does not load the selective-reference helper.  The
    cumulative edition selects the axiomatic-deduction branch explicitly and
    emits the ordinary label reference that the shared reader can resolve.
    """
    def select(value: str) -> str:
        selected = None
        for item in value.split(","):
            item = item.strip()
            if "/" not in item:
                continue
            tag, label = item.split("/", 1)
            if tag.strip().lower() == "prfax":
                selected = label.strip()
                if selected.startswith("{") and selected.endswith("}"):
                    selected = selected[1:-1]
                break
        if selected is None:
            raise AssertionError(value)
        return r"\ref{" + selected + "}"
    text = replace_command(text, "tagrefs", 1, select)
    assert r"\tagrefs" not in text
    return text


def resolve_external_references(text: str) -> str:
    """Link references whose source sections are outside this checkpoint."""
    replacements = {
        r"\olref[mth][ind][idf]{sec}": (
            r"\href{https://github.com/OpenLogicProject/OpenLogic/blob/"
            r"9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/methods/"
            r"induction/inductive-definitions.tex}"
            r"{મૂળ ગ્રંથનો અનુમાનાત્મક વ્યાખ્યાઓ અંગેનો વિભાગ}"
        ),
        r"\olref[mth][ind][sti]{sec}": (
            r"\href{https://github.com/OpenLogicProject/OpenLogic/blob/"
            r"9620cc73f9c8e0ad003c514a5d3748f29611c4c0/content/methods/"
            r"induction/structural-induction.tex}"
            r"{મૂળ ગ્રંથનો રચના પરના અનુમાન અંગેનો વિભાગ}"
        ),
    }
    for reference, replacement in replacements.items():
        text = text.replace(reference, replacement)
    return text


def prepare_text(path: Path) -> str:
    text = path.read_text(encoding="utf-8").split(
        r"\begin{document}", 1
    )[1].rsplit(r"\end{document}", 1)[0]
    # TeX comments may sit between braced conditional arguments.
    text = re.sub(r"(?m)(?<!\\)%.*$", "", text)
    # Correction disclosures name the literal source command; protect those
    # specimens while executable conditionals are resolved.
    text = text.replace(r"\string\iftag", "GU-LITERAL-IFTAG")
    text = resolve_tagged_problems(text)
    text = resolve_tagged_enumerations(text)
    text = resolve_tags(text)
    text = resolve_tagged_references(text)
    text = resolve_external_references(text)
    text = text.replace("GU-LITERAL-IFTAG", r"\string\iftag")
    text = expand_tokens(text)
    text = re.sub(
        r"!([ABCDEFGHKLORST])", lambda match: formula_letters[match[1]], text
    )
    return text


part_root = ROOT / "gu" / "content" / "first-order-logic"
chapter_root = part_root / "introduction"
chapter_driver = chapter_root / "introduction.tex"
part_driver = part_root / "first-order-logic.tex"

# The chapter title provides the cumulative reader's new part heading. The
# broader part driver's title is subsumed by it, while its editorial note is
# retained immediately below the heading.
chapter_driver_text = prepare_text(chapter_driver)
chapter_driver_text = replace_command(
    chapter_driver_text,
    "olchapter",
    3,
    lambda _part, _chapter, title: r"\part{" + title + "}",
)
chapter_driver_text = replace_command(chapter_driver_text, "olimport", 1, lambda _name: "")
chapter_driver_text = chapter_driver_text.replace(r"\OLEndChapterHook", "")
assert r"\olimport" not in chapter_driver_text and r"\olchapter" not in chapter_driver_text

part_driver_text = prepare_text(part_driver)
part_driver_text = replace_command(part_driver_text, "olpart", 2, lambda _part, _title: "")
part_driver_text = re.sub(r"\\olimport(?:\[[^]]+\])?\{[^{}]+\}", "", part_driver_text)
part_driver_text = part_driver_text.replace(r"\OLEndPartHook", "")
assert r"\olimport" not in part_driver_text and r"\olpart" not in part_driver_text
body += "\n" + chapter_driver_text + "\n" + part_driver_text + "\n"

for name in names:
    path = chapter_root / f"{name}.tex"
    try:
        prepared = prepare_text(path)
    except Exception:
        print(json.dumps({"prepare_failed": path.relative_to(ROOT).as_posix()}))
        raise
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
receipts.append({
    "path": part_driver.relative_to(ROOT).as_posix(),
    "sha256": hashlib.sha256(part_driver.read_bytes()).hexdigest(),
    "role": "part_driver_editorial_expanded",
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

(BUILD / "first-order-introduction-body.tex").write_text(
    body, encoding="utf-8", newline="\n"
)
(BUILD / "first-order-introduction-available-labels.tex").write_text(
    "\n".join(
        r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}"
        for key in sorted(keys)
    ) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "first-order-introduction-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "first-order-introduction-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)

assert len(receipts) == 141, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 129, sections
assert not re.search(
    r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])",
    body.replace(r"\string\iftag", ""),
)
print(json.dumps({
    "rendered_sections": sections,
    "source_units_covered": 145,
    "input_receipts": len(receipts),
    "labels": len(keys),
    "logic_profile": "classical_first_order_introduction_after_completeness",
    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
}))
