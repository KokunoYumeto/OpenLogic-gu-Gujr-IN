# Cumulative Sets, Relations, Functions, Size, and Arithmetization build

From the repository root:

    python tools/prepare_arithmetization.py
    python tools/build_functions_html.py arithmetization
    .\tools\build_sets_guarded.ps1 -Edition arithmetization -TimeoutMs 15000

Preparation reads all 45 aligned source units and writes the cumulative TeX body plus its exact input hashes. The HTML builder produces `reader/arithmetization.html` with Unicode Gujarati text, native MathML, local fonts, twelve SVG diagrams, and internal source anchors. The guarded TeX build produces `build/gu-arithmetization.pdf`.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The final two PDF hashes must agree before visual QA begins.

The same script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, or `-Edition size`. The `arithmetization` edition is the current 45-unit target.

Publication requires more than a successful build: render every page to PNG, inspect every page for Gujarati shaping, clipping, overlaps, missing glyphs, diagrams, footnotes, references, and source-correction boxes, then bind the inspected PDF hash into the final QA receipt. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
