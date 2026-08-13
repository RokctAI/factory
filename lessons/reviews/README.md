# Lesson review state

This directory holds one JSON file per reviewed lesson, named
`<lesson_id>.json`, where `<lesson_id>` matches the `id` field in
`lessons/review_index.json` (pipeline lessons use the job-card id verbatim;
session packages use `session_{subject}_g{grade}_t{term}_{topic-slug}_{subtopic-slug}`).

## Who writes and reads these files

- **Written by** the Supacharge admin review endpoint via the GitHub Contents
  API when Ray approves or denies a lesson in the app.
- **Consumed by** the review-index build
  (`lessons/scripts/build_review_index.py`, run by
  `.github/workflows/review_index.yml`) to fill each lesson's `review` block,
  and by regeneration workflows that re-queue denied lessons.

A lesson with no file here is **pending** review.

## Schema

```json
{
  "lesson_id": "maths_g11_quadratic_equations_factoring_method_31d165",
  "status": "approved",
  "reason": null,
  "reviewed_by": "RendaniSinyage",
  "reviewed_at": "2026-08-13T10:15:00Z"
}
```

| Field         | Type             | Notes                                              |
| ------------- | ---------------- | -------------------------------------------------- |
| `lesson_id`   | string           | Must equal the filename (without `.json`).         |
| `status`      | string           | `"approved"` or `"denied"` — nothing else.         |
| `reason`      | string or `null` | Free-text reviewer note; expected for denials.     |
| `reviewed_by` | string           | Reviewer identity (e.g. GitHub login).             |
| `reviewed_at` | string           | ISO 8601 UTC timestamp, e.g. `2026-08-13T10:15:00Z`. |

Files with any other `status` value (or invalid JSON) are ignored by the index
build and treated as pending, with a warning.
