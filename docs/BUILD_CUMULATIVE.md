# Cumulative build through first-order syntax

From the repository root:

    python tools/prepare_first_order_syntax.py
    python tools/build_functions_html.py first-order-syntax
    .\tools\build_sets_guarded.ps1 -Edition first-order-syntax -TimeoutMs 60000
    python tools/build_first_order_introduction_epub.py first-order-syntax

Preparation covers all 155 aligned source units and writes the cumulative TeX body plus exact input hashes. The HTML builder produces `reader/first-order-syntax.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, six line-numbered axiomatic derivation tables, thirteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, fifty signed analytic tableaux, and internal source anchors. The guarded TeX build produces `build/gu-first-order-syntax.pdf`. The EPUB builder consumes the accepted HTML reader and produces `releases/OpenLogic-gu-Gujr-IN-First-Order-Syntax.epub`, a deterministic reflowable EPUB 3.3 publication with XHTML, native MathML, Gujarati metadata and fonts, described figures, a 163-link navigation document, landmarks, and an explicit 155/722 partial-edition disclosure.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current build completed all three passes; all three 196-page PDFs are byte-identical at SHA-256 `2482f8fd54483808f6c390e5c24dbb23d81d247b3556152b80c2c5eae22cf7cc`. All 196 final pages were rendered with Poppler and visually inspected.

The EPUB builder also performs a cold replay. The canonical and replay files are byte-identical at 482,891 bytes and SHA-256 `71402df6b14f90d7d79497868f069f2a49ebec04a49152b4dd5ec4c4104045e2`. EPUBCheck 5.3.0 reports zero fatal errors, errors, warnings, or informational messages. Exact structural QA verifies all 8,426 MathML subtrees and TeX annotations, the Gujarati character stream, 623 content IDs, 163 navigation links, 208 proof representations, 13 described SVG figures, 12 tables, 13 footnotes, and all 106 source-correction disclosures. Silent Chromium inspection of byte-identical XHTML checked every new first-order syntax section, navigation, mathematical displays, figures, editorial notes, and end matter; fonts and images loaded, no unhandled mathematical clipping occurred, and the console was clean.

The verified PDF and EPUB are published in the [First-Order Syntax v0.9.0 release](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/first-order-syntax-v0.9.0) and preserved in the existing Zenodo lineage at [DOI 10.5281/zenodo.22728364](https://doi.org/10.5281/zenodo.22728364), with the PDF as the human-readable preview.

To validate an EPUB independently with EPUBCheck 5.3.0 or later:

    java -jar path\to\epubcheck.jar releases\OpenLogic-gu-Gujr-IN-First-Order-Syntax.epub --json build\EPUBCHECK.json

The same guarded TeX script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, `-Edition sequent-calculus`, `-Edition natural-deduction`, `-Edition tableaux`, `-Edition axiomatic-deduction`, `-Edition completeness`, or `-Edition first-order-introduction`. The `first-order-syntax` edition is the current 155-unit target.

Publication requires the completed validation described above and final hash binding in the QA receipts. `provenance/PDF_QA_015.json`, `provenance/EPUB_QA_015.json`, and `provenance/CUMULATIVE_QA_015.json` record those checks. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
