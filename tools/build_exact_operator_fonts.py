"""Repackage source-font outlines under distinct names; never invoke TeX.

PUA slots are internal glyph identifiers, not claims of Unicode equivalence.
The original operators and TeX annotations remain the semantic identities.
"""
from pathlib import Path
import hashlib
import json
import shutil
import tarfile

from fontTools import t1Lib
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
MIKTEX = Path.home() / 'AppData/Local/Programs/MiKTeX'
OUT = ROOT / 'reader/fonts/exact-operators'
GLYPHS = {
    'FISHHOOKRIGHT': ('tx', 74, 'strict', 0xE074, 'દૃઢ શરતી સંબંધ', 'bin'),
    'BOXRIGHT': ('tx', 128, 'squareright', 0xE080, 'પ્રતિહકીકત શરતી સંબંધ', 'bin'),
    'DIAMONDRIGHT': ('tx', 132, 'Diamondright', 0xE084, 'હીરાકાર શરતી સંકેત', 'bin'),
    'LEFTRIGHTARROWEQ': ('stmary', 45, 'leftrightarroweq', 0xE02D, 'બંને દિશાનો સમકક્ષતા સંકેત', 'rel'),
    'VAROLESSTHAN': ('stmary', 52, 'varolessthan', 0xE034, 'બિનપ્રમાણભૂત અંકગણિતનો વર્તુળવાળો ઓછું-હોવાનો સંકેત', 'bin'),
    'REFLECTEDHASH': ('text', 35, 'reflectednumbersign', 0xE123, 'ગડેલ સંખ્યાનો ડાબો પ્રતિબિંબિત હૅશ સંકેત', 'ord'),
    'HASH': ('text', 35, 'numbersign', 0xE023, 'ગડેલ સંખ્યાનો જમણો હૅશ સંકેત', 'ord'),
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def vf_packets(p):
    b = p.read_bytes()
    assert b[:2] == bytes([247, 202])
    i = 3+b[2]+8
    packets, fonts = {}, {}
    while i < len(b):
        op = b[i]; i += 1
        if op <= 241:
            n, c = op, b[i]
            width = int.from_bytes(b[i+1:i+4], 'big')
            i += 4
            packets[c] = (width, b[i:i+n]); i += n
        elif 243 <= op <= 246:
            k = op-242
            number = int.from_bytes(b[i:i+k], 'big'); i += k
            scale = int.from_bytes(b[i+4:i+8], 'big')
            a, n = b[i+12], b[i+13]
            fonts[number] = (scale, b[i+14:i+14+a+n].decode('ascii'))
            i += 14+a+n
        elif op == 248:
            break
        else:
            raise ValueError(f'Unhandled VF opcode {op}; do not infer mapping')
    assert fonts == {0: (1 << 20, 'txsyc')}
    return packets


def build():
    OUT.mkdir(parents=True, exist_ok=True)
    support=OUT/'source';support.mkdir(exist_ok=True)
    def origin(relative):
        retained=support/Path(relative).name
        return retained if retained.is_file() else MIKTEX/relative
    origins = {
        'tx': origin('fonts/type1/public/txfonts/txsyc.pfb'),
        'stmary': origin('fonts/type1/public/hoekwater/stmary10.pfb'),
    }
    vf = origin('fonts/vf/public/newtx/ntxsyc.vf')
    packets = vf_packets(vf)
    records, outputs = [], {}
    for family, source in origins.items():
        original = t1Lib.T1Font(str(source))
        assert original['FontMatrix'] == [0.001, 0, 0, 0.001, 0, 0]
        gs = original.getGlyphSet()
        relevant = [(marker, row) for marker, row in GLYPHS.items() if row[0] == family]
        order = ['.notdef']+[row[2] for _, row in relevant]
        metrics = {'.notdef': (500, 0)}
        chars = {}
        empty = T2CharStringPen(500, None)
        chars['.notdef'] = empty.getCharString()
        for marker, (_, slot, name, cp, label, kind) in relevant:
            assert original['Encoding'][slot] == name
            shift = 0
            if family == 'tx':
                width, packet = packets[slot]
                expected = b'\x95\x7a\xe1'+(bytes([slot]) if slot < 128 else b'\x80'+bytes([slot]))
                assert packet == expected
                shift = int.from_bytes(packet[1:3], 'big', signed=True)/(1 << 20)*1000
                advance = width/(1 << 20)*1000
            else:
                scratch = RecordingPen(); gs[name].draw(scratch)
                advance = gs[name].width
            # OpenType hmtx uses integer font units; outline coordinates retain
            # the VF translation as 16.16 CFF numbers to within 1/65536 unit.
            pen = T2CharStringPen(round(advance), gs, roundTolerance=0)
            gs[name].draw(TransformPen(pen, (1, 0, 0, 1, shift, 0)))
            chars[name] = pen.getCharString()
            bounds = BoundsPen(gs)
            gs[name].draw(TransformPen(bounds, (1, 0, 0, 1, shift, 0)))
            metrics[name] = (round(advance), round(bounds.bounds[0]))
            records.append({'marker': marker, 'family': family, 'source_font': source.name,
                            'source_sha256': sha(source), 'encoding_slot': slot,
                            'glyph_name': name, 'private_use_codepoint': f'U+{cp:04X}',
                            'vf_translation_font_units': shift, 'source_advance_font_units': advance,
                            'otf_advance_font_units': round(advance), 'outline_bounds': bounds.bounds,
                            'math_class': kind, 'accessible_label_gu': label})
        fb = FontBuilder(1000, isTTF=False)
        name = 'GuOLPExactTX' if family == 'tx' else 'GuOLPExactStMary'
        fb.setupGlyphOrder(order)
        fb.setupCharacterMap({row[3]: row[2] for _, row in relevant})
        fb.setupCFF(name, {'FullName': name, 'FamilyName': name, 'Weight': 'Regular'}, chars, {})
        fb.setupHorizontalMetrics(metrics)
        fb.setupHorizontalHeader(ascent=900, descent=-200)
        fb.setupNameTable({'familyName': name, 'styleName': 'Regular', 'uniqueFontIdentifier': name+'-1',
                          'fullName': name, 'psName': name, 'version': 'Version 1.000'})
        fb.setupOS2(sTypoAscender=900, sTypoDescender=-200, usWinAscent=900, usWinDescent=200)
        fb.setupPost(); fb.setupMaxp()
        fb.font['head'].created = fb.font['head'].modified = 3860740800
        target = OUT/(name+'.otf')
        fb.save(target)
        reread = TTFont(target)
        assert reread.getBestCmap() == {row[3]: row[2] for _, row in relevant}
        newgs = reread.getGlyphSet()
        for marker, row in relevant:
            oldpen, newpen = RecordingPen(), RecordingPen()
            rec = next(r for r in records if r['marker'] == marker)
            gs[row[2]].draw(TransformPen(oldpen, (1, 0, 0, 1, rec['vf_translation_font_units'], 0)))
            newgs[row[2]].draw(newpen)
            assert len(oldpen.value) == len(newpen.value), marker
            error = 0
            for (oa, ops), (na, nps) in zip(oldpen.value, newpen.value):
                assert oa == na and len(ops) == len(nps), marker
                for opoint, npoint in zip(ops, nps):
                    error = max(error, *(abs(a-b) for a,b in zip(opoint,npoint)))
            assert error < .001, (marker, error)
            rec['max_outline_coordinate_error_font_units'] = error
        outputs[family] = {'path': str(target.relative_to(ROOT)).replace('\\','/'), 'sha256': sha(target)}
    # The active reader config uses reflected/unreflected tiny text hashes,
    # not corner quotes. Keep the exact Noto outlines and reflect about advance.
    source = ROOT/'fonts/NotoSansGujarati-Regular.ttf'
    original = TTFont(source); gs = original.getGlyphSet()
    assert original['head'].unitsPerEm == 1000
    source_name = original.getBestCmap()[35]
    advance = original['hmtx'][source_name][0]
    relevant = [(marker,row) for marker,row in GLYPHS.items() if row[0]=='text']
    glyphs = {'.notdef':TTGlyphPen(None).glyph()}; metrics={'.notdef':(500,0)}
    transforms={}
    for marker,(_,slot,name,cp,label,kind) in relevant:
        transform=(-1,0,0,1,advance,0) if marker=='REFLECTEDHASH' else (1,0,0,1,0,0)
        transforms[name]=transform
        pen=TTGlyphPen(gs);gs[source_name].draw(TransformPen(pen,transform))
        glyphs[name]=pen.glyph()
        bounds=BoundsPen(gs);gs[source_name].draw(TransformPen(bounds,transform))
        metrics[name]=(advance,round(bounds.bounds[0]))
        records.append({'marker':marker,'family':'text','source_font':source.name,
                        'source_sha256':sha(source),'encoding_slot':slot,'glyph_name':name,
                        'source_glyph_name':source_name,'private_use_codepoint':f'U+{cp:04X}',
                        'outline_transform':transform,'source_advance_font_units':advance,
                        'otf_advance_font_units':advance,'outline_bounds':bounds.bounds,
                        'math_class':kind,'accessible_label_gu':label})
    name='GuOLPExactText';fb=FontBuilder(1000,isTTF=True)
    fb.setupGlyphOrder(list(glyphs));fb.setupCharacterMap({row[3]:row[2] for _,row in relevant})
    fb.setupGlyf(glyphs);fb.setupHorizontalMetrics(metrics)
    fb.setupHorizontalHeader(ascent=900,descent=-200)
    fb.setupNameTable({'familyName':name,'styleName':'Regular','uniqueFontIdentifier':name+'-1',
                      'fullName':name,'psName':name,'version':'Version 1.000'})
    fb.setupOS2(sTypoAscender=900,sTypoDescender=-200,usWinAscent=900,usWinDescent=200)
    fb.setupPost();fb.setupMaxp();fb.font['head'].created=fb.font['head'].modified=3860740800
    target=OUT/(name+'.ttf');fb.save(target);newgs=TTFont(target).getGlyphSet()
    for marker,row in relevant:
        oldpen,newpen=RecordingPen(),RecordingPen()
        gs[source_name].draw(TransformPen(oldpen,transforms[row[2]]));newgs[row[2]].draw(newpen)
        assert oldpen.value==newpen.value,marker
        next(r for r in records if r['marker']==marker)['max_outline_coordinate_error_font_units']=0
    outputs['text']={'path':target.relative_to(ROOT).as_posix(),'sha256':sha(target)}
    # Preserve originals, source and licences for a reproducible source package.
    for p in [*origins.values(), vf, origin('source/txfonts-src.tar.xz'),
              origin('source/stmaryrd-src.tar.bz2'), origin('doc/fonts/txfonts/COPYRIGHT')]:
        if p.resolve()!=(support/p.name).resolve():shutil.copyfile(p, support/p.name)
    for source, name in [(MIKTEX/'doc/latex/mathpazo/gpl.txt','GPL.txt'),
                         (MIKTEX/'doc/latex/xellipsis/lppl.txt','LPPL.txt')]:
        if not (support/name).is_file():shutil.copyfile(source, support/name)
    with tarfile.open(origin('source/stmaryrd-src.tar.bz2')) as archive:
        for member in ['stmaryrd/stmaryrd.dtx', 'stmaryrd/ps-type1/hoekwater/README']:
            (support/Path(member).name).write_bytes(archive.extractfile(member).read())
    receipt = {'schema': 'openlogic-gu-exact-operator-fonts/1', 'glyphs': records, 'outputs': outputs,
               'vf_sha256': sha(vf), 'support': [{'name':p.name,'sha256':sha(p)} for p in sorted(support.iterdir())],
               'scope': 'Exact source encoding and VF packets; outline comparison after OTF serialization. No browser rendering claim. TeX annotations retain the original operators.',
               'status': 'font_outlines_verified_reader_rendering_pending'}
    (ROOT/'build/FULL_EPUB_EXACT_OPERATOR_FONTS.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return receipt


if __name__ == '__main__':
    r = build()
    print(json.dumps({'glyphs':len(r['glyphs']), 'outputs':r['outputs']}))
