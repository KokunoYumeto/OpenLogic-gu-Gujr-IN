"""Build deterministic 224-unit EPUB from the checked Gujarati HTML reader."""

from pathlib import Path
import sys

from build_lindstrom_epub import code as lindstrom_code


ROOT = Path(__file__).resolve().parents[1]
template = ROOT / "tools" / "build_first_order_introduction_epub.py"
code = lindstrom_code


def replace_once(before, after):
    global code
    assert code.count(before) == 1, (before, code.count(before))
    code = code.replace(before, after)


replace_once(
    '"models-arithmetic", "interpolation", "lindstrom"}',
    '"models-arithmetic", "interpolation", "lindstrom", "computability"}',
)
branch = '''
elif EDITION == "computability":
    INPUT = ROOT / "reader" / "computability.html"
    OUTPUT = ROOT / "releases" / "OpenLogic-gu-Gujr-IN-Recursive-Functions.epub"
    REPLAY = ROOT / "build" / "OpenLogic-gu-Gujr-IN-Recursive-Functions-replay.epub"
    STAGE = ROOT / "build" / "epub023-stage"
    REPLAY_STAGE = ROOT / "build" / "epub023-replay-stage"
    RECEIPT = ROOT / "build" / "EPUB_BUILD_RECEIPT_023.json"
    TITLE = "પુનરાવર્તી વિધેયો સહિત ઓપન લોજિક ગુજરાતી"
    IDENTIFIER = (
        "https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/"
        "releases/tag/recursive-functions-v0.17.0"
    )
    MODIFIED = "2026-09-25T00:00:00Z"
    ZIP_TIME = (2026, 9, 25, 0, 0, 0)
    NAVIGATION_ENTRIES = 230
    COVERAGE = "224/722 units; OLP-0004-0227"
    DESCRIPTION = (
        "ગુજરાતી સંચિત આવૃત્તિ: ૭૨૨માંથી ૨૨૪ મૂળ એકમો, OLP-0004–0227. "
        "પહેલાંનાં ૨૦૪ એકમો OpenAI Codex GPT-5.6 Sol, Ultra effort વડે "
        "અને નવા ૨૦ એકમો GPT-6 Sol, Ultra effort વડે તૈયાર થયા છે."
    )
    ABOUT_COVERAGE = (
        "આ EPUB એક પ્રવાહી, લિપિઆકાર બદલાય એવું ગુજરાતી વાચન છે. તેમાં "
        "૭૨૨ મૂળ એકમોમાંથી ૨૨૪ એકમો, એટલે OLP-0004થી OLP-0227 સુધીનો "
        "સતત આંશિક વિસ્તાર છે. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે."
    )
    ABOUT_SCOPE = (
        "આ સંચિત આવૃત્તિમાં અગાઉના પ્રકરણો સાથે સંગણનીયતા ભાગની શરૂઆત "
        "અને પુનરાવર્તી વિધેયોનું સંપૂર્ણ પ્રકરણ ઉમેરાયું છે. આદિમ અને "
        "આંશિક પુનરાવર્તન, કોડિંગ, સીમિત શોધ, ક્લીનીનું સામાન્ય સ્વરૂપ "
        "અને અટકવાની સમસ્યા સામેલ છે. સંગણનીયતા સિદ્ધાંતનું આગળનું "
        "પ્રકરણ હજી સામેલ નથી."
    )
'''
marker = "\n\n\ndef require(condition: bool, message: str) -> None:\n"
replace_once(marker, "\n" + branch + marker)
replace_once(
    'expected_assets = 15 if EDITION == "lindstrom" else (14 if EDITION == "interpolation" else 13)',
    'expected_assets = 15 if EDITION in {"lindstrom", "computability"} else (14 if EDITION == "interpolation" else 13)',
)
replace_once(
    '"આ યંત્ર દ્વારા કરેલો અનુવાદ છે, જેને મૂળ સાથેના રચનાત્મક અને અર્થલક્ષી સરખામણાં, ગુજરાતી શાસ્ત્રીય સ્રોતોની નોંધ, EPUBCheck અને પ્રતિનિધિ દૃશ્ય તપાસથી ચકાસવામાં આવ્યો છે. સ્વતંત્ર ગુજરાતી નિષ્ણાતનું પ્રમાણપત્ર મળ્યું નથી.",',
    '"આ યંત્ર દ્વારા કરેલો અનુવાદ છે. અગાઉનાં ૨૦૪ એકમો OpenAI Codex GPT-5.6 Sol, Ultra effort વડે અને નવા ૨૦ એકમો OpenAI Codex GPT-6 Sol, Ultra effort વડે તૈયાર થયા છે. મૂળ સાથે આ જ એજન્ટની રચનાત્મક અને અર્થલક્ષી સરખામણી થઈ છે; સ્વતંત્ર ગુજરાતી નિષ્ણાતનું પ્રમાણપત્ર મળ્યું નથી.",',
)
replace_once(
    '    dc("creator", "Open Logic Project; Gujarati machine translation")\n',
    '    dc("creator", "Open Logic Project; OpenAI Codex GPT-5.6 Sol Ultra and GPT-6 Sol Ultra Gujarati machine translation")\n',
)

# safe_clear() in the shared exporter verifies both resolved stage paths are
# direct children of this repository's build directory before recursive clear.

if __name__ == "__main__":
    generated = ROOT / "tools" / "build_computability_epub_expanded.py"
    generated.write_text(code, encoding="utf-8", newline="\n")
    sys.argv = [sys.argv[0], "computability"]
    exec(compile(code, str(generated), "exec"), {"__name__": "__main__", "__file__": str(template)})
