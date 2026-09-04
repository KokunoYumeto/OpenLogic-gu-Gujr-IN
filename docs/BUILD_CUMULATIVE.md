# Cumulative Sets and Relations build

From the repository root:

    python tools/prepare_foundations.py
    python tools/build_foundations_html.py
    .\tools\build_sets_guarded.ps1 -Edition foundations -TimeoutMs 15000

The HTML builder reuses the three checked set-diagram SVGs and generates three graph/tree SVGs. The PDF is build/gu-foundations.pdf. Preparation reads all fourteen aligned sections, expands Gujarati inflections and records input hashes.

The bounded global mutex remains held across all three owned TeX passes and log checks. Failed acquisition starts no TeX process. Installer and shell escape are disabled. Only a captured owned process can be terminated after timeout. The default edition remains sets. See BUILD.md for font/runtime details.

The PDF adds separate editorial notes and the cited Benacerraf bibliography. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
