"""Package the complete corrected draft with chapter files and local resources.

Validate the generated archive against its editable sources and EPUBCheck.
No historical EPUB or public release is overwritten by this draft builder.
"""
from pathlib import Path
from urllib.parse import unquote
import hashlib
import json
import re
import zipfile
from lxml import etree, html
from epub_utils import clone_xhtml, text_without_annotations, make_container
from edition_metadata import AI_NOTICE, EDITORIAL_NOTICE, DESCRIPTION

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT/'build/full-epub-draft.html'
OUTPUT = ROOT/'build/OpenLogic-gu-Gujr-IN-Full-draft.epub'
XHTML='http://www.w3.org/1999/xhtml'
OPF='http://www.idpf.org/2007/opf'
DC='http://purl.org/dc/elements/1.1/'
EPUB='http://www.idpf.org/2007/ops'
XML='http://www.w3.org/XML/1998/namespace'
LANG='gu-Gujr-IN'
REVISION='1e960beff9ed7835bf3e3f1335e21af3439cd107'
TITLE='ઓપન લોજિક — ગુજરાતી આવૃત્તિ'
ZIP_TIME=(2026,11,12,0,0,0)
ALT={
 'union.svg':'બે ગણોના યોગગણમાં બંને પ્રદેશો સમાવાય છે.',
 'intersection.svg':'બે ગણોના છેદગણમાં સામાન્ય પ્રદેશ સમાવાય છે.',
 'difference.svg':'ગણના તફાવતમાં પહેલા ગણનો બીજાની બહારનો પ્રદેશ સમાવાય છે.',
 'function.svg':'બે ગણો વચ્ચે ફલનનો આલેખ: દરેક ઇનપુટનું એક જ આઉટપુટ છે.',
 'surjective.svg':'વ્યાપ્ત ફલનનો આલેખ: સહપ્રદેશના દરેક ઘટકને કોઈ ઇનપુટ મળે છે.',
 'injective.svg':'એક-એક ફલનનો આલેખ: જુદા ઇનપુટના આઉટપુટ જુદા છે.',
 'bijective.svg':'એક-એક અને વ્યાપ્ત ફલનનો આલેખ.',
 'composition.svg':'બે ફલનોના સંયોજનનો આલેખ.',
 'turing-machine.svg':'ટ્યુરિંગ મશીનની પટ્ટી, વાંચન-લેખન મથાળું અને નિયંત્રણનો આલેખ.',
}

def sha(value):return hashlib.sha256(value).hexdigest()

def document(title):
 root=etree.Element('{'+XHTML+'}html',nsmap={None:XHTML,'epub':EPUB})
 root.set('lang',LANG);root.set('{'+XML+'}lang',LANG);root.set('dir','ltr')
 head=etree.SubElement(root,'{'+XHTML+'}head')
 etree.SubElement(head,'{'+XHTML+'}title').text=title
 etree.SubElement(head,'{'+XHTML+'}link',rel='stylesheet',href='styles/reader.css')
 body=etree.SubElement(root,'{'+XHTML+'}body')
 return root,body

def serialize(root):
 return etree.tostring(root,encoding='utf-8',xml_declaration=True,doctype='<!DOCTYPE html>')

def local_name(element):return etree.QName(element).localname

def main():
 source_bytes=INPUT.read_bytes();source_sha=sha((ROOT/'reader/full-reader.tex').read_bytes())
 qa=json.loads((ROOT/'build/FULL_EPUB_HTML_QA.json').read_text(encoding='utf-8-sig'))
 assert qa['accepted_source_sha256']==source_sha
 for name in ['tex_math_fallback_nodes','source_tikz_diagrams','internal_operator_markers_remaining','internal_smallcaps_markers_remaining','internal_math_link_markers_remaining','internal_equation_label_markers_remaining','internal_table_markers_remaining']:
  assert qa[name]==0,(name,qa[name])
 assert not qa['broken_fragment_links'] and not qa['html_duplicate_ids']
 coverage=json.loads((ROOT/'build/FULL_EPUB_FIGURE_COVERAGE.json').read_text(encoding='utf-8-sig'))
 assert coverage['current_source_sha256']==source_sha and coverage['count']==coverage['bound_svg_count']==61
 parser=html.HTMLParser(encoding='utf-8',huge_tree=True)
 source=html.document_fromstring(source_bytes,parser=parser)
 assert not source.xpath('.//script') and not source.xpath('.//svg')
 body=source.find('body');nav=body.find("nav[@id='TOC']")
 assert nav is not None;body.remove(nav)
 expected_text=text_without_annotations(body)
 expected_gu=re.findall('[\u0a80-\u0aff]',expected_text)
 expected_math=len(body.xpath('.//math'))
 files={'META-INF/container.xml':make_container()}
 resources={};resource_sources=[];id_owner={}
 chunks=[];current=[]
 for child in body:
  if not isinstance(child.tag,str):continue
  boundary=child.tag in ['h1','h2'] or 'footnotes' in child.get('class','').split()
  if boundary and current:chunks.append(current);current=[]
  current.append(child)
 if current:chunks.append(current)
 docs=[]
 for i,children in enumerate(chunks,1):
  headings=[c for c in children if c.tag in ['h1','h2']]
  title=text_without_annotations(headings[0]) if headings else ('વાચન' if i==1 else 'નોંધો')
  name=f'chapter-{i:03}.xhtml';root,target=document(title)
  for child in children:target.append(clone_xhtml(child))
  for element in root.xpath('.//*[@id]'):
   ident=element.get('id');assert ident not in id_owner,ident;id_owner[ident]=name
  docs.append((name,root,target))
 navroot,navbody=document('વિષયસૂચિ');toc=clone_xhtml(nav)
 toc.set('{'+EPUB+'}type','toc');navbody.append(toc)
 for e in toc.xpath('.//*[local-name()="ul"]'):
  e.tag='{'+XHTML+'}ol'
 for e in toc.xpath('.//*[@id]')+[toc]:
  if e.get('id'):id_owner[e.get('id')]='nav.xhtml'
 assert len([key for key in id_owner if re.fullmatch(r'guunit:OLP-\d{4}',key)])==722

 def resource(src):
  if src in resources:return resources[src]
  raw=unquote(src)
  if raw.startswith('assets/'):path=ROOT/'reader'/raw
  elif raw.startswith(('build/','upstream/')):path=ROOT/raw
  else:raise AssertionError(('Unregistered resource',src))
  path=path.resolve();assert path.is_relative_to(ROOT.resolve()) and path.is_file(),src
  data=path.read_bytes();ext=path.suffix.lower()
  media={'.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg'}[ext]
  href='assets/'+sha(data)[:12]+'-'+path.name
  files['OEBPS/'+href]=data;resources[src]=href
  resource_sources.append({'source_path':path.relative_to(ROOT).as_posix(),'href':href,'sha256':sha(data),'media_type':media})
  return href

 def transform(root):
  for image in root.xpath('.//*[local-name()="img"]'):
   src=image.get('src');image.set('src',resource(src))
   if not image.get('alt'):
    ancestors=image.xpath('ancestor::*[local-name()="figure"]')
    captions=ancestors[-1].xpath('.//*[local-name()="figcaption"]') if ancestors else []
    caption=text_without_annotations(captions[0]) if captions else ''
    assert caption or Path(src).name in ALT,('Missing image description',src)
    image.set('alt',caption or ALT[Path(src).name])
  for e in root.xpath('.//*[@href]'):
   href=e.get('href')
   if href.startswith('#'):
    ident=unquote(href[1:]);assert ident in id_owner,href
    e.set('href',id_owner[ident]+'#'+ident)
   elif href.startswith(('http:','https:','mailto:')) or e.tag=='{'+XHTML+'}link':pass
   else:raise AssertionError(('Unregistered local link',href))
   if e.get('role')=='doc-noteref':e.set('{'+EPUB+'}type','noteref')
  for e in root.xpath('.//*[@id]'):
   if re.fullmatch(r'fn\d+',e.get('id','')):e.set('{'+EPUB+'}type','footnote')

 for name,root,target in docs:transform(root);files['OEBPS/'+name]=serialize(root)
 transform(navroot);files['OEBPS/nav.xhtml']=serialize(navroot)
 text=' '.join(text_without_annotations(target) for _,_,target in docs)
 assert expected_text==' '.join(text.split()),'Visible character stream drift'
 assert expected_gu==re.findall('[\u0a80-\u0aff]',text),'Gujarati character sequence drift'
 assert sum(len(root.xpath('.//*[local-name()="math"]')) for _,root,_ in docs)==expected_math
 styles='\n'.join(source.xpath('.//style/text()'))
 for family,ext in [('GuOLPExactTX','otf'),('GuOLPExactStMary','otf'),('GuOLPExactText','ttf')]:
  name=family+'.'+ext
  styles=styles.replace('../reader/fonts/exact-operators/'+name,'../fonts/'+name)
  files['OEBPS/fonts/'+name]=(ROOT/'reader/fonts/exact-operators'/name).read_bytes()
 for kind in ['Regular','Bold']:
  name='NotoSansGujarati-'+kind+'.ttf';files['OEBPS/fonts/'+name]=(ROOT/'fonts'/name).read_bytes()
 styles+='''
@font-face{font-family:GuBook;src:url('../fonts/NotoSansGujarati-Regular.ttf');font-weight:400;}
@font-face{font-family:GuBook;src:url('../fonts/NotoSansGujarati-Bold.ttf');font-weight:700;}
body{font-family:GuBook,serif;max-width:none;padding:.7em;margin:0;}
img{max-width:100%;height:auto;} .math.display{display:block;overflow-x:auto;max-width:100%;}
nav ol{list-style-type:none;}
math{font-family:'STIX Two Math','Cambria Math',serif;} mtext{font-family:GuBook,serif;}
'''
 files['OEBPS/styles/reader.css']=styles.encode('utf-8')
 about,abody=document('આ આવૃત્તિ વિશે');etree.SubElement(abody,'{'+XHTML+'}h1').text='આ આવૃત્તિ વિશે'
 assert len(re.findall(r'(?m)^% BEGIN OLP-\d{4}$', (ROOT/'reader/full-reader.tex').read_text(encoding='utf-8'))) == 722
 for paragraph in [
  'આ પ્રવાહી ગુજરાતી આવૃત્તિમાં સ્થિર અંગ્રેજી મૂળના બધા ૭૨૨ સ્રોત એકમો છે. વિષયસૂચિ, સૂત્રો અને સંદર્ભોની કડીઓ પુસ્તકની અંદર છે.',
  AI_NOTICE,
  EDITORIAL_NOTICE,
  'મૂળ લખાણ Open Logic Projectનું છે. લખાણ અને તેનો ગુજરાતી અનુવાદ CC BY 4.0 હેઠળ છે. ફોટોગ્રાફ, ચિત્રો અને ફોન્ટની અલગ મૂળ શરતો તથા શ્રેય પુસ્તકમાં જાળવેલાં છે.'
 ]:etree.SubElement(abody,'{'+XHTML+'}p').text=paragraph
 p=etree.SubElement(abody,'{'+XHTML+'}p');etree.SubElement(p,'{'+XHTML+'}a',href='https://github.com/OpenLogicProject/OpenLogic/tree/'+REVISION).text='ઓપન લોજિક પ્રોજેક્ટનો મૂળ સ્રોત'
 p=etree.SubElement(abody,'{'+XHTML+'}p');etree.SubElement(p,'{'+XHTML+'}a',href='licenses.xhtml').text='ફોન્ટની લાઇસન્સ-શરતો'
 p=etree.SubElement(abody,'{'+XHTML+'}p');etree.SubElement(p,'{'+XHTML+'}a',href='nav.xhtml').text='વિષયસૂચિ પર પાછા જાઓ'
 files['OEBPS/about.xhtml']=serialize(about)
 license_root,lbody=document('ફોન્ટની લાઇસન્સ-શરતો')
 for path in [ROOT/'fonts/OFL.txt']+[ROOT/'reader/fonts/exact-operators/source'/n for n in ['COPYRIGHT','GPL.txt','LPPL.txt','README']]:
  etree.SubElement(lbody,'{'+XHTML+'}h2').text=path.name
  license_text=path.read_text(encoding='utf-8',errors='strict')
  if '\x1a' in license_text:
   assert license_text.endswith('\x1a') and license_text.count('\x1a')==1
   license_text=license_text[:-1]  # Terminal DOS EOF is not licence content.
  assert all(c=='\f' for c in license_text if ord(c)<32 and c not in '\n\r\t')
  # GPL print-page form feeds cannot occur in XML. Preserve all words and
  # render those page boundaries as blank lines; originals remain in source.
  etree.SubElement(lbody,'{'+XHTML+'}pre').text=license_text.replace('\f','\n\n')
 files['OEBPS/licenses.xhtml']=serialize(license_root)
 package=etree.Element('{'+OPF+'}package',nsmap={None:OPF,'dc':DC},version='3.0')
 package.set('unique-identifier','publication-id');package.set('{'+XML+'}lang',LANG)
 package.set('prefix','rendition: http://www.idpf.org/vocab/rendition/#')
 metadata=etree.SubElement(package,'{'+OPF+'}metadata')
 for name,value in [('identifier','urn:sha256:'+source_sha),('title',TITLE),('language',LANG),('creator','Open Logic Project'),('source','https://github.com/OpenLogicProject/OpenLogic/tree/'+REVISION),('description',DESCRIPTION),('rights','લખાણ અને તેનો ગુજરાતી અનુવાદ CC BY 4.0 હેઠળ છે. ફોટોગ્રાફ, ચિત્રો અને ફોન્ટ માટે તેમના મૂળ પરવાના અને ઉપયોગ-શરતો લાગુ પડે છે.')]:
  e=etree.SubElement(metadata,'{'+DC+'}'+name);e.text=value
  if name=='identifier':e.set('id','publication-id')
 for prop,value in [('dcterms:modified','2026-11-12T15:54:48Z'),('rendition:layout','reflowable')]:etree.SubElement(metadata,'{'+OPF+'}meta',property=prop).text=value
 manifest=etree.SubElement(package,'{'+OPF+'}manifest');href_ids={}
 for i,path in enumerate(sorted(p for p in files if p.startswith('OEBPS/')),1):
  href=path[6:];ext=Path(path).suffix.lower();media={'.xhtml':'application/xhtml+xml','.css':'text/css','.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.ttf':'font/ttf','.otf':'font/otf'}[ext]
  ident='item-'+str(i);href_ids[href]=ident;e=etree.SubElement(manifest,'{'+OPF+'}item',id=ident,href=href);e.set('media-type',media)
  props=[]
  if href=='nav.xhtml':props.append('nav')
  if ext=='.xhtml':
   parsed_item=etree.fromstring(files[path],parser=etree.XMLParser(huge_tree=True))
   if parsed_item.xpath('boolean(.//m:math)',namespaces={'m':'http://www.w3.org/1998/Math/MathML'}):props.append('mathml')
  if props:e.set('properties',' '.join(props))
 spine=etree.SubElement(package,'{'+OPF+'}spine')
 for name in ['nav.xhtml']+[name for name,_,_ in docs]+['about.xhtml','licenses.xhtml']:
  etree.SubElement(spine,'{'+OPF+'}itemref',idref=href_ids[name],linear='no' if name in ['nav.xhtml','licenses.xhtml'] else 'yes')
 files['OEBPS/package.opf']=etree.tostring(package,encoding='utf-8',xml_declaration=True)
 stage=ROOT/'build'/('full-epub-stage-'+source_sha[:12]);stage.mkdir(exist_ok=True)
 for path,data in files.items():
  target=stage/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
 def archive():
  with zipfile.ZipFile(OUTPUT,'w') as z:
   e=zipfile.ZipInfo('mimetype',ZIP_TIME);e.compress_type=zipfile.ZIP_STORED;z.writestr(e,b'application/epub+zip')
   for path,data in sorted(files.items()):
    e=zipfile.ZipInfo(path,ZIP_TIME);e.compress_type=zipfile.ZIP_DEFLATED;e.external_attr=0o100644<<16
    z.writestr(e,data,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
 archive();first_sha=sha(OUTPUT.read_bytes());archive();assert sha(OUTPUT.read_bytes())==first_sha
 with zipfile.ZipFile(OUTPUT) as z:
  assert z.infolist()[0].filename=='mimetype' and z.infolist()[0].compress_type==zipfile.ZIP_STORED
  assert set(z.namelist())==set(files)|{'mimetype'}
  parsed={p:etree.fromstring(z.read(p),parser=etree.XMLParser(huge_tree=True)) for p in files if p.endswith('.xhtml')}
  ids={p:{e.get('id') for e in root.xpath('.//*[@id]')} for p,root in parsed.items()}
  for path,root in parsed.items():
   for e in root.xpath('.//*[@src or @href]'):
    value=e.get('src') or e.get('href')
    if value.startswith(('http:','https:','mailto:')):continue
    name,_,fragment=value.partition('#');target='OEBPS/'+name
    if name.startswith('styles/') or name.startswith('assets/') or name.endswith('.xhtml'):assert target in files,(path,value)
    else:raise AssertionError((path,value))
    if fragment:
     assert unquote(fragment) in ids[target],(path,value)
 receipt={'schema':'openlogic-gu-full-epub-draft-build/1','source_reader_sha256':source_sha,'reference_auxiliary':qa['reference_auxiliary'],'html_sha256':sha(source_bytes),'epub_path':OUTPUT.relative_to(ROOT).as_posix(),'epub_sha256':first_sha,'epub_bytes':OUTPUT.stat().st_size,'chapter_documents':len(docs),'unit_anchors':722,'mathml_formulas':expected_math,'visible_character_stream_exact':True,'gujarati_character_sequence_exact':True,'repeated_archive_byte_identical':True,'assets':resource_sources,'stage':stage.relative_to(ROOT).as_posix(),'status':'full_source_epub_built_pending_validation'}
 (ROOT/'build/FULL_EPUB_BUILD.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print({key:receipt[key] for key in ['epub_path','epub_bytes','chapter_documents','unit_anchors','mathml_formulas','status']})

if __name__=='__main__':main()
