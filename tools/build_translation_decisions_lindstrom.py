"""Build translation-decision surfaces for the 204-unit Lindström checkpoint."""

from pathlib import Path


template = Path(__file__).with_name(
    "build_translation_decisions_first_order_introduction.py"
)
code = template.read_text(encoding="utf-8")

replacements = (
    ('"first-order-introduction-body.tex"', '"lindstrom-body.tex"'),
    ('"gu-first-order-introduction.pdf"', '"gu-lindstrom.pdf"'),
    ('"gu-first-order-introduction.synctex.gz"', '"gu-lindstrom.synctex.gz"'),
    ('"BUILD_RECEIPT_014.json"', '"BUILD_RECEIPT_022.json"'),
    ("build/first-order-introduction-body.tex", "build/lindstrom-body.tex"),
    ("build/gu-first-order-introduction.pdf", "build/gu-lindstrom.pdf"),
    (
        '"OLAX-", "OLCO-", "OLFINT-"',
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-", "OLSEM-", "OLMAT-", '
        '"OLBYD-", "OLMTB-", "OLMAR-", "OLINT-", "OLLIN-"',
    ),
    (
        "cumulative Gujarati reader through OLP-0148; first-order introduction after completeness",
        "cumulative Gujarati reader through OLP-0207; Lindstrom after interpolation",
    ),
    ("current 145/722-unit working edition", "current 204/722-unit working edition"),
    ("current 145/722-unit Gujarati", "current 204/722-unit Gujarati"),
    ("assert len(terms) == 140", "assert len(terms) == 198"),
    ("assert len(passages) == 77", "assert len(passages) == 87"),
    ("assert correction_count == 99", "assert correction_count == 175"),
    ('"source_units": 145', '"source_units": 204'),
    (
        "                145\n                if BUILD_RECEIPT_PATH.exists()",
        "                204\n                if BUILD_RECEIPT_PATH.exists()",
    ),
)
for before, after in replacements:
    assert before in code, before
    code = code.replace(before, after)

exec(
    compile(
        code,
        str(template.with_name("build_translation_decisions_lindstrom_expanded.py")),
        "exec",
    ),
    {"__name__": "__main__", "__file__": str(template)},
)
