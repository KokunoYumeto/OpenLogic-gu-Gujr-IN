"""Build translation-decision surfaces for the 163-unit semantics checkpoint."""

from pathlib import Path


template = Path(__file__).with_name(
    "build_translation_decisions_first_order_introduction.py"
)
code = template.read_text(encoding="utf-8")

replacements = (
    ('"first-order-introduction-body.tex"', '"first-order-semantics-body.tex"'),
    ('"gu-first-order-introduction.pdf"', '"gu-first-order-semantics.pdf"'),
    ('"gu-first-order-introduction.synctex.gz"', '"gu-first-order-semantics.synctex.gz"'),
    ('"BUILD_RECEIPT_014.json"', '"BUILD_RECEIPT_016.json"'),
    ("build/first-order-introduction-body.tex", "build/first-order-semantics-body.tex"),
    ("build/gu-first-order-introduction.pdf", "build/gu-first-order-semantics.pdf"),
    (
        '"OLAX-", "OLCO-", "OLFINT-"',
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-", "OLSEM-"',
    ),
    (
        "cumulative Gujarati reader through OLP-0148; first-order introduction after completeness",
        "cumulative Gujarati reader through OLP-0166; first-order semantics after the syntax chapter",
    ),
    ("current 145/722-unit working edition", "current 163/722-unit working edition"),
    ("current 145/722-unit Gujarati", "current 163/722-unit Gujarati"),
    ("assert len(terms) == 140", "assert len(terms) == 151"),
    ("assert correction_count == 99", "assert correction_count == 117"),
    ('"source_units": 145', '"source_units": 163'),
    (
        "                145\n                if BUILD_RECEIPT_PATH.exists()",
        "                163\n                if BUILD_RECEIPT_PATH.exists()",
    ),
)
for before, after in replacements:
    assert before in code, before
    code = code.replace(before, after)

exec(
    compile(
        code,
        str(template.with_name("build_translation_decisions_first_order_semantics_expanded.py")),
        "exec",
    ),
    {"__name__": "__main__", "__file__": str(template)},
)
