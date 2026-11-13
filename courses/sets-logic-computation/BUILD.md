# ગણો, તર્ક, સંગણન

ZIP ખોલીને તેના મુખ્ય ફોલ્ડરમાંથી Windows પર PowerShell 7 વડે ચલાવો.

```powershell
pwsh -NoProfile -File build.ps1 -SourceTree source
```

સંપૂર્ણ સંપાદનીય `slc-screen-gu.tex`માંથી એ જ પાઠ બનાવવા:

```powershell
pwsh -NoProfile -File build.ps1 -SourceTree source -Cumulative
```

Python 3 અને LuaLaTeX, BibTeX, MakeIndex ધરાવતું TeX સ્થાપન જરૂરી છે.
Gujarati Babel, HarfBuzz, fontspec, memoir, adjustbox, glossaries અને
pdfx તથા Open Logic Projectના સામાન્ય TeX પૅકેજો ઉપલબ્ધ રાખો.
ગુજરાતી ફોન્ટ, Open Logic શૈલી અને પુસ્તકનાં ચિત્રો આ ZIPમાં છે.

મૂળ પુસ્તક Richard Zachનું છે અને પાઠ Open Logic Project પર આધારિત છે.
લખાણ CC BY 4.0 હેઠળ છે. Matthew Leadbeaterનાં ચિત્રો CC BY-NC 4.0 હેઠળ
છે. ફોટોગ્રાફની વ્યક્તિગત શરતો `source/assets/photos/README.md` અને પુસ્તકમાં
છે. ફોન્ટની શરતો `source/fonts/OFL.txt`માં છે. પુસ્તક-વિશિષ્ટ ગુજરાતી
અનુવાદ OpenAI Codexના GPT-6.1 Sol (Ultra) વડે તૈયાર થયો છે.
