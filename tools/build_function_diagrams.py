"""Convert all exact upstream Bezier paths to SVG; no TeX or raster substitution."""
from pathlib import Path
import re,json,hashlib
R=Path(__file__).resolve().parents[1];O=R/'reader/assets'
colors={'oldiagcolorA':'#000000','oldiagcolorB':'#808080','oldiagcolorC':'#a81c21','oldiagcolorD':'#1973ba'}
out=[]
for name in ['function','surjective','injective','bijective','composition']:
    src=R/'upstream/assets/diagrams'/f'{name}.tikz';t=src.read_text(encoding='utf-8')
    assert 'yscale=-1.000000, xscale=1.000000' in t
    assert not re.search(r'\\(?:node|draw|fill|clip)\b',t)
    scopes=re.findall(r'\\begin\{scope\}\[([^\]]+)\]',t)
    assert not scopes or (name=='function' and scopes==['shift={(1159.8262,388.50513)}'])
    paths=[];coords=[]
    for m in re.finditer(r'\\path\[([\s\S]*?)\]([\s\S]*?);',t):
        opt,data=m.groups()
        coords+= [(float(x),float(y)) for x,y in re.findall(r'\(([\d.-]+),([\d.-]+)\)',data)]
        stroke=re.search(r'draw=(\w+)',opt);fill=re.search(r'fill=(\w+)',opt)
        width=float(re.search(r'width=([\d.]+)pt',opt)[1])/0.8
        data=re.sub(r'--\s*cycle.*',' Z',data)
        data=re.sub(r'\.\.\s*controls',' C',data);data=re.sub(r'\band\b','',data)
        data=data.replace('..',' ').replace('--',' L ')
        data=re.sub(r'\(([\d.-]+),([\d.-]+)\)',r'\1 \2 ',data).strip()
        data='\n'.join(line.rstrip() for line in data.splitlines())
        assert not re.search(r'[^MLCZ\d.\s-]',data)
        attrs=f'fill="{colors[fill[1]] if fill else "none"}" stroke="{colors[stroke[1]] if stroke else "none"}" stroke-width="{width:g}" stroke-linejoin="miter" stroke-linecap="butt"'
        dash=re.search(r'dash pattern=on ([\d.]+)pt off ([\d.]+)pt',opt)
        if dash:attrs+=f' stroke-dasharray="{float(dash[1])/0.8:g} {float(dash[2])/0.8:g}"'
        paths.append(f'<path d="M {data}" {attrs}/>')
    assert len(paths)==len(re.findall(r'\\path\[',t))
    xs,ys=zip(*coords);pad=8
    view=f'{min(xs)-pad:g} {min(ys)-pad:g} {max(xs)-min(xs)+2*pad:g} {max(ys)-min(ys)+2*pad:g}'
    dest=O/f'{name}.svg'
    dest.write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="'+view+'" role="img">'+''.join(paths)+'</svg>',encoding='utf-8')
    out.append(dict(asset=dest.relative_to(R).as_posix(),source=src.relative_to(R).as_posix(),source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),svg_sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),paths=len(paths),coordinate_pairs=len(coords),method='All Bezier coordinates, control points, paths, colors, fills, widths and dashes retained. Single global translation in function.tikz absorbed into viewBox; original y reflection matches SVG downward y axis.'))
(R/'build/function-diagrams-qa.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps([dict(asset=x['asset'],paths=x['paths']) for x in out]))
