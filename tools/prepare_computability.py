"""Prepare the 224-unit cumulative Gujarati reader through Recursive Functions.

The part driver also imports the untranslated Computability Theory chapter.
Only the complete translated Recursive Functions chapter enters this reader.
No TeX process is launched here.
"""

from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_lindstrom.py"))
body = (BUILD / "lindstrom-body.tex").read_text(encoding="utf-8")
receipts = json.loads((BUILD / "lindstrom-input-hashes.json").read_text(encoding="utf-8"))
prepare_text = scope["prepare_text"]
replace_command = scope["replace_command"]

part_root = ROOT / "gu" / "content" / "computability"
chapter_root = part_root / "recursive-functions"
part_driver = part_root / "computability.tex"
chapter_driver = chapter_root / "recursive-functions.tex"
expected_names = [
    "introduction", "primitive-recursion", "composition", "pr-functions",
    "notation-pr-functions", "pr-functions-computable", "examples",
    "pr-relations", "bounded-minimization", "primes", "sequences", "trees",
    "other-recursions", "non-pr-functions", "partial-functions",
    "normal-form", "halting-problem", "general-recursive-functions",
]

part_text = prepare_text(part_driver)
assert re.findall(r"\\olimport(?:\[[^]]+\])?\{([^{}]+)\}", part_text) == [
    "recursive-functions", "computability-theory"
]
part_text = replace_command(part_text, "olpart", 2, lambda _part, title: r"\part{" + title + "}")
part_text = re.sub(r"\\olimport(?:\[[^]]+\])?\{[^{}]+\}", "", part_text)
part_text = part_text.replace(r"\OLEndPartHook", "")
assert r"\olimport" not in part_text and r"\olpart" not in part_text
body += "\n" + part_text + "\n"

chapter_text = prepare_text(chapter_driver)
assert re.findall(r"\\olimport(?:\[[^]]+\])?\{([^{}]+)\}", chapter_text) == expected_names
chapter_text = replace_command(
    chapter_text, "olchapter", 3,
    lambda _part, _chapter, title: r"\section{" + title + "}",
)
chapter_text = re.sub(r"\\olimport(?:\[[^]]+\])?\{[^{}]+\}", "", chapter_text)
chapter_text = chapter_text.replace(r"\OLEndChapterHook", "")
assert r"\olimport" not in chapter_text and r"\olchapter" not in chapter_text
body += "\n" + chapter_text + "\n"

for name in expected_names:
    path = chapter_root / f"{name}.tex"
    prepared = prepare_text(path)
    identifiers = re.findall(r"\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}", prepared)
    assert len(identifiers) == 1 and identifiers[0][:2] == ("cmp", "rec"), path
    assert len(re.findall(r"\\olsection\{", prepared)) == 1, path
    prefix = ":".join(identifiers[0])
    prepared = replace_command(
        prepared, "olsection", 1,
        lambda title: r"\subsection{" + title + r"}\label{" + prefix + ":sec}",
    )
    assert r"\olsection" not in prepared
    body += prepared + "\n"
    receipts.append({"path": path.relative_to(ROOT).as_posix(),
                     "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})

for path, role in ((part_driver, "part_driver_expanded"),
                   (chapter_driver, "chapter_driver_expanded")):
    receipts.append({"path": path.relative_to(ROOT).as_posix(),
                     "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                     "role": role})

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

(BUILD / "computability-body.tex").write_text(body, encoding="utf-8", newline="\n")
(BUILD / "computability-available-labels.tex").write_text(
    "\n".join(r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}"
              for key in sorted(keys)) + "\n", encoding="utf-8", newline="\n")
(BUILD / "computability-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n", encoding="utf-8", newline="\n")
(BUILD / "computability-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8", newline="\n")

assert len(receipts) == 220, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 197, sections
assert not re.search(r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])",
                     body.replace(r"\string\iftag", ""))
print(json.dumps({"rendered_sections": sections, "source_units_covered": 224,
                  "input_receipts": len(receipts), "labels": len(keys),
                  "logic_profile": "recursive_functions_after_lindstrom",
                  "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest()}))
