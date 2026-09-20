"""Build translation-decision surfaces for the 187-unit model-theory checkpoint."""

from pathlib import Path


template = Path(__file__).with_name(
    "build_translation_decisions_first_order_models_theories.py"
)
code = template.read_text(encoding="utf-8")

replacements = (
    ('"first-order-models-theories-body.tex"', '"model-theory-basics-body.tex"'),
    ('"gu-first-order-models-theories.pdf"', '"gu-model-theory-basics.pdf"'),
    ('"gu-first-order-models-theories.synctex.gz"', '"gu-model-theory-basics.synctex.gz"'),
    ('"BUILD_RECEIPT_017.json"', '"BUILD_RECEIPT_019.json"'),
    ("build/first-order-models-theories-body.tex", "build/model-theory-basics-body.tex"),
    ("build/gu-first-order-models-theories.pdf", "build/gu-model-theory-basics.pdf"),
    (
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-", "OLSEM-", "OLMAT-"',
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-", "OLSEM-", "OLMAT-", "OLBYD-", "OLMTB-"',
    ),
    (
        "cumulative Gujarati reader through OLP-0173; models and theories after first-order semantics",
        "cumulative Gujarati reader through OLP-0190; model-theory basics after logics beyond first order",
    ),
    ("current 170/722-unit working edition", "current 187/722-unit working edition"),
    ("current 170/722-unit Gujarati", "current 187/722-unit Gujarati"),
    ("assert len(terms) == 157", "assert len(terms) == 179"),
    ("assert correction_count == 122", "assert correction_count == 136"),
    ('"source_units": 170', '"source_units": 187'),
    (
        "                170\\\\n                if BUILD_RECEIPT_PATH.exists()",
        "                187\\\\n                if BUILD_RECEIPT_PATH.exists()",
    ),
)
for before, after in replacements:
    assert before in code, before
    code = code.replace(before, after)

exec(
    compile(
        code,
        str(template.with_name("build_translation_decisions_model_theory_basics_expanded.py")),
        "exec",
    ),
    {"__name__": "__main__", "__file__": str(template)},
)
