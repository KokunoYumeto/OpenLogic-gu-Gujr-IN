"""Build the reproducible 204-unit Lindström EPUB checkpoint."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
template = ROOT / "tools" / "build_first_order_introduction_epub.py"
code = template.read_text(encoding="utf-8")

before_set = '"models-arithmetic", "interpolation"}'
after_set = '"models-arithmetic", "interpolation", "lindstrom"}'
assert code.count(before_set) == 1
code = code.replace(before_set, after_set)

marker = "\n\n\ndef require(condition: bool, message: str) -> None:\n"
branch = '''
elif EDITION == "lindstrom":
    INPUT = ROOT / "reader" / "lindstrom.html"
    OUTPUT = ROOT / "releases" / "OpenLogic-gu-Gujr-IN-Lindstrom.epub"
    REPLAY = ROOT / "build" / "OpenLogic-gu-Gujr-IN-Lindstrom-replay.epub"
    STAGE = ROOT / "build" / "epub022-stage"
    REPLAY_STAGE = ROOT / "build" / "epub022-replay-stage"
    RECEIPT = ROOT / "build" / "EPUB_BUILD_RECEIPT_022.json"
    TITLE = "લિન્ડસ્ટ્રોમનું પ્રમેય સહિત ઓપન લોજિક ગુજરાતી"
    IDENTIFIER = (
        "https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/"
        "releases/tag/lindstrom-v0.16.0"
    )
    MODIFIED = "2026-09-21T00:00:00Z"
    ZIP_TIME = (2026, 9, 21, 0, 0, 0)
    NAVIGATION_ENTRIES = 210
    COVERAGE = "204/722 units; OLP-0004-0207"
    DESCRIPTION = "Partial Gujarati cumulative edition: 204 of 722 tracked source units, OLP-0004-0207."
    ABOUT_COVERAGE = (
        "આ EPUB એક પ્રવાહી, લિપિઆકાર બદલાય એવું ગુજરાતી વાચન છે. તેમાં ૭૨૨ "
        "મૂળ એકમોમાંથી ૨૦૪ એકમો, એટલે OLP-0004થી OLP-0207 સુધીનો સતત "
        "આંશિક વિસ્તાર છે. સંપૂર્ણ ૭૨૨-એકમ આવૃત્તિનું કામ ચાલુ છે."
    )
    ABOUT_SCOPE = (
        "આ સંગ્રહમાં ગણો, સંબંધો, વિધેયો, ગણોનું કદ, અંકગણિતીકરણ, અનંત ગણો, "
        "વિધાનાત્મક તથા પ્રથમ-ક્રમ તર્કશાસ્ત્ર, તેની સાબિતી-પદ્ધતિઓ અને પૂર્ણતા, "
        "પ્રથમ-ક્રમના નિદર્શો અને સિદ્ધાંતો, પ્રથમ-ક્રમથી આગળનાં તર્કશાસ્ત્રો, "
        "નિદર્શસિદ્ધાંતના પાયા, અંકગણિતના નિદર્શો, અંતર્વેશન, અમૂર્ત "
        "તર્કશાસ્ત્રો અને લિન્ડસ્ટ્રોમનું પ્રમેય સમાવિષ્ટ છે."
    )
'''
assert code.count(marker) == 1
code = code.replace(marker, "\n" + branch + marker)

old_assets = 'expected_assets = 14 if EDITION == "interpolation" else 13'
new_assets = 'expected_assets = 15 if EDITION == "lindstrom" else (14 if EDITION == "interpolation" else 13)'
assert code.count(old_assets) == 1
code = code.replace(old_assets, new_assets)

old_about_assets = (
    '"ગણિત native MathMLમાં છે. તેર આકૃતિઓમાં ગુજરાતી વૈકલ્પિક વર્ણન છે. '
    'આંતરિક કડીઓ અને વિષયસૂચિ EPUBમાં જ ચાલે છે. MathMLનું દૃશ્યરૂપ વાંચન-સોફ્ટવેર '
    'પ્રમાણે થોડું બદલાઈ શકે છે."'
)
new_about_assets = (
    '"ગણિત native MathMLમાં છે. પંદર આકૃતિઓમાં ગુજરાતી વૈકલ્પિક વર્ણન છે. '
    'આંતરિક કડીઓ અને વિષયસૂચિ EPUBમાં જ ચાલે છે. MathMLનું દૃશ્યરૂપ વાંચન-સોફ્ટવેર '
    'પ્રમાણે થોડું બદલાઈ શકે છે."'
)
assert code.count(old_about_assets) == 1
code = code.replace(old_about_assets, new_about_assets)

if __name__ == "__main__":
    generated = ROOT / "tools" / "build_lindstrom_epub_expanded.py"
    generated.write_text(code, encoding="utf-8", newline="\n")
    sys.argv = [sys.argv[0], "lindstrom"]
    exec(compile(code, str(generated), "exec"), {"__name__": "__main__", "__file__": str(template)})
