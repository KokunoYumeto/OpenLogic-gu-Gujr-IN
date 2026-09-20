"""Prepare the cumulative Gujarati reader through the Interpolation chapter.

This adapter launches no TeX process. It extends the accepted cumulative
Models of Arithmetic body with the complete Interpolation chapter driver and
all four translated sections.
"""

from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_models_arithmetic.py"))
body = (BUILD / "models-arithmetic-body.tex").read_text(encoding="utf-8")
receipts = json.loads(
    (BUILD / "models-arithmetic-input-hashes.json").read_text(encoding="utf-8")
)

prepare_text = scope["prepare_text"]
replace_command = scope["replace_command"]
chapter_root = ROOT / "gu" / "content" / "model-theory" / "interpolation"
chapter_driver = chapter_root / "interpolation.tex"
names = ["introduction", "separation", "interpolation-proof", "definability"]

chapter_driver_text = prepare_text(chapter_driver)
chapter_driver_text = replace_command(
    chapter_driver_text,
    "olchapter",
    3,
    lambda _part, _chapter, title: r"\section{" + title + "}",
)
chapter_driver_text = re.sub(
    r"\\olimport(?:\[[^]]+\])?\{[^{}]+\}", "", chapter_driver_text
)
chapter_driver_text = chapter_driver_text.replace(r"\OLEndChapterHook", "")
assert r"\olimport" not in chapter_driver_text
assert r"\olchapter" not in chapter_driver_text
body += "\n" + chapter_driver_text + "\n"

for name in names:
    path = chapter_root / f"{name}.tex"
    prepared = prepare_text(path)
    source_heading_count = len(
        re.findall(r"\\(?:ol)?section(?:\[[^]]*\])?\{", prepared)
    )
    assert source_heading_count == 1, (path, source_heading_count)
    prepared = re.sub(
        r"\\olsection(?:\[[^]]*\])?\{", r"\\subsection{", prepared, count=1
    )
    prepared = re.sub(r"\\section\{", r"\\subsection{", prepared, count=1)
    assert not re.search(r"\\(?:ol)?section(?:\[[^]]*\])?\{", prepared)
    body += prepared + "\n"
    receipts.append(
        {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        }
    )

receipts.append(
    {
        "path": chapter_driver.relative_to(ROOT).as_posix(),
        "sha256": hashlib.sha256(chapter_driver.read_bytes()).hexdigest(),
        "role": "chapter_driver_expanded",
    }
)

keys = set()
for block in re.split(r"(?=\\olfileid)", body):
    match = re.search(
        r"\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}", block
    )
    if not match:
        continue
    prefix = ":".join(match.groups())
    keys.add(prefix + ":sec")
    for label in re.findall(r"\\ollabel\{([^}]+)\}", block):
        keys.add(prefix + ":" + label)
    for label in re.findall(r"\\label\{([^}]+)\}", block):
        keys.add(label)

(BUILD / "interpolation-body.tex").write_text(
    body, encoding="utf-8", newline="\n"
)
(BUILD / "interpolation-available-labels.tex").write_text(
    "\n".join(
        r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}"
        for key in sorted(keys)
    )
    + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "interpolation-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "interpolation-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)

assert len(receipts) == 195, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 175, sections
assert not re.search(
    r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])",
    body.replace(r"\string\iftag", ""),
)
print(
    json.dumps(
        {
            "rendered_sections": sections,
            "source_units_covered": 199,
            "input_receipts": len(receipts),
            "labels": len(keys),
            "logic_profile": "interpolation_after_models_of_arithmetic",
            "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
        }
    )
)
