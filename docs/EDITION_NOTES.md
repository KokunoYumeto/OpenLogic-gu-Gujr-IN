# Scope, language decisions and verification

This first cumulative release translates OLP-0004 through OLP-0010, the complete Sets chapter. It contains six sections and the chapter driver, covering extensionality, subsets and power sets, important number sets and strings, unions/intersections/difference, ordered tuples and Cartesian products, and Russell's paradox. Every source branch for novice, mathematical and computer-science examples in this chapter is included. References guarded by upstream conditions for later chapters remain conditional.

The complete edition will cover all 722 content units in one coherent reader. This release does not satisfy that terminal goal. Remaining units are explicitly marked untranslated in the coverage record. Alternative wrappers and formal-only units will receive explicit treatment; a detached supplement will not stand in for a complete reader.

## Gujarati canon

The terminology follows actually consulted Gujarati textbook and scholarly prose. Five originals and fifteen exact page/paragraph passages underlie this batch. Source URLs, original hashes, passage locators and short term attestations are in the provenance files. Consulted schoolbook pages were visually read because their PDF extraction is mostly unusable. The current textbook omits the older power-set section; an older textbook's printed page 13 supplies the definition of ઘાતગણ.

Set is ગણ; algebraic group remains સમૂહ. Other attested choices include ઘટક, ઉપગણ, ઉચિત ઉપગણ, ઘાતગણ, યોગગણ, છેદગણ, અલગ ગણો, તફાવત ગણ, કાર્તેઝીય ગુણાકાર and ક્રમયુક્ત જોડ. Extensionality uses the provisional descriptive label ઘટકો દ્વારા નિર્ધારિત સમાનતા, based on the attested equality criterion. String, continuum, perfect-number and general tuple labels retain explicit lexical uncertainty. No dictionary is treated as sufficient evidence for every technical sense.

The CSTT glossary and CIET module were located but their direct downloads failed; neither is claimed as consulted. Gujarati witnesses inform language and terminology. Their mathematical simplifications do not replace the frozen English theorem. In particular, the early discussion of set notation is preserved alongside its later existence qualification in Russell's paradox.

## Actual checks

The seven units contain 86 aligned linguistic blocks. Each block records source/target UTF-8 byte ranges and SHA-256 hashes and the canon passages actually consulted. Structural QA verifies all 327 mathematical spans after removing translated prose within math text macros, every identifier/reference/asset, all environments and balanced braces. All Gujarati source files are NFC; no replacement characters or Devanagari contamination were found. Same-agent source comparison and nine explicit reverse-paraphrase samples examine mathematical meaning, especially quantified directions, membership versus inclusion, products, and Russell's two contradiction branches. This is not independent human review or a fluency certification.

The 10-page LuaLaTeX PDF uses pinned Noto Sans Gujarati with HarfBuzz shaping. All pages were visually inspected. The final two guarded passes were byte-identical. No missing glyphs, overfull boxes or unresolved references appeared. The shell-escape-disabled package notice is expected; no shell escape was enabled.

PDF extraction has a documented limitation: PyMuPDF joins many Gujarati words, and the installed Poppler extractor occasionally displaces vowel signs. The accompanying HTML retains Unicode prose and native MathML, with no JavaScript or external runtime dependency. It is the preferred format for selecting text and assistive reading. PDF visual correctness does not imply perfect PDF text extraction.

## Source alignment and boundaries

The Gujarati files preserve upstream macros and identities. Reader adapters expand the English article/plural text-token mechanism into Gujarati inflections without altering the aligned editable files. Source mathematical notation follows the frozen defaults. The HTML diagrams reproduce the upstream TikZ path coordinates and colors as SVG. Editorial status and diagnostic notes are separated from the translated mathematical text.
