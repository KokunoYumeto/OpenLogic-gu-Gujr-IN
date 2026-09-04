# Gujarati terminology and translation review log

Updated 2026-09-04T21:40:52.462038+00:00. This is a **complete decision log for the current 51/722-unit draft**, while the translation corpus itself remains partial. Public artifact verification currently covers 45/722 units. It contains all 88 terminology decisions from the durable ledger and all 23 source corrections identified so far. It must grow with the translation.

Every term entry names the wording and sense, exact current English/Gujarati use locations where a literal form exists, the Gujarati authorities actually checked, recoverable alternatives, rationale, uncertainty and a question an expert can answer asynchronously. “Retrospective” means the explanation was reconstructed from earlier durable records; it does not claim an unrecorded search or consultation. Provisional entries are open corrections and do not stop the full-corpus workflow.

The machine-readable companion is [`TRANSLATION_DECISIONS.jsonl`](TRANSLATION_DECISIONS.jsonl); completeness metadata is in [`TRANSLATION_DECISION_LOG_METADATA.json`](TRANSLATION_DECISION_LOG_METADATA.json).

## Terminology decisions

### GU-T001: set → ગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:1`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/arithmetization.tex:12` (OLP-0041, “set”)
- **Gujarati use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Authorities actually checked:** `GU-P001` (GU-GSSTB-MATH11, {"pdf_page_one_based": 15, "printed_page": "3"}); `GU-P010` (GU-VK-MATH, {"line_one_based": 478, "utf8_start": 182255, "utf8_end": 182785, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P015` (GU-VK-GROUPS, {"line_one_based": 26, "utf8_start": 820, "utf8_end": 1060, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Actual usage distinguishes set from group સમૂહ.
- **Alternatives:** સમૂહ — rejected for sets because the consulted material distinguishes it as group.
- **Review question:** In Gujarati mathematical-logic prose, does “ગણ” express “set” with the scope stated in this rationale: Actual usage distinguishes set from group સમૂહ. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T002: element → ઘટક

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:2`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:134` (OLP-0048, “element”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex:87` (OLP-0048, “ઘટક”)
- **Authorities actually checked:** `GU-P001` (GU-GSSTB-MATH11, {"pdf_page_one_based": 15, "printed_page": "3"}); `GU-P013` (GU-VK-SETS, {"line_one_based": 36, "utf8_start": 3637, "utf8_end": 4684, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** સભ્ય is attested synonym; element text-token emits ઘટક/ઘટકો.
- **Alternatives:** સભ્ય — retained as an attested synonym, while ઘટક is the edition-wide output token.
- **Review question:** In Gujarati mathematical-logic prose, does “ઘટક” express “element” with the scope stated in this rationale: સભ્ય is attested synonym; element text-token emits ઘટક/ઘટકો. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T003: extensionality → ઘટકો દ્વારા નિર્ધારિત સમાનતા

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:3`.
- **English use:** `upstream/content/sets-functions-relations/functions/function-basics.tex:116` (OLP-0021, “extensionality”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/functions-relations.tex:33` (OLP-0023, “ઘટકો દ્વારા નિર્ધારિત સમાનતા”)
- **Authorities actually checked:** `GU-P002` (GU-GSSTB-MATH11, {"pdf_page_one_based": 20, "printed_page": "8"}); `GU-P013` (GU-VK-SETS, {"line_one_based": 36, "utf8_start": 3637, "utf8_end": 4684, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Concept attested, standard Gujarati single-name not verified; deliberately descriptive. Does not assert existence.
- **Alternatives:** વિસ્તરણાત્મકતા — not adopted because no checked Gujarati authority attested it in this mathematical sense.
- **Review question:** In Gujarati mathematical-logic prose, does “ઘટકો દ્વારા નિર્ધારિત સમાનતા” express “extensionality” with the scope stated in this rationale: Concept attested, standard Gujarati single-name not verified; deliberately descriptive. Does not assert existence. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T004: subset → ઉપગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:4`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:160` (OLP-0047, “subset”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:158` (OLP-0047, “ઉપગણ”)
- **Authorities actually checked:** `GU-P003` (GU-GSSTB-MATH11, {"pdf_page_one_based": 22, "printed_page": "10"}); `GU-P013` (GU-VK-SETS, {"line_one_based": 36, "utf8_start": 3637, "utf8_end": 4684, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Subset includes equality; preserve upstream subseteq.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ઉપગણ” express “subset” with the scope stated in this rationale: Subset includes equality; preserve upstream subseteq. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T005: proper subset → ઉચિત ઉપગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:5`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:160` (OLP-0047, “proper subset”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:158` (OLP-0047, “ઉચિત ઉપગણ”)
- **Authorities actually checked:** `GU-P014` (GU-VK-SETS, {"line_one_based": 37, "utf8_start": 4684, "utf8_end": 4762, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Strictness retained by inequality; do not change source symbols to schoolbook convention.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ઉચિત ઉપગણ” express “proper subset” with the scope stated in this rationale: Strictness retained by inequality; do not change source symbols to schoolbook convention. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T006: power set → ઘાતગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:6`.
- **English use:** `upstream/content/sets-functions-relations/sets/russells-paradox.tex:27` (OLP-0010, “power set”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/russells-paradox.tex:27` (OLP-0010, “ઘાતગણ”)
- **Authorities actually checked:** `GU-P009` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 23, "printed_page": "13"})
- **Chosen sense and rationale:** Actual definition verified in older textbook page; not inferred from glossary.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ઘાતગણ” express “power set” with the scope stated in this rationale: Actual definition verified in older textbook page; not inferred from glossary. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T007: union → યોગગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:7`.
- **English use:** `upstream/content/sets-functions-relations/relations/operations.tex:13` (OLP-0019, “union”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/operations.tex:14` (OLP-0019, “યોગગણ”)
- **Authorities actually checked:** `GU-P005` (GU-GSSTB-MATH11, {"pdf_page_one_based": 28, "printed_page": "16"})
- **Chosen sense and rationale:** Inclusive or, including shared members.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “યોગગણ” express “union” with the scope stated in this rationale: Inclusive or, including shared members. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T008: intersection → છેદગણ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:8`.
- **English use:** `upstream/content/sets-functions-relations/infinite/dedekind-algebra.tex:48` (OLP-0051, “intersection”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/russells-paradox.tex:86` (OLP-0010, “છેદગણ”)
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
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:212` (OLP-0048, “difference”)
- **Gujarati use:** `gu/content/sets-functions-relations/sets/unions-and-intersections.tex:157` (OLP-0008, “તફાવત ગણ”)
- **Authorities actually checked:** `GU-P007` (GU-GSSTB-MATH11, {"pdf_page_one_based": 30, "printed_page": "18"})
- **Chosen sense and rationale:** Direction A minus B retained.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “તફાવત ગણ” express “difference” with the scope stated in this rationale: Direction A minus B retained. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T011: Cartesian product → કાર્તેઝીય ગુણાકાર

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:11`.
- **English use:** `upstream/content/sets-functions-relations/sets/pairs-and-products.tex:52` (OLP-0009, “Cartesian product”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/relations-as-sets.tex:29` (OLP-0012, “કાર્તેઝીય ગુણાકાર”)
- **Authorities actually checked:** `GU-P008` (GU-GSSTB-MATH11, {"pdf_page_one_based": 38, "printed_page": "26"})
- **Chosen sense and rationale:** Actual Gujarati textbook use.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “કાર્તેઝીય ગુણાકાર” express “Cartesian product” with the scope stated in this rationale: Actual Gujarati textbook use. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T012: ordered pair → ક્રમયુક્ત જોડ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:12`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/integers.tex:16` (OLP-0042, “ordered pair”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/integers.tex:15` (OLP-0042, “ક્રમયુક્ત જોડ”)
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
- **English use:** `upstream/content/sets-functions-relations/relations/reflections.tex:64` (OLP-0013, “string”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/reflections.tex:70` (OLP-0013, “પ્રતીકશ્રેણી”)
- **Authorities actually checked:** `GU-P001` (GU-GSSTB-MATH11, {"pdf_page_one_based": 15, "printed_page": "3"}); `GU-P008` (GU-GSSTB-MATH11, {"pdf_page_one_based": 38, "printed_page": "26"})
- **Chosen sense and rationale:** Descriptive formation for finite symbol sequence; no concept-specific string attestation yet.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “પ્રતીકશ્રેણી” express “string” with the scope stated in this rationale: Descriptive formation for finite symbol sequence; no concept-specific string attestation yet. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T015: sequence → અનુક્રમ

- **Status and uncertainty:** `provisional`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:15`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:15` (OLP-0048, “sequence”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/orders.tex:75` (OLP-0016, “અનુક્રમ”)
- **Authorities actually checked:** `GU-P008` (GU-GSSTB-MATH11, {"pdf_page_one_based": 38, "printed_page": "26"})
- **Chosen sense and rationale:** Ordered-object prose supports construction; advanced sequence terminology needs further canon.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “અનુક્રમ” express “sequence” with the scope stated in this rationale: Ordered-object prose supports construction; advanced sequence terminology needs further canon. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T016: tuple → બહુજોડ / ક્રમયુક્ત n-જોડ

- **Status and uncertainty:** `provisional`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:16`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:68` (OLP-0047, “tuple”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/functions-relations.tex:74` (OLP-0023, “બહુજોડ”)
- **Authorities actually checked:** `GU-P008` (GU-GSSTB-MATH11, {"pdf_page_one_based": 38, "printed_page": "26"})
- **Chosen sense and rationale:** Generalization from attested ordered pair; triple ત્રિજોડ and quadruple ચતુર્જોડ provisional.
- **Alternatives:** ટ્યુપલ — avoided as an unexplained transliteration; the descriptive ordered n-tuple wording remains provisional.
- **Review question:** In Gujarati mathematical-logic prose, does “બહુજોડ / ક્રમયુક્ત n-જોડ” express “tuple” with the scope stated in this rationale: Generalization from attested ordered pair; triple ત્રિજોડ and quadruple ચતુર્જોડ provisional. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T017: continuum → સાતત્યક

- **Status and uncertainty:** `provisional`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:17`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/reals.tex:82` (OLP-0044, “continuum”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/reals.tex:95` (OLP-0044, “સાતત્યક”)
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
- **English use:** `upstream/content/sets-functions-relations/infinite/dedekinds-proof.tex:111` (OLP-0053, “paradox”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex:224` (OLP-0048, “વિરોધાભાસ”)
- **Authorities actually checked:** `GU-P012` (GU-VK-MATH, {"line_one_based": 486, "utf8_start": 192646, "utf8_end": 193794, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Contradiction is પરસ્પરવિરોધ; Russell language usage checked.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “વિરોધાભાસ” express “paradox” with the scope stated in this rationale: Contradiction is પરસ્પરવિરોધ; Russell language usage checked. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T020: relation → સંબંધ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:20`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:33` (OLP-0048, “relation”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/arithmetization.tex:1` (OLP-0041, “સંબંધ”)
- **Authorities actually checked:** `GU-P016` (GU-GSSTB-MATH11, {"pdf_page_one_based": 41, "printed_page": "29"}); `GU-P018` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 7, "printed_page": "1"})
- **Chosen sense and rationale:** Direct definition as subset; not a colloquial-only relation word.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સંબંધ” express “relation” with the scope stated in this rationale: Direct definition as subset; not a colloquial-only relation word. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T021: domain → પ્રદેશ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:21`.
- **English use:** `upstream/content/sets-functions-relations/functions/composition.tex:19` (OLP-0025, “domain”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/reals.tex:50` (OLP-0044, “પ્રદેશ”)
- **Authorities actually checked:** `GU-P016` (GU-GSSTB-MATH11, {"pdf_page_one_based": 41, "printed_page": "29"})
- **Chosen sense and rationale:** Base set and set of first coordinates differentiated by source context.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “પ્રદેશ” express “domain” with the scope stated in this rationale: Base set and set of first coordinates differentiated by source context. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T022: reflexive → સ્વવાચક

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:22`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:106` (OLP-0047, “reflexive”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:107` (OLP-0047, “સ્વવાચક”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"})
- **Chosen sense and rationale:** Every domain element relates to itself.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સ્વવાચક” express “reflexive” with the scope stated in this rationale: Every domain element relates to itself. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T023: symmetric → સંમિત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:23`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:106` (OLP-0047, “symmetric”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:107` (OLP-0047, “સંમિત”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"})
- **Chosen sense and rationale:** Both directions; actual Gujarati textbook spelling.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સંમિત” express “symmetric” with the scope stated in this rationale: Both directions; actual Gujarati textbook spelling. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T024: transitive → પરંપરિત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:24`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:106` (OLP-0047, “transitive”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:107` (OLP-0047, “પરંપરિત”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"})
- **Chosen sense and rationale:** Composition of two related pairs; use attested Gujarati, not guessed સંક્રમિત.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “પરંપરિત” express “transitive” with the scope stated in this rationale: Composition of two related pairs; use attested Gujarati, not guessed સંક્રમિત. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T025: antisymmetric → વિસંમિત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:25`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:107` (OLP-0047, “વિસંમિત”)
- **Authorities actually checked:** `GU-P020` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 9, "printed_page": "3"}); `GU-P021` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 10, "printed_page": "4"})
- **Chosen sense and rationale:** Both directions imply equality; not mere negation of symmetry.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “વિસંમિત” express “antisymmetric” with the scope stated in this rationale: Both directions imply equality; not mere negation of symmetry. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T026: equivalence relation/class → સામ્ય સંબંધ / સામ્ય વર્ગ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:26`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:33` (OLP-0048, “equivalence relation”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:134` (OLP-0048, “class”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex:33` (OLP-0048, “સામ્ય સંબંધ”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:115` (OLP-0048, “સામ્ય વર્ગ”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"}); `GU-P023` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 12, "printed_page": "6"})
- **Chosen sense and rationale:** Actual definitions and partition proof inspected.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સામ્ય સંબંધ / સામ્ય વર્ગ” express “equivalence relation/class” with the scope stated in this rationale: Actual definitions and partition proof inspected. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T027: irreflexive → અસ્વવાચક

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:27`.
- **English use:** `upstream/content/sets-functions-relations/relations/orders.tex:83` (OLP-0016, “irreflexive”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/orders.tex:87` (OLP-0016, “અસ્વવાચક”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"})
- **Chosen sense and rationale:** No attested label acquired. Defined explicitly as no self-pairs; do not confuse with merely not reflexive.
- **Alternatives:** અપ્રતિબિંબિત — not found in the authorities actually checked.
- **Review question:** In Gujarati mathematical-logic prose, does “અસ્વવાચક” express “irreflexive” with the scope stated in this rationale: No attested label acquired. Defined explicitly as no self-pairs; do not confuse with merely not reflexive. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T028: asymmetric → અસંમિત

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:28`.
- **English use:** `upstream/content/sets-functions-relations/relations/orders.tex:83` (OLP-0016, “asymmetric”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/orders.tex:87` (OLP-0016, “અસંમિત”)
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
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:149` (OLP-0048, “order”); `upstream/content/sets-functions-relations/relations/orders.tex:22` (OLP-0016, “preorder”); `upstream/content/sets-functions-relations/functions/functions.tex:22` (OLP-0020, “partial”); `upstream/content/sets-functions-relations/relations/orders.tex:32` (OLP-0016, “linear”); `upstream/content/sets-functions-relations/relations/orders.tex:82` (OLP-0016, “strict”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex:45` (OLP-0048, “ક્રમ”); `gu/content/sets-functions-relations/relations/orders.tex:23` (OLP-0016, “પૂર્વક્રમ”); `gu/content/sets-functions-relations/relations/orders.tex:27` (OLP-0016, “આંશિક ક્રમ”); `gu/content/sets-functions-relations/relations/orders.tex:31` (OLP-0016, “રેખીય ક્રમ”); `gu/content/sets-functions-relations/relations/orders.tex:86` (OLP-0016, “કડક ક્રમ”)
- **Authorities actually checked:** `GU-P021` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 10, "printed_page": "4"})
- **Chosen sense and rationale:** Definitions govern. Gujarati relations source supplies prose pattern, not attestation for these specialized labels.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ક્રમ / પૂર્વક્રમ / આંશિક ક્રમ / રેખીય ક્રમ / કડક ક્રમ” express “order/preorder/partial/linear/strict” with the scope stated in this rationale: Definitions govern. Gujarati relations source supplies prose pattern, not attestation for these specialized labels. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T031: predicate → વિધેય

- **Status and uncertainty:** `adopted_contextual`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:31`.
- **English use:** `upstream/content/sets-functions-relations/relations/reflections.tex:60` (OLP-0013, “predicate”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/arithmetization.tex:1` (OLP-0041, “વિધેય”)
- **Authorities actually checked:** `GU-P024` (GU-VK-TRUTH, {"line_one_based": 126, "utf8_start": 43654, "utf8_end": 44439, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P026` (GU-VK-TRUTH, {"line_one_based": 152, "utf8_start": 54422, "utf8_end": 55596, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Attested philosophical usage; same surface word as function, mathematical roles distinguished by context.
- **Alternatives:** પ્રેડિકેટ — avoided where the Gujarati encyclopaedic source uses contextual વિધેય; function senses are disambiguated by context.
- **Review question:** In Gujarati mathematical-logic prose, does “વિધેય” express “predicate” with the scope stated in this rationale: Attested philosophical usage; same surface word as function, mathematical roles distinguished by context. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T032: identity relation → તાદાત્મ્ય સંબંધ

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:32`.
- **English use:** `upstream/content/sets-functions-relations/relations/equivalence-relations.tex:13` (OLP-0015, “identity relation”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/equivalence-relations.tex:13` (OLP-0015, “તાદાત્મ્ય સંબંધ”)
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
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cuts.tex:17` (OLP-0045, “partition”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/equivalence-relations.tex:38` (OLP-0015, “વર્ગ વિભાજન”)
- **Authorities actually checked:** `GU-P023` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 12, "printed_page": "6"})
- **Chosen sense and rationale:** Pairwise disjoint exhaustive classes, not arbitrary overlapping subsets.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “વર્ગ વિભાજન” express “partition” with the scope stated in this rationale: Pairwise disjoint exhaustive classes, not arbitrary overlapping subsets. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T035: binary relation → દ્વિઘટકી સંબંધ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:35`.
- **English use:** `upstream/content/sets-functions-relations/relations/operations.tex:50` (OLP-0019, “binary relation”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/operations.tex:52` (OLP-0019, “દ્વિઘટકી સંબંધ”)
- **Authorities actually checked:** `GU-P016` (GU-GSSTB-MATH11, {"pdf_page_one_based": 41, "printed_page": "29"})
- **Chosen sense and rationale:** Two-place sense anchored in inspected Cartesian-product definition.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “દ્વિઘટકી સંબંધ” express “binary relation” with the scope stated in this rationale: Two-place sense anchored in inspected Cartesian-product definition. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T036: graph, vertex, edge → આલેખ, શિરોબિંદુ, ધાર

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:36`.
- **English use:** `upstream/content/sets-functions-relations/functions/composition.tex:63` (OLP-0025, “graph”); `upstream/content/sets-functions-relations/relations/graphs.tex:13` (OLP-0017, “vertex”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/composition.tex:72` (OLP-0025, “આલેખ”); `gu/content/sets-functions-relations/relations/graphs.tex:13` (OLP-0017, “શિરોબિંદુ”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:15` (OLP-0048, “ધાર”)
- **Authorities actually checked:** `GU-P016` (GU-GSSTB-MATH11, {"pdf_page_one_based": 41, "printed_page": "29"}); `GU-P017` (GU-GSSTB-MATH11, {"pdf_page_one_based": 42, "printed_page": "30"})
- **Chosen sense and rationale:** Relation arrow diagrams inspected; these specific graph-theory names not directly attested by acquired passages.
- **Alternatives:** ગ્રાફ / વર્ટેક્સ / એજ — avoided as English transliterations while the descriptive Gujarati terms remain under review.
- **Review question:** In Gujarati mathematical-logic prose, does “આલેખ, શિરોબિંદુ, ધાર” express “graph, vertex, edge” with the scope stated in this rationale: Relation arrow diagrams inspected; these specific graph-theory names not directly attested by acquired passages. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T037: tree/root/branch → વૃક્ષ / મૂળ / શાખા

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:37`.
- **English use:** `upstream/content/sets-functions-relations/relations/trees.tex:13` (OLP-0018, “tree”); `upstream/content/sets-functions-relations/arithmetization/reals.tex:24` (OLP-0044, “root”); `upstream/content/sets-functions-relations/relations/trees.tex:91` (OLP-0018, “branch”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:10` (OLP-0018, “વૃક્ષ”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:47` (OLP-0048, “મૂળ”); `gu/content/sets-functions-relations/relations/trees.tex:98` (OLP-0018, “શાખા”)
- **Authorities actually checked:** `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"}); `GU-P021` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 10, "printed_page": "4"})
- **Chosen sense and rationale:** Relations and proof prose consulted; graph/set-theoretic tree terminology remains unverified.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “વૃક્ષ / મૂળ / શાખા” express “tree/root/branch” with the scope stated in this rationale: Relations and proof prose consulted; graph/set-theoretic tree terminology remains unverified. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T038: well-ordered / least / maximal chain → સુક્રમિત / લઘુતમ / સમાવેશની દૃષ્ટિએ મહત્તમ શૃંખલા

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:38`.
- **English use:** `upstream/content/sets-functions-relations/relations/trees.tex:46` (OLP-0018, “well-ordered”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:178` (OLP-0048, “least”); `upstream/content/sets-functions-relations/relations/trees.tex:92` (OLP-0018, “maximal chain”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:50` (OLP-0018, “સુક્રમિત”); `gu/content/sets-functions-relations/relations/trees.tex:48` (OLP-0018, “લઘુતમ”); `gu/content/sets-functions-relations/relations/trees.tex:100` (OLP-0018, “સમાવેશની દૃષ્ટિએ મહત્તમ શૃંખલા”)
- **Authorities actually checked:** `GU-P021` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 10, "printed_page": "4"}); `GU-P023` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 12, "printed_page": "6"})
- **Chosen sense and rationale:** Source formal definitions govern; maximal by inclusion distinguished from largest cardinality.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સુક્રમિત / લઘુતમ / સમાવેશની દૃષ્ટિએ મહત્તમ શૃંખલા” express “well-ordered / least / maximal chain” with the scope stated in this rationale: Source formal definitions govern; maximal by inclusion distinguished from largest cardinality. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T039: successor/predecessor → અનુગામી / પુરોગામી

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:39`.
- **English use:** `upstream/content/sets-functions-relations/functions/composition.tex:48` (OLP-0025, “successor”); `upstream/content/sets-functions-relations/functions/function-basics.tex:106` (OLP-0021, “predecessor”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/composition.tex:53` (OLP-0025, “અનુગામી”); `gu/content/sets-functions-relations/functions/function-basics.tex:116` (OLP-0021, “પુરોગામી”)
- **Authorities actually checked:** `GU-P018` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 7, "printed_page": "1"})
- **Chosen sense and rationale:** Immediate neighbors in the given ordering, not arbitrary later/earlier nodes.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “અનુગામી / પુરોગામી” express “successor/predecessor” with the scope stated in this rationale: Immediate neighbors in the given ordering, not arbitrary later/earlier nodes. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T040: inverse, restriction, relative product, transitive closure → વ્યસ્ત / મર્યાદન / સાપેક્ષ ગુણાકાર / પરંપરિત સંવરણ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:40`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:32` (OLP-0047, “inverse”); `upstream/content/sets-functions-relations/functions/functions-relations.tex:81` (OLP-0023, “restriction”); `upstream/content/sets-functions-relations/functions/composition.tex:20` (OLP-0025, “relative product”); `upstream/content/sets-functions-relations/relations/operations.tex:50` (OLP-0019, “transitive closure”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:33` (OLP-0047, “વ્યસ્ત”); `gu/content/sets-functions-relations/functions/functions-relations.tex:92` (OLP-0023, “મર્યાદન”); `gu/content/sets-functions-relations/functions/composition.tex:22` (OLP-0025, “સાપેક્ષ ગુણાકાર”); `gu/content/sets-functions-relations/relations/operations.tex:52` (OLP-0019, “પરંપરિત સંવરણ”)
- **Authorities actually checked:** `GU-P016` (GU-GSSTB-MATH11, {"pdf_page_one_based": 41, "printed_page": "29"}); `GU-P019` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 8, "printed_page": "2"})
- **Chosen sense and rationale:** Native relation and transitivity senses consulted; compound labels provisional pending specialized canon.
- **Alternatives:** પ્રતિબંધ — not adopted for restriction because મર્યાદન better expresses narrowing in the consulted register.
- **Review question:** In Gujarati mathematical-logic prose, does “વ્યસ્ત / મર્યાદન / સાપેક્ષ ગુણાકાર / પરંપરિત સંવરણ” express “inverse, restriction, relative product, transitive closure” with the scope stated in this rationale: Native relation and transitivity senses consulted; compound labels provisional pending specialized canon. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T041: computability, formula, derivation, completeness → સંગણનીયતા / સૂત્ર / નિષ્પત્તિ / પૂર્ણતા

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:41`.
- **English use:** `upstream/content/sets-functions-relations/relations/trees.tex:126` (OLP-0018, “computability”); `upstream/content/sets-functions-relations/functions/function-basics.tex:85` (OLP-0021, “formula”); `upstream/content/sets-functions-relations/relations/trees.tex:15` (OLP-0018, “derivation”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:174` (OLP-0048, “completeness”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:138` (OLP-0018, “સંગણનીયતા”); `gu/content/sets-functions-relations/arithmetization/checking-details.tex:25` (OLP-0047, “સૂત્ર”); `gu/content/sets-functions-relations/infinite/dedekinds-proof.tex:54` (OLP-0053, “નિષ્પત્તિ”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:173` (OLP-0048, “પૂર્ણતા”)
- **Authorities actually checked:** `GU-P024` (GU-VK-TRUTH, {"line_one_based": 126, "utf8_start": 43654, "utf8_end": 44439, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"}); `GU-P026` (GU-VK-TRUTH, {"line_one_based": 152, "utf8_start": 54422, "utf8_end": 55596, "byte_basis": "normalized_extract_identity bytes", "normalization_id": "crlf-to-lf-v1"})
- **Chosen sense and rationale:** Introductory occurrence in Trees only; logic prose consulted, dedicated technical canon expansion still required.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સંગણનીયતા / સૂત્ર / નિષ્પત્તિ / પૂર્ણતા” express “computability, formula, derivation, completeness” with the scope stated in this rationale: Introductory occurrence in Trees only; logic prose consulted, dedicated technical canon expansion still required. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T042: function / domain / codomain / range → વિધેય / પ્રદેશ / સહપ્રદેશ / વિસ્તાર

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:42`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:59` (OLP-0048, “function”); `upstream/content/sets-functions-relations/functions/composition.tex:19` (OLP-0025, “domain”); `upstream/content/sets-functions-relations/functions/function-basics.tex:32` (OLP-0021, “codomain”); `upstream/content/sets-functions-relations/functions/composition.tex:18` (OLP-0025, “range”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/arithmetization.tex:1` (OLP-0041, “વિધેય”); `gu/content/sets-functions-relations/arithmetization/reals.tex:50` (OLP-0044, “પ્રદેશ”); `gu/content/sets-functions-relations/functions/function-basics.tex:33` (OLP-0021, “સહપ્રદેશ”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:83` (OLP-0048, “વિસ્તાર”)
- **Authorities actually checked:** `GU-P032` (GU-GSSTB-MATH11, {"pdf_page_one_based": 43, "printed_page": "31"}); `GU-P033` (GU-GSSTB-MATH11, {"pdf_page_one_based": 44, "printed_page": "32"})
- **Chosen sense and rationale:** Function context distinguished from logical predicate; source domain conventions retained.
- **Alternatives:** કાર્ય — not adopted as the primary term because the inspected textbook directly uses વિધેય.
- **Review question:** In Gujarati mathematical-logic prose, does “વિધેય / પ્રદેશ / સહપ્રદેશ / વિસ્તાર” express “function / domain / codomain / range” with the scope stated in this rationale: Function context distinguished from logical predicate; source domain conventions retained. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T043: injective / injection → એક-એક / એક-એક વિધેય

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:43`.
- **English use:** `upstream/content/sets-functions-relations/functions/composition.tex:54` (OLP-0025, “injective”); `upstream/content/sets-functions-relations/functions/function-kinds.tex:67` (OLP-0022, “injection”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/function-kinds.tex:109` (OLP-0022, “એક-એક”); `gu/content/sets-functions-relations/infinite/dedekind-algebra.tex:111` (OLP-0051, “એક-એક વિધેય”)
- **Authorities actually checked:** `GU-P034` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 14, "printed_page": "8"})
- **Chosen sense and rationale:** Both distinct-input and equal-output definitions actually inspected.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “એક-એક / એક-એક વિધેય” express “injective / injection” with the scope stated in this rationale: Both distinct-input and equal-output definitions actually inspected. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T044: surjective / surjection → વ્યાપ્ત / વ્યાપ્ત વિધેય

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:44`.
- **English use:** `upstream/content/sets-functions-relations/functions/composition.tex:59` (OLP-0025, “surjective”); `upstream/content/sets-functions-relations/functions/function-kinds.tex:36` (OLP-0022, “surjection”)
- **Gujarati use:** `gu/content/sets-functions-relations/infinite/card-sb.tex:56` (OLP-0054, “વ્યાપ્ત”); `gu/content/sets-functions-relations/infinite/card-sb.tex:56` (OLP-0054, “વ્યાપ્ત વિધેય”)
- **Authorities actually checked:** `GU-P036` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 16, "printed_page": "10"})
- **Chosen sense and rationale:** Every codomain element attained; not just each input assigned.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “વ્યાપ્ત / વ્યાપ્ત વિધેય” express “surjective / surjection” with the scope stated in this rationale: Every codomain element attained; not just each input assigned. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T045: bijective / bijection → એક-એક અને વ્યાપ્ત / એક-એક વ્યાપ્ત વિધેય

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:45`.
- **English use:** `upstream/content/sets-functions-relations/functions/function-kinds.tex:100` (OLP-0022, “bijective”); `upstream/content/sets-functions-relations/functions/composition.tex:14` (OLP-0025, “bijection”)
- **Gujarati use:** `gu/content/sets-functions-relations/infinite/card-sb.tex:56` (OLP-0054, “એક-એક વ્યાપ્ત વિધેય”)
- **Authorities actually checked:** `GU-P036` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 16, "printed_page": "10"}); `GU-P044` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 24, "printed_page": "18"})
- **Chosen sense and rationale:** Conjunction retained; one-to-one correspondence rendered as પરસ્પર એક-એક સંગતતા.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “એક-એક અને વ્યાપ્ત / એક-એક વ્યાપ્ત વિધેય” express “bijective / bijection” with the scope stated in this rationale: Conjunction retained; one-to-one correspondence rendered as પરસ્પર એક-એક સંગતતા. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T046: composition → સંયોજન

- **Status and uncertainty:** `adopted_derivation`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:46`.
- **English use:** `upstream/content/sets-functions-relations/functions/composition.tex:3` (OLP-0025, “composition”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/composition.tex:10` (OLP-0025, “સંયોજન”)
- **Authorities actually checked:** `GU-P040` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 20, "printed_page": "14"}); `GU-P041` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 21, "printed_page": "15"})
- **Chosen sense and rationale:** Noun derived from directly attested સંયોજિત વિધેય; order g after f retained.
- **Alternatives:** સંઘટન — not adopted; સંયોજન is derived from the directly attested સંયોજિત વિધેય.
- **Review question:** In Gujarati mathematical-logic prose, does “સંયોજન” express “composition” with the scope stated in this rationale: Noun derived from directly attested સંયોજિત વિધેય; order g after f retained. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T047: inverse function / left inverse / right inverse → પ્રતિવિધેય / ડાબી બાજુનો વ્યસ્ત / જમણી બાજુનો વ્યસ્ત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:47`.
- **English use:** `upstream/content/sets-functions-relations/functions/inverses.tex:57` (OLP-0024, “left inverse”); `upstream/content/sets-functions-relations/functions/inverses.tex:59` (OLP-0024, “right inverse”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/composition.tex:14` (OLP-0025, “પ્રતિવિધેય”); `gu/content/sets-functions-relations/functions/inverses.tex:67` (OLP-0024, “ડાબી બાજુનો વ્યસ્ત”); `gu/content/sets-functions-relations/functions/inverses.tex:70` (OLP-0024, “જમણી બાજુનો વ્યસ્ત”)
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
- **English use:** `upstream/content/sets-functions-relations/functions/partial-functions.tex:21` (OLP-0026, “partial function”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:153` (OLP-0048, “defined”); `upstream/content/sets-functions-relations/functions/partial-functions.tex:24` (OLP-0026, “undefined”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/partial-functions.tex:11` (OLP-0026, “આંશિક વિધેય”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:93` (OLP-0048, “વ્યાખ્યાયિત”); `gu/content/sets-functions-relations/functions/partial-functions.tex:25` (OLP-0026, “અવ્યાખ્યાયિત”)
- **Authorities actually checked:** `GU-P032` (GU-GSSTB-MATH11, {"pdf_page_one_based": 43, "printed_page": "31"}); `GU-P033` (GU-GSSTB-MATH11, {"pdf_page_one_based": 44, "printed_page": "32"})
- **Chosen sense and rationale:** Only ordinary function terminology directly attested; partial/total computability senses governed by OpenLogic definitions.
- **Alternatives:** પૂર્ણ વિધેય — avoided because “total” here means defined on every ambient input, not completeness.
- **Review question:** In Gujarati mathematical-logic prose, does “આંશિક વિધેય / સર્વત્ર વ્યાખ્યાયિત વિધેય / વ્યાખ્યાયિત / અવ્યાખ્યાયિત” express “partial function / total function / defined / undefined” with the scope stated in this rationale: Only ordinary function terminology directly attested; partial/total computability senses governed by OpenLogic definitions. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T050: argument / value / input / output → દલીલ / કિંમત / આગત / નિર્ગત

- **Status and uncertainty:** `provisional_contextual`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:50`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/reflections.tex:78` (OLP-0046, “argument”); `upstream/content/sets-functions-relations/functions/function-basics.tex:35` (OLP-0021, “value”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:91` (OLP-0048, “input”); `upstream/content/sets-functions-relations/functions/composition.tex:29` (OLP-0025, “output”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/integers.tex:99` (OLP-0042, “દલીલ”); `gu/content/sets-functions-relations/functions/function-basics.tex:36` (OLP-0021, “કિંમત”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:84` (OLP-0048, “આગત”); `gu/content/sets-functions-relations/functions/function-basics.tex:19` (OLP-0021, “નિર્ગત”)
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
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/enumerability-alt.tex:39` (OLP-0038, “enumeration”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/enumerability-alt.tex:11` (OLP-0038, “પરિગણના”)
- **Authorities actually checked:** `GU-P046` (GU-VK-COUNT, {"line_one_based": 42, "last_line_one_based": 50, "utf8_start": 4564, "utf8_end": 6197, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P034` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 14, "printed_page": "8"}); `GU-P036` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 16, "printed_page": "10"})
- **Chosen sense and rationale:** Direct canon attests countability and bijection, not this enumeration noun. Definition is an exhaustive list/surjection, and alternative variant a bijection.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “પરિગણના” express “enumeration” with the scope stated in this rationale: Direct canon attests countability and bijection, not this enumeration noun. Definition is an exhaustive list/surjection, and alternative variant a bijection. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T053: enumerable/countable; uncountable → ગણનીય; અગણનીય

- **Status and uncertainty:** `adopted_with_scope_distinction`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:53`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex:44` (OLP-0036, “enumerable”)
- **Gujarati use:** `gu/content/sets-functions-relations/relations/trees.tex:138` (OLP-0018, “ગણનીય”); `gu/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:15` (OLP-0039, “અગણનીય”)
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
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/comparing-size.tex:2` (OLP-0036, “size”)
- **Gujarati use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Authorities actually checked:** `GU-P047` (GU-VK-INFINITY, {"line_one_based": 49, "last_line_one_based": 49, "utf8_start": 12140, "utf8_end": 16135, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P048` (GU-VK-INFINITY, {"line_one_based": 57, "last_line_one_based": 80, "utf8_start": 16162, "utf8_end": 20186, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Avoid ગણનીયતા as cardinality because reserved for countability; ગણાંક directly attested.
- **Alternatives:** કાર્ડિનાલિટી — avoided as an unexplained English borrowing; ગણાંક is directly supported and કદ remains contextual prose.
- **Review question:** In Gujarati mathematical-logic prose, does “ગણાંક / કદ” express “cardinality / size” with the scope stated in this rationale: Avoid ગણનીયતા as cardinality because reserved for countability; ગણાંક directly attested. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T056: finite / infinite → સાન્ત / અનંત

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:56`.
- **English use:** `upstream/content/sets-functions-relations/functions/inverses.tex:109` (OLP-0024, “finite”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:53` (OLP-0048, “infinite”)
- **Gujarati use:** `gu/content/sets-functions-relations/functions/inverses.tex:142` (OLP-0024, “સાન્ત”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:49` (OLP-0048, “અનંત”)
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
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:196` (OLP-0048, “recursive definition”); `upstream/content/sets-functions-relations/infinite/dedekind-induction.tex:3` (OLP-0052, “induction”); `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:163` (OLP-0047, “initial segment”)
- **Gujarati use:** `gu/content/sets-functions-relations/infinite/dedekind-induction.tex:68` (OLP-0052, “પુનરાવર્તી વ્યાખ્યા”); `gu/content/sets-functions-relations/arithmetization/cuts.tex:27` (OLP-0045, “આરંભખંડ”)
- **Authorities actually checked:** `GU-P041` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 21, "printed_page": "15"}); `GU-P046` (GU-VK-COUNT, {"line_one_based": 42, "last_line_one_based": 50, "utf8_start": 4564, "utf8_end": 6197, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Proof-language and initial-segment set displayed in native sources; no exact direct technical attestation for these labels claimed.
- **Alternatives:** અનુમાનપ્રવર્તન — superseded for mathematical induction by directly attested ગાણિતિક અનુમાન; retained only as a reconstructed earlier choice.
- **Review question:** In Gujarati mathematical-logic prose, does “પુનરાવર્તી વ્યાખ્યા / અનુમાનપ્રવર્તન / આરંભખંડ” express “recursive definition / induction / initial segment” with the scope stated in this rationale: Proof-language and initial-segment set displayed in native sources; no exact direct technical attestation for these labels claimed. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T059: diagonalization / zig-zag / pairing function → વિકર્ણ પદ્ધતિ / આડીઅવળી રીત / જોડ-નિરૂપણ વિધેય

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:59`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:106` (OLP-0039, “diagonalization”); `upstream/content/sets-functions-relations/size-of-sets/pairing-alt.tex:49` (OLP-0032, “zig-zag”); `upstream/content/sets-functions-relations/size-of-sets/pairing-alt.tex:11` (OLP-0032, “pairing function”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:38` (OLP-0039, “વિકર્ણ પદ્ધતિ”); `gu/content/sets-functions-relations/size-of-sets/pairing.tex:13` (OLP-0031, “આડીઅવળી રીત”); `gu/content/sets-functions-relations/size-of-sets/pairing-alt.tex:11` (OLP-0032, “જોડ-નિરૂપણ વિધેય”)
- **Authorities actually checked:** `GU-P048` (GU-VK-INFINITY, {"line_one_based": 57, "last_line_one_based": 80, "utf8_start": 16162, "utf8_end": 20186, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P034` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 14, "printed_page": "8"}); `GU-P036` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 16, "printed_page": "10"})
- **Chosen sense and rationale:** Native prose refers to diagonalization but leaves English term; proof mechanism remains source-authoritative.
- **Alternatives:** ઝિગઝૅગ — not adopted as the main term; આડીઅવળી રીત describes the traversal but remains provisional.
- **Review question:** In Gujarati mathematical-logic prose, does “વિકર્ણ પદ્ધતિ / આડીઅવળી રીત / જોડ-નિરૂપણ વિધેય” express “diagonalization / zig-zag / pairing function” with the scope stated in this rationale: Native prose refers to diagonalization but leaves English term; proof mechanism remains source-authoritative. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T060: mathematical induction → ગાણિતિક અનુમાન

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:60`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/infinite/dedekind-induction.tex:10` (OLP-0052, “ગાણિતિક અનુમાન”)
- **Authorities actually checked:** `GU-P051` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 98, "printed_page": "88"}); `GU-P052` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 100, "printed_page": "90"}); `GU-P053` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 101, "printed_page": "91"})
- **Chosen sense and rationale:** Exact textbook chapter title, principle and worked proof inspected. Supersedes provisional induction component of GU-T058; base case and induction step essential.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “ગાણિતિક અનુમાન” express “mathematical induction” with the scope stated in this rationale: Exact textbook chapter title, principle and worked proof inspected. Supersedes provisional induction component of GU-T058; base case and induction step essential. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T061: truth function / truth table → સત્ય વિધેય / સત્ય કોષ્ટક

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:61`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/pairing.tex:81` (OLP-0031, “truth function”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/pairing.tex:89` (OLP-0031, “સત્ય વિધેય”); `gu/content/sets-functions-relations/size-of-sets/pairing.tex:89` (OLP-0031, “સત્ય કોષ્ટક”)
- **Authorities actually checked:** `GU-P042` (GU-GSSTB-MATH12-SEM3, {"pdf_page_one_based": 22, "printed_page": "16"}); `GU-P054` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 319, "printed_page": "309"}); `GU-P056` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 321, "printed_page": "311"})
- **Chosen sense and rationale:** Function and truth/compound-statement roles directly consulted; exact truth-function and truth-table labels not attested in these pages.
- **Alternatives:** ટ્રુથ ટેબલ — avoided as an English transliteration; exact Gujarati compound was not directly attested.
- **Review question:** In Gujarati mathematical-logic prose, does “સત્ય વિધેય / સત્ય કોષ્ટક” express “truth function / truth table” with the scope stated in this rationale: Function and truth/compound-statement roles directly consulted; exact truth-function and truth-table labels not attested in these pages. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T062: encode / decode / code → સંકેતબદ્ધ કરવું / સંકેત ઉકેલવો / સંકેતસંખ્યા

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:62`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/pairing-alt.tex:102` (OLP-0032, “encode”); `upstream/content/sets-functions-relations/size-of-sets/pairing.tex:62` (OLP-0031, “decode”); `upstream/content/sets-functions-relations/size-of-sets/pairing-alt.tex:96` (OLP-0032, “code”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/pairing-alt.tex:119` (OLP-0032, “સંકેતબદ્ધ કરવું”); `gu/content/sets-functions-relations/size-of-sets/pairing-alt.tex:109` (OLP-0032, “સંકેતસંખ્યા”)
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
- **English use:** `upstream/content/sets-functions-relations/relations/relations-as-sets.tex:66` (OLP-0012, “array”); `upstream/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:66` (OLP-0039, “row”); `upstream/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:66` (OLP-0039, “column”); `upstream/content/sets-functions-relations/size-of-sets/pairing.tex:33` (OLP-0031, “triangular number”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:68` (OLP-0039, “સરણિ”); `gu/content/sets-functions-relations/arithmetization/checking-details.tex:13` (OLP-0047, “હાર”); `gu/content/sets-functions-relations/size-of-sets/non-enumerability-alt.tex:69` (OLP-0039, “સ્તંભ”); `gu/content/sets-functions-relations/size-of-sets/pairing.tex:34` (OLP-0031, “ત્રિકોણીય સંખ્યા”)
- **Authorities actually checked:** `GU-P033` (GU-GSSTB-MATH11, {"pdf_page_one_based": 44, "printed_page": "32"}); `GU-P053` (GU-GSSTB-MATH11-2021, {"pdf_page_one_based": 101, "printed_page": "91"})
- **Chosen sense and rationale:** Textbook tabular and arithmetic proof register consulted; exact technical names not all directly attested.
- **Alternatives:** Retrospective: the earlier durable notes preserved no rejected alternative; no exhaustive candidate search is claimed.
- **Review question:** In Gujarati mathematical-logic prose, does “સરણિ / હાર / સ્તંભ / ત્રિકોણીય સંખ્યા” express “array / row / column / triangular number” with the scope stated in this rationale: Textbook tabular and arithmetic proof register consulted; exact technical names not all directly attested. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T065: reduction / reduce one problem to another → ન્યૂનીકરણ / એક સમસ્યાનું બીજી સમસ્યામાં ન્યૂનીકરણ કરવું

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:65`.
- **English use:** `upstream/content/sets-functions-relations/size-of-sets/reduction-alt.tex:3` (OLP-0040, “reduction”)
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/reduction-alt.tex:11` (OLP-0040, “ન્યૂનીકરણ”)
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
- **Gujarati use:** `gu/content/sets-functions-relations/size-of-sets/comparing-size.tex:26` (OLP-0036, “મોટો નથી”); `gu/content/sets-functions-relations/infinite/card-sb.tex:31` (OLP-0054, “નાનો”)
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
- **English use:** `upstream/content/sets-functions-relations/arithmetization/integers.tex:15` (OLP-0042, “integer”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:41` (OLP-0048, “rational”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:23` (OLP-0048, “irrational”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:31` (OLP-0048, “real number”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:41` (OLP-0047, “પૂર્ણાંક”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:23` (OLP-0048, “સંમેય”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:23` (OLP-0048, “અસંમેય”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:11` (OLP-0048, “વાસ્તવિક સંખ્યા”)
- **Authorities actually checked:** `GU-P057` (GU-VK-MATH, {"line_one_based": 60, "last_line_one_based": 60, "utf8_start": 29622, "utf8_end": 31947, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P058` (GU-VK-MATH, {"line_one_based": 75, "last_line_one_based": 80, "utf8_start": 36000, "utf8_end": 40685, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P059` (GU-VK-MATH, {"line_one_based": 349, "last_line_one_based": 349, "utf8_start": 107299, "utf8_end": 110083, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** All four number-kind terms occur directly in the checked Gujarati mathematical source.
- **Alternatives:** No rejected alternative is recorded because all four adopted number-kind terms are directly attested.
- **Review question:** In Gujarati mathematical-logic prose, does “પૂર્ણાંક / સંમેય / અસંમેય / વાસ્તવિક સંખ્યા” express “integer / rational / irrational / real number” with the scope stated in this rationale: All four number-kind terms occur directly in the checked Gujarati mathematical source. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T071: ring / field → મંડળ / ક્ષેત્ર

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:71`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:21` (OLP-0047, “ring”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:162` (OLP-0048, “field”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:11` (OLP-0047, “મંડળ”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:162` (OLP-0048, “ક્ષેત્ર”)
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
- **English use:** `upstream/content/sets-functions-relations/arithmetization/checking-details.tex:112` (OLP-0047, “ordered ring”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:162` (OLP-0048, “ordered field”); `upstream/content/sets-functions-relations/arithmetization/reflections.tex:20` (OLP-0046, “complete ordered field”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/checking-details.tex:11` (OLP-0047, “ક્રમિત મંડળ”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:162` (OLP-0048, “ક્રમિત ક્ષેત્ર”); `gu/content/sets-functions-relations/arithmetization/reflections.tex:19` (OLP-0046, “પૂર્ણ ક્રમિત ક્ષેત્ર”)
- **Authorities actually checked:** `GU-P057` (GU-VK-MATH, {"line_one_based": 60, "last_line_one_based": 60, "utf8_start": 29622, "utf8_end": 31947, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** Compounds preserve the directly attested head nouns મંડળ and ક્ષેત્ર; the order and completeness modifiers are controlled by the displayed definitions.
- **Alternatives:** વ્યવસ્થિત મંડળ / વ્યવસ્થિત ક્ષેત્ર — possible alternatives, but ક્રમિત matches the edition-wide term for ordered relations.
- **Review question:** In Gujarati mathematical-logic prose, does “ક્રમિત મંડળ / ક્રમિત ક્ષેત્ર / પૂર્ણ ક્રમિત ક્ષેત્ર” express “ordered ring / ordered field / complete ordered field” with the scope stated in this rationale: Compounds preserve the directly attested head nouns મંડળ and ક્ષેત્ર; the order and completeness modifiers are controlled by the displayed definitions. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T075: upper bound / lower bound / least upper bound / greatest lower bound → ઉચ્ચસીમા / અધઃસીમા / ન્યૂનતમ ઉચ્ચસીમા / મહત્તમ અધઃસીમા

- **Status and uncertainty:** `provisional_external_glossary_lead`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:75`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:177` (OLP-0048, “upper bound”); `upstream/content/sets-functions-relations/arithmetization/cuts.tex:15` (OLP-0045, “lower bound”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:178` (OLP-0048, “least upper bound”); `upstream/content/sets-functions-relations/arithmetization/cuts.tex:15` (OLP-0045, “greatest lower bound”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex:177` (OLP-0048, “ઉચ્ચસીમા”); `gu/content/sets-functions-relations/arithmetization/cuts.tex:14` (OLP-0045, “અધઃસીમા”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:177` (OLP-0048, “ન્યૂનતમ ઉચ્ચસીમા”); `gu/content/sets-functions-relations/arithmetization/cuts.tex:14` (OLP-0045, “મહત્તમ અધઃસીમા”)
- **Authorities actually checked:** `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The official CSTT mathematics glossary search result supports these forms, but no exact local original was acquired; formal definitions control direction and extremality.
- **Alternatives:** ઉપરિ સીમા / લઘુતમ ઉપરિ સીમા — possible variants; the official glossary search lead supports ઉચ્ચસીમા and ન્યૂનતમ ઉચ્ચસીમા.
- **Review question:** In Gujarati mathematical-logic prose, does “ઉચ્ચસીમા / અધઃસીમા / ન્યૂનતમ ઉચ્ચસીમા / મહત્તમ અધઃસીમા” express “upper bound / lower bound / least upper bound / greatest lower bound” with the scope stated in this rationale: The official CSTT mathematics glossary search result supports these forms, but no exact local original was acquired; formal definitions control direction and extremality. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T076: completeness property → પૂર્ણતા ગુણધર્મ

- **Status and uncertainty:** `provisional_constructed`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:76`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:174` (OLP-0048, “completeness property”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex:173` (OLP-0048, “પૂર્ણતા ગુણધર્મ”)
- **Authorities actually checked:** `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The compound matches the adopted mathematical register and is governed by the least-upper-bound definition; the checked passage supports real-system and limit language but not the exact label.
- **Alternatives:** સંપૂર્ણતા ગુણધર્મ — possible variant, but પૂર્ણતા is the concise transparent modifier used with the controlling least-upper-bound definition.
- **Review question:** In Gujarati mathematical-logic prose, does “પૂર્ણતા ગુણધર્મ” express “completeness property” with the scope stated in this rationale: The compound matches the adopted mathematical register and is governed by the least-upper-bound definition; the checked passage supports real-system and limit language but not the exact label. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T077: Dedekind cut → ડેડેકિન્ડ કાપ

- **Status and uncertainty:** `provisional_compound`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:77`.
- **English use:** No exact literal occurrence found in the current drafted units; see the usage-location note.
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex:13` (OLP-0048, “ડેડેકિન્ડ કાપ”)
- **Authorities actually checked:** `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked history directly attests Dedekind's Gujarati name; the mathematical glossary search result supports કાપ for cut, but the full glossary was not locally acquired.
- **Alternatives:** ડેડેકિન્ડ છેદ — possible literal alternative, but the official glossary search lead supports કાપ for this named construction.
- **Review question:** In Gujarati mathematical-logic prose, does “ડેડેકિન્ડ કાપ” express “Dedekind cut” with the scope stated in this rationale: The checked history directly attests Dedekind's Gujarati name; the mathematical glossary search result supports કાપ for cut, but the full glossary was not locally acquired. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T078: Cauchy sequence / convergence / limit → કોશી શ્રેણી / અભિસાર / લક્ષ

- **Status and uncertainty:** `adopted`; low. Direct authority supports the choice; regional and specialist usage may still be reported.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:78`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:15` (OLP-0048, “Cauchy sequence”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:73` (OLP-0048, “limit”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex:11` (OLP-0048, “કોશી શ્રેણી”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:67` (OLP-0048, “લક્ષ”)
- **Authorities actually checked:** `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P062` (GU-VK-CAUCHY, {"line_one_based": 3, "last_line_one_based": 3, "utf8_start": 4658, "utf8_end": 6713, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The exact Cauchy-sequence name and the convergence and limit vocabulary occur directly in checked scholarly Gujarati prose.
- **Alternatives:** કોશી અનુક્રમ / સીમા — possible alternatives; the checked scholarly Gujarati prose directly uses કોશી શ્રેણી, અભિસાર and લક્ષ.
- **Review question:** In Gujarati mathematical-logic prose, does “કોશી શ્રેણી / અભિસાર / લક્ષ” express “Cauchy sequence / convergence / limit” with the scope stated in this rationale: The exact Cauchy-sequence name and the convergence and limit vocabulary occur directly in checked scholarly Gujarati prose. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T079: even / odd → યુગ્મ / અયુગ્મ

- **Status and uncertainty:** `adopted_contextual`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:79`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:23` (OLP-0048, “even”); `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:66` (OLP-0048, “odd”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex:60` (OLP-0048, “યુગ્મ”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:60` (OLP-0048, “અયુગ્મ”)
- **Authorities actually checked:** `GU-P058` (GU-VK-MATH, {"line_one_based": 75, "last_line_one_based": 80, "utf8_start": 36000, "utf8_end": 40685, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** યુગ્મ is directly attested for even natural numbers; અયુગ્મ is the established paired opposite already used consistently in the edition.
- **Alternatives:** સમ / વિષમ — familiar alternatives, while the checked mathematical source directly attests યુગ્મ for even and the edition uses its paired opposite અયુગ્મ.
- **Review question:** In Gujarati mathematical-logic prose, does “યુગ્મ / અયુગ્મ” express “even / odd” with the scope stated in this rationale: યુગ્મ is directly attested for even natural numbers; અયુગ્મ is the established paired opposite already used consistently in the edition. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T080: decimal expansion / rational approximation → દશાંશ વિસ્તરણ / સંમેય આસન્ન મૂલ્ય

- **Status and uncertainty:** `provisional_descriptive`; open. No checked authority fully settled this exact technical label; treat it as provisional.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:80`.
- **English use:** `upstream/content/sets-functions-relations/arithmetization/cauchy.tex:23` (OLP-0048, “decimal expansion”)
- **Gujarati use:** `gu/content/sets-functions-relations/arithmetization/cauchy.tex:23` (OLP-0048, “દશાંશ વિસ્તરણ”); `gu/content/sets-functions-relations/arithmetization/cauchy.tex:39` (OLP-0048, “સંમેય આસન્ન મૂલ્ય”)
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
- **English use:** `upstream/content/sets-functions-relations/infinite/dedekind-algebra.tex:93` (OLP-0051, “Dedekind infinite”)
- **Gujarati use:** `gu/content/sets-functions-relations/infinite/dedekind-algebra.tex:101` (OLP-0051, “ડેડેકિન્ડ-અનંત”)
- **Authorities actually checked:** `GU-P048` (GU-VK-INFINITY, {"line_one_based": 57, "last_line_one_based": 80, "utf8_start": 16162, "utf8_end": 20186, "byte_basis": "UTF-8 raw extract bytes"}); `GU-P060` (GU-VK-MATH, {"line_one_based": 375, "last_line_one_based": 375, "utf8_start": 122403, "utf8_end": 124473, "byte_basis": "UTF-8 raw extract bytes"})
- **Chosen sense and rationale:** The checked infinity passage states exactly Dedekind's proper-subset definition of an infinite set. The named compound follows the edition's established Gujarati spelling of Dedekind.
- **Alternatives:** ડેડેકિન્ડીય અનંત — a possible inflected eponym; the hyphenated form keeps the name and defined property visibly separate.
- **Review question:** In Gujarati mathematical-logic prose, does “ડેડેકિન્ડ-અનંત” express “Dedekind infinite” with the scope stated in this rationale: The checked infinity passage states exactly Dedekind's proper-subset definition of an infinite set. The named compound follows the edition's established Gujarati spelling of Dedekind. If not, which attested form and inflection should replace it, and at which listed target locations?

### GU-T083: closure / f-closed → સંવરણ / f-સંવૃત

- **Status and uncertainty:** `adopted_derivation`; medium. The head term is supported, but its derivation, context or scope needs expert confirmation.
- **Record origin:** retrospective_reconstruction_from_prior_TERM_DECISIONS; `TERM_DECISIONS.jsonl:83`.
- **English use:** `upstream/content/sets-functions-relations/infinite/card-sb.tex:25` (OLP-0054, “closure”)
- **Gujarati use:** `gu/content/sets-functions-relations/infinite/card-sb.tex:16` (OLP-0054, “સંવરણ”)
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
- **Gujarati use:** `gu/content/sets-functions-relations/functions/functions-relations.tex:75` (OLP-0023, “એકરૂપતા”); `gu/content/sets-functions-relations/functions/functions-relations.tex:19` (OLP-0023, “એકરૂપ”)
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
