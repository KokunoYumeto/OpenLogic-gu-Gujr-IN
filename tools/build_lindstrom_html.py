"""Build the cumulative 204-unit Lindström HTML reader.

The long-lived generic renderer still enumerates released checkpoints. This
small adapter extends its accepted interpolation profile while keeping the
shared rendering and QA implementation byte-for-byte in one place.
"""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
template = ROOT / "tools" / "build_functions_html.py"
code = template.read_text(encoding="utf-8")

assert code.count(",'interpolation'}") == 19
code = code.replace(",'interpolation'}", ",'interpolation','lindstrom'}")

replacements = {
    ",'interpolation':199}[edition]": ",'interpolation':199,'lindstrom':204}[edition]",
    ",'interpolation':'૧૯૯'}[edition]": ",'interpolation':'૧૯૯','lindstrom':'૨૦૪'}[edition]",
    "    'interpolation':'અંતર્વેશન પ્રમેય સહિત ઓપન લોજિક ગુજરાતી',\n": (
        "    'interpolation':'અંતર્વેશન પ્રમેય સહિત ઓપન લોજિક ગુજરાતી',\n"
        "    'lindstrom':'લિન્ડસ્ટ્રોમનું પ્રમેય સહિત ઓપન લોજિક ગુજરાતી',\n"
    ),
    ",'interpolation':124}[edition]": ",'interpolation':124,'lindstrom':124}[edition]",
    ",'interpolation':14}[edition]": ",'interpolation':14,'lindstrom':15}[edition]",
    "    if edition=='interpolation':\n        model_chapters.append(r'\\section{અંતર્વેશન પ્રમેય}')\n": (
        "    if edition in {'interpolation','lindstrom'}:\n"
        "        model_chapters.append(r'\\section{અંતર્વેશન પ્રમેય}')\n"
        "    if edition=='lindstrom':\n"
        "        model_chapters.append(r'\\section{લિન્ડસ્ટ્રોમનું પ્રમેય}')\n"
    ),
    "prefix.startswith(('mod:bas:','mod:mar:','mod:int:'))": (
        "prefix.startswith(('mod:bas:','mod:mar:','mod:int:','mod:lin:'))"
    ),
    "elif edition == 'interpolation':\n    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં અગાઉના સંપૂર્ણ પ્રકરણો તથા અંતર્વેશન પ્રમેયનું સંપૂર્ણ પ્રકરણ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'\n": (
        "elif edition == 'interpolation':\n"
        "    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં અગાઉના સંપૂર્ણ પ્રકરણો તથા અંતર્વેશન પ્રમેયનું સંપૂર્ણ પ્રકરણ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'\n"
        "elif edition == 'lindstrom':\n"
        "    notice_text = f'આ યંત્ર દ્વારા કરેલો અનુવાદ છે. આ આવૃત્તિમાં અગાઉના સંપૂર્ણ પ્રકરણો તથા લિન્ડસ્ટ્રોમના પ્રમેયનું સંપૂર્ણ પ્રકરણ છે: ૭૨૨માંથી {coverage_gu} મૂળ એકમો. સંપૂર્ણ ગ્રંથનું કામ ચાલુ છે.'\n"
    ),
}
for before, after in replacements.items():
    assert code.count(before) == 1, before
    code = code.replace(before, after)

old_read = "body=(B/f'{edition}-body.tex').read_text(encoding='utf-8')\n"
new_read = old_read + r"""# Expand the model-class macro newly exercised by the Lindström chapter.
def expand_model_class(match):
    language, logic, formula = match.groups()
    superscript = r'^{\mathcal{' + language + '}}' if language else ''
    return r'\mathrm{Mod}' + superscript + '_{' + logic + '}(' + formula + ')'
body = re.sub(
    r'\\Mod(?:\[([^\]]+)\])?\(([^)]+)\)\{([^{}]+)\}',
    expand_model_class,
    body,
)
assert r'\Mod' not in body
"""
assert code.count(old_read) == 1
code = code.replace(old_read, new_read)

old_graph_marker = "    if '[grow\\'=up]' in src:\n"
new_graph_case = r"""    if "[node distance=2cm, auto, thick, >=stealth']" in src:
        assert r'\draw [rounded corners] (0,0) -- (8,0) -- (8,4) -- (0,4) --  cycle;' in src
        assert re.findall(r'\\draw \(([^)]+)\) circle \(([^)]+)cm\);', src) == [
            ('2,2', '0.5'), ('2,2', '1.25'), ('6,2', '0.5'), ('6,2', '1.25')
        ]
        for label in (r'\Struct{A}', r'\Struct{M}', r'\Struct{N}', r'\Struct{M}^*', r'\Struct{N}^*', 'I'):
            assert label in src
        name='lindstrom-partial-isomorphism'
        alt=('મોટા આયતથી દર્શાવેલી વ્યાપક સંરચના Aમાં ડાબે M-તારક અને જમણે '
             'N-તારકના વર્તુળો છે; એમની અંદર અનુક્રમે M અને N છે, અને બંને '
             'તરફ વચ્ચેનો દ્વિમુખી તીર આંશિક એકરૂપતા I દર્શાવે છે.')
        svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 400" role="img">
<defs><marker id="lin-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#222"/></marker></defs>
<rect x="10" y="10" width="780" height="380" rx="14" fill="none" stroke="#222" stroke-width="3"/>
<circle cx="200" cy="200" r="125" fill="none" stroke="#222" stroke-width="3"/>
<circle cx="200" cy="200" r="50" fill="none" stroke="#222" stroke-width="3"/>
<circle cx="600" cy="200" r="125" fill="none" stroke="#222" stroke-width="3"/>
<circle cx="600" cy="200" r="50" fill="none" stroke="#222" stroke-width="3"/>
<path d="M325,200 L475,200" fill="none" stroke="#222" stroke-width="3" marker-start="url(#lin-arrow)" marker-end="url(#lin-arrow)"/>
<g font-family="Noto Serif, serif" font-size="34" text-anchor="middle">
<text x="75" y="62">𝔄</text><text x="200" y="212">𝔐</text><text x="600" y="212">𝔑</text>
<text x="200" y="330">𝔐*</text><text x="600" y="330">𝔑*</text><text x="400" y="185">I</text>
</g></svg>'''
        path=O/'assets'/f'{name}.svg';path.write_text(svg,encoding='utf-8',newline='\n')
        graph_receipts.append(dict(
            asset=path.relative_to(R).as_posix(),
            source_tikz_sha256=hashlib.sha256(src.encode('utf-8')).hexdigest(),
            svg_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
            rectangle=[0,0,8,4],
            circles=[[2,2,0.5],[2,2,1.25],[6,2,0.5],[6,2,1.25]],
            relation='I',
            method='Deterministic SVG reconstruction of the exact source rectangle, four nested circles, five structure labels and bidirectional I arrow.',
        ))
        graph_alt[name]=alt
        return '\n\n'+r'\includegraphics{assets/'+name+'.svg}\n\n'
"""
assert code.count(old_graph_marker) == 1
code = code.replace(old_graph_marker, new_graph_case + old_graph_marker)

old_figure = r"""        lid=re.search(r'\\label\{([^}]+)\}',t)[1];labels[lid]=str(figcount)
        return r'\begin{center}\includegraphics{assets/'+asset+r'.svg}'+'\n'+r'\textbf{આકૃતિ '+str(figcount)+'.} '+cap+r'\label{'+lid+r'}\end{center}'
"""
new_figure = r"""        lid_match=re.search(r'\\label\{([^}]+)\}',t)
        label_markup=''
        if lid_match is not None:
            lid=lid_match[1];labels[lid]=str(figcount);label_markup=r'\label{'+lid+'}'
        return r'\begin{center}\includegraphics{assets/'+asset+r'.svg}'+'\n'+r'\textbf{આકૃતિ '+str(figcount)+'.} '+cap+label_markup+r'\end{center}'
"""
assert code.count(old_figure) == 1
code = code.replace(old_figure, new_figure)

old_correction_tail = """        'interpolation':('OLFUN-001થી OLFUN-005, OLSIZ-001થી OLSIZ-012, '
                    'OLARI-001થી OLARI-004, OLINF-001થી OLINF-002, '
                    'OLPL-001થી OLPL-002, OLPRF-001થી OLPRF-004, '
                    'OLSEQ-001થી OLSEQ-006, OLND-001થી OLND-006, '
                    'OLTAB-001થી OLTAB-012, OLAX-001થી OLAX-018, '
                    'OLCO-001થી OLCO-022, OLFINT-001થી OLFINT-006, '
                    'OLSYN-001થી OLSYN-007, OLSEM-001થી OLSEM-011, '
                    'OLMAT-001થી OLMAT-005, OLBYD-001થી OLBYD-006, '
                    'OLMTB-001થી OLMTB-008, OLMAR-001થી OLMAR-016 અને '
                    'OLINT-001થી OLINT-010 સુધીની'),
"""
new_correction_tail = old_correction_tail + """        'lindstrom':('OLFUN-001થી OLFUN-005, OLSIZ-001થી OLSIZ-012, '
                    'OLARI-001થી OLARI-004, OLINF-001થી OLINF-002, '
                    'OLPL-001થી OLPL-002, OLPRF-001થી OLPRF-004, '
                    'OLSEQ-001થી OLSEQ-006, OLND-001થી OLND-006, '
                    'OLTAB-001થી OLTAB-012, OLAX-001થી OLAX-018, '
                    'OLCO-001થી OLCO-022, OLFINT-001થી OLFINT-006, '
                    'OLSYN-001થી OLSYN-007, OLSEM-001થી OLSEM-011, '
                    'OLMAT-001થી OLMAT-005, OLBYD-001થી OLBYD-006, '
                    'OLMTB-001થી OLMTB-008, OLMAR-001થી OLMAR-016, '
                    'OLINT-001થી OLINT-010 અને OLLIN-001થી OLLIN-013 સુધીની'),
"""
assert code.count(old_correction_tail) == 1
code = code.replace(old_correction_tail, new_correction_tail)

old_editorial_tail = """        'interpolation':('અંતર્વેશનના નવા પ્રકરણમાં પૃથક્કરણ, મહત્તમ '
                    'અપૃથક્કરણીય જોડ દ્વારા ક્રેગના પ્રમેયની સાબિતી, સ્પષ્ટ અને '
                    'ગૂઢ વ્યાખ્યેયતા તથા બેથનું વ્યાખ્યેયતા પ્રમેય સામેલ છે. '
                    'સ્થિર મૂળની દસ ઓળખેલી પાઠ્ય, ઔપચારિક અથવા અર્થલક્ષી '
                    'ખામીઓ પારદર્શક નોંધો સાથે મર્યાદિત રીતે સુધારી છે.'),
"""
new_editorial_tail = old_editorial_tail + """        'lindstrom':('લિન્ડસ્ટ્રોમના નવા પ્રકરણમાં અમૂર્ત તર્કશાસ્ત્ર, સામાન્યતા, '
                    'સઘનતા, અધોગામી લેવેનહાઇમ--સ્કોલેમ અને પ્રથમ-ક્રમ તર્કશાસ્ત્રના '
                    'અભિવ્યક્તિશીલ મહત્તમત્વની સાબિતી સામેલ છે. સ્થિર મૂળની તેર '
                    'ઓળખેલી પાઠ્ય, ઔપચારિક અથવા અર્થલક્ષી ખામીઓ પારદર્શક નોંધો '
                    'સાથે મર્યાદિત રીતે સુધારી છે.'),
"""
assert code.count(old_editorial_tail) == 1
code = code.replace(old_editorial_tail, new_editorial_tail)

if __name__ == "__main__":
    generated = ROOT / "tools" / "build_lindstrom_html_expanded.py"
    generated.write_text(code, encoding="utf-8", newline="\n")
    sys.argv = [sys.argv[0], "lindstrom"]
    exec(compile(code, str(generated), "exec"), {"__name__": "__main__", "__file__": str(template)})
