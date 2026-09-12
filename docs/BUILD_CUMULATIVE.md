# Cumulative build through first-order completeness

From the repository root:

    python tools/prepare_completeness.py
    python tools/build_functions_html.py completeness
    .\tools\build_sets_guarded.ps1 -Edition completeness -TimeoutMs 15000
    python tools/build_epub.py

Preparation covers all 134 aligned source units and writes the cumulative TeX body plus exact input hashes for the 130 rendered inputs; four higher-level drivers are represented by the cumulative wrapper structure. The HTML builder produces `reader/completeness.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, six line-numbered axiomatic derivation tables, thirteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, fifty signed analytic tableaux, and internal source anchors. The guarded TeX build produces `build/gu-completeness.pdf`. The EPUB builder consumes the accepted HTML reader and produces `releases/OpenLogic-gu-Gujr-IN-Completeness.epub`, a deterministic reflowable EPUB 3.3 publication with XHTML, native MathML, Gujarati metadata and fonts, described figures, a 145-link navigation document, landmarks, and an explicit 134/722 partial-edition disclosure.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current completeness build completed all three passes; all three 174-page PDFs are byte-identical at SHA-256 `004bce94570b7f986addad0188f6970d86e2a4f9b5ac3a256f4e96df194d3a6a`. All 174 final pages were rendered with Poppler and visually inspected.

The EPUB builder also performs a cold replay. The canonical and replay files are byte-identical at 445,804 bytes and SHA-256 `991e26b9df64a6c4afa18781935772ff20f2ae5f707765c01e5cd5609d052c6e`. EPUBCheck 5.3.0 reports zero fatal errors, errors, warnings, or informational messages. Exact structural QA verifies all 7,278 MathML subtrees and TeX annotations, the Gujarati character stream, 558 content IDs, 145 navigation links, 208 proof representations, 13 described SVG figures, 11 tables, 12 footnotes, and all 93 source-correction disclosures. Silent Chromium inspection of byte-identical XHTML checked representative navigation, theorem, MathML, figure, editorial-note, and bibliography views; fonts and all images loaded, no unhandled mathematical clipping occurred, and the console was clean.

The verified PDF and EPUB are published in the [First-Order Completeness v0.7.0 release](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/completeness-v0.7.0) and preserved in the existing Zenodo lineage at [DOI 10.5281/zenodo.22726447](https://doi.org/10.5281/zenodo.22726447).

To validate an EPUB independently with EPUBCheck 5.3.0 or later:

    java -jar path\to\epubcheck.jar releases\OpenLogic-gu-Gujr-IN-Completeness.epub --json build\EPUBCHECK.json

The same guarded TeX script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, `-Edition sequent-calculus`, `-Edition natural-deduction`, `-Edition tableaux`, or `-Edition axiomatic-deduction`. The `completeness` edition is the current 134-unit target.

Publication requires the completed validation described above and final hash binding in the QA receipts. `provenance/PDF_QA_013.json`, `provenance/EPUB_QA_013.json`, and `provenance/CUMULATIVE_QA_013.json` record those checks. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
