# Cumulative build through Interpolation

From the repository root:

    python tools/prepare_interpolation.py
    python tools/build_functions_html.py interpolation
    .\tools\build_sets_guarded.ps1 -Edition interpolation -TimeoutMs 60000
    python tools/build_first_order_introduction_epub.py interpolation

Preparation covers all 199 aligned source units and writes the cumulative TeX body plus exact input hashes. The HTML builder produces `reader/interpolation.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, six line-numbered axiomatic derivation tables, fourteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, fifty signed analytic tableaux, and internal source anchors. The guarded TeX build produces `build/gu-interpolation.pdf`. The EPUB builder consumes the accepted HTML reader and produces `releases/OpenLogic-gu-Gujr-IN-Interpolation.epub`, a deterministic reflowable EPUB 3.3 publication with XHTML, native MathML, Gujarati metadata and fonts, described figures, a 205-link navigation document, landmarks, and an explicit 199/722 partial-edition disclosure.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current build completed all three passes; all three 255-page PDFs are byte-identical at SHA-256 `3e42c61a77ce9987e8c04e000fc81f19ea5bf4d8bf5e1fe19e0fba6f3d604729`. All 255 final pages were rendered with Poppler and visually inspected.

The EPUB builder also performs a cold replay. The canonical and replay files are byte-identical at 598,724 bytes and SHA-256 `4d43cbc0402e8b95d80308aae60b5249f6953b672fa831555228c5b7aa3f9370`. EPUBCheck 5.3.0 reports zero fatal errors, errors, warnings, or informational messages. Exact structural QA verifies all 11,786 MathML subtrees and TeX annotations, the Gujarati character stream, 759 content IDs, 205 navigation links, 208 proof representations, 14 described SVG figures, 12 tables, 13 footnotes, all 162 keyed disclosures, and the withdrawal of the historical OLINF-002 false-positive classification. Silent Chromium inspection of byte-identical XHTML checked the new Interpolation sections, navigation, mathematical displays, figures, editorial notes, and end matter; fonts and images loaded, no unhandled mathematical clipping occurred, raw problem tags did not leak, and the target console was clean.

The reviewed 194-unit artifacts are public as [Models of Arithmetic v0.14.0](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/models-arithmetic-v0.14.0), preserved at [DOI 10.5281/zenodo.22859970](https://doi.org/10.5281/zenodo.22859970) in the existing Gujarati OpenLogic Zenodo lineage, with the PDF as the human-readable preview. Anonymous readback verified all eight artifact bytes, the direct full-text TeX, and all 1,351 source-archive inventory entries.

To validate an EPUB independently with EPUBCheck 5.3.0 or later:

    java -jar path\to\epubcheck.jar releases\OpenLogic-gu-Gujr-IN-Interpolation.epub --json build\EPUBCHECK.json

The same guarded TeX script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, `-Edition sequent-calculus`, `-Edition natural-deduction`, `-Edition tableaux`, `-Edition axiomatic-deduction`, `-Edition completeness`, `-Edition first-order-introduction`, `-Edition first-order-syntax`, `-Edition first-order-semantics`, `-Edition first-order-models-theories`, `-Edition beyond`, `-Edition model-theory-basics`, or `-Edition models-arithmetic`. The `interpolation` edition is the current 199-unit target.

Publication requires the completed validation described above and final hash binding in the QA receipts. `provenance/PDF_QA_021.json`, `provenance/EPUB_QA_021.json`, and `provenance/CUMULATIVE_QA_021.json` record those checks. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
