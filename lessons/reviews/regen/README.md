# Regeneration briefs

Work queue for denied **session** lessons: one `<lesson_id>.md` brief per
lesson, written by `lessons/scripts/CAPS/regen_denied.py` (run by
`.github/workflows/lesson_regeneration.yml`). Each brief carries the denial
reason, the package path, and the authoring contract. An authoring session
consumes a brief by rewriting the package and deleting the brief in the same
commit; an approved review also removes it. See `../README.md` for the full
regeneration mechanism.
