# Cumulative build through first-order semantics

From the repository root:

    python tools/prepare_first_order_semantics.py
    python tools/build_functions_html.py first-order-semantics
    .\tools\build_sets_guarded.ps1 -Edition first-order-semantics -TimeoutMs 60000
    python tools/build_first_order_introduction_epub.py first-order-semantics

Preparation covers all 163 aligned source units and writes the cumulative TeX body plus exact input hashes. The HTML builder produces `reader/first-order-semantics.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, six line-numbered axiomatic derivation tables, thirteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, fifty signed analytic tableaux, and internal source anchors. The guarded TeX build produces `build/gu-first-order-semantics.pdf`. The EPUB builder consumes the accepted HTML reader and produces `releases/OpenLogic-gu-Gujr-IN-First-Order-Semantics.epub`, a deterministic reflowable EPUB 3.3 publication with XHTML, native MathML, Gujarati metadata and fonts, described figures, a 171-link navigation document, landmarks, and an explicit 163/722 partial-edition disclosure.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current build completed all three passes; all three 211-page PDFs are byte-identical at SHA-256 `fc815250799f3849c9d238701366b08535f9a55a74010026a87dcfcd759352ba`. All 211 final pages were rendered with Poppler and visually inspected.

The EPUB builder also performs a cold replay. The canonical and replay files are byte-identical at 507,586 bytes and SHA-256 `03ebbc4299b413685af345840d1002095c599a82cd1713b93135a628407c81e7`. EPUBCheck 5.3.0 reports zero fatal errors, errors, warnings, or informational messages. Exact structural QA verifies all 9,340 MathML subtrees and TeX annotations, the Gujarati character stream, 654 content IDs, 171 navigation links, 208 proof representations, 13 described SVG figures, 12 tables, 13 footnotes, and all 117 source-correction disclosures. Silent Chromium inspection of byte-identical XHTML checked every new first-order semantics section, navigation, mathematical displays, figures, editorial notes, and end matter; fonts and images loaded, no unhandled mathematical clipping occurred, and the target console was clean.

The verified PDF, cumulative TeX source, complete source ZIP, EPUB, HTML reader, checksums, and QA record are published in the [First-Order Semantics v0.10.0 release](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/first-order-semantics-v0.10.0) and preserved at [DOI 10.5281/zenodo.22848970](https://doi.org/10.5281/zenodo.22848970) in the existing Gujarati OpenLogic Zenodo lineage, with the PDF as the human-readable preview.

To validate an EPUB independently with EPUBCheck 5.3.0 or later:

    java -jar path\to\epubcheck.jar releases\OpenLogic-gu-Gujr-IN-First-Order-Semantics.epub --json build\EPUBCHECK.json

The same guarded TeX script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, `-Edition sequent-calculus`, `-Edition natural-deduction`, `-Edition tableaux`, `-Edition axiomatic-deduction`, `-Edition completeness`, `-Edition first-order-introduction`, or `-Edition first-order-syntax`. The `first-order-semantics` edition is the current 163-unit target.

Publication requires the completed validation described above and final hash binding in the QA receipts. `provenance/PDF_QA_015.json`, `provenance/EPUB_QA_015.json`, and `provenance/CUMULATIVE_QA_015.json` record those checks. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
