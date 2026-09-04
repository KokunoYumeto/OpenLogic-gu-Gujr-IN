"""Build offline semantic HTML from the same aligned chapter sources; no TeX engine."""
from pathlib import Path
import re,json,subprocess,html,hashlib
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1]; B=R/"build"; O=R/"reader"; O.mkdir(exist_ok=True)
(O/"assets").mkdir(exist_ok=True)
def arg(t,i):
    while i<len(t) and t[i].isspace(): i+=1
    assert t[i]=="{",(t[i:i+100],i)
    depth=1;j=i+1
    while depth:
        if t[j]=="{" and t[j-1]!="\\":depth+=1
        if t[j]=="}" and t[j-1]!="\\":depth-=1
        j+=1
    return t[i+1:j-1],j
def command(t,name,n,callback):
    search=re.compile(r"\\"+name+r"(?![A-Za-z])")
    pos=0
    while (m:=search.search(t,pos)):
        vals=[];j=m.end()
        for _ in range(n): v,j=arg(t,j); vals.append(v)
        repl=callback(*vals);t=t[:m.start()]+repl+t[j:];pos=m.start()+len(repl)
    return t
colors={"oldiagcolorA":"#000000","oldiagcolorB":"#808080","oldiagcolorC":"#a81c21"}
for name in ["union","intersection","difference"]:
    t=(R/"upstream"/"assets"/"diagrams"/f"{name}.tikz").read_text()
    paths=[]
    for m in re.finditer(r"\\path\[([\s\S]*?)\]([\s\S]*?);",t):
        opt,data=m.groups()
        color=re.search(r"draw=(\w+)",opt)[1];width=float(re.search(r"width=([\d.]+)pt",opt)[1])/0.8
        data=re.sub(r"--\s*cycle.*"," Z",data)
        data=re.sub(r"\.\.\s*controls"," C",data);data=re.sub(r"\band\b","",data);data=data.replace(".."," ").replace("--"," L ")
        data=re.sub(r"\(([\d.-]+),([\d.-]+)\)",r"\1 \2 ",data).strip()
        paths.append(f'<path d="M {data}" fill="none" stroke="{colors[color]}" stroke-width="{width:g}" stroke-linejoin="miter"/>')
    assert paths
    (O/"assets"/f"{name}.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-4 -4 292 239" role="img">'+"".join(paths)+"</svg>",encoding="utf-8")
body=(B/"sets-body.tex").read_text(encoding="utf-8")
body=command(body,"oliflabeldef",3,lambda key,yes,no:no)
sections=re.split(r"(?=\\olfileid)",body)
labels={}; section_text=[]; figure_count=0
for block in sections:
    if not block.strip():continue
    ident=re.search(r"\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}",block)
    prefix=":".join(ident.groups());num=len(section_text)+1; count=0;probcount=0
    labels[prefix+":sec"]=str(num)
    block=command(block,"olfileid",3,lambda a,b,c:"")
    block=command(block,"olsection",1,lambda title:r"\section{"+title+r"}\label{"+prefix+":sec}")
    block=re.sub(r"\\begin\{tagblock\}\{[^}]+\}|\\end\{tagblock\}","",block)
    block=re.sub(r"\\(?:begin|end)\{(?:explain|digress)\}","",block)
    # In display order, compute counters used by the PDF adapter.
    pat=re.compile(r"\\begin\{(defn|ex|thm|prop|prob|proof)\}(?:\[([^\]]*)\])?(?:\\ollabel\{([^}]+)\})?")
    scanpos=0;out=""
    names={"defn":"વ્યાખ્યા","ex":"ઉદાહરણ","thm":"પ્રમેય","prop":"વિધાન","prob":"સ્વાધ્યાય","proof":"સાબિતી"}
    for m in pat.finditer(block):
        out+=block[scanpos:m.start()]
        typ,title,label=m.groups()
        if typ=="prob":probcount+=1;n=f"{num}.{probcount}"
        elif typ=="proof":n=""
        else:count+=1;n=f"{num}.{count}"
        if label:labels[prefix+":"+label]=n
        text=names[typ]+(" "+n if n else "")+(" ("+title+")" if title else "")+"."
        out+=r"\begin{quote}\textbf{"+text+"} "+(r"\label{"+prefix+":"+label+"}" if label else "")
        scanpos=m.end()
    block=out+block[scanpos:]
    block=re.sub(r"\\end\{(?:defn|ex|thm|prop|prob|proof)\}",r"\\end{quote}",block)
    # Figure source SVG preserves all upstream path coordinates and curve controls.
    fp=re.compile(r"\\begin\{figure\}([\s\S]*?)\\end\{figure\}")
    def figure(m):
        global figure_count
        figure_count+=1
        text=m[1];asset=re.search(r"\\olasset\{assets/diagrams/([^}]+)\.tikz\}",text)[1]
        cm=re.search(r"\\caption",text);caption,_=arg(text,cm.end())
        lm=re.search(r"\\ollabel\{([^}]+)\}",text);lid=prefix+":"+lm[1];labels[lid]=str(figure_count)
        return r"\begin{center}\includegraphics{assets/"+asset+r".svg}"+"\n"+r"\textbf{આકૃતિ "+str(figure_count)+r".} "+caption+r"\label{"+lid+r"}\end{center}"
    block=fp.sub(figure,block)
    section_text.append((prefix,block))
texts=[]
for prefix,block in section_text:
    def ref(m):
        opts=re.findall(r"\[([^\]]*)\]",m[1]);key=m[2]
        if len(opts)==0:lid=prefix+":"+key
        elif len(opts)==1:lid=":".join(prefix.split(":")[:2]+opts+[key])
        elif len(opts)==2:lid=prefix.split(":")[0]+":"+":".join(opts+[key])
        else:lid=":".join(opts+[key])
        assert lid in labels,lid
        return r"\hyperref["+lid+"]{"+labels[lid]+"}"
    block=re.sub(r"\\olref((?:\[[^\]]*\])*)\{([^}]+)\}",ref,block)
    # MathML renderer treats multline as unnumbered aligned display.
    block=block.replace(r"\begin{multline*}",r"\begin{aligned}").replace(r"\end{multline*}",r"\end{aligned}")
    block=command(block,"shoveright",1,lambda x:x);block=command(block,"shoveleft",1,lambda x:x)
    # Pandoc supports aligned within \[...\].
    block=block.replace(r"\begin{aligned}",r"\[\begin{aligned}").replace(r"\end{aligned}",r"\end{aligned}\]")
    texts.append(block)
macros=r"""
\newcommand{\Nat}{\mathbb{N}}
\newcommand{\Int}{\mathbb{Z}}
\newcommand{\Rat}{\mathbb{Q}}
\newcommand{\Real}{\mathbb{R}}
\newcommand{\PosInt}{\mathbb{Z}^+}
\newcommand{\Bin}{\mathbb{B}}
\newcommand{\Pow}[1]{\wp(#1)}
\newcommand{\Setabs}[2]{\{#1:#2\}}
\newcommand{\tuple}[1]{\langle#1\rangle}
\newcommand{\len}[1]{\mathrm{len}(#1)}
\newcommand{\lif}{\rightarrow}
\newcommand{\phi}{\varphi}
\newcommand{\nicefrac}[2]{\frac{#1}{#2}}
"""
src=B/"sets-html.tex";src.write_text(macros+"\n".join(texts),encoding="utf-8")
cmd=["pandoc",str(src),"-f","latex","-t","html5","--mathml","--standalone","--toc","--number-sections","--shift-heading-level-by=1","--metadata","lang=gu-IN","--metadata","title=ગણો — ઓપન લોજિક ગુજરાતી","--css","reader.css","-o",str(O/"sets.html")]
r=subprocess.run(cmd,capture_output=True,encoding="utf-8",errors="replace")
(B/"pandoc.stderr.txt").write_text(r.stderr,encoding="utf-8")
assert r.returncode==0,r.stderr
page=(O/"sets.html").read_text(encoding="utf-8")
notice='<aside aria-label="આવૃત્તિ વિશે"><p>આ યંત્ર દ્વારા કરેલો ગુજરાતી અનુવાદ છે. આ આવૃત્તિમાં ગણોનું સંપૂર્ણ પ્રકરણ છે: મૂળનાં ૭ એકમો, કુલ ૭૨૨માંથી. સમગ્ર ગ્રંથનું કામ ચાલુ છે. <a href="../docs/EDITION_NOTES.md">પરિભાષા અને ચકાસણીની વિગતો</a>.</p><p>મૂળ: <a href="https://github.com/OpenLogicProject/OpenLogic">Open Logic Project</a> · <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> · <a href="https://github.com/KokunoYumeto/OpenLogic-translations">અનુવાદોનું કેન્દ્ર</a>.</p></aside>'
page=page.replace('</header>','</header>'+notice)
for name,alt in [('union','બંને ગણોના બધા ઘટકો દર્શાવતી યોગગણની આકૃતિ'),('intersection','બંને ગણોમાં સામાન્ય ઘટકો દર્શાવતી છેદગણની આકૃતિ'),('difference','પહેલા ગણમાં હોય અને બીજા ગણમાં ન હોય તેવા ઘટકોની આકૃતિ')]:
    page=re.sub(r'(<img src="assets/'+name+r'\.svg"[^>]*?)alt="[^"]*"',lambda m:m[1]+'alt="'+alt+'"',page)
soup=BeautifulSoup(page,"html.parser")
for box in soup.select('div.center'):
    img=box.find('img')
    if img is None: continue
    image_node=img.extract()
    paragraph=box.find('p')
    figure_node=soup.new_tag('figure')
    figure_node.append(image_node)
    caption=soup.new_tag('figcaption')
    for child in list(paragraph.contents): caption.append(child.extract())
    figure_node.append(caption)
    box.replace_with(figure_node)
(O/"sets.html").write_text(str(soup),encoding="utf-8")
print(json.dumps({"html_bytes":(O/"sets.html").stat().st_size,"labels":len(labels),"figures":figure_count,"pandoc_warnings":r.stderr},ensure_ascii=False))
