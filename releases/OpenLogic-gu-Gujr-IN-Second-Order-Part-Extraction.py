"""Reproduce the accepted 17-page second-order part PDF from the cumulative PDF.

Requires pypdf 6.12.2. Run from the release directory:

    python OpenLogic-gu-Gujr-IN-Second-Order-Part-Extraction.py

The part PDF contains the cumulative reader's cover (physical page 1)
followed by its second-order part (physical pages 334 through 349).
The editable text for those pages is in the adjacent Part-Source.tex;
the complete document is in Cumulative-Full-Text.tex. The remaining
styles, fonts, bibliography support, and diagrams are in the source ZIP.
"""

from hashlib import sha256
from pathlib import Path

from pypdf import PdfReader, PdfWriter

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "OpenLogic-gu-Gujr-IN-Second-Order-Cumulative.pdf"
OUTPUT = HERE / "OpenLogic-gu-Gujr-IN-Second-Order-Part.pdf"
ACCEPTED_SOURCE_SHA256 = "67ff7f586e3c19c3d9a673ad3139b5ad9c94e36cf1e2af2a2fa34ea1cc36d6a5"
ACCEPTED_OUTPUT_SHA256 = "899667d2a1a5c7744fe9195756b31c9c3ea66200ed2fdefbc6dd4223f032a90f"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


assert SOURCE.is_file() and digest(SOURCE) == ACCEPTED_SOURCE_SHA256
reader = PdfReader(str(SOURCE))
assert len(reader.pages) == 349
writer = PdfWriter()
writer.add_page(reader.pages[0])
for index in range(333, 349):
    writer.add_page(reader.pages[index])
writer.add_metadata({"/Title": "Open Logic Gujarati — Second-Order Logic Part",
                     "/Subject": "Gujarati translation of OLP-0322–0340; 19 units"})
with OUTPUT.open("wb") as stream:
    writer.write(stream)
assert len(PdfReader(str(OUTPUT)).pages) == 17
assert digest(OUTPUT) == ACCEPTED_OUTPUT_SHA256
print(f"Reproduced {OUTPUT.name}: {OUTPUT.stat().st_size} bytes, SHA-256 {digest(OUTPUT)}")
