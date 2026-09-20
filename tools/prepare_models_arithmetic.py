"""Prepare the cumulative Gujarati reader through Models of Arithmetic.

This adapter launches no TeX process. It extends the accepted cumulative
Model Theory Basics body with the complete Models of Arithmetic chapter
driver and all six translated sections.
"""

from pathlib import Path
import hashlib
import json
import re
import runpy


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
scope = runpy.run_path(str(ROOT / "tools" / "prepare_model_theory_basics.py"))
body = (BUILD / "model-theory-basics-body.tex").read_text(encoding="utf-8")
receipts = json.loads(
    (BUILD / "model-theory-basics-input-hashes.json").read_text(encoding="utf-8")
)

prepare_text = scope["prepare_text"]
replace_command = scope["replace_command"]
tokens = prepare_text.__globals__["tokens"]
tokens.update({
    "derivable": ("નિષ્પન્ન કરી શકાય એવું", "નિષ્પન્ન કરી શકાય એવાં"),
})
chapter_root = ROOT / "gu" / "content" / "model-theory" / "models-of-arithmetic"
chapter_driver = chapter_root / "models-of-arithmetic.tex"
names = [
    "introduction",
    "standard-models",
    "non-standard-models",
    "models-of-q",
    "models-of-pa",
    "computable-models",
]

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
    source_heading_count = len(re.findall(r"\\(?:ol)?section(?:\[[^]]*\])?\{", prepared))
    assert source_heading_count == 1, (path, source_heading_count)
    prepared = re.sub(r"\\olsection(?:\[[^]]*\])?\{", r"\\subsection{", prepared, count=1)
    prepared = re.sub(r"\\section\{", r"\\subsection{", prepared, count=1)
    assert not re.search(r"\\(?:ol)?section(?:\[[^]]*\])?\{", prepared)
    body += prepared + "\n"
    receipts.append({
        "path": path.relative_to(ROOT).as_posix(),
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    })

# These two references point into the later Incompleteness part, which is not
# yet present in the cumulative Gujarati slice. Keep them useful and honest as
# fixed-revision upstream links instead of emitting unresolved local labels.
external_minimization = (
    "https://github.com/OpenLogicProject/OpenLogic/blob/"
    "9620cc73f9c8e0ad003c514a5d3748f29611c4c0/"
    "content/incompleteness/representability-in-q/"
    "minimization-representable.tex"
)
external_refs = {
    r"\olref[inc][req][min]{lem:less-zero}":
        r"\href{" + external_minimization
        + r"}{મૂળ ગ્રંથનું શૂન્યથી નાની સંખ્યા અંગેનું લેમા}",
    r"\olref[inc][req][min]{lem:less-nsucc}":
        r"\href{" + external_minimization
        + r"}{મૂળ ગ્રંથનું ઉત્તરગામીથી નાની સંખ્યા અંગેનું લેમા}",
}
for source_ref, external_ref in external_refs.items():
    assert body.count(source_ref) == 1, source_ref
    body = body.replace(source_ref, external_ref)

receipts.append({
    "path": chapter_driver.relative_to(ROOT).as_posix(),
    "sha256": hashlib.sha256(chapter_driver.read_bytes()).hexdigest(),
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

(BUILD / "models-arithmetic-body.tex").write_text(body, encoding="utf-8", newline="\n")
(BUILD / "models-arithmetic-available-labels.tex").write_text(
    "\n".join(
        r"\expandafter\def\csname guavailable@" + key + r"\endcsname{1}"
        for key in sorted(keys)
    ) + "\n",
    encoding="utf-8",
    newline="\n",
)
(BUILD / "models-arithmetic-available-labels.json").write_text(
    json.dumps(sorted(keys), indent=2) + "\n", encoding="utf-8", newline="\n"
)
(BUILD / "models-arithmetic-input-hashes.json").write_text(
    json.dumps(receipts, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)

assert len(receipts) == 190, len(receipts)
sections = len(re.findall(r"\\olfileid\{", body))
assert sections == 171, sections
assert not re.search(
    r"!!|\\(?:iftag|tagitem|tagprob|tagendprob|startycommalist|ycomma)(?![A-Za-z])",
    body.replace(r"\string\iftag", ""),
)
print(json.dumps({
    "rendered_sections": sections,
    "source_units_covered": 194,
    "input_receipts": len(receipts),
    "labels": len(keys),
    "logic_profile": "models_of_arithmetic_after_model_theory_basics",
    "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
}))
