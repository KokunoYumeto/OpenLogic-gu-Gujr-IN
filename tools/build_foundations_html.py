"""Offline accessible cumulative reader; preserves formula MathML and graph incidence."""
from pathlib import Path
import re,json,subprocess,html,hashlib
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[1];B=R/'build';O=R/'reader'
def arg(t,i):
    while t[i].isspace():i+=1
    assert t[i]=='{',(t[i:i+40],i)
    d=1;j=i+1
    while d:
        if t[j]=='{' and t[j-1]!='\\':d+=1
        if t[j]=='}' and t[j-1]!='\\':d-=1
        j+=1
    return t[i+1:j-1],j
def command(t,name,n,callback):
    pat=re.compile(r'\\'+name+r'(?![A-Za-z])');pos=0
    while (m:=pat.search(t,pos)):
        vals=[];j=m.end()
        for _ in range(n):v,j=arg(t,j);vals.append(v)
        repl=callback(*vals);t=t[:m.start()]+repl+t[j:];pos=m.start()+len(repl)
    return t
body=(B/'foundations-body.tex').read_text(encoding='utf-8')
body=command(body,'oliflabeldef',3,lambda key,yes,no:no)
body=command(body,'part',1,lambda x:'') # Chapter identity appears in grouped introduction; section numbering continuous.
graph_receipts=[];graph_alt={}
def render_graph(m):
    src=m[0]
    if '[grow\'=up]' in src:
        labels=re.findall(r'node\s*\{\$([^$]+)\$\}',src)
        root=re.search(r'\\node\{\$([^$]+)\$\}',src)[1]
        assert root=='r' and labels==['r','a','c','d','e','b']
        positions={'r':(210,215),'a':(145,130),'b':(280,130),'c':(65,45),'d':(145,45),'e':(225,45)}
        edges=[('r','a'),('r','b'),('a','c'),('a','d'),('a','e')]
        name='tree';directed=False
        alt='મૂળ rથી સંતાન a અને b; aનાં સંતાન c, d અને e. મૂળ નીચે અને સંતાનો ઉપર છે.'
    else:
        labels=re.findall(r'\\node\[draw,circle\]\s*\(([A-D])\)[^;]*\{\$([1-4])\$\};',src)
        expected=[('A','1'),('B','2'),('C','3')]
        assert labels in (expected,expected+[('D','4')])
        assert re.findall(r'\\draw \(([A-D])\) to\s*\(([A-D])\);',src)==[('A','B'),('A','C'),('B','C')]
        assert r'\draw (A) to [loop above]  (A);' in src
        pos={'1':(70,80),'2':(180,80),'3':(180,185),'4':(290,80)}
        positions={label:pos[label] for _,label in labels}
        edges=[('1','1'),('1','2'),('1','3'),('2','3')]
        name='graph-four' if len(labels)==4 else 'graph-three';directed=True
        alt='દિશાયુક્ત આલેખ: 1થી 1, 2 અને 3 તરફ ધારો; 2થી 3 તરફ ધાર.'+(' 4 છૂટું શિરોબિંદુ છે.' if len(labels)==4 else '')
    svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 350 260"><defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="none" stroke="#222"/></marker></defs>']
    for a,b in edges:
        x,y=positions[a];xx,yy=positions[b]
        if a==b:
            d=f'M{x-11},{y-11} C{x-40},{y-65} {x+40},{y-65} {x+11},{y-11}'
        else:
            import math
            dx,dy=xx-x,yy-y;ln=math.hypot(dx,dy)
            x+=dx/ln*18;y+=dy/ln*18;xx-=dx/ln*20;yy-=dy/ln*20
            d=f'M{x:.3f},{y:.3f} L{xx:.3f},{yy:.3f}'
        svg.append(f'<path d="{d}" fill="none" stroke="#222" stroke-width="1.5"'+(' marker-end="url(#arrow)"' if directed else '')+'/>')
    for label,(x,y) in positions.items():
        svg.append(f'<circle cx="{x}" cy="{y}" r="17" fill="white" stroke="#222"/><text x="{x}" y="{y+5}" text-anchor="middle" font-family="serif" font-size="17">{label}</text>')
    svg.append('</svg>')
    path=O/'assets'/f'{name}.svg';path.write_text(''.join(svg),encoding='utf-8')
    graph_receipts.append(dict(asset=path.relative_to(R).as_posix(),source_tikz_sha256=hashlib.sha256(src.encode('utf-8')).hexdigest(),svg_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),vertices=list(positions),edges=edges,directed=directed,method='Deterministic SVG graph from validated original TikZ vertices and incidence. Layout computed for accessibility; mathematical incidence preserved.'))
    graph_alt[name]=alt
    return '\n\n'+r'\includegraphics{assets/'+name+'.svg}\n\n'
# Only graph-containing align environments are dismantled for images/intertext; ordinary math remains.
def align_graph(m):
    if r'\begin{tikzpicture}' not in m[0]:return m[0]
    t=m[0].replace(r'\begin{align*}','').replace(r'\end{align*}','')
    t=re.sub(r'(?m)^\s*&\s*','',t)
    return command(t,'intertext',1,lambda x:'\n\n'+x+'\n\n')
body=re.sub(r'\\begin\{align\*\}[\s\S]*?\\end\{align\*\}',align_graph,body)
body=re.sub(r'\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}',render_graph,body)
sections=re.split(r'(?=\\olfileid)',body);labels={};section_text=[];figcount=0
names={'defn':'વ્યાખ્યા','ex':'ઉદાહરણ','thm':'પ્રમેય','prop':'વિધાન','prob':'સ્વાધ્યાય','proof':'સાબિતી'}
for block in sections:
    if not block.strip():continue
    ident=re.search(r'\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}',block);prefix=':'.join(ident.groups())
    num=len(section_text)+1;count=probcount=0
    labels[prefix+':sec']=str(num)
    block=command(block,'olfileid',3,lambda a,b,c:'')
    block=command(block,'olsection',1,lambda title:r'\section{'+title+r'}\label{'+prefix+':sec}')
    block=re.sub(r'\\begin\{tagblock\}\{[^}]+\}|\\end\{tagblock\}','',block)
    block=re.sub(r'\\(?:begin|end)\{(?:explain|digress|intro)\}','',block)
    # Treat environment opening and all subsequent labels in display order.
    pat=re.compile(r'\\begin\{(defn|ex|thm|prop|prob|proof)\}(?:\[([^\]]*)\])?|\\ollabel\{([^}]+)\}')
    last='';out='';start=0
    for m in pat.finditer(block):
        out+=block[start:m.start()]
        typ,title,label=m.groups()
        if label:
            labels[prefix+':'+label]=last
            out+=r'\label{'+prefix+':'+label+'}'
        else:
            if typ=='prob':probcount+=1;last=f'{num}.{probcount}'
            elif typ=='proof':last=''
            else:count+=1;last=f'{num}.{count}'
            out+=r'\begin{quote}\textbf{'+names[typ]+(' '+last if last else '')+(' ('+title+')' if title else '')+'.} '
        start=m.end()
    block=out+block[start:]
    block=re.sub(r'\\end\{(?:defn|ex|thm|prop|prob|proof)\}',r'\\end{quote}',block)
    def figure(m):
        global figcount
        figcount+=1;t=m[1];asset=re.search(r'\\olasset\{assets/diagrams/([^}]+)\.tikz\}',t)[1]
        cap,_=arg(t,re.search(r'\\caption',t).end())
        lid=re.search(r'\\label\{([^}]+)\}',t)[1];labels[lid]=str(figcount)
        return r'\begin{center}\includegraphics{assets/'+asset+r'.svg}'+'\n'+r'\textbf{આકૃતિ '+str(figcount)+'.} '+cap+r'\label{'+lid+r'}\end{center}'
    block=re.sub(r'\\begin\{figure\}([\s\S]*?)\\end\{figure\}',figure,block)
    section_text.append((prefix,block))
texts=[]
for prefix,block in section_text:
    def ref(m):
        opts=re.findall(r'\[([^\]]*)\]',m[1]);key=m[2]
        base=prefix.split(':')
        lid=':'.join(base[:3-len(opts)]+opts+[key])
        assert lid in labels and labels[lid],lid
        return r'\hyperref['+lid+']{'+labels[lid]+'}'
    block=re.sub(r'\\olref((?:\[[^\]]*\])*)\{([^}]+)\}',ref,block)
    block=command(block,'citeyear',1,lambda key:r'\hyperref[bib:'+key+']{1965}' if key=='Benacerraf1965' else (_ for _ in ()).throw(ValueError(key)))
    block=block.replace(r'\begin{multline*}',r'\[\begin{aligned}').replace(r'\end{multline*}',r'\end{aligned}\]')
    block=command(block,'shoveright',1,lambda x:x);block=command(block,'shoveleft',1,lambda x:x)
    texts.append(block)
# The first-release HTML preparation retains its independently verified exact-path set diagrams.
for name in ('union','intersection','difference'):assert (O/'assets'/f'{name}.svg').exists()
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
\newcommand{\liff}{\leftrightarrow}
\newcommand{\phi}{\varphi}
\newcommand{\nicefrac}[2]{\frac{#1}{#2}}
\newcommand{\Id}[1]{\mathrm{Id}_{#1}}
\newcommand{\equivrep}[2]{[#1]_{#2}}
\newcommand{\equivclass}[2]{#1/_{\!{#2}}}
\newcommand{\funrestrictionto}[2]{#1\mathord{\restriction}_{#2}}
\newcommand{\funimage}[2]{#1[#2]}
\newcommand{\emptyseq}{\Lambda}
"""
editorial=(R/'gu-foundations.tex').read_text(encoding='utf-8').split(r'\section*{સંપાદકીય નોંધો}',1)[1].split(r'\begin{thebibliography}',1)[0]
editorial=re.sub(r'\\addcontentsline\{toc\}\{section\}\{[^}]+\}','',editorial)
src=B/'foundations-html.tex'
src.write_text(macros+'\n'.join(texts)+r'\section*{સંપાદકીય નોંધો}'+editorial+r'\section*{સંદર્ભગ્રંથો}\label{bib:Benacerraf1965}'+'\nBenacerraf, Paul. 1965. '+r'\emph{What numbers could not be}'+'. The Philosophical Review 74(1), 47–73.\n',encoding='utf-8')
cmd=['pandoc',str(src),'-f','latex','-t','html5','--mathml','--standalone','--toc','--number-sections','--shift-heading-level-by=1','--metadata','lang=gu-IN','--metadata','title=ગણો અને સંબંધો — ઓપન લોજિક ગુજરાતી','--css','reader.css','-o',str(O/'foundations.html')]
result=subprocess.run(cmd,capture_output=True,encoding='utf-8',errors='replace')
(B/'foundations-pandoc.stderr.txt').write_text(result.stderr,encoding='utf-8')
assert result.returncode==0,result.stderr
soup=BeautifulSoup((O/'foundations.html').read_text(encoding='utf-8'),'html.parser')
notice=BeautifulSoup('<aside aria-label="આવૃત્તિ વિશે"><p>આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં ગણો અને સંબંધોનાં સંપૂર્ણ પ્રકરણો છે: ૭૨૨માંથી ૧૬ મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે. <a href="../docs/EDITION_NOTES.md">પરિભાષા અને ચકાસણીની વિગતો</a>.</p><p>મૂળ: <a href="https://github.com/OpenLogicProject/OpenLogic">Open Logic Project</a> · <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a> · <a href="https://github.com/KokunoYumeto/OpenLogic-translations">અનુવાદોનું કેન્દ્ર</a>.</p></aside>','html.parser')
soup.header.insert_after(notice.aside)
alts={'union':'બંને ગણોના બધા ઘટકો દર્શાવતો યોગગણ','intersection':'બંને ગણોમાં સામાન્ય ઘટકો દર્શાવતો છેદગણ','difference':'પહેલા ગણમાં હોય અને બીજા ગણમાં ન હોય તેવા ઘટકો'}
alts.update(graph_alt)
for img in soup.find_all('img'):img['alt']=alts[Path(img['src']).stem]
for box in soup.select('div.center'):
    img=box.find('img')
    if img is None:continue
    figure=soup.new_tag('figure');figure.append(img.extract())
    if (para:=box.find('p')) and para.get_text(strip=True):
        cap=soup.new_tag('figcaption')
        for child in list(para.contents):cap.append(child.extract())
        figure.append(cap)
    box.replace_with(figure)
ids={e['id'] for e in soup.select('[id]')}
broken=[a['href'] for a in soup.select('a[href^="#"]') if a['href'][1:] not in ids]
assert not broken,broken
assert len(soup.find_all('img'))==6
assert not soup.select('span.math'), 'Pandoc math conversion fell back to source TeX'
(O/'foundations.html').write_text(str(soup),encoding='utf-8')
(B/'foundations-html-qa.json').write_text(json.dumps(dict(mathml_nodes=len(soup.find_all('math')),images=6,source_labels=len(labels),broken_anchors=broken,graph_incidence=graph_receipts,pandoc_stderr=result.stderr,semantic_review='pending actual browser inspection'),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(bytes=(O/'foundations.html').stat().st_size,mathml=len(soup.find_all('math')),labels=len(labels),images=6,warnings=result.stderr),ensure_ascii=False))
