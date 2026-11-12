"""Use the frozen edition's real mathematical definitions for Pandoc.

Only plain zero-argument or mandatory-argument declarations are translated
automatically. Optional arguments and TeX conditionals require explicit,
source-checked handlers in the full EPUB converter.
"""
from __future__ import annotations
from pathlib import Path
import re


def group(text: str, pos: int, opening: str = "{", closing: str = "}"):
    while text[pos:pos+1].isspace():
        pos += 1
    if text[pos:pos+1] != opening:
        raise ValueError("Expected group")
    start = pos + 1
    depth = 1
    pos += 1
    while depth and pos < len(text):
        if text[pos] in {opening, closing}:
            backslashes = 0
            previous = pos-1
            while previous >= 0 and text[previous] == "\\":
                backslashes += 1
                previous -= 1
            # An odd run escapes the brace; an even run ends in a
            # line-break command and leaves the brace structural.
            if backslashes % 2 == 0:
                depth += 1 if text[pos] == opening else -1
        pos += 1
    if depth:
        raise ValueError("Unclosed group")
    return text[start:pos-1], pos


def definitions(path: Path) -> dict[str, tuple[int, str]]:
    source = re.sub(r"(?<!\\)%[^\n]*", "", path.read_text(encoding="utf-8"))
    output = {}
    pattern = re.compile(r"\\(DeclareDocumentMacro|DeclareDocumentCommand|newcommand)\*?\s*")
    for match in pattern.finditer(source):
        pos = match.end()
        try:
            if source[pos:pos+1] == "{":
                token, pos = group(source, pos)
            else:
                hit = re.match(r"\\[A-Za-z]+", source[pos:])
                if not hit:
                    continue
                token = hit[0]
                pos += len(token)
            name = token.strip().lstrip("\\")
            arity = 0
            if match[1] == "DeclareDocumentCommand":
                spec, pos = group(source, pos)
                spec = re.sub(r"\s", "", spec)
                if not re.fullmatch(r"m*", spec):
                    continue
                arity = len(spec)
            elif match[1] == "newcommand":
                while source[pos:pos+1].isspace():
                    pos += 1
                if source[pos:pos+1] == "[":
                    count, pos = group(source, pos, "[", "]")
                    arity = int(count)
                    while source[pos:pos+1].isspace():
                        pos += 1
                    if source[pos:pos+1] == "[":
                        continue
            while source[pos:pos+1].isspace():
                pos += 1
            if source[pos:pos+1] == "{":
                body, pos = group(source, pos)
            else:
                hit = re.match(r"\\[A-Za-z]+", source[pos:])
                if not hit:
                    continue
                body = hit[0]
            if re.search(r"#([1-9])", body) and max(map(int, re.findall(r"#([1-9])", body))) > arity:
                continue
            if re.search(r"\\(?:If|Declare|hbox|hskip|llap|hfil|@|lookup|applytofirst|redone|redpar|red|cd|equal)", body):
                continue
            body = re.sub(r"\s+", " ", body).strip()
            # These wrappers affect font or horizontal layout, not symbols.
            body = body.replace(r"\mathexclaim", "!")
            body = body.replace(r"\emph", r"\text")
            body = re.sub(r"\\ensuremath\{(.*)\}$", r"\1", body)
            output[name] = (arity, body)
        except (ValueError, IndexError):
            continue
    return output


def macros(path: Path) -> tuple[str, dict[str, tuple[int, str]]]:
    mapping = definitions(path)
    # Exact non-plain source definitions, rendered with standard MathML
    # primitives. These replace inherited semantic guesses.
    mapping.update({
        "supstrict": (0, r"\operatorname{lsub}"),
        "precdot": (0, r"\mathrel{\prec\!\cdot}"),
        "closeTuple": (0, r"\rangle"),
        "epsilon": (0, r"\varepsilon"),
        "mathexclaim": (0, "!"),
    })
    result = []
    for name, (arity, body) in sorted(mapping.items()):
        result.append(r"\newcommand{" + chr(92) + name + "}" + ("[" + str(arity) + "]" if arity else "") + "{" + body + "}")
    return "\n".join(result), mapping
