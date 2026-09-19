# Cumulative build through first-order models and theories

From the repository root:

    python tools/prepare_first_order_models_theories.py
    python tools/build_functions_html.py first-order-models-theories
    .\tools\build_sets_guarded.ps1 -Edition first-order-models-theories -TimeoutMs 60000
    python tools/build_first_order_introduction_epub.py first-order-models-theories

Preparation covers all 170 aligned source units and writes the cumulative TeX body plus exact input hashes. The HTML builder produces `reader/first-order-models-theories.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, six line-numbered axiomatic derivation tables, thirteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, fifty signed analytic tableaux, and internal source anchors. The guarded TeX build produces `build/gu-first-order-models-theories.pdf`. The EPUB builder consumes the accepted HTML reader and produces `releases/OpenLogic-gu-Gujr-IN-First-Order-Models-Theories.epub`, a deterministic reflowable EPUB 3.3 publication with XHTML, native MathML, Gujarati metadata and fonts, described figures, a 177-link navigation document, landmarks, and an explicit 170/722 partial-edition disclosure.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current build completed all three passes; all three 219-page PDFs are byte-identical at SHA-256 `0e3660cd6a1d01078d0bf127d07ed61cf47835cd008883f1b69b1d90e24ccf81`. All 219 final pages were rendered with Poppler and visually inspected.

The EPUB builder also performs a cold replay. The canonical and replay files are byte-identical at 524,276 bytes and SHA-256 `ab63ff6142fca4329d92d178834417892764c6a16724e0064395309cc98a655b`. EPUBCheck 5.3.0 reports zero fatal errors, errors, warnings, or informational messages. Exact structural QA verifies all 9,653 MathML subtrees and TeX annotations, the Gujarati character stream, 666 content IDs, 177 navigation links, 208 proof representations, 13 described SVG figures, 12 tables, 13 footnotes, all 122 keyed disclosures, and the withdrawal of the historical OLINF-002 false-positive classification. Silent Chromium inspection of byte-identical XHTML checked the new models-and-theories sections, navigation, mathematical displays, figures, editorial notes, and end matter; fonts and images loaded, no unhandled mathematical clipping occurred, raw problem tags did not leak, and the target console was clean.

The reviewed 170-unit artifacts are being prepared for the Models and Theories checkpoint release. The latest public artifact release remains [First-Order Semantics v0.10.0](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/first-order-semantics-v0.10.0), preserved at [DOI 10.5281/zenodo.22849693](https://doi.org/10.5281/zenodo.22849693) in the existing Gujarati OpenLogic Zenodo lineage, with the PDF as the human-readable preview.

To validate an EPUB independently with EPUBCheck 5.3.0 or later:

    java -jar path\to\epubcheck.jar releases\OpenLogic-gu-Gujr-IN-First-Order-Models-Theories.epub --json build\EPUBCHECK.json

The same guarded TeX script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, `-Edition sequent-calculus`, `-Edition natural-deduction`, `-Edition tableaux`, `-Edition axiomatic-deduction`, `-Edition completeness`, `-Edition first-order-introduction`, `-Edition first-order-syntax`, or `-Edition first-order-semantics`. The `first-order-models-theories` edition is the current 170-unit target.

Publication requires the completed validation described above and final hash binding in the QA receipts. `provenance/PDF_QA_017.json`, `provenance/EPUB_QA_017.json`, and `provenance/CUMULATIVE_QA_017.json` record those checks. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
