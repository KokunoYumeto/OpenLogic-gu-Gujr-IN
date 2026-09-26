"""Deterministic, auditable SVG rendering of the frozen Turing-state TikZ graphs.

The source state positions, initial markers, directed incidence, transition
triples, loops, and bend hints are parsed rather than inferred from prose.
"""

from pathlib import Path
import hashlib
import html
import json
import math
import re


NODE = re.compile(
    r"\\node\[([^]]+)\]\s*\(([^)]+)\)\s*(?:\[([^]]+)\])?\s*"
    r"\{\$([^$]+)\$\}\s*;", re.S
)
TRANSITION = re.compile(r"\\TMtrans\{([^{}]+)\}\{([^{}]+)\}\{([^{}]+)\}")
EDGE = re.compile(r"\bedge\b")
REFERENCE = re.compile(r"\(([A-Za-z0-9]+)\)")
DIRECTIONS = {
    "right": (180, 0), "left": (-180, 0),
    "above": (0, -180), "below": (0, 180),
    "above right": (140, -140), "above left": (-140, -140),
    "below right": (140, 140), "below left": (-140, 140),
}
TM_SYMBOLS = {
    r"\TMendtape": "▷", r"\TMblank": "0", r"\TMstroke": "1",
    r"\TMright": "R", r"\TMleft": "L", r"\TMstay": "N",
}
SUBSCRIPT = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def balanced_brace(text: str, opening: int) -> tuple[str, int]:
    assert text[opening] == "{"
    depth = 0
    for index in range(opening, len(text)):
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return text[opening + 1:index], index + 1
    raise AssertionError("Unclosed edge label")


def display_symbol(symbol: str) -> str:
    symbol = symbol.strip()
    return TM_SYMBOLS.get(symbol, symbol)


def parse_graph(source: str) -> tuple[list[dict], list[dict]]:
    clean = re.sub(r"(?m)%[^\n]*", "", source)
    states = []
    positions = {}
    for match in NODE.finditer(clean):
        style, key, location, latex_label = match.groups()
        assert key not in positions, key
        if location:
            relation = re.fullmatch(
                r"(above right|above left|below right|below left|right|left|above|below) of=([A-Za-z0-9]+)",
                location.strip(),
            )
            assert relation is not None, location
            direction, anchor = relation.groups()
            assert anchor in positions, (key, anchor)
            dx, dy = DIRECTIONS[direction]
            x, y = positions[anchor]
            position = (x + dx, y + dy)
        else:
            assert not states
            position = (0, 0)
        positions[key] = position
        label = re.sub(r"q_\{?(\d+)\}?", lambda m: "q" + m[1].translate(SUBSCRIPT), latex_label)
        label = label.replace("\\", "")
        states.append({
            "id": key, "latex_label": latex_label, "label": label,
            "initial": "initial" in style.split(","), "position": position,
        })
    assert 2 <= len(states) <= 15, len(states)

    path_match = re.search(r"\\path\b([\s\S]*?);", clean)
    assert path_match is not None
    path = path_match[1]
    edges = []
    cursor = 0
    active_source = None
    for match in EDGE.finditer(path):
        preamble = path[cursor:match.start()]
        references = REFERENCE.findall(preamble)
        if references:
            active_source = references[-1]
        assert active_source in positions, (active_source, path[:match.start()][-90:])
        index = match.end()
        while path[index].isspace():
            index += 1
        options = ""
        if path[index] == "[":
            ending = path.index("]", index)
            options = path[index + 1:ending]
            index = ending + 1
        node_match = re.match(r"\s*node(?:\[[^]]*\])?\s*", path[index:])
        assert node_match is not None, path[index:index + 80]
        index += node_match.end()
        assert path[index] == "{", path[index:index + 30]
        raw_label, index = balanced_brace(path, index)
        destination = REFERENCE.match(path, index + len(path[index:]) - len(path[index:].lstrip()))
        assert destination is not None, path[index:index + 35]
        target = destination[1]
        assert target in positions, target
        triples = [tuple(display_symbol(part) for part in groups)
                   for groups in TRANSITION.findall(raw_label)]
        assert 1 <= len(triples) <= 2, (active_source, target, raw_label)
        edges.append({
            "source": active_source, "target": target, "options": options,
            "triples": triples,
        })
        cursor = destination.end()
    assert edges and all(edge["source"] in positions for edge in edges)
    assert clean.count(r"\TMtrans{") == sum(len(edge["triples"]) for edge in edges)
    return states, edges


def transition_lines(edge: dict) -> list[str]:
    return [", ".join(triple) for triple in edge["triples"]]


def render_turing_diagram(
    source: str, output_root: Path, repo_root: Path,
    receipts: list[dict], descriptions: dict[str, str],
) -> str:
    states, edges = parse_graph(source)
    number = 1 + sum(Path(receipt["asset"]).stem.startswith("turing-machine-")
                     for receipt in receipts)
    name = f"turing-machine-{number:02d}"
    coordinates = {state["id"]: state["position"] for state in states}
    xmin = min(x for x, _ in coordinates.values())
    xmax = max(x for x, _ in coordinates.values())
    ymin = min(y for _, y in coordinates.values())
    ymax = max(y for _, y in coordinates.values())
    margin_x, margin_y = 110, 120
    width = xmax - xmin + 2 * margin_x
    height = ymax - ymin + 2 * margin_y
    coords = {key: (x - xmin + margin_x, y - ymin + margin_y)
              for key, (x, y) in coordinates.items()}
    alt = "અવસ્થાચિત્ર: " + "; ".join(
        f"{next(s['label'] for s in states if s['id'] == edge['source'])} થી "
        f"{next(s['label'] for s in states if s['id'] == edge['target'])}: "
        + " અથવા ".join(transition_lines(edge))
        for edge in edges
    )
    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" '
        'role="img" aria-labelledby="tm-title tm-desc">',
        f'<title id="tm-title">ટ્યુરિંગ મશીનનું અવસ્થાચિત્ર {number}</title>',
        f'<desc id="tm-desc">{html.escape(alt)}</desc>',
        '<defs><marker id="tm-arrow" markerWidth="10" markerHeight="10" '
        'refX="9" refY="5" orient="auto" markerUnits="userSpaceOnUse">'
        '<path d="M0,0 L10,5 L0,10" fill="none" stroke="#17233b" '
        'stroke-width="1.5"/></marker></defs>',
        '<g fill="none" stroke="#17233b" stroke-width="2.2" '
        'marker-end="url(#tm-arrow)">',
    ]
    loop_counts = {}
    for edge in edges:
        start = coords[edge["source"]]
        finish = coords[edge["target"]]
        sx, sy = start
        tx, ty = finish
        if start == finish:
            orientation = next((side for side in ("above", "below", "left", "right")
                                if "loop " + side in edge["options"]), "above")
            key = (edge["source"], orientation)
            repeat = loop_counts.get(key, 0)
            loop_counts[key] = repeat + 1
            reach = 68 + 26 * repeat
            if orientation == "above":
                path = f"M{sx-16},{sy-20} C{sx-56},{sy-reach} {sx+56},{sy-reach} {sx+16},{sy-20}"
                label_at = (sx, sy - reach + 8)
            elif orientation == "below":
                path = f"M{sx+16},{sy+20} C{sx+56},{sy+reach} {sx-56},{sy+reach} {sx-16},{sy+20}"
                label_at = (sx, sy + reach - 2)
            elif orientation == "left":
                path = f"M{sx-20},{sy+16} C{sx-reach},{sy+56} {sx-reach},{sy-56} {sx-20},{sy-16}"
                label_at = (sx - reach, sy)
            else:
                path = f"M{sx+20},{sy-16} C{sx+reach},{sy-56} {sx+reach},{sy+56} {sx+20},{sy+16}"
                label_at = (sx + reach, sy)
        else:
            dx, dy = tx - sx, ty - sy
            length = math.hypot(dx, dy)
            ux, uy = dx / length, dy / length
            start_x, start_y = sx + 26 * ux, sy + 26 * uy
            end_x, end_y = tx - 29 * ux, ty - 29 * uy
            if "bend left" in edge["options"]:
                bend = -38
            elif "bend right" in edge["options"]:
                bend = 38
            else:
                bend = 0
            nx, ny = -uy, ux
            mid_x, mid_y = (start_x + end_x) / 2, (start_y + end_y) / 2
            if bend:
                control_x, control_y = mid_x + bend * nx, mid_y + bend * ny
                path = (f"M{start_x:.1f},{start_y:.1f} Q{control_x:.1f},{control_y:.1f} "
                        f"{end_x:.1f},{end_y:.1f}")
                label_at = (mid_x + bend * nx / 2, mid_y + bend * ny / 2)
            else:
                path = f"M{start_x:.1f},{start_y:.1f} L{end_x:.1f},{end_y:.1f}"
                label_at = (mid_x, mid_y)
            label_at = (label_at[0] + (16 if abs(dy) > abs(dx) else 0),
                        label_at[1] - (13 if abs(dx) >= abs(dy) else 0))
        svg.append(f'<path d="{path}"/>')
        edge["label_position"] = [round(value, 1) for value in label_at]
    svg.append('</g>')
    for edge in edges:
        x, y = edge["label_position"]
        lines = transition_lines(edge)
        line_height = 19
        box_width = max(62, 8 * max(len(line) for line in lines) + 16)
        box_height = 9 + line_height * len(lines)
        svg.append(f'<rect x="{x-box_width/2:.1f}" y="{y-box_height/2:.1f}" '
                   f'width="{box_width}" height="{box_height}" rx="4" '
                   'fill="white" fill-opacity="0.93"/>')
        for line_number, line in enumerate(lines):
            baseline = y - (len(lines)-1) * line_height/2 + line_number * line_height + 5
            svg.append(f'<text x="{x:.1f}" y="{baseline:.1f}" text-anchor="middle" '
                       'font-family="Noto Sans, DejaVu Sans, sans-serif" '
                       f'font-size="15" fill="#17233b">{html.escape(line)}</text>')
    for state in states:
        x, y = coords[state["id"]]
        if state["initial"]:
            svg.append(f'<path d="M{x-70},{y} L{x-27},{y}" fill="none" '
                       'stroke="#17233b" stroke-width="2.2" marker-end="url(#tm-arrow)"/>')
        svg.append(f'<circle cx="{x}" cy="{y}" r="26" fill="white" '
                   'stroke="#17233b" stroke-width="2.2"/>')
        svg.append(f'<text x="{x}" y="{y+6}" text-anchor="middle" '
                   'font-family="Noto Sans, DejaVu Sans, sans-serif" '
                   f'font-size="19" fill="#17233b">{html.escape(state["label"])}</text>')
    svg.append('</svg>')
    payload = "\n".join(svg) + "\n"
    path = output_root / "assets" / f"{name}.svg"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(payload, encoding="utf-8", newline="\n")
    receipts.append({
        "asset": path.relative_to(repo_root).as_posix(),
        "source_tikz_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
        "svg_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "states": [{key: value for key, value in state.items() if key != "position"}
                   for state in states],
        "transitions": [{key: value for key, value in edge.items()
                         if key != "label_position"} for edge in edges],
        "method": "Source-derived SVG: state positions, initial arrows, directed edges, loops, bend hints, and every transition triple are parsed and checked.",
    })
    descriptions[name] = alt
    return "\n\n" + r"\includegraphics{assets/" + name + ".svg}" + "\n\n"


if __name__ == "__main__":
    import sys
    repo = Path(__file__).resolve().parents[1]
    prepared = (repo / "build" / "turing-machines-body.tex").read_text(encoding="utf-8")
    pictures = [picture for picture in re.findall(
        r"\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}", prepared
    ) if r"\tikzstyle{every state}" in picture]
    receipts: list[dict] = []
    descriptions: dict[str, str] = {}
    for picture in pictures:
        render_turing_diagram(picture, repo / "reader", repo, receipts, descriptions)
    assert len(receipts) == 13
    print(json.dumps({
        "diagrams": len(receipts),
        "states": sum(len(receipt["states"]) for receipt in receipts),
        "transitions": sum(len(receipt["transitions"]) for receipt in receipts),
        "transition_triples": sum(sum(len(edge["triples"]) for edge in receipt["transitions"])
                                  for receipt in receipts),
    }))
