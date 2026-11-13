"""Source-derived renderer for the two numeric relation graphs in this reader."""
from pathlib import Path
import hashlib
import json
import math
import re


def render_relation_graph(diagram, output_dir, root, records, descriptions):
    if not diagram.startswith(r'\begin{tikzpicture}[->,node distance=2cm]'):
        return None
    nodes = re.findall(r'\\node\[draw,circle\]\s*\((\w+)\)\s*(\[[^]]+\])?\s*\{\$?([1-4])\$?\};', diagram)
    edges = re.findall(r'\\draw\s*\((\w+)\)\s*to\s*(\[loop above\])?\s*\((\w+)\);', diagram)
    if len(nodes) not in {3,4} or len(edges) != 4:
        return None
    if {(a,b) for a,_,b in edges} != {('A','A'),('A','B'),('A','C'),('B','C')}:
        return None
    residual = re.sub(r'\\begin\{tikzpicture\}\[[^]]+\]|\\end\{tikzpicture\}', '', diagram)
    residual = re.sub(r'\\node\[draw,circle\]\s*\(\w+\)\s*(?:\[[^]]+\])?\s*\{\$?[1-4]\$?\};', '', residual)
    residual = re.sub(r'\\draw\s*\(\w+\)\s*to\s*(?:\[loop above\])?\s*\(\w+\);', '', residual)
    assert not residual.strip(), residual
    positions, labels = {}, {}
    for name, option, label in nodes:
        labels[name] = label
        if not positions:
            assert not option
            positions[name] = (70,80)
        else:
            placement = re.fullmatch(r'\[(right|below) of=(\w+)\]', option)
            assert placement and placement[2] in positions
            x,y = positions[placement[2]]
            positions[name] = (x+90,y) if placement[1] == 'right' else (x,y+90)
    width = max(x for x,y in positions.values())+65
    height = max(y for x,y in positions.values())+55
    edge_labels = [labels[a]+'→'+labels[b] for a,_,b in edges]
    description = 'ઘટકો '+', '.join(labels.values())+'; દિશાસંબંધ: '+', '.join(edge_labels)+'.'
    name = f'relation-graph-{len(records)+1:02}'
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
             f'<title>{description}</title>', '<g fill="none" stroke="#111" stroke-width="1.6">']
    def arrow(x,y,dx,dy):
        norm=math.hypot(dx,dy);dx/=norm;dy/=norm
        return f'<path d="M {x-8*dx+4*dy:.3f} {y-8*dy-4*dx:.3f} L {x:.3f} {y:.3f} L {x-8*dx-4*dy:.3f} {y-8*dy+4*dx:.3f}"/>'
    for a,loop,b in edges:
        x,y = positions[a];xx,yy = positions[b]
        if loop:
            assert a == b
            x0,y0,x1,y1 = x-10,y-15,x+10,y-15
            lines.append(f'<path d="M {x0} {y0} C {x-43} {y-69}, {x+43} {y-69}, {x1} {y1}"/>')
            lines.append(arrow(x1,y1,x1-(x+43),y1-(y-69)))
        else:
            assert a != b
            dx,dy=xx-x,yy-y; norm=math.hypot(dx,dy);ux,uy=dx/norm,dy/norm
            x0,y0=x+18*ux,y+18*uy;x1,y1=xx-18*ux,yy-18*uy
            lines.append(f'<path d="M {x0:.3f} {y0:.3f} L {x1:.3f} {y1:.3f}"/>')
            lines.append(arrow(x1,y1,dx,dy))
    for x,y in positions.values():lines.append(f'<circle cx="{x}" cy="{y}" r="18"/>')
    lines.append('</g><g fill="#111" font-family="serif" font-size="18" text-anchor="middle">')
    for n,(x,y) in positions.items():lines.append(f'<text x="{x}" y="{y+6}">{labels[n]}</text>')
    lines.append('</g></svg>')
    svg = output_dir/'assets'/(name+'.svg');svg.parent.mkdir(parents=True,exist_ok=True)
    svg.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    records.append({'name':name,'source_sha256':hashlib.sha256(diagram.encode()).hexdigest(),
                    'svg_sha256':hashlib.sha256(svg.read_bytes()).hexdigest(),
                    'nodes':[{'id':n,'label':labels[n],'position':positions[n]} for n in positions],
                    'edges':[{'from':a,'to':b,'loop_above':bool(loop)} for a,loop,b in edges],
                    'alt_text_gu':description,'scope':'All source nodes/placement relations and directed edges parsed; explicit arrowheads.'})
    descriptions[name]=description
    return r'\includegraphics{build/full-epub-media/assets/'+name+'.svg}'
