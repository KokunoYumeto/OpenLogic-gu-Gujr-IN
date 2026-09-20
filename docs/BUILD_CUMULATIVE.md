# Cumulative build through Models of Arithmetic

From the repository root:

    python tools/prepare_models_arithmetic.py
    python tools/build_functions_html.py models-arithmetic
    .\tools\build_sets_guarded.ps1 -Edition models-arithmetic -TimeoutMs 60000
    python tools/build_first_order_introduction_epub.py models-arithmetic

Preparation covers all 194 aligned source units and writes the cumulative TeX body plus exact input hashes. The HTML builder produces `reader/models-arithmetic.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, six line-numbered axiomatic derivation tables, thirteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, fifty signed analytic tableaux, and internal source anchors. The guarded TeX build produces `build/gu-models-arithmetic.pdf`. The EPUB builder consumes the accepted HTML reader and produces `releases/OpenLogic-gu-Gujr-IN-Models-of-Arithmetic.epub`, a deterministic reflowable EPUB 3.3 publication with XHTML, native MathML, Gujarati metadata and fonts, described figures, a 200-link navigation document, landmarks, and an explicit 194/722 partial-edition disclosure.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current build completed all three passes; all three 250-page PDFs are byte-identical at SHA-256 `b89dfb3d89f3dcdbf206b03056a38f31811bae351c44249854b27ff940693765`. All 250 final pages were rendered with Poppler and visually inspected.

The EPUB builder also performs a cold replay. The canonical and replay files are byte-identical at 585,940 bytes and SHA-256 `f37aeff33831e876354615c7cdd3b026b7aae3dabc6acafada7f5bc6e1f88dde`. EPUBCheck 5.3.0 reports zero fatal errors, errors, warnings, or informational messages. Exact structural QA verifies all 11,324 MathML subtrees and TeX annotations, the Gujarati character stream, 743 content IDs, 200 navigation links, 208 proof representations, 13 described SVG figures, 12 tables, 13 footnotes, all 152 keyed disclosures, and the withdrawal of the historical OLINF-002 false-positive classification. Silent Chromium inspection of byte-identical XHTML checked the new Models of Arithmetic sections, navigation, mathematical displays, figures, editorial notes, and end matter; fonts and images loaded, no unhandled mathematical clipping occurred, raw problem tags did not leak, and the target console was clean.

The prior reviewed 187-unit artifacts remain public as [Model Theory Basics v0.13.0](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/model-theory-basics-v0.13.0), preserved at [DOI 10.5281/zenodo.22851934](https://doi.org/10.5281/zenodo.22851934) in the existing Gujarati OpenLogic Zenodo lineage, with the PDF as the human-readable preview. Anonymous readback verified all eight artifact bytes, the direct full-text TeX, and all 1,317 source-archive inventory entries.

To validate an EPUB independently with EPUBCheck 5.3.0 or later:

    java -jar path\to\epubcheck.jar releases\OpenLogic-gu-Gujr-IN-Models-of-Arithmetic.epub --json build\EPUBCHECK.json

The same guarded TeX script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, `-Edition sequent-calculus`, `-Edition natural-deduction`, `-Edition tableaux`, `-Edition axiomatic-deduction`, `-Edition completeness`, `-Edition first-order-introduction`, `-Edition first-order-syntax`, `-Edition first-order-semantics`, `-Edition first-order-models-theories`, `-Edition beyond`, or `-Edition model-theory-basics`. The `models-arithmetic` edition is the current 194-unit target.

Publication requires the completed validation described above and final hash binding in the QA receipts. `provenance/PDF_QA_020.json`, `provenance/EPUB_QA_020.json`, and `provenance/CUMULATIVE_QA_020.json` record those checks. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
