"""Check that the one-file 260-unit TeX recreates the accepted reader PDF."""

from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[1]
STATE = Path(r"C:\interlanguage-task-state\openlogic-gu-Gujr-IN")
SOURCE = ROOT / "releases/OpenLogic-gu-Gujr-IN-Turing-Machines-Full-Text.tex"
PDF = ROOT / "releases/OpenLogic-gu-Gujr-IN-Turing-Machines.pdf"
RECEIPT = STATE / "work/fulltext025/BUILD_RECEIPT_025.json"
OUTPUT = STATE / "FULL_TEXT_SOURCE_QA_025.json"
MATERIALIZATION = STATE / "FULL_TEXT_SOURCE_MATERIALIZATION_025.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write(path: Path, value: dict) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )


receipt = load(RECEIPT)
materialization = load(MATERIALIZATION)
assert receipt["acquired"] and receipt["status"] == "built_pending_visual_and_semantic_qa"
assert Path(receipt["input_file"]).resolve() == SOURCE.resolve()
assert len(receipt["passes"]) == 3
assert all(row["exit_code"] == 0 for row in receipt["passes"])
source_hash, pdf_hash = digest(SOURCE), digest(PDF)
assert materialization["output"]["sha256"] == source_hash
assert materialization["output"]["bytes"] == SOURCE.stat().st_size
assert materialization["content_checks"]["reader_body_embedded_exactly"]
assert materialization["content_checks"]["unresolved_cumulative_body_inputs"] == 0
assert all(row["pdf_sha256"] == pdf_hash for row in receipt["passes"])
assert receipt["replay_equal"]

qa = {
    "schema": "openlogic-gu-full-text-source-qa/25",
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "input": {"path": str(SOURCE), "bytes": SOURCE.stat().st_size, "sha256": source_hash},
    "accepted_release_pdf": {"path": str(PDF), "bytes": PDF.stat().st_size, "sha256": pdf_hash},
    "guarded_receipt_sha256": digest(RECEIPT),
    "verification": {
        "verification_passes": 3,
        "all_three_verification_passes_byte_identical": True,
        "exact_reader_reproduction": True,
        "accepted_pdf_byte_identity": True,
        "source_units": 260,
        "total_units": 722,
    },
    "status": "passed_materialized_full_text_and_exact_reader_reproduction",
}
write(OUTPUT, qa)
materialization["status"] = "passed_guarded_exact_reader_reproduction"
materialization["reproduction_qa_sha256"] = digest(OUTPUT)
write(MATERIALIZATION, materialization)
print(json.dumps({"input_sha256": source_hash, "pdf_sha256": pdf_hash, "status": qa["status"]}))
