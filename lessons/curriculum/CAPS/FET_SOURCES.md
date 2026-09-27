# CAPS Grades 10-12 source documents (FET band)

Fetched 2026-09-27 straight from the Department of Basic Education site by
`lessons/scripts/CAPS/fetch_fet_sources.py`. This covers the FET subjects beyond the original six
(Maths, Maths Literacy, Physical Sciences, Accounting, Economics, Geography). The script finds each
link by its label on the CAPS FET page and the national ATP index. It records every file's DBE source
URL, edition, size and sha256 in `fet_sources.json`: 138 PDFs, about 100 MB. Run
`python3 fetch_fet_sources.py --verify` to re-hash them.

Content subjects are the English versions. Each language is in its own language. Every ATP is the
2023/24 edition, the current one on the DBE index. Sepedi prints the year as "20203/24".

Syllabus JSON sits beside the PDFs as `{subject}/syllabus/grade{10,11,12}.json` (54 files). It is
built by `lessons/scripts/CAPS/extract_fet_syllabus.py`. Every file has the same shape as the other
syllabi. It carries `"pipeline_enabled": false` and a `pathway` block. None of these folders is in
`CAPS_TYPE_BY_FOLDER`, so no FET row reaches lesson generation until a subject is added there and the
flag is removed.

`parse_status` is `extracted`, not `curated`. The topics, subtopics, weeks and SBA tasks are read from
the ATP tables mechanically and have not been reviewed by hand. Known noise:

- a few wrapped lines are split into two subtopics;
- scattered exam-table fragments;
- some overlaid text in English FAL Grade 12 Terms 2-3, where DBE's PDF prints two text layers on top
  of each other.

Review a subject before you switch it on.

## Layout

Same as the other grades:

- `{subject}/curriculum/caps_gr10-12.pdf` is the CAPS policy document.
  CAT and IT also have `caps_gr10-12_amendment_2024_section3.pdf`, the 2024 replacement of Section 3.
- `{subject}/syllabus/grade{N}_atp.pdf` is the Annual Teaching Plan.
- `{subject}/syllabus/grade{N}.json` is the syllabus, for the subjects marked JSON below.

English HL, English FAL and Life Orientation share their existing Grades R-9 folders.

| Subject | CAPS | ATP Gr 10 | ATP Gr 11 | ATP Gr 12 | Syllabus JSON |
|---|---|---|---|---|---|
| english_home_language | ✓ | ✓ | ✓ | ✓ | ✓ |
| english_first_additional_language | ✓ | ✓ | ✓ | ✓ | ✓ |
| afrikaans_home_language | ✓ | ✓ | ✓ | ✓ | ✓ |
| afrikaans_first_additional_language | ✓ | ✓ | ✓ | ✓ | ✓ |
| isizulu_home_language | ✓ | ✓ | ✓ | ✓ | ✓ |
| isizulu_first_additional_language | ✓ | ✓ | ✓ | ✓ | ✓ |
| isixhosa, isindebele, sepedi, sesotho, setswana, siswati, tshivenda, xitsonga (HL and FAL each) | ✓ | ✓ | ✓ | ✓ | — |
| life_sciences | ✓ | ✓ | ✓ | ✓ | ✓ |
| agricultural_sciences | ✓ | ✓ | ✓ | ✓ | ✓ |
| history | ✓ | ✓ | ✓ | ✓ | ✓ |
| business_studies | ✓ | ✓ | ✓ | ✓ | ✓ |
| life_orientation | ✓ | ✓ | ✓ | ✓ | ✓ |
| computer_applications_technology | ✓ + 2024 amendment | ✓ | ✓ | ✓ | ✓ |
| information_technology | ✓ + 2024 amendment | ✓ | ✓ | ✓ | ✓ |
| tourism | ✓ | ✓ | ✓ | ✓ | ✓ |
| consumer_studies | ✓ | ✓ | ✓ | ✓ | ✓ |
| engineering_graphics_and_design | ✓ | ✓ | ✓ | ✓ | ✓ |
| visual_arts | ✓ | ✓ | ✓ | ✓ | ✓ |
| religion_studies | ✓ | ✓ | ✓ | ✓ | ✓ |

## Gaps

- History: the CAPS FET page links only the Afrikaans CAPS. The English document is the amended
  edition that DBE hosts at a direct URL, which is recorded in the manifest.
- History Grade 12: the ATP has no Term 4 plan, so `grade12.json` has three terms.
- Afrikaans FAL Grade 10: the Term 4 plan covers four weeks.
- The eight other official languages (isiXhosa, isiNdebele, Sepedi, Sesotho, Setswana, siSwati,
  Tshivenda, Xitsonga) have their CAPS and ATP PDFs here but no syllabus JSON yet. Their ATP tables
  use a different row layout in each language, so the extraction is not reliable without a reviewer
  who reads the language.
- The fetch reported nothing missing (`gaps: []` in the manifest).

## Subject pathway

Every FET syllabus file has the same `pathway` block as the Grades R-9 files:

- `comes_from`: the Grade 9 subject (and strand) for Grade 10, otherwise the grade before;
- `leads_to`: the next grade, or the NSC examination for Grade 12;
- `fet_subjects`: the subject itself.

The mapping is in `lessons/scripts/CAPS/fet_pathways.py`.

| FET subject | Comes from (Grade 9) |
|---|---|
| Life Sciences | Natural Sciences: Life and Living |
| Agricultural Sciences | Natural Sciences (Life and Living, Matter and Materials), EMS |
| History | Social Sciences: History |
| Business Studies | EMS: Entrepreneurship |
| Life Orientation | Life Orientation |
| CAT | Technology |
| IT | Mathematics, Technology |
| Tourism | Social Sciences: Geography, EMS |
| Consumer Studies | EMS, Natural Sciences, Technology |
| EGD | Technology, Mathematics |
| Visual Arts | Creative Arts: Visual Arts |
| Religion Studies | Life Orientation, Social Sciences |
| {Language} HL / FAL | {Language} HL / FAL (Grade 9) |

## Scripts

    python3 lessons/scripts/CAPS/fetch_fet_sources.py            # fetch new or changed files, rewrite fet_sources.json
    python3 lessons/scripts/CAPS/fetch_fet_sources.py --verify   # re-hash committed PDFs
    python3 lessons/scripts/CAPS/extract_fet_syllabus.py         # write missing grade{N}.json (needs pdfplumber, pymupdf)
    python3 lessons/scripts/CAPS/extract_fet_syllabus.py history --force   # rebuild one subject

`lessons/scripts/CAPS/tests/test_fet_syllabus.py` checks the following:

- the manifest hashes match the committed PDFs;
- every subject has a CAPS document and three ATPs;
- every syllabus file is held (`pipeline_enabled: false`) and carries a pathway.
