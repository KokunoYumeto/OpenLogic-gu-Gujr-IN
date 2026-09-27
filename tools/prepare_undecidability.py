"""Prepare the 270-unit cumulative reader through Undecidability.

This expands the translated chapter into a derived body; no TeX process runs.
"""

from hashlib import sha256
from pathlib import Path
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools/prepare_turing_machines.py"))
body = (BUILD / "turing-machines-body.tex").read_text(encoding="utf-8")
receipts = json.loads((BUILD / "turing-machines-input-hashes.json").read_text(encoding="utf-8"))
prepare_text = scope["prepare_text"]
replace_command = scope["replace_command"]

parity = json.loads((ROOT / "provenance/DRAFT_PARITY_026.json").read_text(encoding="utf-8"))
assert len(parity["reports"]) == 10 and "parity_passed" in parity["status"]
chapter_root = ROOT / "gu/content/turing-machines/undecidability"
driver = chapter_root / "undecidability.tex"
names = [
    "introduction", "enumerating-tms", "universal-tm", "halting-problem",
    "decision-problem", "representing-tms", "verification",
    "unsolvability-decision-problem", "trakhtenbrot",
]
expected = ["undecidability", *names]
assert [Path(row["source_path"]).stem for row in parity["reports"]] == expected
for row in parity["reports"]:
    path = chapter_root / Path(row["source_path"]).name
    assert path.is_file() and sha256(path.read_bytes()).hexdigest() == row["draft_sha256"]

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
    assert len(identifiers) == 1 and identifiers[0][:2] == ("tur", "und"), path
    assert len(re.findall(r"\\olsection(?:\[[^]]*\])?\{", prepared)) == 1, path
    prefix = ":".join(identifiers[0])
    prepared = re.sub(r"\\olsection\[[^]]*\]", lambda _m: r"\olsection", prepared, count=1)
    prepared = replace_command(
        prepared, "olsection", 1,
        lambda title: r"\subsection{" + title + r"}\label{" + prefix + ":sec}",
    )
    assert r"\olsection" not in prepared
    body += prepared + "\n"
    receipts.append({"path": path.relative_to(ROOT).as_posix(), "sha256": sha256(path.read_bytes()).hexdigest()})

receipts.append({
    "path": driver.relative_to(ROOT).as_posix(),
    "sha256": sha256(driver.read_bytes()).hexdigest(),
    "role": "chapter_driver_expanded",
})
assert len(receipts) == 266

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

(BUILD / "undecidability-body.tex").write_text(body, encoding="utf-8", newline="\n")
(BUILD / "undecidability-available-labels.tex").write_text(
    "\n".join(r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}" for key in sorted(keys)) + "\n",
    encoding="utf-8", newline="\n",
)
(BUILD / "undecidability-available-labels.json").write_text(json.dumps(sorted(keys), indent=2) + "\n", encoding="utf-8", newline="\n")
(BUILD / "undecidability-input-hashes.json").write_text(json.dumps(receipts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 239
assert not re.search(r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])", body.replace(r"\string\iftag", ""))
print(json.dumps({"rendered_sections": sections, "source_units_covered": 270,
                  "input_receipts": len(receipts), "labels": len(keys),
                  "sha256": sha256(body.encode("utf-8")).hexdigest()}))
