"""Build the canonical Gujarati translation-decision release surfaces.

The generator converts the durable terminology ledger and every applied
frozen-source correction receipt into the shared v1 decision schema.  Each
decision receives at least one exact source/target byte locator.  Reader pages
are included only when a deterministic target-to-assembled-body alignment and
SyncTeX query both succeed; otherwise the locator remains explicitly pending.
"""

from __future__ import annotations

import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
STATE = Path(r"C:\interlanguage-task-state\openlogic-gu-Gujr-IN")
OUT = ROOT / "docs" / "translation-decisions"
SCHEMA_PATH = OUT / "translation-decision.schema.json"
SOURCE_REVISION = "9620cc73f9c8e0ad003c514a5d3748f29611c4c0"
BODY_PATH = ROOT / "build" / "natural-deduction-body.tex"
PDF_PATH = ROOT / "build" / "gu-natural-deduction.pdf"
SYNCTEX_PATH = ROOT / "build" / "gu-natural-deduction.synctex.gz"
BUILD_RECEIPT_PATH = ROOT / "build" / "BUILD_RECEIPT_010.json"
BT = chr(96)

EDITION = {
    "edition_id": "openlogic-gu-Gujr-IN",
    "language_tag": "gu-Gujr-IN",
    "language_name": "Gujarati",
    "script": "Gujr",
    "territory": "IN",
    "locale": "gu_IN",
    "register_or_variant": "standard contemporary Gujarati mathematical didactic register",
    "notation_profile": "international mathematical notation with Gujarati prose numerals",
    "layer_type": "semantic_translation",
    "parent_semantic_edition_id": None,
}

MANUAL_OCCURRENCES = {
    "GU-T001": {
        "unit_id": "OLP-0005",
        "source_path": "upstream/content/sets-functions-relations/sets/basics.tex",
        "source_line": 12,
        "target_path": "gu/content/sets-functions-relations/sets/basics.tex",
        "target_line": 12,
    },
    "GU-T044": {
        "unit_id": "OLP-0034",
        "source_path": "upstream/content/sets-functions-relations/size-of-sets/reduction.tex",
        "source_line": 38,
        "target_path": "gu/content/sets-functions-relations/size-of-sets/reduction.tex",
        "target_line": 39,
    },
    "GU-T045": {
        "unit_id": "OLP-0038",
        "source_path": "upstream/content/sets-functions-relations/size-of-sets/enumerability-alt.tex",
        "source_line": 40,
        "target_path": "gu/content/sets-functions-relations/size-of-sets/enumerability-alt.tex",
        "target_line": 39,
    },
    "GU-T051": {
        "unit_id": "OLP-0026",
        "source_path": "upstream/content/sets-functions-relations/functions/partial-functions.tex",
        "source_line": 63,
        "target_path": "gu/content/sets-functions-relations/functions/partial-functions.tex",
        "target_line": 72,
    },
    "GU-T057": {
        "unit_id": "OLP-0040",
        "source_path": "upstream/content/sets-functions-relations/size-of-sets/enumerability-alt.tex",
        "source_line": 100,
        "target_path": "gu/content/sets-functions-relations/size-of-sets/enumerability-alt.tex",
        "target_line": 98,
    },
}


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def repo_path(path_string: str) -> Path:
    value = path_string.replace("\\", "/")
    if value.startswith("content/"):
        value = "upstream/" + value
    return ROOT / Path(value)


def source_rel_from_target(target_rel: str) -> str:
    value = target_rel.replace("\\", "/")
    assert value.startswith("gu/content/"), value
    return "upstream/" + value[3:]


def target_rel_from_source(source_rel: str) -> str:
    value = source_rel.replace("\\", "/")
    if value.startswith("upstream/"):
        value = value[len("upstream/") :]
    assert value.startswith("content/"), value
    return "gu/" + value


def line_bounds(raw: bytes, line_number: int) -> tuple[int, int, str]:
    lines = raw.splitlines(keepends=True)
    if not 1 <= line_number <= len(lines):
        raise AssertionError((line_number, len(lines)))
    start = sum(len(part) for part in lines[: line_number - 1])
    payload = lines[line_number - 1].rstrip(b"\r\n")
    end = start + len(payload)
    excerpt = payload.decode("utf-8")
    if not excerpt.strip():
        raise AssertionError(f"Blank evidence line {line_number}")
    return start, end, excerpt


def text_locator(
    path_string: str,
    line_number: int,
    term: str | None,
    intended_sense: str,
    context: str,
) -> dict[str, Any]:
    path = repo_path(path_string)
    raw = path.read_bytes()
    start, end, excerpt = line_bounds(raw, line_number)
    normalized_path = rel(path)
    return {
        "path": normalized_path,
        "file_id": normalized_path,
        "file_sha256": hashlib.sha256(raw).hexdigest(),
        "line_span": {"status": "available", "start": line_number, "end": line_number},
        "byte_span": {"status": "available", "start": start, "end_exclusive": end},
        "printed_page": None,
        "excerpt": excerpt,
        "term": term,
        "intended_sense": intended_sense,
        "context": context,
    }


def masked_source_note_text(path: Path) -> tuple[str, set[int]]:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    masked: list[str] = []
    note_lines: set[int] = set()
    in_note = False
    depth = 0
    for line_number, line in enumerate(lines, 1):
        if not in_note and r"\sourcecorrection{" in line:
            in_note = True
            fragment = line[line.index(r"\sourcecorrection{") :]
            depth = fragment.count("{") - fragment.count("}")
        elif in_note:
            depth += line.count("{") - line.count("}")
        if in_note:
            note_lines.add(line_number)
            masked.append("\n" if line.endswith(("\n", "\r")) else "")
            if depth <= 0:
                in_note = False
                depth = 0
        else:
            masked.append(line)
    assert not in_note, path
    return "".join(masked), note_lines


def blocks(path: Path, omit_source_notes: bool = False) -> list[tuple[int, int, str]]:
    text = (
        masked_source_note_text(path)[0]
        if omit_source_notes
        else path.read_text(encoding="utf-8")
    )
    output: list[tuple[int, int, str]] = []
    for match in re.finditer(r"\S[\s\S]*?(?=\n\s*\n|\Z)", text):
        value = match.group(0)
        start = text.count("\n", 0, match.start()) + 1
        end = start + value.count("\n")
        if omit_source_notes and r"\sourcecorrection{" in value:
            continue
        output.append((start, end, value))
    return output


def evidence_line_is_usable(path: Path, line_number: int) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not 1 <= line_number <= len(lines):
        return False
    if not lines[line_number - 1].strip() or lines[line_number - 1].lstrip().startswith("%"):
        return False
    _masked, note_lines = masked_source_note_text(path)
    return line_number not in note_lines


def first_global_evidence_line(path: Path, terms: list[str]) -> int | None:
    masked, _note_lines = masked_source_note_text(path)
    lines = masked.splitlines()
    for term in terms:
        needle = term.casefold()
        for line_number, line in enumerate(lines, 1):
            if line.lstrip().startswith("%"):
                continue
            if needle in line.casefold():
                return line_number
    return None


def search_parts(value: str) -> list[str]:
    candidates = []
    for part in re.split(r"\s*/\s*|,\s*|;\s*", value):
        cleaned = part.strip()
        if cleaned:
            candidates.append(cleaned)
        candidates.extend(
            word
            for word in re.findall(r"[A-Za-z][A-Za-z -]{2,}|[\u0A80-\u0AFF]{2,}", cleaned)
            if len(word.strip()) >= 3
        )
    return sorted(set(candidates), key=len, reverse=True)


def first_matching_line(
    path: Path, start: int, end: int, terms: list[str]
) -> int | None:
    lines = path.read_text(encoding="utf-8").splitlines()
    for term in terms:
        needle = term.casefold()
        for number in range(start, min(end, len(lines)) + 1):
            if needle in lines[number - 1].casefold():
                return number
    return None


def first_substantive_line(path: Path, start: int, end: int) -> int:
    lines = path.read_text(encoding="utf-8").splitlines()
    for number in range(start, min(end, len(lines)) + 1):
        value = lines[number - 1].strip()
        if value and not value.startswith("%") and value not in {
            r"\begin{document}",
            r"\end{document}",
        }:
            return number
    raise AssertionError((path, start, end))


def aligned_line(
    known_path: Path,
    other_path: Path,
    known_line: int,
    other_terms: list[str],
) -> int:
    known_blocks = blocks(known_path, omit_source_notes=True)
    other_blocks = blocks(other_path, omit_source_notes=True)
    known_index = next(
        (
            index
            for index, (start, end, _text) in enumerate(known_blocks)
            if start <= known_line <= end
        ),
        None,
    )
    if known_index is None:
        raise AssertionError((known_path, known_line))
    if known_index >= len(other_blocks):
        raise AssertionError(
            f"Unaligned block {known_index}: {known_path} -> {other_path}"
        )
    start, end, _text = other_blocks[known_index]
    return (
        first_matching_line(other_path, start, end, other_terms)
        or first_substantive_line(other_path, start, end)
    )


def normalize_source_path(value: str) -> str:
    value = value.replace("\\", "/")
    return value if value.startswith("upstream/") else "upstream/" + value


def normalize_target_path(value: str) -> str:
    value = value.replace("\\", "/")
    return value if value.startswith("gu/") else "gu/" + value


def term_occurrence(term: dict[str, Any]) -> dict[str, Any]:
    decision_id = term["term_id"]
    english_parts = search_parts(term["english"])
    gujarati_parts = search_parts(term["gujarati"])
    source_uses = []
    for candidate in term.get("english_usage_locations", []):
        adjusted = dict(candidate)
        path = repo_path(normalize_source_path(adjusted["path"]))
        if not path.exists():
            continue
        if not evidence_line_is_usable(path, int(adjusted["line"])):
            recovered = first_global_evidence_line(path, english_parts)
            if recovered is None:
                continue
            adjusted["line"] = recovered
        source_uses.append(adjusted)
    target_uses = []
    for candidate in term.get("gujarati_usage_locations", []):
        adjusted = dict(candidate)
        path = repo_path(normalize_target_path(adjusted["path"]))
        if not path.exists():
            continue
        if not evidence_line_is_usable(path, int(adjusted["line"])):
            recovered = first_global_evidence_line(path, gujarati_parts)
            if recovered is None:
                continue
            adjusted["line"] = recovered
        target_uses.append(adjusted)

    if decision_id in MANUAL_OCCURRENCES:
        selected = MANUAL_OCCURRENCES[decision_id]
        unit_id = selected["unit_id"]
        source_path = selected["source_path"]
        source_line = selected["source_line"]
        target_path = selected["target_path"]
        target_line = selected["target_line"]
    elif target_uses:
        target_use = next(
            (
                candidate
                for candidate in target_uses
                if repo_path(normalize_target_path(candidate["path"])).exists()
            ),
            target_uses[0],
        )
        unit_id = target_use["unit_id"]
        target_path = normalize_target_path(target_use["path"])
        target_line = int(target_use["line"])
        if not evidence_line_is_usable(repo_path(target_path), target_line):
            target_line = first_global_evidence_line(
                repo_path(target_path), gujarati_parts
            ) or target_line
        source_path = source_rel_from_target(target_path)
        same_source = next(
            (
                candidate
                for candidate in source_uses
                if candidate["unit_id"] == unit_id
                and normalize_source_path(candidate["path"]) == source_path
            ),
            None,
        )
        source_line = (
            int(same_source["line"])
            if same_source
            else aligned_line(
                repo_path(target_path),
                repo_path(source_path),
                target_line,
                english_parts,
            )
        )
        if not evidence_line_is_usable(repo_path(source_path), source_line):
            source_line = first_global_evidence_line(
                repo_path(source_path), english_parts
            ) or source_line
    elif source_uses:
        source_use = next(
            (
                candidate
                for candidate in source_uses
                if repo_path(normalize_source_path(candidate["path"])).exists()
            ),
            source_uses[0],
        )
        unit_id = source_use["unit_id"]
        source_path = normalize_source_path(source_use["path"])
        source_line = int(source_use["line"])
        if not evidence_line_is_usable(repo_path(source_path), source_line):
            source_line = first_global_evidence_line(
                repo_path(source_path), english_parts
            ) or source_line
        target_path = target_rel_from_source(source_path)
        target_line = aligned_line(
            repo_path(source_path),
            repo_path(target_path),
            source_line,
            gujarati_parts,
        )
        if not evidence_line_is_usable(repo_path(target_path), target_line):
            target_line = first_global_evidence_line(
                repo_path(target_path), gujarati_parts
            ) or target_line
    else:
        raise AssertionError(f"No occurrence evidence for {decision_id}")

    context = "Representative aligned occurrence for this decision."
    source = text_locator(
        source_path,
        source_line,
        term["english"],
        term["rationale"],
        context,
    )
    target = text_locator(
        target_path,
        target_line,
        term["gujarati"],
        term["rationale"],
        context,
    )
    source_block_number = next(
        index
        for index, (start, end, _text) in enumerate(blocks(repo_path(source_path)), 1)
        if start <= source_line <= end
    )
    return {
        "occurrence_id": f"{decision_id}-O001",
        "unit_id": unit_id,
        "semantic_unit_id": f"{unit_id}:B{source_block_number:04d}",
        "source": source,
        "target": target,
        "reader_locator": {},
        "evidence_refs": [
            {
                "path_or_uri": source["path"],
                "bytes": repo_path(source["path"]).stat().st_size,
                "sha256": source["file_sha256"],
                "version_or_ref": SOURCE_REVISION,
            },
            {
                "path_or_uri": target["path"],
                "bytes": repo_path(target["path"]).stat().st_size,
                "sha256": target["file_sha256"],
            },
        ],
    }


def authority_from_passage(
    passage: dict[str, Any],
    canon_sources: dict[str, dict[str, Any]],
    supports: bool,
) -> dict[str, Any]:
    source = canon_sources.get(passage["source_id"], {})
    passage_hash = (
        passage.get("passage_sha256")
        or passage.get("render_sha256")
        or passage.get("extract_sha256")
    )
    source_hash = (
        passage.get("extract_sha256")
        or passage.get("render_sha256")
        or source.get("extract_sha256")
        or source.get("original_sha256")
    )
    assert passage_hash and re.fullmatch(r"[0-9a-f]{64}", passage_hash)
    return {
        "authority_id": passage["passage_id"],
        "citation": source.get("title", passage["source_id"]),
        "passage_id": passage["passage_id"],
        "locator": json.dumps(passage["locator"], ensure_ascii=False, sort_keys=True),
        "source_sha256": source_hash,
        "passage_sha256": passage_hash,
        "status": "checked_supports" if supports else "checked_context_only",
        "note": (
            passage.get("inspection", "Passage inspected.")
            + " "
            + passage.get(
                "evidence_role",
                "Gujarati usage and expository register evidence.",
            )
        ).strip(),
    }


def alternatives_from_term(term: dict[str, Any]) -> list[dict[str, str]]:
    output = []
    for item in term.get("alternatives_considered", {}).get("items", []):
        if item.casefold().startswith("no rejected alternative"):
            continue
        pieces = re.split(r"\s+[—–-]\s+", item, maxsplit=1)
        rendering = pieces[0].strip(" .")
        reason = (
            pieces[1].strip()
            if len(pieces) == 2
            else "Recorded as an alternative in the durable decision ledger."
        )
        if not rendering:
            continue
        lowered = reason.casefold()
        if "supersed" in lowered:
            disposition = "superseded"
        elif "reserved" in lowered:
            disposition = "reserved_for_other_sense"
        elif any(word in lowered for word in ("possible", "plausible", "retained", "variant")):
            disposition = "viable_alternative"
        else:
            disposition = "rejected"
        output.append(
            {
                "rendering": rendering,
                "disposition": disposition,
                "reason": reason,
            }
        )
    return output


def term_decision(
    term: dict[str, Any],
    passages: dict[str, dict[str, Any]],
    canon_sources: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    uncertainty = term.get("uncertainty", {})
    level = str(uncertainty.get("level", "open")).casefold()
    provisional = bool(uncertainty.get("open_correction")) or "provisional" in term.get(
        "status", ""
    )
    if provisional or level == "open":
        confidence = "low"
    elif level == "medium":
        confidence = "medium"
    else:
        confidence = "high"
    priority = {"low": "high", "medium": "normal", "high": "low"}[confidence]
    origin = term.get("decision_record_origin", "")
    recording_mode = "retrospective" if origin.startswith("retrospective") else "contemporaneous"
    question = term.get("precise_review_question")
    if provisional and question and not question.startswith("Please double-check"):
        question = "Please double-check: " + question
    expert_useful = provisional or confidence != "high"
    if not expert_useful:
        question = None
    checked = []
    for passage_id in term.get("passages", []):
        passage = passages[passage_id]
        directly_supported = (
            confidence == "high"
            and bool(passage.get("short_term_attestation"))
            and term.get("status") == "adopted"
        )
        checked.append(
            authority_from_passage(passage, canon_sources, directly_supported)
        )
    if not checked:
        raise AssertionError(f"No checked authority for {term['term_id']}")
    return {
        "decision_id": term["term_id"],
        "record_kind": term.get("decision_type", "terminology"),
        "recording_mode": recording_mode,
        "edition": EDITION,
        "source_term_or_construction": term["english"],
        "intended_sense": term["rationale"],
        "chosen_rendering": term["gujarati"],
        "rationale": term["rationale"],
        "authorities_checked": checked,
        "alternatives": alternatives_from_term(term),
        "confidence": confidence,
        "confidence_reason": uncertainty.get(
            "note", "Confidence follows the checked authority and recorded scope."
        ),
        "provisional": provisional,
        "review_priority": priority,
        "expert_review_useful": expert_useful,
        "expert_review_reason": (
            "Native Gujarati mathematical-logic review can confirm the exact specialist form and inflection."
            if expert_useful
            else None
        ),
        "please_double_check_question": question,
        "occurrences": [term_occurrence(term)],
    }


def parse_locator_lines(locator: str) -> list[int]:
    match = re.search(r":\s*([0-9][0-9,\s-]*)", locator)
    if not match:
        raise AssertionError(locator)
    tail = match.group(1)
    output: list[int] = []
    for start, end in re.findall(r"(\d+)(?:-(\d+))?", tail):
        first = int(start)
        last = int(end) if end else first
        output.extend(range(first, last + 1))
    if not output:
        raise AssertionError(locator)
    return output


def correction_decision(
    receipt_path: Path, receipt: dict[str, Any], item: dict[str, Any]
) -> dict[str, Any]:
    decision_id = item["finding_id"]
    source_path = normalize_source_path(item["source_path"])
    target_path = normalize_target_path(item["target_path"])
    source_lines = parse_locator_lines(item["source_locator"])
    target_lines = item.get("corrected_body_lines", [item["corrected_body_line"]])
    occurrences = []
    for index, target_line in enumerate(target_lines, 1):
        source_line = source_lines[min(index - 1, len(source_lines) - 1)]
        source = text_locator(
            source_path,
            source_line,
            item["classification"],
            item.get("finding", item["handling"]),
            "Frozen-source defect locus.",
        )
        target = text_locator(
            target_path,
            target_line,
            item["handling"],
            item.get("finding", item["handling"]),
            "Applied Gujarati correction locus.",
        )
        source_block_number = next(
            block_index
            for block_index, (start, end, _text) in enumerate(
                blocks(repo_path(source_path)), 1
            )
            if start <= source_line <= end
        )
        occurrences.append(
            {
                "occurrence_id": f"{decision_id}-O{index:03d}",
                "unit_id": item["unit_id"],
                "semantic_unit_id": f"{item['unit_id']}:B{source_block_number:04d}",
                "source": source,
                "target": target,
                "reader_locator": {},
                "evidence_refs": [
                    {
                        "path_or_uri": source["path"],
                        "bytes": repo_path(source["path"]).stat().st_size,
                        "sha256": source["file_sha256"],
                        "version_or_ref": SOURCE_REVISION,
                    },
                    {
                        "path_or_uri": target["path"],
                        "bytes": repo_path(target["path"]).stat().st_size,
                        "sha256": target["file_sha256"],
                    },
                    {
                        "path_or_uri": "state/" + receipt_path.name,
                        "bytes": receipt_path.stat().st_size,
                        "sha256": sha256_path(receipt_path),
                    },
                ],
            }
        )
    delta = item.get("mathematical_delta") or {}
    removed = delta.get("removed") or item["classification"].replace("_", " ")
    added = delta.get("added") or item["handling"]
    if not isinstance(removed, str):
        removed = json.dumps(removed, ensure_ascii=False)
    if not isinstance(added, str):
        added = json.dumps(added, ensure_ascii=False)
    evidence = item.get(
        "controlling_evidence",
        item.get("finding", "The bounded frozen-source audit controls this correction."),
    )
    evidence_hash = sha256_text(evidence)
    authority = {
        "authority_id": f"{decision_id}-SOURCE-CONTROL",
        "citation": f"Open Logic frozen source {SOURCE_REVISION}",
        "passage_id": f"{decision_id}-SOURCE-CONTROL",
        "locator": item["source_locator"],
        "source_sha256": occurrences[0]["source"]["file_sha256"],
        "passage_sha256": evidence_hash,
        "status": "checked_supports",
        "note": evidence,
    }
    question = (
        f"Please double-check whether {decision_id} is fully repaired by the "
        "listed Gujarati handling without changing an unaffected claim or formula."
    )
    return {
        "decision_id": decision_id,
        "record_kind": "source_correction",
        "recording_mode": "contemporaneous",
        "recorded_utc": receipt.get("recorded_at_utc"),
        "edition": EDITION,
        "source_term_or_construction": removed,
        "intended_sense": item.get("finding", item["classification"].replace("_", " ")),
        "chosen_rendering": added,
        "rationale": (item["handling"] + " " + evidence).strip(),
        "authorities_checked": [authority],
        "alternatives": [
            {
                "rendering": "Literal preservation of the defective source",
                "disposition": "rejected",
                "reason": "It would reproduce the identified defect in Gujarati.",
            },
            {
                "rendering": "Silent correction",
                "disposition": "rejected",
                "reason": "It would make the inherited source defect untraceable.",
            },
            {
                "rendering": "Corrected body with an adjacent keyed disclosure",
                "disposition": "viable_alternative",
                "reason": "Adopted because it restores the intended claim and preserves auditability.",
            },
        ],
        "confidence": "high",
        "confidence_reason": "The frozen source, local formal context, corrected body, and adjacent disclosure were compared directly.",
        "provisional": False,
        "review_priority": "normal",
        "expert_review_useful": True,
        "expert_review_reason": "Independent mathematical and editorial review remains useful for every deliberate source correction.",
        "please_double_check_question": question,
        "occurrences": occurrences,
    }


def scope_decisions(
    passages: dict[str, dict[str, Any]],
    canon_sources: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    source_path = "upstream/content/sets-functions-relations/sets/basics.tex"
    target_path = "gu/content/sets-functions-relations/sets/basics.tex"
    base_occurrence = {
        "unit_id": "OLP-0005",
        "semantic_unit_id": "OLP-0005:B0004",
        "source": text_locator(
            source_path,
            12,
            "English textbook prose and mathematical notation",
            "Edition-wide script, register, and notation profile.",
            "Representative prose-and-formula paragraph.",
        ),
        "target": text_locator(
            target_path,
            12,
            "ગુજરાતી શૈક્ષણિક ગદ્ય અને આંતરરાષ્ટ્રીય ગણિતીય સંજ્ઞા",
            "Edition-wide script, register, and notation profile.",
            "Representative prose-and-formula paragraph.",
        ),
        "reader_locator": {},
    }
    base_occurrence["evidence_refs"] = [
        {
            "path_or_uri": base_occurrence["source"]["path"],
            "bytes": repo_path(base_occurrence["source"]["path"]).stat().st_size,
            "sha256": base_occurrence["source"]["file_sha256"],
            "version_or_ref": SOURCE_REVISION,
        },
        {
            "path_or_uri": base_occurrence["target"]["path"],
            "bytes": repo_path(base_occurrence["target"]["path"]).stat().st_size,
            "sha256": base_occurrence["target"]["file_sha256"],
        },
        {
            "path_or_uri": "docs/GUJARATI_EDITION_SCOPE.md",
            "bytes": (ROOT / "docs" / "GUJARATI_EDITION_SCOPE.md").stat().st_size,
            "sha256": sha256_path(ROOT / "docs" / "GUJARATI_EDITION_SCOPE.md"),
        },
    ]

    specifications = [
        (
            "GU-SCRIPT-001",
            "script",
            "English Latin-script prose",
            "ગુજરાતી લિપિ (Unicode NFC)",
            "Use the standard Gujarati script, store authored text in Unicode NFC, and keep the edition left to right.",
            ["GU-P001"],
        ),
        (
            "GU-REGISTER-001",
            "register",
            "Open Logic educational and scholarly exposition",
            "સમકાલીન શૈક્ષણિક અને શાસ્ત્રીય ગુજરાતી",
            "Use clear contemporary Gujarati suitable for a logic textbook, informed by inspected school mathematics and scholarly encyclopaedic prose.",
            ["GU-P076", "GU-P077"],
        ),
        (
            "GU-NOTATION-001",
            "notation",
            "Latin and Greek variables, logical signs, and Arabic digits in formulas",
            "આંતરરાષ્ટ્રીય ગણિતીય સંજ્ઞા; ગુજરાતી ગદ્યમાં ગુજરાતી અંકો સ્વીકાર્ય",
            "Preserve the source's international mathematical notation while allowing Gujarati digits in prose and reader-interface counts.",
            ["GU-P001"],
        ),
    ]
    output = []
    for decision_id, kind, source_term, chosen, rationale, passage_ids in specifications:
        occurrence = json.loads(json.dumps(base_occurrence, ensure_ascii=False))
        occurrence["occurrence_id"] = f"{decision_id}-O001"
        output.append(
            {
                "decision_id": decision_id,
                "record_kind": kind,
                "recording_mode": "derived",
                "edition": EDITION,
                "source_term_or_construction": source_term,
                "intended_sense": rationale,
                "chosen_rendering": chosen,
                "rationale": rationale,
                "authorities_checked": [
                    authority_from_passage(
                        passages[passage_id], canon_sources, supports=True
                    )
                    for passage_id in passage_ids
                ],
                "alternatives": [],
                "confidence": "high",
                "confidence_reason": "The selected layer follows the encoded language tag, inspected Gujarati publications, and the edition's verified text and formula practice.",
                "provisional": False,
                "review_priority": "low",
                "expert_review_useful": False,
                "expert_review_reason": None,
                "please_double_check_question": None,
                "occurrences": [occurrence],
            }
        )
    return output


def gujarati_words(text: str) -> set[str]:
    return {
        word
        for word in re.findall(r"[\u0A80-\u0AFF]+", text)
        if len(word) >= 2
    }


def unique_token_aligned_line(
    body_lines: list[str],
    start: int,
    end: int,
    target_lines: list[str],
    target_line: int,
) -> tuple[int, str] | None:
    exact = target_lines[target_line - 1].strip()
    exact_matches = [
        index + 1
        for index in range(start, end)
        if exact and body_lines[index].strip() == exact
    ]
    if len(exact_matches) == 1:
        return exact_matches[0], "exact assembled target line"

    exact_words = gujarati_words(target_lines[target_line - 1])
    frequencies = {
        word: sum(
            word in gujarati_words(body_lines[index])
            for index in range(start, end)
        )
        for word in exact_words
    }
    usable = sorted(
        (word for word in exact_words if frequencies[word] > 0),
        key=lambda word: (frequencies[word], -len(word), word),
    )
    candidates = set(range(start, end))
    used: list[str] = []
    for word in usable:
        candidates &= {
            index
            for index in range(start, end)
            if word in gujarati_words(body_lines[index])
        }
        used.append(word)
        if len(candidates) == 1 and (
            len(used) >= 2 or sum(len(item) for item in used) >= 6
        ):
            return (
                next(iter(candidates)) + 1,
                "unique exact-line Gujarati-token intersection",
            )
        if not candidates:
            break

    window_start = max(0, target_line - 2)
    window_end = min(len(target_lines), target_line + 1)
    words = gujarati_words("\n".join(target_lines[window_start:window_end]))
    if len(words) < 2:
        return None
    scored = []
    for index in range(start, end):
        body_window = "\n".join(
            body_lines[max(start, index - 1) : min(end, index + 2)]
        )
        overlap = len(words & gujarati_words(body_window))
        coverage = overlap / len(words)
        if overlap >= 2 and coverage >= 0.5:
            scored.append((overlap, coverage, index + 1))
    if not scored:
        return None
    scored.sort(reverse=True)
    best = scored[0]
    if len(scored) > 1 and scored[1][:2] == best[:2]:
        return None
    return best[2], "unique Gujarati-token window alignment"


def find_body_line(target: dict[str, Any], decision_id: str) -> tuple[int, str] | None:
    if not BODY_PATH.exists():
        return None
    body_lines = BODY_PATH.read_text(encoding="utf-8").splitlines()
    target_path = repo_path(target["path"])
    target_lines = target_path.read_text(encoding="utf-8").splitlines()
    if decision_id.startswith(("OLFUN-", "OLSIZ-", "OLARI-", "OLINF-", "OLPL-", "OLPRF-", "OLSEQ-", "OLND-")):
        note = r"\sourcecorrection{" + decision_id + "}"
        matches = [
            index + 1
            for index, line in enumerate(body_lines)
            if note in line
        ]
        if len(matches) == 1:
            return matches[0], "exact adjacent source-correction disclosure marker"

    marker_matches = re.findall(
        r"\\olfileid\{[^}]+\}\{[^}]+\}\{[^}]+\}",
        target_path.read_text(encoding="utf-8"),
    )
    target_line = target["line_span"]["start"]
    marker_ranges = []
    for marker in set(marker_matches):
        starts = [
            index for index, line in enumerate(body_lines) if marker in line
        ]
        if len(starts) == 1:
            start = starts[0]
            end = next(
                (
                    index
                    for index in range(start + 1, len(body_lines))
                    if r"\olfileid{" in body_lines[index]
                ),
                len(body_lines),
            )
            marker_ranges.append((start, end))
    if len(marker_ranges) == 1:
        aligned = unique_token_aligned_line(
            body_lines,
            marker_ranges[0][0],
            marker_ranges[0][1],
            target_lines,
            target_line,
        )
        if aligned:
            return aligned

    raw_line = target_lines[target_line - 1]
    title_match = re.search(r"\{([\u0A80-\u0AFF][^{}]*)\}\s*$", raw_line)
    if title_match:
        title = title_match.group(1)
        title_matches = [
            index + 1
            for index, line in enumerate(body_lines)
            if title in line and re.search(r"\\(?:part|chapter|section)\{", line)
        ]
        if len(title_matches) == 1:
            return title_matches[0], "unique transformed Gujarati driver title"

    return unique_token_aligned_line(
        body_lines,
        0,
        len(body_lines),
        target_lines,
        target_line,
    )


def synctex_page(body_line: int) -> int | None:
    command = [
        "synctex",
        "view",
        "-i",
        f"{body_line}:1:build/natural-deduction-body.tex",
        "-o",
        "build/gu-natural-deduction.pdf",
    ]
    completed = subprocess.run(
        command,
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    match = re.search(r"^Page:(\d+)$", completed.stdout, re.MULTILINE)
    return int(match.group(1)) if match else None


def attach_reader_locators(decisions: list[dict[str, Any]]) -> dict[str, int]:
    receipt = (
        json.loads(BUILD_RECEIPT_PATH.read_text(encoding="utf-8"))
        if BUILD_RECEIPT_PATH.exists()
        else {}
    )
    pdf_ready = (
        PDF_PATH.exists()
        and SYNCTEX_PATH.exists()
        and receipt.get("status") == "passed"
    )
    pdf_hash = sha256_path(PDF_PATH) if pdf_ready else None
    cache: dict[int, int | None] = {}
    counts = {"available": 0, "pending": 0, "not_applicable": 0}
    for decision in decisions:
        for occurrence in decision["occurrences"]:
            target_path = occurrence["target"]["path"]
            target_line = occurrence["target"]["line_span"]["start"]
            intentionally_unrendered = (
                target_path
                == "gu/content/propositional-logic/propositional-logic.tex"
                and 9 <= target_line <= 20
            )
            if intentionally_unrendered:
                occurrence["reader_locator"] = {
                    "status": "not_applicable",
                    "reason": "This occurrence is in a translated driver editorial that the cumulative reader intentionally omits; there is no assembled reader page for it.",
                }
                counts["not_applicable"] += 1
                continue
            alignment = (
                find_body_line(
                    occurrence["target"],
                    decision["decision_id"],
                )
                if pdf_ready
                else None
            )
            if alignment:
                body_line, method = alignment
                if body_line not in cache:
                    cache[body_line] = synctex_page(body_line)
                page = cache[body_line]
            else:
                body_line = None
                method = ""
                page = None
            if page is not None:
                occurrence["reader_locator"] = {
                    "status": "available",
                    "artifact_filename": PDF_PATH.name,
                    "artifact_sha256": pdf_hash,
                    "profile": "cumulative Gujarati reader through OLP-0097; classical first-order natural deduction",
                    "printed_page": None,
                    "assembled_pdf_page": page,
                    "provenance": (
                        f"SyncTeX forward query at build/natural-deduction-body.tex:{body_line}; "
                        f"target mapping method: {method}. Printed page was not inferred."
                    ),
                }
                counts["available"] += 1
            else:
                reason = (
                    "Guarded cumulative PDF and SyncTeX artifacts are not both available."
                    if not pdf_ready
                    else "No unique deterministic target-to-assembled-body line and SyncTeX page were both established; the page is deliberately not guessed."
                )
                occurrence["reader_locator"] = {
                    "status": "pending",
                    "reason": reason,
                }
                counts["pending"] += 1
    return counts


def markdown_full(decisions: list[dict[str, Any]], generated: str) -> str:
    lines = [
        "# Full Gujarati translation-decision register",
        "",
        f"Generated {generated}. This register covers all {len(decisions)} material decisions recorded for the current 94/722-unit working edition. Each occurrence has exact source and Gujarati line and UTF-8 byte evidence. Reader pages are reported only when deterministic alignment and SyncTeX agree; unresolved pages remain explicitly pending.",
        "",
    ]
    for decision in decisions:
        lines.extend(
            [
                f"## {decision['decision_id']}: {decision['source_term_or_construction']} → {decision['chosen_rendering']}",
                "",
                f"- **Kind / mode:** {decision['record_kind']} / {decision['recording_mode']}",
                f"- **Confidence / priority:** {decision['confidence']} / {decision['review_priority']}; provisional: {str(decision['provisional']).lower()}",
                f"- **Intended sense:** {decision['intended_sense']}",
                f"- **Rationale:** {decision['rationale']}",
                f"- **Authority:** "
                + "; ".join(
                    f"{authority['authority_id']} ({authority['status']})"
                    for authority in decision["authorities_checked"]
                ),
            ]
        )
        if decision["alternatives"]:
            lines.append(
                "- **Alternatives:** "
                + "; ".join(
                    f"{alternative['rendering']} [{alternative['disposition']}] — {alternative['reason']}"
                    for alternative in decision["alternatives"]
                )
            )
        if decision["please_double_check_question"]:
            lines.append(
                f"- **Please double-check:** {decision['please_double_check_question']}"
            )
        lines.extend(["", "Occurrences:", ""])
        for occurrence in decision["occurrences"]:
            source_line = occurrence["source"]["line_span"]["start"]
            target_line = occurrence["target"]["line_span"]["start"]
            reader = occurrence["reader_locator"]
            reader_text = (
                f"{reader['artifact_filename']} assembled page {reader['assembled_pdf_page']}"
                if reader["status"] == "available"
                else f"{reader['status']}: {reader['reason']}"
            )
            lines.append(
                f"- {BT}{occurrence['occurrence_id']}{BT} / {BT}{occurrence['semantic_unit_id']}{BT}: "
                f"{BT}{occurrence['source']['path']}:{source_line}{BT} → "
                f"{BT}{occurrence['target']['path']}:{target_line}{BT}; reader {reader_text}."
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def markdown_priority(decisions: list[dict[str, Any]], generated: str) -> str:
    selected = [
        decision
        for decision in decisions
        if decision["review_priority"] in {"urgent", "high"}
    ]
    lines = [
        "# Priority Gujarati review",
        "",
        f"Generated {generated}. This focused queue contains {len(selected)} high-priority decisions from the complete register. Review can proceed asynchronously from the exact source and target locators.",
        "",
    ]
    if not selected:
        lines.append("No urgent or high-priority decision is currently open.")
    for decision in selected:
        occurrence = decision["occurrences"][0]
        question = decision["please_double_check_question"] or (
            f"Please double-check whether {decision['chosen_rendering']} is the appropriate Gujarati rendering for {decision['source_term_or_construction']} in the stated sense."
        )
        lines.extend(
            [
                f"## {decision['decision_id']}: {decision['source_term_or_construction']} → {decision['chosen_rendering']}",
                "",
                f"- **Why prioritized:** {decision['confidence_reason']}",
                f"- **Question:** {question}",
                f"- **Source:** {BT}{occurrence['source']['path']}:{occurrence['source']['line_span']['start']}{BT}",
                f"- **Gujarati:** {BT}{occurrence['target']['path']}:{occurrence['target']['line_span']['start']}{BT}",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def markdown_start(
    decisions: list[dict[str, Any]],
    occurrence_count: int,
    reader_counts: dict[str, int],
) -> str:
    priority_count = sum(
        decision["review_priority"] in {"urgent", "high"} for decision in decisions
    )
    return f"""# Start here: Gujarati translation decisions

This directory is the review entry point for the current 94/722-unit Gujarati
working edition.

- {BT}DECISIONS.json{BT} is the canonical schema-valid register.
- {BT}TRANSLATION_DECISIONS_FULL.md{BT} presents all {len(decisions)} decisions in readable form.
- {BT}PRIORITY_REVIEW.md{BT} isolates {priority_count} urgent or high-priority items.
- {BT}DECISION_OCCURRENCES.csv{BT} flattens all {occurrence_count} exact source/target occurrence records.
- {BT}TRANSLATION_DECISION_QA.json{BT} records schema, hash, locator, and cross-surface checks.
- {BT}translation-decision.schema.json{BT} is the frozen normative schema.
- {BT}../GUJARATI_EDITION_SCOPE.md{BT} states the script, register, notation, and variant policy.

Reader locations currently include {reader_counts['available']} verified PDF
pages and {reader_counts['pending']} explicitly pending pages. A pending page is
never an inferred or estimated page.
"""


def write_occurrences_csv(decisions: list[dict[str, Any]], path: Path) -> int:
    fieldnames = [
        "decision_id",
        "record_kind",
        "review_priority",
        "provisional",
        "source_term_or_construction",
        "chosen_rendering",
        "occurrence_id",
        "unit_id",
        "semantic_unit_id",
        "source_path",
        "source_line_start",
        "source_line_end",
        "source_byte_start",
        "source_byte_end_exclusive",
        "source_excerpt",
        "target_path",
        "target_line_start",
        "target_line_end",
        "target_byte_start",
        "target_byte_end_exclusive",
        "target_excerpt",
        "reader_status",
        "reader_artifact",
        "reader_assembled_pdf_page",
        "reader_reason_or_provenance",
    ]
    count = 0
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for decision in decisions:
            for occurrence in decision["occurrences"]:
                reader = occurrence["reader_locator"]
                writer.writerow(
                    {
                        "decision_id": decision["decision_id"],
                        "record_kind": decision["record_kind"],
                        "review_priority": decision["review_priority"],
                        "provisional": str(decision["provisional"]).lower(),
                        "source_term_or_construction": decision[
                            "source_term_or_construction"
                        ],
                        "chosen_rendering": decision["chosen_rendering"],
                        "occurrence_id": occurrence["occurrence_id"],
                        "unit_id": occurrence["unit_id"],
                        "semantic_unit_id": occurrence["semantic_unit_id"],
                        "source_path": occurrence["source"]["path"],
                        "source_line_start": occurrence["source"]["line_span"]["start"],
                        "source_line_end": occurrence["source"]["line_span"]["end"],
                        "source_byte_start": occurrence["source"]["byte_span"]["start"],
                        "source_byte_end_exclusive": occurrence["source"]["byte_span"][
                            "end_exclusive"
                        ],
                        "source_excerpt": occurrence["source"]["excerpt"],
                        "target_path": occurrence["target"]["path"],
                        "target_line_start": occurrence["target"]["line_span"]["start"],
                        "target_line_end": occurrence["target"]["line_span"]["end"],
                        "target_byte_start": occurrence["target"]["byte_span"]["start"],
                        "target_byte_end_exclusive": occurrence["target"]["byte_span"][
                            "end_exclusive"
                        ],
                        "target_excerpt": occurrence["target"]["excerpt"],
                        "reader_status": reader["status"],
                        "reader_artifact": reader.get("artifact_filename", ""),
                        "reader_assembled_pdf_page": reader.get(
                            "assembled_pdf_page", ""
                        ),
                        "reader_reason_or_provenance": reader.get(
                            "provenance", reader.get("reason", "")
                        ),
                    }
                )
                count += 1
    return count


def validate_locator(locator: dict[str, Any]) -> None:
    path = repo_path(locator["path"])
    raw = path.read_bytes()
    assert sha256_path(path) == locator["file_sha256"]
    start = locator["byte_span"]["start"]
    end = locator["byte_span"]["end_exclusive"]
    assert raw[start:end].decode("utf-8") == locator["excerpt"]
    line_start = locator["line_span"]["start"]
    line_end = locator["line_span"]["end"]
    assert line_start == line_end
    expected_start, expected_end, expected_excerpt = line_bounds(raw, line_start)
    assert (start, end, locator["excerpt"]) == (
        expected_start,
        expected_end,
        expected_excerpt,
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    assert SCHEMA_PATH.exists()
    assert SCHEMA_PATH.stat().st_size == 10787
    assert sha256_path(SCHEMA_PATH) == (
        "50e7fa407b62c711f92f8b93be591d3b4a6e1c4adb1386c398bb5f76844d9f90"
    )

    terms = read_jsonl(STATE / "TERM_DECISIONS.jsonl")
    passages = {
        item["passage_id"]: item
        for item in read_jsonl(STATE / "CANON_PASSAGES.jsonl")
    }
    canon_sources = {
        item["source_id"]: item
        for item in read_jsonl(STATE / "CANON_SOURCES.jsonl")
    }
    assert len(terms) == 123
    assert len(passages) == 77

    decisions = [
        term_decision(term, passages, canon_sources) for term in terms
    ]
    correction_receipts = sorted(STATE.glob("SOURCE_CORRECTIONS_*.json"))
    correction_count = 0
    for receipt_path in correction_receipts:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        assert receipt["source_revision"] == SOURCE_REVISION
        for item in receipt["corrections"]:
            decisions.append(correction_decision(receipt_path, receipt, item))
            correction_count += 1
    assert correction_count == 41
    decisions.extend(scope_decisions(passages, canon_sources))

    reader_counts = attach_reader_locators(decisions)
    generated = datetime.now(timezone.utc).isoformat()
    payload = {
        "schema_version": "openlogic-translation-decisions/1.0.0",
        "edition_release": {
            "edition": EDITION,
            "release_tag": None,
            "repository": "https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN",
            "doi": None,
            "source_revision": SOURCE_REVISION,
            "coverage_state": "partial",
            "source_units": 94,
            "reader_units": (
                94
                if BUILD_RECEIPT_PATH.exists()
                and json.loads(BUILD_RECEIPT_PATH.read_text(encoding="utf-8")).get(
                    "status"
                )
                == "passed"
                else None
            ),
        },
        "generated_utc": generated,
        "decisions": decisions,
    }
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(payload), key=lambda error: list(error.path))
    if errors:
        formatted = "\n".join(
            f"{list(error.path)}: {error.message}" for error in errors[:20]
        )
        raise AssertionError("Schema errors:\n" + formatted)

    decision_ids = [decision["decision_id"] for decision in decisions]
    assert len(decision_ids) == len(set(decision_ids))
    occurrence_ids = [
        occurrence["occurrence_id"]
        for decision in decisions
        for occurrence in decision["occurrences"]
    ]
    assert len(occurrence_ids) == len(set(occurrence_ids))
    for decision in decisions:
        assert not re.search(r"[\u0900-\u097F]", decision["chosen_rendering"])
        for occurrence in decision["occurrences"]:
            validate_locator(occurrence["source"])
            validate_locator(occurrence["target"])

    decisions_path = OUT / "DECISIONS.json"
    decisions_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    full_path = OUT / "TRANSLATION_DECISIONS_FULL.md"
    full_text = markdown_full(decisions, generated)
    full_path.write_text(full_text, encoding="utf-8", newline="\n")
    priority_path = OUT / "PRIORITY_REVIEW.md"
    priority_text = markdown_priority(decisions, generated)
    priority_path.write_text(priority_text, encoding="utf-8", newline="\n")
    csv_path = OUT / "DECISION_OCCURRENCES.csv"
    occurrence_count = write_occurrences_csv(decisions, csv_path)
    start_path = OUT / "START_HERE.md"
    start_path.write_text(
        markdown_start(decisions, occurrence_count, reader_counts),
        encoding="utf-8",
        newline="\n",
    )

    with csv_path.open(encoding="utf-8", newline="") as handle:
        csv_rows = list(csv.DictReader(handle))
    assert len(csv_rows) == occurrence_count
    assert {row["occurrence_id"] for row in csv_rows} == set(occurrence_ids)
    assert all(
        f"## {decision_id}:" in full_text
        for decision_id in decision_ids
    )
    high_ids = {
        decision["decision_id"]
        for decision in decisions
        if decision["review_priority"] in {"urgent", "high"}
    }
    assert high_ids == {
        decision_id
        for decision_id in decision_ids
        if f"## {decision_id}:" in priority_text
    }

    qa = {
        "schema": "openlogic-gu-translation-decision-qa/1",
        "generated_utc": generated,
        "status": "passed",
        "normative_schema": {
            "path": rel(SCHEMA_PATH),
            "bytes": SCHEMA_PATH.stat().st_size,
            "sha256": sha256_path(SCHEMA_PATH),
            "upstream_revision": "811091d54be4989918864732073279a588340e6f",
        },
        "coverage": {
            "source_units": 94,
            "total_source_units": 722,
            "term_decisions": len(terms),
            "source_correction_decisions": correction_count,
            "edition_scope_decisions": 3,
            "all_decisions": len(decisions),
            "occurrences": occurrence_count,
        },
        "checks": {
            "json_schema_valid": True,
            "unique_decision_ids": True,
            "unique_occurrence_ids": True,
            "all_source_and_target_line_byte_spans_exact": True,
            "all_locator_file_hashes_exact": True,
            "all_decisions_have_checked_authority": True,
            "all_decisions_have_occurrences": True,
            "csv_matches_json_occurrences": True,
            "full_markdown_contains_every_decision": True,
            "priority_markdown_matches_high_priority_set": True,
            "chosen_renderings_have_no_devanagari": True,
            "unknown_reader_pages_are_explicitly_pending": True,
        },
        "reader_locators": reader_counts,
        "reader_locator_policy": "Available only after a unique deterministic target-to-assembled-body alignment and successful SyncTeX forward query. Printed-page fields remain null unless independently established. Pending pages are never guessed.",
        "input_artifacts": {
            "TERM_DECISIONS.jsonl": {
                "bytes": (STATE / "TERM_DECISIONS.jsonl").stat().st_size,
                "sha256": sha256_path(STATE / "TERM_DECISIONS.jsonl"),
            },
            "CANON_PASSAGES.jsonl": {
                "bytes": (STATE / "CANON_PASSAGES.jsonl").stat().st_size,
                "sha256": sha256_path(STATE / "CANON_PASSAGES.jsonl"),
            },
            "GUJARATI_EDITION_SCOPE.md": {
                "bytes": (ROOT / "docs" / "GUJARATI_EDITION_SCOPE.md").stat().st_size,
                "sha256": sha256_path(ROOT / "docs" / "GUJARATI_EDITION_SCOPE.md"),
            },
        },
        "release_surfaces": {
            path.name: {
                "bytes": path.stat().st_size,
                "sha256": sha256_path(path),
            }
            for path in (
                start_path,
                full_path,
                priority_path,
                csv_path,
                decisions_path,
                SCHEMA_PATH,
            )
        },
    }
    qa_path = OUT / "TRANSLATION_DECISION_QA.json"
    qa_path.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(
        json.dumps(
            {
                "decisions": len(decisions),
                "occurrences": occurrence_count,
                "reader_locators": reader_counts,
                "schema_valid": True,
                "qa_sha256": sha256_path(qa_path),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
