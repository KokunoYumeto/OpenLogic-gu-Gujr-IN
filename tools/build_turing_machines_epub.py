"""Build the deterministic 260-unit EPUB from the accepted HTML reader."""

from pathlib import Path
import sys
from build_computability_theory_epub import code as inherited_code


ROOT = Path(__file__).resolve().parents[1]
code = inherited_code


def replace_once(before: str, after: str) -> None:
    global code
    assert code.count(before) == 1, (before, code.count(before))
    code = code.replace(before, after)


assert code.count("computability-theory") >= 3
code = code.replace("computability-theory", "turing-machines")
code = code.replace("Computability-Theory", "Turing-Machines")
replace_once("epub024-stage", "epub025-stage")
replace_once("epub024-replay-stage", "epub025-replay-stage")
replace_once("EPUB_BUILD_RECEIPT_024.json", "EPUB_BUILD_RECEIPT_025.json")
replace_once('CSS = ROOT / "reader" / "reader.css"',
             'CSS = ROOT / "reader" / "turing-machines.css"')
replace_once("સંગણનીયતા સિદ્ધાંત સહિત ઓપન લોજિક ગુજરાતી",
             "ટ્યુરિંગ મશીનો સહિત ઓપન લોજિક ગુજરાતી")
replace_once("releases/tag/turing-machines-v0.18.0",
             "releases/tag/turing-machines-v0.19.0")
replace_once('MODIFIED = "2026-09-25T00:00:00Z"',
             'MODIFIED = "2026-09-26T00:00:00Z"')
replace_once("ZIP_TIME = (2026, 9, 25, 0, 0, 0)",
             "ZIP_TIME = (2026, 9, 26, 0, 0, 0)")
replace_once("NAVIGATION_ENTRIES = 254", "NAVIGATION_ENTRIES = 266")
replace_once('COVERAGE = "248/722 units; OLP-0004-0251"',
             'COVERAGE = "260/722 units; OLP-0004-0263"')
replace_once("ગુજરાતી સંચિત આવૃત્તિ: ૭૨૨માંથી ૨૪૮ મૂળ એકમો, OLP-0004–0251.",
             "ગુજરાતી સંચિત આવૃત્તિ: ૭૨૨માંથી ૨૬૦ મૂળ એકમો, OLP-0004–0263.")
replace_once("૭૨૨ મૂળ એકમોમાંથી ૨૪૮ એકમો, એટલે OLP-0004થી OLP-0251 સુધીનો",
             "૭૨૨ મૂળ એકમોમાંથી ૨૬૦ એકમો, એટલે OLP-0004થી OLP-0263 સુધીનો")
replace_once("અને નવા ૪૪ એકમો GPT-6 Sol", "અને નવા ૫૬ એકમો GPT-6 Sol")
replace_once("અને નવા ૪૪ એકમો OpenAI Codex GPT-6 Sol",
             "અને નવા ૫૬ એકમો OpenAI Codex GPT-6 Sol")
replace_once(
    "પુનરાવર્તી વિધેયો અને સંગણનીયતા સિદ્ધાંતનાં સંપૂર્ણ પ્રકરણો સામેલ છે. ",
    "પુનરાવર્તી વિધેયો અને સંગણનીયતા સિદ્ધાંતનાં સંપૂર્ણ પ્રકરણો તથા "
    "ટ્યુરિંગ મશીનની સંગણનાઓનું સંપૂર્ણ પ્રકરણ સામેલ છે. ",
)
replace_once(
    "અટકવાની સમસ્યા, સંગણકીય રીતે પરિગણનીય ગણો, બહુ-એક ન્યૂનીકરણ, ",
    "અટકવાની સમસ્યા, સંગણકીય રીતે પરિગણનીય ગણો, બહુ-એક ન્યૂનીકરણ, ",
)
replace_once(
    "રાઇસનું પ્રમેય અને સ્થિર-બિંદુ પ્રમેયનો સમાવેશ છે.",
    "રાઇસનું પ્રમેય, સ્થિર-બિંદુ પ્રમેય, અવસ્થાચિત્રો અને ચર્ચ--ટ્યુરિંગ માન્યતાનો સમાવેશ છે.",
)
replace_once(
    'expected_assets = 15 if EDITION in {"lindstrom", "turing-machines"} else (14 if EDITION == "interpolation" else 13)',
    'expected_assets = 29 if EDITION == "turing-machines" else (15 if EDITION == "lindstrom" else (14 if EDITION == "interpolation" else 13))',
)

generated = ROOT / "tools" / "build_turing_machines_epub_expanded.py"
generated.write_text(code, encoding="utf-8", newline="\n")
sys.argv = [sys.argv[0], "turing-machines"]
exec(compile(code, str(generated), "exec"),
     {"__name__": "__main__", "__file__": str(generated)})
