# Cumulative build through first-order natural deduction

From the repository root:

    python tools/prepare_natural_deduction.py
    python tools/build_functions_html.py natural-deduction
    .\tools\build_sets_guarded.ps1 -Edition natural-deduction -TimeoutMs 15000

Preparation covers all 94 aligned source units and writes the cumulative TeX body plus exact input hashes for the 90 rendered inputs; four higher-level drivers are represented by the cumulative wrapper structure. The HTML builder produces `reader/natural-deduction.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, thirteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, and internal source anchors. The guarded TeX build produces `build/gu-natural-deduction.pdf`.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current natural-deduction build completed all three passes; all three 121-page PDFs are byte-identical at SHA-256 `9cf3db8b374373bdb0f37cefa8ecff9e59db0da5b4a91e5df8df9591cd3b31a3`. All 121 final pages were rendered with Poppler and visually inspected.

The same script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, or `-Edition sequent-calculus`. The `natural-deduction` edition is the current 94-unit target.

Publication requires more than a successful build: render every page to PNG, inspect every page for Gujarati shaping, clipping, overlaps, missing glyphs, diagrams, proof displays, footnotes, references, and source-correction boxes, then bind the inspected PDF hash into the final QA receipt. `provenance/PDF_QA_010.json` records that completed check. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
