"""Build the 224-unit Gujarati HTML reader with exact AI disclosure."""

from pathlib import Path
import sys

from build_lindstrom_html import code as lindstrom_code


ROOT = Path(__file__).resolve().parents[1]
template = ROOT / "tools" / "build_functions_html.py"
code = lindstrom_code


def replace_once(before, after):
    global code
    assert code.count(before) == 1, (before, code.count(before))
    code = code.replace(before, after)


assert code.count(",'lindstrom'}") == 20
code = code.replace(",'lindstrom'}", ",'lindstrom','computability'}")
replace_once(",'lindstrom':204}[edition]", ",'lindstrom':204,'computability':224}[edition]")
replace_once(",'lindstrom':'૨૦૪'}[edition]", ",'lindstrom':'૨૦૪','computability':'૨૨૪'}[edition]")
replace_once(
    "    'lindstrom':'લિન્ડસ્ટ્રોમનું પ્રમેય સહિત ઓપન લોજિક ગુજરાતી',\n",
    "    'lindstrom':'લિન્ડસ્ટ્રોમનું પ્રમેય સહિત ઓપન લોજિક ગુજરાતી',\n"
    "    'computability':'પુનરાવર્તી વિધેયો સહિત ઓપન લોજિક ગુજરાતી',\n",
)
replace_once(",'lindstrom':124}[edition]", ",'lindstrom':124,'computability':124}[edition]")
replace_once(",'lindstrom':15}[edition]", ",'lindstrom':15,'computability':15}[edition]")

# The earlier Model Theory part and its four chapters remain nested, while the
# new Computability part starts another top-level HTML chapter.
replace_once(
    "    if edition=='lindstrom':\n        model_chapters.append(r'\\section{લિન્ડસ્ટ્રોમનું પ્રમેય}')\n",
    "    if edition in {'lindstrom','computability'}:\n"
    "        model_chapters.append(r'\\section{લિન્ડસ્ટ્રોમનું પ્રમેય}')\n",
)
replace_once(
    "    assert model_part in before and r'\\part{' not in model_tail\n",
    "    assert model_part in before and model_tail.count(r'\\part{') == (1 if edition=='computability' else 0)\n",
)
replace_once(
    "body=command(body,'part',1,lambda x:'') # Earlier chapter identity appears in grouped introduction; section numbering stays continuous.\n",
    "if edition=='computability':\n"
    "    assert body.count(r'\\part{સંગણનીયતા}')==1\n"
    "    body=body.replace(r'\\part{સંગણનીયતા}',r'\\chapter{સંગણનીયતા}',1)\n"
    "body=command(body,'part',1,lambda x:'') # Earlier chapter identity appears in grouped introduction; section numbering stays continuous.\n",
)

correction_entry = """        'computability':('OLFUN-001થી OLFUN-005, OLSIZ-001થી OLSIZ-012, '
                         'OLARI-001થી OLARI-004, OLINF-001થી OLINF-002, '
                         'OLPL-001થી OLPL-002, OLPRF-001થી OLPRF-004, '
                         'OLSEQ-001થી OLSEQ-006, OLND-001થી OLND-006, '
                         'OLTAB-001થી OLTAB-012, OLAX-001થી OLAX-018, '
                         'OLCO-001થી OLCO-022, OLFINT-001થી OLFINT-006, '
                         'OLSYN-001થી OLSYN-007, OLSEM-001થી OLSEM-011, '
                         'OLMAT-001થી OLMAT-005, OLBYD-001થી OLBYD-006, '
                         'OLMTB-001થી OLMTB-008, OLMAR-001થી OLMAR-016, '
                         'OLINT-001થી OLINT-010, OLLIN-001થી OLLIN-013 અને '
                         'OLCMP-001થી OLCMP-010 સુધીની'),
"""
replace_once("    }[edition]\n    latest_editorial={", correction_entry + "    }[edition]\n    latest_editorial={")
editorial_entry = """        'computability':('પુનરાવર્તી વિધેયોના નવા પ્રકરણમાં આદિમ અને '
                         'આંશિક પુનરાવર્તન, કોડિંગ, સીમિત લઘુત્તમીકરણ, '
                         'ક્લીનીનું સામાન્ય સ્વરૂપ અને અટકવાની સમસ્યા '
                         'સમાવિષ્ટ છે. સ્થિર મૂળની દસ ઓળખેલી ખામીઓ '
                         'દેખાતી નોંધો સાથે સુધારી છે.'),
"""
replace_once("    }[edition]\n    editorial=editorial.replace", editorial_entry + "    }[edition]\n    editorial=editorial.replace")
replace_once(
    "else:\n    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે.",
    "elif edition == 'computability':\n"
    "    notice_text = f'આ ગુજરાતી યંત્ર-અનુવાદ છે. અગાઉનાં ૨૦૪ એકમો OpenAI Codex GPT-5.6 Sol, Ultra effort વડે અને નવા ૨૦ એકમો OpenAI Codex GPT-6 Sol, Ultra effort વડે તૈયાર થયા છે. મૂળ સાથે આ જ એજન્ટની સરખામણી થઈ છે; સ્વતંત્ર ગુજરાતી નિષ્ણાતનું પ્રમાણપત્ર મળેલું નથી. સંગણનીયતા ભાગની શરૂઆત અને પુનરાવર્તી વિધેયોનું સંપૂર્ણ પ્રકરણ સામેલ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'\n"
    "else:\n    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે.",
)

# Pandoc's TeX reader does not load OpenLogic's custom recursion macros.
# Expand them in the derived HTML source using the frozen upstream definitions.
marker = "available=set(json.loads((B/f'{edition}-available-labels.json').read_text()))\n"
expansion = r'''if edition=='computability':
    tower_source=(r'2^{(2^{\iddots^{2^{x}}})}\raisebox{1ex}{\bigg\rbrace}'+'\n'
                  +r'\raisebox{1ex}{\text {$y$ વખત $2$}}')
    tower_html=r'\underbrace{2^{(2^{\ddots^{2^{x}}})}}_{\text{$y$ વખત $2$}}'
    assert body.count(tower_source)==1
    body=body.replace(tower_source,tower_html)
    for original, rendered in {
        r'\Zero':r'\mathrm{zero}', r'\Succ':r'\mathrm{succ}',
        r'\Add':r'\mathrm{add}', r'\Mult':r'\mathrm{mult}',
        r'\Exp':r'\mathrm{exp}', r'\Pred':r'\mathrm{pred}',
        r'\tsub':r'\mathbin{\dot{-}}', r'\defis':'=',
        r'\defiff':r'\Leftrightarrow',
    }.items():
        body=re.sub(re.escape(original)+r'(?![A-Za-z])',lambda _m:rendered,body)
    body=command(body,'Proj',2,lambda arity,index:r'P^{'+arity+'}_{'+index+'}')
    body=command(body,'Char',1,lambda relation:r'\chi_{'+relation+'}')
    body=command(body,'bexists',2,lambda bound,predicate:r'(\exists '+bound+r')\;'+predicate)
    body=command(body,'bforall',2,lambda bound,predicate:r'(\forall '+bound+r')\;'+predicate)
    body=command(body,'bmin',2,lambda bound,predicate:r'(\mathrm{min}\;'+bound+r')\,'+predicate)
    body=command(body,'bforall',2,lambda bound,predicate:r'(\forall '+bound+r')\;'+predicate)
    body=command(body,'umin',2,lambda variable,predicate:r'\mu '+variable+r'\;'+predicate)
    body=command(body,'fact',1,lambda value:value+r'\,!')
    body=re.sub(r'\\cfind\{([^{}]+)\}(?:\[([^\[\]]+)\])?',
                lambda m:r'\varphi_{'+m[1]+'}'+(('^{'+m[2]+'}') if m[2] else ''),body)
    body=command(body,'fn',1,lambda name:r'\mathrm{'+name+'}')
'''
replace_once(marker, expansion + marker)

if __name__ == "__main__":
    generated = ROOT / "tools" / "build_computability_html_expanded.py"
    generated.write_text(code, encoding="utf-8", newline="\n")
    sys.argv = [sys.argv[0], "computability"]
    exec(compile(code, str(generated), "exec"), {"__name__": "__main__", "__file__": str(template)})
