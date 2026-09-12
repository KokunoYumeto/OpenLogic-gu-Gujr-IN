"""Build translation-decision surfaces for the 155-unit syntax checkpoint."""

from pathlib import Path


template = Path(__file__).with_name(
    "build_translation_decisions_first_order_introduction.py"
)
code = template.read_text(encoding="utf-8")

replacements = (
    ('"first-order-introduction-body.tex"', '"first-order-syntax-body.tex"'),
    ('"gu-first-order-introduction.pdf"', '"gu-first-order-syntax.pdf"'),
    ('"gu-first-order-introduction.synctex.gz"', '"gu-first-order-syntax.synctex.gz"'),
    ('"BUILD_RECEIPT_014.json"', '"BUILD_RECEIPT_015.json"'),
    ("build/first-order-introduction-body.tex", "build/first-order-syntax-body.tex"),
    ("build/gu-first-order-introduction.pdf", "build/gu-first-order-syntax.pdf"),
    (
        '"OLAX-", "OLCO-", "OLFINT-"',
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-"',
    ),
    (
        "cumulative Gujarati reader through OLP-0148; first-order introduction after completeness",
        "cumulative Gujarati reader through OLP-0158; first-order syntax after the introduction",
    ),
    ("current 145/722-unit working edition", "current 155/722-unit working edition"),
    ("current 145/722-unit Gujarati", "current 155/722-unit Gujarati"),
    ("assert len(terms) == 140", "assert len(terms) == 145"),
    ("assert correction_count == 99", "assert correction_count == 106"),
    ('"source_units": 145', '"source_units": 155'),
    ("                145\n                if BUILD_RECEIPT_PATH.exists()", "                155\n                if BUILD_RECEIPT_PATH.exists()"),
)
for before, after in replacements:
    assert before in code, before
    code = code.replace(before, after)

exec(
    compile(code, str(template.with_name("build_translation_decisions_first_order_syntax_expanded.py")), "exec"),
    {"__name__": "__main__", "__file__": str(template)},
)
