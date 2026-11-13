"""Package the cumulative reader and its editable build inputs.

Membership is explicit. Private task state, review ledgers, old editions,
rendering caches and administrative documents are outside this distribution.
"""
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
VERSION = 'full-edition-v1.1.0'
OUT = ROOT/'releases'/VERSION
BUILD = ROOT/'build/full-reader-public-20261105'
JOB = 'gu-full-reader-public-20261105'
NAMES = ['01-OpenLogic-gu-Gujr-IN-Full.pdf',
         '02-OpenLogic-gu-Gujr-IN-Full-Text.tex',
         '03-OpenLogic-gu-Gujr-IN-Full-Source.zip',
         '04-OpenLogic-gu-Gujr-IN-Source-Index.html',
         '05-OpenLogic-gu-Gujr-IN-Edition-Source.json',
         '06-OpenLogic-gu-Gujr-IN-Full.epub']
TOOLS = ['build_full_reader_guarded.ps1','prepare_full_epub_html.py',
         'build_full_epub.py','audit_full_epub_figures.py','epub_utils.py',
         'epub_base_macros.py','full_epub_source_macros.py','full_reader_aux.py',
         'render_turing_graphs.py','render_relation_graphs.py',
         'render_native_epub_figures.py','build_exact_operator_fonts.py',
         'edition_metadata.py','package_reader_edition.py']
FILES = ['LICENSE.md','README.md','CITATION.cff','SOURCE_PROVENANCE.json',
         'docs/BUILD_FULL_READER.gu.md','docs/LICENSE_NOTES.md',
         'docs/EDITION_HISTORY.gu.md','reader/full-reader.tex',
         'reader/full-reader-resolved-body.tex','reader/full-reader-config.sty',
         'reader/gu-reader-layout.tex','reader/full-reader.bbl',
         'reader/full-source-index.html','upstream/LICENSE.md','upstream/README.md',
         'upstream/open-logic-config.sty','upstream/open-logic-envs.sty',
         'upstream/open-logic-locale.sty','upstream/open-logic-complete-config.sty']
DIRECTORIES = ['gu/content','upstream/content','upstream/sty','upstream/include','upstream/bib',
               'upstream/assets/diagrams','upstream/assets/photos','fonts',
               'reader/assets','reader/figures/native','reader/fonts/exact-operators']
GENERATED_SUFFIXES = {'.aux','.fls','.fdb_latexmk','.log','.out','.pcr','.pyc','.pyo','.synctex','.toc'}


def load(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')


def members():
    result={}
    def add(path):
        assert path.is_file() and path.resolve().is_relative_to(ROOT.resolve())
        name=path.relative_to(ROOT).as_posix()
        assert not any(part in ('.git','__pycache__') for part in path.parts)
        assert path.suffix.lower() not in GENERATED_SUFFIXES
        result[name]=path
    for name in FILES:
        add(ROOT/name)
    for name in TOOLS:
        add(ROOT/'tools'/name)
    for name in DIRECTORIES:
        for path in sorted((ROOT/name).rglob('*')):
            if path.is_file() and not any(part in ('.git','__pycache__') for part in path.parts) and path.suffix.lower() not in GENERATED_SUFFIXES:
                add(path)
    assert sum(name.startswith('gu/content/') and name.endswith('.tex') for name in result)==722
    assert sum(name.startswith('upstream/content/') and name.endswith('.tex') for name in result)==722
    return result


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    provenance=load(ROOT/'SOURCE_PROVENANCE.json')
    assert len(provenance['units'])==722
    for row in provenance['units']:
        assert digest(ROOT/'upstream'/row['path'])==row['english_sha256'],row['id']
        assert digest(ROOT/'gu'/row['path'])==row['gujarati_sha256'],row['id']
    reader=ROOT/'reader/full-reader.tex';body=ROOT/'reader/full-reader-resolved-body.tex'
    assert digest(body)=='0e9dc34d708e74ab6eb9eae02f1ba094b5e895adfe4e73db75b6c3b13b18041d', 'The cumulative mathematical baseline changed; compare it explicitly.'
    build=load(BUILD/'FULL_READER_BUILD.json')
    assert build['input']['sha256']==digest(reader)
    assert build['status']=='three_lualatex_passes_succeeded_visual_QA_pending'
    assert not build['missing_characters'] and not build['undefined_references'] and not build['tex_errors']
    pdf=BUILD/(JOB+'.pdf');assert digest(pdf)==build['pdf']['sha256']
    epub_build=load(ROOT/'build/FULL_EPUB_BUILD.json')
    assert epub_build['source_reader_sha256']==digest(reader)
    epub=ROOT/epub_build['epub_path'];assert digest(epub)==epub_build['epub_sha256']
    assert epub_build['unit_anchors']==722 and epub_build['mathml_formulas']==40892
    shutil.copyfile(pdf,OUT/NAMES[0]);shutil.copyfile(reader,OUT/NAMES[1]);shutil.copyfile(epub,OUT/NAMES[5])
    index=(ROOT/'reader/full-source-index.html').read_text(encoding='utf-8')
    url='https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/blob/'+VERSION+'/'
    index=re.sub(r'href="\.\./(gu|upstream)/',lambda m:'href="'+url+m[1]+'/',index)
    (OUT/NAMES[3]).write_text(index,encoding='utf-8',newline='\n')
    edition={'schema':'openlogic-gu-edition-source/1','title':'ઓપન લોજિક — ગુજરાતી',
             'original_author':'Open Logic Project','source_url':provenance['source_url'],
             'source_revision':provenance['source_revision'],'photo_source_revision':provenance['photo_source_revision'],
             'language':'gu-Gujr-IN','source_units':722,'edition':'corrected Gujarati AI-translated edition',
             'ai_production':'OpenAI Codex GPT-5.6 Sol, GPT-6 Sol and GPT-6.1 Sol; Ultra effort',
             'text_licence':'CC BY 4.0; separate photograph, image and font terms apply',
             'source_provenance':'SOURCE_PROVENANCE.json','component_notices':'docs/LICENSE_NOTES.md'}
    save(OUT/NAMES[4],edition)
    text=body.read_text(encoding='utf-8')
    begins={m[1]:m.start() for m in re.finditer(r'(?m)^% BEGIN (OLP-\d{4})\s*$',text)}
    ends={m[1]:m.end() for m in re.finditer(r'(?m)^% END (OLP-\d{4})\s*$',text)}
    assert len(begins)==len(ends)==722
    # Source part drivers distinguish primary full parts from local variants.
    primary=['OLP-0003','OLP-0055','OLP-0138','OLP-0182','OLP-0208',
             'OLP-0252','OLP-0274','OLP-0322','OLP-0341','OLP-0685',
             'OLP-0383','OLP-0407','OLP-0475','OLP-0491','OLP-0516',
             'OLP-0529','OLP-0601','OLP-0620','OLP-0640']
    parts=[]
    for number,uid in enumerate(primary,10):
        name=f'{number:02d}-OpenLogic-gu-Gujr-IN-{uid}-Part-Text.tex'
        part=text[begins[uid]:ends[uid]].rstrip()+'\n'
        prefix='% ભાગનો સંપાદનીય પાઠ. સંપૂર્ણ પ્રોજેક્ટની શૈલી અને સંદર્ભ સાથે વાપરો; મુખ્ય દસ્તાવેજ reader/full-reader.tex છે.\n\n'
        (OUT/name).write_text(prefix+part,encoding='utf-8',newline='\n');parts.append(name)
    selected=members()
    for name in [NAMES[1],NAMES[4]]+parts:
        path=OUT/name;selected[path.relative_to(ROOT).as_posix()]=path
    private_terms = ['interlanguage-'+'task-state', 'BEGIN '+'PRIVATE',
                     '<'+'codex_internal_context', 'User set '+'goal status',
                     'source='+'"goal"']
    forbidden=re.compile(r'(?i)C:[/\\]+Users[/\\]+|'+'|'.join(re.escape(term) for term in private_terms))
    for name,path in selected.items():
        assert not name.startswith(('provenance/','work/','build/','tmp/'))
        if path.suffix.lower() in ('.py','.ps1','.md','.txt','.tex','.json','.jsonl','.html','.cff'):
            content=path.read_text(encoding='utf-8-sig',errors='replace')
            assert not forbidden.search(content),'Private administrative content in '+name
    inventory={'schema':'openlogic-gu-editable-source-inventory/1','edition':VERSION,
               'source_revision':provenance['source_revision'],
               'files':[{'path':name,'bytes':path.stat().st_size,'sha256':digest(path)} for name,path in sorted(selected.items())]}
    manifest=(json.dumps(inventory,ensure_ascii=False,indent=2)+'\n').encode('utf-8')
    with ZipFile(OUT/NAMES[2],'w') as archive:
        for name,path in sorted(selected.items()):
            info=ZipInfo(name,(2026,11,5,0,0,0));info.external_attr=0o100644<<16
            archive.writestr(info,path.read_bytes(),compress_type=ZIP_DEFLATED,compresslevel=9)
        info=ZipInfo('SOURCE_INVENTORY.json',(2026,11,5,0,0,0));info.external_attr=0o100644<<16
        archive.writestr(info,manifest,compress_type=ZIP_DEFLATED,compresslevel=9)
    with ZipFile(OUT/NAMES[2]) as archive:
        assert set(archive.namelist())==set(selected)|{'SOURCE_INVENTORY.json'}
        for row in inventory['files']:
            data=archive.read(row['path']);assert len(data)==row['bytes'] and sha256(data).hexdigest()==row['sha256']
        assert archive.read('reader/full-reader.tex')==(OUT/NAMES[1]).read_bytes()
    names=NAMES+parts
    (OUT/'99-SHA256SUMS-Full.txt').write_text(''.join(digest(OUT/name)+'  '+name+'\n' for name in names),encoding='utf-8',newline='\n')
    names=names+['99-SHA256SUMS-Full.txt']
    receipt={'schema':'openlogic-gu-reader-edition-local-package/1','version':VERSION,'source_units':722,
             'reader_sha256':digest(reader),'pdf_sha256':digest(pdf),'epub_sha256':digest(epub),
             'source_inventory_sha256':sha256(manifest).hexdigest(),'source_inventory_entries':len(selected),
             'archive_entries':len(selected)+1,'preview_file':NAMES[0],'ordered_files':names,
             'artifacts':[{'filename':name,'path':(OUT/name).relative_to(ROOT).as_posix(),'bytes':(OUT/name).stat().st_size,'sha256':digest(OUT/name)} for name in names],
             'status':'local_candidate_requires_final_private_qa_and_authorized_publication'}
    save(ROOT/'build/PUBLIC_READER_PACKAGE.json',receipt)
    print(json.dumps({key:receipt[key] for key in ['source_units','source_inventory_entries','pdf_sha256','epub_sha256','status']}))


if __name__=='__main__':
    main()
