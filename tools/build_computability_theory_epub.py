"""Build the deterministic 248-unit EPUB from the checked HTML reader."""

from pathlib import Path
import sys

from build_computability_epub import code as recursive_functions_code


ROOT = Path(__file__).resolve().parents[1]
code = recursive_functions_code
assert code.count("computability") >= 3
code = code.replace("computability", "computability-theory")

start = code.index('elif EDITION == "computability-theory":')
end = code.index("\n\n\ndef require(condition:", start)
code = code[:start] + '''elif EDITION == "computability-theory":
    INPUT = ROOT / "reader" / "computability-theory.html"
    OUTPUT = ROOT / "releases" / "OpenLogic-gu-Gujr-IN-Computability-Theory.epub"
    REPLAY = ROOT / "build" / "OpenLogic-gu-Gujr-IN-Computability-Theory-replay.epub"
    STAGE = ROOT / "build" / "epub024-stage"
    REPLAY_STAGE = ROOT / "build" / "epub024-replay-stage"
    RECEIPT = ROOT / "build" / "EPUB_BUILD_RECEIPT_024.json"
    TITLE = "સંગણનીયતા સિદ્ધાંત સહિત ઓપન લોજિક ગુજરાતી"
    IDENTIFIER = (
        "https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/"
        "releases/tag/computability-theory-v0.18.0"
    )
    MODIFIED = "2026-09-25T00:00:00Z"
    ZIP_TIME = (2026, 9, 25, 0, 0, 0)
    NAVIGATION_ENTRIES = 254
    COVERAGE = "248/722 units; OLP-0004-0251"
    DESCRIPTION = (
        "ગુજરાતી સંચિત આવૃત્તિ: ૭૨૨માંથી ૨૪૮ મૂળ એકમો, OLP-0004–0251. "
        "પહેલાંનાં ૨૦૪ એકમો OpenAI Codex GPT-5.6 Sol, Ultra effort વડે "
        "અને નવા ૪૪ એકમો GPT-6 Sol, Ultra effort વડે તૈયાર થયા છે."
    )
    ABOUT_COVERAGE = (
        "આ EPUB એક પ્રવાહી, લિપિઆકાર બદલાય એવું ગુજરાતી વાચન છે. તેમાં "
        "૭૨૨ મૂળ એકમોમાંથી ૨૪૮ એકમો, એટલે OLP-0004થી OLP-0251 સુધીનો "
        "સતત આંશિક વિસ્તાર છે. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે."
    )
    ABOUT_SCOPE = (
        "આ સંચિત આવૃત્તિમાં અગાઉના પ્રકરણો સાથે સંગણનીયતા ભાગનાં "
        "પુનરાવર્તી વિધેયો અને સંગણનીયતા સિદ્ધાંતનાં સંપૂર્ણ પ્રકરણો સામેલ છે. "
        "અટકવાની સમસ્યા, સંગણકીય રીતે પરિગણનીય ગણો, બહુ-એક ન્યૂનીકરણ, "
        "રાઇસનું પ્રમેય અને સ્થિર-બિંદુ પ્રમેયનો સમાવેશ છે."
    )
''' + code[end:]

before = ("આ યંત્ર દ્વારા કરેલો અનુવાદ છે. અગાઉનાં ૨૦૪ એકમો OpenAI Codex GPT-5.6 Sol, "
          "Ultra effort વડે અને નવા ૨૦ એકમો OpenAI Codex GPT-6 Sol, Ultra effort વડે")
after = ("આ યંત્ર દ્વારા કરેલો અનુવાદ છે. અગાઉનાં ૨૦૪ એકમો OpenAI Codex GPT-5.6 Sol, "
         "Ultra effort વડે અને નવા ૪૪ એકમો OpenAI Codex GPT-6 Sol, Ultra effort વડે")
assert code.count(before) == 1
code = code.replace(before, after)

generated = ROOT / "tools" / "build_computability_theory_epub_expanded.py"
generated.write_text(code, encoding="utf-8", newline="\n")
sys.argv = [sys.argv[0], "computability-theory"]
exec(compile(code, str(generated), "exec"),
     {"__name__": "__main__", "__file__": str(generated)})
