"""Build the 248-unit cumulative Gujarati HTML reader."""

from pathlib import Path
import sys

from build_computability_html import code as recursive_functions_code


ROOT = Path(__file__).resolve().parents[1]
code = recursive_functions_code


def replace_once(before: str, after: str) -> None:
    global code
    assert code.count(before) == 1, (before, code.count(before))
    code = code.replace(before, after)


# Inherit all previously checked reader structure and mathematical diagrams.
# The new edition selects the larger prepared body and its label inventory.
assert code.count("computability") > 20
code = code.replace("computability", "computability-theory")
replace_once("'computability-theory':224", "'computability-theory':248")
replace_once("'computability-theory':'૨૨૪'", "'computability-theory':'૨૪૮'")
replace_once(
    "'computability-theory':'પુનરાવર્તી વિધેયો સહિત ઓપન લોજિક ગુજરાતી'",
    "'computability-theory':'સંગણનીયતા સિદ્ધાંત સહિત ઓપન લોજિક ગુજરાતી'",
)
replace_once(
    "'OLCMP-001થી OLCMP-010 સુધીની'),",
    "'OLCMP-001થી OLCMP-010 અને OLCT-001થી OLCT-012 સુધીની'),",
)

start = code.index("        'computability-theory':('પુનરાવર્તી વિધેયોના નવા પ્રકરણમાં")
end = code.index("),\n    }[edition]", start) + 2
code = code[:start] + """        'computability-theory':('સંગણનીયતા સિદ્ધાંતના નવા પ્રકરણમાં '
                         'સંગણકીય રીતે પરિગણનીય ગણો, પૂરક, બહુ-એક ન્યૂનીકરણ, પૂર્ણતા, '
                         'રાઇસનું પ્રમેય અને સ્થિર-બિંદુ પ્રમેય સામેલ છે. સ્થિર મૂળની '
                         'બાર ઓળખેલી ખામીઓ દેખાતી નોંધો સાથે સુધારી છે.'),""" + code[end:]
replace_once("નવા ૨૦ એકમો OpenAI Codex GPT-6 Sol", "નવા ૪૪ એકમો OpenAI Codex GPT-6 Sol")
replace_once(
    "સંગણનીયતા ભાગની શરૂઆત અને પુનરાવર્તી વિધેયોનું સંપૂર્ણ પ્રકરણ સામેલ છે:",
    "પુનરાવર્તી વિધેયો અને સંગણનીયતા સિદ્ધાંતનાં સંપૂર્ણ પ્રકરણો સામેલ છે:",
)

# These two frozen-source macros occur for the first time in this chapter.
start = code.index("    body=re.sub(r'\\\\cfind")
end = code.index("    body=command(body,'fn'", start)
code = code[:start] + (
    "    def expand_cfind(t):\n"
    "        pat=re.compile(r'\\\\cfind(?![A-Za-z])');pos=0\n"
    "        while (m:=pat.search(t,pos)):\n"
    "            index,j=arg(t,m.end())\n"
    "            power=None\n"
    "            if j<len(t) and t[j]=='[':\n"
    "                end=t.index(']',j+1);power=t[j+1:end];j=end+1\n"
    "            repl=r'\\varphi_{'+index+'}'+(('^{'+power+'}') if power else '')\n"
    "            t=t[:m.start()]+repl+t[j:];pos=m.start()+len(repl)\n"
    "        return t\n"
    "    body=expand_cfind(body)\n"
) + code[end:]
replace_once(
    "    body=command(body,'fn',1,lambda name:r'\\mathrm{'+name+'}')\n",
    "    body=command(body,'fn',1,lambda name:r'\\mathrm{'+name+'}')\n"
    "    body=command(body,'Complement',1,lambda value:r'\\overline{'+value+'}')\n"
    "    body=re.sub(r'\\\\red(?![A-Za-z])',r'\\\\Longrightarrow',body)\n"
    "    body=body.replace(r'\\/', '')\n",
)

generated = ROOT / "tools" / "build_computability_theory_html_expanded.py"
generated.write_text(code, encoding="utf-8", newline="\n")
sys.argv = [sys.argv[0], "computability-theory"]
exec(compile(code, str(generated), "exec"),
     {"__name__": "__main__", "__file__": str(generated)})
