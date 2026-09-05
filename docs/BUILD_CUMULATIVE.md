# Cumulative build through first-order sequent calculus

From the repository root:

    python tools/prepare_sequent_calculus.py
    python tools/build_functions_html.py sequent-calculus
    .\tools\build_sets_guarded.ps1 -Edition sequent-calculus -TimeoutMs 15000

Preparation covers all 80 aligned source units and writes the cumulative TeX body plus exact input hashes for the 76 rendered inputs; four higher-level drivers are represented by the cumulative wrapper structure. The HTML builder produces `reader/sequent-calculus.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, thirteen SVG diagrams, recursively rendered LK rule and proof trees, and internal source anchors. The guarded TeX build produces `build/gu-sequent-calculus.pdf`.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current sequent-calculus build completed all three passes; all three 100-page PDFs are byte-identical at SHA-256 `654565f746938f91a2d3ff9ade7f019c276927cb12b9728e99379c2a90365861`. All 100 final pages were rendered with Poppler and visually inspected.

The same script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, or `-Edition proof-systems`. The `sequent-calculus` edition is the current 80-unit target.

Publication requires more than a successful build: render every page to PNG, inspect every page for Gujarati shaping, clipping, overlaps, missing glyphs, diagrams, proof displays, footnotes, references, and source-correction boxes, then bind the inspected PDF hash into the final QA receipt. `provenance/PDF_QA_009.json` records that completed check. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
