# CAPS Grades R-9 source documents (GET band)

Fetched 2026-09-25 straight from the Department of Basic Education site, English versions only.
Every file, its DBE source URL, edition and sha256 is listed in `get_sources.json`.

These are **raw sources only**. No `syllabus/grade*.json` exists yet for Grades R-9, so the lesson
pipeline (`load_seed_entries`) and the index builders see nothing new. Curated syllabus JSON in the
same shape as the Grade 10-12 files comes next, subject by subject.

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
- Not committed: the Grade R Resource Kit lesson plans (147 MB of scans, over GitHub's file limit). The URL is in `get_sources.json` under `not_committed`.
