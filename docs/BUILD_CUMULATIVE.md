# Cumulative build through the first-order introduction

From the repository root:

    python tools/prepare_first_order_introduction.py
    python tools/build_functions_html.py first-order-introduction
    .\tools\build_sets_guarded.ps1 -Edition first-order-introduction -TimeoutMs 60000
    python tools/build_first_order_introduction_epub.py

Preparation covers all 145 aligned source units and writes the cumulative TeX body plus exact input hashes. The HTML builder produces `reader/first-order-introduction.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, six line-numbered axiomatic derivation tables, thirteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, fifty signed analytic tableaux, and internal source anchors. The guarded TeX build produces `build/gu-first-order-introduction.pdf`. The EPUB builder consumes the accepted HTML reader and produces `releases/OpenLogic-gu-Gujr-IN-First-Order-Introduction.epub`, a deterministic reflowable EPUB 3.3 publication with XHTML, native MathML, Gujarati metadata and fonts, described figures, a 154-link navigation document, landmarks, and an explicit 145/722 partial-edition disclosure.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current build completed all three passes; all three 183-page PDFs are byte-identical at SHA-256 `d7ebbe1041f551ef8f7a12aff97fab2729d0f5444e94ca6caac94a5b937f6ae7`. All 183 final pages were rendered with Poppler and visually inspected.

The EPUB builder also performs a cold replay. The canonical and replay files are byte-identical at 461,737 bytes and SHA-256 `a6ffe47ce1c76967bd9920a39b5dc3feb8308d80ede26169c32d79dabfd35e5a`. EPUBCheck 5.3.0 reports zero fatal errors, errors, warnings, or informational messages. Exact structural QA verifies all 7,620 MathML subtrees and TeX annotations, the Gujarati character stream, 583 content IDs, 154 navigation links, 208 proof representations, 13 described SVG figures, 11 tables, 13 footnotes, and all 99 source-correction disclosures. Silent Chromium inspection of byte-identical XHTML checked the new first-order introduction, navigation, mathematical displays, figures, editorial notes, and end matter; fonts and images loaded, no unhandled mathematical clipping occurred, and the console was clean.

The latest publicly verified PDF and EPUB are in the [First-Order Completeness v0.7.0 release](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/completeness-v0.7.0) and the existing Zenodo lineage at [DOI 10.5281/zenodo.22726447](https://doi.org/10.5281/zenodo.22726447). The 145-unit first-order introduction artifacts described above are the current reviewed working checkpoint.

To validate an EPUB independently with EPUBCheck 5.3.0 or later:

    java -jar path\to\epubcheck.jar releases\OpenLogic-gu-Gujr-IN-First-Order-Introduction.epub --json build\EPUBCHECK.json

The same guarded TeX script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, `-Edition sequent-calculus`, `-Edition natural-deduction`, `-Edition tableaux`, `-Edition axiomatic-deduction`, or `-Edition completeness`. The `first-order-introduction` edition is the current 145-unit target.

Publication requires the completed validation described above and final hash binding in the QA receipts. `provenance/PDF_QA_014.json`, `provenance/EPUB_QA_014.json`, and `provenance/CUMULATIVE_QA_014.json` record those checks. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
