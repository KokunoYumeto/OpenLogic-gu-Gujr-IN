"""Prepare the 260-unit cumulative reader through Turing-machine computations.

The new part also imports an untranslated undecidability chapter; omit that
import from this derived reader without changing the source driver.
No TeX process is launched here.
"""

from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_computability_theory.py"))
body = (BUILD / "computability-theory-body.tex").read_text(encoding="utf-8")
receipts = json.loads(
    (BUILD / "computability-theory-input-hashes.json").read_text(encoding="utf-8")
)
prepare_text = scope["prepare_text"]
replace_command = scope["replace_command"]

part_root = ROOT / "gu" / "content" / "turing-machines"
chapter_root = part_root / "machines-computations"
part_driver = part_root / "turing-machines.tex"
chapter_driver = chapter_root / "machines-computations.tex"
names = [
    "introduction", "representing-tms", "turing-machines", "configuration",
    "unary-numbers", "halting-states", "disciplined-machines",
    "combining-machines", "variants", "church-turing-thesis",
]

part_text = prepare_text(part_driver)
assert re.findall(r"\\olimport(?:\[[^]]+\])?\{([^{}]+)\}", part_text) == [
    "machines-computations", "undecidability"
]
part_text = replace_command(
    part_text, "olpart", 2, lambda _part, title: r"\part{" + title + "}"
)
part_text = re.sub(r"\\olimport(?:\[[^]]+\])?\{[^{}]+\}", "", part_text)
part_text = part_text.replace(r"\OLEndPartHook", "")
assert r"\olimport" not in part_text and r"\olpart" not in part_text
body += "\n" + part_text + "\n"

chapter_text = prepare_text(chapter_driver)
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
    identifiers = re.findall(
        r"\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}", prepared
    )
    # The frozen source assigns configuration.tex the exceptional cmp:tur:con
    # file ID; preserve it so its existing cross-references keep resolving.
    expected_prefix = ("cmp", "tur") if name == "configuration" else ("tur", "mac")
    assert len(identifiers) == 1 and identifiers[0][:2] == expected_prefix, path
    assert len(re.findall(r"\\olsection(?:\[[^]]*\])?\{", prepared)) == 1, path
    prefix = ":".join(identifiers[0])
    prepared = re.sub(
        r"\\olsection\[[^]]*\]", lambda _match: r"\olsection", prepared,
        count=1,
    )
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

for path, role in ((part_driver, "part_driver_expanded"),
                   (chapter_driver, "chapter_driver_expanded")):
    receipts.append({
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "role": role,
    })

# The frozen intro uses the upstream-style \olpath inside \olasset.  This
# standalone reader's \olasset already prefixes upstream/, so normalize the
# derived stream once; keep the translated source and its receipt unchanged.
assert body.count(r"\olasset{\olpath/assets/diagrams/turing-machine.tikz}") == 1
body = body.replace(
    r"\olasset{\olpath/assets/diagrams/turing-machine.tikz}",
    r"\olasset{assets/diagrams/turing-machine.tikz}", 1,
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

(BUILD / "turing-machines-body.tex").write_text(
    body, encoding="utf-8", newline="\n"
)
(BUILD / "turing-machines-available-labels.tex").write_text(
    "\n".join(r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}"
              for key in sorted(keys)) + "\n", encoding="utf-8", newline="\n"
)
(BUILD / "turing-machines-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n", encoding="utf-8", newline="\n"
)
(BUILD / "turing-machines-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8", newline="\n"
)

assert len(receipts) == 256, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 230, sections
assert not re.search(
    r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])",
    body.replace(r"\string\iftag", ""),
)
print(json.dumps({
    "rendered_sections": sections,
    "source_units_covered": 260,
    "input_receipts": len(receipts),
    "labels": len(keys),
    "logic_profile": "turing_machine_computations_after_computability_theory",
    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
}))
