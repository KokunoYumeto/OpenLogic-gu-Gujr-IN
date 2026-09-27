"""Build the cumulative 270-unit HTML reader from the checked TeX body."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
template = (ROOT / "tools/build_turing_machines_html.py").read_text(encoding="utf-8")
namespace = {"__file__": str(ROOT / "tools/build_turing_machines_html.py")}
exec(template[:template.index("\ngenerated = ROOT")], namespace)
code = namespace["code"]
assert code.count("turing-machines") > 20
code = code.replace("turing-machines", "undecidability")


def replace_once(before, after):
    global code
    assert code.count(before) == 1, (before, code.count(before))
    code = code.replace(before, after)


replace_once("'undecidability':260", "'undecidability':270")
replace_once("'undecidability':'૨૬૦'", "'undecidability':'૨૭૦'")
replace_once("'undecidability':'ટ્યુરિંગ મશીનો સહિત ઓપન લોજિક ગુજરાતી'",
             "'undecidability':'અનિર્ણેયતા સહિત ઓપન લોજિક ગુજરાતી'")
replace_once("'undecidability':29", "'undecidability':32")
replace_once("'mod:int:prf:part-b':'2',", "'mod:int:prf:part-b':'2',\n                'tur:und:uni:find-inst':'3',")
replace_once("'tur:und:uni:find-inst':'3',", "'tur:und:uni:find-inst':'3',\n                'tur:und:ver:right':'1', 'tur:und:ver:left':'2', 'tur:und:ver:stay':'3',\n                'tur:und:rep:rep-right':'1', 'tur:und:rep:rep-left':'2', 'tur:und:rep:rep-stay':'3',\n                'tur:und:tra:rep-right':'1', 'tur:und:tra:rep-left':'2', 'tur:und:tra:rep-stay':'3',")
replace_once("'--css','undecidability.css?v=1'", "'--css','turing-machines.css?v=1'")
replace_once("નવા ૫૬ એકમો OpenAI Codex GPT-6 Sol", "નવા ૬૬ એકમો OpenAI Codex GPT-6 Sol")
replace_once("OLTM-001થી OLTM-004 સુધીની'),",
             "OLTM-001થી OLTM-004 તથા OLUN-002 અને OLUN-004થી OLUN-024 સુધીની'),")
replace_once("'undecidability':('ટ્યુરિંગ મશીનની સંગણનાઓના નવા પ્રકરણમાં '",
             "'undecidability':('અનિર્ણેયતાના નવા પ્રકરણમાં '")
replace_once("'અવસ્થાચિત્રો, સંરૂપણો, એક-પ્રતીકી સંખ્યાઓ અને મશીનોનું સંયોજન, '",
             "'પરિગણના, સાર્વત્રિક મશીન, અટકવાની અને નિર્ણયની સમસ્યાઓ, '")
replace_once("'વિવિધ સ્વરૂપો તથા ચર્ચ--ટ્યુરિંગ માન્યતા સામેલ છે. સ્થિર મૂળની '",
             "'પ્રથમ-ક્રમ નિરૂપણ અને સાન્ત નિદર્શો સામેલ છે. સ્થિર મૂળના '")
replace_once("'ચાર ઓળખેલી ખામીઓ દેખાતી નોંધો સાથે સુધારી છે.'),",
             "'બાવીસ સૂચિત સુધારા દેખાતી નોંધો સાથે મૂક્યા છે.'),")

# The new variants figure contains two separate state diagrams. Preserve both
# renderings in its single captioned figure; the inherited builder took only
# the first includegraphics match.
replace_once(
    "        asset=(source_asset or rendered_asset)[1]\n",
    "        asset=(source_asset or rendered_asset)[1]\n"
    "        figure_assets=re.findall(r'\\\\includegraphics\\{assets/([^}]+)\\.svg\\}',t)\n"
    "        assert len(figure_assets)<=2\n"
    "        if not figure_assets:figure_assets=[asset]\n"
    "        assert figure_assets[0]==asset\n"
    "        figure_markup='\\n'.join(r'\\includegraphics{assets/'+name+r'.svg}' for name in figure_assets)\n",
)
replace_once(
    "return r'\\begin{center}\\includegraphics{assets/'+asset+r'.svg}'+'\\n'+r'\\textbf{આકૃતિ '",
    "return r'\\begin{center}'+figure_markup+'\\n'+r'\\textbf{આકૃતિ '",
)

generated = ROOT / "tools/build_undecidability_html_expanded.py"
generated.write_text(code, encoding="utf-8", newline="\n")
sys.argv = [sys.argv[0], "undecidability"]
exec(compile(code, str(generated), "exec"),
     {"__name__": "__main__", "__file__": str(generated)})
