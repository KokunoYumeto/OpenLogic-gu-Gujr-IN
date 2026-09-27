"""Assemble a cumulative 289-unit reader including the complete SOL part.

The 48 drafted OLP-0274–0321 units are not yet integrated; this derived
reader states its non-contiguous coverage explicitly. No TeX process runs.
"""

from hashlib import sha256
from pathlib import Path
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools/prepare_undecidability.py"))
body = (BUILD / "undecidability-body.tex").read_text(encoding="utf-8")
receipts = json.loads((BUILD / "undecidability-input-hashes.json").read_text(encoding="utf-8"))
prepare_text = scope["prepare_text"]
replace_command = scope["replace_command"]
prepare_text.__globals__["tokens"]["bijective"] = ("એક-એક અને વ્યાપ્ત", "એક-એક અને વ્યાપ્ત")

integration = json.loads((ROOT / "provenance/SECOND_ORDER_PART_INTEGRATION.json").read_text(encoding="utf-8"))
assert integration["unit_ids"] == [f"OLP-{i:04}" for i in range(322, 341)]
assert len(integration["files"]) == 19
verified = {}
for row in integration["files"]:
    path = ROOT / row["production_path"]
    data = path.read_bytes()
    assert len(data) == row["bytes"] and sha256(data).hexdigest() == row["sha256"]
    verified[row["source_path"]] = path
assert len(verified) == 19
assert len(receipts) == 266

part = ROOT / "gu/content/second-order-logic/second-order-logic.tex"
part_text = prepare_text(part)
chapter_names = re.findall(r"\\olimport(?:\[[^]]+\])?\{([^{}]+)\}", part_text)
assert chapter_names == ["syntax-and-semantics", "metatheory", "sol-and-set-theory"]
part_text = replace_command(part_text, "olpart", 2, lambda _id, title: r"\part{" + title + "}")
part_text = re.sub(r"\\olimport(?:\[[^]]+\])?\{[^{}]+\}", "", part_text)
part_text = part_text.replace(r"\OLEndPartHook", "")
assert r"\olimport" not in part_text and r"\olpart" not in part_text
body += "\n" + part_text + "\n"
receipts.append({"path": part.relative_to(ROOT).as_posix(),
                 "sha256": sha256(part.read_bytes()).hexdigest(),
                 "role": "part_driver_expanded"})

for chapter_name in chapter_names:
    chapter_root = part.parent / chapter_name
    driver = chapter_root / f"{chapter_name}.tex"
    chapter_text = prepare_text(driver)
    section_names = re.findall(r"\\olimport(?:\[[^]]+\])?\{([^{}]+)\}", chapter_text)
    expected = [verified[row["source_path"]].stem for row in integration["files"]
                if Path(row["source_path"]).parent == Path("content/second-order-logic") / chapter_name
                and verified[row["source_path"]] != driver]
    assert section_names == expected, (chapter_name, section_names, expected)
    chapter_text = replace_command(
        chapter_text, "olchapter", 3,
        lambda _part, _chapter, title: r"\section{" + title + "}",
    )
    chapter_text = re.sub(r"\\olimport(?:\[[^]]+\])?\{[^{}]+\}", "", chapter_text)
    chapter_text = chapter_text.replace(r"\OLEndChapterHook", "")
    assert r"\olimport" not in chapter_text and r"\olchapter" not in chapter_text
    body += "\n" + chapter_text + "\n"
    receipts.append({"path": driver.relative_to(ROOT).as_posix(),
                     "sha256": sha256(driver.read_bytes()).hexdigest(),
                     "role": "chapter_driver_expanded"})

    for section_name in section_names:
        path = chapter_root / f"{section_name}.tex"
        prepared = prepare_text(path)
        identifiers = re.findall(r"\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}", prepared)
        assert len(identifiers) == 1 and identifiers[0][0] == "sol", path
        assert len(re.findall(r"\\olsection(?:\[[^]]*\])?\{", prepared)) == 1, path
        prefix = ":".join(identifiers[0])
        prepared = re.sub(r"\\olsection\[[^]]*\]", lambda _m: r"\olsection", prepared, count=1)
        prepared = replace_command(
            prepared, "olsection", 1,
            lambda title: r"\subsection{" + title + r"}\label{" + prefix + ":sec}",
        )
        assert r"\olsection" not in prepared
        body += prepared + "\n"
        receipts.append({"path": path.relative_to(ROOT).as_posix(),
                         "sha256": sha256(path.read_bytes()).hexdigest()})

assert len(receipts) == 285
assert len(re.findall(r"\\olfileid\{", body)) == 254
assert not re.search(r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])", body.replace(r"\string\iftag", ""))
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

name = "second-order-part-cumulative"
(BUILD / f"{name}-body.tex").write_text(body, encoding="utf-8", newline="\n")
(BUILD / f"{name}-available-labels.tex").write_text(
    "\n".join(r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}" for key in sorted(keys)) + "\n",
    encoding="utf-8", newline="\n",
)
(BUILD / f"{name}-available-labels.json").write_text(
    json.dumps(sorted(keys), ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
(BUILD / f"{name}-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"rendered_sections": 254, "source_units_covered": 289,
                  "coverage_scope": "OLP-0004–0273 and OLP-0322–0340",
                  "input_receipts": len(receipts), "labels": len(keys),
                  "sha256": sha256(body.encode("utf-8")).hexdigest()}))
