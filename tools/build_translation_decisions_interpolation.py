"""Build translation-decision surfaces for the 199-unit interpolation checkpoint."""

from pathlib import Path


template = Path(__file__).with_name(
    "build_translation_decisions_first_order_introduction.py"
)
code = template.read_text(encoding="utf-8")

replacements = (
    ('"first-order-introduction-body.tex"', '"interpolation-body.tex"'),
    ('"gu-first-order-introduction.pdf"', '"gu-interpolation.pdf"'),
    ('"gu-first-order-introduction.synctex.gz"', '"gu-interpolation.synctex.gz"'),
    ('"BUILD_RECEIPT_014.json"', '"BUILD_RECEIPT_021.json"'),
    ("build/first-order-introduction-body.tex", "build/interpolation-body.tex"),
    ("build/gu-first-order-introduction.pdf", "build/gu-interpolation.pdf"),
    (
        '"OLAX-", "OLCO-", "OLFINT-"',
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-", "OLSEM-", "OLMAT-", '
        '"OLBYD-", "OLMTB-", "OLMAR-", "OLINT-"',
    ),
    (
        "cumulative Gujarati reader through OLP-0148; first-order introduction after completeness",
        "cumulative Gujarati reader through OLP-0202; interpolation after models of arithmetic",
    ),
    ("current 145/722-unit working edition", "current 199/722-unit working edition"),
    ("current 145/722-unit Gujarati", "current 199/722-unit Gujarati"),
    ("assert len(terms) == 140", "assert len(terms) == 191"),
    ("assert len(passages) == 77", "assert len(passages) == 82"),
    ("assert correction_count == 99", "assert correction_count == 162"),
    ('"source_units": 145', '"source_units": 199'),
    (
        "                145\n                if BUILD_RECEIPT_PATH.exists()",
        "                199\n                if BUILD_RECEIPT_PATH.exists()",
    ),
)
for before, after in replacements:
    assert before in code, before
    code = code.replace(before, after)

exec(
    compile(
        code,
        str(template.with_name("build_translation_decisions_interpolation_expanded.py")),
        "exec",
    ),
    {"__name__": "__main__", "__file__": str(template)},
)
