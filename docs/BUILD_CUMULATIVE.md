# Cumulative build through Model Theory Basics

From the repository root:

    python tools/prepare_model_theory_basics.py
    python tools/build_functions_html.py model-theory-basics
    .\tools\build_sets_guarded.ps1 -Edition model-theory-basics -TimeoutMs 60000
    python tools/build_first_order_introduction_epub.py model-theory-basics

Preparation covers all 187 aligned source units and writes the cumulative TeX body plus exact input hashes. The HTML builder produces `reader/model-theory-basics.html` with Unicode Gujarati text, native MathML, local fonts, five truth tables, six line-numbered axiomatic derivation tables, thirteen SVG diagrams, recursively rendered LK and natural-deduction rules and proof trees, fifty signed analytic tableaux, and internal source anchors. The guarded TeX build produces `build/gu-model-theory-basics.pdf`. The EPUB builder consumes the accepted HTML reader and produces `releases/OpenLogic-gu-Gujr-IN-Model-Theory-Basics.epub`, a deterministic reflowable EPUB 3.3 publication with XHTML, native MathML, Gujarati metadata and fonts, described figures, a 193-link navigation document, landmarks, and an explicit 187/722 partial-edition disclosure.

The global mutex `Global\InterlanguageTeXSlotV1` is acquired with a bounded wait and remains held across all three owned LuaLaTeX passes and log checks. Failed acquisition starts no TeX process. Installer access and shell escape are disabled. Only the process captured by this script can be terminated after its timeout. The current build completed all three passes; all three 240-page PDFs are byte-identical at SHA-256 `2601984ffd377d3a44c86598485cb6e02e0aac04b7dcd3d328da94c967c6f09a`. All 240 final pages were rendered with Poppler and visually inspected.

The EPUB builder also performs a cold replay. The canonical and replay files are byte-identical at 560,795 bytes and SHA-256 `c76190ae589df8f032a3856c83eff94877cae1eb72e20302a3bac461d469876b`. EPUBCheck 5.3.0 reports zero fatal errors, errors, warnings, or informational messages. Exact structural QA verifies all 10,503 MathML subtrees and TeX annotations, the Gujarati character stream, 721 content IDs, 193 navigation links, 208 proof representations, 13 described SVG figures, 12 tables, 13 footnotes, all 136 keyed disclosures, and the withdrawal of the historical OLINF-002 false-positive classification. Silent Chromium inspection of byte-identical XHTML checked the new Model Theory Basics sections, navigation, mathematical displays, figures, editorial notes, and end matter; fonts and images loaded, no unhandled mathematical clipping occurred, raw problem tags did not leak, and the target console was clean.

The reviewed 187-unit artifacts are public as [Model Theory Basics v0.13.0](https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/releases/tag/model-theory-basics-v0.13.0), preserved at [DOI 10.5281/zenodo.22851934](https://doi.org/10.5281/zenodo.22851934) in the existing Gujarati OpenLogic Zenodo lineage, with the PDF as the human-readable preview. Anonymous readback verified all eight artifact bytes, the direct full-text TeX, and all 1,317 source-archive inventory entries.

To validate an EPUB independently with EPUBCheck 5.3.0 or later:

    java -jar path\to\epubcheck.jar releases\OpenLogic-gu-Gujr-IN-Model-Theory-Basics.epub --json build\EPUBCHECK.json

The same guarded TeX script can reproduce earlier cumulative stages with `-Edition sets`, `-Edition foundations`, `-Edition functions`, `-Edition size`, `-Edition arithmetization`, `-Edition infinite`, `-Edition propositional`, `-Edition proof-systems`, `-Edition sequent-calculus`, `-Edition natural-deduction`, `-Edition tableaux`, `-Edition axiomatic-deduction`, `-Edition completeness`, `-Edition first-order-introduction`, `-Edition first-order-syntax`, `-Edition first-order-semantics`, `-Edition first-order-models-theories`, or `-Edition beyond`. The `model-theory-basics` edition is the current 187-unit target.

Publication requires the completed validation described above and final hash binding in the QA receipts. `provenance/PDF_QA_019.json`, `provenance/EPUB_QA_019.json`, and `provenance/CUMULATIVE_QA_019.json` record those checks. Canon PDFs remain local research evidence and are excluded from distributable artifacts.
