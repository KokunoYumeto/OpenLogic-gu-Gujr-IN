"""Link batch-025 terminology and correction occurrences to checked HTML anchors."""

from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import csv
import json
import re


ROOT = Path(__file__).resolve().parents[1]
STATE = Path(r"C:\interlanguage-task-state\openlogic-gu-Gujr-IN")
HTML = ROOT / "reader/turing-machines.html"
OUT = ROOT / "docs/translation-decisions/TURING_MACHINES_OCCURRENCES.csv"
QA = STATE / "DECISION_OCCURRENCES_QA_025.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


html = HTML.read_text(encoding="utf-8")
ids = set(re.findall(r'\bid="([^"]+)"', html))
segments = {
    row["segment_id"]: row
    for row in map(json.loads, (STATE / "SEGMENT_CANON_USE_025.jsonl").read_text(encoding="utf-8").splitlines())
}
choices = load(STATE / "CHOICES_025.json")["choices"]
corrections = load(STATE / "SOURCE_CORRECTIONS_025.json")["corrections"]
unit_by_path = {
    (ROOT / "gu" / row["source_path"]).resolve(): row["unit_id"]
    for row in map(json.loads, (ROOT / "provenance/SOURCE_MANIFEST.jsonl").read_text(encoding="utf-8").splitlines())
}


def anchor(path: Path) -> str:
    name = path.name
    if name == "turing-machines.tex" and path.parent.name == "turing-machines":
        result = "ટયરગ-મશન"
    elif name == "machines-computations.tex":
        result = "ટયરગ-મશનન-સગણનઓ"
    else:
        match = re.search(r"\\olfileid\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}", path.read_text(encoding="utf-8"))
        assert match, path
        result = ":".join(match.groups()) + ":sec"
    assert result in ids, (path, result)
    return result


rows = []
for choice in choices:
    for segment_id in choice["segment_ids"]:
        segment = segments[segment_id]
        path = ROOT / "gu" / segment["source_path"]
        data = path.read_bytes()
        start, end = segment["target_range_utf8"]
        excerpt = data[start:end]
        assert sha256(excerpt).hexdigest() == segment["target_segment_sha256"]
        assert sha256(data).hexdigest() == segment["target_file_sha256"]
        line = data[:start].count(b"\n") + 1
        target_anchor = anchor(path)
        rows.append({
            "record_kind": "terminology", "decision_id": choice["choice_id"],
            "unit_id": segment["unit_id"], "segment_id": segment_id,
            "target_path": path.relative_to(ROOT).as_posix(), "target_line": line,
            "target_excerpt": " ".join(excerpt.decode("utf-8").split())[:200],
            "reader_artifact": "reader/turing-machines.html", "reader_anchor": target_anchor,
            "reader_status": "verified_html_section_anchor_near_exact_source_segment",
        })

for correction in corrections:
    path = ROOT / correction["target_path"]
    line = correction["adjacent_note_line"]
    text = path.read_text(encoding="utf-8").splitlines()[line - 1]
    assert correction["finding_id"] in path.read_text(encoding="utf-8")
    target_anchor = anchor(path)
    rows.append({
        "record_kind": "keyed_source_correction", "decision_id": correction["finding_id"],
        "unit_id": unit_by_path[path.resolve()],
        "segment_id": "", "target_path": path.relative_to(ROOT).as_posix(),
        "target_line": line, "target_excerpt": text.strip()[:200],
        "reader_artifact": "reader/turing-machines.html", "reader_anchor": target_anchor,
        "reader_status": "verified_html_section_anchor_near_keyed_note",
    })

fields = [
    "record_kind", "decision_id", "unit_id", "segment_id", "target_path", "target_line",
    "target_excerpt", "reader_artifact", "reader_anchor", "reader_status",
]
with OUT.open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)

qa = {
    "schema": "openlogic-gu-decision-occurrences-qa/25",
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "coverage": "260/722; new occurrences OLP-0252–0263",
    "terminology_decisions": len(choices),
    "terminology_occurrences": sum(row["record_kind"] == "terminology" for row in rows),
    "keyed_correction_occurrences": len(corrections),
    "html_sha256": digest(HTML),
    "csv_path": OUT.relative_to(ROOT).as_posix(),
    "csv_sha256": digest(OUT),
    "all_source_segments_hashed": True,
    "all_reader_anchors_present": True,
    "status": "passed_exact_source_locations_and_nearby_html_anchors",
}
QA.write_text(json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"occurrences": len(rows), "terminology": qa["terminology_occurrences"], "corrections": len(corrections)}))
