"""Prepare the cumulative reader through the complete Computability Theory chapter.

Extends the already checked 224-unit Recursive Functions body; launches no
TeX process. The chapter driver imports exactly its 23 translated sections.
"""

from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_computability.py"))
body = (BUILD / "computability-body.tex").read_text(encoding="utf-8")
receipts = json.loads((BUILD / "computability-input-hashes.json").read_text(encoding="utf-8"))
prepare_text = scope["prepare_text"]
replace_command = scope["replace_command"]
prepare_text.__globals__["tokens"].update({
    "computably enumerable": ("સંગણકીય રીતે પરિગણનીય", "સંગણકીય રીતે પરિગણનીય"),
    "c.e.": ("સંગણકીય રીતે પરિગણનીય", "સંગણકીય રીતે પરિગણનીય"),
})

# The frozen source contains some older two-argument \iftag{TMs}{...}
# commands. The cumulative reader's shared resolver expects an explicit
# empty third argument. Supply it only in the derived rendering stream;
# source and translated files remain byte-identical to their QA receipts.
argument = replace_command.__globals__["argument"]
resolve_tags_base = prepare_text.__globals__["resolve_tags"]


def resolve_legacy_tags(text: str) -> str:
    pattern = re.compile(r"\\iftag(?![A-Za-z])")
    position = 0
    while match := pattern.search(text, position):
        tags, cursor = argument(text, match.end())
        _yes, cursor = argument(text, cursor)
        following = cursor
        while following < len(text) and text[following].isspace():
            following += 1
        if tags.strip() == "TMs" and (following == len(text) or text[following] != "{"):
            text = text[:cursor] + "{}" + text[cursor:]
            cursor += 2
        position = cursor
    return resolve_tags_base(text)


prepare_text.__globals__["resolve_tags"] = resolve_legacy_tags

chapter_root = ROOT / "gu" / "content" / "computability" / "computability-theory"
driver = chapter_root / "computability-theory.tex"
names = [
    "introduction", "coding-computations", "normal-form", "s-m-n",
    "universal-part-function", "no-universal-function", "halting-problem",
    "russells-paradox", "computable-sets", "ce-sets", "equiv-ce-defs",
    "non-comp-set", "ce-closed-cup-cap", "complement-ce", "reducibility",
    "prop-reduce", "complete-ce-sets", "k-1", "total", "rice-theorem",
    "fixed-point-thm", "application-fixed-point",
    "def-functions-self-reference",
]

chapter_text = prepare_text(driver)
assert re.findall(r"\\olimport(?:\[[^]]+\])?\{([^{}]+)\}", chapter_text) == names
chapter_text = replace_command(
    chapter_text, "olchapter", 3,
    lambda _part, _chapter, title: r"\section{" + title + "}",
)
chapter_text = re.sub(r"\\olimport(?:\[[^]]+\])?\{[^{}]+\}", "", chapter_text)
chapter_text = chapter_text.replace(r"\OLEndChapterHook", "")
assert r"\olimport" not in chapter_text and r"\olchapter" not in chapter_text
body += "\n" + chapter_text + "\n"

for name in names:
    path = chapter_root / f"{name}.tex"
    prepared = prepare_text(path)
    identifiers = re.findall(r"\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}", prepared)
    assert len(identifiers) == 1 and identifiers[0][:2] == ("cmp", "thy"), path
    assert len(re.findall(r"\\olsection(?:\[[^]]*\])?\{", prepared)) == 1, path
    prefix = ":".join(identifiers[0])
    prepared = re.sub(r"\\olsection\[[^]]*\]", lambda _m: r"\olsection", prepared, count=1)
    prepared = replace_command(
        prepared, "olsection", 1,
        lambda title: r"\subsection{" + title + r"}\label{" + prefix + ":sec}",
    )
    assert r"\olsection" not in prepared
    body += prepared + "\n"
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

(BUILD / "computability-theory-body.tex").write_text(body, encoding="utf-8", newline="\n")
(BUILD / "computability-theory-available-labels.tex").write_text(
    "\n".join(r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}"
              for key in sorted(keys)) + "\n", encoding="utf-8", newline="\n")
(BUILD / "computability-theory-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n", encoding="utf-8", newline="\n")
(BUILD / "computability-theory-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8", newline="\n")

assert len(receipts) == 244, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 220, sections
assert not re.search(r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])",
                     body.replace(r"\string\iftag", ""))
print(json.dumps({
    "rendered_sections": sections,
    "source_units_covered": 248,
    "input_receipts": len(receipts),
    "labels": len(keys),
    "logic_profile": "computability_theory_after_recursive_functions",
    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
}))
