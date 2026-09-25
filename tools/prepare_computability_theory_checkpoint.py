"""Inventory the exact reviewed 248-unit source checkpoint for public readback."""

from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
STATE = Path(r"C:\interlanguage-task-state\openlogic-gu-Gujr-IN")
PROV = ROOT / "provenance"
SOURCE_REVISION = "9620cc73f9c8e0ad003c514a5d3748f29611c4c0"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


manifest = [json.loads(line) for line in (PROV / "SOURCE_MANIFEST.jsonl").read_text(encoding="utf-8-sig").splitlines() if line]
coverage = load(PROV / "COVERAGE.json")
qa = load(PROV / "CUMULATIVE_QA_024.json")
html = load(PROV / "HTML_QA_024.json")
pdf = load(PROV / "PDF_QA_024.json")
epub = load(PROV / "EPUB_QA_024.json")
full_text = load(PROV / "FULL_TEXT_SOURCE_QA_024.json")
assert len(manifest) == len(coverage["units"]) == 722
assert coverage["translated"] == qa["working_coverage"]["translated"] == 248
assert qa["status"] == "passed_local_248_unit_html_pdf_epub_gate_pending_source_package_and_publication"
assert len({row["unit_id"] for row in manifest}) == 722
translated = []
for source_row, status_row in zip(manifest, coverage["units"]):
    assert source_row["unit_id"] == status_row["unit_id"]
    assert source_row["source_sha256"] == status_row["source_sha256"]
    original = ROOT / "upstream" / source_row["source_path"]
    assert digest(original) == source_row["source_sha256"]
    target = ROOT / "gu" / source_row["source_path"]
    if "translation_sha256" in status_row:
        assert target.is_file() and digest(target) == status_row["translation_sha256"]
        translated.append(source_row["unit_id"])
    else:
        assert not target.exists()
assert translated == [f"OLP-{number:04}" for number in range(4, 252)]
assert digest(ROOT / html["path"]) == html["sha256"]
assert digest(ROOT / pdf["path"]) == pdf["sha256"]
assert digest(ROOT / epub["path"]) == epub["sha256"]
assert digest(ROOT / "releases/OpenLogic-gu-Gujr-IN-Computability-Theory-Full-Text.tex") == full_text["input"]["sha256"]
assert full_text["status"] == "passed_materialized_full_text_and_exact_reader_reproduction"
assert len((ROOT / "docs/translation-decisions/COMPUTABILITY_OCCURRENCES.csv").read_text(encoding="utf-8").splitlines()) == 134

files = [
    path
    for folder in ("upstream", "gu", "fonts", "tools", "reader", "docs", "provenance", "releases")
    for path in (ROOT / folder).rglob("*")
    if path.is_file()
    and "__pycache__" not in path.parts
    and not path.name.endswith("_expanded.py")
    and path.name not in {"PUBLIC_FILES.json", "SOURCE_CHECKPOINT_024.json"}
]
files += [ROOT / name for name in (".gitattributes", ".gitignore", "LICENSE.md", "README.md")]
files += list(ROOT.glob("gu-*.tex"))
files = sorted(set(files))
for path in files:
    if path.suffix.lower() in {".md", ".json", ".jsonl", ".csv", ".html", ".py", ".ps1", ".tex", ".svg", ".txt"} and "upstream" not in path.parts:
        data = path.read_bytes().lower()
        forbidden = (
            b"c:" + b"\\users\\", b"c:/" + b"users/", b"authorization:" + b" bearer",
            b"github_" + b"pat_", b"gh" + b"p_",
        )
        assert not any(token in data for token in forbidden), path

checkpoint = {
    "schema": "openlogic-gu-source-checkpoint/24",
    "prepared_utc": datetime.now(timezone.utc).isoformat(),
    "source_revision": SOURCE_REVISION,
    "coverage": {
        "translated": 248, "total": 722, "public_release_verified_at_preparation": 204,
        "scope": "OLP-0004–0251; cumulative through complete Computability Theory chapter",
        "complete_edition": False,
    },
    "qa": {
        "linguistic_blocks": 2498,
        "source_math_spans": 14203,
        "semantic_reverse_samples": 1193,
        "term_decisions": 224,
        "historical_and_current_keyed_disclosures": 197,
        "html_sha256": html["sha256"], "html_mathml": html["mathml_nodes"],
        "pdf_sha256": pdf["sha256"], "pdf_pages": pdf["pages"],
        "epub_sha256": epub["sha256"], "epubcheck_messages": epub["epubcheck"]["messages"],
        "full_text_source_sha256": full_text["input"]["sha256"],
        "full_text_exact_pdf_reproduction": full_text["verification"]["exact_reader_reproduction"],
        "computability_decision_occurrences": 133,
    },
    "files": [
        {"path": path.relative_to(ROOT).as_posix(), "bytes": path.stat().st_size, "sha256": digest(path)}
        for path in files
    ],
}
out = PROV / "SOURCE_CHECKPOINT_024.json"
out.write_text(json.dumps(checkpoint, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
pathspecs = [path.relative_to(ROOT).as_posix() for path in files + [out]]
(STATE / "work/git-pathspecs024.txt").write_text("\n".join(pathspecs) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"translated": len(translated), "files": len(files), "checkpoint_sha256": digest(out), "pathspec": str(STATE / "work/git-pathspecs024.txt")}))
