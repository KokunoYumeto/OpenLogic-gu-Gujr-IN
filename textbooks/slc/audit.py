"""Compare SLC outlines and find possible English in the rendered Gujarati book."""

import argparse
from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import unicodedata
from xml.etree import ElementTree

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parent
CHAPTER = re.compile(r"^(\d{1,2}|[A-D])\s+(\D.+)$")
ENGLISH_WORDS = frozenset(
    "the this these those each every which what where whenever unless therefore "
    "with without from into between both their its some then cannot whether "
    "other such however suppose assume follows since must under above below "
    "there are is of by for and iff or entails otherwise".split()
)
ENGLISH_LABEL = re.compile(
    r"\b(?:chapter|summary|problems|preface|bibliography|photo credits|further reading|"
    r"historical remarks|glossary|continued|input(?:[eé])?|output(?:[eé])?|"
    r"blank|domain(?:[eé])?|otherwise|iff|term(?:s|[eé])?|natural|valid|"
    r"lemma|soundness|enumerable|atomic|equality|truth|falsity|falsehood|absurdity|exercise|"
    r"substitution|tuple|start|halt|subterm|prefix|balance|vertices|"
    r"assumption|left shift|right shift|blank symbol|"
    r"if and only if|for every|such that|if there is|we can|let us|"
    r"without loss of generality|the following|this means|as follows)\b", re.I
)


def outline(reader, tree=None):
    for item in reader.outline if tree is None else tree:
        if isinstance(item, list):
            yield from outline(reader, item)
        else:
            yield item.title, reader.get_destination_page_number(item) + 1


def text_pages(pdf):
    stdout = subprocess.check_output(["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), "-"])
    return stdout.decode("utf-8").rstrip("\f").split("\f")


def words(text):
    text = unicodedata.normalize("NFKC", text).casefold()
    return re.findall(r"[^\W\d_]+", text)


def phrase_windows(text, width):
    tokens = words(text)
    for index in range(len(tokens) - width + 1):
        window = tuple(tokens[index:index + width])
        if sum(token in ENGLISH_WORDS for token in window) >= 2:
            yield window


def joined_hyphens(page):
    return re.sub(r"(?<=[A-Za-z])[-\u00ad][ \t]*\r?\n[ \t]*(?=[a-z])", "", page)


def shared_words(pages, original_pages, omit):
    # Repeated English source words can reveal isolated labels and terminology
    # that do not occur in a longer matching phrase.
    pattern = re.compile(r"(?<![\w-])[a-zA-Z]{5,}(?![\w-])")

    def matches(page):
        text = unicodedata.normalize("NFKC", page)
        return {match.casefold() for match in pattern.findall(text)}

    frequencies = Counter(
        match.casefold() for page in original_pages
        for match in pattern.findall(unicodedata.normalize("NFKC", joined_hyphens(page)))
    )
    records = {}
    for number, page in enumerate(pages, 1):
        if number in omit:
            continue
        for line in joined_hyphens(page).splitlines():
            for word in matches(line):
                if frequencies[word] >= 3:
                    candidate = records.setdefault(word, {"pages": set(), "example": " ".join(line.split())})
                    candidate["pages"].add(number)
    return [
        {"word": word, "pages": sorted(record["pages"]), "example": record["example"]}
        for word, record in sorted(records.items())
    ]


def english_candidates(pages, original_pages, omit):
    width = 5
    reference = {phrase for page in original_pages for phrase in phrase_windows(page, width)}
    matched_phrases = defaultdict(set)
    flagged_lines = []
    for number, page in enumerate(pages, 1):
        if number in omit:
            continue
        page = joined_hyphens(page)
        for phrase in phrase_windows(page, width):
            if phrase in reference:
                matched_phrases[" ".join(phrase)].add(number)
        for line in page.splitlines():
            excerpt = " ".join(line.split())
            if ENGLISH_LABEL.search(excerpt):
                flagged_lines.append({"page": number, "text": excerpt})
    return (
        [{"phrase": phrase, "pages": sorted(numbers)} for phrase, numbers in sorted(matched_phrases.items())],
        flagged_lines,
    )


def latin_inventory(pages, omit):
    """List every Latin-letter run and a sample line for human classification."""
    records = defaultdict(dict)
    for page_number, page in enumerate(pages, 1):
        if page_number in omit:
            continue
        for line in joined_hyphens(page).splitlines():
            for match in re.finditer(r"[A-Za-z]{2,}", line):
                word = match[0].casefold()
                records[word].setdefault(page_number, " ".join(line.split()))
    return [
        {"word": word, "pages": sorted(instances), "example": next(iter(instances.values()))}
        for word, instances in sorted(records.items())
    ]


def out_of_page_text(pdf):
    xml = subprocess.check_output(["pdftotext", "-bbox-layout", "-enc", "UTF-8", str(pdf), "-"])
    pages = ElementTree.fromstring(xml).findall(".//{*}page")
    violations = []
    for number, page in enumerate(pages, 1):
        width = float(page.attrib["width"])
        height = float(page.attrib["height"])
        for word in page.findall(".//{*}word"):
            x0, y0, x1, y1 = (
                float(word.attrib[key]) for key in ("xMin", "yMin", "xMax", "yMax")
            )
            clearance = min(x0, y0, width - x1, height - y1)
            if clearance < -.25:
                violations.append({"page": number, "text": word.text,
                                   "points_past_page": round(-clearance, 2)})
    return violations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, default=ROOT / "slc-screen-gu.pdf")
    parser.add_argument("--reference", type=Path, required=True, help="Pinned English screen PDF")
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    manifest = json.loads((ROOT / "MANIFEST.json").read_bytes())
    reference_sha = sha256(args.reference.read_bytes()).hexdigest()
    if reference_sha != manifest["sources"]["slc"]["comparison_pdf_sha256"]:
        raise ValueError("The English comparison PDF differs from the pinned baseline")

    original = PdfReader(args.reference)
    target = PdfReader(args.pdf, strict=True)
    original_outline = list(outline(original))
    target_outline = list(outline(target))
    originals = [(match[1], match[2], page) for title, page in original_outline
                 if (match := CHAPTER.fullmatch(title))]
    targets = [(match[1], match[2], page) for title, page in target_outline
               if (match := CHAPTER.fullmatch(title))]
    expected = [str(n) for n in range(1, 16)] + list("ABCD")
    same_chapters = [row[0] for row in originals] == [row[0] for row in targets] == expected
    bib_start = next(page for title, page in target_outline if title.strip() == "સંદર્ભગ્રંથો")
    after_bib = next((page for title, page in target_outline
                      if page > bib_start and title.strip().startswith("ઓપન લોજિક")), len(target.pages) + 1)
    omit = set(range(bib_start, after_bib))
    text = text_pages(args.pdf)
    if len(text) != len(target.pages):
        raise ValueError("Text extraction did not yield a page record for each PDF page")
    reference_text = text_pages(args.reference)
    phrases, labels = english_candidates(text, reference_text, omit)
    vocabulary = shared_words(text, reference_text, omit)
    result = {
        "sha256": sha256(args.pdf.read_bytes()).hexdigest(),
        "pages": len(target.pages),
        "english_comparison_pages": len(original.pages),
        "same_chapter_numbers": same_chapters,
        "english_chapters": originals,
        "gujarati_chapters": targets,
        "preface": [page for title, page in target_outline if title == "પ્રસ્તાવના"],
        "glossary": [page for title, page in target_outline if title == "પરિભાષાકોશ"],
        "summary_bookmarks": [page for title, page in target_outline if title == "સારાંશ"],
        "bibliography_pages_excluded": sorted(omit),
        "shared_english_phrase_candidates": phrases,
        "english_label_candidates": labels,
        "shared_english_word_candidates": vocabulary,
        "latin_word_inventory": latin_inventory(text, omit),
        "text_past_page_edge": out_of_page_text(args.pdf),
    }
    args.report.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "pages": len(target.pages), "same_chapter_numbers": same_chapters,
        "summaries": len(result["summary_bookmarks"]),
        "phrase_candidates": len(phrases), "label_candidates": len(labels),
        "word_candidates": len(vocabulary),
    }))
    if result["text_past_page_edge"]:
        raise SystemExit("Text extends past a physical page edge. See the report.")
    if not same_chapters:
        raise SystemExit("Chapter inventory differs from the English screen edition")
    if len(result["summary_bookmarks"]) != len(manifest["screen"]["chapter_summaries"]):
        raise SystemExit("The PDF does not contain all required summary bookmarks")
    if not result["preface"] or len(result["glossary"]) != 1:
        raise SystemExit("The PDF is missing a unique glossary or a preface bookmark")


if __name__ == "__main__":
    main()
