"""Add source-line and HTML-anchor locators for new computability decisions."""

from csv import DictWriter
from hashlib import sha256
from pathlib import Path
import json
import re


ROOT = Path(__file__).resolve().parents[1]
PROV = ROOT / "provenance"
HTML = ROOT / "reader/computability-theory.html"
OUT = ROOT / "docs/translation-decisions/COMPUTABILITY_OCCURRENCES.csv"
FIELDS = [
    "record_kind", "decision_id", "unit_id", "segment_id", "target_path",
    "target_line", "target_excerpt", "reader_artifact", "reader_anchor",
    "anchor_distance_lines", "reader_status",
]


def load(name: str):
    return json.loads((PROV / name).read_text(encoding="utf-8-sig"))


def lines(name: str):
    return [json.loads(line) for line in (PROV / name).read_text(encoding="utf-8-sig").splitlines() if line]


html = HTML.read_text(encoding="utf-8")
segments = {
    row["segment_id"]: row
    for batch in ("023", "024")
    for row in lines(f"SEGMENT_CANON_USE_{batch}.jsonl")
}
cache = {}


def file_data(path: str):
    path = path.replace("\\", "/")
    if path not in cache:
        data = (ROOT / path).read_bytes()
        labels = []
        file_id = re.search(rb"\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}", data)
        prefix = ":".join(part.decode("utf-8") for part in file_id.groups()) + ":" if file_id else ""
        for match in re.finditer(rb"\\(?:ol)?label\{([^}]+)\}", data):
            label = match.group(1).decode("utf-8")
            if data[match.start():].startswith(b"\\ollabel"):
                label = prefix + label
            if f'id="{label}"' in html:
                labels.append((match.start(), label))
        if prefix and f'id="{prefix}sec"' in html:
            labels.append((0, prefix + "sec"))
        cache[path] = (data, labels)
    return cache[path]


def locator(path: str, byte_offset: int):
    data, labels = file_data(path)
    line = data[:byte_offset].count(b"\n") + 1
    if not labels:
        driver_headings = {
            "gu/content/computability/computability.tex": "સગણનયત",
            "gu/content/computability/recursive-functions/recursive-functions.tex": "પનરવરત-વધય",
        }
        anchor = driver_headings.get(path)
        if anchor:
            assert f'id="{anchor}"' in html
            return line, anchor, "", "verified_html_heading_anchor"
        return line, "", "", "no_file_label_in_reader"
    anchor_offset, anchor = min(labels, key=lambda entry: abs(entry[0] - byte_offset))
    distance = abs(data[:anchor_offset].count(b"\n") + 1 - line)
    return line, anchor, distance, "verified_html_anchor_near_target_line"


rows = []
for batch in ("023", "024"):
    for choice in load(f"CHOICES_{batch}.json")["choices"]:
        for segment_id in choice["segment_ids"]:
            segment = segments[segment_id]
            path = "gu/" + segment["source_path"]
            data, _ = file_data(path)
            assert sha256(data).hexdigest() == segment["target_file_sha256"]
            start, end = segment["target_range_utf8"]
            excerpt = data[start:end]
            assert sha256(excerpt).hexdigest() == segment["target_segment_sha256"]
            line, anchor, distance, status = locator(path, start)
            rows.append({
                "record_kind": "terminology", "decision_id": choice["choice_id"],
                "unit_id": segment["unit_id"], "segment_id": segment_id,
                "target_path": path, "target_line": line,
                "target_excerpt": excerpt.decode("utf-8").strip().replace("\n", " ")[:180],
                "reader_artifact": "reader/computability-theory.html",
                "reader_anchor": anchor, "anchor_distance_lines": distance,
                "reader_status": status,
            })
    for correction in load(f"SOURCE_CORRECTIONS_{batch}.json")["corrections"]:
        path = correction["target_path"]
        data, _ = file_data(path)
        assert sha256(data).hexdigest() == correction["target_sha256"]
        note_line = correction["adjacent_note_line"]
        byte_offset = sum(len(line) for line in data.splitlines(keepends=True)[: note_line - 1])
        line, anchor, distance, status = locator(path, byte_offset)
        rows.append({
            "record_kind": "source_correction", "decision_id": correction["finding_id"],
            "unit_id": correction["unit_id"], "segment_id": "",
            "target_path": path, "target_line": line,
            "target_excerpt": data.splitlines()[note_line - 1].decode("utf-8")[:180],
            "reader_artifact": "reader/computability-theory.html",
            "reader_anchor": anchor, "anchor_distance_lines": distance,
            "reader_status": status,
        })

with OUT.open("w", encoding="utf-8", newline="") as stream:
    writer = DictWriter(stream, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)

summary = {
    "choices": len({row["decision_id"] for row in rows if row["record_kind"] == "terminology"}),
    "choice_occurrences": sum(row["record_kind"] == "terminology" for row in rows),
    "corrections": sum(row["record_kind"] == "source_correction" for row in rows),
    "verified_html_anchors": sum(row["reader_status"].startswith("verified") for row in rows),
    "without_file_anchor": sum(row["reader_status"] == "no_file_label_in_reader" for row in rows),
    "output_sha256": sha256(OUT.read_bytes()).hexdigest(),
}
print(json.dumps(summary))
