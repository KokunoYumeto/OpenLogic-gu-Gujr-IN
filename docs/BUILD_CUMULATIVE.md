# Cumulative build through first-order tableaux

From the repository root:

    python tools/prepare_tableaux.py
    python tools/build_functions_html.py tableaux
    .\tools\build_sets_guarded.ps1 -Edition tableaux -TimeoutMs 15000

Preparation covers all 108 aligned source units and writes the cumulative TeX body plus exact input hashes for the 104 rendered inputs; four higher-level drivers are represented by the cumulative wrapper structure. The HTML builder produces `reader/tableaux.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, thirteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, fifty signed analytic tableaux, and internal source anchors. The guarded TeX build produces `build/gu-tableaux.pdf`.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current tableaux build completed all three passes; all three 144-page PDFs are byte-identical at SHA-256 `3bbc0dd6e7f3b31cefce2935f054e989e4145070492b4efed13331611fe8244a`. All 144 final pages were rendered with Poppler and visually inspected.

The verified 144-page PDF is published in the First-Order Tableaux v0.5.0 release and preserved as the human-readable preview for Zenodo DOI `10.5281/zenodo.22649735`.

The same script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, `-Edition sequent-calculus`, or `-Edition natural-deduction`. The `tableaux` edition is the current 108-unit target.

Publication requires more than a successful build: render every page to PNG, inspect every page for Gujarati shaping, clipping, overlaps, missing glyphs, diagrams, proof displays, footnotes, references, and source-correction boxes, then bind the inspected PDF hash into the final QA receipt. `provenance/PDF_QA_011.json` records that completed check. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
