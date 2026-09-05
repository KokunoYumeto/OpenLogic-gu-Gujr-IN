# Cumulative build through the proof-systems overview

From the repository root:

    python tools/prepare_proof_systems.py
    python tools/build_functions_html.py proof-systems
    .\tools\build_sets_guarded.ps1 -Edition proof-systems -TimeoutMs 15000

Preparation covers all 65 aligned source units and writes the cumulative TeX body plus exact input hashes for the 61 rendered inputs; four higher-level drivers are represented by the cumulative wrapper structure. The HTML builder produces `reader/proof-systems.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, thirteen SVG diagrams, four explicit proof-system representations, and internal source anchors. The guarded TeX build produces `build/gu-proof-systems.pdf`.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current proof-systems build completed all three passes; all three 79-page PDFs are byte-identical at SHA-256 `dc9dac4d37335cba20eda1411383059ad9822dcf8fbcbb84e2ba75fd590d12c5`. All 79 final pages were rendered with Poppler and visually inspected.

The same script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, or `-Edition propositional`. The `proof-systems` edition is the current 65-unit target.

Publication requires more than a successful build: render every page to PNG, inspect every page for Gujarati shaping, clipping, overlaps, missing glyphs, diagrams, proof displays, footnotes, references, and source-correction boxes, then bind the inspected PDF hash into the final QA receipt. `provenance/PDF_QA_008.json` records that completed check. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
