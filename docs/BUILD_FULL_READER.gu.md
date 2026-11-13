# ગુજરાતી PDF અને EPUB બનાવવાં

પૂર્ણ સ્રોત ZIP ખોલીને તેના મૂળ ફોલ્ડરમાંથી બિલ્ડ કરો. `reader/full-reader.tex`માં બધો પાઠ, સંદર્ભગ્રંથો અને ફોટોગ્રાફનો શ્રેય છે. સીધી ડાઉનલોડ થતી `02-OpenLogic-gu-Gujr-IN-Full-Text.tex`ના બાઇટ્સ એ જ છે. શૈલી, ફોન્ટ અને ચિત્રો માટે ZIPના સાથી ફોલ્ડર જરૂરી છે.

PDF માટે PowerShell 7 અને MiKTeX LuaLaTeX તથા સામાન્ય TeX પૅકેજો વાપરો:

```powershell
& .\tools\build_full_reader_guarded.ps1 -BuildSubdir full-reader-sync-1e960bef -JobName gu-full-reader-sync-1e960bef
```

PDF `build/full-reader-sync-1e960bef/gu-full-reader-sync-1e960bef.pdf`માં મળે છે. ગ્રંથસૂચિ સીધી TeXમાં છે; BibTeX જરૂરી નથી. મૂળ `.bib` અને `.bst` સાથી સ્રોતમાં છે. સ્ક્રિપ્ટ shell escape અને પૅકેજોનું સ્વયંસ્થાપન બંધ રાખે છે. અન્ય TeX, ફોન્ટ કે converter સંસ્કરણથી બાઇટ્સ બદલાઈ શકે છે.

EPUB માટે Python 3, Pandoc અને Python પૅકેજો `beautifulsoup4`, `lxml`, `PyMuPDF`, `fonttools` જરૂરી છે. પહેલાં PDF બિલ્ડ કરો, જેથી સૂત્ર અને આકૃતિના સંદર્ભો તેની વર્તમાન `.aux` ફાઇલ પરથી આવે. પછી:

```powershell
python -X utf8 .\tools\prepare_full_epub_html.py
python -X utf8 .\tools\audit_full_epub_figures.py
python -X utf8 .\tools\build_full_epub.py
```

EPUB `build/OpenLogic-gu-Gujr-IN-Full-draft.epub`માં મળે છે. અહીં `draft` સાધનની ફાઇલ-નામ પરંપરા છે. EPUBCheckથી EPUBનું માળખું તપાસી શકાય છે.

સંપાદનીય ગુજરાતી મોડ્યુલો `gu/content`માં અને સ્થિર અંગ્રેજી મૂળ `upstream/content`માં છે. સીધો સંપૂર્ણ વાચનપાઠ `reader/full-reader.tex`માં અને તેનો સંલગ્ન મુખ્ય પાઠ `reader/full-reader-resolved-body.tex`માં છે. મૂળ મોડ્યુલો આયાત-માળખું વાપરે છે અને એકલા નાના દસ્તાવેજ તરીકે કમ્પાઇલ થતા નથી. ભાગવાર TeX સંપૂર્ણ પ્રોજેક્ટ સાથે સંપાદન માટે છે.

`reader/figures/native`માં સંપાદનીય TikZ આકૃતિઓના વેક્ટર SVG રૂપ છે. તેમની સાથેના સ્રોત-બંધનો આકૃતિ, વ્યાખ્યા અને શૈલીના ચોક્કસ બાઇટ્સ ઓળખે છે. આકૃતિ કે તેની વ્યાખ્યા બદલાય ત્યારે વેક્ટર રૂપ પણ ફરી બનાવવું જરૂરી છે. અન્ય સંબંધ અને ટ્યુરિંગ આકૃતિઓ converter તેમના સંપાદનીય સ્રોત પરથી બનાવે છે. બધા આકૃતિ-લેબલ મૂળ TeXમાં સંપાદનીય છે.

`SOURCE_INVENTORY.json` ZIPમાં રહેલી ફાઇલો અને તેમના SHA-256 સરવાળા આપે છે. લખાણ, ફોટોગ્રાફ, ફોન્ટ અને અન્ય ઘટકોના મૂળ શ્રેય તથા પરવાના જાળવો; [પરવાના-નોંધ](LICENSE_NOTES.md) જુઓ.
