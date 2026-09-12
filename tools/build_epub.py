"""Build the deterministic reflowable EPUB 3 completeness checkpoint.

The accepted cumulative HTML is the semantic source.  This exporter preserves
its Gujarati character stream, native MathML, anchors, tables and described SVG
figures while replacing web-only links and metadata with EPUB equivalents.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import zipfile

from lxml import etree, html


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "reader" / "completeness.html"
CSS = ROOT / "reader" / "reader.css"
ASSETS = ROOT / "reader" / "assets"
FONTS = ROOT / "fonts"
OUTPUT = ROOT / "releases" / "OpenLogic-gu-Gujr-IN-Completeness.epub"
REPLAY = ROOT / "build" / "OpenLogic-gu-Gujr-IN-Completeness-replay.epub"
STAGE = ROOT / "build" / "epub013-stage"
REPLAY_STAGE = ROOT / "build" / "epub013-replay-stage"
RECEIPT = ROOT / "build" / "EPUB_BUILD_RECEIPT_013.json"

TITLE = "પૂર્ણતા પ્રમેય સહિત ઓપન લોજિક ગુજરાતી"
LANGUAGE = "gu-IN"
IDENTIFIER = (
    "https://github.com/KokunoYumeto/OpenLogic-gu-Gujr-IN/"
    "releases/tag/completeness-v0.7.0"
)
SOURCE_REVISION = "9620cc73f9c8e0ad003c514a5d3748f29611c4c0"
MODIFIED = "2026-09-10T00:00:00Z"
ZIP_TIME = (2026, 9, 10, 0, 0, 0)

XHTML = "http://www.w3.org/1999/xhtml"
MATHML = "http://www.w3.org/1998/Math/MathML"
EPUB = "http://www.idpf.org/2007/ops"
OPF = "http://www.idpf.org/2007/opf"
DC = "http://purl.org/dc/elements/1.1/"
CONTAINER = "urn:oasis:names:tc:opendocument:xmlns:container"
XML = "http://www.w3.org/XML/1998/namespace"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local_name(value: str) -> str:
    if value.startswith("{"):
        return etree.QName(value).localname
    return value.split(":", 1)[-1]


def clone_xhtml(
    source: etree._Element,
    *,
    in_math: bool = False,
    root: bool = False,
) -> etree._Element:
    name = local_name(str(source.tag))
    math = in_math or name == "math"
    namespace = MATHML if math else XHTML
    nsmap = ({None: XHTML, "epub": EPUB} if root else ({None: MATHML} if name == "math" else None))
    target = etree.Element(f"{{{namespace}}}{name}", nsmap=nsmap)
    for raw_name, value in source.attrib.items():
        name_key = str(raw_name)
        if local_name(name_key) == "xmlns":
            continue
        if name_key == "xml:lang" or name_key == f"{{{XML}}}lang":
            target.set(f"{{{XML}}}lang", value)
        elif name_key == "epub:type" or name_key == f"{{{EPUB}}}type":
            target.set(f"{{{EPUB}}}type", value)
        else:
            target.set(name_key, value)
    target.text = source.text
    target.tail = source.tail
    for child in source:
        if isinstance(child.tag, str):
            target.append(clone_xhtml(child, in_math=math))
    return target


def parse_input() -> html.HtmlElement:
    parser = html.HTMLParser(encoding="utf-8", remove_comments=False, recover=True, huge_tree=True)
    document = html.document_fromstring(INPUT.read_bytes(), parser=parser)
    require(local_name(str(document.tag)) == "html", "missing HTML root")
    return document


def text_without_annotations(element: etree._Element) -> str:
    parts: list[str] = []

    def visit(node: etree._Element) -> None:
        if local_name(str(node.tag)) == "annotation":
            if node.tail:
                parts.append(node.tail)
            return
        if node.text:
            parts.append(node.text)
        for child in node:
            if isinstance(child.tag, str):
                visit(child)
            elif child.tail:
                parts.append(child.tail)
        if node.tail:
            parts.append(node.tail)

    visit(element)
    return " ".join("".join(parts).split())


def serialize(document: etree._Element) -> bytes:
    return etree.tostring(
        document,
        encoding="utf-8",
        xml_declaration=True,
        doctype="<!DOCTYPE html>",
        pretty_print=False,
    )


def make_content(source: html.HtmlElement) -> tuple[bytes, list[tuple[str, str]]]:
    document = clone_xhtml(source, root=True)
    document.set("lang", LANGUAGE)
    document.set(f"{{{XML}}}lang", LANGUAGE)
    document.set("dir", "ltr")

    for meta in document.xpath(
        ".//*[local-name()='meta' and translate(@name,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='viewport']"
    ):
        meta.getparent().remove(meta)
    for link in document.xpath(".//*[local-name()='link']"):
        rel = set((link.get("rel") or "").lower().split())
        if "icon" in rel:
            link.getparent().remove(link)
        elif "stylesheet" in rel:
            link.set("href", "styles/reader.css")
    for anchor in document.xpath(".//*[local-name()='a' and @href='../docs/EDITION_NOTES.md']"):
        anchor.set("href", "about.xhtml")

    toc_nodes = document.xpath(".//*[local-name()='nav' and @id='TOC']")
    require(len(toc_nodes) == 1, "expected one cumulative table of contents")
    toc_nodes[0].set(f"{{{EPUB}}}type", "toc")
    toc_links: list[tuple[str, str]] = []
    for anchor in toc_nodes[0].xpath(".//*[local-name()='a' and starts-with(@href, '#')]"):
        label = text_without_annotations(anchor)
        require(label, "empty table-of-contents label")
        toc_links.append((anchor.get("href") or "", label))
    require(len(toc_links) == 145, f"unexpected navigation-entry count: {len(toc_links)}")
    return serialize(document), toc_links


def xhtml_document(title: str) -> tuple[etree._Element, etree._Element]:
    root = etree.Element(f"{{{XHTML}}}html", nsmap={None: XHTML, "epub": EPUB})
    root.set("lang", LANGUAGE)
    root.set(f"{{{XML}}}lang", LANGUAGE)
    root.set("dir", "ltr")
    head = etree.SubElement(root, f"{{{XHTML}}}head")
    etree.SubElement(head, f"{{{XHTML}}}title").text = title
    link = etree.SubElement(head, f"{{{XHTML}}}link")
    link.set("rel", "stylesheet")
    link.set("href", "styles/reader.css")
    body = etree.SubElement(root, f"{{{XHTML}}}body")
    return root, body


def make_nav(toc_links: list[tuple[str, str]]) -> bytes:
    root, body = xhtml_document("વિષયસૂચિ")
    heading = etree.SubElement(body, f"{{{XHTML}}}h1")
    heading.text = "વિષયસૂચિ"
    nav = etree.SubElement(body, f"{{{XHTML}}}nav")
    nav.set(f"{{{EPUB}}}type", "toc")
    nav.set("role", "doc-toc")
    nav.set("aria-label", "વિષયસૂચિ")
    ordered = etree.SubElement(nav, f"{{{XHTML}}}ol")
    for fragment, label in toc_links:
        item = etree.SubElement(ordered, f"{{{XHTML}}}li")
        anchor = etree.SubElement(item, f"{{{XHTML}}}a")
        anchor.set("href", f"content.xhtml{fragment}")
        anchor.text = label

    landmarks = etree.SubElement(body, f"{{{XHTML}}}nav")
    landmarks.set(f"{{{EPUB}}}type", "landmarks")
    landmarks.set("aria-label", "મુખ્ય સ્થળો")
    listing = etree.SubElement(landmarks, f"{{{XHTML}}}ol")
    for label, href, kind in (
        ("વિષયસૂચિ", "nav.xhtml", "toc"),
        ("ગુજરાતી વાચન", "content.xhtml", "bodymatter"),
        ("આ આવૃત્તિ વિશે", "about.xhtml", "colophon"),
    ):
        item = etree.SubElement(listing, f"{{{XHTML}}}li")
        anchor = etree.SubElement(item, f"{{{XHTML}}}a")
        anchor.set("href", href)
        anchor.set(f"{{{EPUB}}}type", kind)
        anchor.text = label
    return serialize(root)


def make_about() -> bytes:
    root, body = xhtml_document("આ આવૃત્તિ વિશે")
    main = etree.SubElement(body, f"{{{XHTML}}}main")
    main.set(f"{{{EPUB}}}type", "colophon")
    etree.SubElement(main, f"{{{XHTML}}}h1").text = "આ આવૃત્તિ વિશે"
    paragraphs = (
        "આ EPUB એક પ્રવાહી, લિપિઆકાર બદલાય એવું ગુજરાતી વાચન છે. તેમાં ૭૨૨ મૂળ એકમોમાંથી ૧૩૪ એકમો, એટલે OLP-0004થી OLP-0137 સુધીનો સતત આંશિક વિસ્તાર છે. સંપૂર્ણ ૭૨૨-એકમ આવૃત્તિનું કામ ચાલુ છે.",
        "આ સંગ્રહમાં ગણો, સંબંધો, વિધેયો, ગણોનું કદ, અંકગણિતીકરણ, અનંત ગણો, વિધાનાત્મક તર્કશાસ્ત્ર તથા પ્રથમ-ક્રમ તર્કશાસ્ત્રની સાબિતી-પદ્ધતિઓ, સિક્વન્ટ કલન, પ્રાકૃતિક નિગમન, ટેબ્લો, સ્વયંસિદ્ધ નિગમન અને પૂર્ણતા પ્રમેય સમાવિષ્ટ છે.",
        "ગણિત native MathMLમાં છે. તેર આકૃતિઓમાં ગુજરાતી વૈકલ્પિક વર્ણન છે. આંતરિક કડીઓ અને વિષયસૂચિ EPUBમાં જ ચાલે છે. MathMLનું દૃશ્યરૂપ વાંચન-સોફ્ટવેર પ્રમાણે થોડું બદલાઈ શકે છે.",
        "આ યંત્ર દ્વારા કરેલો અનુવાદ છે, જેને મૂળ સાથેના રચનાત્મક અને અર્થલક્ષી સરખામણાં, ગુજરાતી શાસ્ત્રીય સ્રોતોની નોંધ, EPUBCheck અને પ્રતિનિધિ દૃશ્ય તપાસથી ચકાસવામાં આવ્યો છે. સ્વતંત્ર ગુજરાતી નિષ્ણાતનું પ્રમાણપત્ર મળ્યું નથી.",
    )
    for value in paragraphs:
        etree.SubElement(main, f"{{{XHTML}}}p").text = value
    source = etree.SubElement(main, f"{{{XHTML}}}p")
    source.text = "મૂળ સત્તા: Open Logic Project, frozen revision " + SOURCE_REVISION + "."
    rights = etree.SubElement(main, f"{{{XHTML}}}p")
    rights.text = "લખાણ અને અનુવાદ: CC BY 4.0; Noto Sans Gujarati: SIL Open Font License."
    back = etree.SubElement(main, f"{{{XHTML}}}p")
    anchor = etree.SubElement(back, f"{{{XHTML}}}a")
    anchor.set("href", "nav.xhtml")
    anchor.text = "વિષયસૂચિ પર પાછા જાઓ"
    return serialize(root)


def make_package(asset_names: list[str]) -> bytes:
    nsmap = {None: OPF, "dc": DC}
    package = etree.Element(f"{{{OPF}}}package", nsmap=nsmap)
    package.set("version", "3.0")
    package.set("unique-identifier", "pub-id")
    package.set(f"{{{XML}}}lang", LANGUAGE)
    package.set(
        "prefix",
        "schema: http://schema.org/ rendition: http://www.idpf.org/vocab/rendition/#",
    )
    metadata = etree.SubElement(package, f"{{{OPF}}}metadata")

    def dc(name: str, value: str, identifier: str | None = None) -> None:
        element = etree.SubElement(metadata, f"{{{DC}}}{name}")
        if identifier:
            element.set("id", identifier)
        element.text = value

    def meta(prop: str, value: str) -> None:
        element = etree.SubElement(metadata, f"{{{OPF}}}meta")
        element.set("property", prop)
        element.text = value

    dc("identifier", IDENTIFIER, "pub-id")
    dc("title", TITLE, "title")
    dc("language", LANGUAGE)
    dc("creator", "Open Logic Project; Gujarati machine translation")
    dc("source", f"https://github.com/OpenLogicProject/OpenLogic/tree/{SOURCE_REVISION}")
    dc("rights", "CC BY 4.0; bundled Noto Sans Gujarati fonts under SIL OFL 1.1")
    dc("description", "Partial Gujarati cumulative edition: 134 of 722 tracked source units, OLP-0004–0137.")
    meta("dcterms:modified", MODIFIED)
    meta("rendition:layout", "reflowable")
    meta("rendition:orientation", "auto")
    meta("rendition:spread", "auto")
    for value in ("textual", "visual"):
        meta("schema:accessMode", value)
    meta("schema:accessModeSufficient", "textual,visual")
    for value in (
        "MathML",
        "alternativeText",
        "displayTransformability",
        "readingOrder",
        "structuralNavigation",
        "tableOfContents",
    ):
        meta("schema:accessibilityFeature", value)
    meta("schema:accessibilityHazard", "none")
    meta(
        "schema:accessibilitySummary",
        "Reflowable Gujarati text with native MathML, semantic headings, internal navigation, tables, and Gujarati alternative text for all figures. The package is script-free. Reading-system support for MathML varies.",
    )

    manifest = etree.SubElement(package, f"{{{OPF}}}manifest")

    def item(identifier: str, href: str, media: str, properties: str | None = None) -> None:
        element = etree.SubElement(manifest, f"{{{OPF}}}item")
        element.set("id", identifier)
        element.set("href", href)
        element.set("media-type", media)
        if properties:
            element.set("properties", properties)

    item("nav", "nav.xhtml", "application/xhtml+xml", "nav")
    item("content", "content.xhtml", "application/xhtml+xml", "mathml")
    item("about", "about.xhtml", "application/xhtml+xml")
    item("css", "styles/reader.css", "text/css")
    item("font-regular", "fonts/NotoSansGujarati-Regular.ttf", "font/ttf")
    item("font-bold", "fonts/NotoSansGujarati-Bold.ttf", "font/ttf")
    for index, name in enumerate(asset_names, 1):
        item(f"image-{index:02}", f"assets/{name}", "image/svg+xml")

    spine = etree.SubElement(package, f"{{{OPF}}}spine")
    for identifier, linear in (("nav", "no"), ("content", "yes"), ("about", "yes")):
        ref = etree.SubElement(spine, f"{{{OPF}}}itemref")
        ref.set("idref", identifier)
        ref.set("linear", linear)
    return etree.tostring(package, encoding="utf-8", xml_declaration=True, pretty_print=True)


def make_container() -> bytes:
    container = etree.Element(f"{{{CONTAINER}}}container", nsmap={None: CONTAINER})
    container.set("version", "1.0")
    rootfiles = etree.SubElement(container, f"{{{CONTAINER}}}rootfiles")
    rootfile = etree.SubElement(rootfiles, f"{{{CONTAINER}}}rootfile")
    rootfile.set("full-path", "OEBPS/package.opf")
    rootfile.set("media-type", "application/oebps-package+xml")
    return etree.tostring(container, encoding="utf-8", xml_declaration=True, pretty_print=True)


def safe_clear(stage: Path) -> None:
    resolved = stage.resolve()
    allowed = {STAGE.resolve(), REPLAY_STAGE.resolve()}
    require(resolved in allowed and resolved.parent == (ROOT / "build").resolve(), "unsafe stage")
    if resolved.exists():
        shutil.rmtree(resolved)
    resolved.mkdir(parents=True)


def stage_book(stage: Path) -> dict[str, object]:
    safe_clear(stage)
    (stage / "META-INF").mkdir()
    (stage / "OEBPS" / "styles").mkdir(parents=True)
    (stage / "OEBPS" / "fonts").mkdir()
    (stage / "OEBPS" / "assets").mkdir()
    (stage / "mimetype").write_bytes(b"application/epub+zip")
    (stage / "META-INF" / "container.xml").write_bytes(make_container())

    source = parse_input()
    content, toc_links = make_content(source)
    (stage / "OEBPS" / "content.xhtml").write_bytes(content)
    (stage / "OEBPS" / "nav.xhtml").write_bytes(make_nav(toc_links))
    (stage / "OEBPS" / "about.xhtml").write_bytes(make_about())
    shutil.copyfile(CSS, stage / "OEBPS" / "styles" / "reader.css")
    for name in ("NotoSansGujarati-Regular.ttf", "NotoSansGujarati-Bold.ttf"):
        shutil.copyfile(FONTS / name, stage / "OEBPS" / "fonts" / name)
    asset_names = sorted(path.name for path in ASSETS.glob("*.svg"))
    require(len(asset_names) == 13, "expected thirteen described diagrams")
    for name in asset_names:
        shutil.copyfile(ASSETS / name, stage / "OEBPS" / "assets" / name)
    (stage / "OEBPS" / "package.opf").write_bytes(make_package(asset_names))
    return {"toc_links": len(toc_links), "assets": asset_names}


def zip_book(stage: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", allowZip64=True) as archive:
        mimetype = zipfile.ZipInfo("mimetype", ZIP_TIME)
        mimetype.compress_type = zipfile.ZIP_STORED
        mimetype.external_attr = 0o100644 << 16
        archive.writestr(mimetype, (stage / "mimetype").read_bytes())
        for path in sorted(stage.rglob("*")):
            if not path.is_file() or path.name == "mimetype":
                continue
            relative = path.relative_to(stage).as_posix()
            info = zipfile.ZipInfo(relative, ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def archive_inventory(path: Path) -> list[dict[str, object]]:
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        require(infos[0].filename == "mimetype", "mimetype is not first")
        require(infos[0].compress_type == zipfile.ZIP_STORED, "mimetype is compressed")
        require(archive.read("mimetype") == b"application/epub+zip", "wrong mimetype")
        require([row.filename for row in infos[1:]] == sorted(row.filename for row in infos[1:]), "archive order drift")
        return [
            {
                "path": row.filename,
                "bytes": len(archive.read(row.filename)),
                "sha256": hashlib.sha256(archive.read(row.filename)).hexdigest(),
                "compression": "stored" if row.compress_type == zipfile.ZIP_STORED else "deflated",
            }
            for row in infos
        ]


def main() -> None:
    require(INPUT.is_file() and CSS.is_file(), "missing accepted semantic reader")
    canonical_details = stage_book(STAGE)
    zip_book(STAGE, OUTPUT)
    replay_details = stage_book(REPLAY_STAGE)
    zip_book(REPLAY_STAGE, REPLAY)
    require(OUTPUT.read_bytes() == REPLAY.read_bytes(), "cold replay differs")
    require(canonical_details == replay_details, "stage discovery differs")
    inventory = archive_inventory(OUTPUT)
    receipt = {
        "schema": "openlogic-gu-epub-build/1",
        "source_revision": SOURCE_REVISION,
        "source": {
            "path": "reader/completeness.html",
            "bytes": INPUT.stat().st_size,
            "sha256": sha(INPUT),
        },
        "epub": {
            "path": OUTPUT.relative_to(ROOT).as_posix(),
            "bytes": OUTPUT.stat().st_size,
            "sha256": sha(OUTPUT),
            "format": "EPUB 3 reflowable",
            "language": LANGUAGE,
            "coverage": "134/722 units; OLP-0004–0137",
            "complete_edition": False,
        },
        "cold_replay": {
            "path": REPLAY.relative_to(ROOT).as_posix(),
            "bytes": REPLAY.stat().st_size,
            "sha256": sha(REPLAY),
            "byte_identical": True,
        },
        "navigation_links": canonical_details["toc_links"],
        "described_svg_figures": len(canonical_details["assets"]),
        "archive_entries": len(inventory),
        "archive_inventory": inventory,
        "status": "built_reproducibly_pending_epubcheck_and_runtime_qa",
    }
    RECEIPT.write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(json.dumps(receipt["epub"], ensure_ascii=False))


if __name__ == "__main__":
    main()
