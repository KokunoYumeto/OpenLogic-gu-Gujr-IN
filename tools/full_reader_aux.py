"""Select reference numbers only from a successful build of this exact reader."""
from pathlib import Path
import hashlib
import json
import re


def current_aux(root):
    root = Path(root)
    reader_sha = hashlib.sha256((root/'reader/full-reader.tex').read_bytes()).hexdigest()
    candidates = []
    for path in (root/'build').glob('*/FULL_READER_BUILD.json'):
        record = json.loads(path.read_text(encoding='utf-8-sig'))
        if record.get('input', {}).get('sha256') != reader_sha:
            continue
        if record.get('status') != 'three_lualatex_passes_succeeded_visual_QA_pending':
            continue
        assert record.get('ended_at_utc'), path
        job = record['job_name']
        assert re.fullmatch(r'gu-[a-z0-9-]+', job), job
        aux = path.parent/(job+'.aux')
        pdf = path.parent/(job+'.pdf')
        assert aux.is_file() and pdf.is_file(), path
        assert hashlib.sha256(pdf.read_bytes()).hexdigest() == record['pdf']['sha256'], path
        dependency = record.get('reader_layout_dependency')
        if dependency:
            assert hashlib.sha256((root/'reader/gu-reader-layout.tex').read_bytes()).hexdigest() == dependency['sha256'], path
        candidates.append((record['ended_at_utc'], aux, path, record))
    if not candidates:
        raise RuntimeError('Build the current reader successfully before converting its EPUB references.')
    _, aux, receipt, record = max(candidates, key=lambda item: item[0])
    return aux, {
        'path': aux.relative_to(root).as_posix(),
        'sha256': hashlib.sha256(aux.read_bytes()).hexdigest(),
        'build_receipt': receipt.relative_to(root).as_posix(),
        'reader_sha256': reader_sha,
        'pdf_sha256': record['pdf']['sha256'],
        'scope': 'Theorem and figure numbers from the successful current-source PDF build.'
    }
