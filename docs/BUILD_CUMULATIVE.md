# Cumulative build through Beyond First-order Logic

From the repository root:

    python tools/prepare_beyond.py
    python tools/build_functions_html.py beyond
    .\tools\build_sets_guarded.ps1 -Edition beyond -TimeoutMs 60000
    python tools/build_first_order_introduction_epub.py beyond

Preparation covers all 178 aligned source units and writes the cumulative TeX body plus exact input hashes. The HTML builder produces `reader/beyond.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, six line-numbered axiomatic derivation tables, thirteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, fifty signed analytic tableaux, and internal source anchors. The guarded TeX build produces `build/gu-beyond.pdf`. The EPUB builder consumes the accepted HTML reader and produces `releases/OpenLogic-gu-Gujr-IN-Beyond.epub`, a deterministic reflowable EPUB 3.3 publication with XHTML, native MathML, Gujarati metadata and fonts, described figures, a 184-link navigation document, landmarks, and an explicit 178/722 partial-edition disclosure.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current build completed all three passes; all three 231-page PDFs are byte-identical at SHA-256 `3d1bada274079b4c3b573bb431a467cf8ab41b695f0b2cdfe57bf68d0c259ed0`. All 231 final pages were rendered with Poppler and visually inspected.

The EPUB builder also performs a cold replay. The canonical and replay files are byte-identical at 545,538 bytes and SHA-256 `f69b056e0883707286a44772e999e47c51b7488e258ddd3924ec8ecfbfb81d41`. EPUBCheck 5.3.0 reports zero fatal errors, errors, warnings, or informational messages. Exact structural QA verifies all 10,000 MathML subtrees and TeX annotations, the Gujarati character stream, 680 content IDs, 184 navigation links, 208 proof representations, 13 described SVG figures, 12 tables, 13 footnotes, all 128 keyed disclosures, and the withdrawal of the historical OLINF-002 false-positive classification. Silent Chromium inspection of byte-identical XHTML checked the new Beyond First-order Logic sections, navigation, mathematical displays, figures, editorial notes, and end matter; fonts and images loaded, no unhandled mathematical clipping occurred, raw problem tags did not leak, and the target console was clean.

The reviewed 178-unit artifacts are public as [Beyond First-order Logic v0.12.0](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/beyond-v0.12.0), preserved at [DOI 10.5281/zenodo.22851169](https://doi.org/10.5281/zenodo.22851169) in the existing Gujarati OpenLogic Zenodo lineage, with the PDF as the human-readable preview. Anonymous readback verified all eight artifact bytes, the direct full-text TeX, and all 1,285 source-archive inventory entries.

To validate an EPUB independently with EPUBCheck 5.3.0 or later:

    java -jar path\to\epubcheck.jar releases\OpenLogic-gu-Gujr-IN-Beyond.epub --json build\EPUBCHECK.json

The same guarded TeX script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, `-Edition sequent-calculus`, `-Edition natural-deduction`, `-Edition tableaux`, `-Edition axiomatic-deduction`, `-Edition completeness`, `-Edition first-order-introduction`, `-Edition first-order-syntax`, `-Edition first-order-semantics`, or `-Edition first-order-models-theories`. The `beyond` edition is the current 178-unit target.

Publication requires the completed validation described above and final hash binding in the QA receipts. `provenance/PDF_QA_018.json`, `provenance/EPUB_QA_018.json`, and `provenance/CUMULATIVE_QA_018.json` record those checks. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
