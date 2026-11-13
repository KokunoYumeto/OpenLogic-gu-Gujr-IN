"""Prepare a full-corpus HTML/MathML EPUB input from the accepted direct TeX.

This is an incremental converter. Its QA receipt deliberately marks missing
math and figures as publication blockers; it never promotes a Pandoc fallback
to a complete EPUB merely because the source unit identifiers are present.
"""

from __future__ import annotations

from bisect import bisect_right
from collections import Counter
from pathlib import Path
import hashlib
import json
import re
import subprocess
import shutil
import textwrap

from bs4 import BeautifulSoup
from full_epub_source_macros import macros as source_macros
from epub_base_macros import macros as base_macros, PROOF_TEMPLATE
from render_turing_graphs import render_turing_diagram
from build_exact_operator_fonts import GLYPHS, build as build_operator_fonts
from render_relation_graphs import render_relation_graph
from render_native_epub_figures import render_native_figures, PDF_SHA as NATIVE_FIGURE_PDF_SHA
from full_reader_aux import current_aux


ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "reader" / "full-reader.tex"
PREPARED = ROOT / "build" / "full-epub-prepared.tex"
HTML = ROOT / "build" / "full-epub-draft.html"
STDERR = ROOT / "build" / "full-epub-pandoc.stderr.txt"
RECEIPT = ROOT / "build" / "FULL_EPUB_HTML_QA.json"
PANDOC = Path(shutil.which('pandoc') or (Path.home() / "AppData" / "Local" / "Pandoc" / "pandoc.exe"))
MATH_LINKS: dict[str, dict[str, str]] = {}
EQUATION_LABELS: dict[str, str] = {}
EXACT_OPERATOR_MACROS = "\n".join(
    "\\newcommand{\\" + marker.lower() + r"}{\math" + row[5] + r"{\text{OLPGLYPH" + marker + "}}}"
    for marker, row in GLYPHS.items()
)
PORTABLE_SOURCE_MACROS = r"""
\newcommand{\Gn}[1]{{^{\text{OLPGLYPHREFLECTEDHASH}}}{#1}{^{\text{OLPGLYPHHASH}}}}
\newcommand{\oldepsilon}{ϵ}
\newcommand{\textsc}[1]{\text{OLPSMALLCAPSSTART#1OLPSMALLCAPSEND}}
"""
FONT_FAMILIES = {'tx':('GuOLPExactTX','otf'),
                 'stmary':('GuOLPExactStMary','otf'),
                 'text':('GuOLPExactText','ttf')}


def unique_macro_preamble(phases):
    """Pandoc ignores duplicate newcommands; explicitly select final definitions.

    The phase order is the authored priority: legacy converter, extra handlers,
    frozen source definitions, Log wrapper, exact source-font operators.
    Nested macro bodies are read as balanced groups, never split by a regex.
    """
    pieces, latest, histories = [], {}, {}
    for phase, value in phases:
        pos = 0
        while hit := re.search(r"\\(?:newcommand|renewcommand)\*?", value[pos:]):
            start = pos+hit.start(); end = pos+hit.end()
            pieces.append((None,value[pos:start]))
            name, end = balanced(value,end,"{","}")
            assert re.fullmatch(r"\\[A-Za-z]+",name), (phase,name)
            while value[end:end+1].isspace(): end += 1
            for _ in range(2):
                if value[end:end+1] == '[':
                    _,end = balanced(value,end,'[',']')
                    while value[end:end+1].isspace(): end += 1
            _,end = balanced(value,end,'{','}')
            declaration = value[start:end]
            declaration = re.sub(r'^\\renewcommand',r'\\newcommand',declaration)
            latest[name] = len(pieces)
            pieces.append((name,declaration))
            histories.setdefault(name,[]).append({'phase':phase,'declaration_sha256':hashlib.sha256(declaration.encode('utf-8')).hexdigest()})
            pos = end
        pieces.append((None,value[pos:]))
    merged = '\n'.join(value for i,(name,value) in enumerate(pieces)
                       if name is None or latest[name]==i)
    receipt = {'schema':'openlogic-gu-pandoc-macro-priority/1',
               'priority':[phase for phase,_ in phases],
               'method':'One balanced declaration per name; final authored definition retained because Pandoc ignores later duplicate newcommands.',
               'definitions':histories,
               'duplicate_names_resolved':sorted(name for name,rows in histories.items() if len(rows)>1),
               'merged_sha256':hashlib.sha256(merged.encode('utf-8')).hexdigest()}
    (ROOT/'build/FULL_EPUB_MACRO_PRECEDENCE.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return merged


EXTRA_MATH_MACROS = r"""
\newcommand{\Th}[1]{\mathbf{#1}}
\newcommand{\mModel}[1]{\mathfrak{#1}}
\newcommand{\mClass}[1]{\mathcal{#1}}
\newcommand{\Undef}{\mathbb{U}}
\newcommand{\TMblank}{0}
\newcommand{\TMstroke}{1}
\newcommand{\TMendtape}{\triangleright}
\newcommand{\nszero}{\mathbf{z}}
\newcommand{\nssucc}{*}
\newcommand{\nsplus}{\oplus}
\newcommand{\nstimes}{\otimes}
\newcommand{\nsless}{\mathrel{⋖}}
\newcommand{\cardfont}[1]{\mathfrak{#1}}
\newcommand{\card}[1]{\left|#1\right|}
\newcommand{\pheight}[1]{\mathrm{ht}(#1)}
\newcommand{\depth}[1]{\mathrm{dp}(#1)}
\newcommand{\setrank}[1]{\mathrm{rank}(#1)}
\newcommand{\Char}[1]{\chi_{#1}}
\newcommand{\Proj}[2]{P^{#1}_{#2}}
\newcommand{\Ax}[1]{\mathrm{#1}}
\newcommand{\FV}[1]{\mathrm{FV}(#1)}
\newcommand{\ordplus}{+}
\newcommand{\ordsucc}[1]{#1^{+}}
\newcommand{\ordtimes}{\cdot}
\newcommand{\ZF}{\mathbf{ZF}}
\newcommand{\ZFC}{\mathbf{ZFC}}
\newcommand{\ZFminus}{\mathbf{ZF}^{-}}
\newcommand{\rotationsgroup}{R}
\newcommand{\LogCL}{\mathbf{C}}
\newcommand{\LogGod}{\mathbf{G}}
\newcommand{\LogKs}{\mathbf{K}_{s}}
\newcommand{\Gn}[1]{\ulcorner #1\urcorner}
\newcommand{\gn}[1]{\ulcorner #1\urcorner}
\newcommand{\Add}{\mathrm{add}}
\newcommand{\Mult}{\mathrm{mult}}
\newcommand{\Zero}{\mathrm{zero}}
\newcommand{\Succ}{\mathrm{succ}}
\newcommand{\Pred}{\mathrm{pred}}
\newcommand{\Exp}{\mathrm{exp}}
\newcommand{\OProv}{\mathsf{Prov}}
\newcommand{\Prf}[1]{\mathsf{Prf}(#1)}
\newcommand{\Prop}[2]{[\![#2]\!]_{\mathfrak{#1}}}
\newcommand{\pFmla}[3]{#3\,#1\,#2}
\newcommand{\Thms}[1]{\mathrm{Thm}(#1)}
\newcommand{\fn}[1]{\mathrm{#1}}
\newcommand{\nSequent}{\mid}
\newcommand{\Z}{\mathbf{Z}}
\newcommand{\Zminus}{\mathbf{Z}^{-}}
\newcommand{\Zr}{\mathbf{Zr}}
\newcommand{\Knows}{\mathsf{K}}
\newcommand{\EKnows}{\mathsf{E}}
\newcommand{\CKnows}{\mathsf{C}}
\newcommand{\cardexpo}[2]{#1^{#2}}
\newcommand{\cutrank}[1]{\mathrm{cr}(#1)}
\newcommand{\typeof}[2]{#1^{#2}}
\newcommand{\concat}{\frown}
\newcommand{\onesphere}{\mathbf{S}}
\newcommand{\Complement}[1]{\overline{#1}}
\newcommand{\tsub}{\mathbin{\dot{-}}}
\newcommand{\cif}{\mathbin{\Box\!\rightarrow}}
\newcommand{\supstrict}{\supsetneq}
\newcommand{\ordtype}[1]{\mathrm{ot}(#1)}
\newcommand{\pair}[2]{\langle#1,#2\rangle}
\newcommand{\proj}[2]{\pi_{#1}(#2)}
\newcommand{\CutCS}{\mathrm{Cut}_{\mathrm{CS}}}
\newcommand{\LogLuk}{\mathbf{Ł}}
\newcommand{\LogLP}{\mathbf{LP}}
\newcommand{\LogKw}{\mathbf{Kw}}
\newcommand{\disjointsum}{\sqcup}
\newcommand{\unitsquare}{\mathrm{S}}
\newcommand{\unitline}{\mathrm{L}}
\newcommand{\aeq}{\stackrel{\alpha}{=}}
\newcommand{\bcd}[1]{#1^{*\beta}}
\newcommand{\becd}[1]{#1^{*\beta\eta}}
\newcommand{\maeh}[2]{#1\mathrel{;}#2}
\newcommand{\ordeq}[2]{#1\cong #2}
\newcommand{\scode}[1]{\mathrm{c}_{#1}}
\newcommand{\LT}{\mathbf{LT}}
\newcommand{\ordexpo}[2]{#1^{(#2)}}
\newcommand{\defiff}{\Leftrightarrow}
\newcommand{\TMstay}{N}
\newcommand{\TMright}{R}
\newcommand{\TMleft}{L}
\newcommand{\ext}{\mathit{ext}}
\newcommand{\fregeext}[2]{\epsilon #1\,#2}
\newcommand{\Ftemp}{\mathsf{F}}
\newcommand{\Htemp}{\mathsf{H}}
\newcommand{\Gtemp}{\mathsf{G}}
\newcommand{\cardtimes}{\otimes}
\newcommand{\canonord}{\lhd}
\newcommand{\cheight}[1]{\mathrm{ch}(#1)}
\newcommand{\ande}[2]{\mathrm{p}_{#1}(#2)}
\newcommand{\ST}{\mathrm{ST}}
\newcommand{\cardsucc}[1]{#1^{\oplus}}
\newcommand{\trcl}[1]{\mathrm{trcl}(#1)}
\newcommand{\rlexless}{\mathrel{\sphericalangle}}
\newcommand{\andi}[2]{\langle#1,#2\rangle}
\newcommand{\ori}[3]{\mathrm{in}_{#1}^{#2}(#3)}
\newcommand{\ore}[5]{\mathrm{case}(#1,#2.#3,#4.#5)}
\newcommand{\Ptemp}{\mathsf{P}}
\newcommand{\dcase}[5]{\delta\,#1\,#2.#3\,#4.#5}
\newcommand{\abort}[2]{\varepsilon^{#1}(#2)}
\newcommand{\maxrank}[1]{\mathrm{mr}(#1)}
\newcommand{\cardplus}{\oplus}
\newcommand{\Dual}{\mathrm{dual}}
\newcommand{\Since}{\mathsf{S}}
\newcommand{\Until}{\mathsf{U}}
\newcommand{\fregenum}[2]{\# #1\,#2}
\newcommand{\LogHal}{\mathbf{Hal}}
\newcommand{\Interior}[1]{\mathrm{Int}(#1)}
\newcommand{\eqs}{\equiv}
\newcommand{\cutr}[1]{\mathrm{cr}(#1)}
\newcommand{\lnand}{\mathbin{\uparrow}}
\newcommand{\LogRM}{\mathbf{RM}}
\newcommand{\Nec}{\mathrm{nec}}
\newcommand{\isomorphic}{\cong}
\newcommand{\cardnless}[2]{#1\npreceq #2}
\newcommand{\TMtrans}[3]{#1,#2,#3}
\newcommand{\openTuple}{\langle}
\newcommand{\ordneq}[2]{#1\ncong #2}
\newcommand{\RK}{\mathrm{rk}}
\newcommand{\mTrue}[1]{#1}
\newcommand{\lcm}{\operatorname{lcm}}
\newcommand{\boxright}{\mathbin{\Box\!\rightarrow}}
"""


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def balanced(text: str, pos: int, opening: str, closing: str) -> tuple[str, int]:
    while pos < len(text) and text[pos].isspace():
        pos += 1
    if pos >= len(text) or text[pos] != opening:
        raise ValueError(f"Expected {opening!r} at {pos}: {text[pos:pos+60]!r}")
    depth = 1
    cursor = pos + 1
    while depth:
        if cursor >= len(text):
            raise ValueError("Unclosed delimited argument")
        char = text[cursor]
        if char == opening and text[cursor - 1] != "\\":
            depth += 1
        if char == closing and text[cursor - 1] != "\\":
            depth -= 1
        cursor += 1
    return text[pos + 1:cursor - 1], cursor


def replace_command(text: str, name: str, arity: int, render,
                    *, skip_unbraced: bool = False) -> str:
    pattern = re.compile(r"\\" + re.escape(name) + r"(?![A-Za-z])")
    cursor = 0
    while match := pattern.search(text, cursor):
        args = []
        end = match.end()
        if skip_unbraced and (end >= len(text) or text[end:].lstrip()[:1] != "{"):
            cursor = end
            continue
        for _ in range(arity):
            value, end = balanced(text, end, "{", "}")
            args.append(value)
        replacement = render(*args)
        text = text[:match.start()] + replacement + text[end:]
        cursor = match.start() + len(replacement)
    return text


def optional_quantifier(text: str, name: str, sign: str, unique: bool = False,
                        separator: str = r"\,") -> str:
    pattern = re.compile(r"\\" + name + r"(?![A-Za-z])")
    cursor = 0
    while match := pattern.search(text, cursor):
        end = match.end()
        uniqueness = unique and end < len(text) and text[end] == "!"
        if uniqueness:
            end += 1
        args = []
        for _ in range(2):
            while end < len(text) and text[end].isspace():
                end += 1
            if end >= len(text) or text[end] != "[":
                break
            value, end = balanced(text, end, "[", "]")
            args.append(value)
        replacement = sign + (r"\mathexclaim{}" if uniqueness else "")
        if args:
            replacement += " " + args[0]
        if len(args) == 2:
            replacement += separator + args[1]
        text = text[:match.start()] + replacement + text[end:]
        cursor = match.start() + len(replacement)
    return text


def identity(text: str) -> str:
    pattern = re.compile(r"\\eq(?![A-Za-z])")
    cursor = 0
    while match := pattern.search(text, cursor):
        end = match.end()
        negated = end < len(text) and text[end] == "/"
        if negated:
            end += 1
        args = []
        for _ in range(2):
            if end < len(text) and text[end] == "[":
                value, end = balanced(text, end, "[", "]")
                args.append(value)
            else:
                break
        relation = r"\neq" if negated else "="
        replacement = "{}" + args[0] + relation + "{}" + args[1] if len(args) == 2 else relation + "{}"
        text = text[:match.start()] + replacement + text[end:]
        cursor = match.start() + len(replacement)
    return text


def optional_math_macro(text: str, name: str, arity: int, render) -> str:
    pattern = re.compile(r"\\" + re.escape(name) + r"(?![A-Za-z])")
    cursor = 0
    while match := pattern.search(text, cursor):
        end = match.end()
        args = []
        for _ in range(arity):
            while end < len(text) and text[end].isspace():
                end += 1
            if end < len(text) and text[end] == "{":
                value, end = balanced(text, end, "{", "}")
            elif end < len(text) and text[end] == "\\":
                token = re.match(r"\\(?:[A-Za-z]+|.)", text[end:])
                if token is None:
                    raise ValueError(f"Invalid TeX token for {name}")
                value = token[0]
                end += len(value)
            elif end < len(text):
                value = text[end]
                end += 1
            else:
                raise ValueError(f"Missing TeX argument for {name}")
            args.append(value)
        option = None
        lookahead = end
        while lookahead < len(text) and text[lookahead].isspace():
            lookahead += 1
        if lookahead < len(text) and text[lookahead] == "[":
            option, end = balanced(text, lookahead, "[", "]")
        replacement = render(args, option)
        text = text[:match.start()] + replacement + text[end:]
        cursor = match.start() + len(replacement)
    return text


def optional_relation(text: str, name: str, symbol: str) -> str:
    pattern = re.compile(r"\\" + name + r"(?![A-Za-z])")
    cursor = 0
    while match := pattern.search(text, cursor):
        end = match.end()
        negated = end < len(text) and text[end] == "/"
        if negated:
            end += 1
        option = None
        if end < len(text) and text[end] == "[":
            option, end = balanced(text, end, "[", "]")
        replacement = (r"\not" if negated else "") + symbol
        if option is not None:
            replacement += "_{" + option + "}"
        replacement += "{}"
        text = text[:match.start()] + replacement + text[end:]
        cursor = match.start() + len(replacement)
    return text


def latex_labels() -> dict[str, str]:
    aux, _ = current_aux(ROOT)
    labels = {}
    for line in aux.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith(r"\newlabel{"):
            continue
        label, end = balanced(line, len(r"\newlabel"), "{", "}")
        if label.endswith("@cref"):
            continue
        payload, _ = balanced(line, end, "{", "}")
        value = balanced(payload, 0, "{", "}")[0] if payload.startswith("{") else payload
        labels[label] = value
    return labels


def reference_preprocess(text: str, labels: dict[str, str]) -> tuple[str, list[str]]:
    """Expand OLP's relative anchors/references using the accepted PDF aux."""
    pattern = re.compile(r"\\(olpart|olchapter|olfileid|ollabel|olref)(?![A-Za-z])")
    cursor = 0
    prefix = ""
    missing = []
    while match := pattern.search(text, cursor):
        name = match[1]
        end = match.end()
        if text[match.start()-7:match.start()] == r"\string":
            cursor = end
            continue
        if end >= len(text) or text[end:].lstrip()[:1] not in ("{", "["):
            cursor = end
            continue
        if name == "olpart":
            part, end = balanced(text, end, "{", "}")
            _, end = balanced(text, end, "{", "}")
            prefix = part + "::"
            cursor = end
            continue
        if name == "olchapter":
            part, end = balanced(text, end, "{", "}")
            chapter, end = balanced(text, end, "{", "}")
            _, end = balanced(text, end, "{", "}")
            prefix = part + ":" + chapter + ":"
            cursor = end
            continue
        if name == "olfileid":
            values = []
            for _ in range(3):
                value, end = balanced(text, end, "{", "}")
                values.append(value)
            prefix = ":".join(values)
            replacement = r"\label{" + prefix + ":sec}"
        elif name == "ollabel":
            value, end = balanced(text, end, "{", "}")
            replacement = r"\label{" + prefix + ":" + value + "}"
        else:
            options = []
            while end < len(text) and text[end] == "[":
                value, end = balanced(text, end, "[", "]")
                options.append(value)
            key, end = balanced(text, end, "{", "}")
            base = prefix.split(":")
            target = ":".join(base[:3-len(options)] + options + [key])
            value = labels.get(target, "")
            if not value:
                missing.append(target)
                replacement = r"\texttt{" + target + "}"
            else:
                replacement = r"\hyperref[" + target + "]{" + value + "}"
        text = text[:match.start()] + replacement + text[end:]
        cursor = match.start() + len(replacement)
    def direct_cref(keys: str) -> str:
        result = []
        for key in (part.strip() for part in keys.split(",")):
            value = labels.get(key, "")
            if not value:
                missing.append(key)
                result.append(r"\texttt{" + key + "}")
            else:
                result.append(r"\hyperref[" + key + "]{" + value + "}")
        return " અને ".join(result)
    text = replace_command(text, "cref", 1, direct_cref, skip_unbraced=True)
    text = replace_command(text, "Cref", 1, direct_cref, skip_unbraced=True)
    return text, missing


def satisfaction(text: str, name: str, model_command: str, relation: str) -> str:
    pattern = re.compile(r"\\" + name + r"(?![A-Za-z])")
    cursor = 0
    while match := pattern.search(text, cursor):
        end = match.end()
        negated = end < len(text) and text[end] == "/"
        if negated:
            end += 1
        model, end = balanced(text, end, "{", "}")
        formula, end = balanced(text, end, "{", "}")
        lookahead = end
        while lookahead < len(text) and text[lookahead].isspace():
            lookahead += 1
        assignment = None
        if lookahead < len(text) and text[lookahead] == "[":
            assignment, end = balanced(text, lookahead, "[", "]")
        relation_name = "n" + relation if negated else relation
        replacement = model_command + "{" + model + "}"
        if assignment is not None and name != "pSat":
            replacement += ", " + assignment
        replacement += " \\" + relation_name
        if assignment is not None and name == "pSat":
            replacement += "_{" + assignment + "}"
        replacement += "{} " + formula
        text = text[:match.start()] + replacement + text[end:]
        cursor = match.start() + len(replacement)
    return text


def math_preprocess(text: str, labels: dict[str, str]) -> str:
    def induction_cases(source: str) -> str:
        pattern = re.compile(r"\\indcase(?![A-Za-z])")
        pos = 0
        while match := pattern.search(source, pos):
            end = match.end()
            star = end < len(source) and source[end] == "*"
            exercise = end < len(source) and source[end] == "!"
            if star or exercise:
                end += 1
            formula, end = balanced(source, end, "{", "}")
            complex_formula, end = balanced(source, end, "{", "}")
            case_text, end = balanced(source, end, "{", "}")
            for marker, value in (("indfrmp", formula), ("indfrm", formula),
                                  ("indcomplex", complex_formula)):
                case_text = re.sub(r"\\" + marker + r"(?![A-Za-z])",
                                   lambda _hit, replacement=value: replacement, case_text)
            if star:
                replacement = "$" + formula + "$ પરમાણુક છે: "
            else:
                replacement = "$" + formula + r"\ident " + complex_formula + "$: "
            replacement += "સ્વાધ્યાય." if exercise else case_text
            source = source[:match.start()] + replacement + source[end:]
            pos = match.start() + len(replacement)
        return source
    text = induction_cases(text)
    for _ in range(12):
        pending = text.count(r"\lexists") + text.count(r"\lforall") + text.count(r"\lambd")
        text = optional_quantifier(text, "lexists", r"\exists", unique=True)
        text = optional_quantifier(text, "lforall", r"\forall")
        text = optional_quantifier(text, "lambd", r"\lambda", separator=r".\,")
        if not pending:
            break
    text = identity(text)
    text = optional_relation(text, "iso", r"\simeq")
    text = optional_relation(text, "elemequiv", r"\equiv")
    text = optional_relation(text, "Proves", r"\vdash")
    text = optional_relation(text, "Entails", r"\vDash")
    text = optional_math_macro(text, "iR", 2,
                               lambda args, option: args[0]
                               + ("_{" + option + "}" if option is not None else "")
                               + args[1])
    text = optional_math_macro(text, "rep", 1,
                               lambda args, option: r"\underline{" + args[0] + "}"
                               + ("_{" + option + "}" if option is not None else ""))
    text = optional_math_macro(text, "varAssign", 3,
                               lambda args, option:
                               args[0] + r"\sim_{" + args[2] + "}" + args[1]
                               if option is None else args[0] + "=" + args[1]
                               + "[^{" + option + "}/{" + args[2] + "}]")
    for name, base in (("Trm", r"\mathrm{Trm}"),
                       ("Frm", r"\mathrm{Frm}"),
                       ("Sent", r"\mathrm{Sent}"),
                       ("TrmSOL", r"\mathrm{Trm}^{2}"),
                       ("FrmSOL", r"\mathrm{Frm}^{2}")):
        text = optional_math_macro(text, name, 0,
                                   lambda _args, option, title=base: title
                                   + ("(" + r"\Lang{" + option + "})" if option is not None else ""))
    def injection(source: str) -> str:
        pattern = re.compile(r"\\inj(?![A-Za-z])")
        pos = 0
        while match := pattern.search(source, pos):
            end = match.end()
            option = None
            if end < len(source) and source[end] == "[":
                option, end = balanced(source, end, "[", "]")
            index, end = balanced(source, end, "{", "}")
            argument, end = balanced(source, end, "{", "}")
            replacement = r"\iota_{" + index + "}"
            if option is not None:
                replacement += "^{" + option + "}"
            replacement += "(" + argument + ")"
            source = source[:match.start()] + replacement + source[end:]
            pos = match.start() + len(replacement)
        return source
    text = injection(text)
    def model_class(source: str) -> str:
        pattern = re.compile(r"\\Mod(?![A-Za-z])")
        pos = 0
        while match := pattern.search(source, pos):
            end = match.end()
            language = logic = None
            if end < len(source) and source[end] == "[":
                language, end = balanced(source, end, "[", "]")
            if end < len(source) and source[end] == "(":
                logic, end = balanced(source, end, "(", ")")
            theory, end = balanced(source, end, "{", "}")
            replacement = r"\mathrm{Mod}"
            if language is not None:
                replacement += "^{" + r"\mathcal{" + language + "}}"
            if logic is not None:
                replacement += "_{" + logic + "}"
            replacement += "(" + theory + ")"
            source = source[:match.start()] + replacement + source[end:]
            pos = match.start() + len(replacement)
        return source
    text = model_class(text)
    text = optional_math_macro(text, "tf", 1,
                               lambda args, option: r"\widetilde{" + args[0] + "}"
                               + ("_{" + option + "}" if option is not None else ""))
    for name, printed in (("OCon", "Con"), ("OPrf", "Prf"),
                          ("OProv", "Prov"), ("ORefut", "Ref"),
                          ("ORProv", "RProv"), ("Prov", "Prov"),
                          ("Prf", "Prf"), ("RProv", "RProv"),
                          ("Refut", "Ref")):
        text = optional_math_macro(text, name, 0,
                                   lambda _args, option, label=printed, style=(r"\mathsf" if name.startswith("O") else r"\mathrm"):
                                   style + "{" + label + "}"
                                   + ("_{" + option + "}" if option is not None else ""))
    for name, label, long in (("redone", "", False),
                              ("bredone", r"\beta", False),
                              ("aconvone", r"\alpha", False),
                              ("beredone", r"\beta\eta", False),
                              ("eredone", r"\eta", False),
                              ("xredone", "X", False),
                              ("red", "", True)):
        text = optional_math_macro(text, name, 0,
                                   lambda _args, option, name_label=label, is_long=long:
                                   (r"\overset{" + (option or name_label) + r"}{\twoheadrightarrow}"
                                    if is_long else r"\xrightarrow{" + (option or name_label) + "}"))
    for _ in range(8):
        previous = text.count(r"\bexists") + text.count(r"\bforall")
        for name, quantifier in (("bexists", "exists"), ("bforall", "forall")):
            text = replace_command(text, name, 2,
                                   lambda variable, predicate, q=quantifier:
                                   "(" + chr(92) + q + " " + variable + r")\;" + predicate,
                                   skip_unbraced=True)
        if text.count(r"\bexists") + text.count(r"\bforall") == previous:
            break
    text = replace_command(text, "umin", 2,
                           lambda variable, predicate: r"\mu " + variable + r"\;" + predicate,
                           skip_unbraced=True)
    text = replace_command(text, "bmin", 2,
                           lambda variable, predicate: r"(\mathrm{min}\;" + variable
                           + r")\," + predicate, skip_unbraced=True)
    text = replace_command(text, "fact", 1,
                           lambda value: value + r"\,!", skip_unbraced=True)
    for command_name in ("smash", "shoveright", "shoveleft"):
        text = replace_command(text, command_name, 1, lambda value: value,
                               skip_unbraced=True)
    text = re.sub(r"\\bottomAlignProof(?![A-Za-z])", "", text)
    text = re.sub(r"\\def\\arraystretch\{[^}]+\}", "", text)
    text = re.sub(r"\\small(?=\s*\\begin\{array\})", "", text)
    text = re.sub(r"\\joinrel(?![A-Za-z])", "", text)
    text = re.sub(r"\\(?:xred|bered|aconv|ered)(?![A-Za-z])",
                  lambda match: r"\overset{" + {
                      "xred": "X", "bered": r"\beta\eta",
                      "aconv": r"\alpha", "ered": r"\eta",
                  }[match[0][1:]] + r"}{\twoheadrightarrow}", text)
    text = satisfaction(text, "Sat", r"\Struct", "vDash")
    text = satisfaction(text, "mSat", r"\mModel", "Vdash")
    text = satisfaction(text, "pSat", r"\pAssign", "vDash")
    def truth_value(source):
        pattern = re.compile(r"\\pValue(?![A-Za-z])")
        pos = 0
        while hit := pattern.search(source, pos):
            end = hit.end()
            while end < len(source) and source[end].isspace():
                end += 1
            if source[end:end+1] == "{":
                assignment, end = balanced(source, end, "{", "}")
            elif source[end:end+1] == chr(92):
                assignment = re.match(r"\\(?:[A-Za-z]+|.)", source[end:])[0]
                end += len(assignment)
            else:
                assignment = source[end]
                end += 1
            matrix = logic = None
            lookahead = end
            while lookahead < len(source) and source[lookahead].isspace():
                lookahead += 1
            if source[lookahead:lookahead+1] == "(":
                matrix, end = balanced(source, lookahead, "(", ")")
            lookahead = end
            while lookahead < len(source) and source[lookahead].isspace():
                lookahead += 1
            if source[lookahead:lookahead+1] == "[":
                logic, end = balanced(source, lookahead, "[", "]")
            # Source also uses pValue v[L](A), in which (A) is outside
            # the macro but remains the same visible function application.
            lookahead = end
            while lookahead < len(source) and source[lookahead].isspace():
                lookahead += 1
            if matrix is None and source[lookahead:lookahead+1] == "(":
                matrix, end = balanced(source, lookahead, "(", ")")
            replacement = r"\overline{\pAssign{" + assignment + "}}"
            if logic is not None:
                replacement += "_{" + logic + "}"
            if matrix is not None:
                replacement += "(" + matrix + ")"
            source = source[:hit.start()] + replacement + source[end:]
            pos = hit.start() + len(replacement)
        return source
    text = truth_value(text)
    for name in ("Intro", "Elim"):
        text = optional_math_macro(text, name, 1,
                                   lambda args, option, printed=name:
                                   "{" + args[0] + "}" + r"\mathrm{" + printed + "}"
                                   + ("_{" + option + "}" if option is not None else ""))
    text = optional_math_macro(text, "Log", 1,
                               lambda args, option: r"\ensuremath{\mathbf{" + args[0] + "}"
                               + ("_{" + option + "}" if option is not None else "") + "}")
    for _ in range(12):
        pending = text.count(r"\Value")
        text = optional_math_macro(text, "Value", 2, lambda args, option:
                                   r"\mathrm{Val}^{\Struct{" + args[1] + "}}"
                                   + ("_{" + option + "}" if option is not None else "")
                                   + "(" + args[0] + ")")
        if not text.count(r"\Value") or text.count(r"\Value") == pending:
            break
    text = optional_math_macro(text, "cfind", 1, lambda args, option:
                               r"\varphi_{" + args[0] + "}"
                               + ("^{" + option + "}" if option is not None else ""))
    for original, replacement in {
        "\\bred": r"\overset{\beta}{\twoheadrightarrow}",
        "\\bredpar": r"\overset{\beta}{\Longrightarrow}",
        "\\beredpar": r"\overset{\beta\eta}{\Longrightarrow}",
    }.items():
        text = re.sub(re.escape(original) + r"(?![A-Za-z])", lambda _: replacement, text)
    def align_intertext(match: re.Match[str]) -> str:
        source = re.sub(r"\\emph\{([^{}]*)\}",
                        lambda item: r"\text{" + item[1] + "}", match[0])
        name = match[1]
        if r"\intertext" not in source:
            return source
        content = source[len(r"\begin{" + name + "}"):-len(r"\end{" + name + "}")]
        chunks = []
        pos = 0
        pattern = re.compile(r"\\intertext(?![A-Za-z])")
        while hit := pattern.search(content, pos):
            prose, end = balanced(content, hit.end(), "{", "}")
            before = content[pos:hit.start()].strip()
            if before:
                chunks.append(r"\begin{" + name + "}" + before + r"\end{" + name + "}")
            chunks.append("\n\n" + prose + "\n\n")
            pos = end
        after = content[pos:].strip()
        if after:
            chunks.append(r"\begin{" + name + "}" + after + r"\end{" + name + "}")
        return "\n".join(chunks)
    text = re.sub(r"\\begin\{(align\*?)\}[\s\S]*?\\end\{\1\}",
                  align_intertext, text)
    text = re.sub(r"\\begin\{array\}\{@\{\}([^}]*)@\{\}\}",
                  lambda match: r"\begin{array}{" + match[1] + "}", text)
    # TeX permits prose, links, and even locally delimited formulae inside an
    # alignment. Texmath does not; preserve the visible formula and keep the
    # equation anchors for the later DOM binding pass.
    def math_links(source: str) -> str:
        def marker(target: str, shown: str, original: str) -> str:
            key = "OLPMATHLINK" + str(len(MATH_LINKS)).zfill(6)
            MATH_LINKS[key] = {"target": target, "shown": shown, "original": original}
            return r"\text{" + key + "}"
        pattern = re.compile(r"\\hyperref\[([^]]+)\]")
        pos = 0
        while hit := pattern.search(source, pos):
            shown, end = balanced(source, hit.end(), "{", "}")
            replacement = marker(hit[1], shown, source[hit.start():end])
            source = source[:hit.start()] + replacement + source[end:]
            pos = hit.start() + len(replacement)
        pattern = re.compile(r"\\eqref\{([^}]+)\}")
        source = pattern.sub(lambda hit: marker(hit[1], "(" + labels.get(hit[1], hit[1]) + ")", hit[0]), source)
        return source
    def split_text_math(source: str) -> str:
        pattern = re.compile(r"\\(?:text|mbox|textrm)\s*\{")
        pos = 0
        while hit := pattern.search(source, pos):
            content, end = balanced(source, hit.end()-1, "{", "}")
            # TeX text may contain a nested link marker or locally delimited
            # mathematics. Texmath requires separate sibling math/text nodes.
            content = content.replace(r"\/", "")
            embedded = re.compile(r"\$[^$]*\$|\\text\{OLPMATHLINK\d+\}|\\(?:qquad|quad)(?![A-Za-z])|\\(?:Taut|PL)(?![A-Za-z])|\\textsc\{[^{}]*\}")
            pieces = []
            previous = 0
            for nested in embedded.finditer(content):
                if nested.start() > previous:
                    pieces.append(r"\text{"+content[previous:nested.start()]+"}")
                value = nested[0]
                if value.startswith("$"):
                    value = value[1:-1]
                elif value == r"\Taut":
                    value = r"\mathrm{TAUT}"
                elif value == r"\PL":
                    value = r"\mathrm{PL}"
                elif value.startswith(r"\textsc{"):
                    value = r"\mathrm{"+value[len(r"\textsc{"):-1].upper()+"}"
                pieces.append(value)
                previous = nested.end()
            if previous == 0:
                replacement = r"\text{"+content+"}"
            else:
                if previous < len(content):
                    pieces.append(r"\text{"+content[previous:]+"}")
                replacement = "".join(pieces)
            source = source[:hit.start()] + replacement + source[end:]
            pos = hit.start() + len(replacement)
        return source
    def tagged_math(source: str) -> str:
        pattern = re.compile(r"\\tag\{")
        pos = 0
        while hit := pattern.search(source, pos):
            label, end = balanced(source, hit.end()-1, "{", "}")
            label = label.replace("$", "")
            replacement = r"\quad\text{(}" + label + r"\text{)}"
            source = source[:hit.start()] + replacement + source[end:]
            pos = hit.start() + len(replacement)
        return source
    def clean_display_body(source: str) -> str:
        source = split_text_math(source)
        source = math_links(source)
        source = split_text_math(source)
        source = tagged_math(source)
        source = source.replace(r"\notag", "").replace(r"\nonumber", "")
        source = source.replace(r"\emph", r"\text")
        source = re.sub(r"(?<!\\)\$", "", source)
        # In standalone rule fractions the source table's leading alignment
        # tab has no second column. Real arrays/alignments start with an
        # environment command and retain every alignment tab.
        source = re.sub(r"^(\\\[\s*)?\s*&\s*", lambda m: m[1] or "", source)
        return source
    def clean_display(hit: re.Match[str]) -> str:
        return clean_display_body(hit[0])
    text = re.sub(
        r"\\begin\{(align\*?|gather\*?|multline\*?|equation\*?|cases|array)\}"
        r"[\s\S]*?\\end\{\1\}", clean_display, text)
    text = re.sub(
        r"\\\[\s*\\centering\s*(\\begin\{tabular\}[\s\S]*?\\end\{tabular\})\s*\\\]",
        lambda hit: "\n\n" + hit[1] + "\n\n", text)
    text = re.sub(r"(?<!\$)\$(?!\$)(?:\\.|[^$])*\$(?!\$)",
                  lambda hit: hit[0].replace(r"\emph", r"\text"), text)
    # Source-font operators are resolved by exact glyph placeholders only
    # after Pandoc; their original TeX remains in semantic annotations.
    text = text.replace(r"$\bexists$", r"\texttt{\textbackslash{}bexists}")
    text = text.replace(r"\Cuti,j", r"\mathrm{Cut}_{i,j}")
    for command, label in (("Weakening", "W"), ("Contraction", "C"), ("Exchange", "X"), ("Cut", "Cut")):
        text = text.replace("\\" + command + "i", r"\mathrm{" + label + "}_i")
    text = text.replace(
        r"2^{(2^{\iddots^{2^{x}}})}\raisebox{1ex}{\bigg\rbrace}"
        "\n" r"\raisebox{1ex}{\text {$y$ વખત $2$}}",
        r"\underbrace{2^{(2^{\ddots^{2^{x}}})}}_{\text{$y$ વખત $2$}}",
    )
    # The accepted reader uses open-logic-config.sty's default Greek formula
    # metavariables. A bare exclamation mark in Pandoc is not that shorthand.
    greek = dict(zip("ABCDEFGHKLORST", (r"\varphi", r"\psi", r"\chi", r"\theta", r"\alpha",
                                       r"\beta", r"\gamma", r"\delta", r"\xi", r"\zeta",
                                       r"\omega", r"\rho", r"\sigma", r"\tau")))
    text = re.sub(r"(?<!\\)!([A-Z])", lambda hit: greek.get(hit[1], hit[1]) + "{}", text)
    text = text.replace(r"\small", "")
    text = replace_command(text, "equivclass", 2,
                           lambda obj, relation: obj + r"/_{\!{" + relation + "}}")
    text = re.sub(r"(?<!\\)\\\[[\s\S]*?(?<!\\)\\\]",
                  clean_display, text)
    text = re.sub(r"(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$",
                  lambda hit: "$$"+clean_display_body(hit[0][2:-2])+"$$", text)
    for name, printed in (("Struct", r"\mathfrak"), ("mModel", r"\mathfrak"),
                           ("pAssign", r"\mathfrak"), ("Lang", r"\mathcal")):
        def first_token(args, _option, style=printed):
            value = args[0]
            if value.startswith("{"):
                first, end = balanced(value, 0, "{", "}")
            elif value.startswith(chr(92)):
                first = re.match(r"\\(?:[A-Za-z]+|.)", value)[0]
                end = len(first)
            else:
                first, end = value[:1], 1
            return "{" + style + "{" + first + "}" + value[end:] + "}"
        text = optional_math_macro(text, name, 1, first_token)
    def equation_labels(match: re.Match[str]) -> str:
        def replace_label(label: re.Match[str]) -> str:
            key = f"OLPEQLABEL{len(EQUATION_LABELS)+1:06d}"
            EQUATION_LABELS[key] = label[1]
            return r"\text{"+key+"}"
        return re.sub(r"\\label\{([^{}]+)\}", replace_label, match[0])
    text = re.sub(r"\\begin\{equation\*?\}[\s\S]*?\\end\{equation\*?\}", equation_labels, text)
    return text


def structural_preprocess(text: str) -> str:
    text = text.replace(
        r"\DeclareRobustCommand{\VDash}{\mathrel{||}\joinrel\Relbar}", ""
    ).replace(r"\VDash", r"\Vdash")
    # Pandoc otherwise executes these literal correction-note examples as
    # commands (notably a bare \item) and aborts mid-book.
    for literal in ("sFmla", "item", "iftag", "top", "lexists", "Atom", "dots", "newcommand"):
        text = text.replace(chr(92) + "string" + chr(92) + literal,
                            chr(92) + "textbackslash{}" + literal)
    text = text.replace(r"\string!", "!")
    text = replace_command(text, "olpart", 2, lambda ident, title:
                           r"\part{" + title + r"}\label{" + ident + ":::part}")
    text = replace_command(text, "olchapter", 3,
                           lambda _part, _chapter, title: r"\chapter{" + title + "}")
    for name, target in (("olsection", "section"), ("olsubsection", "subsection"),
                         ("olsubsubsection", "subsubsection")):
        text = re.sub(r"\\" + name + r"\[[^]]*\](?=\s*\{)",
                      lambda _match, command=name: "\\" + command, text)
        text = replace_command(text, name, 1,
                               lambda title, heading=target: "\\" + heading + "{" + title + "}")
    text = replace_command(text, "olchapterid", 2, lambda part, chapter:
                           r"\label{" + part + ":" + chapter + "::chap}")
    text = replace_command(text, "sourcecorrection", 2,
                           lambda ident, note: "\n\n" + r"\begin{quote}\textbf{સ્રોત-સુધારો "
                           + ident + ".} " + note + r"\end{quote}" + "\n\n")
    for name, kind in (("editorial", "સંપાદકીય નોંધ"),
                       ("history", "ઇતિહાસ")):
        text = text.replace(r"\begin{" + name + "}",
                            r"\begin{quote}\textbf{" + kind + ".} ")
        text = text.replace(r"\end{" + name + "}", r"\end{quote}")
    for path in sorted(set(re.findall(r"\\olasset(?:\[[^]]*\])?\{([^}]+)\}", text))):
        name = Path(path).stem
        if name == "turing-machine":
            name = "turing-machine"
        svg = ROOT / "reader" / "assets" / (name + ".svg")
        if not svg.is_file():
            raise FileNotFoundError(f"Missing asset for {path}: {svg}")
        text = re.sub(r"\\olasset(?:\[[^]]*\])?\{" + re.escape(path) + r"\}",
                      lambda _: "\n\n" + r"\includegraphics{assets/" + name + ".svg}\n\n",
                      text)
    text = replace_command(text, "olphoto", 2,
                           lambda name, caption: ("\n\n" + r"\begin{figure}"
                                                  + r"\includegraphics{upstream/assets/photos/"
                                                  + name + "/" + name + "-small.png}"
                                                  + r"\caption{" + caption + "}"
                                                  + r"\label{photo-" + name + "}"
                                                  + r"\end{figure}" + "\n\n"),
                           skip_unbraced=True)
    return text


def source_table_groups(text: str) -> tuple[str, list[dict[str, object]]]:
    """Retain all table content under one source caption and canonical anchor.

    Pandoc splits some tabular floats and discards caption anchors on others
    containing only display math. Explicit group boundaries avoid both defects.
    """
    groups = []
    def table(match):
        body = match[1]
        captions = list(re.finditer(r"\\caption(?:\[[^]]*\])?\s*\{", body))
        assert len(captions) == 1, "Source table must have one explicit caption"
        start = captions[0].start()
        caption, end = balanced(body, captions[0].end()-1, "{", "}")
        suffix = body[end:]
        labels = re.findall(r"\\label\{([^{}]+)\}", suffix)
        assert len(labels) == 1, "Do not infer source table identity"
        suffix = re.sub(r"\\label\{([^{}]+)\}", "", suffix)
        content = body[:start]+suffix
        marker = f"OLPTABLECAP{len(groups)+1:03}"
        groups.append({"marker": marker, "label": labels[0],
                       "source_float_sha256": hashlib.sha256(match[0].encode()).hexdigest(),
                       "content_sha256": hashlib.sha256(content.encode()).hexdigest(),
                       "caption_tex": caption})
        return ("\n\n"+r"\begin{quote}\hypertarget{"+labels[0]+"}{}"
                +r"\hypertarget{"+marker+"}{"+caption+r"}\par"+"\n"+content
                +r"\end{quote}"+"\n\n")
    return re.sub(r"\\begin\{table\}(?:\[[^]]*\])?([\s\S]*?)\\end\{table\}", table, text), groups


def render_proof_structures(text: str) -> tuple[str, list[dict[str, object]]]:
    """Reuse the audited tableau/inference renderer from the 270-unit EPUB.

    Its executable slice starts at the standalone TableauNode declaration and
    ends before citation processing. This interim coupling is recorded in the
    reproducibility source; extraction fails if either boundary changes.
    """
    # The two node names are only TikZ placement handles; the recursive
    # MathML tableau renders the same signed formulas and branch structure.
    text = re.sub(r",\s*name=(?:one|two)(?=\s|\])", "", text)
    text = re.sub(
        r"\\begin\{defish\}[\s\S]*?\\end\{defish\}",
        lambda match: match[0] if re.search(r"\\(?:AxiomC|Axiom)(?![A-Za-z])", match[0])
        else match[0].replace(r"\begin{defish}", r"\begin{quote}")
        .replace(r"\end{defish}", r"\end{quote}"),
        text,
    )
    fragment = PROOF_TEMPLATE.replace("r'\\qquad'.join", "r'\\qquad{}'.join")
    scope = {
        "edition": "undecidability",
        "body": text,
        "proof_render_receipts": [],
        "re": re,
        "hashlib": hashlib,
        "arg": lambda value, pos: balanced(value, pos, "{", "}"),
    }
    exec(textwrap.dedent(fragment), scope)
    standalone = re.compile(
        r"\\(?:AxiomC|Axiom)(?![A-Za-z])[\s\S]*?\\DisplayProof(?![A-Za-z])"
    )
    openings = [match.start() for match in re.finditer(r"(?<!\\)\\\[", scope["body"])]
    closings = [match.start() for match in re.finditer(r"(?<!\\)\\\]", scope["body"])]
    def render_standalone(match: re.Match[str]) -> str:
        rendered = scope["proof_region"](match[0], "standalone_inference").strip()
        if not (rendered.startswith(r"\[") and rendered.endswith(r"\]")):
            raise RuntimeError("Unexpected standalone inference rendering")
        start = match.start()
        oi = bisect_right(openings, start) - 1
        ci = bisect_right(closings, start) - 1
        inside_display = oi >= 0 and (ci < 0 or openings[oi] > closings[ci])
        return rendered[2:-2] if inside_display else "$" + rendered[2:-2] + "$"
    body = standalone.sub(render_standalone, scope["body"])
    return body, scope["proof_render_receipts"]


def main() -> None:
    MATH_LINKS.clear()
    EQUATION_LABELS.clear()
    source = MASTER.read_text(encoding="utf-8")
    macros = base_macros
    text = source.split(r"\begin{document}", 1)[1].rsplit(r"\end{document}", 1)[0]
    labels = latex_labels()
    text, unresolved_refs = reference_preprocess(text, labels)
    # Match exact diagram bytes before any macro/heading normalization.
    text, native_receipts, native_descriptions = render_native_figures(text)
    (ROOT/'build/FULL_EPUB_NATIVE_FIGURES.json').write_text(
        json.dumps({'schema':'openlogic-gu-full-epub-native-pdf-figures/1',
                    'input_sha256':sha(MASTER), 'pdf_sha256':NATIVE_FIGURE_PDF_SHA,
                    'figures':native_receipts},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # maxwidth changes print geometry only. Keep the same proof/tableau
    # content and present it in the converter's existing display environments.
    text = re.sub(
        r"\\begin\{maxwidth\}\s*\\begin\{tableau\}\{\}([\s\S]*?)"
        r"\\end\{tableau\}\s*\\end\{maxwidth\}",
        lambda match: r"\begin{oltableau}" + match[1] + r"\end{oltableau}", text,
    )
    text = re.sub(
        r"\\begin\{maxwidth\}\s*\$\s*([\s\S]*?\\DisplayProof)\$\s*\\end\{maxwidth\}",
        lambda match: r"\[" + "\n" + match[1] + "\n" + r"\]", text,
    )
    text = structural_preprocess(text)
    text, proof_receipts = render_proof_structures(text)
    text, table_groups = source_table_groups(text)
    graph_receipts, graph_descriptions = [], {}
    relation_receipts, relation_descriptions = [], {}
    def turing_graph(match: re.Match[str]) -> str:
        diagram = match[1]
        if r"\tikzstyle{every state}" not in diagram:
            output = render_relation_graph(diagram, ROOT/"build/full-epub-media", ROOT,
                                           relation_receipts, relation_descriptions)
            return output if output else match[0]
        output = render_turing_diagram(diagram, ROOT / "build/full-epub-media", ROOT,
                                      graph_receipts, graph_descriptions)
        return output.replace("{assets/", "{build/full-epub-media/assets/")
    text = re.sub(r"(?:\\\[\s*)?(\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\})(?:\s*\\\])?", turing_graph, text)
    assert len(relation_receipts) == 2, "Both source-verified numeric relation graphs must be converted"
    (ROOT/"build/FULL_EPUB_RELATION_FIGURES.json").write_text(
        json.dumps({'schema':'openlogic-gu-source-relation-graphs/1','input_sha256':sha(MASTER),
                    'figures':relation_receipts},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    graph_descriptions.update(relation_descriptions)
    graph_descriptions.update(native_descriptions)
    (ROOT / "build/FULL_EPUB_TURING_FIGURES.json").write_text(
        json.dumps({"schema": "openlogic-gu-full-epub-turing-figures/1", "input_sha256": sha(MASTER),
                    "figures": graph_receipts, "alt_text_gu": graph_descriptions}, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    text = math_preprocess(text, labels)
    # math_preprocess normalizes the original aligned displays to align*.
    # Each of these two displays contains only its graph, so keep the image
    # in flow content instead of sending it to the formula parser.
    text, relation_displays = re.subn(
        r"\\begin\{align\*\}\s*&\s*(\\includegraphics\{build/full-epub-media/assets/relation-graph-\d+\.svg\})\s*\\end\{align\*\}",
        lambda m: "\n\n"+m[1]+"\n\n", text)
    assert relation_displays == 2, "Both relation-only displays must become flow images"
    exact_macros, macro_mapping = source_macros(ROOT / "upstream/open-logic-config.sty")
    operator_fonts = build_operator_fonts()
    PREPARED.parent.mkdir(parents=True, exist_ok=True)
    preamble = unique_macro_preamble([
        ('legacy_converter',macros),('explicit_handlers',EXTRA_MATH_MACROS),
        ('frozen_source_definitions',exact_macros),
        ('Log_wrapper',r"\newcommand{\Log}[1]{\ensuremath{\mathbf{#1}}}"),
        ('exact_source_font_operators',EXACT_OPERATOR_MACROS),
        ('portable_active_source_definitions',PORTABLE_SOURCE_MACROS)])
    PREPARED.write_text(preamble + "\n" + text,
                        encoding="utf-8", newline="\n")
    command = [str(PANDOC), str(PREPARED), "-f", "latex", "-t", "html5",
               "--mathml", "--standalone", "--toc", "--toc-depth=4",
               "--metadata", "lang=gu-IN", "--metadata",
               "title=ઓપન લોજિક ગુજરાતી — સંપૂર્ણ ૭૨૨-એકમ આવૃત્તિ",
               "-o", str(HTML)]
    result = subprocess.run(command, capture_output=True, text=True,
                            encoding="utf-8", errors="replace", check=False)
    STDERR.write_text(result.stderr, encoding="utf-8", newline="\n")
    if result.returncode:
        raise RuntimeError(f"Pandoc failed ({result.returncode}); see {STDERR}")
    soup = BeautifulSoup(HTML.read_text(encoding="utf-8"), "html.parser")
    for group in table_groups:
        captions = soup.find_all(id=group["marker"])
        assert len(captions) == 1, group
        caption = captions[0]
        container = caption.find_parent("blockquote")
        assert container is not None and caption.parent is container, group
        anchors = container.find_all(id=group["label"])
        assert len(anchors) == 1 and not anchors[0].get_text(strip=True), group
        anchors[0].decompose()
        container.name = "figure"
        container["id"] = group["label"]
        container["class"] = "olp-source-table"
        container["aria-labelledby"] = group["label"]+"-caption"
        caption.name = "figcaption"
        caption["id"] = group["label"]+"-caption"
        group["rendered_native_tables"] = len(container.find_all("table"))
        group["rendered_mathml_formulas"] = len(container.find_all("math"))
    style = soup.new_tag("style")
    style.string = "\n".join(
        '@font-face{font-family:'+name+';src:url("../reader/fonts/exact-operators/'+name+'.'+ext+'") format("'+('opentype' if ext=='otf' else 'truetype')+'");}'
        for name,ext in FONT_FAMILIES.values()
    )
    soup.head.append(style)
    rendered_operators = Counter()
    for element in soup.find_all(["mtext", "mo", "mi"]):
        marker = element.get_text(strip=True).removeprefix("OLPGLYPH")
        if element.get_text(strip=True) != "OLPGLYPH"+marker or marker not in GLYPHS:
            continue
        family, _, _, cp, label, kind = GLYPHS[marker]
        op = soup.new_tag("mo")
        op.string = chr(cp)
        op["class"] = "olp-exact-operator"
        op["style"] = "font-family:"+FONT_FAMILIES[family][0]
        op["mathvariant"] = "normal"
        op["stretchy"] = "false"
        op["lspace"] = op["rspace"] = {"bin":"0.222222em","rel":"0.277778em","ord":"0em"}[kind]
        op["aria-label"] = label
        if family == 'text':
            size=soup.new_tag('mstyle')
            size['scriptlevel']='0';size['mathsize']='0.545455em'
            size.append(op);element.replace_with(size)
        else:
            element.replace_with(op)
        rendered_operators[marker] += 1
    rendered_smallcaps=0
    for element in soup.find_all('mtext'):
        hit=re.fullmatch(r'OLPSMALLCAPSSTART(.*?)OLPSMALLCAPSEND',element.get_text(),re.S)
        if hit:
            element.string=hit[1]
            element['style']='font-variant:small-caps'
            rendered_smallcaps+=1
    for img in soup.find_all("img"):
        name = Path(img.get("src", "")).stem
        if name in graph_descriptions:
            img["alt"] = graph_descriptions[name]
    rendered_equation_labels = 0
    for element in soup.find_all("mtext"):
        key = element.get_text(strip=True)
        if key in EQUATION_LABELS:
            formula = element.find_parent("math")
            assert formula is not None and not formula.has_attr("id"), key
            formula["id"] = EQUATION_LABELS[key]
            element.decompose()
            rendered_equation_labels += 1
    rendered_math_links = 0
    unsupported_math_links = []
    for element in soup.find_all("mtext"):
        key = element.get_text(strip=True)
        if key not in MATH_LINKS:
            continue
        link = MATH_LINKS[key]
        if re.search(r"[\\$]", link["shown"]):
            unsupported_math_links.append({"marker": key, **link})
            continue
        # Braces in auxiliary theorem numbers are TeX grouping, not glyphs.
        element.string = link["shown"].replace("{", "").replace("}", "")
        element["href"] = "#" + link["target"]
        rendered_math_links += 1
    # Pandoc keeps TeX equation labels in annotations without DOM anchors.
    # Attach each exact label to its matching MathML row when possible.
    for formula in soup.find_all("math"):
        annotation = formula.find("annotation", attrs={"encoding": "application/x-tex"})
        if annotation is None:
            continue
        annotation.string = re.sub(r"\\text\{(OLPMATHLINK\d+)\}",
                                   lambda m: MATH_LINKS[m[1]]["original"], annotation.get_text())
        annotation.string = re.sub(r"\\text\{(OLPEQLABEL\d+)\}",
                                   lambda m: r"\label{"+EQUATION_LABELS[m[1]]+"}", annotation.get_text())
        for marker in GLYPHS:
            annotation.string = annotation.get_text().replace(r"\text{OLPGLYPH"+marker+"}", "\\"+marker.lower())
        annotation.string=re.sub(r'\\text\{OLPSMALLCAPSSTART(.*?)OLPSMALLCAPSEND\}',
                                 lambda m:r'\textsc{'+m[1]+'}',annotation.get_text(),flags=re.S)
        math_labels = re.findall(r"\\label\{([^}]+)\}", annotation.get_text())
        if not math_labels:
            continue
        rows = formula.find_all("mtr")
        if len(rows) == len(math_labels):
            for row, label in zip(rows, math_labels):
                row["id"] = label
        elif len(math_labels) == 1:
            formula["id"] = math_labels[0]
        else:
            for label in math_labels:
                anchor = soup.new_tag("span", id=label)
                formula.insert_before(anchor)
    HTML.write_text(str(soup), encoding="utf-8", newline="\n")
    ids = [element["id"] for element in soup.select("[id]")]
    ids_set = set(ids)
    source_units = re.findall(r"(?m)^% BEGIN (OLP-\d{4})$", text)
    html_units = re.findall(r"guunit:(OLP-\d{4})", " ".join(ids))
    warnings = Counter(re.findall(r"unexpected control sequence (\\[A-Za-z]+)", result.stderr))
    receipt = {
        "schema": "openlogic-gu-full-epub-html-preparation/1",
        "status": "draft_blocked_until_all_semantic_checks_pass",
        "accepted_source_sha256": sha(MASTER),
        "reference_auxiliary": current_aux(ROOT)[1],
        "prepared_sha256": sha(PREPARED),
        "html_sha256": sha(HTML),
        "source_unit_markers": len(source_units),
        "source_unique_units": len(set(source_units)),
        "html_unique_unit_ids": len(set(html_units)),
        "html_duplicate_ids": [key for key, count in Counter(ids).items() if count > 1][:100],
        "mathml_nodes": len(soup.find_all("math")),
        "tex_math_fallback_nodes": len(soup.select("span.math")),
        "svg_images": len(soup.select('img[src$=".svg"]')),
        "all_images": len(soup.find_all("img")),
        "source_tikz_diagrams": text.count(r"\begin{tikzpicture}"),
        "broken_fragment_links": [a.get("href") for a in soup.select('[href^="#"]')
                                  if a.get("href", "")[1:] not in ids_set][:100],
        "registered_math_links": len(MATH_LINKS),
        "rendered_math_links": rendered_math_links,
        "unsupported_math_links": unsupported_math_links,
        "internal_math_link_markers_remaining": len(re.findall(r"OLPMATHLINK\d+", str(soup))),
        "rendered_turing_figures": len(graph_receipts),
        "rendered_relation_figures": len(relation_receipts),
        "rendered_native_pdf_figures": len(native_receipts),
        "registered_equation_labels": len(EQUATION_LABELS),
        "rendered_equation_labels": rendered_equation_labels,
        "internal_equation_label_markers_remaining": len(re.findall(r"OLPEQLABEL\d+", str(soup))),
        "exact_source_font_operators": dict(rendered_operators),
        "exact_operator_font_outputs": operator_fonts["outputs"],
        "rendered_smallcaps_labels": rendered_smallcaps,
        "internal_smallcaps_markers_remaining":len(re.findall(r'OLPSMALLCAPS(?:START|END)',str(soup))),
        "internal_operator_markers_remaining": len(re.findall(r"OLPGLYPH[A-Z]+", str(soup))),
        "source_table_groups": table_groups,
        "rendered_source_table_groups": len(soup.select("figure.olp-source-table")),
        "internal_table_markers_remaining": len(re.findall(r"OLPTABLECAP\d+", str(soup))),
        "unknown_math_macros_top": warnings.most_common(60),
        "unresolved_relative_references": sorted(set(unresolved_refs))[:100],
        "rendered_proof_structures": len(proof_receipts),
        "remaining_proof_commands": len(re.findall(
            r"\\(?:AxiomC|Axiom|DeduceC|Deduce|UnaryInfC|UnaryInf|BinaryInfC|BinaryInf|TrinaryInfC|TrinaryInf)(?![A-Za-z])",
            text)),
        "source_derived_math_definitions": len(macro_mapping),
        "pandoc_stderr_bytes": STDERR.stat().st_size,
    }
    RECEIPT.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8", newline="\n")
    print(json.dumps({key: receipt[key] for key in (
        "source_unique_units", "html_unique_unit_ids", "mathml_nodes",
        "tex_math_fallback_nodes", "svg_images", "source_tikz_diagrams",
        "pandoc_stderr_bytes")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
