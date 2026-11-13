# ગણો, તર્ક, સંગણન

અધિતર્કનો મુક્ત પરિચય. ગુજરાતી આવૃત્તિમાં ગણો, સંબંધો અને ફલનો, પ્રથમ-ક્રમ તર્ક, સ્વાભાવિક નિગમન, સિક્વન્ટ કલન અને ટ્યુરિંગ મશીનોનો અભ્યાસ છે. તેમાં પ્રસ્તાવના, બાર પ્રકરણસાર, પરિશિષ્ટો અને પરિભાષાકોશ છે.

[ગુજરાતી પુસ્તક વાંચો (પીડીએફ)](slc-screen-gu.pdf)

## શ્રેય અને પરવાના

મૂળ પુસ્તક *Sets, Logic, Computation* Richard Zachનું છે અને તે Open Logic Projectના *The Open Logic Text* પર આધારિત છે. બંને પાઠો [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) પરવાના હેઠળ છે. આ અનુવાદે [મૂળ પુસ્તકની આવૃત્તિ](https://github.com/rzach/sets-logic-computation/tree/6178f32f61645f3b62ef621b4c5a88f8e67778ad) અને [Open Logic Projectની આવૃત્તિ](https://github.com/OpenLogicProject/OpenLogic/tree/1e960beff9ed7835bf3e3f1335e21af3439cd107) વાપરી છે.

પુસ્તક-વિશિષ્ટ ગુજરાતી અનુવાદ અને ગોઠવણી OpenAI Codexના GPT-6.1 Sol (Ultra) વડે કૃત્રિમ બુદ્ધિથી તૈયાર થયાં છે. સમાવેલા પ્રકરણો ગુજરાતી Open Logic Projectની [પૂર્ણ આવૃત્તિ v1.2.0](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/tree/3e743c5d2bfd8dd246d36bda047b6b7b8e98116d)માંથી છે. એ ગુજરાતી આવૃત્તિનો અનુવાદ OpenAI Codexના GPT-5.6 Sol, GPT-6 Sol અને GPT-6.1 Sol (Ultra) વડે તૈયાર થયો છે. મૂળ માનવીય લેખનનો શ્રેય તેના લેખકોને છે.

Matthew Leadbeaterનાં મુખપૃષ્ઠ અને ભાગચિત્રો [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) હેઠળ છે. જીવનચરિત્રોમાં વપરાયેલા ફોટોગ્રાફ માટે પુસ્તકમાં આપેલો વ્યક્તિગત શ્રેય અને વપરાશની શરતો લાગુ પડે છે. સ્રોતો, મોડેલ અને આવૃત્તિઓ [મેનિફેસ્ટમાં](MANIFEST.json) નોંધેલાં છે.

## પીડીએફ બનાવવી

આ ભંડારના મુખ્ય ફોલ્ડરમાંથી PowerShell 7 વડે ચલાવો.

```powershell
pwsh -NoProfile -File textbooks/slc/build.ps1
```

Python 3.10 કે પછીનું સંસ્કરણ અને LuaLaTeX, BibTeX તથા MakeIndex ધરાવતું TeX સ્થાપન જરૂરી છે. TeXમાં Babelનું Gujarati સ્થાનકીકરણ, HarfBuzz, fontspec, memoir, newtx, glossaries, truncate, pdfx અને Open Logic Projectના સામાન્ય પૅકેજો ઉપલબ્ધ હોવા જોઈએ. Gujarati અક્ષરરૂપ ભંડારમાં છે. આ આદેશ સ્થિર સ્રોતોને ચકાસે છે, `locale/gu` બનાવે છે અને `textbooks/slc/slc-screen-gu.pdf`માં પુસ્તક મૂકે છે. ગોઠવણી અને કમ્પાઇલરની નોંધો અવગણેલી `.build` ડિરેક્ટરીમાં મળે છે.

પરિભાષાકોશના સૉર્ટ ક્રમની ચકાસણી માટે ICU સાથેનું Node.js વાપરો.

```powershell
node textbooks/slc/sort-glossary.mjs --check
```

મૂળ [અંગ્રેજી પીડીએફ](https://slc.openlogicproject.org/slc-screen.pdf)ની મેનિફેસ્ટમાં નોંધાયેલી નકલ સામે પ્રકરણો અને અંગ્રેજી અંશો તપાસવા Pythonમાં `pypdf` અને PATH પર Popplerનું `pdftotext` જરૂરી છે. `--reference` પછી અંગ્રેજી પીડીએફનો સ્થાનિક માર્ગ આપો.

```powershell
python textbooks/slc/audit.py --reference upstream-slc-screen.pdf --report slc-gu-audit.json
```
