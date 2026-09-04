"""Reproduce the cumulative Gujarati Sets chapter from aligned editable sources.
Does not run TeX. Unmodified source files remain independently auditable.
"""
from pathlib import Path
import re, json, hashlib
R=Path(__file__).resolve().parents[1]
B=R/"build"; B.mkdir(exist_ok=True)
names=["basics","subsets","important-sets","unions-and-intersections","pairs-and-products","russells-paradox"]
receipts=[]; bodies=[]
for n in names:
    p=R/"gu"/"content"/"sets-functions-relations"/"sets"/f"{n}.tex"
    text=p.read_text(encoding="utf-8")
    body=text.split(r"\begin{document}",1)[1].rsplit(r"\end{document}",1)[0]
    # English article/plural machinery has no English surface text in the Gujarati reader.
    body=re.sub(r"!!\^?a?\{element\}(s?)",lambda m:"ઘટકો" if m[1] else "ઘટક",body)
    bodies.append(body)
    receipts.append({"path":str(p.relative_to(R)).replace("\\","/"),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
(B/"sets-body.tex").write_text("\n".join(bodies),encoding="utf-8")
(B/"input-hashes.json").write_text(json.dumps(receipts,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"prepared_sections":len(bodies),"translation_inputs":receipts}))

