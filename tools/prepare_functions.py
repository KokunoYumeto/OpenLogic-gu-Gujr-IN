"""Prepare the cumulative three-chapter reader; no TeX process is launched."""
from pathlib import Path
import re,json,hashlib,runpy
R=Path(__file__).resolve().parents[1];B=R/'build'
runpy.run_path(str(R/'tools/prepare_foundations.py'))
body=(B/'foundations-body.tex').read_text(encoding='utf-8')
receipts=json.loads((B/'foundations-input-hashes.json').read_text())
names=['function-basics','function-kinds','functions-relations','inverses','composition','partial-functions']
tokens={'element':('ઘટક','ઘટકો'),'surjective':('વ્યાપ્ત','વ્યાપ્ત'),'surjection':('વ્યાપ્ત વિધેય','વ્યાપ્ત વિધેયો'),'injective':('એક-એક','એક-એક'),'injection':('એક-એક વિધેય','એક-એક વિધેયો'),'bijective':('એક-એક અને વ્યાપ્ત','એક-એક અને વ્યાપ્ત'),'bijection':('એક-એક વ્યાપ્ત વિધેય','એક-એક વ્યાપ્ત વિધેયો')}
body+='\n\\part{વિધેયો}\n'
for n in names:
    path=R/'gu/content/sets-functions-relations/functions'/f'{n}.tex'
    text=path.read_text(encoding='utf-8').split(r'\begin{document}',1)[1].rsplit(r'\end{document}',1)[0]
    text=re.sub(r'!!\^?a?\{([^}]+)\}(s?)',lambda m:tokens[m[1]][bool(m[2])],text)
    assert '!!' not in text
    body+=text+'\n'
    receipts.append(dict(path=path.relative_to(R).as_posix(),sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
# Freeze conditional availability from actual included units, independently of prior aux files.
keys=set()
for block in re.split(r'(?=\\olfileid)',body):
    m=re.search(r'\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}',block)
    if m:
        prefix=':'.join(m.groups());keys.add(prefix+':sec')
        for label in re.findall(r'\\ollabel\{([^}]+)\}',block):keys.add(prefix+':'+label)
(B/'functions-body.tex').write_text(body,encoding='utf-8')
(B/'functions-available-labels.tex').write_text('\n'.join(r'\expandafter\def\csname guavailable@'+k+r'\endcsname{1}' for k in sorted(keys))+'\n',encoding='utf-8')
(B/'functions-available-labels.json').write_text(json.dumps(sorted(keys),indent=2)+'\n',encoding='utf-8')
(B/'functions-input-hashes.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(sections=len(receipts),labels=len(keys),sha256=hashlib.sha256(body.encode()).hexdigest())))
