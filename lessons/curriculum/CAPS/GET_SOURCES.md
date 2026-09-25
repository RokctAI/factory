# CAPS Grades R-9 source documents (GET band)

Fetched 2026-09-25 straight from the Department of Basic Education site, English versions only.
Every file, its DBE source URL, edition and sha256 is listed in `get_sources.json`.

Curated syllabus JSON now sits beside the PDFs as `{subject}/syllabus/grade{N}.json` (Grade R:
`gradeR.json`), 60 files in the same shape as Grades 10-12. Every one carries `"pipeline_enabled": false`,
which `load_seed_entries` and `atp_drift_check` skip, so no Grade R-9 row reaches lesson generation
until that flag is removed. `parse_status` is `curated` from the ATP, except Grade 3 English FAL
(`caps_only`, no ATP published). Grade R is built from the Grade R Resource Kit lesson plans because DBE
publishes no Grade R ATP; that scan stops at week 34, so Term 4 weeks 5-10 are missing from it.

## Layout

Same as Grades 10-12:

- `{subject}/curriculum/caps_gr{R-3|4-6|7-9|R}.pdf` holds the CAPS policy document for that phase.
- `{subject}/syllabus/grade{N}[_termT][_stream]_atp.pdf` holds the Annual Teaching Plan.
  Foundation Phase language plans are published per term. Creative Arts is published per stream (dance, drama, music, visual arts).

Maths shares the existing `maths/` folder. The new subject folders are:

| Subject | CAPS document(s) | Gr R | Gr 1 | Gr 2 | Gr 3 | Gr 4 | Gr 5 | Gr 6 | Gr 7 | Gr 8 | Gr 9 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| coding_and_robotics | R-3, 4-6, 7-9 | — | — | — | — | — | — | — | — | — | — |
| creative_arts | 7-9 | — | — | — | — | — | — | — | ✓ | ✓ | ✓ |
| economic_and_management_sciences | 7-9 | — | — | — | — | — | — | — | ✓ | ✓ | ✓ |
| english_first_additional_language | R-3, 4-6, 7-9 | — | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| english_home_language | R-3, 4-6, 7-9 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| life_orientation | 7-9 | — | — | — | — | — | — | — | ✓ | ✓ | ✓ |
| life_skills | R-3, 4-6 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — |
| maths | R-3, R, 7-9, 4-6 | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| natural_sciences | 7-9 | — | — | — | — | — | — | — | ✓ | ✓ | ✓ |
| natural_sciences_and_technology | 4-6 | — | — | — | — | ✓ | ✓ | ✓ | — | — | — |
| social_sciences | 7-9, 4-6 | — | — | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| technology | 7-9 | — | — | — | — | — | — | — | ✓ | ✓ | ✓ |

## Gaps

- Grade R: DBE publishes no 2023/24 ATP; the Grade R Resource Kit (teachers' guide here, lesson plans listed under not_committed) stands in.
- Grade 2 English HL Term 3: the DBE page links the English FAL Term 3 file under that label, so the real HL Term 3 plan is missing.
- Grade 3 English FAL: not listed on the DBE Foundation Phase ATP page.
- Coding and Robotics: CAPS documents only (draft/pilot subject); no ATPs published.
- Editions differ: most ATPs are 2023/24; IP/SP Maths and Natural Sciences carry 2026 revisions; some Foundation Phase language plans are the 2020/2021 editions DBE still links.
- The Grade R Resource Kit lesson plans are re-encoded from a 147 MB scan to about 10 MB (130 dpi greyscale) so they fit in git.
