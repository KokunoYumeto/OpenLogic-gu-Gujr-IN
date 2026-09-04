# Cumulative build through Propositional Logic syntax and semantics

From the repository root:

    python tools/prepare_propositional.py
    python tools/build_functions_html.py propositional
    .\tools\build_sets_guarded.ps1 -Edition propositional -TimeoutMs 15000

Preparation reads all 59 aligned source units and writes the cumulative TeX body plus its exact input hashes. The HTML builder produces `reader/propositional.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, thirteen SVG diagrams, and internal source anchors. The guarded TeX build produces `build/gu-propositional.pdf`.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current Propositional Logic build completed all three passes; the final two 73-page PDFs are byte-identical at SHA-256 `2dded6e59f70bfd61b6d0361bca269c5d3c8f37911a9352ab0cc6b61e4422ffa`. All 73 final pages were rendered with Poppler and visually inspected.

The same script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, or `-Edition infinite`. The `propositional` edition is the current 59-unit target.

Publication requires more than a successful build: render every page to PNG, inspect every page for Gujarati shaping, clipping, overlaps, missing glyphs, diagrams, footnotes, references, and source-correction boxes, then bind the inspected PDF hash into the final QA receipt. `provenance/PDF_QA_007.json` records that completed check. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
