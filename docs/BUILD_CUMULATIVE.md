# સંચિત ગુજરાતી આવૃત્તિ કેવી રીતે બનાવવી

OLP-0004–0263ના હાલના 260/722 એકમો માટે સંગ્રહની મુખ્ય નિર્દેશિકામાંથી નીચેના આદેશ ચલાવો:

```powershell
python tools/prepare_turing_machines.py
python tools/build_turing_machines_html.py
.\tools\build_sets_guarded.ps1 -Edition turing-machines -TimeoutMs 60000
python tools/build_turing_machines_epub.py
```

HTML વાચક `reader/turing-machines.html`, PDF `build/gu-turing-machines.pdf` અને EPUB `releases/OpenLogic-gu-Gujr-IN-Turing-Machines.epub`માં મળે છે. સંપૂર્ણ સંચિત લખાણની સીધી TeX ફાઇલ `releases/OpenLogic-gu-Gujr-IN-Turing-Machines-Full-Text.tex` છે. સંપૂર્ણ સ્રોત ZIPના ફોન્ટ, શૈલી, આકૃતિ અને ગ્રંથસૂચિ આધાર સાથે તેમાંથી PDF ફરી બનાવવા નિયંત્રિત બિલ્ડમાં `-InputFile releases\OpenLogic-gu-Gujr-IN-Turing-Machines-Full-Text.tex` ઉમેરો. સ્વીકૃત 316-પાનાના PDF સાથે ત્રણેય પાસના બાઇટ્સ સમાન મળ્યા. [પૂર્ણ સ્રોતની તપાસ](../provenance/FULL_TEXT_SOURCE_QA_025.json), [સંચિત ગુણવત્તા નોંધ](../provenance/CUMULATIVE_QA_025.json), [પ્રકરણની સમીક્ષા](TURING_MACHINES_REVIEW.md), [GitHub આવૃત્તિ](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/turing-machines-v0.19.0) અને [Zenodo DOI](https://doi.org/10.5281/zenodo.22970545) વિગતો આપે છે.

## અગાઉની સંગણનીયતા સિદ્ધાંત આવૃત્તિ

OLP-0004–0251ના 248/722 એકમો માટે સંગ્રહની મુખ્ય નિર્દેશિકામાંથી નીચેના આદેશ ચલાવો:

```powershell
python tools/prepare_computability_theory.py
python tools/build_computability_theory_html.py
.\tools\build_sets_guarded.ps1 -Edition computability-theory -TimeoutMs 60000
python tools/build_computability_theory_epub.py
```

HTML વાચક `reader/computability-theory.html`, PDF `build/gu-computability-theory.pdf` અને EPUB `releases/OpenLogic-gu-Gujr-IN-Computability-Theory.epub`માં મળે છે. સંચિત પૂર્ણ-લખાણની સીધી TeX ફાઇલ `releases/OpenLogic-gu-Gujr-IN-Computability-Theory-Full-Text.tex` છે. સાથેની સંપૂર્ણ સ્રોત ZIPના ફોન્ટ, શૈલી, આકૃતિ અને ગ્રંથસૂચિ આધાર સાથે તેનો ચોક્કસ PDF ફરી બનાવવા `-InputFile releases\OpenLogic-gu-Gujr-IN-Computability-Theory-Full-Text.tex` ઉમેરો. ત્રણ નિયંત્રિત પાસના બાઇટ્સ સ્વીકૃત 304-પાનાના PDF સાથે સમાન મળ્યા. [પૂર્ણ સ્રોતની તપાસ](../provenance/FULL_TEXT_SOURCE_QA_024.json), [સંચિત ગુણવત્તા નોંધ](../provenance/CUMULATIVE_QA_024.json), [નવી સમીક્ષા](COMPUTABILITY_REVIEW.md), [GitHub આવૃત્તિ](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/computability-theory-v0.18.0) અને [Zenodo DOI](https://doi.org/10.5281/zenodo.22951232) વિગતો આપે છે.

## અગાઉની લિન્ડસ્ટ્રોમ આવૃત્તિ

સંગ્રહની મુખ્ય નિર્દેશિકામાંથી નીચેના આદેશ આ ક્રમમાં ચલાવો:

```powershell
python tools/prepare_lindstrom.py
python tools/build_lindstrom_html.py
.\tools\build_sets_guarded.ps1 -Edition lindstrom -TimeoutMs 60000
python tools/build_lindstrom_epub.py
```

તૈયારીની પ્રક્રિયા OLP-0004–OLP-0207 સુધીના **204 અનુરૂપ ગુજરાતી સ્રોત એકમો**નું સંચિત TeX લખાણ અને ચોક્કસ ઇનપુટ-હૅશ બનાવે છે. HTML પ્રક્રિયા `reader/lindstrom.html` તૈયાર કરે છે. તેમાં Unicode ગુજરાતી ગદ્ય, મૂળ MathML, સ્થાનિક ફોન્ટ, પાંચ સત્યતા કોષ્ટકો, છ ક્રમ-ચિહ્નિત સ્વયંસિદ્ધ નિષ્પત્તિ કોષ્ટકો, 15 વર્ણનવાળી SVG આકૃતિઓ, પુરાવા અને વિશ્લેષણાત્મક ટેબ્લો તથા આંતરિક સ્રોત-કડીઓ છે. નિયંત્રિત TeX પ્રક્રિયાનું પરિણામ `build/gu-lindstrom.pdf` છે. EPUB પ્રક્રિયા સ્વીકૃત HTMLમાંથી `releases/OpenLogic-gu-Gujr-IN-Lindstrom.epub` બનાવે છે; તેમાં ગુજરાતી મેટાડેટા, MathML, સ્થાનિક ફોન્ટ, 210 માર્ગદર્શક કડીઓ અને 204/722 જેટલો અધૂરો વ્યાપ સ્પષ્ટ નોંધાયેલો છે.

TeX પ્રક્રિયા મર્યાદિત રાહ સાથે વૈશ્વિક mutex `Global\InterlanguageTeXSlotV1` મેળવે છે અને પોતાના ત્રણેય LuaLaTeX ફેરા તથા લૉગ-તપાસ પૂરી ન થાય ત્યાં સુધી તેને રાખે છે. mutex ન મળે તો કોઈ TeX પ્રક્રિયા શરૂ થતી નથી. શેલ-એસ્કેપ તથા ઇન્સ્ટૉલર ઍક્સેસ બંધ છે; સમયમર્યાદા વટે તો સ્ક્રિપ્ટ માત્ર પોતે શરૂ કરેલી પ્રક્રિયા બંધ કરી શકે છે. સ્વીકૃત બિલ્ડમાં ત્રણેય 260-પાનાના PDF બાઇટ-દર-બાઇટ સમાન છે; તેમનો SHA-256 `129753a75224434ad65ea0a40356e868084eaec414b9da43b5e9aec392bfeb73` છે. બધા 260 પાનાં Popplerથી ચિત્રરૂપે ઉતારીને દૃષ્ટિથી તપાસાયા.

EPUBનું ઠંડા આરંભથી પુનઃબિલ્ડ મૂળ ફાઇલ સાથે બાઇટ-દર-બાઇટ સમાન છે. 611,382 બાઇટની EPUB ફાઇલનો SHA-256 `6276bc4a9b650a397ebc285ac79acd9769db98af86017e91eb68fbf6416da146` છે. EPUBCheck 5.3.0એ ગંભીર ભૂલ, ભૂલ, ચેતવણી કે માહિતી સંદેશ — કોઈ પણ આપ્યો નથી. બાંધકામની તપાસમાં 12,178 MathML અભિવ્યક્તિઓ તથા તેમની TeX નોંધો, ગુજરાતી અક્ષરપ્રવાહ, 772 ઓળખચિહ્નો, 210 માર્ગદર્શક કડીઓ, 208 પુરાવા-પ્રસ્તુતિઓ, 15 આકૃતિઓ અને 175 ચાવીબદ્ધ ખુલાસા યથાવત્ મળ્યા. Chromiumમાં HTML અને EPUBના ચોક્કસ લખાણ પર દૃશ્ય તપાસ પણ પસાર થઈ.

EPUBને સ્વતંત્ર રીતે તપાસવા માટે EPUBCheck 5.3.0 કે પછીનું સ્વરૂપ વાપરો:

```powershell
java -jar path\to\epubcheck.jar releases\OpenLogic-gu-Gujr-IN-Lindstrom.epub --json build\EPUBCHECK.json
```

અગાઉની સંચિત આવૃત્તિઓ માટે એ જ નિયંત્રિત TeX સ્ક્રિપ્ટમાં લાગુ પડતું `-Edition` નામ આપી શકાય છે. અહીં વર્ણવાયેલું અગાઉનું પ્રકાશન લક્ષ્ય `lindstrom` હતું. ગુણવત્તા-તપાસની વિગત `provenance/PDF_QA_022.json`, `provenance/EPUB_QA_022.json` અને `provenance/CUMULATIVE_QA_022.json`માં છે. પ્રકાશિત [v0.16.0 આવૃત્તિ](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/lindstrom-v0.16.0) અને [Zenodo DOI](https://doi.org/10.5281/zenodo.22865986) પરથી આઠેય ફાઇલો અનામી રીતે પાછી વાંચીને સરખાવાઈ છે. પરિભાષા માટે વાંચેલા તૃતીય-પક્ષના મૂળ PDF સ્થાનિક સંશોધન પુરાવા છે; પ્રકાશિત ફાઇલોમાં તેમનો સમાવેશ થતો નથી.

આ આવૃત્તિની રચના, ભાષાંતર, ગણિતીય સુધારા અને મૂળ ચકાસણીઓનું AI કાર્ય OpenAI Codex — GPT-5.6 Sol, Ultra effort દ્વારા થયું. આ ગુજરાતી બિલ્ડ-માર્ગદર્શિકાનું સંપાદન OpenAI Codex — GPT-6 Sol, Ultra effort દ્વારા થયું; સ્વતંત્ર માનવીય પ્રમાણિત સમીક્ષા થયેલી નથી.
