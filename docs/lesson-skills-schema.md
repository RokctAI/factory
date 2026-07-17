# Skills Schema — the app-side contract

> Built 2026-07-16, replacing the ad-hoc `term: "all"` convention. This document is the
> ground truth for app-side work (pre-session assessment skill-check tagging; the
> non-forcing "review this skill first?" suggestion on attendance confirmation).
> Everything below is implemented and validated in the factory repo — nothing is aspirational.

## The one-sentence model

A **skill lesson** is structurally identical to any other lesson — same seven content
items, same job-card pipeline (Levels 0–4), same human gates — the **only** distinction
is scheduling: a skill lesson never gets a live broadcast slot; it lives in the Library
as always-available on-demand content.

## Job-card fields (frontmatter, exact names)

| Field | On | Value | Meaning |
|---|---|---|---|
| `category` | skill lesson cards | `skill` | Library-only: never scheduled for live broadcast. Absent/empty = standard schedulable lesson. |
| `skill_ref` | skill lesson cards | `<subject_slug>.<skill_slug>` e.g. `geography.gradient_calculation` | The **stable reference id**. Card ids embed content hashes (`..._dc21d0`) and change if reseeded; `skill_ref` is what everything else points at. Unique across the repo (validated). |
| `requires_skills` | any lesson card | comma-separated `skill_ref`s, e.g. `geography.gradient_calculation` | This lesson assumes the student has the skill. Empty/absent = no prerequisite skills. |
| `term` | skill lesson cards | *(empty)* | Skills are term-independent by design. Standard lessons keep `term: 1-4` or `unknown`. `"all"` is retired and no longer a valid term. |

## Content location

- Standard lesson: `lessons/<subject>/grade<g>/term<t>/<card_id>/`
- Skill lesson: `lessons/<subject>/grade<g>/skills/<card_id>/`

Skills stay **grade-scoped** (CAPS assesses the same skill at different depths per
grade — a G12 gradient question expects more than G10) but carry no false term claim.

## `lessons/skills_index.json` — the lookup the app reads

Generated (never hand-edited) by `python lessons/scripts/lesson_pipeline.py skills-index`,
which **fails (exit 1)** if: a `category: skill` card lacks a `skill_ref`, a `skill_ref`
is defined twice, any `requires_skills` entry doesn't resolve, or a card requires itself.

```json
{
  "generated": "YYYY-MM-DD HH:MM:SS",
  "skills": {
    "<skill_ref>": {
      "card_id": "…",           // current job-card id (hash-suffixed)
      "card_file": "…",          // repo path of the job card
      "subject": "Geography",
      "grade": 12,
      "topic": "…",
      "subtopic": "…",
      "lesson_name": "…",        // empty until Level 2 fills it
      "lesson_path": "…",        // empty until content exists
      "status": "evaluated",     // pipeline status; only 'evaluated' skills are servable
      "required_by": ["<card_id>", "…"]   // reverse edges, for impact analysis
    }
  }
}
```

**App-side rule of thumb:** join on `skill_ref` (stable), read `status` to know whether
the skill's content is actually servable, and treat `required_by` as informational.

## How the app is expected to use `requires_skills`

For a session whose lesson card lists `requires_skills`:

1. **Pre-session assessment**: include one question tagged with each required
   `skill_ref` (skill-check question), so the assessment can tell "doesn't know the
   topic" apart from "missing the underlying skill".
2. **Attendance confirmation**: when a student confirms attendance, surface a
   non-forcing suggestion — "This session uses *Gradient calculation*. Review it in the
   Library first?" — linking to the skill lesson's content. Never block attendance on it.
3. **Scheduling**: skill lessons never appear in the broadcast schedule. They are
   Library items only.

## Current real data (migrated from `term: "all"`)

- `geography.gradient_calculation` → card `…gradient_ca_dc21d0` (**evaluated**, full
  content at `lessons/geography/grade12/skills/…dc21d0/`), required by the G12
  Geomorphology *River profiles and rejuvenation* lesson (river gradient computation is
  part of profile analysis).
- `geography.map_scale_and_distance` → card `…map_scale_a_eb274e` (pending approval, no
  content yet).

## Validation surface (factory side, already wired)

- `lesson_pipeline.py check` (Level 3) fails a card whose `requires_skills` doesn't
  resolve, whose `skill_ref` is set without `category: skill`, or vice versa.
- `lesson_pipeline.py skills-index` validates the whole graph and regenerates the index.
- `lesson_pipeline.py seed` refuses skill seed rows without `skill_ref` or with a `term`.
- `atp_drift_check.py` reports where a skill's topic appears in the ATPs but never
  flags a skill as term drift.
