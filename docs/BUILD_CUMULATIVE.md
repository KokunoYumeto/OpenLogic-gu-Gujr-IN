# Cumulative Sets, Relations, Functions, Size, Arithmetization, and Infinite Sets build

From the repository root:

    python tools/prepare_infinite.py
    python tools/build_functions_html.py infinite
    .\tools\build_sets_guarded.ps1 -Edition infinite -TimeoutMs 15000

Preparation reads all 51 aligned source units and writes the cumulative TeX body plus its exact input hashes. The HTML builder produces `reader/infinite.html` with Unicode Gujarati text, native MathML, local fonts, thirteen SVG diagrams, and internal source anchors. The guarded TeX build produces `build/gu-infinite.pdf`.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The latest Infinite Sets build completed all three passes, but their PDF hashes differed, so the PDF remains outside the publication gate and all-page visual QA has not begun. The final two PDF hashes must agree before visual QA begins.

The same script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, or `-Edition arithmetization`. The `infinite` edition is the current 51-unit target.

Publication requires more than a successful build: render every page to PNG, inspect every page for Gujarati shaping, clipping, overlaps, missing glyphs, diagrams, footnotes, references, and source-correction boxes, then bind the inspected PDF hash into the final QA receipt. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
