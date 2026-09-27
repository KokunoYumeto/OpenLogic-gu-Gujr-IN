# Building and checking the second-order readers

The v0.21.0 release covers earlier OLP-0004–0273 and the new OLP-0322–0340 part. OLP-0274–0321 is absent from the cumulative reader.

`OpenLogic-gu-Gujr-IN-Second-Order-Cumulative-Full-Text.tex` contains the complete text, label index, preamble and reader drivers for the 349-page PDF. Unpack the companion source ZIP at the same root to supply Open Logic styles, fonts, diagrams and bibliography support. Run LuaLaTeX on that TeX file three times from the archive root, with job name `gu-second-order-part` and shell escape disabled. The accepted cumulative PDF is `OpenLogic-gu-Gujr-IN-Second-Order-Cumulative.pdf`.

`OpenLogic-gu-Gujr-IN-Second-Order-Part-Source.tex` is the exact editable 19-unit body at the end of the cumulative text. The accepted 17-page part PDF retains the cumulative cover and pagination. It was made from physical page 1 followed by pages 334–349 of the accepted cumulative PDF. With pypdf 6.12.2 installed, `OpenLogic-gu-Gujr-IN-Second-Order-Part-Extraction.py` reproduces that PDF byte for byte; it checks both the input and output SHA-256 hashes.

The direct full-text TeX was materialized from the same wrapper and body files that produced the accepted cumulative PDF. A fresh TeX replay of this direct file is pending because the shared build slot was occupied at the first two bounded attempts; neither attempt started a TeX process. This affects only the independent byte-for-byte replay claim. The accepted PDFs, source-body equality and part extraction checks remain unchanged.
