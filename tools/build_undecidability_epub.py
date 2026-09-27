"""Build a reproducible local 270-unit EPUB from the checked HTML reader."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
template = (ROOT / "tools/build_turing_machines_epub.py").read_text(encoding="utf-8")
namespace = {"__file__": str(ROOT / "tools/build_turing_machines_epub.py")}
exec(template[:template.index("\ngenerated = ROOT")], namespace)
code = namespace["code"]
assert code.count("turing-machines") >= 3
code = code.replace("turing-machines", "undecidability")
code = code.replace("Turing-Machines", "Undecidability")


def replace_once(before, after):
    global code
    assert code.count(before) == 1, (before, code.count(before))
    code = code.replace(before, after)


replace_once('CSS = ROOT / "reader" / "undecidability.css"',
             'CSS = ROOT / "reader" / "turing-machines.css"')
replace_once('"epub025-stage"', '"epub026-stage"')
replace_once('"epub025-replay-stage"', '"epub026-replay-stage"')
replace_once('"EPUB_BUILD_RECEIPT_025.json"', '"EPUB_BUILD_RECEIPT_026.json"')
replace_once('TITLE = "ટ્યુરિંગ મશીનો સહિત ઓપન લોજિક ગુજરાતી"',
             'TITLE = "અનિર્ણેયતા સહિત ઓપન લોજિક ગુજરાતી"')
replace_once('"releases/tag/undecidability-v0.19.0"', '""')
replace_once('NAVIGATION_ENTRIES = 266', 'NAVIGATION_ENTRIES = 276')
replace_once('COVERAGE = "260/722 units; OLP-0004-0263"',
             'COVERAGE = "270/722 units; OLP-0004-0273"')
replace_once('ગુજરાતી સંચિત આવૃત્તિ: ૭૨૨માંથી ૨૬૦ મૂળ એકમો, OLP-0004–0263.',
             'ગુજરાતી સંચિત આવૃત્તિ: ૭૨૨માંથી ૨૭૦ મૂળ એકમો, OLP-0004–0273.')
replace_once('૭૨૨ મૂળ એકમોમાંથી ૨૬૦ એકમો, એટલે OLP-0004થી OLP-0263 સુધીનો',
             '૭૨૨ મૂળ એકમોમાંથી ૨૭૦ એકમો, એટલે OLP-0004થી OLP-0273 સુધીનો')
assert code.count('નવા ૫૬ એકમો') == 2
code = code.replace('નવા ૫૬ એકમો', 'નવા ૬૬ એકમો')
replace_once('ટ્યુરિંગ મશીનની સંગણનાઓનું સંપૂર્ણ પ્રકરણ સામેલ છે.',
             'ટ્યુરિંગ મશીનોનાં સંગણનાઓ અને અનિર્ણેયતા એમ બંને સંપૂર્ણ પ્રકરણો સામેલ છે.')
replace_once('રાઇસનું પ્રમેય, સ્થિર-બિંદુ પ્રમેય, અવસ્થાચિત્રો અને ચર્ચ--ટ્યુરિંગ માન્યતાનો સમાવેશ છે.',
             'રાઇસનું પ્રમેય, સ્થિર-બિંદુ પ્રમેય, સાર્વત્રિક મશીન, નિર્ણય સમસ્યા અને ટ્રાખ્ટેનબ્રોટના પ્રમેયનો સમાવેશ છે.')
replace_once('expected_assets = 29 if EDITION == "undecidability"',
             'expected_assets = 32 if EDITION == "undecidability"')

generated = ROOT / "tools/build_undecidability_epub_expanded.py"
generated.write_text(code, encoding="utf-8", newline="\n")
sys.argv = [sys.argv[0], "undecidability"]
exec(compile(code, str(generated), "exec"),
     {"__name__": "__main__", "__file__": str(generated)})
