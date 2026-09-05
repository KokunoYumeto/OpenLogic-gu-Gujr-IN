# Gujarati edition scope and variant policy

This repository publishes one semantic Gujarati edition identified as
`gu-Gujr-IN`. Its script subtag is `Gujr`, its territory subtag is `IN`, and its
text direction is left to right. The edition uses the standard contemporary
Gujarati script throughout prose. It does not currently define separate
regional, community, or register variants.

The prose register is educational and scholarly Gujarati suited to a logic
textbook. Terminology decisions draw on locally inspected Gujarati State School
Textbook Board mathematics books and Gujarati Vishwakosh mathematical and
logical writing. The frozen English Open Logic source controls each formal
claim. The authority passages support vocabulary and expository register; they
are not treated as substitute sources for the mathematics.

Mathematical displays retain the source's international notation, including
Latin and Greek variables, logical signs, and Arabic digits inside formulas.
Gujarati digits may appear in Gujarati prose and reader-interface counts. This
is one notation profile within the semantic edition, rather than a second
translation layer.

All authored Gujarati text is stored as Unicode and checked in NFC. Reader PDFs
embed Noto Sans Gujarati, while the HTML reader ships the corresponding local
webfonts. Names and specialist terms for which the checked authorities provide
no exact Gujarati form may be transliterated into Gujarati script. Such choices
are marked provisional or prioritized for expert review in
[`translation-decisions/PRIORITY_REVIEW.md`](translation-decisions/PRIORITY_REVIEW.md).

No deterministic script projection is needed because Gujarati has a single
standard script for this edition. A separate regional adaptation would be
warranted only after evidence of a materially different terminology or register
requirement. A pronunciation or accessibility companion could be added later as
a child layer, but it would not change the semantic Gujarati text. The current
release therefore records one `semantic_translation` layer and does not invent
unsupported variants.

The policy is reviewable rather than prescriptive: corrections supported by
Gujarati mathematical usage can update the decision register and every linked
occurrence without creating a new variant unless the correction establishes a
systematic audience-specific layer.
