"""Inventory the exact TikZ illustrations needed by the 722-unit EPUB."""

from __future__ import annotations

from bisect import bisect_right
from pathlib import Path
import hashlib
import json
import re

from prepare_full_epub_html import balanced
from full_reader_aux import current_aux


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "reader" / "full-reader.tex"
OUTPUT = ROOT / "build" / "FULL_EPUB_FIGURE_COVERAGE.json"


def aux_pages(text: str) -> dict[str, int]:
    pages = {}
    for line in text.splitlines():
        if not line.startswith(r"\newlabel{"):
            continue
        label, pos = balanced(line, len(r"\newlabel"), "{", "}")
        if label.endswith("@cref"):
            continue
        payload, _ = balanced(line, pos, "{", "}")
        if not payload.startswith("{"):
            continue
        _, end = balanced(payload, 0, "{", "}")
        page, _ = balanced(payload, end, "{", "}")
        if page.isdigit():
            pages[label] = int(page)
    return pages


def main() -> None:
    source = SOURCE.read_text(encoding="utf-8")
    source_sha = hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    bindings = []
    for filename, method in [('FULL_EPUB_NATIVE_FIGURES.json','inspected_exact_pdf_vector_crop'),
                             ('FULL_EPUB_TURING_FIGURES.json','source_derived_turing_svg'),
                             ('FULL_EPUB_RELATION_FIGURES.json','source_derived_relation_svg')]:
        receipt = json.loads((ROOT/'build'/filename).read_text(encoding='utf-8-sig'))
        assert receipt['input_sha256'] == source_sha, (filename,'Stale figure conversion')
        for entry in receipt['figures']:
            path = entry.get('svg_path') or entry.get('asset')
            if path is None:
                matches = list((ROOT/'build/full-epub-media').rglob(entry['name']+'.svg'))
                assert len(matches)==1, entry['name']
                path = str(matches[0].relative_to(ROOT))
            assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == entry['svg_sha256'], path
            bindings.append({'source_sha256':entry.get('source_sha256') or entry['source_tikz_sha256'],
                             'unit':entry.get('unit'), 'svg_path':path,
                             'svg_sha256':entry['svg_sha256'], 'method':method})
    used = set()
    aux, auxiliary = current_aux(ROOT)
    pages = aux_pages(aux.read_text(encoding="utf-8", errors="replace"))
    units = list(re.finditer(r"(?m)^% BEGIN (OLP-\d{4})$", source))
    starts = [match.start() for match in units]
    pictures = list(re.finditer(
        r"\\begin\{tikzpicture\}[\s\S]*?\\end\{tikzpicture\}", source
    ))
    rows = []
    for index, picture in enumerate(pictures, 1):
        unit = units[bisect_right(starts, picture.start()) - 1][1]
        section = source[starts[bisect_right(starts, picture.start()) - 1]:picture.start()]
        ident = list(re.finditer(r"\\olfileid\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}", section))
        prefix = ":".join(ident[-1].groups()) if ident else None
        figure_begin = source.rfind(r"\begin{figure}", 0, picture.start())
        figure_end_before = source.rfind(r"\end{figure}", 0, picture.start())
        in_figure = figure_begin > figure_end_before
        caption = None
        full_label = None
        if in_figure:
            figure_end = source.find(r"\end{figure}", picture.end())
            figure_source = source[figure_begin:figure_end]
            caption_command = re.search(r"\\caption(?:\[[^]]*\])?", figure_source)
            if caption_command:
                caption, _ = balanced(figure_source, caption_command.end(), "{", "}")
            label_match = re.search(r"\\(ollabel|label)\{([^}]+)\}",
                                    source[picture.end():figure_end])
            if label_match:
                full_label = (prefix + ":" + label_match[2]
                              if label_match[1] == "ollabel" and prefix else label_match[2])
        page = pages.get(full_label) if full_label else None
        unit_page = pages.get("guunit:" + unit)
        diagram_sha = hashlib.sha256(picture[0].encode("utf-8")).hexdigest()
        candidates = [(i,b) for i,b in enumerate(bindings) if i not in used
                      and b['source_sha256']==diagram_sha and (b['unit'] is None or b['unit']==unit)]
        assert candidates, (index,unit,'No exact source/asset binding')
        binding_index,binding=candidates[0];used.add(binding_index)
        rows.append({
            "index": index,
            "unit": unit,
            "source_sha256": diagram_sha,
            "source_bytes": len(picture[0].encode("utf-8")),
            "source_offset": picture.start(),
            "in_figure": in_figure,
            "caption_tex": caption,
            "label": full_label,
            "printed_page": page,
            "unit_start_printed_page": unit_page,
            "render_binding": binding,
        })
    output = {
        "schema": "openlogic-gu-full-epub-figure-coverage/2",
        "current_source_sha256": source_sha,
        "scope": "Exact current diagram bytes bound one-to-one to verified SVG assets. Page hints and references are from a successful build of this exact current reader. No EPUB-reader QA claim.",
        "reference_auxiliary": auxiliary,
        "count": len(rows),
        "bound_svg_count": len(used),
        "figures": rows,
    }
    assert len(used)==len(bindings)==len(rows), 'Unused or missing figure binding'
    OUTPUT.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8", newline="\n")
    print(json.dumps({key: output[key] for key in (
        "count", "bound_svg_count")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
