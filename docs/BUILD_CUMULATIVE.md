# Cumulative Sets, Relations, Functions, and Size build

From the repository root:

    python tools/prepare_size.py
    python tools/build_functions_html.py size
    .\tools\build_sets_guarded.ps1 -Edition size -TimeoutMs 15000

Preparation reads all 37 aligned source units and writes the cumulative TeX body plus its exact input hashes. The HTML builder produces `reader/size.html` with Unicode Gujarati text, native MathML, local fonts, eleven SVG diagrams, and internal source anchors. The guarded TeX build produces `build/gu-size.pdf`.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The final two PDF hashes must agree before visual QA begins.

The same script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, or `-Edition functions`. The `size` edition is the current 37-unit target.

Publication requires more than a successful build: render every page to PNG, inspect every page for Gujarati shaping, clipping, overlaps, missing glyphs, diagrams, footnotes, references, and source-correction boxes, then bind the inspected PDF hash into the final QA receipt. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
