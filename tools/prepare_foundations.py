"""Prepare the cumulative Gujarati Sets and Relations reader, without launching TeX."""
from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parents[1]
B=R/'build'; B.mkdir(exist_ok=True)
preamble=(R/'gu-sets.tex').read_text(encoding='utf-8').split(r'\begin{document}',1)[0]
(B/'foundations-preamble.tex').write_text(preamble,encoding='utf-8')
chapters=[
 ('sets','ગણો',['basics','subsets','important-sets','unions-and-intersections','pairs-and-products','russells-paradox']),
 ('relations','સંબંધો',['relations-as-sets','reflections','special-properties','equivalence-relations','orders','graphs','trees','operations'])
]
tokens={'element':('ઘટક','ઘટકો'),'formula':('સૂત્ર','સૂત્રો'),'derivation':('નિષ્પત્તિ','નિષ્પત્તિઓ')}
bodies=[];receipts=[]
for dirname,title,names in chapters:
    bodies.append('\\part{'+title+'}\n')
    for n in names:
        p=R/'gu/content/sets-functions-relations'/dirname/f'{n}.tex'
        text=p.read_text(encoding='utf-8')
        body=text.split(r'\begin{document}',1)[1].rsplit(r'\end{document}',1)[0]
        body=re.sub(r'!![\^a]?\{([^}]+)\}(s?)',lambda m:tokens[m[1]][bool(m[2])],body)
        assert '!!{' not in body
        bodies.append(body)
        receipts.append(dict(path=p.relative_to(R).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(B/'foundations-body.tex').write_text('\n'.join(bodies),encoding='utf-8')
(B/'foundations-input-hashes.json').write_text(json.dumps(receipts,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(prepared_sections=len(receipts),sha256=hashlib.sha256((B/'foundations-body.tex').read_bytes()).hexdigest())))
