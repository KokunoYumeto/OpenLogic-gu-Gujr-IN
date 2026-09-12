# Gujarati terminology and translation review log

Updated 2026-09-09T21:47:22.672463+00:00. This is a **complete decision log for the current 134/722-unit draft**, while the translation corpus itself remains partial. Public source-checkpoint verification covers 122/722 units with checkpoint 012. It contains all 136 terminology decisions from the durable ledger and all 93 source corrections identified so far. It must grow with the translation.

Every term entry names the wording and sense, exact current English/Gujarati use locations where a literal form exists, the Gujarati authorities actually checked, recoverable alternatives, rationale, uncertainty and a question an expert can answer asynchronously. “Retrospective” means the explanation was reconstructed from earlier durable records; it does not claim an unrecorded search or consultation. Provisional entries are open corrections and do not stop the full-corpus workflow.

The machine-readable companion is [`TRANSLATION_DECISIONS.jsonl`](TRANSLATION_DECISIONS.jsonl); completeness metadata is in [`TRANSLATION_DECISION_LOG_METADATA.json`](TRANSLATION_DECISION_LOG_METADATA.json).

## Terminology decisions

### GU-T001: set → ગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:1`.
- **English use:** `upstream/content/sets-functions-relations/sets/sets.tex:8` (OLP-0004, “set”)
- **Gujarati use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Authorities actually checked:** `GU-P001` (GU-GSSTB-MATH11, {"pdf_page_one_based": 15, "printed_page": "3"}); `GU-P010` (GU-VK-MATH, {"line_one_based": 478, "utf8_start": 182255, "utf8_end": 182785, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P015` (GU-VK-GROUPS, {"line_one_based": 26, "utf8_start": 820, "utf8_end": 1060, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Actual usage distinguishes set from group સમૂહ.
- **Alternatives:** સમૂહ — rejected for sets because the consulted material distinguishes it as group.
- **Review question:** In Gujarati mathematical-logic prose, does “ગણ” express “set” with the scope stated in this rationale: Actual usage distinguishes set from group સમૂહ. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T002: element → ઘટક

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:2`.
- **English use:** `upstream/content/sets-functions-relations/sets/basics.tex:14` (OLP-0005, “element”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/basics.tex:10` (OLP-0005, “ઘટક”)
- **Authorities actually checked:** `GU-P001` (GU-GSSTB-MATH11, {"pdf_page_one_based": 15, "printed_page": "3"}); `GU-P013` (GU-VK-SETS, {"line_one_based": 36, "utf8_start": 3637, "utf8_end": 4684, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** સભ્ય is attested synonym; element text-token emits ઘટક/ઘટકો.
- **Alternatives:** સભ્ય — retained as an attested synonym, while ઘટક is the edition-wide output token.
- **Review question:** In Gujarati mathematical-logic prose, does “ઘટક” express “element” with the scope stated in this rationale: સભ્ય is attested synonym; element text-token emits ઘટક/ઘટકો. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T003: extensionality → ઘટકો દ્વારા નિર્ધારિત સમાનતા

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:3`.
- **English use:** `upstream/content/sets-functions-relations/sets/basics.tex:10` (OLP-0005, “extensionality”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/basics.tex:10` (OLP-0005, “ઘટકો દ્વારા નિર્ધારિત સમાનતા”)
- **Authorities actually checked:** `GU-P002` (GU-GSSTB-MATH11, {"pdf_page_one_based": 20, "printed_page": "8"}); `GU-P013` (GU-VK-SETS, {"line_one_based": 36, "utf8_start": 3637, "utf8_end": 4684, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Concept attested, standard Gujarati single-name not verified; deliberately descriptive. Does not assert existence.
- **Alternatives:** વિસ્તરણાત્મકતા — not adopted because no checked Gujarati authority attested it in this mathematical sense.
- **Review question:** In Gujarati mathematical-logic prose, does “ઘટકો દ્વારા નિર્ધારિત સમાનતા” express “extensionality” with the scope stated in this rationale: Concept attested, standard Gujarati single-name not verified; deliberately descriptive. Does not assert existence. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T004: subset → ઉપગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:4`.
- **English use:** `upstream/content/sets-functions-relations/sets/subsets.tex:19` (OLP-0006, “subset”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/subsets.tex:10` (OLP-0006, “ઉપગણ”)
- **Authorities actually checked:** `GU-P003` (GU-GSSTB-MATH11, {"pdf_page_one_based": 22, "printed_page": "10"}); `GU-P013` (GU-VK-SETS, {"line_one_based": 36, "utf8_start": 3637, "utf8_end": 4684, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Subset includes equality; preserve upstream subseteq.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ઉપગણ” express “subset” with the scope stated in this rationale: Subset includes equality; preserve upstream subseteq. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T005: proper subset → ઉચિત ઉપગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:5`.
- **English use:** `upstream/content/sets-functions-relations/sets/subsets.tex:24` (OLP-0006, “proper subset”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/subsets.tex:23` (OLP-0006, “ઉચિત ઉપગણ”)
- **Authorities actually checked:** `GU-P014` (GU-VK-SETS, {"line_one_based": 37, "utf8_start": 4684, "utf8_end": 4762, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Strictness retained by inequality; do not change source symbols to schoolbook convention.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ઉચિત ઉપગણ” express “proper subset” with the scope stated in this rationale: Strictness retained by inequality; do not change source symbols to schoolbook convention. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T006: power set → ઘાતગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:6`.
- **English use:** `upstream/content/sets-functions-relations/sets/subsets.tex:75` (OLP-0006, “power set”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/subsets.tex:10` (OLP-0006, “ઘાતગણ”)
- **Authorities actually checked:** `GU-P009` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 23, "printed_page": "13"})
- **Chosen sense and rationale:** Actual definition verified in older textbook page; not inferred from glossary.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ઘાતગણ” express “power set” with the scope stated in this rationale: Actual definition verified in older textbook page; not inferred from glossary. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T007: union → યોગગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:7`.
- **English use:** `upstream/content/sets-functions-relations/sets/unions-and-intersections.tex:20` (OLP-0008, “union”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/unions-and-intersections.tex:10` (OLP-0008, “યોગગણ”)
- **Authorities actually checked:** `GU-P005` (GU-GSSTB-MATH11, {"pdf_page_one_based": 28, "printed_page": "16"})
- **Chosen sense and rationale:** Inclusive or, including shared members.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “યોગગણ” express “union” with the scope stated in this rationale: Inclusive or, including shared members. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T008: intersection → છેદગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:8`.
- **English use:** `upstream/content/sets-functions-relations/sets/unions-and-intersections.tex:62` (OLP-0008, “intersection”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/unions-and-intersections.tex:10` (OLP-0008, “છેદગણ”)
- **Authorities actually checked:** `GU-P005` (GU-GSSTB-MATH11, {"pdf_page_one_based": 28, "printed_page": "16"}); `GU-P006` (GU-GSSTB-MATH11, {"pdf_page_one_based": 29, "printed_page": "17"})
- **Chosen sense and rationale:** Members in both sets.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “છેદગણ” express “intersection” with the scope stated in this rationale: Members in both sets. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T009: disjoint → અલગ ગણો

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:9`.
- **English use:** `upstream/content/sets-functions-relations/sets/unions-and-intersections.tex:77` (OLP-0008, “disjoint”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/unions-and-intersections.tex:77` (OLP-0008, “અલગ ગણો”)
- **Authorities actually checked:** `GU-P006` (GU-GSSTB-MATH11, {"pdf_page_one_based": 29, "printed_page": "17"})
- **Chosen sense and rationale:** Technical definition is empty intersection, not mere inequality.
- **Alternatives:** વિચ્છેદી — not adopted without direct authority; the definition “empty intersection” controls.
- **Review question:** In Gujarati mathematical-logic prose, does “અલગ ગણો” express “disjoint” with the scope stated in this rationale: Technical definition is empty intersection, not mere inequality. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T010: difference → તફાવત ગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:10`.
- **English use:** `upstream/content/sets-functions-relations/sets/unions-and-intersections.tex:153` (OLP-0008, “difference”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/unions-and-intersections.tex:157` (OLP-0008, “તફાવત ગણ”)
- **Authorities actually checked:** `GU-P007` (GU-GSSTB-MATH11, {"pdf_page_one_based": 30, "printed_page": "18"})
- **Chosen sense and rationale:** Direction A minus B retained.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “તફાવત ગણ” express “difference” with the scope stated in this rationale: Direction A minus B retained. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T011: Cartesian product → કાર્તેઝીય ગુણાકાર

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:11`.
- **English use:** `upstream/content/sets-functions-relations/sets/pairs-and-products.tex:52` (OLP-0009, “Cartesian product”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/pairs-and-products.tex:10` (OLP-0009, “કાર્તેઝીય ગુણાકાર”)
- **Authorities actually checked:** `GU-P008` (GU-GSSTB-MATH11, {"pdf_page_one_based": 38, "printed_page": "26"})
- **Chosen sense and rationale:** Actual Gujarati textbook use.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “કાર્તેઝીય ગુણાકાર” express “Cartesian product” with the scope stated in this rationale: Actual Gujarati textbook use. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T012: ordered pair → ક્રમયુક્ત જોડ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:12`.
- **English use:** `upstream/content/sets-functions-relations/sets/pairs-and-products.tex:16` (OLP-0009, “ordered pair”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/pairs-and-products.tex:14` (OLP-0009, “ક્રમયુક્ત જોડ”)
- **Authorities actually checked:** `GU-P008` (GU-GSSTB-MATH11, {"pdf_page_one_based": 38, "printed_page": "26"})
- **Chosen sense and rationale:** Coordinates ordered; set-theoretic Wiener–Kuratowski definition remains English-authoritative.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ક્રમયુક્ત જોડ” express “ordered pair” with the scope stated in this rationale: Coordinates ordered; set-theoretic Wiener–Kuratowski definition remains English-authoritative. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T013: perfect number → પૂર્ણ સંખ્યા

- **Status and uncertainty:** `provisional`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:13`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/sets/basics.tex:71` (OLP-0005, “પૂર્ણ સંખ્યા”)
- **Authorities actually checked:** `GU-P004` (GU-GSSTB-MATH11, {"pdf_page_one_based": 19, "printed_page": "7"})
- **Chosen sense and rationale:** Native numeracy prose only; exact perfect-number name not verified. Definition supplied; integers always પૂર્ણાંક.
- **Alternatives:** સંપૂર્ણ સંખ્યા — avoided because the recovered school material uses it for whole number, creating a sense collision.
- **Review question:** In Gujarati mathematical-logic prose, does “પૂર્ણ સંખ્યા” express “perfect number” with the scope stated in this rationale: Native numeracy prose only; exact perfect-number name not verified. Definition supplied; integers always પૂર્ણાંક. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T014: string → પ્રતીકશ્રેણી

- **Status and uncertainty:** `provisional`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:14`.
- **English use:** `upstream/content/sets-functions-relations/sets/important-sets.tex:49` (OLP-0007, “string”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/important-sets.tex:43` (OLP-0007, “પ્રતીકશ્રેણી”)
- **Authorities actually checked:** `GU-P001` (GU-GSSTB-MATH11, {"pdf_page_one_based": 15, "printed_page": "3"}); `GU-P008` (GU-GSSTB-MATH11, {"pdf_page_one_based": 38, "printed_page": "26"})
- **Chosen sense and rationale:** Descriptive formation for finite symbol sequence; no concept-specific string attestation yet.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “પ્રતીકશ્રેણી” express “string” with the scope stated in this rationale: Descriptive formation for finite symbol sequence; no concept-specific string attestation yet. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T015: sequence → અનુક્રમ

- **Status and uncertainty:** `provisional`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:15`.
- **English use:** `upstream/content/sets-functions-relations/sets/important-sets.tex:48` (OLP-0007, “sequence”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/important-sets.tex:45` (OLP-0007, “અનુક્રમ”)
- **Authorities actually checked:** `GU-P008` (GU-GSSTB-MATH11, {"pdf_page_one_based": 38, "printed_page": "26"})
- **Chosen sense and rationale:** Ordered-object prose supports construction; advanced sequence terminology needs further canon.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “અનુક્રમ” express “sequence” with the scope stated in this rationale: Ordered-object prose supports construction; advanced sequence terminology needs further canon. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T016: tuple → બહુજોડ / ક્રમયુક્ત n-જોડ

- **Status and uncertainty:** `provisional`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:16`.
- **English use:** `upstream/content/sets-functions-relations/sets/pairs-and-products.tex:15` (OLP-0009, “tuple”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/pairs-and-products.tex:10` (OLP-0009, “બહુજોડ”)
- **Authorities actually checked:** `GU-P008` (GU-GSSTB-MATH11, {"pdf_page_one_based": 38, "printed_page": "26"})
- **Chosen sense and rationale:** Generalization from attested ordered pair; triple ત્રિજોડ and quadruple ચતુર્જોડ provisional.
- **Alternatives:** ટ્યુપલ — avoided as an unexplained transliteration; the descriptive ordered n-tuple wording remains provisional.
- **Review question:** In Gujarati mathematical-logic prose, does “બહુજોડ / ક્રમયુક્ત n-જોડ” express “tuple” with the scope stated in this rationale: Generalization from attested ordered pair; triple ત્રિજોડ and quadruple ચતુર્જોડ provisional. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T017: continuum → સાતત્યક

- **Status and uncertainty:** `provisional`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:17`.
- **English use:** `upstream/content/sets-functions-relations/sets/important-sets.tex:24` (OLP-0007, “continuum”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/important-sets.tex:23` (OLP-0007, “સાતત્યક”)
- **Authorities actually checked:** `GU-P011` (GU-VK-MATH, {"line_one_based": 479, "utf8_start": 182785, "utf8_end": 185277, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Witness describes real-number set; precise lexical choice unverified.
- **Alternatives:** નિરંતરક — not found in the authorities actually checked.
- **Review question:** In Gujarati mathematical-logic prose, does “સાતત્યક” express “continuum” with the scope stated in this rationale: Witness describes real-number set; precise lexical choice unverified. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T018: comprehension → ગુણધર્મ વડે ગણરચના

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:18`.
- **English use:** `upstream/content/sets-functions-relations/sets/russells-paradox.tex:22` (OLP-0010, “comprehension”)
- **Gujarati use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Authorities actually checked:** `GU-P001` (GU-GSSTB-MATH11, {"pdf_page_one_based": 15, "printed_page": "3"}); `GU-P012` (GU-VK-MATH, {"line_one_based": 486, "utf8_start": 192646, "utf8_end": 193794, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Preserve existence qualification; not general comprehension by reading a sentence.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ગુણધર્મ વડે ગણરચના” express “comprehension” with the scope stated in this rationale: Preserve existence qualification; not general comprehension by reading a sentence. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T019: paradox → વિરોધાભાસ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:19`.
- **English use:** `upstream/content/sets-functions-relations/sets/sets.tex:20` (OLP-0004, “paradox”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/russells-paradox.tex:11` (OLP-0010, “વિરોધાભાસ”)
- **Authorities actually checked:** `GU-P012` (GU-VK-MATH, {"line_one_based": 486, "utf8_start": 192646, "utf8_end": 193794, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Contradiction is પરસ્પરવિરોધ; Russell language usage checked.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “વિરોધાભાસ” express “paradox” with the scope stated in this rationale: Contradiction is પરસ્પરવિરોધ; Russell language usage checked. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T020: relation → સંબંધ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:20`.
- **English use:** `upstream/content/sets-functions-relations/relations/relations-as-sets.tex:17` (OLP-0012, “relation”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/relations-complete.tex:8` (OLP-0011, “સંબંધ”)
- **Authorities actually checked:** `GU-P016` (GU-GSSTB-MATH11, {"pdf_page_one_based": 41, "printed_page": "29"}); `GU-P018` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 7, "printed_page": "1"})
- **Chosen sense and rationale:** Direct definition as subset; not a colloquial-only relation word.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સંબંધ” express “relation” with the scope stated in this rationale: Direct definition as subset; not a colloquial-only relation word. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T021: domain → પ્રદેશ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:21`.
- **English use:** `upstream/content/sets-functions-relations/relations/equivalence-relations.tex:24` (OLP-0015, “domain”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/special-properties.tex:15` (OLP-0014, “પ્રદેશ”)
- **Authorities actually checked:** `GU-P016` (GU-GSSTB-MATH11, {"pdf_page_one_based": 41, "printed_page": "29"})
- **Chosen sense and rationale:** Base set and set of first coordinates differentiated by source context.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “પ્રદેશ” express “domain” with the scope stated in this rationale: Base set and set of first coordinates differentiated by source context. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T022: reflexive → સ્વવાચક

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:22`.
- **English use:** `upstream/content/sets-functions-relations/relations/special-properties.tex:24` (OLP-0014, “reflexive”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/relations-as-sets.tex:109` (OLP-0012, “સ્વવાચક”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"})
- **Chosen sense and rationale:** Every domain element relates to itself.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સ્વવાચક” express “reflexive” with the scope stated in this rationale: Every domain element relates to itself. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T023: symmetric → સંમિત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:23`.
- **English use:** `upstream/content/sets-functions-relations/relations/special-properties.tex:34` (OLP-0014, “symmetric”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/special-properties.tex:33` (OLP-0014, “સંમિત”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"})
- **Chosen sense and rationale:** Both directions; actual Gujarati textbook spelling.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સંમિત” express “symmetric” with the scope stated in this rationale: Both directions; actual Gujarati textbook spelling. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T024: transitive → પરંપરિત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:24`.
- **English use:** `upstream/content/sets-functions-relations/relations/special-properties.tex:29` (OLP-0014, “transitive”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/special-properties.tex:28` (OLP-0014, “પરંપરિત”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"})
- **Chosen sense and rationale:** Composition of two related pairs; use attested Gujarati, not guessed સંક્રમિત.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “પરંપરિત” express “transitive” with the scope stated in this rationale: Composition of two related pairs; use attested Gujarati, not guessed સંક્રમિત. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T025: antisymmetric → વિસંમિત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:25`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/relations/special-properties.tex:38` (OLP-0014, “વિસંમિત”)
- **Authorities actually checked:** `GU-P020` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 9, "printed_page": "3"}); `GU-P021` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 10, "printed_page": "4"})
- **Chosen sense and rationale:** Both directions imply equality; not mere negation of symmetry.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “વિસંમિત” express “antisymmetric” with the scope stated in this rationale: Both directions imply equality; not mere negation of symmetry. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T026: equivalence relation/class → સામ્ય સંબંધ / સામ્ય વર્ગ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:26`.
- **English use:** `upstream/content/sets-functions-relations/relations/equivalence-relations.tex:17` (OLP-0015, “equivalence relation”); `upstream/content/sets-functions-relations/relations/equivalence-relations.tex:24` (OLP-0015, “class”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/special-properties.tex:20` (OLP-0014, “સામ્ય સંબંધ”); `gu/content/sets-functions-relations/relations/equivalence-relations.tex:22` (OLP-0015, “સામ્ય વર્ગ”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"}); `GU-P023` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 12, "printed_page": "6"})
- **Chosen sense and rationale:** Actual definitions and partition proof inspected.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સામ્ય સંબંધ / સામ્ય વર્ગ” express “equivalence relation/class” with the scope stated in this rationale: Actual definitions and partition proof inspected. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T027: irreflexive → અસ્વવાચક

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:27`.
- **English use:** `upstream/content/sets-functions-relations/relations/relations-as-sets.tex:104` (OLP-0012, “irreflexive”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/relations-as-sets.tex:109` (OLP-0012, “અસ્વવાચક”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"})
- **Chosen sense and rationale:** No attested label acquired. Defined explicitly as no self-pairs; do not confuse with merely not reflexive.
- **Alternatives:** અપ્રતિબિંબિત — not found in the authorities actually checked.
- **Review question:** In Gujarati mathematical-logic prose, does “અસ્વવાચક” express “irreflexive” with the scope stated in this rationale: No attested label acquired. Defined explicitly as no self-pairs; do not confuse with merely not reflexive. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T028: asymmetric → અસંમિત

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:28`.
- **English use:** `upstream/content/sets-functions-relations/relations/special-properties.tex:75` (OLP-0014, “asymmetric”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/special-properties.tex:77` (OLP-0014, “અસંમિત”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"}); `GU-P020` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 9, "printed_page": "3"})
- **Chosen sense and rationale:** No attested label acquired. Both directions never coexist, including self-pairs. Distinguished from વિસંમિત and merely not symmetric.
- **Alternatives:** વિષમિત — rejected because it risks confusion with other symmetry vocabulary and lacked direct attestation.
- **Review question:** In Gujarati mathematical-logic prose, does “અસંમિત” express “asymmetric” with the scope stated in this rationale: No attested label acquired. Both directions never coexist, including self-pairs. Distinguished from વિસંમિત and merely not symmetric. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T029: connected relation → તુલનાયુક્ત સંબંધ

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:29`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:107` (OLP-0047, “તુલનાયુક્ત સંબંધ”)
- **Authorities actually checked:** `GU-P021` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 10, "printed_page": "4"})
- **Chosen sense and rationale:** Every distinct pair comparable in at least one direction; no verified standard label.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “તુલનાયુક્ત સંબંધ” express “connected relation” with the scope stated in this rationale: Every distinct pair comparable in at least one direction; no verified standard label. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T030: order/preorder/partial/linear/strict → ક્રમ / પૂર્વક્રમ / આંશિક ક્રમ / રેખીય ક્રમ / કડક ક્રમ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:30`.
- **English use:** `upstream/content/sets-functions-relations/sets/basics.tex:21` (OLP-0005, “order”); `upstream/content/sets-functions-relations/relations/orders.tex:22` (OLP-0016, “preorder”); `upstream/content/sets-functions-relations/relations/orders.tex:27` (OLP-0016, “partial”); `upstream/content/sets-functions-relations/relations/orders.tex:32` (OLP-0016, “linear”); `upstream/content/sets-functions-relations/relations/relations-as-sets.tex:105` (OLP-0012, “strict”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/basics.tex:20` (OLP-0005, “ક્રમ”); `gu/content/sets-functions-relations/relations/orders.tex:23` (OLP-0016, “પૂર્વક્રમ”); `gu/content/sets-functions-relations/relations/orders.tex:27` (OLP-0016, “આંશિક ક્રમ”); `gu/content/sets-functions-relations/relations/orders.tex:31` (OLP-0016, “રેખીય ક્રમ”); `gu/content/sets-functions-relations/relations/relations-as-sets.tex:110` (OLP-0012, “કડક ક્રમ”)
- **Authorities actually checked:** `GU-P021` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 10, "printed_page": "4"})
- **Chosen sense and rationale:** Definitions govern. Gujarati relations source supplies prose pattern, not attestation for these specialized labels.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ક્રમ / પૂર્વક્રમ / આંશિક ક્રમ / રેખીય ક્રમ / કડક ક્રમ” express “order/preorder/partial/linear/strict” with the scope stated in this rationale: Definitions govern. Gujarati relations source supplies prose pattern, not attestation for these specialized labels. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T031: predicate → વિધેય

- **Status and uncertainty:** `adopted_contextual`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:31`.
- **English use:** `upstream/content/sets-functions-relations/relations/reflections.tex:60` (OLP-0013, “predicate”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/reflections.tex:64` (OLP-0013, “વિધેય”)
- **Authorities actually checked:** `GU-P024` (GU-VK-TRUTH, {"line_one_based": 126, "utf8_start": 43654, "utf8_end": 44439, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P026` (GU-VK-TRUTH, {"line_one_based": 152, "utf8_start": 54422, "utf8_end": 55596, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Attested philosophical usage; same surface word as function, mathematical roles distinguished by context.
- **Alternatives:** પ્રેડિકેટ — avoided where the Gujarati encyclopaedic source uses contextual વિધેય; function senses are disambiguated by context.
- **Review question:** In Gujarati mathematical-logic prose, does “વિધેય” express “predicate” with the scope stated in this rationale: Attested philosophical usage; same surface word as function, mathematical roles distinguished by context. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T032: identity relation → તાદાત્મ્ય સંબંધ

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:32`.
- **English use:** `upstream/content/sets-functions-relations/relations/relations-as-sets.tex:83` (OLP-0012, “identity relation”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/relations-as-sets.tex:86` (OLP-0012, “તાદાત્મ્ય સંબંધ”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"}); `GU-P025` (GU-VK-TRUTH, {"line_one_based": 128, "utf8_start": 44931, "utf8_end": 46011, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Numerical identity, not similarity/equivalence. English source governs.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “તાદાત્મ્ય સંબંધ” express “identity relation” with the scope stated in this rationale: Numerical identity, not similarity/equivalence. English source governs. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T033: quotient set → ભાગફળ ગણ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:33`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/relations/equivalence-relations.tex:33` (OLP-0015, “ભાગફળ ગણ”)
- **Authorities actually checked:** `GU-P023` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 12, "printed_page": "6"})
- **Chosen sense and rationale:** Set of equivalence classes; canon attests classes but no verified quotient label.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ભાગફળ ગણ” express “quotient set” with the scope stated in this rationale: Set of equivalence classes; canon attests classes but no verified quotient label. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T034: partition → વર્ગ વિભાજન

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:34`.
- **English use:** `upstream/content/sets-functions-relations/relations/equivalence-relations.tex:25` (OLP-0015, “partition”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/equivalence-relations.tex:38` (OLP-0015, “વર્ગ વિભાજન”)
- **Authorities actually checked:** `GU-P023` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 12, "printed_page": "6"})
- **Chosen sense and rationale:** Pairwise disjoint exhaustive classes, not arbitrary overlapping subsets.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “વર્ગ વિભાજન” express “partition” with the scope stated in this rationale: Pairwise disjoint exhaustive classes, not arbitrary overlapping subsets. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T035: binary relation → દ્વિઘટકી સંબંધ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:35`.
- **English use:** `upstream/content/sets-functions-relations/relations/relations-as-sets.tex:55` (OLP-0012, “binary relation”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/relations-as-sets.tex:57` (OLP-0012, “દ્વિઘટકી સંબંધ”)
- **Authorities actually checked:** `GU-P016` (GU-GSSTB-MATH11, {"pdf_page_one_based": 41, "printed_page": "29"})
- **Chosen sense and rationale:** Two-place sense anchored in inspected Cartesian-product definition.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “દ્વિઘટકી સંબંધ” express “binary relation” with the scope stated in this rationale: Two-place sense anchored in inspected Cartesian-product definition. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T036: graph, vertex, edge → આલેખ, શિરોબિંદુ, ધાર

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:36`.
- **English use:** `upstream/content/sets-functions-relations/relations/graphs.tex:12` (OLP-0017, “graph”); `upstream/content/sets-functions-relations/relations/graphs.tex:13` (OLP-0017, “vertex”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/graphs.tex:10` (OLP-0017, “આલેખ”); `gu/content/sets-functions-relations/relations/graphs.tex:13` (OLP-0017, “શિરોબિંદુ”); `gu/content/sets-functions-relations/sets/basics.tex:10` (OLP-0005, “ધાર”)
- **Authorities actually checked:** `GU-P016` (GU-GSSTB-MATH11, {"pdf_page_one_based": 41, "printed_page": "29"}); `GU-P017` (GU-GSSTB-MATH11, {"pdf_page_one_based": 42, "printed_page": "30"})
- **Chosen sense and rationale:** Relation arrow diagrams inspected; these specific graph-theory names not directly attested by acquired passages.
- **Alternatives:** ગ્રાફ / વર્ટેક્સ / એજ — avoided as English transliterations while the descriptive Gujarati terms remain under review.
- **Review question:** In Gujarati mathematical-logic prose, does “આલેખ, શિરોબિંદુ, ધાર” express “graph, vertex, edge” with the scope stated in this rationale: Relation arrow diagrams inspected; these specific graph-theory names not directly attested by acquired passages. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T037: tree/root/branch → વૃક્ષ / મૂળ / શાખા

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:37`.
- **English use:** `upstream/content/sets-functions-relations/relations/trees.tex:13` (OLP-0018, “tree”); `upstream/content/sets-functions-relations/relations/trees.tex:37` (OLP-0018, “root”); `upstream/content/sets-functions-relations/relations/trees.tex:91` (OLP-0018, “branch”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:10` (OLP-0018, “વૃક્ષ”); `gu/content/sets-functions-relations/sets/important-sets.tex:44` (OLP-0007, “મૂળ”); `gu/content/sets-functions-relations/relations/trees.tex:98` (OLP-0018, “શાખા”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"}); `GU-P021` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 10, "printed_page": "4"})
- **Chosen sense and rationale:** Relations and proof prose consulted; graph/set-theoretic tree terminology remains unverified.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “વૃક્ષ / મૂળ / શાખા” express “tree/root/branch” with the scope stated in this rationale: Relations and proof prose consulted; graph/set-theoretic tree terminology remains unverified. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T038: well-ordered / least / maximal chain → સુક્રમિત / લઘુતમ / સમાવેશની દૃષ્ટિએ મહત્તમ શૃંખલા

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:38`.
- **English use:** `upstream/content/sets-functions-relations/relations/trees.tex:46` (OLP-0018, “well-ordered”); `upstream/content/sets-functions-relations/sets/unions-and-intersections.tex:105` (OLP-0008, “least”); `upstream/content/sets-functions-relations/relations/trees.tex:92` (OLP-0018, “maximal chain”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:50` (OLP-0018, “સુક્રમિત”); `gu/content/sets-functions-relations/relations/trees.tex:48` (OLP-0018, “લઘુતમ”); `gu/content/sets-functions-relations/relations/trees.tex:100` (OLP-0018, “સમાવેશની દૃષ્ટિએ મહત્તમ શૃંખલા”)
- **Authorities actually checked:** `GU-P021` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 10, "printed_page": "4"}); `GU-P023` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 12, "printed_page": "6"})
- **Chosen sense and rationale:** Source formal definitions govern; maximal by inclusion distinguished from largest cardinality.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સુક્રમિત / લઘુતમ / સમાવેશની દૃષ્ટિએ મહત્તમ શૃંખલા” express “well-ordered / least / maximal chain” with the scope stated in this rationale: Source formal definitions govern; maximal by inclusion distinguished from largest cardinality. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T039: successor/predecessor → અનુગામી / પુરોગામી

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:39`.
- **English use:** `upstream/content/sets-functions-relations/relations/trees.tex:59` (OLP-0018, “successor”); `upstream/content/sets-functions-relations/relations/trees.tex:63` (OLP-0018, “predecessor”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:61` (OLP-0018, “અનુગામી”); `gu/content/sets-functions-relations/relations/trees.tex:70` (OLP-0018, “પુરોગામી”)
- **Authorities actually checked:** `GU-P018` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 7, "printed_page": "1"})
- **Chosen sense and rationale:** Immediate neighbors in the given ordering, not arbitrary later/earlier nodes.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “અનુગામી / પુરોગામી” express “successor/predecessor” with the scope stated in this rationale: Immediate neighbors in the given ordering, not arbitrary later/earlier nodes. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T040: inverse, restriction, relative product, transitive closure → વ્યસ્ત / મર્યાદન / સાપેક્ષ ગુણાકાર / પરંપરિત સંવરણ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:40`.
- **English use:** `upstream/content/sets-functions-relations/relations/operations.tex:22` (OLP-0019, “inverse”); `upstream/content/sets-functions-relations/relations/operations.tex:28` (OLP-0019, “restriction”); `upstream/content/sets-functions-relations/relations/operations.tex:25` (OLP-0019, “relative product”); `upstream/content/sets-functions-relations/relations/operations.tex:50` (OLP-0019, “transitive closure”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/operations.tex:23` (OLP-0019, “વ્યસ્ત”); `gu/content/sets-functions-relations/relations/operations.tex:29` (OLP-0019, “મર્યાદન”); `gu/content/sets-functions-relations/relations/operations.tex:26` (OLP-0019, “સાપેક્ષ ગુણાકાર”); `gu/content/sets-functions-relations/relations/operations.tex:52` (OLP-0019, “પરંપરિત સંવરણ”)
- **Authorities actually checked:** `GU-P016` (GU-GSSTB-MATH11, {"pdf_page_one_based": 41, "printed_page": "29"}); `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"})
- **Chosen sense and rationale:** Native relation and transitivity senses consulted; compound labels provisional pending specialized canon.
- **Alternatives:** પ્રતિબંધ — not adopted for restriction because મર્યાદન better expresses narrowing in the consulted register.
- **Review question:** In Gujarati mathematical-logic prose, does “વ્યસ્ત / મર્યાદન / સાપેક્ષ ગુણાકાર / પરંપરિત સંવરણ” express “inverse, restriction, relative product, transitive closure” with the scope stated in this rationale: Native relation and transitivity senses consulted; compound labels provisional pending specialized canon. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T041: computability, formula, derivation, completeness → સંગણનીયતા / સૂત્ર / નિષ્પત્તિ / પૂર્ણતા

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:41`.
- **English use:** `upstream/content/sets-functions-relations/relations/trees.tex:126` (OLP-0018, “computability”); `upstream/content/sets-functions-relations/relations/trees.tex:14` (OLP-0018, “formula”); `upstream/content/sets-functions-relations/relations/trees.tex:15` (OLP-0018, “derivation”); `upstream/content/sets-functions-relations/relations/trees.tex:18` (OLP-0018, “completeness”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:138` (OLP-0018, “સંગણનીયતા”); `gu/content/sets-functions-relations/functions/function-basics.tex:93` (OLP-0021, “સૂત્ર”); `gu/content/sets-functions-relations/infinite/dedekinds-proof.tex:54` (OLP-0053, “નિષ્પત્તિ”); `gu/content/sets-functions-relations/relations/trees.tex:19` (OLP-0018, “પૂર્ણતા”)
- **Authorities actually checked:** `GU-P024` (GU-VK-TRUTH, {"line_one_based": 126, "utf8_start": 43654, "utf8_end": 44439, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P026` (GU-VK-TRUTH, {"line_one_based": 152, "utf8_start": 54422, "utf8_end": 55596, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Introductory occurrence in Trees only; logic prose consulted, dedicated technical canon expansion still required.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સંગણનીયતા / સૂત્ર / નિષ્પત્તિ / પૂર્ણતા” express “computability, formula, derivation, completeness” with the scope stated in this rationale: Introductory occurrence in Trees only; logic prose consulted, dedicated technical canon expansion still required. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T042: function / domain / codomain / range → વિધેય / પ્રદેશ / સહપ્રદેશ / વિસ્તાર

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:42`.
- **English use:** `upstream/content/sets-functions-relations/functions/functions.tex:10` (OLP-0020, “function”); `upstream/content/sets-functions-relations/relations/equivalence-relations.tex:24` (OLP-0015, “domain”); `upstream/content/sets-functions-relations/functions/function-basics.tex:32` (OLP-0021, “codomain”); `upstream/content/sets-functions-relations/functions/function-basics.tex:38` (OLP-0021, “range”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/reflections.tex:64` (OLP-0013, “વિધેય”); `gu/content/sets-functions-relations/relations/special-properties.tex:15` (OLP-0014, “પ્રદેશ”); `gu/content/sets-functions-relations/functions/function-basics.tex:33` (OLP-0021, “સહપ્રદેશ”); `gu/content/sets-functions-relations/sets/unions-and-intersections.tex:20` (OLP-0008, “વિસ્તાર”)
- **Authorities actually checked:** `GU-P032` (GU-GSSTB-MATH11, {"pdf_page_one_based": 43, "printed_page": "31"}); `GU-P033` (GU-GSSTB-MATH11, {"pdf_page_one_based": 44, "printed_page": "32"})
- **Chosen sense and rationale:** Function context distinguished from logical predicate; source domain conventions retained.
- **Alternatives:** કાર્ય — not adopted as the primary term because the inspected textbook directly uses વિધેય.
- **Review question:** In Gujarati mathematical-logic prose, does “વિધેય / પ્રદેશ / સહપ્રદેશ / વિસ્તાર” express “function / domain / codomain / range” with the scope stated in this rationale: Function context distinguished from logical predicate; source domain conventions retained. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T043: injective / injection → એક-એક / એક-એક વિધેય

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:43`.
- **English use:** `upstream/content/sets-functions-relations/functions/function-kinds.tex:54` (OLP-0022, “injective”); `upstream/content/sets-functions-relations/functions/function-kinds.tex:67` (OLP-0022, “injection”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/function-kinds.tex:109` (OLP-0022, “એક-એક”); `gu/content/sets-functions-relations/infinite/dedekind-algebra.tex:111` (OLP-0051, “એક-એક વિધેય”)
- **Authorities actually checked:** `GU-P034` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 14, "printed_page": "8"})
- **Chosen sense and rationale:** Both distinct-input and equal-output definitions actually inspected.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “એક-એક / એક-એક વિધેય” express “injective / injection” with the scope stated in this rationale: Both distinct-input and equal-output definitions actually inspected. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T044: surjective / surjection → વ્યાપ્ત / વ્યાપ્ત વિધેય

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:44`.
- **English use:** `upstream/content/sets-functions-relations/functions/function-kinds.tex:18` (OLP-0022, “surjective”); `upstream/content/sets-functions-relations/functions/function-kinds.tex:36` (OLP-0022, “surjection”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/size-of-sets-complete.tex:13` (OLP-0027, “વ્યાપ્ત”); `gu/content/sets-functions-relations/size-of-sets/size-of-sets-complete.tex:13` (OLP-0027, “વ્યાપ્ત વિધેય”)
- **Authorities actually checked:** `GU-P036` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 16, "printed_page": "10"})
- **Chosen sense and rationale:** Every codomain element attained; not just each input assigned.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “વ્યાપ્ત / વ્યાપ્ત વિધેય” express “surjective / surjection” with the scope stated in this rationale: Every codomain element attained; not just each input assigned. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T045: bijective / bijection → એક-એક અને વ્યાપ્ત / એક-એક વ્યાપ્ત વિધેય

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:45`.
- **English use:** `upstream/content/sets-functions-relations/functions/function-kinds.tex:100` (OLP-0022, “bijective”); `upstream/content/sets-functions-relations/functions/function-kinds.tex:101` (OLP-0022, “bijection”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/size-of-sets-complete.tex:15` (OLP-0027, “એક-એક વ્યાપ્ત વિધેય”)
- **Authorities actually checked:** `GU-P036` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 16, "printed_page": "10"}); `GU-P044` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 24, "printed_page": "18"})
- **Chosen sense and rationale:** Conjunction retained; one-to-one correspondence rendered as પરસ્પર એક-એક સંગતતા.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “એક-એક અને વ્યાપ્ત / એક-એક વ્યાપ્ત વિધેય” express “bijective / bijection” with the scope stated in this rationale: Conjunction retained; one-to-one correspondence rendered as પરસ્પર એક-એક સંગતતા. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T046: composition → સંયોજન

- **Status and uncertainty:** `adopted_derivation`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:46`.
- **English use:** `upstream/content/sets-functions-relations/functions/functions.tex:18` (OLP-0020, “composition”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/special-properties.tex:20` (OLP-0014, “સંયોજન”)
- **Authorities actually checked:** `GU-P040` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 20, "printed_page": "14"}); `GU-P041` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 21, "printed_page": "15"})
- **Chosen sense and rationale:** Noun derived from directly attested સંયોજિત વિધેય; order g after f retained.
- **Alternatives:** સંઘટન — not adopted; સંયોજન is derived from the directly attested સંયોજિત વિધેય.
- **Review question:** In Gujarati mathematical-logic prose, does “સંયોજન” express “composition” with the scope stated in this rationale: Noun derived from directly attested સંયોજિત વિધેય; order g after f retained. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T047: inverse function / left inverse / right inverse → પ્રતિવિધેય / ડાબી બાજુનો વ્યસ્ત / જમણી બાજુનો વ્યસ્ત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:47`.
- **English use:** `upstream/content/sets-functions-relations/functions/inverses.tex:57` (OLP-0024, “left inverse”); `upstream/content/sets-functions-relations/functions/inverses.tex:59` (OLP-0024, “right inverse”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/inverses.tex:10` (OLP-0024, “પ્રતિવિધેય”); `gu/content/sets-functions-relations/functions/inverses.tex:67` (OLP-0024, “ડાબી બાજુનો વ્યસ્ત”); `gu/content/sets-functions-relations/functions/inverses.tex:70` (OLP-0024, “જમણી બાજુનો વ્યસ્ત”)
- **Authorities actually checked:** `GU-P042` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 22, "printed_page": "16"}); `GU-P043` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 23, "printed_page": "17"}); `GU-P044` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 24, "printed_page": "18"})
- **Chosen sense and rationale:** Inverse relation stays વ્યસ્ત; function-specific પ્રતિવિધેય now directly attested.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “પ્રતિવિધેય / ડાબી બાજુનો વ્યસ્ત / જમણી બાજુનો વ્યસ્ત” express “inverse function / left inverse / right inverse” with the scope stated in this rationale: Inverse relation stays વ્યસ્ત; function-specific પ્રતિવિધેય now directly attested. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T048: identity function → તદેવ વિધેય

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:48`.
- **English use:** `upstream/content/sets-functions-relations/functions/function-kinds.tex:80` (OLP-0022, “identity function”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/function-kinds.tex:85` (OLP-0022, “તદેવ વિધેય”)
- **Authorities actually checked:** `GU-P042` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 22, "printed_page": "16"}); `GU-P043` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 23, "printed_page": "17"})
- **Chosen sense and rationale:** Function name distinguished from earlier generic identity relation terminology.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “તદેવ વિધેય” express “identity function” with the scope stated in this rationale: Function name distinguished from earlier generic identity relation terminology. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T049: partial function / total function / defined / undefined → આંશિક વિધેય / સર્વત્ર વ્યાખ્યાયિત વિધેય / વ્યાખ્યાયિત / અવ્યાખ્યાયિત

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:49`.
- **English use:** `upstream/content/sets-functions-relations/functions/partial-functions.tex:21` (OLP-0026, “partial function”); `upstream/content/sets-functions-relations/sets/unions-and-intersections.tex:16` (OLP-0008, “defined”); `upstream/content/sets-functions-relations/functions/partial-functions.tex:24` (OLP-0026, “undefined”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/partial-functions.tex:11` (OLP-0026, “આંશિક વિધેય”); `gu/content/first-order-logic/completeness/compactness.tex:143` (OLP-0135, “સર્વત્ર વ્યાખ્યાયિત વિધેય”); `gu/content/sets-functions-relations/sets/unions-and-intersections.tex:16` (OLP-0008, “વ્યાખ્યાયિત”); `gu/content/sets-functions-relations/functions/partial-functions.tex:25` (OLP-0026, “અવ્યાખ્યાયિત”)
- **Authorities actually checked:** `GU-P032` (GU-GSSTB-MATH11, {"pdf_page_one_based": 43, "printed_page": "31"}); `GU-P033` (GU-GSSTB-MATH11, {"pdf_page_one_based": 44, "printed_page": "32"})
- **Chosen sense and rationale:** Only ordinary function terminology directly attested; partial/total computability senses governed by OpenLogic definitions.
- **Alternatives:** પૂર્ણ વિધેય — avoided because “total” here means defined on every ambient input, not completeness.
- **Review question:** In Gujarati mathematical-logic prose, does “આંશિક વિધેય / સર્વત્ર વ્યાખ્યાયિત વિધેય / વ્યાખ્યાયિત / અવ્યાખ્યાયિત” express “partial function / total function / defined / undefined” with the scope stated in this rationale: Only ordinary function terminology directly attested; partial/total computability senses governed by OpenLogic definitions. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T050: argument / value / input / output → દલીલ / કિંમત / આગત / નિર્ગત

- **Status and uncertainty:** `provisional_contextual`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:50`.
- **English use:** `upstream/content/sets-functions-relations/relations/reflections.tex:37` (OLP-0013, “argument”); `upstream/content/sets-functions-relations/functions/function-basics.tex:35` (OLP-0021, “value”); `upstream/content/sets-functions-relations/functions/function-basics.tex:24` (OLP-0021, “input”); `upstream/content/sets-functions-relations/functions/function-basics.tex:19` (OLP-0021, “output”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/reflections.tex:40` (OLP-0013, “દલીલ”); `gu/content/sets-functions-relations/functions/function-basics.tex:36` (OLP-0021, “કિંમત”); `gu/content/sets-functions-relations/functions/function-basics.tex:18` (OLP-0021, “આગત”); `gu/content/sets-functions-relations/functions/function-basics.tex:19` (OLP-0021, “નિર્ગત”)
- **Authorities actually checked:** `GU-P032` (GU-GSSTB-MATH11, {"pdf_page_one_based": 43, "printed_page": "31"}); `GU-P033` (GU-GSSTB-MATH11, {"pdf_page_one_based": 44, "printed_page": "32"})
- **Chosen sense and rationale:** કિંમત attested in function context; input/argument labels remain provisional.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “દલીલ / કિંમત / આગત / નિર્ગત” express “argument / value / input / output” with the scope stated in this rationale: કિંમત attested in function context; input/argument labels remain provisional. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T051: serial relation → સર્વાગત સંબંધ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:51`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Authorities actually checked:** `GU-P032` (GU-GSSTB-MATH11, {"pdf_page_one_based": 43, "printed_page": "31"}); `GU-P033` (GU-GSSTB-MATH11, {"pdf_page_one_based": 44, "printed_page": "32"})
- **Chosen sense and rationale:** Means each source element has a related target; never confused with linear order.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સર્વાગત સંબંધ” express “serial relation” with the scope stated in this rationale: Means each source element has a related target; never confused with linear order. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T052: enumeration → પરિગણના

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:52`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/introduction.tex:21` (OLP-0028, “enumeration”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/size-of-sets-complete.tex:11` (OLP-0027, “પરિગણના”)
- **Authorities actually checked:** `GU-P046` (GU-VK-COUNT, {"line_one_based": 42, "last_line_one_based": 50, "utf8_start": 4564, "utf8_end": 6197, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P034` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 14, "printed_page": "8"}); `GU-P036` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 16, "printed_page": "10"})
- **Chosen sense and rationale:** Direct canon attests countability and bijection, not this enumeration noun. Definition is an exhaustive list/surjection, and alternative variant a bijection.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “પરિગણના” express “enumeration” with the scope stated in this rationale: Direct canon attests countability and bijection, not this enumeration noun. Definition is an exhaustive list/surjection, and alternative variant a bijection. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T053: enumerable/countable; uncountable → ગણનીય; અગણનીય

- **Status and uncertainty:** `adopted_with_scope_distinction`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:53`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/introduction.tex:24` (OLP-0028, “enumerable”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:138` (OLP-0018, “ગણનીય”); `gu/content/sets-functions-relations/size-of-sets/size-of-sets-complete.tex:11` (OLP-0027, “અગણનીય”)
- **Authorities actually checked:** `GU-P046` (GU-VK-COUNT, {"line_one_based": 42, "last_line_one_based": 50, "utf8_start": 4564, "utf8_end": 6197, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P050` (GU-VK-MATH, {"line_one_based": 80, "last_line_one_based": 80, "utf8_start": 39535, "utf8_end": 40685, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Both countable and uncountable directly attested. Canon countable means countably infinite; OpenLogic enumerable includes finite and empty. Preserve OpenLogic scope explicitly.
- **Alternatives:** પરિગણનીય — left open as a possible rendering of the broader OpenLogic “enumerable”; ગણનીય is directly attested but the authority uses a narrower countably-infinite convention.
- **Review question:** In Gujarati mathematical-logic prose, does “ગણનીય; અગણનીય” express “enumerable/countable; uncountable” with the scope stated in this rationale: Both countable and uncountable directly attested. Canon countable means countably infinite; OpenLogic enumerable includes finite and empty. Preserve OpenLogic scope explicitly. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T054: equinumerous sets → સામ્ય ગણો

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:54`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:28` (OLP-0035, “સામ્ય ગણો”)
- **Authorities actually checked:** `GU-P045` (GU-VK-COUNT, {"line_one_based": 25, "last_line_one_based": 29, "utf8_start": 848, "utf8_end": 3636, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P047` (GU-VK-INFINITY, {"line_one_based": 49, "last_line_one_based": 49, "utf8_start": 12140, "utf8_end": 16135, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Same cardinality via bijection; distinct from same members and equivalence classes.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સામ્ય ગણો” express “equinumerous sets” with the scope stated in this rationale: Same cardinality via bijection; distinct from same members and equivalence classes. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T055: cardinality / size → ગણાંક / કદ

- **Status and uncertainty:** `adopted_contextual`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:55`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/size-of-sets-complete.tex:2` (OLP-0027, “size”)
- **Gujarati use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Authorities actually checked:** `GU-P047` (GU-VK-INFINITY, {"line_one_based": 49, "last_line_one_based": 49, "utf8_start": 12140, "utf8_end": 16135, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P048` (GU-VK-INFINITY, {"line_one_based": 57, "last_line_one_based": 80, "utf8_start": 16162, "utf8_end": 20186, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Avoid ગણનીયતા as cardinality because reserved for countability; ગણાંક directly attested.
- **Alternatives:** કાર્ડિનાલિટી — avoided as an unexplained English borrowing; ગણાંક is directly supported and કદ remains contextual prose.
- **Review question:** In Gujarati mathematical-logic prose, does “ગણાંક / કદ” express “cardinality / size” with the scope stated in this rationale: Avoid ગણનીયતા as cardinality because reserved for countability; ગણાંક directly attested. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T056: finite / infinite → સાન્ત / અનંત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:56`.
- **English use:** `upstream/content/sets-functions-relations/sets/important-sets.tex:47` (OLP-0007, “finite”); `upstream/content/sets-functions-relations/sets/important-sets.tex:26` (OLP-0007, “infinite”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/inverses.tex:142` (OLP-0024, “સાન્ત”); `gu/content/sets-functions-relations/sets/important-sets.tex:25` (OLP-0007, “અનંત”)
- **Authorities actually checked:** `GU-P049` (GU-VK-SETS, {"line_one_based": 46, "last_line_one_based": 46, "utf8_start": 6583, "utf8_end": 9817, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P046` (GU-VK-COUNT, {"line_one_based": 42, "last_line_one_based": 50, "utf8_start": 4564, "utf8_end": 6197, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Keep previously adopted spelling સાન્ત even when source writes સાંત.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સાન્ત / અનંત” express “finite / infinite” with the scope stated in this rationale: Keep previously adopted spelling સાન્ત even when source writes સાંત. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T057: ceiling function → ઊર્ધ્વ પૂર્ણાંક વિધેય

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:57`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Authorities actually checked:** `GU-P033` (GU-GSSTB-MATH11, {"pdf_page_one_based": 44, "printed_page": "32"}); `GU-P038` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 18, "printed_page": "12"})
- **Chosen sense and rationale:** Least integer at least x; source explanatory rounding-up definition governs.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ઊર્ધ્વ પૂર્ણાંક વિધેય” express “ceiling function” with the scope stated in this rationale: Least integer at least x; source explanatory rounding-up definition governs. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T058: recursive definition / induction / initial segment → પુનરાવર્તી વ્યાખ્યા / અનુમાનપ્રવર્તન / આરંભખંડ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:58`.
- **English use:** `upstream/content/sets-functions-relations/sets/pairs-and-products.tex:72` (OLP-0009, “recursive definition”); `upstream/content/sets-functions-relations/sets/pairs-and-products.tex:111` (OLP-0009, “induction”); `upstream/content/sets-functions-relations/relations/orders.tex:77` (OLP-0016, “initial segment”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/pairs-and-products.tex:74` (OLP-0009, “પુનરાવર્તી વ્યાખ્યા”); `gu/content/sets-functions-relations/size-of-sets/size-of-sets-complete.tex:48` (OLP-0027, “આરંભખંડ”)
- **Authorities actually checked:** `GU-P041` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 21, "printed_page": "15"}); `GU-P046` (GU-VK-COUNT, {"line_one_based": 42, "last_line_one_based": 50, "utf8_start": 4564, "utf8_end": 6197, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Proof-language and initial-segment set displayed in native sources; no exact direct technical attestation for these labels claimed.
- **Alternatives:** અનુમાનપ્રવર્તન — superseded for mathematical induction by directly attested ગાણિતિક અનુમાન; retained only as a reconstructed earlier choice.
- **Review question:** In Gujarati mathematical-logic prose, does “પુનરાવર્તી વ્યાખ્યા / અનુમાનપ્રવર્તન / આરંભખંડ” express “recursive definition / induction / initial segment” with the scope stated in this rationale: Proof-language and initial-segment set displayed in native sources; no exact direct technical attestation for these labels claimed. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T059: diagonalization / zig-zag / pairing function → વિકર્ણ પદ્ધતિ / આડીઅવળી રીત / જોડ-નિરૂપણ વિધેય

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:59`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/non-enumerability.tex:140` (OLP-0033, “diagonalization”); `upstream/content/sets-functions-relations/size-of-sets/size-of-sets-complete.tex:21` (OLP-0027, “zig-zag”); `upstream/content/sets-functions-relations/size-of-sets/pairing.tex:51` (OLP-0031, “pairing function”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/non-enumerability.tex:40` (OLP-0033, “વિકર્ણ પદ્ધતિ”); `gu/content/sets-functions-relations/size-of-sets/zig-zag.tex:11` (OLP-0030, “આડીઅવળી રીત”); `gu/content/sets-functions-relations/size-of-sets/pairing.tex:10` (OLP-0031, “જોડ-નિરૂપણ વિધેય”)
- **Authorities actually checked:** `GU-P048` (GU-VK-INFINITY, {"line_one_based": 57, "last_line_one_based": 80, "utf8_start": 16162, "utf8_end": 20186, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P034` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 14, "printed_page": "8"}); `GU-P036` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 16, "printed_page": "10"})
- **Chosen sense and rationale:** Native prose refers to diagonalization but leaves English term; proof mechanism remains source-authoritative.
- **Alternatives:** ઝિગઝૅગ — not adopted as the main term; આડીઅવળી રીત describes the traversal but remains provisional.
- **Review question:** In Gujarati mathematical-logic prose, does “વિકર્ણ પદ્ધતિ / આડીઅવળી રીત / જોડ-નિરૂપણ વિધેય” express “diagonalization / zig-zag / pairing function” with the scope stated in this rationale: Native prose refers to diagonalization but leaves English term; proof mechanism remains source-authoritative. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T060: mathematical induction → ગાણિતિક અનુમાન

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:60`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/sets/pairs-and-products.tex:114` (OLP-0009, “ગાણિતિક અનુમાન”)
- **Authorities actually checked:** `GU-P051` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 98, "printed_page": "88"}); `GU-P052` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 100, "printed_page": "90"}); `GU-P053` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 101, "printed_page": "91"})
- **Chosen sense and rationale:** Exact textbook chapter title, principle and worked proof inspected. Supersedes provisional induction component of GU-T058; base case and induction step essential.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ગાણિતિક અનુમાન” express “mathematical induction” with the scope stated in this rationale: Exact textbook chapter title, principle and worked proof inspected. Supersedes provisional induction component of GU-T058; base case and induction step essential. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T061: truth-functional / truth table → સત્યતાફલનલક્ષી / સત્યાર્થતા સારણી

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:61`.
- **English use:** `upstream/content/propositional-logic/propositional-logic.tex:22` (OLP-0055, “truth-functional”); `upstream/content/propositional-logic/syntax-and-semantics/valuations-sat.tex:130` (OLP-0061, “truth table”)
- **Gujarati use:** `gu/content/propositional-logic/propositional-logic.tex:18` (OLP-0055, “સત્યતાફલનલક્ષી”); `gu/content/propositional-logic/syntax-and-semantics/valuations-sat.tex:61` (OLP-0061, “સત્યાર્થતા સારણી”)
- **Authorities actually checked:** `GU-P065` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 5, "last_line_one_based": 5, "utf8_start": 6117, "utf8_end": 8867, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P069` (GU-VK-TRUTH, {"line_one_based": 96, "last_line_one_based": 101, "utf8_start": 36552, "utf8_end": 38930, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Both labels are directly attested in the checked mathematical-logic and truth passages; this supersedes the earlier provisional compounds.
- **Alternatives:** ટ્રુથ ટેબલ — avoided as an English transliteration; exact Gujarati compound was not directly attested.
- **Review question:** In Gujarati mathematical-logic prose, does “સત્યતાફલનલક્ષી / સત્યાર્થતા સારણી” express “truth-functional / truth table” with the scope stated in this rationale: Both labels are directly attested in the checked mathematical-logic and truth passages; this supersedes the earlier provisional compounds. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T062: encode / decode / code → સંકેતબદ્ધ કરવું / સંકેત ઉકેલવો / સંકેતસંખ્યા

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:62`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/pairing.tex:59` (OLP-0031, “encode”); `upstream/content/sets-functions-relations/size-of-sets/pairing.tex:62` (OLP-0031, “decode”); `upstream/content/sets-functions-relations/size-of-sets/pairing.tex:55` (OLP-0031, “code”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/pairing-alt.tex:119` (OLP-0032, “સંકેતબદ્ધ કરવું”); `gu/content/sets-functions-relations/size-of-sets/pairing.tex:10` (OLP-0031, “સંકેતસંખ્યા”)
- **Authorities actually checked:** `GU-P034` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 14, "printed_page": "8"}); `GU-P036` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 16, "printed_page": "10"}); `GU-P047` (GU-VK-INFINITY, {"line_one_based": 49, "last_line_one_based": 49, "utf8_start": 12140, "utf8_end": 16135, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Injective numerical representation of pairs; inverse interpreted on attained range.
- **Alternatives:** કોડ / ડિકોડ — avoided as unexplained English borrowings; the descriptive verbs remain provisional.
- **Review question:** In Gujarati mathematical-logic prose, does “સંકેતબદ્ધ કરવું / સંકેત ઉકેલવો / સંકેતસંખ્યા” express “encode / decode / code” with the scope stated in this rationale: Injective numerical representation of pairs; inverse interpreted on attained range. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T063: cofinite → સહસાન્ત

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:63`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/pairing.tex:92` (OLP-0031, “cofinite”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/pairing.tex:101` (OLP-0031, “સહસાન્ત”)
- **Authorities actually checked:** `GU-P049` (GU-VK-SETS, {"line_one_based": 46, "last_line_one_based": 46, "utf8_start": 6583, "utf8_end": 9817, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P003` (GU-GSSTB-MATH11, {"pdf_page_one_based": 22, "printed_page": "10"})
- **Chosen sense and rationale:** Complement finite in the specified ambient set. Source faulty introductory wording retained and flagged.
- **Alternatives:** કો-ફાઇનાઇટ — avoided as an English transliteration; સહસાન્ત is a transparent construction awaiting expert confirmation.
- **Review question:** In Gujarati mathematical-logic prose, does “સહસાન્ત” express “cofinite” with the scope stated in this rationale: Complement finite in the specified ambient set. Source faulty introductory wording retained and flagged. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T064: array / row / column / triangular number → સરણિ / હાર / સ્તંભ / ત્રિકોણીય સંખ્યા

- **Status and uncertainty:** `provisional_contextual`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:64`.
- **English use:** `upstream/content/sets-functions-relations/sets/pairs-and-products.tex:98` (OLP-0009, “array”); `upstream/content/sets-functions-relations/size-of-sets/zig-zag.tex:39` (OLP-0030, “row”); `upstream/content/sets-functions-relations/size-of-sets/zig-zag.tex:39` (OLP-0030, “column”); `upstream/content/sets-functions-relations/size-of-sets/pairing.tex:33` (OLP-0031, “triangular number”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/zig-zag.tex:22` (OLP-0030, “સરણિ”); `gu/content/sets-functions-relations/size-of-sets/enumerability.tex:178` (OLP-0029, “હાર”); `gu/content/sets-functions-relations/size-of-sets/zig-zag.tex:40` (OLP-0030, “સ્તંભ”); `gu/content/sets-functions-relations/size-of-sets/pairing.tex:34` (OLP-0031, “ત્રિકોણીય સંખ્યા”)
- **Authorities actually checked:** `GU-P033` (GU-GSSTB-MATH11, {"pdf_page_one_based": 44, "printed_page": "32"}); `GU-P053` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 101, "printed_page": "91"})
- **Chosen sense and rationale:** Textbook tabular and arithmetic proof register consulted; exact technical names not all directly attested.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સરણિ / હાર / સ્તંભ / ત્રિકોણીય સંખ્યા” express “array / row / column / triangular number” with the scope stated in this rationale: Textbook tabular and arithmetic proof register consulted; exact technical names not all directly attested. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T065: reduction / reduce one problem to another → ન્યૂનીકરણ / એક સમસ્યાનું બીજી સમસ્યામાં ન્યૂનીકરણ કરવું

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:65`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/size-of-sets-complete.tex:29` (OLP-0027, “reduction”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/reduction.tex:11` (OLP-0034, “ન્યૂનીકરણ”)
- **Authorities actually checked:** `GU-P034` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 14, "printed_page": "8"}); `GU-P050` (GU-VK-MATH, {"line_one_based": 80, "last_line_one_based": 80, "utf8_start": 39535, "utf8_end": 40685, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked sources support function and countability prose but do not attest the technical proof-method label. ન્યૂનીકરણ transparently expresses transforming one enumeration problem into another; the direction is always stated explicitly.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ન્યૂનીકરણ / એક સમસ્યાનું બીજી સમસ્યામાં ન્યૂનીકરણ કરવું” express “reduction / reduce one problem to another” with the scope stated in this rationale: The checked sources support function and countability prose but do not attest the technical proof-method label. ન્યૂનીકરણ transparently expresses transforming one enumeration problem into another; the direction is always stated explicitly. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T066: equinumerosity → ગણસામ્ય

- **Status and uncertainty:** `adopted_derivation`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:66`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:11` (OLP-0035, “equinumerosity”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex:11` (OLP-0035, “ગણસામ્ય”)
- **Authorities actually checked:** `GU-P045` (GU-VK-COUNT, {"line_one_based": 25, "last_line_one_based": 29, "utf8_start": 848, "utf8_end": 3636, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P047` (GU-VK-INFINITY, {"line_one_based": 49, "last_line_one_based": 49, "utf8_start": 12140, "utf8_end": 16135, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked Gujarati source directly attests સામ્ય ગણો for equinumerous sets. ગણસામ્ય is the concise abstract noun formed from that attested phrase and is used only for the bijection-based equivalence relation.
- **Alternatives:** ગણસામ્યતા — possible abstract-noun variant, but the shorter ગણસામ્ય follows the directly attested phrase સામ્ય ગણો more closely.
- **Review question:** In Gujarati mathematical-logic prose, does “ગણસામ્ય” express “equinumerosity” with the scope stated in this rationale: The checked Gujarati source directly attests સામ્ય ગણો for equinumerous sets. ગણસામ્ય is the concise abstract noun formed from that attested phrase and is used only for the bijection-based equivalence relation. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T067: no larger than / smaller than (cardinal comparison) → મોટો નથી / નાનો

- **Status and uncertainty:** `adopted_descriptive`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:67`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex:27` (OLP-0036, “no larger than”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/comparing-size.tex:26` (OLP-0036, “મોટો નથી”); `gu/content/sets-functions-relations/sets/subsets.tex:13` (OLP-0006, “નાનો”)
- **Authorities actually checked:** `GU-P045` (GU-VK-COUNT, {"line_one_based": 25, "last_line_one_based": 29, "utf8_start": 848, "utf8_end": 3636, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P047` (GU-VK-INFINITY, {"line_one_based": 49, "last_line_one_based": 49, "utf8_start": 12140, "utf8_end": 16135, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The formal injection and non-bijection clauses control the two cardinal comparisons. The plain Gujarati comparative phrases preserve the source distinction and avoid introducing an unattested cardinal-order noun.
- **Alternatives:** ગણાંકમાં ન્યૂન / ચુસ્તપણે ન્યૂન — possible symbolic-register alternatives, but no checked Gujarati authority attested them for cardinal comparison.
- **Review question:** In Gujarati mathematical-logic prose, does “મોટો નથી / નાનો” express “no larger than / smaller than (cardinal comparison)” with the scope stated in this rationale: The formal injection and non-bijection clauses control the two cardinal comparisons. The plain Gujarati comparative phrases preserve the source distinction and avoid introducing an unattested cardinal-order noun. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T068: Schroder-Bernstein theorem → શ્રેડર--બર્નસ્ટાઇન પ્રમેય

- **Status and uncertainty:** `provisional_transliteration`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:68`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/schroder-bernstein.tex:11` (OLP-0037, “શ્રેડર--બર્નસ્ટાઇન પ્રમેય”)
- **Authorities actually checked:** `GU-P045` (GU-VK-COUNT, {"line_one_based": 25, "last_line_one_based": 29, "utf8_start": 848, "utf8_end": 3636, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P047` (GU-VK-INFINITY, {"line_one_based": 49, "last_line_one_based": 49, "utf8_start": 12140, "utf8_end": 16135, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The theorem name is transliterated in Gujarati script and its formal statement controls the meaning. The checked cardinality sources do not attest a Gujarati spelling of either surname.
- **Alternatives:** શ્રોડર--બર્નસ્ટીન — plausible transliteration variant; the adopted spelling remains open because the checked sources do not name the theorem.
- **Review question:** In Gujarati mathematical-logic prose, does “શ્રેડર--બર્નસ્ટાઇન પ્રમેય” express “Schroder-Bernstein theorem” with the scope stated in this rationale: The theorem name is transliterated in Gujarati script and its formal statement controls the meaning. The checked cardinality sources do not attest a Gujarati spelling of either surname. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T069: arithmetization → અંકગણિતીકરણ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:69`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/arithmetization.tex:2` (OLP-0041, “arithmetization”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/arithmetization.tex:2` (OLP-0041, “અંકગણિતીકરણ”)
- **Authorities actually checked:** `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The authority directly describes a logical development of the real number system from natural numbers, but does not attest this chapter-level noun.
- **Alternatives:** અંકગણિતકરણ / સંખ્યાકરણ — possible shorter constructions, but neither was attested in the checked authority.
- **Review question:** In Gujarati mathematical-logic prose, does “અંકગણિતીકરણ” express “arithmetization” with the scope stated in this rationale: The authority directly describes a logical development of the real number system from natural numbers, but does not attest this chapter-level noun. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T070: integer / rational / irrational / real number → પૂર્ણાંક / સંમેય / અસંમેય / વાસ્તવિક સંખ્યા

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:70`.
- **English use:** `upstream/content/sets-functions-relations/sets/basics.tex:79` (OLP-0005, “integer”); `upstream/content/sets-functions-relations/sets/important-sets.tex:32` (OLP-0007, “rational”); `upstream/content/sets-functions-relations/arithmetization/reals.tex:22` (OLP-0044, “irrational”); `upstream/content/sets-functions-relations/arithmetization/reals.tex:82` (OLP-0044, “real number”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/basics.tex:47` (OLP-0005, “પૂર્ણાંક”); `gu/content/sets-functions-relations/sets/important-sets.tex:21` (OLP-0007, “સંમેય”); `gu/content/sets-functions-relations/arithmetization/reals.tex:22` (OLP-0044, “અસંમેય”); `gu/content/sets-functions-relations/sets/important-sets.tex:23` (OLP-0007, “વાસ્તવિક સંખ્યા”)
- **Authorities actually checked:** `GU-P057` (GU-VK-MATH, {"line_one_based": 60, "last_line_one_based": 60, "utf8_start": 29622, "utf8_end": 31947, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P058` (GU-VK-MATH, {"line_one_based": 75, "last_line_one_based": 80, "utf8_start": 36000, "utf8_end": 40685, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P059` (GU-VK-MATH, {"line_one_based": 349, "last_line_one_based": 349, "utf8_start": 107299, "utf8_end": 110083, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** All four number-kind terms occur directly in the checked Gujarati mathematical source.
- **Alternatives:** No rejected alternative is recorded because all four adopted number-kind terms are directly attested.
- **Review question:** In Gujarati mathematical-logic prose, does “પૂર્ણાંક / સંમેય / અસંમેય / વાસ્તવિક સંખ્યા” express “integer / rational / irrational / real number” with the scope stated in this rationale: All four number-kind terms occur directly in the checked Gujarati mathematical source. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T071: ring / field → મંડળ / ક્ષેત્ર

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:71`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:21` (OLP-0047, “ring”); `upstream/content/sets-functions-relations/arithmetization/reflections.tex:20` (OLP-0046, “field”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:11` (OLP-0047, “મંડળ”); `gu/content/sets-functions-relations/arithmetization/reals.tex:17` (OLP-0044, “ક્ષેત્ર”)
- **Authorities actually checked:** `GU-P057` (GU-VK-MATH, {"line_one_based": 60, "last_line_one_based": 60, "utf8_start": 29622, "utf8_end": 31947, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Both algebraic-structure terms are directly paired with the English terms and explained in context.
- **Alternatives:** વલય — a possible Sanskrit-derived rendering of ring, but the checked Gujarati mathematical authority directly pairs મંડળ with ring.
- **Review question:** In Gujarati mathematical-logic prose, does “મંડળ / ક્ષેત્ર” express “ring / field” with the scope stated in this rationale: Both algebraic-structure terms are directly paired with the English terms and explained in context. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T072: commutative / commutative ring → સમક્રમી / સમક્રમી મંડળ

- **Status and uncertainty:** `adopted_derivation`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:72`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:21` (OLP-0047, “commutative”); `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:21` (OLP-0047, “commutative ring”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:20` (OLP-0047, “સમક્રમી”); `gu/content/sets-functions-relations/arithmetization/checking-details.tex:24` (OLP-0047, “સમક્રમી મંડળ”)
- **Authorities actually checked:** `GU-P057` (GU-VK-MATH, {"line_one_based": 60, "last_line_one_based": 60, "utf8_start": 29622, "utf8_end": 31947, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P061` (GU-VK-GROUPS, {"line_one_based": 49, "last_line_one_based": 54, "utf8_start": 4551, "utf8_end": 5785, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** સમક્રમી is directly defined by a*b=b*a for groups; its use with the directly attested મંડળ is a transparent algebraic derivation.
- **Alternatives:** ક્રમવિનિમેય — possible descriptive alternative, but સમક્રમી is directly defined by the commutative law in the checked authority.
- **Review question:** In Gujarati mathematical-logic prose, does “સમક્રમી / સમક્રમી મંડળ” express “commutative / commutative ring” with the scope stated in this rationale: સમક્રમી is directly defined by a*b=b*a for groups; its use with the directly attested મંડળ is a transparent algebraic derivation. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T073: associativity / commutativity / distributivity → સંગઠિતતા / સમક્રમિતા / વિતરણાત્મકતા

- **Status and uncertainty:** `provisional_external_glossary_lead`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:73`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:26` (OLP-0047, “associativity”); `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:28` (OLP-0047, “commutativity”); `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:33` (OLP-0047, “distributivity”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:27` (OLP-0047, “સંગઠિતતા”); `gu/content/sets-functions-relations/arithmetization/checking-details.tex:29` (OLP-0047, “સમક્રમિતા”); `gu/content/sets-functions-relations/arithmetization/checking-details.tex:34` (OLP-0047, “વિતરણાત્મકતા”)
- **Authorities actually checked:** `GU-P057` (GU-VK-MATH, {"line_one_based": 60, "last_line_one_based": 60, "utf8_start": 29622, "utf8_end": 31947, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P061` (GU-VK-GROUPS, {"line_one_based": 49, "last_line_one_based": 54, "utf8_start": 4551, "utf8_end": 5785, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The local authority explains associativity using જૂથ and directly supports સમક્રમી. The chosen abstract nouns follow the official CSTT mathematics glossary search result, whose full PDF could not be locally acquired, so this decision remains open.
- **Alternatives:** સંયોગિતા / ક્રમવિનિમેયતા — possible alternatives; the official glossary search lead and local algebraic context favor the recorded forms pending full-source acquisition.
- **Review question:** In Gujarati mathematical-logic prose, does “સંગઠિતતા / સમક્રમિતા / વિતરણાત્મકતા” express “associativity / commutativity / distributivity” with the scope stated in this rationale: The local authority explains associativity using જૂથ and directly supports સમક્રમી. The chosen abstract nouns follow the official CSTT mathematics glossary search result, whose full PDF could not be locally acquired, so this decision remains open. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T074: ordered ring / ordered field / complete ordered field → ક્રમિત મંડળ / ક્રમિત ક્ષેત્ર / પૂર્ણ ક્રમિત ક્ષેત્ર

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:74`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:112` (OLP-0047, “ordered ring”); `upstream/content/sets-functions-relations/arithmetization/reflections.tex:20` (OLP-0046, “ordered field”); `upstream/content/sets-functions-relations/arithmetization/reflections.tex:20` (OLP-0046, “complete ordered field”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:11` (OLP-0047, “ક્રમિત મંડળ”); `gu/content/sets-functions-relations/arithmetization/reals.tex:17` (OLP-0044, “ક્રમિત ક્ષેત્ર”); `gu/content/sets-functions-relations/arithmetization/reflections.tex:19` (OLP-0046, “પૂર્ણ ક્રમિત ક્ષેત્ર”)
- **Authorities actually checked:** `GU-P057` (GU-VK-MATH, {"line_one_based": 60, "last_line_one_based": 60, "utf8_start": 29622, "utf8_end": 31947, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Compounds preserve the directly attested head nouns મંડળ and ક્ષેત્ર; the order and completeness modifiers are controlled by the displayed definitions.
- **Alternatives:** વ્યવસ્થિત મંડળ / વ્યવસ્થિત ક્ષેત્ર — possible alternatives, but ક્રમિત matches the edition-wide term for ordered relations.
- **Review question:** In Gujarati mathematical-logic prose, does “ક્રમિત મંડળ / ક્રમિત ક્ષેત્ર / પૂર્ણ ક્રમિત ક્ષેત્ર” express “ordered ring / ordered field / complete ordered field” with the scope stated in this rationale: Compounds preserve the directly attested head nouns મંડળ and ક્ષેત્ર; the order and completeness modifiers are controlled by the displayed definitions. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T075: upper bound / lower bound / least upper bound / greatest lower bound → ઉચ્ચસીમા / અધઃસીમા / ન્યૂનતમ ઉચ્ચસીમા / મહત્તમ અધઃસીમા

- **Status and uncertainty:** `provisional_external_glossary_lead`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:75`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/reals.tex:74` (OLP-0044, “upper bound”); `upstream/content/sets-functions-relations/arithmetization/cuts.tex:15` (OLP-0045, “lower bound”); `upstream/content/sets-functions-relations/arithmetization/reals.tex:74` (OLP-0044, “least upper bound”); `upstream/content/sets-functions-relations/arithmetization/cuts.tex:15` (OLP-0045, “greatest lower bound”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/reals.tex:80` (OLP-0044, “ઉચ્ચસીમા”); `gu/content/sets-functions-relations/arithmetization/cuts.tex:14` (OLP-0045, “અધઃસીમા”); `gu/content/sets-functions-relations/arithmetization/reals.tex:81` (OLP-0044, “ન્યૂનતમ ઉચ્ચસીમા”); `gu/content/sets-functions-relations/arithmetization/cuts.tex:14` (OLP-0045, “મહત્તમ અધઃસીમા”)
- **Authorities actually checked:** `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The official CSTT mathematics glossary search result supports these forms, but no exact local original was acquired; formal definitions control direction and extremality.
- **Alternatives:** ઉપરિ સીમા / લઘુતમ ઉપરિ સીમા — possible variants; the official glossary search lead supports ઉચ્ચસીમા and ન્યૂનતમ ઉચ્ચસીમા.
- **Review question:** In Gujarati mathematical-logic prose, does “ઉચ્ચસીમા / અધઃસીમા / ન્યૂનતમ ઉચ્ચસીમા / મહત્તમ અધઃસીમા” express “upper bound / lower bound / least upper bound / greatest lower bound” with the scope stated in this rationale: The official CSTT mathematics glossary search result supports these forms, but no exact local original was acquired; formal definitions control direction and extremality. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T076: completeness property → પૂર્ણતા ગુણધર્મ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:76`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/reals.tex:74` (OLP-0044, “completeness property”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/reals.tex:80` (OLP-0044, “પૂર્ણતા ગુણધર્મ”)
- **Authorities actually checked:** `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The compound matches the adopted mathematical register and is governed by the least-upper-bound definition; the checked passage supports real-system and limit language but not the exact label.
- **Alternatives:** સંપૂર્ણતા ગુણધર્મ — possible variant, but પૂર્ણતા is the concise transparent modifier used with the controlling least-upper-bound definition.
- **Review question:** In Gujarati mathematical-logic prose, does “પૂર્ણતા ગુણધર્મ” express “completeness property” with the scope stated in this rationale: The compound matches the adopted mathematical register and is governed by the least-upper-bound definition; the checked passage supports real-system and limit language but not the exact label. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T077: Dedekind cut → ડેડેકિન્ડ કાપ

- **Status and uncertainty:** `provisional_compound`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:77`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/reflections.tex:17` (OLP-0046, “ડેડેકિન્ડ કાપ”)
- **Authorities actually checked:** `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked history directly attests Dedekind's Gujarati name; the mathematical glossary search result supports કાપ for cut, but the full glossary was not locally acquired.
- **Alternatives:** ડેડેકિન્ડ છેદ — possible literal alternative, but the official glossary search lead supports કાપ for this named construction.
- **Review question:** In Gujarati mathematical-logic prose, does “ડેડેકિન્ડ કાપ” express “Dedekind cut” with the scope stated in this rationale: The checked history directly attests Dedekind's Gujarati name; the mathematical glossary search result supports કાપ for cut, but the full glossary was not locally acquired. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T078: Cauchy sequence / convergence / limit → કોશી શ્રેણી / અભિસાર / લક્ષ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:78`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/reflections.tex:29` (OLP-0046, “Cauchy sequence”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:73` (OLP-0048, “limit”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex:11` (OLP-0048, “કોશી શ્રેણી”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:67` (OLP-0048, “લક્ષ”)
- **Authorities actually checked:** `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P062` (GU-VK-CAUCHY, {"line_one_based": 3, "last_line_one_based": 3, "utf8_start": 4658, "utf8_end": 6713, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The exact Cauchy-sequence name and the convergence and limit vocabulary occur directly in checked scholarly Gujarati prose.
- **Alternatives:** કોશી અનુક્રમ / સીમા — possible alternatives; the checked scholarly Gujarati prose directly uses કોશી શ્રેણી, અભિસાર and લક્ષ.
- **Review question:** In Gujarati mathematical-logic prose, does “કોશી શ્રેણી / અભિસાર / લક્ષ” express “Cauchy sequence / convergence / limit” with the scope stated in this rationale: The exact Cauchy-sequence name and the convergence and limit vocabulary occur directly in checked scholarly Gujarati prose. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T079: even / odd → યુગ્મ / અયુગ્મ

- **Status and uncertainty:** `adopted_contextual`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:79`.
- **English use:** `upstream/content/sets-functions-relations/sets/basics.tex:51` (OLP-0005, “even”); `upstream/content/sets-functions-relations/functions/function-basics.tex:130` (OLP-0021, “odd”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/subsets.tex:28` (OLP-0006, “યુગ્મ”); `gu/content/sets-functions-relations/functions/function-basics.tex:145` (OLP-0021, “અયુગ્મ”)
- **Authorities actually checked:** `GU-P058` (GU-VK-MATH, {"line_one_based": 75, "last_line_one_based": 80, "utf8_start": 36000, "utf8_end": 40685, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** યુગ્મ is directly attested for even natural numbers; અયુગ્મ is the established paired opposite already used consistently in the edition.
- **Alternatives:** સમ / વિષમ — familiar alternatives, while the checked mathematical source directly attests યુગ્મ for even and the edition uses its paired opposite અયુગ્મ.
- **Review question:** In Gujarati mathematical-logic prose, does “યુગ્મ / અયુગ્મ” express “even / odd” with the scope stated in this rationale: યુગ્મ is directly attested for even natural numbers; અયુગ્મ is the established paired opposite already used consistently in the edition. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T080: decimal expansion / rational approximation → દશાંશ વિસ્તરણ / સંમેય આસન્ન મૂલ્ય

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:80`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:23` (OLP-0048, “decimal expansion”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/reflections.tex:24` (OLP-0046, “દશાંશ વિસ્તરણ”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:39` (OLP-0048, “સંમેય આસન્ન મૂલ્ય”)
- **Authorities actually checked:** `GU-P058` (GU-VK-MATH, {"line_one_based": 75, "last_line_one_based": 80, "utf8_start": 36000, "utf8_end": 40685, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P062` (GU-VK-CAUCHY, {"line_one_based": 3, "last_line_one_based": 3, "utf8_start": 4658, "utf8_end": 6713, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The number-system and sequence context is directly supported, while these exact compounds remain transparent descriptive choices.
- **Alternatives:** દશાંશ પ્રસાર / સંમેય સન્નિકટન — possible technical variants without exact attestation in the checked passages.
- **Review question:** In Gujarati mathematical-logic prose, does “દશાંશ વિસ્તરણ / સંમેય આસન્ન મૂલ્ય” express “decimal expansion / rational approximation” with the scope stated in this rationale: The number-system and sequence context is directly supported, while these exact compounds remain transparent descriptive choices. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T081: additive inverse / multiplicative inverse / identity element → યોજક વ્યસ્ત / ગુણાકારી વ્યસ્ત / એકમ ઘટક

- **Status and uncertainty:** `adopted_derivation`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:81`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:32` (OLP-0047, “additive inverse”); `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:134` (OLP-0047, “multiplicative inverse”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:33` (OLP-0047, “યોજક વ્યસ્ત”); `gu/content/sets-functions-relations/arithmetization/checking-details.tex:133` (OLP-0047, “ગુણાકારી વ્યસ્ત”)
- **Authorities actually checked:** `GU-P057` (GU-VK-MATH, {"line_one_based": 60, "last_line_one_based": 60, "utf8_start": 29622, "utf8_end": 31947, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P061` (GU-VK-GROUPS, {"line_one_based": 49, "last_line_one_based": 54, "utf8_start": 4551, "utf8_end": 5785, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** એકમ ઘટક and વ્યસ્ત ઘટક are directly attested. The operation-specific modifiers distinguish the two inverse axioms.
- **Alternatives:** યોગાત્મક વ્યસ્ત / ગુણાત્મક વ્યસ્ત / તટસ્થ ઘટક — possible alternatives; the adopted compounds extend directly attested વ્યસ્ત ઘટક and એકમ ઘટક.
- **Review question:** In Gujarati mathematical-logic prose, does “યોજક વ્યસ્ત / ગુણાકારી વ્યસ્ત / એકમ ઘટક” express “additive inverse / multiplicative inverse / identity element” with the scope stated in this rationale: એકમ ઘટક and વ્યસ્ત ઘટક are directly attested. The operation-specific modifiers distinguish the two inverse axioms. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T082: Dedekind infinite → ડેડેકિન્ડ-અનંત

- **Status and uncertainty:** `adopted_derivation`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:82`.
- **English use:** `upstream/content/sets-functions-relations/infinite/hilberts-hotel.tex:61` (OLP-0050, “Dedekind infinite”)
- **Gujarati use:** `gu/content/sets-functions-relations/infinite/hilberts-hotel.tex:59` (OLP-0050, “ડેડેકિન્ડ-અનંત”)
- **Authorities actually checked:** `GU-P048` (GU-VK-INFINITY, {"line_one_based": 57, "last_line_one_based": 80, "utf8_start": 16162, "utf8_end": 20186, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked infinity passage states exactly Dedekind's proper-subset definition of an infinite set. The named compound follows the edition's established Gujarati spelling of Dedekind.
- **Alternatives:** ડેડેકિન્ડીય અનંત — a possible inflected eponym; the hyphenated form keeps the name and defined property visibly separate.
- **Review question:** In Gujarati mathematical-logic prose, does “ડેડેકિન્ડ-અનંત” express “Dedekind infinite” with the scope stated in this rationale: The checked infinity passage states exactly Dedekind's proper-subset definition of an infinite set. The named compound follows the edition's established Gujarati spelling of Dedekind. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T083: closure / f-closed → સંવરણ / f-સંવૃત

- **Status and uncertainty:** `adopted_derivation`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:83`.
- **English use:** `upstream/content/sets-functions-relations/relations/orders.tex:100` (OLP-0016, “closure”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/orders.tex:102` (OLP-0016, “સંવરણ”)
- **Authorities actually checked:** `GU-P057` (GU-VK-MATH, {"line_one_based": 60, "last_line_one_based": 60, "utf8_start": 29622, "utf8_end": 31947, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked algebra passage directly pairs closure with સંવૃતતા. The adjective f-સંવૃત and the set noun સંવરણ preserve that attested root and the edition's earlier transitive-closure usage.
- **Alternatives:** બંધતા / f-બંધ — possible literal alternatives, but they risk collision with topological closedness; the checked algebraic source supports સંવૃતતા and સંવરણ.
- **Review question:** In Gujarati mathematical-logic prose, does “સંવરણ / f-સંવૃત” express “closure / f-closed” with the scope stated in this rationale: The checked algebra passage directly pairs closure with સંવૃતતા. The adjective f-સંવૃત and the set noun સંવરણ preserve that attested root and the edition's earlier transitive-closure usage. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T084: Dedekind algebra → ડેડેકિન્ડ બીજગણિત

- **Status and uncertainty:** `provisional_named_compound`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:84`.
- **English use:** `upstream/content/sets-functions-relations/infinite/dedekind-algebra.tex:82` (OLP-0051, “Dedekind algebra”)
- **Gujarati use:** `gu/content/sets-functions-relations/infinite/dedekind-algebra.tex:10` (OLP-0051, “ડેડેકિન્ડ બીજગણિત”)
- **Authorities actually checked:** `GU-P057` (GU-VK-MATH, {"line_one_based": 60, "last_line_one_based": 60, "utf8_start": 29622, "utf8_end": 31947, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The Gujarati authorities directly support the algebraic-structure register and Dedekind's name, while this exact named structure is a transparent compound not directly attested.
- **Alternatives:** ડેડેકિન્ડ બૈજિક સંરચના — a descriptive alternative, but the source defines a named algebra and the edition already uses બીજગણિત for algebra.
- **Review question:** In Gujarati mathematical-logic prose, does “ડેડેકિન્ડ બીજગણિત” express “Dedekind algebra” with the scope stated in this rationale: The Gujarati authorities directly support the algebraic-structure register and Dedekind's name, while this exact named structure is a transparent compound not directly attested. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T085: parameter → પ્રાચલ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:85`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/infinite/dedekind-induction.tex:38` (OLP-0052, “પ્રાચલ”)
- **Authorities actually checked:** `GU-P063` (GU-VK-VARIABLE, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 4865, "utf8_end": 5737, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The exact Gujarati scholarly passage explicitly pairs પ્રાચલ with parameter and explains its auxiliary-variable role.
- **Alternatives:** પારામિતિ — a possible technical alternative; the checked Gujarati encyclopaedic source explicitly pairs parameter with પ્રાચલ.
- **Review question:** In Gujarati mathematical-logic prose, does “પ્રાચલ” express “parameter” with the scope stated in this rationale: The exact Gujarati scholarly passage explicitly pairs પ્રાચલ with parameter and explains its auxiliary-variable role. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T086: free variable → મુક્ત ચલ

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:86`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/infinite/dedekind-induction.tex:55` (OLP-0052, “મુક્ત ચલ”)
- **Authorities actually checked:** `GU-P063` (GU-VK-VARIABLE, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 4865, "utf8_end": 5737, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The authority directly supports ચલ for variable. The modifier મુક્ત transparently preserves the logical distinction, but the exact compound was not found in the checked passage.
- **Alternatives:** અબદ્ધ ચલ — a plausible alternative without direct attestation in the checked passages; મુક્ત ચલ remains open to specialist correction.
- **Review question:** In Gujarati mathematical-logic prose, does “મુક્ત ચલ” express “free variable” with the scope stated in this rationale: The authority directly supports ચલ for variable. The modifier મુક્ત transparently preserves the logical distinction, but the exact compound was not found in the checked passage. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T087: isomorphism / isomorphic → એકરૂપતા / એકરૂપ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:87`.
- **English use:** `upstream/content/sets-functions-relations/functions/functions.tex:20` (OLP-0020, “isomorphic”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/functions-relations.tex:75` (OLP-0023, “એકરૂપતા”); `gu/content/sets-functions-relations/relations/reflections.tex:62` (OLP-0013, “એકરૂપ”)
- **Authorities actually checked:** `GU-P064` (GU-VK-ALGEBRA, {"line_one_based": 104, "last_line_one_based": 104, "utf8_start": 78692, "utf8_end": 80312, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked algebra article directly pairs એકરૂપતા with isomorphism in a structure-preserving correspondence between algebraic spaces.
- **Alternatives:** સમરૂપતા — a familiar possible alternative; the checked Gujarati algebra article explicitly pairs isomorphism with એકરૂપતા.
- **Review question:** In Gujarati mathematical-logic prose, does “એકરૂપતા / એકરૂપ” express “isomorphism / isomorphic” with the scope stated in this rationale: The checked algebra article directly pairs એકરૂપતા with isomorphism in a structure-preserving correspondence between algebraic spaces. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T088: structuralism / structuralist → સંરચનાવાદ / સંરચનાવાદી

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:88`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/infinite/dedekinds-proof.tex:38` (OLP-0053, “સંરચનાવાદ”); `gu/content/sets-functions-relations/infinite/dedekinds-proof.tex:38` (OLP-0053, “સંરચનાવાદી”)
- **Authorities actually checked:** `GU-P057` (GU-VK-MATH, {"line_one_based": 60, "last_line_one_based": 60, "utf8_start": 29622, "utf8_end": 31947, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P064` (GU-VK-ALGEBRA, {"line_one_based": 104, "last_line_one_based": 104, "utf8_start": 78692, "utf8_end": 80312, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked sources directly support સંરચના and algebraic isomorphism. The philosophical school name is a transparent construction but was not directly attested.
- **Alternatives:** બંધારણવાદ — a possible alternative without direct attestation in the checked sources; સંરચનાવાદ transparently follows સંરચના.
- **Review question:** In Gujarati mathematical-logic prose, does “સંરચનાવાદ / સંરચનાવાદી” express “structuralism / structuralist” with the scope stated in this rationale: The checked sources directly support સંરચના and algebraic isomorphism. The philosophical school name is a transparent construction but was not directly attested. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T089: propositional logic / propositional calculus → વિધાનાત્મક તર્કશાસ્ત્ર / વિધાનોનું કલન

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:89`.
- **English use:** `upstream/content/propositional-logic/propositional-logic.tex:7` (OLP-0055, “propositional logic”)
- **Gujarati use:** `gu/content/propositional-logic/propositional-logic.tex:7` (OLP-0055, “વિધાનાત્મક તર્કશાસ્ત્ર”)
- **Authorities actually checked:** `GU-P067` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 7, "last_line_one_based": 7, "utf8_start": 10292, "utf8_end": 12844, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P068` (GU-VK-TRUTH, {"line_one_based": 82, "last_line_one_based": 83, "utf8_start": 32344, "utf8_end": 34738, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P069` (GU-VK-TRUTH, {"line_one_based": 96, "last_line_one_based": 101, "utf8_start": 36552, "utf8_end": 38930, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Both forms are directly attested in scholarly Gujarati logic prose.
- **Alternatives:** પ્રસ્તાવનાત્મક તર્કશાસ્ત્ર — a plausible literal alternative; the checked scholarly sources directly use વિધાનાત્મક તર્કશાસ્ત્ર and વિધાનોનું કલન.
- **Review question:** In Gujarati mathematical-logic prose, does “વિધાનાત્મક તર્કશાસ્ત્ર / વિધાનોનું કલન” express “propositional logic / propositional calculus” with the scope stated in this rationale: Both forms are directly attested in scholarly Gujarati logic prose. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T090: propositional variable / atomic formula → વિધાનચલ / આણ્વિક સૂત્ર

- **Status and uncertainty:** `adopted_derivation`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:90`.
- **English use:** `upstream/content/propositional-logic/syntax-and-semantics/introduction.tex:14` (OLP-0057, “propositional variable”); `upstream/content/propositional-logic/syntax-and-semantics/formation-sequences.tex:25` (OLP-0060, “atomic formula”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/complete-consistent-sets.tex:39` (OLP-0129, “વિધાનચલ”); `gu/content/propositional-logic/syntax-and-semantics/formulas.tex:111` (OLP-0058, “આણ્વિક સૂત્ર”)
- **Authorities actually checked:** `GU-P065` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 5, "last_line_one_based": 5, "utf8_start": 6117, "utf8_end": 8867, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P067` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 7, "last_line_one_based": 7, "utf8_start": 10292, "utf8_end": 12844, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The sources directly use p, q and r for propositions and આણ્વિક વિધાન for atomic proposition; the formula and variable compounds follow the edition's established સૂત્ર and ચલ.
- **Alternatives:** પ્રસ્તાવચલ / પરમાણ્વીય સૂત્ર — possible alternatives; the adopted compounds preserve the directly checked વિધાન and આણ્વિક usage while matching the edition-wide ચલ and સૂત્ર.
- **Review question:** In Gujarati mathematical-logic prose, does “વિધાનચલ / આણ્વિક સૂત્ર” express “propositional variable / atomic formula” with the scope stated in this rationale: The sources directly use p, q and r for propositions and આણ્વિક વિધાન for atomic proposition; the formula and variable compounds follow the edition's established સૂત્ર and ચલ. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T091: syntax / semantics → વાક્યરચના / અર્થવિચાર

- **Status and uncertainty:** `provisional_contextual`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:91`.
- **English use:** `upstream/content/sets-functions-relations/relations/trees.tex:15` (OLP-0018, “syntax”); `upstream/content/propositional-logic/propositional-logic.tex:25` (OLP-0055, “semantics”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:14` (OLP-0018, “વાક્યરચના”); `gu/content/propositional-logic/syntax-and-semantics/syntax-and-semantics.tex:8` (OLP-0056, “અર્થવિચાર”)
- **Authorities actually checked:** `GU-P024` (GU-VK-TRUTH, {"line_one_based": 126, "utf8_start": 43654, "utf8_end": 44439, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P026` (GU-VK-TRUTH, {"line_one_based": 152, "utf8_start": 54422, "utf8_end": 55596, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P068` (GU-VK-TRUTH, {"line_one_based": 82, "last_line_one_based": 83, "utf8_start": 32344, "utf8_end": 34738, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The semantic side is supported by the Vishwakosh's વાક્યાર્થવિચાર and satisfaction discussion. The paired formal-language syntax label remains a transparent contextual choice.
- **Alternatives:** પદાવલી / અર્થવિજ્ઞાન — possible broader alternatives; વાક્યરચના and અર્થવિચાર keep the formal-string and interpretation roles explicit.
- **Review question:** In Gujarati mathematical-logic prose, does “વાક્યરચના / અર્થવિચાર” express “syntax / semantics” with the scope stated in this rationale: The semantic side is supported by the Vishwakosh's વાક્યાર્થવિચાર and satisfaction discussion. The paired formal-language syntax label remains a transparent contextual choice. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T092: logical connective → તાર્કિક સંયોજક

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:92`.
- **English use:** `upstream/content/first-order-logic/sequent-calculus/proving-things.tex:110` (OLP-0075, “logical connective”)
- **Gujarati use:** `gu/content/propositional-logic/syntax-and-semantics/introduction.tex:57` (OLP-0057, “તાર્કિક સંયોજક”)
- **Authorities actually checked:** `GU-P054` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 319, "printed_page": "309"}); `GU-P065` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 5, "last_line_one_based": 5, "utf8_start": 6117, "utf8_end": 8867, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P069` (GU-VK-TRUTH, {"line_one_based": 96, "last_line_one_based": 101, "utf8_start": 36552, "utf8_end": 38930, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The exact compound appears in the checked truth passage, with સંયોજક independently attested in the textbook.
- **Alternatives:** તર્કીય જોડક — a possible descriptive alternative; the exact checked compound is તાર્કિક સંયોજક.
- **Review question:** In Gujarati mathematical-logic prose, does “તાર્કિક સંયોજક” express “logical connective” with the scope stated in this rationale: The exact compound appears in the checked truth passage, with સંયોજક independently attested in the textbook. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T093: negation / conjunction / disjunction / conditional / biconditional → નિષેધ / સંયોજન / વિયોજન / પ્રેરણ / દ્વિમુખી પ્રેરણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:93`.
- **English use:** `upstream/content/propositional-logic/syntax-and-semantics/formulas.tex:27` (OLP-0058, “negation”); `upstream/content/propositional-logic/syntax-and-semantics/formulas.tex:28` (OLP-0058, “conjunction”); `upstream/content/propositional-logic/syntax-and-semantics/formulas.tex:29` (OLP-0058, “disjunction”); `upstream/content/sets-functions-relations/sets/russells-paradox.tex:21` (OLP-0010, “conditional”); `upstream/content/propositional-logic/syntax-and-semantics/formulas.tex:31` (OLP-0058, “biconditional”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/reflections.tex:52` (OLP-0013, “નિષેધ”); `gu/content/sets-functions-relations/relations/special-properties.tex:20` (OLP-0014, “સંયોજન”); `gu/content/propositional-logic/syntax-and-semantics/formulas.tex:29` (OLP-0058, “વિયોજન”); `gu/content/sets-functions-relations/relations/trees.tex:45` (OLP-0018, “પ્રેરણ”); `gu/content/propositional-logic/syntax-and-semantics/formulas.tex:68` (OLP-0058, “દ્વિમુખી પ્રેરણ”)
- **Authorities actually checked:** `GU-P054` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 319, "printed_page": "309"}); `GU-P055` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 320, "printed_page": "310"}); `GU-P056` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 321, "printed_page": "311"}); `GU-P065` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 5, "last_line_one_based": 5, "utf8_start": 6117, "utf8_end": 8867, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked textbook and mathematical-logic article directly pair these names with the five displayed connectives.
- **Alternatives:** નકાર / જોડાણ / વિકલ્પ / શરતી / દ્વિશરતી — possible classroom-register alternatives; the adopted five names are directly paired with the connectives in the checked source.
- **Review question:** In Gujarati mathematical-logic prose, does “નિષેધ / સંયોજન / વિયોજન / પ્રેરણ / દ્વિમુખી પ્રેરણ” express “negation / conjunction / disjunction / conditional / biconditional” with the scope stated in this rationale: The checked textbook and mathematical-logic article directly pair these names with the five displayed connectives. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T094: inductive definition / induction on formulas → અનુમાનાત્મક વ્યાખ્યા / સૂત્રો પર અનુમાન

- **Status and uncertainty:** `provisional_transferred`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:94`.
- **English use:** `upstream/content/propositional-logic/syntax-and-semantics/introduction.tex:48` (OLP-0057, “inductive definition”)
- **Gujarati use:** `gu/content/propositional-logic/syntax-and-semantics/introduction.tex:46` (OLP-0057, “અનુમાનાત્મક વ્યાખ્યા”); `gu/content/propositional-logic/syntax-and-semantics/syntax-and-semantics.tex:11` (OLP-0056, “સૂત્રો પર અનુમાન”)
- **Authorities actually checked:** `GU-P051` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 98, "printed_page": "88"}); `GU-P052` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 100, "printed_page": "90"}); `GU-P053` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 101, "printed_page": "91"}); `GU-P067` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 7, "last_line_one_based": 7, "utf8_start": 10292, "utf8_end": 12844, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Gujarati mathematical induction is directly attested; its structural use over formulas is an explicit transfer governed by the source definition.
- **Alternatives:** આવર્તક વ્યાખ્યા / રચનાત્મક અનુમાન — possible descriptions; the adopted wording extends directly attested ગાણિતિક અનુમાન to the source-governed structural case.
- **Review question:** In Gujarati mathematical-logic prose, does “અનુમાનાત્મક વ્યાખ્યા / સૂત્રો પર અનુમાન” express “inductive definition / induction on formulas” with the scope stated in this rationale: Gujarati mathematical induction is directly attested; its structural use over formulas is an explicit transfer governed by the source definition. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T095: unique readability / syntactic identity → એકમાત્ર વાચનીયતા / વાક્યરચનાત્મક અભિન્નતા

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:95`.
- **English use:** `upstream/content/propositional-logic/syntax-and-semantics/preliminaries.tex:58` (OLP-0059, “unique readability”); `upstream/content/propositional-logic/syntax-and-semantics/formulas.tex:167` (OLP-0058, “syntactic identity”)
- **Gujarati use:** `gu/content/propositional-logic/syntax-and-semantics/preliminaries.tex:58` (OLP-0059, “એકમાત્ર વાચનીયતા”); `gu/content/propositional-logic/syntax-and-semantics/formulas.tex:168` (OLP-0058, “વાક્યરચનાત્મક અભિન્નતા”)
- **Authorities actually checked:** `GU-P067` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 7, "last_line_one_based": 7, "utf8_start": 10292, "utf8_end": 12844, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The distinction between atomic and compound formal strings is attested, while these exact metalogical labels are transparent descriptions.
- **Alternatives:** અદ્વિતીય પઠનીયતા / સંકેતશ્રેણી અભિન્નતા — possible descriptive alternatives without direct attestation in the checked passages.
- **Review question:** In Gujarati mathematical-logic prose, does “એકમાત્ર વાચનીયતા / વાક્યરચનાત્મક અભિન્નતા” express “unique readability / syntactic identity” with the scope stated in this rationale: The distinction between atomic and compound formal strings is attested, while these exact metalogical labels are transparent descriptions. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T096: formation sequence / uniform substitution → રચના-શ્રેણી / એકરૂપ પ્રતિસ્થાપન

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:96`.
- **English use:** `upstream/content/propositional-logic/syntax-and-semantics/formation-sequences.tex:18` (OLP-0060, “formation sequence”); `upstream/content/propositional-logic/syntax-and-semantics/preliminaries.tex:91` (OLP-0059, “uniform substitution”)
- **Gujarati use:** `gu/content/propositional-logic/syntax-and-semantics/formation-sequences.tex:11` (OLP-0060, “રચના-શ્રેણી”); `gu/content/propositional-logic/syntax-and-semantics/preliminaries.tex:94` (OLP-0059, “એકરૂપ પ્રતિસ્થાપન”)
- **Authorities actually checked:** `GU-P051` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 98, "printed_page": "88"}); `GU-P052` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 100, "printed_page": "90"}); `GU-P067` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 7, "last_line_one_based": 7, "utf8_start": 10292, "utf8_end": 12844, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The choices preserve the source's stepwise construction and identical replacement operation; the exact compounds were not found in the checked canon.
- **Alternatives:** નિર્માણ-અનુક્રમ / સમાન પ્રતિસ્થાપન — possible alternatives; the adopted forms more directly express a sequence of formation steps and uniform replacement.
- **Review question:** In Gujarati mathematical-logic prose, does “રચના-શ્રેણી / એકરૂપ પ્રતિસ્થાપન” express “formation sequence / uniform substitution” with the scope stated in this rationale: The choices preserve the source's stepwise construction and identical replacement operation; the exact compounds were not found in the checked canon. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T097: valuation / evaluation function → સત્યમૂલ્ય-નિયુક્તિ / મૂલ્યાંકન વિધેય

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:97`.
- **English use:** `upstream/content/propositional-logic/propositional-logic.tex:18` (OLP-0055, “valuation”); `upstream/content/propositional-logic/syntax-and-semantics/valuations-sat.tex:22` (OLP-0061, “evaluation function”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/outline.tex:163` (OLP-0128, “સત્યમૂલ્ય-નિયુક્તિ”); `gu/content/propositional-logic/syntax-and-semantics/valuations-sat.tex:22` (OLP-0061, “મૂલ્યાંકન વિધેય”)
- **Authorities actually checked:** `GU-P065` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 5, "last_line_one_based": 5, "utf8_start": 6117, "utf8_end": 8867, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P068` (GU-VK-TRUTH, {"line_one_based": 82, "last_line_one_based": 83, "utf8_start": 32344, "utf8_end": 34738, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P069` (GU-VK-TRUTH, {"line_one_based": 96, "last_line_one_based": 101, "utf8_start": 36552, "utf8_end": 38930, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The sources directly support truth values and truth-functional determination. These labels distinguish the initial assignment from its inductive extension.
- **Alternatives:** મૂલ્યનિર્ધારણ / અર્થઘટન વિધેય — possible alternatives; the adopted pair explicitly distinguishes assignment from its recursively extended evaluation.
- **Review question:** In Gujarati mathematical-logic prose, does “સત્યમૂલ્ય-નિયુક્તિ / મૂલ્યાંકન વિધેય” express “valuation / evaluation function” with the scope stated in this rationale: The sources directly support truth values and truth-functional determination. These labels distinguish the initial assignment from its inductive extension. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T098: satisfaction / satisfiable / unsatisfiable → સંતોષ / સંતોષ્ય / અસંતોષ્ય

- **Status and uncertainty:** `adopted_derivation`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:98`.
- **English use:** `upstream/content/propositional-logic/syntax-and-semantics/introduction.tex:54` (OLP-0057, “satisfaction”); `upstream/content/propositional-logic/syntax-and-semantics/introduction.tex:71` (OLP-0057, “satisfiable”); `upstream/content/propositional-logic/syntax-and-semantics/semantic-notions.tex:19` (OLP-0062, “unsatisfiable”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/orders.tex:159` (OLP-0016, “સંતોષ”); `gu/content/propositional-logic/syntax-and-semantics/introduction.tex:62` (OLP-0057, “સંતોષ્ય”); `gu/content/propositional-logic/syntax-and-semantics/semantic-notions.tex:19` (OLP-0062, “અસંતોષ્ય”)
- **Authorities actually checked:** `GU-P065` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 5, "last_line_one_based": 5, "utf8_start": 6117, "utf8_end": 8867, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P068` (GU-VK-TRUTH, {"line_one_based": 82, "last_line_one_based": 83, "utf8_start": 32344, "utf8_end": 34738, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Formal Gujarati prose directly uses સંતોષે for satisfying axioms and વિધેય-સિદ્ધિ for semantic satisfaction; the adjective pair is a concise derivation kept open for native review.
- **Alternatives:** સિદ્ધિ / સિદ્ધિયોગ્ય / અસિદ્ધિયોગ્ય — possible terminology suggested by related semantic prose; the adopted સંતોષ family is concise but remains open to native review.
- **Review question:** In Gujarati mathematical-logic prose, does “સંતોષ / સંતોષ્ય / અસંતોષ્ય” express “satisfaction / satisfiable / unsatisfiable” with the scope stated in this rationale: Formal Gujarati prose directly uses સંતોષે for satisfying axioms and વિધેય-સિદ્ધિ for semantic satisfaction; the adjective pair is a concise derivation kept open for native review. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T099: tautology / contingent / contradiction → પુનરુક્તિ / નિવાર્ય / વ્યાઘાત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:99`.
- **English use:** `upstream/content/propositional-logic/syntax-and-semantics/introduction.tex:65` (OLP-0057, “tautology”); `upstream/content/propositional-logic/syntax-and-semantics/semantic-notions.tex:22` (OLP-0062, “contingent”); `upstream/content/sets-functions-relations/sets/russells-paradox.tex:51` (OLP-0010, “contradiction”)
- **Gujarati use:** `gu/content/propositional-logic/syntax-and-semantics/introduction.tex:61` (OLP-0057, “પુનરુક્તિ”); `gu/content/propositional-logic/syntax-and-semantics/introduction.tex:23` (OLP-0057, “નિવાર્ય”); `gu/content/first-order-logic/proof-systems/natural-deduction.tex:21` (OLP-0066, “વ્યાઘાત”)
- **Authorities actually checked:** `GU-P066` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 6, "last_line_one_based": 6, "utf8_start": 8867, "utf8_end": 10292, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P071` (GU-VK-WITTGENSTEIN, {"line_one_based": 20, "last_line_one_based": 20, "utf8_start": 24066, "utf8_end": 27691, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The mathematical-logic article explicitly defines પુનરુક્તિ as tautology, and the philosophy article directly distinguishes નિવાર્ય and વ્યાઘાતી propositions.
- **Alternatives:** સર્વસત્ય / પ્રસંગાધીન / વિરોધાભાસ — possible descriptive alternatives; the checked sources directly support પુનરુક્તિ, નિવાર્ય and વ્યાઘાત in the relevant logical senses.
- **Review question:** In Gujarati mathematical-logic prose, does “પુનરુક્તિ / નિવાર્ય / વ્યાઘાત” express “tautology / contingent / contradiction” with the scope stated in this rationale: The mathematical-logic article explicitly defines પુનરુક્તિ as tautology, and the philosophy article directly distinguishes નિવાર્ય and વ્યાઘાતી propositions. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T100: entailment / semantic consequence → તાર્કિક ફલિતતા / અર્થાનુસારી ફલિતતા

- **Status and uncertainty:** `adopted_contextual`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:100`.
- **English use:** `upstream/content/propositional-logic/syntax-and-semantics/introduction.tex:66` (OLP-0057, “entailment”); `upstream/content/first-order-logic/completeness/introduction.tex:18` (OLP-0127, “semantic consequence”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/introduction.tex:17` (OLP-0127, “અર્થાનુસારી ફલિતતા”)
- **Authorities actually checked:** `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The exact passage describes what follows તાર્કિક રીતે from given propositions; અર્થાનુસારી marks the semantic relation when contrast is required.
- **Alternatives:** અનુસરણ / અર્થવિચારી પરિણામ — possible alternatives; ફલિતતા keeps the checked તાર્કિક રીતે ફલિત થવું construction visible.
- **Review question:** In Gujarati mathematical-logic prose, does “તાર્કિક ફલિતતા / અર્થાનુસારી ફલિતતા” express “entailment / semantic consequence” with the scope stated in this rationale: The exact passage describes what follows તાર્કિક રીતે from given propositions; અર્થાનુસારી marks the semantic relation when contrast is required. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T101: local determination / semantic deduction theorem → સ્થાનિક નિર્ધારણ / અર્થાનુસારી નિગમન પ્રમેય

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:101`.
- **English use:** `upstream/content/propositional-logic/syntax-and-semantics/valuations-sat.tex:133` (OLP-0061, “local determination”); `upstream/content/propositional-logic/syntax-and-semantics/semantic-notions.tex:83` (OLP-0062, “semantic deduction theorem”)
- **Gujarati use:** `gu/content/propositional-logic/syntax-and-semantics/valuations-sat.tex:134` (OLP-0061, “સ્થાનિક નિર્ધારણ”); `gu/content/propositional-logic/syntax-and-semantics/semantic-notions.tex:84` (OLP-0062, “અર્થાનુસારી નિગમન પ્રમેય”)
- **Authorities actually checked:** `GU-P065` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 5, "last_line_one_based": 5, "utf8_start": 6117, "utf8_end": 8867, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P069` (GU-VK-TRUTH, {"line_one_based": 96, "last_line_one_based": 101, "utf8_start": 36552, "utf8_end": 38930, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Each component is supported by the truth-value and consequence discussion, while these exact theorem names are not directly attested.
- **Alternatives:** સ્થાનીય નિશ્ચય / અર્થવિચારી નિગમન પ્રમેય — possible variants; the exact theorem compounds remain provisional pending specialist attestation.
- **Review question:** In Gujarati mathematical-logic prose, does “સ્થાનિક નિર્ધારણ / અર્થાનુસારી નિગમન પ્રમેય” express “local determination / semantic deduction theorem” with the scope stated in this rationale: Each component is supported by the truth-value and consequence discussion, while these exact theorem names are not directly attested. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T102: proof / derivation / derivation system / derivable → સાબિતી / નિષ્પત્તિ / નિષ્પત્તિ-તંત્ર / નિષ્પન્ન કરી શકાય એવું

- **Status and uncertainty:** `adopted_derivation`; medium. The head term or its components are supported, but the exact compound or scope remains open to expert correction.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/sets-functions-relations/sets/pairs-and-products.tex:88` (OLP-0009, “proof”); `upstream/content/sets-functions-relations/relations/trees.tex:15` (OLP-0018, “derivation”); `upstream/content/first-order-logic/proof-systems/introduction.tex:53` (OLP-0064, “derivable”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/russells-paradox.tex:56` (OLP-0010, “સાબિતી”); `gu/content/sets-functions-relations/infinite/dedekinds-proof.tex:54` (OLP-0053, “નિષ્પત્તિ”); `gu/content/first-order-logic/natural-deduction/quantifier-rules.tex:101` (OLP-0087, “નિષ્પન્ન કરી શકાય એવું”)
- **Authorities actually checked:** `GU-P072` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 9, "last_line_one_based": 9, "utf8_start": 13274, "utf8_end": 15728, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P073` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 17833, "utf8_end": 19671, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The canon directly uses સાબિતી for finite proof and નિષ્પન્ન for derivation from primitive propositions. The noun નિષ્પત્તિ is already established in this edition; the system compound and modal phrase make the syntactic role explicit.
- **Alternatives:** ઉપપત્તિ / વ્યુત્પત્તિ — possible learned-register alternatives, but neither was found in the checked Gujarati mathematical-logic passages.
- **Review question:** In Gujarati mathematical-logic prose, does ‘સાબિતી / નિષ્પત્તિ / નિષ્પત્તિ-તંત્ર / નિષ્પન્ન કરી શકાય એવું’ accurately express ‘proof / derivation / derivation system / derivable’ with the scope stated here: The canon directly uses સાબિતી for finite proof and નિષ્પન્ન for derivation from primitive propositions. The noun નિષ્પત્તિ is already established in this edition; the system compound and modal phrase make the syntactic role explicit. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T103: axiom / axiomatic derivation / axiom schema / axiom system → સ્વયંસિદ્ધિ / સ્વયંસિદ્ધિમૂલક નિષ્પત્તિ / સ્વયંસિદ્ધિ-પ્રરૂપ / સ્વયંસિદ્ધિ-તંત્ર

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or scope remains open to expert correction.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/sets-functions-relations/functions/inverses.tex:106` (OLP-0024, “axiom”); `upstream/content/first-order-logic/proof-systems/axiomatic-deduction.tex:67` (OLP-0068, “axiom system”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/reflections.tex:57` (OLP-0013, “સ્વયંસિદ્ધિ”); `gu/content/first-order-logic/axiomatic-deduction/provability-propositional.tex:16` (OLP-0122, “સ્વયંસિદ્ધિમૂલક નિષ્પત્તિ”); `gu/content/first-order-logic/axiomatic-deduction/identity.tex:14` (OLP-0125, “સ્વયંસિદ્ધિ-પ્રરૂપ”); `gu/content/first-order-logic/proof-systems/axiomatic-deduction.tex:35` (OLP-0068, “સ્વયંસિદ્ધિ-તંત્ર”)
- **Authorities actually checked:** `GU-P065` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 5, "last_line_one_based": 5, "utf8_start": 6117, "utf8_end": 8867, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The canon discusses propositions satisfying axioms and a symbolic axiomatic approach; સ્વયંસિદ્ધિ is also already used for the axiom of choice in the edition. The schema compound is a transparent contextual extension.
- **Alternatives:** પૂર્વધારણા / પૂર્વધારણાયુક્ત તંત્ર — directly attested as broader explanatory wording and retained in the rationale, while સ્વયંસિદ્ધિ distinguishes a formal axiom line in these sections.
- **Review question:** In Gujarati mathematical-logic prose, does ‘સ્વયંસિદ્ધિ / સ્વયંસિદ્ધિમૂલક નિષ્પત્તિ / સ્વયંસિદ્ધિ-પ્રરૂપ / સ્વયંસિદ્ધિ-તંત્ર’ accurately express ‘axiom / axiomatic derivation / axiom schema / axiom system’ with the scope stated here: The canon discusses propositions satisfying axioms and a symbolic axiomatic approach; સ્વયંસિદ્ધિ is also already used for the axiom of choice in the edition. The schema compound is a transparent contextual extension. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T104: inference rule / modus ponens → અનુમાન-નિયમ / મોડસ પોનેન્સ

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or scope remains open to expert correction.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/first-order-logic/sequent-calculus/derivations.tex:30` (OLP-0074, “inference rule”); `upstream/content/first-order-logic/proof-systems/axiomatic-deduction.tex:62` (OLP-0068, “modus ponens”)
- **Gujarati use:** `gu/content/first-order-logic/proof-systems/introduction.tex:30` (OLP-0064, “અનુમાન-નિયમ”); `gu/content/first-order-logic/proof-systems/axiomatic-deduction.tex:40` (OLP-0068, “મોડસ પોનેન્સ”)
- **Authorities actually checked:** `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** અનુમાન and its formal validity are directly attested. The international rule name is transliterated and its exact conditional operation is stated in the body.
- **Alternatives:** ફલનિયમ / પૂર્વપક્ષ-સ્થાપન — unattested constructions that would obscure the familiar rule name.
- **Review question:** In Gujarati mathematical-logic prose, does ‘અનુમાન-નિયમ / મોડસ પોનેન્સ’ accurately express ‘inference rule / modus ponens’ with the scope stated here: અનુમાન and its formal validity are directly attested. The international rule name is transliterated and its exact conditional operation is stated in the body. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T105: soundness / sound / unsound → યથાર્થતા / યથાર્થ / અયથાર્થ

- **Status and uncertainty:** `provisional_contextual`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/first-order-logic/proof-systems/introduction.tex:66` (OLP-0064, “soundness”); `upstream/content/first-order-logic/proof-systems/introduction.tex:66` (OLP-0064, “sound”); `upstream/content/first-order-logic/proof-systems/introduction.tex:68` (OLP-0064, “unsound”)
- **Gujarati use:** `gu/content/first-order-logic/proof-systems/introduction.tex:63` (OLP-0064, “યથાર્થતા”); `gu/content/first-order-logic/proof-systems/introduction.tex:63` (OLP-0064, “યથાર્થ”); `gu/content/first-order-logic/proof-systems/introduction.tex:66` (OLP-0064, “અયથાર્થ”)
- **Authorities actually checked:** `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked canon attests logical consequence and formal validity but not a dedicated Gujarati label for the metatheoretic property. યથાર્થતા is defined in place by the exact direction from derivability to entailment.
- **Alternatives:** સાધુતા / ધ્વન્યતા / પ્રમાણભૂતતા — possible specialist calques, none attested in the Gujarati authorities actually checked.
- **Review question:** In Gujarati mathematical-logic prose, does ‘યથાર્થતા / યથાર્થ / અયથાર્થ’ accurately express ‘soundness / sound / unsound’ with the scope stated here: The checked canon attests logical consequence and formal validity but not a dedicated Gujarati label for the metatheoretic property. યથાર્થતા is defined in place by the exact direction from derivability to entailment. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T106: completeness / complete derivation system → પૂર્ણતા / પૂર્ણ નિષ્પત્તિ-તંત્ર

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or scope remains open to expert correction.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/sets-functions-relations/relations/trees.tex:18` (OLP-0018, “completeness”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:19` (OLP-0018, “પૂર્ણતા”)
- **Authorities actually checked:** `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The canon directly describes a consistent system that is not પૂર્ણ and identifies sentences unprovable either way. The abstract noun and derivation-system compound preserve that exact system-level sense.
- **Alternatives:** સંપૂર્ણતા — a possible fuller noun; the edition already consistently uses the concise પૂર્ણતા.
- **Review question:** In Gujarati mathematical-logic prose, does ‘પૂર્ણતા / પૂર્ણ નિષ્પત્તિ-તંત્ર’ accurately express ‘completeness / complete derivation system’ with the scope stated here: The canon directly describes a consistent system that is not પૂર્ણ and identifies sentences unprovable either way. The abstract noun and derivation-system compound preserve that exact system-level sense. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T107: consistency / inconsistent / contradiction → સુસંગતતા / અસુસંગત / વ્યાઘાત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/first-order-logic/proof-systems/introduction.tex:83` (OLP-0064, “consistency”); `upstream/content/sets-functions-relations/sets/russells-paradox.tex:74` (OLP-0010, “inconsistent”); `upstream/content/sets-functions-relations/sets/russells-paradox.tex:51` (OLP-0010, “contradiction”)
- **Gujarati use:** `gu/content/first-order-logic/proof-systems/introduction.tex:80` (OLP-0064, “સુસંગતતા”); `gu/content/first-order-logic/proof-systems/introduction.tex:82` (OLP-0064, “અસુસંગત”); `gu/content/first-order-logic/proof-systems/natural-deduction.tex:21` (OLP-0066, “વ્યાઘાત”)
- **Authorities actually checked:** `GU-P071` (GU-VK-WITTGENSTEIN, {"line_one_based": 20, "last_line_one_based": 20, "utf8_start": 24066, "utf8_end": 27691, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The formal-system canon directly pairs consistency with સુસંગતતા and describes contradictory results; the edition's checked logic canon already supports વ્યાઘાત for contradiction.
- **Alternatives:** સંગતિ / વિસંગતિ — familiar variants, while the exact formal-system passage uses સુસંગતતા.
- **Review question:** In Gujarati mathematical-logic prose, does ‘સુસંગતતા / અસુસંગત / વ્યાઘાત’ accurately express ‘consistency / inconsistent / contradiction’ with the scope stated here: The formal-system canon directly pairs consistency with સુસંગતતા and describes contradictory results; the edition's checked logic canon already supports વ્યાઘાત for contradiction. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T108: sequent / sequent calculus / initial sequent → સિક્વન્ટ / સિક્વન્ટ કલન / આરંભિક સિક્વન્ટ

- **Status and uncertainty:** `provisional_transliteration`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/propositional-logic/propositional-logic.tex:32` (OLP-0055, “sequent”); `upstream/content/first-order-logic/proof-systems/sequent-calculus.tex:13` (OLP-0065, “sequent calculus”); `upstream/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:52` (OLP-0070, “initial sequent”)
- **Gujarati use:** `gu/content/first-order-logic/proof-systems/introduction.tex:40` (OLP-0064, “સિક્વન્ટ”); `gu/content/first-order-logic/proof-systems/introduction.tex:40` (OLP-0064, “સિક્વન્ટ કલન”); `gu/content/first-order-logic/proof-systems/sequent-calculus.tex:24` (OLP-0065, “આરંભિક સિક્વન્ટ”)
- **Authorities actually checked:** `GU-P072` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 9, "last_line_one_based": 9, "utf8_start": 13274, "utf8_end": 15728, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** No checked Gujarati authority names this specialized calculus. The internationally recognizable name is transliterated, while the body immediately defines its two sequence components, separator and initial form.
- **Alternatives:** અનુક્રમ કલન / અનુસરણ-કલન — unattested native constructions that risk confusing a sequent with an ordinary sequence or semantic consequence.
- **Review question:** In Gujarati mathematical-logic prose, does ‘સિક્વન્ટ / સિક્વન્ટ કલન / આરંભિક સિક્વન્ટ’ accurately express ‘sequent / sequent calculus / initial sequent’ with the scope stated here: No checked Gujarati authority names this specialized calculus. The internationally recognizable name is transliterated, while the body immediately defines its two sequence components, separator and initial form. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T109: natural deduction / introduction rule / elimination rule → સ્વાભાવિક નિગમન / પરિચય-નિયમ / નિવારણ-નિયમ

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/first-order-logic/proof-systems/natural-deduction.tex:13` (OLP-0066, “natural deduction”); `upstream/content/first-order-logic/proof-systems/natural-deduction.tex:26` (OLP-0066, “elimination rule”)
- **Gujarati use:** `gu/content/first-order-logic/proof-systems/introduction.tex:39` (OLP-0064, “સ્વાભાવિક નિગમન”); `gu/content/first-order-logic/proof-systems/natural-deduction.tex:25` (OLP-0066, “પરિચય-નિયમ”); `gu/content/first-order-logic/proof-systems/natural-deduction.tex:26` (OLP-0066, “નિવારણ-નિયમ”)
- **Authorities actually checked:** `GU-P072` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 9, "last_line_one_based": 9, "utf8_start": 13274, "utf8_end": 15728, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** નિગમન and inference are supported in the checked canon. The exact system name and paired rule labels are transparent descriptions whose behavior is defined by the examples.
- **Alternatives:** પ્રાકૃતિક નિગમન / પ્રવેશ-નિયમ / નિષ્કાસન-નિયમ — plausible literal variants without direct Gujarati specialist attestation.
- **Review question:** In Gujarati mathematical-logic prose, does ‘સ્વાભાવિક નિગમન / પરિચય-નિયમ / નિવારણ-નિયમ’ accurately express ‘natural deduction / introduction rule / elimination rule’ with the scope stated here: નિગમન and inference are supported in the checked canon. The exact system name and paired rule labels are transparent descriptions whose behavior is defined by the examples. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T110: assumption / discharge / undischarged assumption → ધારણા / નિવૃત્ત કરવું / અનિવૃત્ત ધારણા

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/sets-functions-relations/sets/russells-paradox.tex:64` (OLP-0010, “assumption”); `upstream/content/first-order-logic/proof-systems/natural-deduction.tex:49` (OLP-0066, “discharge”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/russells-paradox.tex:66` (OLP-0010, “ધારણા”); `gu/content/first-order-logic/natural-deduction/proving-things-quant.tex:89` (OLP-0090, “અનિવૃત્ત ધારણા”)
- **Authorities actually checked:** `GU-P073` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 17833, "utf8_end": 19671, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The temporary proof role is explained in full before the technical verb is used. નિવૃત્ત marks that the assumption's scope ends without suggesting that the formula is false.
- **Alternatives:** ધારણા રદ કરવી / ધારણા છોડી દેવી — more conversational variants that can wrongly suggest rejection rather than scope closure.
- **Review question:** In Gujarati mathematical-logic prose, does ‘ધારણા / નિવૃત્ત કરવું / અનિવૃત્ત ધારણા’ accurately express ‘assumption / discharge / undischarged assumption’ with the scope stated here: The temporary proof role is explained in full before the technical verb is used. નિવૃત્ત marks that the assumption's scope ends without suggesting that the formula is false. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T111: proof by cases / indirect proof / conditional proof → કિસ્સાવાર સાબિતી / પરોક્ષ સાબિતી / શરતી સાબિતી

- **Status and uncertainty:** `adopted_derivation`; medium. The head term or its components are supported, but the exact compound or scope remains open to expert correction.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/first-order-logic/proof-systems/natural-deduction.tex:18` (OLP-0066, “proof by cases”); `upstream/content/first-order-logic/proof-systems/natural-deduction.tex:20` (OLP-0066, “indirect proof”); `upstream/content/first-order-logic/proof-systems/natural-deduction.tex:22` (OLP-0066, “conditional proof”)
- **Gujarati use:** `gu/content/first-order-logic/proof-systems/natural-deduction.tex:18` (OLP-0066, “કિસ્સાવાર સાબિતી”); `gu/content/first-order-logic/proof-systems/natural-deduction.tex:20` (OLP-0066, “પરોક્ષ સાબિતી”); `gu/content/first-order-logic/proof-systems/natural-deduction.tex:22` (OLP-0066, “શરતી સાબિતી”)
- **Authorities actually checked:** `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P073` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 17833, "utf8_end": 19671, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** સાબિતી is directly attested and the three modifiers transparently preserve the source's proof patterns, each of which is explicitly explained in the target paragraph.
- **Alternatives:** કિસ્સાઓ દ્વારા સાબિતી — a longer equivalent retained in explanatory prose where needed.
- **Review question:** In Gujarati mathematical-logic prose, does ‘કિસ્સાવાર સાબિતી / પરોક્ષ સાબિતી / શરતી સાબિતી’ accurately express ‘proof by cases / indirect proof / conditional proof’ with the scope stated here: સાબિતી is directly attested and the three modifiers transparently preserve the source's proof patterns, each of which is explicitly explained in the target paragraph. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T112: tableau / truth tree / signed formula / closed tableau → ટેબ્લો / સત્ય-વૃક્ષ / ચિહ્નિત સૂત્ર / બંધ ટેબ્લો

- **Status and uncertainty:** `provisional_transliteration`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/first-order-logic/proof-systems/tableaux.tex:13` (OLP-0067, “tableau”); `upstream/content/first-order-logic/proof-systems/tableaux.tex:16` (OLP-0067, “signed formula”); `upstream/content/first-order-logic/tableaux/provability-consistency.tex:90` (OLP-0106, “closed tableau”)
- **Gujarati use:** `gu/content/first-order-logic/proof-systems/introduction.tex:39` (OLP-0064, “ટેબ્લો”); `gu/content/first-order-logic/proof-systems/introduction.tex:39` (OLP-0064, “સત્ય-વૃક્ષ”); `gu/content/first-order-logic/tableaux/provability-quantifiers.tex:87` (OLP-0108, “ચિહ્નિત સૂત્ર”); `gu/content/first-order-logic/tableaux/propositional-rules.tex:91` (OLP-0100, “બંધ ટેબ્લો”)
- **Authorities actually checked:** `GU-P065` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 5, "last_line_one_based": 5, "utf8_start": 6117, "utf8_end": 8867, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P073` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 17833, "utf8_end": 19671, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked Gujarati sources support truth, formula and finite proof but do not name this proof system. The technical name is transliterated and every structural term is defined in place.
- **Alternatives:** સારણી / અર્થવૃક્ષ — rejected because સારણી is already used for truth table and the source system is conventionally called tableau.
- **Review question:** In Gujarati mathematical-logic prose, does ‘ટેબ્લો / સત્ય-વૃક્ષ / ચિહ્નિત સૂત્ર / બંધ ટેબ્લો’ accurately express ‘tableau / truth tree / signed formula / closed tableau’ with the scope stated here: The checked Gujarati sources support truth, formula and finite proof but do not name this proof system. The technical name is transliterated and every structural term is defined in place. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T113: theorem / provability → પ્રમેય / સાબિત કરી શકાય તેવું

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or scope remains open to expert correction.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex:11` (OLP-0036, “theorem”); `upstream/content/first-order-logic/sequent-calculus/sequent-calculus.tex:39` (OLP-0069, “provability”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:19` (OLP-0018, “પ્રમેય”)
- **Authorities actually checked:** `GU-P073` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 17833, "utf8_end": 19671, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The canon directly uses સાબિત for what can be proved within a system; પ્રમેય is the edition's established mathematical noun. The displayed Proves relation fixes the formal scope.
- **Alternatives:** સિદ્ધેયતા — a concise learned formation without direct attestation in the checked passages.
- **Review question:** In Gujarati mathematical-logic prose, does ‘પ્રમેય / સાબિત કરી શકાય તેવું’ accurately express ‘theorem / provability’ with the scope stated here: The canon directly uses સાબિત for what can be proved within a system; પ્રમેય is the edition's established mathematical noun. The displayed Proves relation fixes the formal scope. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T114: proof-theoretic semantics → સાબિતી-સૈદ્ધાંતિક અર્થવિચાર

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/first-order-logic/proof-systems/natural-deduction.tex:88` (OLP-0066, “proof-theoretic semantics”)
- **Gujarati use:** `gu/content/first-order-logic/proof-systems/natural-deduction.tex:85` (OLP-0066, “સાબિતી-સૈદ્ધાંતિક અર્થવિચાર”)
- **Authorities actually checked:** `GU-P073` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 17833, "utf8_end": 19671, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The compound joins the directly attested proof vocabulary to the edition's established term for semantics; the source's parenthetical context controls the philosophical sense.
- **Alternatives:** ઉપપત્તિશાસ્ત્રીય અર્થવિજ્ઞાન — a possible specialist formation not found in the Gujarati canon checked for this batch.
- **Review question:** In Gujarati mathematical-logic prose, does ‘સાબિતી-સૈદ્ધાંતિક અર્થવિચાર’ accurately express ‘proof-theoretic semantics’ with the scope stated here: The compound joins the directly attested proof vocabulary to the edition's established term for semantics; the source's parenthetical context controls the philosophical sense. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T115: resolution method / resolution refutation → રિઝોલ્યૂશન પદ્ધતિ / રિઝોલ્યૂશન વડે ખંડન

- **Status and uncertainty:** `provisional_transliteration`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_proof_systems_translation; `work/record_proof_systems_terms.py`.
- **English use:** `upstream/content/first-order-logic/proof-systems/introduction.tex:43` (OLP-0064, “resolution method”)
- **Gujarati use:** `gu/content/first-order-logic/proof-systems/introduction.tex:53` (OLP-0064, “રિઝોલ્યૂશન વડે ખંડન”)
- **Authorities actually checked:** `GU-P072` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 9, "last_line_one_based": 9, "utf8_start": 13274, "utf8_end": 15728, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** No checked Gujarati authority names the automated proof method. The conventional technical name is transliterated and the operation is identified as a method or refutation in context.
- **Alternatives:** નિરાકરણ પદ્ધતિ — potentially confused with elimination rules and not attested for resolution in the checked sources.
- **Review question:** In Gujarati mathematical-logic prose, does ‘રિઝોલ્યૂશન પદ્ધતિ / રિઝોલ્યૂશન વડે ખંડન’ accurately express ‘resolution method / resolution refutation’ with the scope stated here: No checked Gujarati authority names the automated proof method. The conventional technical name is transliterated and the operation is identified as a method or refutation in context. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T116: antecedent / succedent → પૂર્વાંગ / ઉત્તરાંગ

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_sequent_calculus_translation; `work/record_sequent_terms.py`.
- **English use:** `upstream/content/first-order-logic/proof-systems/natural-deduction.tex:24` (OLP-0066, “antecedent”); `upstream/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:25` (OLP-0070, “succedent”)
- **Gujarati use:** `gu/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:24` (OLP-0070, “પૂર્વાંગ”); `gu/content/first-order-logic/sequent-calculus/rules-and-proofs.tex:25` (OLP-0070, “ઉત્તરાંગ”)
- **Authorities actually checked:** `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The paired compounds mark the before/after sides of a sequent without conflating them with the premise and conclusion of an inference. Checked Gujarati sources attest the neighboring premise/conclusion contrast, but not these exact side labels.
- **Alternatives:** પૂર્વપક્ષ / ઉત્તરપક્ષ — a viable learned pair, but potentially confused with positions in philosophical debate rather than the two sides of a formal sequent.
- **Review question:** Please double-check whether ‘પૂર્વાંગ / ઉત્તરાંગ’ accurately expresses ‘antecedent / succedent’ in Gujarati mathematical-logic prose with this scope: The paired compounds mark the before/after sides of a sequent without conflating them with the premise and conclusion of an inference. Checked Gujarati sources attest the neighboring premise/conclusion contrast, but not these exact side labels. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T117: premise / conclusion / end-sequent → આધાર-સિક્વન્ટ / ફલિત-સિક્વન્ટ / અંતિમ સિક્વન્ટ

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or proof-theoretic scope remains open to expert correction.
- **Record origin:** contemporaneous_sequent_calculus_translation; `work/record_sequent_terms.py`.
- **English use:** `upstream/content/first-order-logic/proof-systems/natural-deduction.tex:19` (OLP-0066, “premise”); `upstream/content/first-order-logic/proof-systems/sequent-calculus.tex:29` (OLP-0065, “conclusion”); `upstream/content/first-order-logic/sequent-calculus/derivations.tex:33` (OLP-0074, “end-sequent”)
- **Gujarati use:** `gu/content/first-order-logic/sequent-calculus/derivations.tex:29` (OLP-0074, “આધાર-સિક્વન્ટ”); `gu/content/first-order-logic/sequent-calculus/derivations.tex:29` (OLP-0074, “ફલિત-સિક્વન્ટ”); `gu/content/first-order-logic/sequent-calculus/derivations.tex:32` (OLP-0074, “અંતિમ સિક્વન્ટ”)
- **Authorities actually checked:** `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** આધારવિધાન and ફલિતવિધાન are directly attested for premise and conclusion. The edition carries those heads into the sequent compounds and uses અંતિમ for the bottom sequent of a finished derivation.
- **Alternatives:** ઉપરનું સિક્વન્ટ / નીચલું સિક્વન્ટ — useful spatial descriptions, but they do not express the inference roles as precisely.
- **Review question:** Please double-check whether ‘આધાર-સિક્વન્ટ / ફલિત-સિક્વન્ટ / અંતિમ સિક્વન્ટ’ accurately expresses ‘premise / conclusion / end-sequent’ in Gujarati mathematical-logic prose with this scope: આધારવિધાન and ફલિતવિધાન are directly attested for premise and conclusion. The edition carries those heads into the sequent compounds and uses અંતિમ for the bottom sequent of a finished derivation. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T118: eigenvariable / eigenvariable condition → આઇગનચલ / આઇગનચલ-શરત

- **Status and uncertainty:** `provisional_transliteration`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_sequent_calculus_translation; `work/record_sequent_terms.py`.
- **English use:** `upstream/content/first-order-logic/sequent-calculus/quantifier-rules.tex:30` (OLP-0072, “eigenvariable”); `upstream/content/first-order-logic/sequent-calculus/quantifier-rules.tex:54` (OLP-0072, “eigenvariable condition”)
- **Gujarati use:** `gu/content/first-order-logic/sequent-calculus/quantifier-rules.tex:30` (OLP-0072, “આઇગનચલ”); `gu/content/first-order-logic/sequent-calculus/quantifier-rules.tex:53` (OLP-0072, “આઇગનચલ-શરત”)
- **Authorities actually checked:** `GU-P067` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 7, "last_line_one_based": 7, "utf8_start": 10292, "utf8_end": 12844, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P077` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 2, "last_line_one_based": 2, "utf8_start": 1405, "utf8_end": 3561, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** No checked Gujarati authority names this proof-theoretic device. The conventional technical stem is transliterated, joined transparently to ચલ, and immediately defined by its freshness condition; the source's own note says its object is formally a constant here.
- **Alternatives:** વિશિષ્ટ ચલ — readable but too general and liable to hide the freshness condition.; મુક્ત અચળ — describes part of the rule behavior but would replace the conventional name and conflict with the source's explicit terminology note.
- **Review question:** Please double-check whether ‘આઇગનચલ / આઇગનચલ-શરત’ accurately expresses ‘eigenvariable / eigenvariable condition’ in Gujarati mathematical-logic prose with this scope: No checked Gujarati authority names this proof-theoretic device. The conventional technical stem is transliterated, joined transparently to ચલ, and immediately defined by its freshness condition; the source's own note says its object is formally a constant here. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T119: weakening / contraction / exchange / cut → શિથિલીકરણ / સંકોચન / અદલાબદલી / કટ

- **Status and uncertainty:** `provisional_mixed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_sequent_calculus_translation; `work/record_sequent_terms.py`.
- **English use:** `upstream/content/first-order-logic/proof-systems/sequent-calculus.tex:55` (OLP-0065, “weakening”); `upstream/content/first-order-logic/sequent-calculus/structural-rules.tex:37` (OLP-0073, “contraction”); `upstream/content/first-order-logic/sequent-calculus/structural-rules.tex:18` (OLP-0073, “exchange”); `upstream/content/sets-functions-relations/arithmetization/cuts.tex:18` (OLP-0045, “cut”)
- **Gujarati use:** `gu/content/first-order-logic/sequent-calculus/structural-rules.tex:22` (OLP-0073, “શિથિલીકરણ”); `gu/content/first-order-logic/sequent-calculus/structural-rules.tex:36` (OLP-0073, “સંકોચન”); `gu/content/sets-functions-relations/sets/subsets.tex:45` (OLP-0006, “અદલાબદલી”)
- **Authorities actually checked:** `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The first three names describe the structural effect of each inference. Cut retains the familiar short technical borrowing because Gujarati છેદ already carries established set and geometric senses; every rule is displayed formally, which controls the exact operation.
- **Alternatives:** ક્ષીણીકરણ / સંકુચન / વિનિમય / છેદ — a viable more Sanskritized set, but not attested for sequent rules in the checked sources and છેદ risks a mathematical sense collision.
- **Review question:** Please double-check whether ‘શિથિલીકરણ / સંકોચન / અદલાબદલી / કટ’ accurately expresses ‘weakening / contraction / exchange / cut’ in Gujarati mathematical-logic prose with this scope: The first three names describe the structural effect of each inference. Cut retains the familiar short technical borrowing because Gujarati છેદ already carries established set and geometric senses; every rule is displayed formally, which controls the exact operation. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T120: reflexivity / monotonicity / transitivity / compactness → સ્વવાચકતા / એકદિશવર્ધિતા / પરંપરિતતા / સઘનતા

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or proof-theoretic scope remains open to expert correction.
- **Record origin:** contemporaneous_sequent_calculus_translation; `work/record_sequent_terms.py`.
- **English use:** `upstream/content/sets-functions-relations/relations/special-properties.tex:23` (OLP-0014, “reflexivity”); `upstream/content/propositional-logic/syntax-and-semantics/semantic-notions.tex:54` (OLP-0062, “monotonicity”); `upstream/content/sets-functions-relations/relations/special-properties.tex:28` (OLP-0014, “transitivity”); `upstream/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex:147` (OLP-0077, “compactness”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/special-properties.tex:23` (OLP-0014, “સ્વવાચકતા”); `gu/content/propositional-logic/syntax-and-semantics/semantic-notions.tex:54` (OLP-0062, “એકદિશવર્ધિતા”); `gu/content/sets-functions-relations/relations/special-properties.tex:28` (OLP-0014, “પરંપરિતતા”); `gu/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex:152` (OLP-0077, “સઘનતા”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** સ્વવાચક and પરંપરિત are directly attested relation-property heads and match established edition usage. એકદિશવર્ધિતા is retained from the earlier semantic chapter for monotonic enlargement, while સઘનતા is the established edition-wide mathematical rendering of compactness; the displayed propositions fix each proof-theoretic sense.
- **Alternatives:** સ્વપ્રતિબિંબકતા / એકદિશતા / સંક્રમણતા / સંક્ષિપ્તતા — possible descriptive variants, but they would break established edition terminology or blur the formal property.
- **Review question:** Please double-check whether ‘સ્વવાચકતા / એકદિશવર્ધિતા / પરંપરિતતા / સઘનતા’ accurately expresses ‘reflexivity / monotonicity / transitivity / compactness’ in Gujarati mathematical-logic prose with this scope: સ્વવાચક and પરંપરિત are directly attested relation-property heads and match established edition usage. એકદિશવર્ધિતા is retained from the earlier semantic chapter for monotonic enlargement, while સઘનતા is the established edition-wide mathematical rendering of compactness; the displayed propositions fix each proof-theoretic sense. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T121: identity / substitutability of identicals / Leibniz's law → તાદાત્મ્ય / અભિન્ન વસ્તુઓની પ્રતિસ્થાપનીયતા / લાઇબ્નિત્સનો નિયમ

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or proof-theoretic scope remains open to expert correction.
- **Record origin:** contemporaneous_sequent_calculus_translation; `work/record_sequent_terms.py`.
- **English use:** `upstream/content/sets-functions-relations/sets/basics.tex:85` (OLP-0005, “identity”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/relations-as-sets.tex:17` (OLP-0012, “તાદાત્મ્ય”); `gu/content/first-order-logic/sequent-calculus/identity.tex:43` (OLP-0082, “અભિન્ન વસ્તુઓની પ્રતિસ્થાપનીયતા”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"}); `GU-P025` (GU-VK-TRUTH, {"line_one_based": 128, "utf8_start": 44931, "utf8_end": 46011, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P077` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 2, "last_line_one_based": 2, "utf8_start": 1405, "utf8_end": 3561, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** તાદાત્મ્ય preserves the edition's earlier name for the identity relation. અભિન્ન વસ્તુઓ renders identicals inside the explanatory principle, while the eponym is transliterated and the two displayed equality rules control the formal meaning.
- **Alternatives:** અભિન્નતા — viable for abstract identity and retained in the established phrase વાક્યરચનાત્મક અભિન્નતા, but તાદાત્મ્ય avoids changing the edition's object-level identity-relation terminology.
- **Review question:** Please double-check whether ‘તાદાત્મ્ય / અભિન્ન વસ્તુઓની પ્રતિસ્થાપનીયતા / લાઇબ્નિત્સનો નિયમ’ accurately expresses ‘identity / substitutability of identicals / Leibniz's law’ in Gujarati mathematical-logic prose with this scope: તાદાત્મ્ય preserves the edition's earlier name for the identity relation. અભિન્ન વસ્તુઓ renders identicals inside the explanatory principle, while the eponym is transliterated and the two displayed equality rules control the formal meaning. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T122: quantifier / universal quantifier / existential quantifier → પરિમાણક / સાર્વત્રિક પરિમાણક / અસ્તિત્વલક્ષી પરિમાણક

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** contemporaneous_sequent_calculus_translation; `work/record_sequent_terms.py`.
- **English use:** `upstream/content/first-order-logic/sequent-calculus/sequent-calculus.tex:24` (OLP-0069, “quantifier”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:36` (OLP-0047, “પરિમાણક”)
- **Authorities actually checked:** `GU-P067` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 7, "last_line_one_based": 7, "utf8_start": 10292, "utf8_end": 12844, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked Gujarati mathematical-logic source directly names both quantifier types and explains their ordinary-language readings.
- **Alternatives:** માત્રાસૂચક — not adopted because the checked specialist source directly uses પરિમાણક.
- **Review question:** Please double-check whether ‘પરિમાણક / સાર્વત્રિક પરિમાણક / અસ્તિત્વલક્ષી પરિમાણક’ accurately expresses ‘quantifier / universal quantifier / existential quantifier’ in Gujarati mathematical-logic prose with this scope: The checked Gujarati mathematical-logic source directly names both quantifier types and explains their ordinary-language readings. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T123: closed term / sentence → બંધ પદ / વાક્ય

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or proof-theoretic scope remains open to expert correction.
- **Record origin:** contemporaneous_sequent_calculus_translation; `work/record_sequent_terms.py`.
- **English use:** `upstream/content/first-order-logic/sequent-calculus/quantifier-rules.tex:27` (OLP-0072, “closed term”); `upstream/content/propositional-logic/syntax-and-semantics/introduction.tex:16` (OLP-0057, “sentence”)
- **Gujarati use:** `gu/content/first-order-logic/sequent-calculus/quantifier-rules.tex:27` (OLP-0072, “બંધ પદ”); `gu/content/sets-functions-relations/relations/orders.tex:137` (OLP-0016, “વાક્ય”)
- **Authorities actually checked:** `GU-P067` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 7, "last_line_one_based": 7, "utf8_start": 10292, "utf8_end": 12844, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P077` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 2, "last_line_one_based": 2, "utf8_start": 1405, "utf8_end": 3561, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** વાક્ય is directly supported in logical analysis. બંધ પદ is a transparent compositional rendering of a term with no free variable, and the source supplies that definition at first use.
- **Alternatives:** મુક્તચલવિહોણું પદ — an accurate explanatory expansion, retained in the in-place definition rather than used as the repeating term.
- **Review question:** Please double-check whether ‘બંધ પદ / વાક્ય’ accurately expresses ‘closed term / sentence’ in Gujarati mathematical-logic prose with this scope: વાક્ય is directly supported in logical analysis. બંધ પદ is a transparent compositional rendering of a term with no free variable, and the source supplies that definition at first use. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T124: deduction theorem → નિગમન પ્રમેય

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or proof-theoretic scope remains open to expert correction.
- **Record origin:** contemporaneous_axiomatic_deduction_translation; `work/add_axiomatic_terms.py`.
- **English use:** `upstream/content/propositional-logic/syntax-and-semantics/semantic-notions.tex:83` (OLP-0062, “deduction theorem”)
- **Gujarati use:** `gu/content/propositional-logic/syntax-and-semantics/semantic-notions.tex:84` (OLP-0062, “નિગમન પ્રમેય”)
- **Authorities actually checked:** `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P072` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 9, "last_line_one_based": 9, "utf8_start": 13274, "utf8_end": 15728, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** નિગમન is established in the edition for deduction and the checked canon directly supports formal consequence, derivation from assumptions, system-relative proof and rule-governed reasoning. The displayed biconditional fixes the metatheorem's exact syntactic scope.
- **Alternatives:** નિષ્પત્તિ પ્રમેય — would blur the distinction between a derivation and the theorem that internalizes an added hypothesis.; અનુમાન પ્રમેય — could be confused with an inference rule or mathematical induction.
- **Review question:** In Gujarati mathematical-logic prose, does ‘નિગમન પ્રમેય’ accurately express ‘deduction theorem’ with the scope stated here: નિગમન is established in the edition for deduction and the checked canon directly supports formal consequence, derivation from assumptions, system-relative proof and rule-governed reasoning. The displayed biconditional fixes the metatheorem's exact syntactic scope. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T125: contraposition / ex falso quodlibet / explosion / double negation elimination → પ્રતિપક્ષન / એક્સ ફાલ્સો ક્વોડલિબેટ / વિસ્ફોટ / દ્વિ-નિષેધ નિકાલ

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or proof-theoretic scope remains open to expert correction.
- **Record origin:** contemporaneous_axiomatic_deduction_translation; `work/add_axiomatic_terms.py`.
- **English use:** `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:110` (OLP-0119, “contraposition”); `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:112` (OLP-0119, “ex falso quodlibet”); `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:112` (OLP-0119, “explosion”); `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:114` (OLP-0119, “double negation elimination”)
- **Gujarati use:** `gu/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:115` (OLP-0119, “પ્રતિપક્ષન”); `gu/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:117` (OLP-0119, “એક્સ ફાલ્સો ક્વોડલિબેટ”); `gu/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:117` (OLP-0119, “વિસ્ફોટ”); `gu/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex:119` (OLP-0119, “દ્વિ-નિષેધ નિકાલ”)
- **Authorities actually checked:** `GU-P065` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 5, "last_line_one_based": 5, "utf8_start": 6117, "utf8_end": 8867, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P071` (GU-VK-WITTGENSTEIN, {"line_one_based": 20, "last_line_one_based": 20, "utf8_start": 24066, "utf8_end": 27691, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P073` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 17833, "utf8_end": 19671, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The canon directly attests implication, negation, contradiction, finite proof and formal consequence. પ્રતિપક્ષન and દ્વિ-નિષેધ નિકાલ state the operations compositionally; the traditional Latin label is transliterated beside the descriptive વિસ્ફોટ, and every displayed formula controls the exact rule.
- **Alternatives:** પ્રતિસ્થાપન — rejected because it already denotes substitution rather than contraposition.; વિરોધાભાસમાંથી કંઈપણ — accurate explanatory prose, but less suitable as the compact named rule beside the traditional label.
- **Review question:** In Gujarati mathematical-logic prose, does ‘પ્રતિપક્ષન / એક્સ ફાલ્સો ક્વોડલિબેટ / વિસ્ફોટ / દ્વિ-નિષેધ નિકાલ’ accurately express ‘contraposition / ex falso quodlibet / explosion / double negation elimination’ with the scope stated here: The canon directly attests implication, negation, contradiction, finite proof and formal consequence. પ્રતિપક્ષન and દ્વિ-નિષેધ નિકાલ state the operations compositionally; the traditional Latin label is transliterated beside the descriptive વિસ્ફોટ, and every displayed formula controls the exact rule. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T126: proof-theoretic notions / proof-theoretic property → સાબિતી-સૈદ્ધાંતિક ખ્યાલો / સાબિતી-સૈદ્ધાંતિક ગુણધર્મ

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_axiomatic_deduction_translation; `work/add_axiomatic_terms.py`.
- **English use:** `upstream/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex:18` (OLP-0077, “proof-theoretic notions”)
- **Gujarati use:** `gu/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex:23` (OLP-0077, “સાબિતી-સૈદ્ધાંતિક ખ્યાલો”); `gu/content/first-order-logic/sequent-calculus/soundness.tex:19` (OLP-0081, “સાબિતી-સૈદ્ધાંતિક ગુણધર્મ”)
- **Authorities actually checked:** `GU-P072` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 9, "last_line_one_based": 9, "utf8_start": 13274, "utf8_end": 15728, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P073` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 17833, "utf8_end": 19671, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P077` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 2, "last_line_one_based": 2, "utf8_start": 1405, "utf8_end": 3561, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** સાબિતી, formal systems, derivation from premises and exact symbolic exposition are attested in the checked passages. The compound explicitly marks notions defined through derivability rather than satisfaction, as the surrounding paragraph explains.
- **Alternatives:** ઉપપત્તિશાસ્ત્રીય ખ્યાલ — a possible learned-register compound not found in the checked Gujarati sources.; સિદ્ધાંતાત્મક ગુણધર્મ — too broad because it does not identify proof theory.
- **Review question:** In Gujarati mathematical-logic prose, does ‘સાબિતી-સૈદ્ધાંતિક ખ્યાલો / સાબિતી-સૈદ્ધાંતિક ગુણધર્મ’ accurately express ‘proof-theoretic notions / proof-theoretic property’ with the scope stated here: સાબિતી, formal systems, derivation from premises and exact symbolic exposition are attested in the checked passages. The compound explicitly marks notions defined through derivability rather than satisfaction, as the surrounding paragraph explains. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T127: model / model existence result → નિદર્શ / સંરચના-અસ્તિત્વનું પરિણામ

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or model-theoretic scope remains open to expert correction.
- **Record origin:** contemporaneous_completeness_translation; `work/add_completeness_terms.py`.
- **English use:** `upstream/content/first-order-logic/completeness/compactness-direct.tex:22` (OLP-0136, “model”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/compactness-direct.tex:20` (OLP-0136, “નિદર્શ”)
- **Authorities actually checked:** `GU-P025` (GU-VK-TRUTH, {"line_one_based": 128, "utf8_start": 44931, "utf8_end": 46011, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** નિદર્શ is the established edition term for a structure satisfying a theory, while સંરચના is retained for the underlying interpretation. The checked canon supports logical consequence, formal systems and structure, though the exact model-theoretic compound is contextual rather than directly attested.
- **Alternatives:** મૉડલ — a transparent transliteration, but less integrated with the edition's established Gujarati register.; નિદર્શ-અસ્તિત્વ પરિણામ — concise, but the translated passage deliberately foregrounds existence of a satisfying structure.
- **Review question:** In Gujarati mathematical-logic prose, does ‘નિદર્શ / સંરચના-અસ્તિત્વનું પરિણામ’ accurately express ‘model / model existence result’ with the scope stated here: નિદર્શ is the established edition term for a structure satisfying a theory, while સંરચના is retained for the underlying interpretation. The checked canon supports logical consequence, formal systems and structure, though the exact model-theoretic compound is contextual rather than directly attested. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T128: complete set → પૂર્ણ ગણ

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or model-theoretic scope remains open to expert correction.
- **Record origin:** contemporaneous_completeness_translation; `work/add_completeness_terms.py`.
- **English use:** `upstream/content/first-order-logic/completeness/outline.tex:80` (OLP-0128, “complete set”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/outline.tex:74` (OLP-0128, “પૂર્ણ ગણ”)
- **Authorities actually checked:** `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P077` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 2, "last_line_one_based": 2, "utf8_start": 1405, "utf8_end": 3561, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The canon directly uses પૂર્ણ for a formal system that leaves no sentence undecided. Here the displayed definition fixes the set-level sense: for every sentence, the set contains it or its negation.
- **Alternatives:** સંપૂર્ણ ગણ — possible fuller wording, but the checked formal-system source and established edition usage favor પૂર્ણ.; નિર્ણાયક ગણ — would blur completeness with decidability.
- **Review question:** In Gujarati mathematical-logic prose, does ‘પૂર્ણ ગણ’ accurately express ‘complete set’ with the scope stated here: The canon directly uses પૂર્ણ for a formal system that leaves no sentence undecided. Here the displayed definition fixes the set-level sense: for every sentence, the set contains it or its negation. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T129: saturated set / Henkin expansion / witness / counterexample → સંતૃપ્ત ગણ / હેન્કિન વિસ્તાર / સાક્ષી / પ્રતિદૃષ્ટાંત

- **Status and uncertainty:** `provisional_mixed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_completeness_translation; `work/add_completeness_terms.py`.
- **English use:** `upstream/content/first-order-logic/completeness/outline.tex:140` (OLP-0128, “saturated set”); `upstream/content/first-order-logic/completeness/henkin-expansions.tex:11` (OLP-0130, “Henkin expansion”); `upstream/content/first-order-logic/completeness/henkin-expansions.tex:27` (OLP-0130, “witness”); `upstream/content/first-order-logic/completeness/henkin-expansions.tex:28` (OLP-0130, “counterexample”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/outline.tex:143` (OLP-0128, “સંતૃપ્ત ગણ”); `gu/content/first-order-logic/completeness/henkin-expansions.tex:11` (OLP-0130, “હેન્કિન વિસ્તાર”); `gu/content/first-order-logic/completeness/henkin-expansions.tex:26` (OLP-0130, “સાક્ષી”); `gu/content/first-order-logic/completeness/henkin-expansions.tex:27` (OLP-0130, “પ્રતિદૃષ્ટાંત”)
- **Authorities actually checked:** `GU-P067` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 7, "last_line_one_based": 7, "utf8_start": 10292, "utf8_end": 12844, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P072` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 9, "last_line_one_based": 9, "utf8_start": 13274, "utf8_end": 15728, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P073` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 17833, "utf8_end": 19671, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P077` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 2, "last_line_one_based": 2, "utf8_start": 1405, "utf8_end": 3561, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Quantifiers, formal derivation and finite proof steps are directly supported. સંતૃપ્ત and the Henkin name are contextual technical renderings; સાક્ષી is used for a true existential and પ્રતિદૃષ્ટાંત for a false universal, with the displayed Henkin implications controlling their exact roles.
- **Alternatives:** પરિપૂર્ણ ગણ — risks collision with complete set, which has a different definition.; હેન્કિન પ્રસરણ — a possible rendering of expansion, but વિસ્તાર is already established for language and set extension in this edition.
- **Review question:** In Gujarati mathematical-logic prose, does ‘સંતૃપ્ત ગણ / હેન્કિન વિસ્તાર / સાક્ષી / પ્રતિદૃષ્ટાંત’ accurately express ‘saturated set / Henkin expansion / witness / counterexample’ with the scope stated here: Quantifiers, formal derivation and finite proof steps are directly supported. સંતૃપ્ત and the Henkin name are contextual technical renderings; સાક્ષી is used for a true existential and પ્રતિદૃષ્ટાંત for a false universal, with the displayed Henkin implications controlling their exact roles. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T130: Lindenbaum's Lemma → લિન્ડનબાઉમનું સહાયક પ્રમેય

- **Status and uncertainty:** `provisional_transliteration`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_completeness_translation; `work/add_completeness_terms.py`.
- **English use:** `upstream/content/first-order-logic/completeness/lindenbaums-lemma.tex:13` (OLP-0131, “Lindenbaum's Lemma”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/lindenbaums-lemma.tex:13` (OLP-0131, “લિન્ડનબાઉમનું સહાયક પ્રમેય”)
- **Authorities actually checked:** `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P072` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 9, "last_line_one_based": 9, "utf8_start": 13274, "utf8_end": 15728, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P073` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 17833, "utf8_end": 19671, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P077` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 2, "last_line_one_based": 2, "utf8_start": 1405, "utf8_end": 3561, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The personal name is transliterated and lemma is rendered with the edition's established સહાયક પ્રમેય. The checked canon supports theorem, proof and formal derivation register but does not directly attest the eponym.
- **Alternatives:** લિન્ડેનબાઉમનું લેમા — closer to English sound and form, but retains an avoidable English technical noun.; લિન્ડનબાઉમ ઉપપ્રમેય — concise, but less consistent with existing edition terminology for lemma.
- **Review question:** In Gujarati mathematical-logic prose, does ‘લિન્ડનબાઉમનું સહાયક પ્રમેય’ accurately express ‘Lindenbaum's Lemma’ with the scope stated here: The personal name is transliterated and lemma is rendered with the edition's established સહાયક પ્રમેય. The checked canon supports theorem, proof and formal derivation register but does not directly attest the eponym. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T131: term model / Truth Lemma → પદ-નિદર્શ / સત્યતા સહાયક પ્રમેય

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_completeness_translation; `work/add_completeness_terms.py`.
- **English use:** `upstream/content/first-order-logic/completeness/outline.tex:156` (OLP-0128, “term model”); `upstream/content/first-order-logic/completeness/construction-of-model.tex:163` (OLP-0132, “Truth Lemma”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/outline.tex:159` (OLP-0128, “પદ-નિદર્શ”); `gu/content/first-order-logic/completeness/construction-of-model.tex:168` (OLP-0132, “સત્યતા સહાયક પ્રમેય”)
- **Authorities actually checked:** `GU-P025` (GU-VK-TRUTH, {"line_one_based": 128, "utf8_start": 44931, "utf8_end": 46011, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P067` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 7, "last_line_one_based": 7, "utf8_start": 10292, "utf8_end": 12844, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P077` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 2, "last_line_one_based": 2, "utf8_start": 1405, "utf8_end": 3561, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** પદ and નિદર્શ are established edition components; the exact compound names the model whose domain consists of closed terms. સત્યતા સહાયક પ્રમેય states the lemma's role, and its displayed biconditional fixes truth in the constructed model as equivalent to membership in the completed set.
- **Alternatives:** ટર્મ મૉડલ / ટ્રુથ લેમા — recognizable transliterations, but they discard useful Gujarati composition.; સત્ય સહાયક પ્રમેય — shorter, while સત્યતા better denotes the semantic property used throughout the proof.
- **Review question:** In Gujarati mathematical-logic prose, does ‘પદ-નિદર્શ / સત્યતા સહાયક પ્રમેય’ accurately express ‘term model / Truth Lemma’ with the scope stated here: પદ and નિદર્શ are established edition components; the exact compound names the model whose domain consists of closed terms. સત્યતા સહાયક પ્રમેય states the lemma's role, and its displayed biconditional fixes truth in the constructed model as equivalent to membership in the completed set. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T132: factoring / representative / well defined → ભાગફલન / પ્રતિનિધિ / સુવ્યાખ્યાયિત

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_completeness_translation; `work/add_completeness_terms.py`.
- **English use:** `upstream/content/first-order-logic/completeness/identity.tex:23` (OLP-0133, “factoring”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:154` (OLP-0048, “representative”); `upstream/content/first-order-logic/completeness/identity.tex:136` (OLP-0133, “well defined”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/identity.tex:21` (OLP-0133, “ભાગફલન”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:149` (OLP-0048, “પ્રતિનિધિ”); `gu/content/sets-functions-relations/functions/functions-relations.tex:61` (OLP-0023, “સુવ્યાખ્યાયિત”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"}); `GU-P025` (GU-VK-TRUTH, {"line_one_based": 128, "utf8_start": 44931, "utf8_end": 46011, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P077` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 2, "last_line_one_based": 2, "utf8_start": 1405, "utf8_end": 3561, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The visually checked relation canon directly supports equivalence relations, and prior decision GU-T026 directly supports સામ્ય વર્ગ. These three forms describe forming the quotient, choosing a class representative and proving the resulting interpretations independent of that choice; the exact compounds remain open.
- **Alternatives:** ભાગફળ રચના — clear prose alternative to ભાગફલન and used where the construction itself is emphasized.; સુનિર્ધારિત — a possible rendering of well defined, but can suggest uniqueness rather than representative independence.
- **Review question:** In Gujarati mathematical-logic prose, does ‘ભાગફલન / પ્રતિનિધિ / સુવ્યાખ્યાયિત’ accurately express ‘factoring / representative / well defined’ with the scope stated here: The visually checked relation canon directly supports equivalence relations, and prior decision GU-T026 directly supports સામ્ય વર્ગ. These three forms describe forming the quotient, choosing a class representative and proving the resulting interpretations independent of that choice; the exact compounds remain open. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T133: finitely satisfiable → સાન્ત રીતે સંતોષ્ય

- **Status and uncertainty:** `adopted_derivation`; medium. The head term or its components are supported, but the exact compound or model-theoretic scope remains open to expert correction.
- **Record origin:** contemporaneous_completeness_translation; `work/add_completeness_terms.py`.
- **English use:** `upstream/content/first-order-logic/completeness/compactness.tex:30` (OLP-0135, “finitely satisfiable”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/introduction.tex:59` (OLP-0127, “સાન્ત રીતે સંતોષ્ય”)
- **Authorities actually checked:** `GU-P046` (GU-VK-COUNT, {"line_one_based": 42, "last_line_one_based": 50, "utf8_start": 4564, "utf8_end": 6197, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P050` (GU-VK-MATH, {"line_one_based": 80, "last_line_one_based": 80, "utf8_start": 39535, "utf8_end": 40685, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** સાન્ત is the established edition form for finite and સંતોષ્ય is governed by GU-T098. The adverbial construction keeps the definition distinct from saying that the whole set is finite: every finite subset is satisfiable.
- **Alternatives:** દરેક સાન્ત ઉપગણે સંતોષ્ય — accurate expansion suitable in explanatory prose, but not a compact adjective.; સાન્ત-સંતોષ્ય — could be misread as a finite object that is satisfiable.
- **Review question:** In Gujarati mathematical-logic prose, does ‘સાન્ત રીતે સંતોષ્ય’ accurately express ‘finitely satisfiable’ with the scope stated here: સાન્ત is the established edition form for finite and સંતોષ્ય is governed by GU-T098. The adverbial construction keeps the definition distinct from saying that the whole set is finite: every finite subset is satisfiable. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T134: L\"owenheim--Skolem theorem → લેવેનહાઇમ--સ્કોલેમ પ્રમેય

- **Status and uncertainty:** `adopted_contextual`; medium. The head term or its components are supported, but the exact compound or model-theoretic scope remains open to expert correction.
- **Record origin:** contemporaneous_completeness_translation; `work/add_completeness_terms.py`.
- **English use:** `upstream/content/first-order-logic/completeness/introduction.tex:71` (OLP-0127, “L\"owenheim--Skolem theorem”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/introduction.tex:66` (OLP-0127, “લેવેનહાઇમ--સ્કોલેમ પ્રમેય”)
- **Authorities actually checked:** `GU-P046` (GU-VK-COUNT, {"line_one_based": 42, "last_line_one_based": 50, "utf8_start": 4564, "utf8_end": 6197, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P050` (GU-VK-MATH, {"line_one_based": 80, "last_line_one_based": 80, "utf8_start": 39535, "utf8_end": 40685, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P075` (GU-VK-WITTGENSTEIN, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 14904, "utf8_end": 17212, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The theorem name is transliterated; ગણનીય and અગણનીય are directly attested in the checked canon and governed by GU-T053. The theorem statement itself keeps OpenLogic's enumerable scope explicit as finite or denumerable.
- **Alternatives:** લોવેનહાઇમ--સ્કોલેમ — a common spelling possibility; લેવેનહાઇમ more closely follows the pronunciation used for Löwenheim here.; અવરોહી લેવેનહાઇમ--સ્કોલેમ પ્રમેય — descriptive, but the section title follows the source's shorter theorem name.
- **Review question:** In Gujarati mathematical-logic prose, does ‘લેવેનહાઇમ--સ્કોલેમ પ્રમેય’ accurately express ‘L\"owenheim--Skolem theorem’ with the scope stated here: The theorem name is transliterated; ગણનીય and અગણનીય are directly attested in the checked canon and governed by GU-T053. The theorem statement itself keeps OpenLogic's enumerable scope explicit as finite or denumerable. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T135: infinitesimal → અનંતસૂક્ષ્મ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_completeness_translation; `work/add_completeness_terms.py`.
- **English use:** `upstream/content/first-order-logic/completeness/compactness.tex:132` (OLP-0135, “infinitesimal”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/compactness.tex:139` (OLP-0135, “અનંતસૂક્ષ્મ”)
- **Authorities actually checked:** `GU-P046` (GU-VK-COUNT, {"line_one_based": 42, "last_line_one_based": 50, "utf8_start": 4564, "utf8_end": 6197, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P050` (GU-VK-MATH, {"line_one_based": 80, "last_line_one_based": 80, "utf8_start": 39535, "utf8_end": 40685, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P070` (GU-VK-TRUTH, {"line_one_based": 110, "last_line_one_based": 110, "utf8_start": 39315, "utf8_end": 40735, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P077` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 2, "last_line_one_based": 2, "utf8_start": 1405, "utf8_end": 3561, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The compound expresses a nonzero magnitude smaller than every positive rational bound in the example. The checked mathematics passages support infinite, rational and real-number register, but do not directly attest this exact term.
- **Alternatives:** અતિસૂક્ષ્મ — idiomatic but does not by itself encode the quantified smaller-than-every-standard-bound sense.; અનંતલઘુ — a possible learned-register form not found in the checked sources.
- **Review question:** In Gujarati mathematical-logic prose, does ‘અનંતસૂક્ષ્મ’ accurately express ‘infinitesimal’ with the scope stated here: The compound expresses a nonzero magnitude smaller than every positive rational bound in the example. The checked mathematics passages support infinite, rational and real-number register, but do not directly attest this exact term. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T136: axiomatizable / decidable → સ્વયંસિદ્ધીકરણીય / નિર્ણેય

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** contemporaneous_completeness_translation; `work/add_completeness_terms.py`.
- **English use:** `upstream/content/first-order-logic/completeness/complete-consistent-sets.tex:30` (OLP-0129, “axiomatizable”); `upstream/content/first-order-logic/completeness/complete-consistent-sets.tex:30` (OLP-0129, “decidable”)
- **Gujarati use:** `gu/content/first-order-logic/completeness/complete-consistent-sets.tex:29` (OLP-0129, “સ્વયંસિદ્ધીકરણીય”); `gu/content/first-order-logic/completeness/complete-consistent-sets.tex:30` (OLP-0129, “નિર્ણેય”)
- **Authorities actually checked:** `GU-P072` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 9, "last_line_one_based": 9, "utf8_start": 13274, "utf8_end": 15728, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P073` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 11, "last_line_one_based": 11, "utf8_start": 17833, "utf8_end": 19671, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P074` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 12, "last_line_one_based": 12, "utf8_start": 19671, "utf8_end": 21872, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P076` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 1, "last_line_one_based": 1, "utf8_start": 0, "utf8_end": 1405, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P077` (GU-VK-MATHEMATICAL-LOGIC, {"line_one_based": 2, "last_line_one_based": 2, "utf8_start": 1405, "utf8_end": 3561, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked canon directly supports axiomatic systems, finite proof procedures and formal decision-oriented reasoning. The derived adjectives state respectively that a theory can be axiomatized and that sentence membership or truth is decidable; neither exact form is directly attested.
- **Alternatives:** સ્વયંસિદ્ધિગમ્ય / નિર્ણયક્ષમ — plausible shorter compounds, but their precise technical scope is less explicit.; ઍક્સિયોમેટાઇઝેબલ / ડિસાઇડેબલ — transparent transliterations, but less consistent with the Gujarati scholarly register used here.
- **Review question:** In Gujarati mathematical-logic prose, does ‘સ્વયંસિદ્ધીકરણીય / નિર્ણેય’ accurately express ‘axiomatizable / decidable’ with the scope stated here: The checked canon directly supports axiomatic systems, finite proof procedures and formal decision-oriented reasoning. The derived adjectives state respectively that a theory can be axiomatized and that sentence membership or truth is decidable; neither exact form is directly attested. If not, which attested form and inflection should replace it, and at which listed target locations?

## Difficult source-correction decisions

### OLFUN-001: confirmed_mathematical_defect

- **Frozen source:** `upstream/content/sets-functions-relations/functions/inverses.tex` at `functions/inverses.tex:62-84`; SHA-256 `96e36d8cd8dc4ec0e73e9507147ecfe33d7e4f368ecf46de92efb423a7d409c1`.
- **Gujarati target:** `gu/content/sets-functions-relations/functions/inverses.tex` body line(s) 75; adjacent note line 104; SHA-256 `d782d6872d682641ec8ccd156efcfce26b78dc81d2ce0155297cb0e17c22de5c`.
- **Chosen handling:** Added the nonempty-domain hypothesis to the theorem and proof; disclosed the counterexample and exact general condition.
- **Rationale:** The injection-implies-left-inverse proposition omits the nonempty-domain condition used by its proof.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLFUN-001 without changing any unaffected claim or formula?

### OLFUN-002: confirmed_wording_defect

- **Frozen source:** `upstream/content/sets-functions-relations/functions/function-basics.tex` at `functions/function-basics.tex:64-71; sets/important-sets.tex:17`; SHA-256 `d1fa0923e303fc49a88d4e476c319d6e91a8088de44c232dcfba5878325faea3`.
- **Gujarati target:** `gu/content/sets-functions-relations/functions/function-basics.tex` body line(s) 73; adjacent note line 78; SHA-256 `1975bcc7f35c81564a91660b46f9934627b027cdec695ba1f960baad4e209364`.
- **Chosen handling:** Used nonnegative (principal) square root on the natural-number domain and disclosed the English adjective correction.
- **Rationale:** The selector on Nat is called the positive square root although Nat includes zero and sqrt(0)=0.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLFUN-002 without changing any unaffected claim or formula?

### OLFUN-003: confirmed_typographical_inconsistency

- **Frozen source:** `upstream/content/sets-functions-relations/functions/function-basics.tex` at `functions/function-basics.tex:103-107`; SHA-256 `d1fa0923e303fc49a88d4e476c319d6e91a8088de44c232dcfba5878325faea3`.
- **Gujarati target:** `gu/content/sets-functions-relations/functions/function-basics.tex` body line(s) 115; adjacent note line 118; SHA-256 `1975bcc7f35c81564a91660b46f9934627b027cdec695ba1f960baad4e209364`.
- **Chosen handling:** Normalized the input variable from n to x and disclosed the frozen typographical inconsistency.
- **Rationale:** The example introduces input n and immediately describes x.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLFUN-003 without changing any unaffected claim or formula?

### OLFUN-004: confirmed_terminology_imprecision

- **Frozen source:** `upstream/content/sets-functions-relations/functions/functions-relations.tex` at `functions/functions-relations.tex:24-30,61-64; relations/relations-as-sets.tex:55-58`; SHA-256 `e2e46c0270c44b6f54861a4565f3829b1b5f91a7f72dca84046361e5abf622c3`.
- **Gujarati target:** `gu/content/sets-functions-relations/functions/functions-relations.tex` body line(s) 67; adjacent note line 84; SHA-256 `b348c926961347405fb3589274e0ad70c027d84e9c92f745e378734199b0c909`.
- **Chosen handling:** Typed the graph as a relation contained in A times B and disclosed the source imprecision.
- **Rationale:** A graph R_f subset A x B is called a relation on A x B, which under the project's own definition would mean a subset of (A x B)^2.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLFUN-004 without changing any unaffected claim or formula?

### OLFUN-005: confirmed_explanatory_inconsistency_explicit_definition_correct

- **Frozen source:** `upstream/content/sets-functions-relations/functions/functions-relations.tex` at `functions/functions-relations.tex:78-100; relations/operations.tex:20-32`; SHA-256 `e2e46c0270c44b6f54861a4565f3829b1b5f91a7f72dca84046361e5abf622c3`.
- **Gujarati target:** `gu/content/sets-functions-relations/functions/functions-relations.tex` body line(s) 110; adjacent note line 116; SHA-256 `b348c926961347405fb3589274e0ad70c027d84e9c92f745e378734199b0c909`.
- **Chosen handling:** Kept the correct domain-only function restriction and qualified its analogy with the earlier two-coordinate relation restriction.
- **Rationale:** Function restriction keeps pairs whose first coordinate lies in C, whereas the earlier relation restriction R intersect C^2 restricts both coordinates; the source nevertheless calls the notions exact counterparts.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLFUN-005 without changing any unaffected claim or formula?

### OLSIZ-001: confirmed_tabular_value_omission

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/enumerability.tex` at `enumerability.tex:140-153`; SHA-256 `bf6be35c0e393cb6e1d227f8e9024df4216792e663f23beb7277045487acfa67`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/enumerability.tex` body line(s) 174; adjacent note line 177; SHA-256 `ae95ab24ac3c3306d59b0367ad1b3448883afe73a034510ca724ba59f0ee505d`.
- **Chosen handling:** Completed the Gujarati values row with -3 and added an adjacent keyed note.
- **Rationale:** The header and formula rows include f(7), but the final values row omits its value -3.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-001 without changing any unaffected claim or formula?

### OLSIZ-002: confirmed_grammatical_defect_clarified_by_following_formula

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/pairing.tex` at `pairing.tex:91-97`; SHA-256 `fb6cc1176e91e56cea5f5b9708723c59191813f8fe256aac8ed0457a0119a9bf`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/pairing.tex` body line(s) 102; adjacent note line 108; SHA-256 `d647d28c903c54c4a3aa2aefe711ad620b4b4a34249428234d50752edabf3ba6`.
- **Chosen handling:** Translated the formula-controlled meaning and added an adjacent keyed note.
- **Rationale:** The source says “the complement of a finite set Nat”; the next equivalence shows it means the complement of a finite subset of Nat.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-002 without changing any unaffected claim or formula?

### OLSIZ-003: confirmed_typographical_duplication

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/pairing-alt.tex` at `pairing-alt.tex:39-45`; SHA-256 `c26b4e0da9e2e0b0ec839470ddd1d0d5eb1b3d3922d3b6986c9a795f34328797`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/pairing-alt.tex` body line(s) 42; adjacent note line 52; SHA-256 `40904100170476dac400d273c4eceddc5750aacd22d4d383bffaed2604c9a9a8`.
- **Chosen handling:** Corrected the second family to (3,m) and added an adjacent keyed note.
- **Rationale:** The source repeats the (2,m) family; the immediately following table uses the intended (2,m), (3,m), and subsequent families.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-003 without changing any unaffected claim or formula?

### OLSIZ-004: confirmed_undefined_index_in_function_definition

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/reduction.tex` at `reduction.tex:51-58`; SHA-256 `0d6d2e3280698668b837cef6dcf3134b86d2a4b48831ae516e6e33e42898c79a`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/reduction.tex` body line(s) 55; adjacent note line 62; SHA-256 `f87e04b6c9b161fd013d69c12446a5de4a81cf9a2fbbb944c37a49e3c9fe7653`.
- **Chosen handling:** Used s consistently in the characteristic-sequence definition and added an adjacent keyed note.
- **Rationale:** The definition calls f(Z) a sequence s_k although k is not bound; the later surjectivity proof consistently calls the arbitrary sequence s.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-004 without changing any unaffected claim or formula?

### OLSIZ-005: confirmed_codomain_error_finite_string_used_as_infinite_sequence

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/reduction.tex` at `reduction.tex:85-101`; SHA-256 `0d6d2e3280698668b837cef6dcf3134b86d2a4b48831ae516e6e33e42898c79a`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/reduction.tex` body line(s) 103; adjacent note line 107; SHA-256 `f87e04b6c9b161fd013d69c12446a5de4a81cf9a2fbbb944c37a49e3c9fe7653`.
- **Chosen handling:** Appended an infinite tail of ones, producing a valid nonsurjective map into the intended codomain, and added an adjacent keyed note.
- **Rationale:** The displayed h(n) contains only n zeros and is finite, so it is not an element of the declared codomain of infinite binary sequences.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-005 without changing any unaffected claim or formula?

### OLSIZ-006: confirmed_undefined_function_in_empty_set_branch

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex` at `equinumerous-sets.tex:68-94`; SHA-256 `025a3fc368d6873825effcb07631913762edbf2d3f9a0711d57dcd9575361251`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/equinumerous-sets.tex` body line(s) 74, 90; adjacent note line 94; SHA-256 `6fbd4a47047c24d9dc2f53b708812801075de97462a139f0ae6b7852a0bac85b`.
- **Chosen handling:** Used f(x)=y in both conditional branches and added one adjacent keyed note covering both repairs.
- **Rationale:** Both conditional variants of the empty-set argument refer to g(x)=y before g is introduced; the bijection already in scope is f.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-006 without changing any unaffected claim or formula?

### OLSIZ-007: confirmed_wrong_domain_in_arbitrary_element_conclusion

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex` at `comparing-size.tex:91-95`; SHA-256 `075810b1cf1c8b54266518523d4665d3deae4a4937f4e19a66a09cc0e1aaebf7`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/comparing-size.tex` body line(s) 89; adjacent note line 93; SHA-256 `cf50fcd95edeadb0e27343b90e92c238c4b53c6e8bc8bcbd65c53fe1ca4a51dd`.
- **Chosen handling:** Restored the quantified domain A and added an adjacent keyed note inside the affected conditional proof branch.
- **Rationale:** After choosing an arbitrary x in A, the source mistakenly says the conclusion holds for each x in overline(A), which is too narrow and does not establish inequality with every g(x).
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-007 without changing any unaffected claim or formula?

### OLSIZ-008: confirmed_reversed_index_description_vs_array

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex` at `non-enumerability-alt.tex:59-62`; SHA-256 `a075f6c63879101314fb20fa493acfb38d78ff24095bb55914f2af4527e1ad3e`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex` body line(s) 68; adjacent note line 70; SHA-256 `bbf7f9fe3a894044e816432156c06a083dbf4e7aa5b8899e35c00cb28003520f`.
- **Chosen handling:** Translated the indexing in the order fixed by the array and added an adjacent keyed note.
- **Rationale:** The prose calls s_n(m) the nth digit of the mth string, while the immediately following row-column placement and array make it the mth digit of the nth string.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-008 without changing any unaffected claim or formula?

### OLSIZ-009: confirmed_duplicated_bit_flip_instruction

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex` at `non-enumerability-alt.tex:76-78`; SHA-256 `a075f6c63879101314fb20fa493acfb38d78ff24095bb55914f2af4527e1ad3e`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex` body line(s) 88; adjacent note line 89; SHA-256 `bbf7f9fe3a894044e816432156c06a083dbf4e7aa5b8899e35c00cb28003520f`.
- **Chosen handling:** Restored the complementary 0-to-1 bit flip and added an adjacent keyed note.
- **Rationale:** The source says to change every 1 to 0 twice; the immediately following cases require the second instruction to change every 0 to 1.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-009 without changing any unaffected claim or formula?

### OLSIZ-010: confirmed_undefined_index_in_function_definition

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/reduction-alt.tex` at `reduction-alt.tex:53-56`; SHA-256 `f7717d8394048096cf7a65bc87a1a1ed15861cdfb8c7edb23429d5256d954d11`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/reduction-alt.tex` body line(s) 55; adjacent note line 57; SHA-256 `1c0dd4b5ba5d8c82b6e9620c34080cd16728323f5dc44d74fab7c10f69d7c18d`.
- **Chosen handling:** Used s consistently throughout the definition and added an adjacent keyed note.
- **Rationale:** The characteristic-sequence definition calls f(N) a sequence s_k although k is not bound; the following surjectivity proof consistently calls an arbitrary sequence s.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-010 without changing any unaffected claim or formula?

### OLSIZ-011: confirmed_malformed_three_argument_conditional

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex` at `non-enumerability-alt.tex:47-53`; SHA-256 `a075f6c63879101314fb20fa493acfb38d78ff24095bb55914f2af4527e1ad3e`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex` body line(s) 50; adjacent note line 52; SHA-256 `bbf7f9fe3a894044e816432156c06a083dbf4e7aa5b8899e35c00cb28003520f`.
- **Chosen handling:** Closed the positive footnote branch, supplied the empty negative branch, kept the following sentence outside the conditional, and added an adjacent keyed note.
- **Rationale:** The source never closes the positive branch of oliflabeldef after its footnote, so the empty alternative and following unconditional sentence are swallowed into that branch and the required third argument is missing.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-011 without changing any unaffected claim or formula?

### OLSIZ-012: confirmed_duplicate_cross_section_label

- **Frozen source:** `upstream/content/sets-functions-relations/size-of-sets/reduction-alt.tex` at `reduction-alt.tex:107`; SHA-256 `f7717d8394048096cf7a65bc87a1a1ed15861cdfb8c7edb23429d5256d954d11`.
- **Gujarati target:** `gu/content/sets-functions-relations/size-of-sets/reduction-alt.tex` body line(s) 112; adjacent note line 113; SHA-256 `1c0dd4b5ba5d8c82b6e9620c34080cd16728323f5dc44d74fab7c10f69d7c18d`.
- **Chosen handling:** Changed only the target label section component from red to red-alt and added an adjacent keyed note.
- **Rationale:** The alternative reduction exercise reuses the fully qualified label of the primary reduction exercise, producing duplicate anchors and a duplicate-label warning when both variants are included.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSIZ-012 without changing any unaffected claim or formula?

### OLARI-001: confirmed_reversed_subtraction_in_nonnegativity_gloss

- **Frozen source:** `upstream/content/sets-functions-relations/arithmetization/rationals.tex` at `rationals.tex:53-58`; SHA-256 `7140495368042fcbc55907e6ee568c5bc8b7066e44a01a50cbf4202acebe71d2`.
- **Gujarati target:** `gu/content/sets-functions-relations/arithmetization/rationals.tex` body line(s) 54; adjacent note line 61; SHA-256 `3679f4a3d9a09466b28cfe9543479a720522cc1b38a6c935b09866c73200ee94`.
- **Chosen handling:** Used s-r consistently with the inequality and displayed definition and added an adjacent keyed note.
- **Rationale:** The source first correctly says r≤s iff s-r is nonnegative, then mistakenly calls r-s nonnegative; the displayed definition again uses s-r.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLARI-001 without changing any unaffected claim or formula?

### OLARI-002: confirmed_wrong_premise_for_nonempty_union

- **Frozen source:** `upstream/content/sets-functions-relations/arithmetization/cuts.tex` at `cuts.tex:61-65`; SHA-256 `e7cb1029bcb0f0f1ac677c005af8d4e6a10df84bfff50c7483447b972324b44c`.
- **Gujarati target:** `gu/content/sets-functions-relations/arithmetization/cuts.tex` body line(s) 64; adjacent note line 84; SHA-256 `4c561ba8bc656647400630dd331bc68ed1f4eb170eb9ab4cb7253303306b4565`.
- **Chosen handling:** Invoked the stated nonemptiness premise and added an adjacent keyed note.
- **Rationale:** The proof says that S contains a cut because S has an upper bound, whereas the stated nonemptiness of S is the premise that supplies a member.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLARI-002 without changing any unaffected claim or formula?

### OLARI-003: confirmed_quotient_object_category_errors

- **Frozen source:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex` at `cauchy.tex:84-93,152-161`; SHA-256 `35d0a39913340eadcab7fb9d7742b56aef0d0f29868cd65eeca9dc53694e8ac2`.
- **Gujarati target:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex` body line(s) 101, 162, 170; adjacent note line 116; SHA-256 `08fd34248ef36f5e12d234f75f76e88383e8b81eca37862d4f6788bc976e7d34`.
- **Chosen handling:** Named the equivalence classes in the construction, theorem and exercise and added one adjacent keyed note covering all three repairs.
- **Rationale:** The construction says to identify reals with equivalence relations rather than equivalence classes, and its theorem and exercise call the raw Cauchy sequences an ordered field although the operations were defined on their classes.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLARI-003 without changing any unaffected claim or formula?

### OLARI-004: confirmed_wrong_number_system_zero

- **Frozen source:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex` at `cauchy.tex:137-139`; SHA-256 `35d0a39913340eadcab7fb9d7742b56aef0d0f29868cd65eeca9dc53694e8ac2`.
- **Gujarati target:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex` body line(s) 146; adjacent note line 151; SHA-256 `08fd34248ef36f5e12d234f75f76e88383e8b81eca37862d4f6788bc976e7d34`.
- **Chosen handling:** Used real zero in the positivity definition and added an adjacent keyed note.
- **Rationale:** The positivity definition compares a real equivalence class with rational zero, although the class and order belong to the constructed real field.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLARI-004 without changing any unaffected claim or formula?

### OLINF-001: confirmed_unbound_carrier_and_missing_self_map_constraints

- **Frozen source:** `upstream/content/sets-functions-relations/infinite/dedekind-algebra.tex` at `dedekind-algebra.tex:41-64`; SHA-256 `9cee716bb8cb3bfd507ed5c17bbd4477d05995af6f8f8d411087793bdaa86036`.
- **Gujarati target:** `gu/content/sets-functions-relations/infinite/dedekind-algebra.tex` body line(s) 41; adjacent note line 47; SHA-256 `8fa27f1cf0441b5e33e791dc1db162a62542a908ab4a96d1b537e9b8c495f8fe`.
- **Chosen handling:** Made the carrier explicit throughout the controlling definition and lemma as f:A→A, X⊆A and o∈A, and added an adjacent keyed note.
- **Rationale:** The closure definition quantifies over any function and any o, the following lemma mentions o∈A without binding A, and its proof assumes ran(f)∪{o} is f-closed. That proof requires f to be a self-map on a carrier containing o.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLINF-001 without changing any unaffected claim or formula?

### OLINF-002: confirmed_malformed_nested_cardinality_conclusion

- **Frozen source:** `upstream/content/sets-functions-relations/infinite/card-sb.tex` at `card-sb.tex:49-53`; SHA-256 `88534a3f2be736a704ab31343e45933edb9712fa5b4411eb102c0f4a12d656e9`.
- **Gujarati target:** `gu/content/sets-functions-relations/infinite/card-sb.tex` body line(s) 51; adjacent note line 53; SHA-256 `630473ca6541f5695021d114c57f55a360532ade6ac7a261d21f639b43a16c6b`.
- **Chosen handling:** Stated the two cardinality equalities actually established by the proof and added an adjacent keyed note.
- **Rationale:** The helper proposition nests A≈B inside the first argument of another cardinality comparison. Its proof constructs bijections C→B and A→B, yielding A≈B and B≈C.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLINF-002 without changing any unaffected claim or formula?

### OLPL-001: confirmed_unmatched_parenthesis_in_defined_conditional

- **Frozen source:** `upstream/content/propositional-logic/syntax-and-semantics/formulas.tex` at `formulas.tex:158-159`; SHA-256 `f05ab9c5e23b362dbee9f6063f096f52ebc9e7f97b29acc9c07f18788f1f8f48`.
- **Gujarati target:** `gu/content/propositional-logic/syntax-and-semantics/formulas.tex` body line(s) 155; adjacent note line 163; SHA-256 `759ce2b24633dbdbbf798103b980025599bc741377792cad68c1f069a7c66701`.
- **Chosen handling:** Removed the unmatched parenthesis, yielding the well-formed abbreviation ¬A∨B, and added an adjacent keyed note.
- **Rationale:** In the branch where disjunction is primitive, the material conditional is printed as ¬A∨B) with an unmatched closing parenthesis.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLPL-001 without changing any unaffected claim or formula?

### OLPL-002: confirmed_wrong_relation_symbol_in_syntactic_proof

- **Frozen source:** `upstream/content/propositional-logic/syntax-and-semantics/formation-sequences.tex` at `formation-sequences.tex:141-142`; SHA-256 `fff70555c1ef515d9092e72c91496aa898f74e4dd41e4cadc82f49a30c5850f5`.
- **Gujarati target:** `gu/content/propositional-logic/syntax-and-semantics/formation-sequences.tex` body line(s) 136; adjacent note line 145; SHA-256 `eb4cdbd2f1f8f7e1301dbedf18589ab7decf4da152b2454ad531fc462f98da23`.
- **Chosen handling:** Restored the syntactic-identity symbol used in the controlling definition and added an adjacent keyed note.
- **Rationale:** The formation-sequence proof uses the logical-equivalence symbol between a string A and its conjunction parse, although the chapter explicitly defines and repeatedly uses the syntactic-identity symbol for this relation.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLPL-002 without changing any unaffected claim or formula?

### OLPRF-001: confirmed_mismatched_right_sequence_index

- **Frozen source:** `upstream/content/first-order-logic/proof-systems/sequent-calculus.tex` at `sequent-calculus.tex:19`; SHA-256 `5448a91da184ef1d41e40ec2d56b74db63d49412d8b96b3f2a39a101b0191bad`.
- **Gujarati target:** `gu/content/first-order-logic/proof-systems/sequent-calculus.tex` body line(s) 19; adjacent note line 35; SHA-256 `91f89402c36aacf95aac325abee69ee78c588149b34c164023d9ceff86cb1581`.
- **Chosen handling:** Ended the right sequence at B_n and added an adjacent keyed note.
- **Rationale:** The generic sequent uses independently sized left and right sequences but ends both at index m, contradicting the controlling sequent definition's A_1,...,A_m and B_1,...,B_n notation.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLPRF-001 without changing any unaffected claim or formula?

### OLPRF-002: confirmed_wrong_tableau_rule_name

- **Frozen source:** `upstream/content/first-order-logic/proof-systems/tableaux.tex` at `tableaux.tex:38`; SHA-256 `8c9db50bcbc7a4aa757b8d57796b2e51df04b1cabb61f46756a79f72a1780b8f`.
- **Gujarati target:** `gu/content/first-order-logic/proof-systems/tableaux.tex` body line(s) 37; adjacent note line 42; SHA-256 `90f2d849c025a41ac4dbc059ac423c60522c38990194c87bc9d1173df149219c`.
- **Chosen handling:** Restored the false-conjunction rule name F∧ and added an adjacent keyed note.
- **Rationale:** The false-conjunction tableau rule is named with the entire operand formula A∧B in the rule-name slot, whereas the controlling rule table and every ordinary use name the connective ∧ only.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLPRF-002 without changing any unaffected claim or formula?

### OLPRF-003: confirmed_reversed_finite_subset_scope

- **Frozen source:** `upstream/content/first-order-logic/proof-systems/tableaux.tex` at `tableaux.tex:70`; SHA-256 `8c9db50bcbc7a4aa757b8d57796b2e51df04b1cabb61f46756a79f72a1780b8f`.
- **Gujarati target:** `gu/content/first-order-logic/proof-systems/tableaux.tex` body line(s) 76; adjacent note line 77; SHA-256 `90f2d849c025a41ac4dbc059ac423c60522c38990194c87bc9d1173df149219c`.
- **Chosen handling:** Required B_i to belong to Gamma for every i=1,...,n and added an adjacent keyed note.
- **Rationale:** The consistency paragraph requires only some B_i to belong to Gamma although the displayed tableau contains all B_1,...,B_n; that condition would not make the tableau an inconsistency witness for Gamma.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLPRF-003 without changing any unaffected claim or formula?

### OLPRF-004: confirmed_wrong_rule_names_in_tableau_example

- **Frozen source:** `upstream/content/first-order-logic/proof-systems/tableaux.tex` at `tableaux.tex:59-60`; SHA-256 `8c9db50bcbc7a4aa757b8d57796b2e51df04b1cabb61f46756a79f72a1780b8f`.
- **Gujarati target:** `gu/content/first-order-logic/proof-systems/tableaux.tex` body line(s) 59; adjacent note line 66; SHA-256 `90f2d849c025a41ac4dbc059ac423c60522c38990194c87bc9d1173df149219c`.
- **Chosen handling:** Changed both line-2 justification labels from T→ to T∧ and added an adjacent keyed note.
- **Rationale:** Both formulas obtained by decomposing the true conjunction on tableau line 2 are labelled with the true-conditional rule, although they are applications of the true-conjunction rule.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLPRF-004 without changing any unaffected claim or formula?

### OLSEQ-001: confirmed_wrong_exchange_side_labels

- **Frozen source:** `upstream/content/first-order-logic/sequent-calculus/proving-things.tex` at `proving-things.tex:86,104,125,147`; SHA-256 `8c94fddc6d2f4c5faee64e84c1216e1c1ca096719b5528ea4faff753b906d303`.
- **Gujarati target:** `gu/content/first-order-logic/sequent-calculus/proving-things.tex` body line(s) 80, 102, 123, 145; adjacent note line 85; SHA-256 `547fbb9dc4bae7a4f347834882cefe4e784f17580d2213214ddb79a8d0d8102f`.
- **Chosen handling:** Changed those four inference labels from right exchange to left exchange and added one adjacent keyed note.
- **Rationale:** Four inferences exchange formulas in the antecedent but are labelled as right exchange; the displayed rule shapes and accompanying prose require left exchange.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSEQ-001 without changing any unaffected claim or formula?

### OLSEQ-002: confirmed_missing_negation_in_two_candidate_sequents

- **Frozen source:** `upstream/content/first-order-logic/sequent-calculus/proving-things.tex` at `proving-things.tex:178-179`; SHA-256 `8c94fddc6d2f4c5faee64e84c1216e1c1ca096719b5528ea4faff753b906d303`.
- **Gujarati target:** `gu/content/first-order-logic/sequent-calculus/proving-things.tex` body line(s) 173, 174; adjacent note line 176; SHA-256 `547fbb9dc4bae7a4f347834882cefe4e784f17580d2213214ddb79a8d0d8102f`.
- **Chosen handling:** Restored the negation on B in both prose candidate sequents and added an adjacent keyed note.
- **Rationale:** The prose candidate sequents omit the negation on B although the stated end-sequent, the immediately preceding tree, and both subsequent branch trees use not-B.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSEQ-002 without changing any unaffected claim or formula?

### OLSEQ-003: confirmed_copied_wrong_proof_system_scope

- **Frozen source:** `upstream/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex` at `proof-theoretic-notions.tex:11`; SHA-256 `91c07ed071c2f9c18d3f10665b163b35dcc8636e7e0f27b4586aa9df63177a53`.
- **Gujarati target:** `gu/content/first-order-logic/sequent-calculus/proof-theoretic-notions.tex` body line(s) 10; adjacent note line 13; SHA-256 `4198b3cbe7c82641e4b723e334b3ec2c81ddc6d29242fd8638a2d0ec9ee81ec3`.
- **Chosen handling:** Replaced the copied natural-deduction scope with sequent calculus and added an adjacent keyed note.
- **Rationale:** The editorial sentence says the definitions concern natural deduction, although the file is in the sequent-calculus chapter and every definition is stated using LK sequents.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSEQ-003 without changing any unaffected claim or formula?

### OLSEQ-004: confirmed_incomplete_weakening_case_assignments

- **Frozen source:** `upstream/content/first-order-logic/sequent-calculus/soundness.tex` at `soundness.tex:98-101`; SHA-256 `4de487cafc9d685844abb2c0b29c7b51debeb30a9b1129c7a2fa8c13ae48b151`.
- **Gujarati target:** `gu/content/first-order-logic/sequent-calculus/soundness.tex` body line(s) 99, 104; adjacent note line 107; SHA-256 `4d11d1ccf5f7ab9f2382de0c6971a8405286ecfc3a9da004f4f19cd141fec441`.
- **Chosen handling:** Stated Theta and Xi separately for the left- and right-weakening cases and added an adjacent keyed note.
- **Rationale:** The weakening proof assigns Theta only as in left weakening while arguing both left and right cases, and leaves the corresponding Xi split implicit.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSEQ-004 without changing any unaffected claim or formula?

### OLSEQ-005: confirmed_wrong_conclusion_sequent_in_soundness_case

- **Frozen source:** `upstream/content/first-order-logic/sequent-calculus/soundness.tex` at `soundness.tex:158`; SHA-256 `4de487cafc9d685844abb2c0b29c7b51debeb30a9b1129c7a2fa8c13ae48b151`.
- **Gujarati target:** `gu/content/first-order-logic/sequent-calculus/soundness.tex` body line(s) 168; adjacent note line 171; SHA-256 `4d11d1ccf5f7ab9f2382de0c6971a8405286ecfc3a9da004f4f19cd141fec441`.
- **Chosen handling:** Restored the actual conclusion sequent with the principal conjunction and added an adjacent keyed note.
- **Rationale:** The left-conjunction soundness case concludes that Gamma implies Delta is valid, dropping the principal conjunction from the rule's actual conclusion.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSEQ-005 without changing any unaffected claim or formula?

### OLSEQ-006: confirmed_set_difference_instead_of_sequent

- **Frozen source:** `upstream/content/first-order-logic/sequent-calculus/soundness.tex` at `soundness.tex:288`; SHA-256 `4de487cafc9d685844abb2c0b29c7b51debeb30a9b1129c7a2fa8c13ae48b151`.
- **Gujarati target:** `gu/content/first-order-logic/sequent-calculus/soundness.tex` body line(s) 308; adjacent note line 310; SHA-256 `4d11d1ccf5f7ab9f2382de0c6971a8405286ecfc3a9da004f4f19cd141fec441`.
- **Chosen handling:** Replaced the accidental set-difference expression with the right premise sequent and added an adjacent keyed note.
- **Rationale:** The cut soundness proof writes set difference Pi minus Lambda where it must refer to the right premise sequent Pi implies Lambda.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLSEQ-006 without changing any unaffected claim or formula?

### OLND-001: confirmed_copied_sequent_term_in_sentence_tree

- **Frozen source:** `upstream/content/first-order-logic/natural-deduction/rules-and-proofs.tex` at `rules-and-proofs.tex:33`; SHA-256 `e6e8bed6816bd64ac24342fd4d591ca0e7c1ddf82fc056b452aa87c45d810506`.
- **Gujarati target:** `gu/content/first-order-logic/natural-deduction/rules-and-proofs.tex` body line(s) 32; adjacent note line 41; SHA-256 `31eebdfe5797424cd4224b145215c435df47173c10ff549a4cc804a41280d4ee`.
- **Chosen handling:** Read the copied term as ‘sentences’ and added an adjacent keyed note.
- **Rationale:** The natural-deduction tree is explicitly a tree of sentences, but one copied phrase calls the nodes above a sentence ‘sequents’.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLND-001 without changing any unaffected claim or formula?

### OLND-002: confirmed_copied_end_sequent_term_in_natural_deduction

- **Frozen source:** `upstream/content/first-order-logic/natural-deduction/proving-things.tex` at `proving-things.tex:67`; SHA-256 `d39069643439c576cb5813ef635725ac09ef83257571e380b92dfa223a801ecc`.
- **Gujarati target:** `gu/content/first-order-logic/natural-deduction/proving-things.tex` body line(s) 59; adjacent note line 63; SHA-256 `ff8d304b76983fd480a52086a4c2fbf9f9f0f4659df28c8822ee743a803eadd3`.
- **Chosen handling:** Referred to the sentence in the conclusion and added an adjacent keyed note.
- **Rationale:** The prose calls the final natural-deduction sentence a sentence in the end-sequent, although no sequent occurs in this proof system or example.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLND-002 without changing any unaffected claim or formula?

### OLND-003: confirmed_wrong_rule_label_on_contradiction_step

- **Frozen source:** `upstream/content/first-order-logic/natural-deduction/proving-things.tex` at `proving-things.tex:133`; SHA-256 `d39069643439c576cb5813ef635725ac09ef83257571e380b92dfa223a801ecc`.
- **Gujarati target:** `gu/content/first-order-logic/natural-deduction/proving-things.tex` body line(s) 125; adjacent note line 140; SHA-256 `ff8d304b76983fd480a52086a4c2fbf9f9f0f4659df28c8822ee743a803eadd3`.
- **Chosen handling:** Relabelled the step as negation elimination and added an adjacent keyed note.
- **Rationale:** A binary step from not-A and A to falsity is labelled falsity introduction, although the defined falsity-introduction rule is unary and derives an arbitrary formula from falsity.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLND-003 without changing any unaffected claim or formula?

### OLND-004: confirmed_missing_negation_in_eigenvariable_check

- **Frozen source:** `upstream/content/first-order-logic/natural-deduction/proving-things-quant.tex` at `proving-things-quant.tex:39`; SHA-256 `962c30713b222744c165ce87f7cb8ab11d18d0e805d8d386900bfe8e8104f63f`.
- **Gujarati target:** `gu/content/first-order-logic/natural-deduction/proving-things-quant.tex` body line(s) 35; adjacent note line 38; SHA-256 `d209af97317ad61cc26a4da1cd40366e592b982c6b7f429c77070ed698e7b81a`.
- **Chosen handling:** Restored the negation in the prose premise and added an adjacent keyed note.
- **Rationale:** The eigenvariable discussion drops the negation from the existential premise used throughout the declared goal and every adjacent proof tree.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLND-004 without changing any unaffected claim or formula?

### OLND-005: confirmed_undefined_existential_elimination_operator

- **Frozen source:** `upstream/content/first-order-logic/natural-deduction/proving-things-quant.tex` at `proving-things-quant.tex:91`; SHA-256 `962c30713b222744c165ce87f7cb8ab11d18d0e805d8d386900bfe8e8104f63f`.
- **Gujarati target:** `gu/content/first-order-logic/natural-deduction/proving-things-quant.tex` body line(s) 88; adjacent note line 91; SHA-256 `d209af97317ad61cc26a4da1cd40366e592b982c6b7f429c77070ed698e7b81a`.
- **Chosen handling:** Used the defined existential-elimination operator consistently and added an adjacent keyed note.
- **Rationale:** The final eigenvariable check uses the raw TeX existential symbol rather than the chapter's defined logical existential operator inside the elimination-rule macro.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLND-005 without changing any unaffected claim or formula?

### OLND-006: confirmed_undefined_universal_elimination_operator

- **Frozen source:** `upstream/content/first-order-logic/natural-deduction/soundness.tex` at `soundness.tex:207`; SHA-256 `8b90318e1a2ed38568fb61cd5529d496cdfd17f322fd9c731a194e2d08e0a4b9`.
- **Gujarati target:** `gu/content/first-order-logic/natural-deduction/soundness.tex` body line(s) 202; adjacent note line 204; SHA-256 `23055ad895028174f53f9061f2724fdd4f8df49941d2d085216c4bda6d32cbb8`.
- **Chosen handling:** Used the defined universal-elimination operator consistently and added an adjacent keyed note.
- **Rationale:** One soundness case uses the raw TeX universal symbol rather than the chapter's defined logical universal operator inside the elimination-rule macro.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLND-006 without changing any unaffected claim or formula?

### OLTAB-001: confirmed_copied_natural_deduction_name_in_tableaux_driver

- **Frozen source:** `upstream/content/first-order-logic/tableaux/tableaux.tex` at `tableaux.tex:15`; SHA-256 `1c6e7018e63cae3440e85d537303288261afd422b9e13bc455b99c2d206aa1b6`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/tableaux.tex` body line(s) 15; adjacent note line 17; SHA-256 `a3e7ac8d0723cce7fe690054403a03f6be495a5a3cbf8f9a2f97f6ca0d378dc7`.
- **Chosen handling:** Referred to tableaux and added an adjacent keyed note.
- **Rationale:** The tableaux chapter driver calls the proof system natural deduction although its chapter, imports and prfTab profile all concern tableaux.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-001 without changing any unaffected claim or formula?

### OLTAB-002: confirmed_conflated_signed_assumptions_in_exercise

- **Frozen source:** `upstream/content/first-order-logic/tableaux/proving-things.tex` at `proving-things.tex:439`; SHA-256 `6940ff2f8466cfb9dc740a4e7aa2cf9551c9a3d3304aa8ebe93217d11e451e90`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/proving-things.tex` body line(s) 437; adjacent note line 443; SHA-256 `18e0c01c0b070c994c9c640539da0ea31b7adb6fd014032213e0fea16033eb81`.
- **Chosen handling:** Restored the negated formula as a separate true-signed assumption and added an adjacent keyed note.
- **Rationale:** An exercise places a comma and negated formula inside the first signed-formula argument, so it is not one well-formed signed formula.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-002 without changing any unaffected claim or formula?

### OLTAB-003: confirmed_missing_finite_set_braces

- **Frozen source:** `upstream/content/first-order-logic/tableaux/proof-theoretic-notions.tex` at `proof-theoretic-notions.tex:105`; SHA-256 `38a3260d51ba6fc9db22f6b40b1a57f5c46e80d2a008053beffbb7cf5eff7e71`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/proof-theoretic-notions.tex` body line(s) 106; adjacent note line 134; SHA-256 `05a2f37ff1201fab781e5dd0faba149daa056a37869e04e36904057edebc4777`.
- **Chosen handling:** Restored braces around the finite subset and added an adjacent keyed note.
- **Rationale:** The transitivity proof applies the subset relation to an individual terminal sentence rather than to the finite collection of D-sentences.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-003 without changing any unaffected claim or formula?

### OLTAB-004: confirmed_wrong_terminal_index_in_second_finite_set

- **Frozen source:** `upstream/content/first-order-logic/tableaux/provability-consistency.tex` at `provability-consistency.tex:26`; SHA-256 `1e3cd1b98b0dae48850118a996aa37c04da92108c91d2096e51ac4a19025f348`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/provability-consistency.tex` body line(s) 26; adjacent note line 38; SHA-256 `06fb3b1be5d82522eaaab3e975f208e4884c05c5a67ba5d0d7e0b2aadabd50eb`.
- **Chosen handling:** Restored terminal index m and added an adjacent keyed note.
- **Rationale:** The second finite subset ends at C_n although its immediately displayed members and the remainder of the proof end at C_m.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-004 without changing any unaffected claim or formula?

### OLTAB-005: confirmed_wrong_premise_named_for_true_negation_rule

- **Frozen source:** `upstream/content/first-order-logic/tableaux/provability-consistency.tex` at `provability-consistency.tex:92`; SHA-256 `1e3cd1b98b0dae48850118a996aa37c04da92108c91d2096e51ac4a19025f348`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/provability-consistency.tex` body line(s) 96; adjacent note line 102; SHA-256 `06fb3b1be5d82522eaaab3e975f208e4884c05c5a67ba5d0d7e0b2aadabd50eb`.
- **Chosen handling:** Restored true not-A as the rule premise and added an adjacent keyed note.
- **Rationale:** The proof says the true-negation rule is applied to false A, although it has just replaced that assumption by true not-A.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-005 without changing any unaffected claim or formula?

### OLTAB-006: confirmed_malformed_true_signed_formula_macros

- **Frozen source:** `upstream/content/first-order-logic/tableaux/provability-propositional.tex` at `provability-propositional.tex:43`; SHA-256 `342109e7ee29a08f322f02df997f40ca08aa60cc1388f150b7b23c0aaddd9f13`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/provability-propositional.tex` body line(s) 63; adjacent note line 72; SHA-256 `bc4f46f02a764209aa652aea1031be8fe0e2496f86cd5272b081896e20a56693`.
- **Chosen handling:** Restored the two arguments in all four true-signed nodes and added an adjacent keyed note.
- **Rationale:** Four proof-tree nodes nest each formula inside the truth-sign argument and omit the signed-formula macro's second argument.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-006 without changing any unaffected claim or formula?

### OLTAB-007: confirmed_malformed_false_signed_formula_macros

- **Frozen source:** `upstream/content/first-order-logic/tableaux/provability-propositional.tex` at `provability-propositional.tex:106`; SHA-256 `342109e7ee29a08f322f02df997f40ca08aa60cc1388f150b7b23c0aaddd9f13`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/provability-propositional.tex` body line(s) 121; adjacent note line 129; SHA-256 `bc4f46f02a764209aa652aea1031be8fe0e2496f86cd5272b081896e20a56693`.
- **Chosen handling:** Restored the two arguments in all four false-signed nodes and added an adjacent keyed note.
- **Rationale:** Four proof-tree nodes nest each formula inside the falsity-sign argument and omit the signed-formula macro's second argument.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-007 without changing any unaffected claim or formula?

### OLTAB-008: confirmed_extraneous_punctuation_inside_formula_span

- **Frozen source:** `upstream/content/first-order-logic/tableaux/provability-quantifiers.tex` at `provability-quantifiers.tex:79`; SHA-256 `0087b4788815c95c714158f2f37438e351183f97d8388c0acde21c20a6e8aa0f`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/provability-quantifiers.tex` body line(s) 79; adjacent note line 86; SHA-256 `9786a809d09d6b8b12a92bd934667dd94b6caab9b1608be98abf75b7b16ae4dc`.
- **Chosen handling:** Removed the extraneous comma and added an adjacent keyed note.
- **Rationale:** An extraneous comma is placed inside the mathematical span after the final signed assumption.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-008 without changing any unaffected claim or formula?

### OLTAB-009: confirmed_formula_letter_mismatch_in_quantified_soundness_cases

- **Frozen source:** `upstream/content/first-order-logic/tableaux/soundness.tex` at `soundness.tex:128`; SHA-256 `d08c0332f74466555414fa2463a0d32e8bcf40abdf7cab4016c1c48133166a80`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/soundness.tex` body line(s) 123; adjacent note line 158; SHA-256 `291222506a17a5547b8e8b90b0ead8de9b77c8c3b6153839ad28ce3173c3a9a3`.
- **Chosen handling:** Used A consistently throughout both cases and added an adjacent keyed note.
- **Rationale:** Two quantified soundness cases switch their quantified premise from A to B while their conclusions and the rest of each argument remain about A.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-009 without changing any unaffected claim or formula?

### OLTAB-010: confirmed_wrong_instantiated_equality_in_transitivity_explanation

- **Frozen source:** `upstream/content/first-order-logic/tableaux/identity.tex` at `identity.tex:89`; SHA-256 `3e088c34666999c12f7a9c60aee27e93d0a5e917b9af2afc47115c7c52ef4c1d`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/identity.tex` body line(s) 92; adjacent note line 95; SHA-256 `b31dd806e3355a74f544de6d189bc6e67cca39c665e43369b7b95f265289276d`.
- **Chosen handling:** Restored the instantiated equality s1=s2 and added an adjacent keyed note.
- **Rationale:** The transitivity explanation calls line 2 the generic first equality t1=t2, although the declared predicate instance on that line is s1=s2.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-010 without changing any unaffected claim or formula?

### OLTAB-011: confirmed_wrong_argument_in_symmetry_rule_prerequisite

- **Frozen source:** `upstream/content/first-order-logic/tableaux/identity.tex` at `identity.tex:69`; SHA-256 `3e088c34666999c12f7a9c60aee27e93d0a5e917b9af2afc47115c7c52ef4c1d`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/identity.tex` body line(s) 68; adjacent note line 71; SHA-256 `b31dd806e3355a74f544de6d189bc6e67cca39c665e43369b7b95f265289276d`.
- **Chosen handling:** Restored A(s1) as the prerequisite and added an adjacent keyed note.
- **Rationale:** The symmetry explanation names A(s2) as the second prerequisite although the rule instance needs A(s1) to infer A(s2).
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-011 without changing any unaffected claim or formula?

### OLTAB-012: confirmed_undefined_sign_in_true_identity_soundness_case

- **Frozen source:** `upstream/content/first-order-logic/tableaux/soundness-identity.tex` at `soundness-identity.tex:31`; SHA-256 `d86101dc8eb627b831cd3c1f637102f221e755df98c96fe8ba74170f4a60f58b`.
- **Gujarati target:** `gu/content/first-order-logic/tableaux/soundness-identity.tex` body line(s) 30; adjacent note line 44; SHA-256 `7a0cf8db202a3dbcb17fb8903f28a79a0f28c10900612b44868e7592d7f4a1c3`.
- **Chosen handling:** Restored the true sign and added an adjacent keyed note.
- **Rationale:** The soundness case for the true-identity rule gives its conclusion an undefined generic sign S even though both premises and the displayed rule use the true sign.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLTAB-012 without changing any unaffected claim or formula?

### OLAX-001: confirmed_duplicated_preposition_in_axiom_set_definition

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex` at `axioms-rules-propositional.tex:16`; SHA-256 `c6332d0af2635bb1c79d1f0e418f26472cdf1022ed23818ca51e9e1226889810`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/axioms-rules-propositional.tex` body line(s) 16; adjacent note line 36; SHA-256 `33c9a80b4a926e08c5a03e3f9eb8b32c0355fd61a6adeebf7e28e7b5a67655df`.
- **Chosen handling:** Stated directly that PAx is the set of axioms and added an adjacent keyed note.
- **Rationale:** The definition says the set of PAx of axioms, with an extra preposition that obscures PAx as the set being defined.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-001 without changing any unaffected claim or formula?

### OLAX-002: confirmed_item_commands_outside_list_environment

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex` at `axioms-rules-quantifiers.tex:23`; SHA-256 `fa0af48f98b58f2c7b5df8aa80cf2e4981936e237594ddce342e826bbca2ddc8`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex` body line(s) 24; adjacent note line 35; SHA-256 `eae7c9239fdbbfc1de118279c2e6729d1570edc018a15641a14e16842ec86157`.
- **Chosen handling:** Wrapped the two rules in an enumerate environment and added an adjacent keyed note.
- **Rationale:** Both item commands in the quantifier-rule definition occur outside any list environment.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-002 without changing any unaffected claim or formula?

### OLAX-003: confirmed_incomplete_eigenconstant_conditions_in_both_quantifier_rules

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex` at `axioms-rules-quantifiers.tex:25`; SHA-256 `fa0af48f98b58f2c7b5df8aa80cf2e4981936e237594ddce342e826bbca2ddc8`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/axioms-rules-quantifiers.tex` body line(s) 26; adjacent note line 40; SHA-256 `eae7c9239fdbbfc1de118279c2e6729d1570edc018a15641a14e16842ec86157`.
- **Chosen handling:** Added exclusion from A(x) to both rules and added an adjacent keyed note.
- **Rationale:** Both quantifier rules exclude the eigenconstant from Gamma and B but fail to exclude it from A(x).
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-003 without changing any unaffected claim or formula?

### OLAX-004: confirmed_overstated_rule_justification_in_transitivity_proof

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex` at `proof-theoretic-notions.tex:82`; SHA-256 `0afb9df4b5f0f5c1e892cf411d126f45acce94cfbdc9087e4bd37cb851cc370b`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex` body line(s) 82; adjacent note line 86; SHA-256 `8ddc8f4fb15873b3cc76d6ae3ab42aacc3cddea451f2f22cead67d87178189d3`.
- **Chosen handling:** Used the broader and exact phrase same reason and added an adjacent keyed note.
- **Rationale:** The proof says every replacement occurrence is justified by the same rule as A_k, although A_k may instead be an axiom or a member of Gamma.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-004 without changing any unaffected claim or formula?

### OLAX-005: confirmed_missing_closing_parenthesis_in_derivability_fact

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex` at `deduction-theorem.tex:106`; SHA-256 `ef122fcfc1a8c24e89cf5abe30efa11bcd0a1cc3ed9fca2426618e9174481780`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex` body line(s) 112; adjacent note line 125; SHA-256 `b557deada5a7da1e9a3f27f805c4df14a48521fb2bb5a6f87d7f2a8c0fff02ff`.
- **Chosen handling:** Restored the final closing parenthesis and added an adjacent keyed note.
- **Rationale:** The first listed derivability fact lacks the closing parenthesis for its outer consequent.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-005 without changing any unaffected claim or formula?

### OLAX-006: confirmed_missing_closing_parenthesis_in_displayed_propositional_theorem

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex` at `deduction-theorem-quantifiers.tex:44`; SHA-256 `79f2ddf58916652493c2892078b01dd53ae1691a97e28cfed043cbe285d11888`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex` body line(s) 43; adjacent note line 53; SHA-256 `161b3919783ad57e965b1c608e8b4b4847a9770ecce817b440b1dc2e3dac8463`.
- **Chosen handling:** Restored the final closing parenthesis and added an adjacent keyed note.
- **Rationale:** A displayed propositional theorem used in the quantified deduction proof lacks its final closing parenthesis.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-006 without changing any unaffected claim or formula?

### OLAX-007: confirmed_wrong_final_conclusion_in_quantified_deduction_proof

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex` at `deduction-theorem-quantifiers.tex:48`; SHA-256 `79f2ddf58916652493c2892078b01dd53ae1691a97e28cfed043cbe285d11888`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/deduction-theorem-quantifiers.tex` body line(s) 47; adjacent note line 59; SHA-256 `161b3919783ad57e965b1c608e8b4b4847a9770ecce817b440b1dc2e3dac8463`.
- **Chosen handling:** Restored A implies B as the conclusion and added an adjacent keyed note.
- **Rationale:** The proof concludes Gamma proves B although the theorem and immediately preceding derivation require Gamma proves A implies B.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-007 without changing any unaffected claim or formula?

### OLAX-008: confirmed_repeated_left_conjunction_axiom_reference

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/provability-propositional.tex` at `provability-propositional.tex:33`; SHA-256 `25274e10fe6d96292fe2c701b7af38291dd1d98de12a62ef385a5efd1c413007`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/provability-propositional.tex` body line(s) 34; adjacent note line 39; SHA-256 `7a2a9e65285fe271a219bbbdcb5e4b332d1c926fee73bafb8ca7c97133a129b4`.
- **Chosen handling:** Cited the right-conjunction axiom for the second projection and added an adjacent keyed note.
- **Rationale:** The proof cites the left-conjunction axiom for both conjunction projections.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-008 without changing any unaffected claim or formula?

### OLAX-009: confirmed_wrong_negation_axiom_reference

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/provability-propositional.tex` at `provability-propositional.tex:50`; SHA-256 `25274e10fe6d96292fe2c701b7af38291dd1d98de12a62ef385a5efd1c413007`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/provability-propositional.tex` body line(s) 55; adjacent note line 69; SHA-256 `7a2a9e65285fe271a219bbbdcb5e4b332d1c926fee73bafb8ca7c97133a129b4`.
- **Chosen handling:** Cited ax:lnot2 and added an adjacent keyed note.
- **Rationale:** The proof attributes not-A implies A implies false to ax:lnot1, although it is the B=false instance of ax:lnot2.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-009 without changing any unaffected claim or formula?

### OLAX-010: confirmed_misspelled_modus_ponens

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/provability-propositional.tex` at `provability-propositional.tex:58`; SHA-256 `25274e10fe6d96292fe2c701b7af38291dd1d98de12a62ef385a5efd1c413007`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/provability-propositional.tex` body line(s) 34; adjacent note line 75; SHA-256 `7a2a9e65285fe271a219bbbdcb5e4b332d1c926fee73bafb8ca7c97133a129b4`.
- **Chosen handling:** Used the established Gujarati form of modus ponens and added an adjacent keyed note.
- **Rationale:** The rule name modus ponens is misspelled as modus ponsens.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-010 without changing any unaffected claim or formula?

### OLAX-011: confirmed_raw_top_symbol_instead_of_language_macro

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/provability-quantifiers.tex` at `provability-quantifiers.tex:29`; SHA-256 `07225de499f34bd17eec7586fc9bcc59e98ea3cfa064172091fa66a336bf20b6`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/provability-quantifiers.tex` body line(s) 29; adjacent note line 35; SHA-256 `be284680373f418e0e888a7af7ea72e92cb6cf683d61854aaa4cfd0fb692758f`.
- **Chosen handling:** Used ltrue consistently and added an adjacent keyed note.
- **Rationale:** The proof switches from the configured language symbol ltrue to a raw top symbol.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-011 without changing any unaffected claim or formula?

### OLAX-012: confirmed_wrong_final_rule_justification_in_strong_generalization

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/provability-quantifiers.tex` at `provability-quantifiers.tex:30`; SHA-256 `07225de499f34bd17eec7586fc9bcc59e98ea3cfa064172091fa66a336bf20b6`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/provability-quantifiers.tex` body line(s) 31; adjacent note line 40; SHA-256 `be284680373f418e0e888a7af7ea72e92cb6cf683d61854aaa4cfd0fb692758f`.
- **Chosen handling:** Used the ltrue axiom and modus ponens as the actual final inference and added an adjacent keyed note.
- **Rationale:** The final step from ltrue implies forall x A(x) to forall x A(x) is attributed to the deduction theorem again.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-012 without changing any unaffected claim or formula?

### OLAX-013: confirmed_missing_source_authoring_markers_in_quantified_soundness_case

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex` at `soundness.tex:80`; SHA-256 `b5a11dd6a46306a767149f694f099bd9f57396013b4dfe67965e68ccae411ecb`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/soundness.tex` body line(s) 114; adjacent note line 132; SHA-256 `b6f1511cf1883217a4868139dceaa296731590635da137084f2e503073c98165`.
- **Chosen handling:** Restored the marker in all three occurrences and added an adjacent keyed note.
- **Rationale:** Three formula-variable occurrences omit the source authoring marker before B.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-013 without changing any unaffected claim or formula?

### OLAX-014: confirmed_incomplete_all_axioms_validity_argument

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex` at `soundness.tex:42`; SHA-256 `b5a11dd6a46306a767149f694f099bd9f57396013b4dfe67965e68ccae411ecb`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/soundness.tex` body line(s) 57; adjacent note line 62; SHA-256 `b6f1511cf1883217a4868139dceaa296731590635da137084f2e503073c98165`.
- **Chosen handling:** Made explicit that q2 follows by the reverse substitution direction and that truth tables verify the propositional schemas, then added an adjacent keyed note.
- **Rationale:** The proposition covers every axiom, but the first-order proof presents only q1 and leaves q2 and the propositional schemas unstated.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-014 without changing any unaffected claim or formula?

### OLAX-015: confirmed_term_scope_exceeds_governing_identity_axioms

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/identity.tex` at `identity.tex:39`; SHA-256 `9a4f25fcf00baab5d8d5f05e7fe2315ca9f4ceaa39a67551489a5130b9b8a2d4`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/identity.tex` body line(s) 43; adjacent note line 47; SHA-256 `376bfd806ca894c1b467ce19eee52d2c7eb80e11b7d3bad13d3635e80af34096`.
- **Chosen handling:** Restricted both propositions to closed terms and added an adjacent keyed note.
- **Rationale:** Two propositions are stated for arbitrary terms although the immediately governing identity axiom schemas are restricted to closed terms.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-015 without changing any unaffected claim or formula?

### OLAX-016: confirmed_missing_source_authoring_marker_before_repeated_formula_variable

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex` at `proof-theoretic-notions.tex:82`; SHA-256 `0afb9df4b5f0f5c1e892cf411d126f45acce94cfbdc9087e4bd37cb851cc370b`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/proof-theoretic-notions.tex` body line(s) 82; adjacent note line 92; SHA-256 `8ddc8f4fb15873b3cc76d6ae3ab42aacc3cddea451f2f22cead67d87178189d3`.
- **Chosen handling:** Restored the marker and added an adjacent keyed note.
- **Rationale:** One repeated occurrence of B_i lacks the source authoring marker used by every other formula variable in the derivation.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-016 without changing any unaffected claim or formula?

### OLAX-017: confirmed_membership_symbol_separated_from_left_operand

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex` at `deduction-theorem.tex:67`; SHA-256 `ef122fcfc1a8c24e89cf5abe30efa11bcd0a1cc3ed9fca2426618e9174481780`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/deduction-theorem.tex` body line(s) 64; adjacent note line 73; SHA-256 `b557deada5a7da1e9a3f27f805c4df14a48521fb2bb5a6f87d7f2a8c0fff02ff`.
- **Chosen handling:** Expressed B as a member of Gamma union {A} in one coherent statement and added an adjacent keyed note.
- **Rationale:** The membership symbol is isolated in a separate math span from its left operand B, leaving an ill-formed mathematical fragment.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-017 without changing any unaffected claim or formula?

### OLAX-018: confirmed_shared_driver_uses_first_order_term_for_propositional_case

- **Frozen source:** `upstream/content/first-order-logic/axiomatic-deduction/soundness.tex` at `soundness.tex:22`; SHA-256 `b5a11dd6a46306a767149f694f099bd9f57396013b4dfe67965e68ccae411ecb`.
- **Gujarati target:** `gu/content/first-order-logic/axiomatic-deduction/soundness.tex` body line(s) 22; adjacent note line 33; SHA-256 `b6f1511cf1883217a4868139dceaa296731590635da137084f2e503073c98165`.
- **Chosen handling:** Selected validity for FOL and tautologicity for the propositional rendering, with an adjacent keyed note.
- **Rationale:** The shared FOL and propositional chapter calls every derivable propositional formula valid instead of using the corresponding term tautology.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLAX-018 without changing any unaffected claim or formula?

### OLCO-001: confirmed_duplicated_definite_article

- **Frozen source:** `upstream/content/first-order-logic/completeness/introduction.tex` at `introduction.tex:61`; SHA-256 `e263d8a466c6fa7457f247217e75e7d571fe5af13faf97e24472e2273a089498`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/introduction.tex` body line(s) 55; adjacent note line 61; SHA-256 `9deed047b56ec031023874148b1cd98f81de7b783715e6c96fa85ed445b324fb`.
- **Chosen handling:** Removed the duplicated article in translation and added an adjacent keyed note.
- **Rationale:** The phrase the proof of is preceded by a second definite article.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-001 without changing any unaffected claim or formula?

### OLCO-002: confirmed_plural_suffix_on_adjectival_term

- **Frozen source:** `upstream/content/first-order-logic/completeness/introduction.tex` at `introduction.tex:70`; SHA-256 `e263d8a466c6fa7457f247217e75e7d571fe5af13faf97e24472e2273a089498`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/introduction.tex` body line(s) 65; adjacent note line 69; SHA-256 `9deed047b56ec031023874148b1cd98f81de7b783715e6c96fa85ed445b324fb`.
- **Chosen handling:** Rendered denumerable as an adjective modifying one structure and added an adjacent keyed note.
- **Rationale:** The adjectival token denumerable carries a plural suffix before singular model.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-002 without changing any unaffected claim or formula?

### OLCO-003: confirmed_atomic_only_restriction_conflicts_with_completeness_definition

- **Frozen source:** `upstream/content/first-order-logic/completeness/outline.tex` at `outline.tex:68`; SHA-256 `b3cbb5543255b168edbed2239981fa772d3a954bd5ce3dbf5bb8073e9b0525b1`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/outline.tex` body line(s) 63; adjacent note line 77; SHA-256 `5f9f5b5bc389566820a7a13c338771f5fd1614f5c19a9552aac872ea620cef64`.
- **Chosen handling:** Removed the atomic-only restriction so the outline matches the complete-set definition and added an adjacent keyed note.
- **Rationale:** Condition (b) requires a decision only for atomic sentences, while the definition immediately below requires a decision for every sentence.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-003 without changing any unaffected claim or formula?

### OLCO-004: confirmed_singular_noun_after_all

- **Frozen source:** `upstream/content/first-order-logic/completeness/outline.tex` at `outline.tex:76`; SHA-256 `b3cbb5543255b168edbed2239981fa772d3a954bd5ce3dbf5bb8073e9b0525b1`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/outline.tex` body line(s) 72; adjacent note line 82; SHA-256 `5f9f5b5bc389566820a7a13c338771f5fd1614f5c19a9552aac872ea620cef64`.
- **Chosen handling:** Used the intended plural phrase all sentences and added an adjacent keyed note.
- **Rationale:** The quantifier all is followed by singular sentence.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-004 without changing any unaffected claim or formula?

### OLCO-005: confirmed_wrong_theory_in_identity_quotient_outline

- **Frozen source:** `upstream/content/first-order-logic/completeness/outline.tex` at `outline.tex:126`; SHA-256 `b3cbb5543255b168edbed2239981fa772d3a954bd5ce3dbf5bb8073e9b0525b1`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/outline.tex` body line(s) 124; adjacent note line 132; SHA-256 `5f9f5b5bc389566820a7a13c338771f5fd1614f5c19a9552aac872ea620cef64`.
- **Chosen handling:** Used Gamma-star as the theory controlling equality classes and added an adjacent keyed note.
- **Rationale:** The quotient classes are said to collect terms that the original set Gamma requires equal, although the formal equivalence relation is defined from the completed extension Gamma-star.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-005 without changing any unaffected claim or formula?

### OLCO-006: confirmed_missing_argument_on_formula_metavariable

- **Frozen source:** `upstream/content/first-order-logic/completeness/henkin-expansions.tex` at `henkin-expansions.tex:141`; SHA-256 `353b1ea300b6d916be92a5100dfa2e2f4cf9ad9f44e9506c96f028acea3b1ec8`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/henkin-expansions.tex` body line(s) 139; adjacent note line 148; SHA-256 `681a89524550a5b248a4821a8b9dfe5993ce283a229ce8b2bebcc60b4293a1d3`.
- **Chosen handling:** Restored A_n(x_n), matching the adjacent branch and definition, and added an adjacent keyed note.
- **Rationale:** One branch omits the argument x_n from A_n inside a universal formula.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-006 without changing any unaffected claim or formula?

### OLCO-007: confirmed_wrong_feature_gate_on_existential_clause

- **Frozen source:** `upstream/content/first-order-logic/completeness/henkin-expansions.tex` at `henkin-expansions.tex:153`; SHA-256 `353b1ea300b6d916be92a5100dfa2e2f4cf9ad9f44e9506c96f028acea3b1ec8`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/henkin-expansions.tex` body line(s) 157; adjacent note line 164; SHA-256 `681a89524550a5b248a4821a8b9dfe5993ce283a229ce8b2bebcc60b4293a1d3`.
- **Chosen handling:** Changed the clause gate to prvEx, matching the formal proposition below, and added an adjacent keyed note.
- **Rationale:** The explanatory existential-instance clause is gated by prvAll rather than prvEx.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-007 without changing any unaffected claim or formula?

### OLCO-008: confirmed_missing_empty_finite_subset_case

- **Frozen source:** `upstream/content/first-order-logic/completeness/lindenbaums-lemma.tex` at `lindenbaums-lemma.tex:78`; SHA-256 `096a854cefe8f47251e7ad20747bda7e3832a0272a8e38ba71d732d913a9be47`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/lindenbaums-lemma.tex` body line(s) 75; adjacent note line 92; SHA-256 `f935fb4f466f9b2fecfaec834d7d4429cef602559072c463d694507ab6e11b69`.
- **Chosen handling:** Separated the empty subset case before selecting a largest index and added an adjacent keyed note.
- **Rationale:** The proof selects the largest index contributed by an arbitrary finite subset without handling the empty subset, for which no such index exists.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-008 without changing any unaffected claim or formula?

### OLCO-009: confirmed_quantifier_truth_lemma_requires_closed_terms

- **Frozen source:** `upstream/content/first-order-logic/completeness/construction-of-model.tex` at `construction-of-model.tex:243`; SHA-256 `4eefa87745fd3f79045f8f49b82dcd2c0a9c3268148150863870c82401c60702`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/construction-of-model.tex` body line(s) 22; adjacent note line 274; SHA-256 `b5b8005342e5e6c3e6605a5b43f8a64acf3f8e2355ee51c97708befa54196365`.
- **Chosen handling:** Restricted all four occurrences to closed terms and added an adjacent keyed note.
- **Rationale:** Four quantifier-case occurrences say terms without the closed-term restriction required by the cited term-model and saturation propositions.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-009 without changing any unaffected claim or formula?

### OLCO-010: confirmed_wrong_matrix_metavariable_in_universal_induction_case

- **Frozen source:** `upstream/content/first-order-logic/completeness/construction-of-model.tex` at `construction-of-model.tex:247`; SHA-256 `4eefa87745fd3f79045f8f49b82dcd2c0a9c3268148150863870c82401c60702`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/construction-of-model.tex` body line(s) 257; adjacent note line 282; SHA-256 `b5b8005342e5e6c3e6605a5b43f8a64acf3f8e2355ee51c97708befa54196365`.
- **Chosen handling:** Restored B as the quantified matrix and added an adjacent keyed note.
- **Rationale:** The universal induction case ends with forall x A(x), though the case assumption identifies A with forall x B(x).
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-010 without changing any unaffected claim or formula?

### OLCO-011: confirmed_duplicated_comma_in_function_term

- **Frozen source:** `upstream/content/first-order-logic/completeness/identity.tex` at `identity.tex:69`; SHA-256 `bc3391e4db38b0552ee8429b14f32124cdb7ee71e766ce17a5eaa2422126aa71`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/identity.tex` body line(s) 44; adjacent note line 81; SHA-256 `9fed54ac2824ca92bc5828157f54e8314961039ed8e7afc4eb98c3cb16d72a93`.
- **Chosen handling:** Removed the stray comma and added an adjacent keyed note.
- **Rationale:** The first compound function term contains a duplicated comma after t_{i+1}.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-011 without changing any unaffected claim or formula?

### OLCO-012: confirmed_wrong_representative_in_well_definedness_countercase

- **Frozen source:** `upstream/content/first-order-logic/completeness/identity.tex` at `identity.tex:126`; SHA-256 `bc3391e4db38b0552ee8429b14f32124cdb7ee71e766ce17a5eaa2422126aa71`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/identity.tex` body line(s) 129; adjacent note line 138; SHA-256 `9fed54ac2824ca92bc5828157f54e8314961039ed8e7afc4eb98c3cb16d72a93`.
- **Chosen handling:** Used R(t-prime) in the alternative-representative premise and added an adjacent keyed note.
- **Rationale:** The discussion introduces an alternative representative t-prime but states non-satisfaction for R(t), repeating the original representative.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-012 without changing any unaffected claim or formula?

### OLCO-013: confirmed_incomplete_justification_of_first_identity_truth_equivalence

- **Frozen source:** `upstream/content/first-order-logic/completeness/identity.tex` at `identity.tex:187`; SHA-256 `bc3391e4db38b0552ee8429b14f32124cdb7ee71e766ce17a5eaa2422126aa71`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/identity.tex` body line(s) 196; adjacent note line 204; SHA-256 `9fed54ac2824ca92bc5828157f54e8314961039ed8e7afc4eb98c3cb16d72a93`.
- **Chosen handling:** Cited the value lemma together with the identity interpretation and added an adjacent keyed note.
- **Rationale:** The first Truth Lemma equivalence is attributed only to the quotient-structure definition, omitting the lemma that computes term values as equivalence classes.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-013 without changing any unaffected claim or formula?

### OLCO-014: confirmed_malformed_variable_types_in_compactness_statement

- **Frozen source:** `upstream/content/first-order-logic/completeness/compactness.tex` at `compactness.tex:35`; SHA-256 `427e195e6bab0024f56954406ec4d9303573e4c2c796e8bf7446c45fcf253407`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/compactness.tex` body line(s) 33; adjacent note line 42; SHA-256 `fa1e0514041303d1bcd629e1287dabe8c0b45473bddb40bf161053aebdaf5858`.
- **Chosen handling:** Stated the two variable types explicitly and added an adjacent keyed note.
- **Rationale:** The theorem calls both Gamma and A sentences, although Gamma is a set of sentences and A is one sentence.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-014 without changing any unaffected claim or formula?

### OLCO-015: confirmed_malformed_model_existence_sentence_and_variable_shadowing

- **Frozen source:** `upstream/content/first-order-logic/completeness/compactness.tex` at `compactness.tex:118`; SHA-256 `427e195e6bab0024f56954406ec4d9303573e4c2c796e8bf7446c45fcf253407`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/compactness.tex` body line(s) 119; adjacent note line 125; SHA-256 `fa1e0514041303d1bcd629e1287dabe8c0b45473bddb40bf161053aebdaf5858`.
- **Chosen handling:** Introduced a fresh structure N and separately stated that N satisfies Gamma union Delta, then added an adjacent keyed note.
- **Rationale:** The sentence says there are models followed by a satisfaction formula rather than a structure, and it reuses M from the finite-subset construction.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-015 without changing any unaffected claim or formula?

### OLCO-016: confirmed_malformed_quantifier_scope_in_infinitesimal_example

- **Frozen source:** `upstream/content/first-order-logic/completeness/compactness.tex` at `compactness.tex:145`; SHA-256 `427e195e6bab0024f56954406ec4d9303573e4c2c796e8bf7446c45fcf253407`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/compactness.tex` body line(s) 152; adjacent note line 163; SHA-256 `fa1e0514041303d1bcd629e1287dabe8c0b45473bddb40bf161053aebdaf5858`.
- **Chosen handling:** Stated that every relevant sentence occurring in Delta-zero has index k below K and added an adjacent keyed note.
- **Rationale:** The phrase for all the sentences ... have k<K is grammatically malformed and obscures the scope of the index bound.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-016 without changing any unaffected claim or formula?

### OLCO-017: confirmed_missing_empty_delta_prime_case

- **Frozen source:** `upstream/content/first-order-logic/completeness/compactness.tex` at `compactness.tex:190`; SHA-256 `427e195e6bab0024f56954406ec4d9303573e4c2c796e8bf7446c45fcf253407`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/compactness.tex` body line(s) 199; adjacent note line 210; SHA-256 `fa1e0514041303d1bcd629e1287dabe8c0b45473bddb40bf161053aebdaf5858`.
- **Chosen handling:** Separated the empty Delta-prime case before selecting the maximum and added an adjacent keyed note.
- **Rationale:** The proof chooses the largest n represented in an arbitrary finite Delta-prime without handling the empty set.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-017 without changing any unaffected claim or formula?

### OLCO-018: confirmed_incomplete_direct_truth_lemma_adaptation

- **Frozen source:** `upstream/content/first-order-logic/completeness/compactness-direct.tex` at `compactness-direct.tex:139`; SHA-256 `7334d3683b1ca6356dea7526b1a53448c6d768353e720c31d766a07c67017122`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/compactness-direct.tex` body line(s) 144; adjacent note line 162; SHA-256 `46656017e4ea4b32f5374388da42ede76b1796ac27f0dbb6088a46b3a3326319`.
- **Chosen handling:** Added the finite-satisfiability arguments establishing false is absent, true is present and negation membership complements membership, then added an adjacent keyed note.
- **Rationale:** The source says that changing two cited propositions makes the Truth Lemma proof go through, but its falsity, truth and negation cases also invoke consistency directly.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-018 without changing any unaffected claim or formula?

### OLCO-019: confirmed_missing_identity_quotient_case_in_direct_compactness_proof

- **Frozen source:** `upstream/content/first-order-logic/completeness/compactness-direct.tex` at `compactness-direct.tex:22`; SHA-256 `7334d3683b1ca6356dea7526b1a53448c6d768353e720c31d766a07c67017122`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/compactness-direct.tex` body line(s) 152; adjacent note line 168; SHA-256 `46656017e4ea4b32f5374388da42ede76b1796ac27f0dbb6088a46b3a3326319`.
- **Chosen handling:** Added the quotient term-model case, including finite-satisfiability arguments for well-definedness, and added an adjacent keyed note.
- **Rationale:** The general first-order compactness proof constructs only the plain term model and cites a Truth Lemma explicitly restricted to formulas without identity.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-019 without changing any unaffected claim or formula?

### OLCO-020: confirmed_wrong_language_scope_for_henkin_term_domain

- **Frozen source:** `upstream/content/first-order-logic/completeness/downward-ls.tex` at `downward-ls.tex:29`; SHA-256 `31e60aefb151429d7af1e982f1d44a05c4a4b37b8ea03d8163016fdf6d6058d3`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/downward-ls.tex` body line(s) 27; adjacent note line 32; SHA-256 `f10ba30be44d7dd4ca2da7dec80f9f23ab5a71117db2a6ecce1b515d66754549`.
- **Chosen handling:** Used the expanded language L-prime, whose term set remains countable, and added an adjacent keyed note.
- **Rationale:** The proof bounds the constructed domain by terms of the original language L, although the completeness construction first adds Henkin constants and uses terms of the expanded language L-prime.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-020 without changing any unaffected claim or formula?

### OLCO-021: confirmed_missing_third_argument_on_fol_conditional

- **Frozen source:** `upstream/content/first-order-logic/completeness/construction-of-model.tex` at `construction-of-model.tex:75`; SHA-256 `4eefa87745fd3f79045f8f49b82dcd2c0a9c3268148150863870c82401c60702`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/construction-of-model.tex` body line(s) 95; adjacent note line 98; SHA-256 `b5b8005342e5e6c3e6605a5b43f8a64acf3f8e2355ee51c97708befa54196365`.
- **Chosen handling:** Added the required empty false branch and an adjacent keyed note.
- **Rationale:** The FOL-only term-value block supplies only two of iftag's three required arguments.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-021 without changing any unaffected claim or formula?

### OLCO-022: confirmed_missing_third_argument_on_fol_conditional

- **Frozen source:** `upstream/content/first-order-logic/completeness/compactness-direct.tex` at `compactness-direct.tex:140`; SHA-256 `7334d3683b1ca6356dea7526b1a53448c6d768353e720c31d766a07c67017122`.
- **Gujarati target:** `gu/content/first-order-logic/completeness/compactness-direct.tex` body line(s) 143; adjacent note line 175; SHA-256 `46656017e4ea4b32f5374388da42ede76b1796ac27f0dbb6088a46b3a3326319`.
- **Chosen handling:** Added the required empty false branch and an adjacent keyed note.
- **Rationale:** The FOL-only clause naming the saturation reference supplies no third argument to iftag.
- **Alternatives:** Preserve the false or imprecise English wording literally — rejected. Correct silently — rejected because the inherited source defect must remain traceable. Correct the Gujarati body and add an adjacent keyed note — adopted.
- **Uncertainty:** The correction is applied, but mathematical and editorial review remains welcome.
- **Review question:** Does the Gujarati handling at the listed body and note lines fully and accurately repair OLCO-022 without changing any unaffected claim or formula?
