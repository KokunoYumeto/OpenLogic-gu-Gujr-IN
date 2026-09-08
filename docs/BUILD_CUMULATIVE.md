# Cumulative build through first-order axiomatic deduction

From the repository root:

    python tools/prepare_axiomatic_deduction.py
    python tools/build_functions_html.py axiomatic-deduction
    .\tools\build_sets_guarded.ps1 -Edition axiomatic-deduction -TimeoutMs 15000

Preparation covers all 122 aligned source units and writes the cumulative TeX body plus exact input hashes for the 118 rendered inputs; four higher-level drivers are represented by the cumulative wrapper structure. The HTML builder produces `reader/axiomatic-deduction.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, six line-numbered axiomatic derivation tables, thirteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, fifty signed analytic tableaux, and internal source anchors. The guarded TeX build produces `build/gu-axiomatic-deduction.pdf`.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current axiomatic-deduction build completed all three passes; all three 158-page PDFs are byte-identical at SHA-256 `66379898ed8eb34bfb510d310275264102229928165e26f11a8fd7846e6265bc`. All 158 final pages were rendered with Poppler and visually inspected.

The previously verified 144-page PDF remains published in the First-Order Tableaux v0.5.0 release and preserved as the human-readable preview for Zenodo DOI `10.5281/zenodo.22649735`. The 158-page axiomatic-deduction artifact is the current release candidate.

The same script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, `-Edition sequent-calculus`, `-Edition natural-deduction`, or `-Edition tableaux`. The `axiomatic-deduction` edition is the current 122-unit target.

Publication requires more than a successful build: render every page to PNG, inspect every page for Gujarati shaping, clipping, overlaps, missing glyphs, diagrams, proof displays, footnotes, references, and source-correction boxes, then bind the inspected PDF hash into the final QA receipt. `provenance/PDF_QA_012.json` records that completed check. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
