"""Build the 260-unit cumulative Gujarati HTML reader and exact graph receipts."""

from pathlib import Path
import sys
from build_computability_theory_html import code as inherited_code


ROOT = Path(__file__).resolve().parents[1]
code = inherited_code


def replace_once(before: str, after: str) -> None:
    global code
    assert code.count(before) == 1, (before, code.count(before))
    code = code.replace(before, after)


assert code.count("computability-theory") > 20
code = code.replace("computability-theory", "turing-machines")
replace_once("'turing-machines':248", "'turing-machines':260")
replace_once("'turing-machines':'૨૪૮'", "'turing-machines':'૨૬૦'")
replace_once(
    "'turing-machines':'સંગણનીયતા સિદ્ધાંત સહિત ઓપન લોજિક ગુજરાતી'",
    "'turing-machines':'ટ્યુરિંગ મશીનો સહિત ઓપન લોજિક ગુજરાતી'",
)
replace_once(
    "'OLCMP-001થી OLCMP-010 અને OLCT-001થી OLCT-012 સુધીની'),",
    "'OLCMP-001થી OLCMP-010, OLCT-001થી OLCT-012 અને OLTM-001થી OLTM-004 સુધીની'),",
)
replace_once(
    "'turing-machines':('સંગણનીયતા સિદ્ધાંતના નવા પ્રકરણમાં '",
    "'turing-machines':('ટ્યુરિંગ મશીનની સંગણનાઓના નવા પ્રકરણમાં '",
)
replace_once(
    "'સંગણકીય રીતે પરિગણનીય ગણો, પૂરક, બહુ-એક ન્યૂનીકરણ, પૂર્ણતા, '",
    "'અવસ્થાચિત્રો, સંરૂપણો, એક-પ્રતીકી સંખ્યાઓ અને મશીનોનું સંયોજન, '",
)
replace_once(
    "'રાઇસનું પ્રમેય અને સ્થિર-બિંદુ પ્રમેય સામેલ છે. સ્થિર મૂળની '",
    "'વિવિધ સ્વરૂપો તથા ચર્ચ--ટ્યુરિંગ માન્યતા સામેલ છે. સ્થિર મૂળની '",
)
replace_once(
    "'બાર ઓળખેલી ખામીઓ દેખાતી નોંધો સાથે સુધારી છે.'),",
    "'ચાર ઓળખેલી ખામીઓ દેખાતી નોંધો સાથે સુધારી છે.'),",
)
replace_once("નવા ૪૪ એકમો OpenAI Codex GPT-6 Sol", "નવા ૫૬ એકમો OpenAI Codex GPT-6 Sol")
replace_once(
    "પુનરાવર્તી વિધેયો અને સંગણનીયતા સિદ્ધાંતનાં સંપૂર્ણ પ્રકરણો સામેલ છે:",
    "પુનરાવર્તી વિધેયો, સંગણનીયતા સિદ્ધાંત અને ટ્યુરિંગ મશીનની સંગણનાઓનું પ્રકરણ સામેલ છે:",
)

# Model Theory is followed by two parts in this cumulative reader.
replace_once(
    "model_tail.count(r'\\part{') == (1 if edition=='turing-machines' else 0)",
    "model_tail.count(r'\\part{') == (2 if edition=='turing-machines' else 0)",
)
replace_once(
    "    body=body.replace(r'\\part{સંગણનીયતા}',r'\\chapter{સંગણનીયતા}',1)\n",
    "    body=body.replace(r'\\part{સંગણનીયતા}',r'\\chapter{સંગણનીયતા}',1)\n"
    "    assert body.count(r'\\part{ટ્યુરિંગ મશીનો}')==1\n"
    "    body=body.replace(r'\\part{ટ્યુરિંગ મશીનો}',r'\\chapter{ટ્યુરિંગ મશીનો}',1)\n",
)

# Graphs are generated from the checked TikZ state/edge/transition grammar.
code = code.replace(
    "from bs4 import BeautifulSoup\n",
    "from bs4 import BeautifulSoup\nfrom render_turing_graphs import render_turing_diagram\n",
    1,
)
replace_once(
    "    src=m[0]\n",
    "    src=m[0]\n"
    "    if r'\\tikzstyle{every state}' in src:\n"
    "        return render_turing_diagram(src,O,R,graph_receipts,graph_alt)\n",
)

# The intro uses the upstream, artist-drawn machine asset.  The reflowable
# reader includes a clearly identified accessible schematic of its tape/head/
# finite-control components, while the PDF retains the original TikZ asset.
asset_line = next(line for line in code.splitlines()
                  if "source_asset=re.search(" in line)
assert asset_line.count("assets/diagrams/") == 1
code = code.replace(
    asset_line,
    asset_line.replace("assets/diagrams/", r"(?:\\olpath/)?assets/diagrams/"),
    1,
)
replace_once(
    "graph_receipts=[];graph_alt={}\n",
    "graph_receipts=[];graph_alt={}\n"
    "tape_source=R/'upstream'/'assets'/'diagrams'/'turing-machine.tikz'\n"
    "tape_svg=O/'assets'/'turing-machine.svg'\n"
    "assert tape_source.is_file() and tape_svg.is_file()\n"
    "graph_receipts.append(dict(asset=tape_svg.relative_to(R).as_posix(),"
    "source_tikz_sha256=hashlib.sha256(tape_source.read_bytes()).hexdigest(),"
    "svg_sha256=hashlib.sha256(tape_svg.read_bytes()).hexdigest(),"
    "method='Accessible schematic of the tape, reading/writing head and finite control; original artist-drawn TikZ remains in the PDF and source archive.'))\n"
    "graph_alt['turing-machine']='ટ્યુરિંગ મશીનનું યોજનાત્મક ચિત્ર: ડાબી સીમાથી શરૂ થતી ટેપ, એક ખાનાં સામેનો વાંચન-લેખન હેડ અને તેની સાથે જોડાયેલું સાન્ત નિયંત્રણ.'\n",
)

needle = "body=re.sub(r'\\\\begin\\{tikzpicture\\}[\\s\\S]*?\\\\end\\{tikzpicture\\}',render_graph,body)\n"
assert code.count(needle) == 1
code = code.replace(
    needle,
    needle
    + "body=re.sub(r'\\\\\\[\\s*(\\\\includegraphics\\{assets/turing-machine-\\d+\\.svg\\})\\s*\\\\\\]',"
      "r'\\n\\n\\1\\n\\n',body)\n"
    + "body=command(body,'TMtrans',3,lambda read,write,move:read+', '+write+', '+move)\n"
    + "for original,rendered in {r'\\TMendtape':r'\\triangleright',r'\\TMblank':'0',"
      "r'\\TMstroke':'1',r'\\TMleft':'L',r'\\TMright':'R',r'\\TMstay':'N'}.items():\n"
    + "    body=re.sub(re.escape(original)+r'(?![A-Za-z])',lambda _match:rendered,body)\n",
)
replace_once("'turing-machines':15}[edition]", "'turing-machines':29}[edition]")
replace_once("'--css','reader.css?v=3'", "'--css','turing-machines.css?v=1'")
replace_once(
    "for img in soup.find_all('img'):img['alt']=alts[Path(img['src']).stem]",
    "for img in soup.find_all('img'):\n"
    "    img['alt']=alts[Path(img['src']).stem]\n"
    "    if Path(img['src']).stem.startswith('turing-machine'):\n"
    "        img['class']=list(img.get('class',[]))+['tm-illustration']",
)

# Pandoc treats the frozen display-wrapped LaTeX tabular as unsupported math.
# Its three formal transition cells are restored as a semantic HTML table with
# MathML for the state and transition entries; the source TeX is untouched.
table_repair = '''machine_fallbacks=soup.select('span.math')
assert len(machine_fallbacks)==1 and r'\\begin{tabular}{lllll}' in machine_fallbacks[0].get_text()
assert r'\\triangleright' in machine_fallbacks[0].get_text()
assert machine_fallbacks[0].parent.name=='p'
machine_table=BeautifulSoup("""<table class="machine-table">
<caption>સમ મશીનનું મશીન-કોષ્ટક</caption>
<thead><tr><th scope="col">અવસ્થા</th><th scope="col">0</th><th scope="col">1</th><th scope="col">▷</th></tr></thead>
<tbody>
<tr><th scope="row"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>0</mn></msub></math></th><td></td><td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><msub><mi>q</mi><mn>1</mn></msub><mo>,</mo><mi>R</mi></math></td><td></td></tr>
<tr><th scope="row"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>q</mi><mn>1</mn></msub></math></th><td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>,</mo><msub><mi>q</mi><mn>1</mn></msub><mo>,</mo><mi>R</mi></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>,</mo><msub><mi>q</mi><mn>0</mn></msub><mo>,</mo><mi>R</mi></math></td><td></td></tr>
</tbody></table>""",'html.parser').table
machine_fallbacks[0].parent.replace_with(machine_table)
assert len(soup.select('table.machine-table'))==1
'''
replace_once(
    "assert not soup.select('span.math'), 'Pandoc math conversion fell back to source TeX'",
    table_repair
    + "assert not soup.select('span.math'), 'Pandoc math conversion fell back to source TeX'",
)

generated = ROOT / "tools" / "build_turing_machines_html_expanded.py"
generated.write_text(code, encoding="utf-8", newline="\n")
sys.argv = [sys.argv[0], "turing-machines"]
exec(compile(code, str(generated), "exec"),
     {"__name__": "__main__", "__file__": str(generated)})
