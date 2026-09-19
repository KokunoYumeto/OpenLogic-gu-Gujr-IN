"""Build translation-decision surfaces for the 170-unit models-and-theories checkpoint."""

from pathlib import Path


template = Path(__file__).with_name(
    "build_translation_decisions_first_order_semantics.py"
)
code = template.read_text(encoding="utf-8")

replacements = (
    ('"first-order-semantics-body.tex"', '"first-order-models-theories-body.tex"'),
    ('"gu-first-order-semantics.pdf"', '"gu-first-order-models-theories.pdf"'),
    ('"gu-first-order-semantics.synctex.gz"', '"gu-first-order-models-theories.synctex.gz"'),
    ('"BUILD_RECEIPT_016.json"', '"BUILD_RECEIPT_017.json"'),
    ("build/first-order-semantics-body.tex", "build/first-order-models-theories-body.tex"),
    ("build/gu-first-order-semantics.pdf", "build/gu-first-order-models-theories.pdf"),
    (
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-", "OLSEM-"',
        '"OLAX-", "OLCO-", "OLFINT-", "OLSYN-", "OLSEM-", "OLMAT-"',
    ),
    (
        "cumulative Gujarati reader through OLP-0166; first-order semantics after the syntax chapter",
        "cumulative Gujarati reader through OLP-0173; models and theories after first-order semantics",
    ),
    ("current 163/722-unit working edition", "current 170/722-unit working edition"),
    ("current 163/722-unit Gujarati", "current 170/722-unit Gujarati"),
    ("assert len(terms) == 151", "assert len(terms) == 157"),
    ("assert correction_count == 117", "assert correction_count == 122"),
    ('"source_units": 163', '"source_units": 170'),
    (
        "                163\\n                if BUILD_RECEIPT_PATH.exists()",
        "                170\\n                if BUILD_RECEIPT_PATH.exists()",
    ),
)
for before, after in replacements:
    assert before in code, before
    code = code.replace(before, after)

exec(
    compile(
        code,
        str(template.with_name("build_translation_decisions_first_order_models_theories_expanded.py")),
        "exec",
    ),
    {"__name__": "__main__", "__file__": str(template)},
)
