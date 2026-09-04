"""Prepare the cumulative Sets, Relations, Functions, and Size reader; no TeX process is launched."""
from pathlib import Path
import hashlib
import json
import re
import runpy

R = Path(__file__).resolve().parents[1]
B = R / 'build'
runpy.run_path(str(R / 'tools' / 'prepare_functions.py'))
body = (B / 'functions-body.tex').read_text(encoding='utf-8')
receipts = json.loads((B / 'functions-input-hashes.json').read_text(encoding='utf-8'))
names = [
    'introduction', 'enumerability', 'zig-zag', 'pairing', 'pairing-alt',
    'non-enumerability', 'reduction', 'equinumerous-sets', 'comparing-size',
    'schroder-bernstein', 'enumerability-alt', 'non-enumerability-alt',
    'reduction-alt',
]
tokens = {
    'element': ('ઘટક', 'ઘટકો'),
    'surjective': ('વ્યાપ્ત', 'વ્યાપ્ત'),
    'surjection': ('વ્યાપ્ત વિધેય', 'વ્યાપ્ત વિધેયો'),
    'injective': ('એક-એક', 'એક-એક'),
    'injection': ('એક-એક વિધેય', 'એક-એક વિધેયો'),
    'bijective': ('એક-એક અને વ્યાપ્ત', 'એક-એક અને વ્યાપ્ત'),
    'bijection': ('એક-એક વ્યાપ્ત વિધેય', 'એક-એક વ્યાપ્ત વિધેયો'),
    'enumerable': ('ગણનીય', 'ગણનીય'),
    'nonenumerable': ('અગણનીય', 'અગણનીય'),
}
body += '\n\\part{ગણોનું કદ}\n'
for name in names:
    path = R / 'gu' / 'content' / 'sets-functions-relations' / 'size-of-sets' / f'{name}.tex'
    text = path.read_text(encoding='utf-8').split(r'\begin{document}', 1)[1].rsplit(r'\end{document}', 1)[0]
    text = re.sub(r'!!\^?a?\{([^}]+)\}(s?)', lambda m: tokens[m[1]][bool(m[2])], text)
    assert '!!' not in text
    body += text + '\n'
    receipts.append({'path': path.relative_to(R).as_posix(), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})

# Freeze conditional availability from the exact cumulative body.
keys = set()
for block in re.split(r'(?=\\olfileid)', body):
    match = re.search(r'\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}', block)
    if not match:
        continue
    prefix = ':'.join(match.groups())
    keys.add(prefix + ':sec')
    for label in re.findall(r'\\ollabel\{([^}]+)\}', block):
        keys.add(prefix + ':' + label)
    for label in re.findall(r'\\label\{([^}]+)\}', block):
        keys.add(label)

(B / 'size-body.tex').write_text(body, encoding='utf-8')
(B / 'size-available-labels.tex').write_text(
    '\n'.join(r'\expandafter\def\csname guavailable@' + key + r'\endcsname{1}' for key in sorted(keys)) + '\n',
    encoding='utf-8')
(B / 'size-available-labels.json').write_text(json.dumps(sorted(keys), indent=2) + '\n', encoding='utf-8')
(B / 'size-input-hashes.json').write_text(json.dumps(receipts, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'rendered_sections': len(receipts), 'source_units_covered': 37,
                  'labels': len(keys), 'sha256': hashlib.sha256(body.encode()).hexdigest()}))
