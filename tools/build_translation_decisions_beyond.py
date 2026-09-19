"""Build translation-decision surfaces for the 178-unit beyond checkpoint."""

from pathlib import Path


template = Path(__file__).with_name(
    "build_translation_decisions_first_order_models_theories.py"
)
code = template.read_text(encoding="utf-8")

replacements = (
    ('"first-order-models-theories-body.tex"', '"beyond-body.tex"'),
    ('"gu-first-order-models-theories.pdf"', '"gu-beyond.pdf"'),
    ('"gu-first-order-models-theories.synctex.gz"', '"gu-beyond.synctex.gz"'),
    ('"BUILD_RECEIPT_017.json"', '"BUILD_RECEIPT_018.json"'),
    ("build/first-order-models-theories-body.tex", "build/beyond-body.tex"),
    ("build/gu-first-order-models-theories.pdf", "build/gu-beyond.pdf"),
    (
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-", "OLSEM-", "OLMAT-"',
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-", "OLSEM-", "OLMAT-", "OLBYD-"',
    ),
    (
        "cumulative Gujarati reader through OLP-0173; models and theories after first-order semantics",
        "cumulative Gujarati reader through OLP-0181; logics beyond first order after models and theories",
    ),
    ("current 170/722-unit working edition", "current 178/722-unit working edition"),
    ("current 170/722-unit Gujarati", "current 178/722-unit Gujarati"),
    ("assert len(terms) == 157", "assert len(terms) == 168"),
    ("assert correction_count == 122", "assert correction_count == 128"),
    ('"source_units": 170', '"source_units": 178'),
    (
        "                170\\\\n                if BUILD_RECEIPT_PATH.exists()",
        "                178\\\\n                if BUILD_RECEIPT_PATH.exists()",
    ),
)
for before, after in replacements:
    assert before in code, before
    code = code.replace(before, after)

exec(
    compile(
        code,
        str(template.with_name("build_translation_decisions_beyond_expanded.py")),
        "exec",
    ),
    {"__name__": "__main__", "__file__": str(template)},
)
