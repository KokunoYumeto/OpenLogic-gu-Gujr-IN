"""Build translation-decision surfaces for the 194-unit arithmetic-models checkpoint."""

from pathlib import Path


template = Path(__file__).with_name(
    "build_translation_decisions_first_order_models_theories.py"
)
code = template.read_text(encoding="utf-8")

replacements = (
    ('"first-order-models-theories-body.tex"', '"models-arithmetic-body.tex"'),
    ('"gu-first-order-models-theories.pdf"', '"gu-models-arithmetic.pdf"'),
    ('"gu-first-order-models-theories.synctex.gz"', '"gu-models-arithmetic.synctex.gz"'),
    ('"BUILD_RECEIPT_017.json"', '"BUILD_RECEIPT_020.json"'),
    ("build/first-order-models-theories-body.tex", "build/models-arithmetic-body.tex"),
    ("build/gu-first-order-models-theories.pdf", "build/gu-models-arithmetic.pdf"),
    (
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-", "OLSEM-", "OLMAT-"',
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-", "OLSEM-", "OLMAT-", "OLBYD-", "OLMTB-", "OLMAR-"',
    ),
    (
        "cumulative Gujarati reader through OLP-0173; models and theories after first-order semantics",
        "cumulative Gujarati reader through OLP-0197; models of arithmetic after model-theory basics",
    ),
    ("current 170/722-unit working edition", "current 194/722-unit working edition"),
    ("current 170/722-unit Gujarati", "current 194/722-unit Gujarati"),
    ("assert len(terms) == 157", "assert len(terms) == 187"),
    ("assert correction_count == 122", "assert correction_count == 152"),
    ('"source_units": 170', '"source_units": 194'),
    (
        "                170\\\\n                if BUILD_RECEIPT_PATH.exists()",
        "                194\\\\n                if BUILD_RECEIPT_PATH.exists()",
    ),
)
for before, after in replacements:
    assert before in code, before
    code = code.replace(before, after)

exec(
    compile(
        code,
        str(template.with_name("build_translation_decisions_models_arithmetic_expanded.py")),
        "exec",
    ),
    {"__name__": "__main__", "__file__": str(template)},
)
