# CAPS Grades R-9 source documents (GET band)

Fetched 2026-09-25 straight from the Department of Basic Education site, English versions only.
Every file, its DBE source URL, edition and sha256 is listed in `get_sources.json`.

Curated syllabus JSON now sits beside the PDFs as `{subject}/syllabus/grade{N}.json` (Grade R:
`gradeR.json`), 60 files in the same shape as Grades 10-12. Files carrying `"pipeline_enabled": false`
are skipped by `load_seed_entries` and `atp_drift_check`. The Grade 8-9 files of the subjects that feed
the six FET subjects (Maths, Natural Sciences, Social Sciences, EMS) have that hold lifted; every other
Grade R-9 file still carries it. `SEED_MIN_GRADE` in `lesson_pipeline.py` is 8 (Ray's go-ahead,
2026-10-01), so the seed step now writes Grade 8-9 cards for those four subjects.

A second switch, `"lessons_enabled"`, is whole-subject (ruled 2026-10-01: a learner who takes a subject
expects all of it). A subject is either on in full or off as a file; no topic is switched off inside an
enabled subject. On: Maths R-9, Natural Sciences 7-9 and NST 4-6, Social Sciences 4-9 (Geography and
History), EMS 7-9 (including Entrepreneurship) and Life Skills R-3 (all strands). Languages are on only
in the Foundation Phase: English Home Language in Grades R-3 (reading, writing, phonics) and First
Additional Language in Grades 1-3; both are off from Grade 4. `parse_status` is `curated` from the ATP, except Grade 3 English FAL
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

## Subject pathway (choosing subjects)

Every R-9 syllabus file has a `pathway` block: `comes_from`, `leads_to`, and `fet_subjects` (the Grade 10-12 subjects it feeds). NS, SS and EMS topics also carry their own `leads_to`, because those subjects split later.

| Grades | Subject | Leads to |
|---|---|---|
| R-3 | Life Skills (Beginning Knowledge) | NST and Social Sciences (4-6) |
| R-3 | Life Skills (PSW, PE, Creative Arts) | Life Skills 4-6 |
| 4-6 | Natural Sciences and Technology | Natural Sciences, Technology (7-9) |
| 4-6 | Life Skills | Life Orientation, Creative Arts (7-9) |
| 7-9 | Natural Sciences | Physical Sciences (Matter, Energy, Planet Earth), Life Sciences (Life and Living) |
| 4-9 | Social Sciences | Geography, History |
| 7-9 | EMS | Economics (The economy), Accounting (Financial literacy), Business Studies (Entrepreneurship) |
| R-9 | Mathematics | Mathematics, Mathematical Literacy, Technical Mathematics |
| 7-9 | Technology | EGD, Civil/Electrical/Mechanical Technology, CAT |
| 7-9 | Creative Arts | Dance, Drama, Music, Visual Arts |
| 7-9 | Life Orientation | Life Orientation 10-12 |
| R-9 | English HL / FAL | English HL / FAL 10-12 |
