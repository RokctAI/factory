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
  and by the regeneration consumer (`lessons/scripts/regen_denied.py`, run by
  `.github/workflows/lesson_regeneration.yml`) which re-queues denied lessons.

A lesson with no file here is **pending** review.

## What happens on denial

`regen_denied.py` re-enters each newly denied lesson into generation with the
reviewer's `reason` attached:

- **Pipeline lessons** (job-card lessons): the card is moved back to
  `.rokct/agent/jobs/pending/`, its `status` is reset to `concept_generated`
  (the direct-authoring "fix the content" state), `concept_status` is reset
  to `pending` so the human concept gate re-arms, and the reason is written
  into a `review_feedback` frontmatter field — the card is the generation
  brief, so the feedback rides into the next authoring pass.
- **Session lessons** (folder-is-the-contract packages): a regeneration brief
  is written to `regen/<lesson_id>.md` with the reason, the package path, and
  the authoring contract. An authoring session consumes the brief and deletes
  it in the commit that rewrites the package.

State lives in `regen_state.json` (per lesson: `attempts`,
`last_reviewed_at`, `last_queued_at`, `parked`), surfaced in the review index
as a `regen` block. A given denial (`lesson_id` + `reviewed_at`) queues
exactly once — re-runs are no-ops until a newer denial arrives. **Max 2
regeneration attempts per lesson**: a third denial sets `parked: true` and
queues nothing — the lesson then needs human intervention. An `approved`
review clears the lesson's regen state and removes any pending regen brief.

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
