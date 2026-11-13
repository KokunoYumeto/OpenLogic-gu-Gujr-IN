"""Use vector derivatives only with their exact editable diagram sources.

Changed diagrams or shared definitions require fresh vector export. This tool
does not silently reuse an illustration after its TeX definitions change.
"""
from pathlib import Path
from bisect import bisect_right
import hashlib
import json
import re
import shutil
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PDF_SHA = None  # Converter receipt compatibility; no old PDF is required.


def sha(data):
    return hashlib.sha256(data).hexdigest()


def render_native_figures(text):
    manifest = json.loads((ROOT/'reader/figures/native/sources.json').read_text(encoding='utf-8'))
    assert manifest['schema'] == 'openlogic-gu-native-vector-sources/1'
    current = (ROOT/'reader/full-reader.tex').read_text(encoding='utf-8')
    preamble = current.split(r'\begin{document}', 1)[0]
    assert sha(preamble.encode('utf-8')) == manifest['preamble_sha256'], 'Diagram definitions changed; export the vectors again.'
    actual = {p.relative_to(ROOT).as_posix()
              for directory in ('upstream/sty', 'upstream/include')
              for p in (ROOT/directory).rglob('*') if p.is_file()}
    assert actual == {row['path'] for row in manifest['dependencies']}
    for row in manifest['dependencies']:
        assert sha((ROOT/row['path']).read_bytes()) == row['sha256'], row['path']
    markers = list(re.finditer(r'(?m)^% BEGIN (OLP-\d{4})$', text))
    positions = [marker.start() for marker in markers]
    assert markers
    rows = manifest['figures']
    assert len(rows) == 43 and len({row['index'] for row in rows}) == 43
    used, receipts, descriptions = set(), [], {}
    def convert(match):
        unit_index = bisect_right(positions, match.start()) - 1
        assert unit_index >= 0
        unit = markers[unit_index][1]
        diagram_sha = sha(match[0].encode('utf-8'))
        found = [row for row in rows if row['unit'] == unit
                 and row['source_sha256'] == diagram_sha and row['index'] not in used]
        if not found:
            return match[0]
        assert len(found) == 1
        row = found[0];used.add(row['index'])
        source = ROOT/row['asset']
        assert source.resolve().is_relative_to((ROOT/'reader/figures/native').resolve())
        data = source.read_bytes();assert sha(data) == row['svg_sha256']
        tree = ET.fromstring(data)
        assert not tree.findall('.//{http://www.w3.org/2000/svg}image')
        target = ROOT/'build/full-epub-media/assets'/source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
        descriptions[target.stem] = row['description_gu']
        receipts.append({'index':row['index'],'unit':unit,'source_sha256':diagram_sha,
                         'svg_path':target.relative_to(ROOT).as_posix(),'svg_sha256':row['svg_sha256'],
                         'source_match':'exact_current_editable_diagram_and_shared_definitions'})
        return r'\includegraphics{'+target.relative_to(ROOT).as_posix()+'}'
    text = re.sub(r'\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}', convert, text)
    assert len(used) == len(rows), 'A retained vector has no matching current editable diagram.'
    return text, receipts, descriptions
