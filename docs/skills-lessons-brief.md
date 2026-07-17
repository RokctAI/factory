# Task Brief: Skills Category — Same Lesson Pipeline, Not-Scheduled Flag

> Self-contained brief for a fresh session. Read in full; should not require the conversation that
> produced it. Real product decision made: a "skill" (e.g. Geography's cross-term "Gradient calculation")
> is structurally identical to any other lesson — same 7 content items (script, Manim scene, subtopic
> markers, MCQs, comprehension check, reel clip, Mandy Q&A), same subtopic/MCQ pipeline, **nothing
> simplified or given a different content shape**. The only real distinction is scheduling: a skill lesson
> never gets a live broadcast slot — it lives in the Library as always-available, on-demand content from
> the moment it's produced.

## What NOT to do — read this first

Do not design a separate "Skills" content pipeline, separate doctype shape, or separate folder structure
with different fields. This is explicitly wrong per the product decision. Reuse the exact existing
`lesson.*` job-card/Level-0-through-6 pipeline unchanged in shape.

## What to actually build

1. **A "library-only, not scheduled" flag** on the lesson job card schema (`template_lesson.md` and every
   real card) — a boolean or status-like field (your call on exact naming, but keep it consistent with
   existing card field conventions) marking a lesson as never eligible for live-broadcast scheduling. Check
   how scheduling currently reads job cards (if it does yet — the live-broadcast scheduling side may not
   be fully built; confirm before assuming this flag needs to integrate with something that doesn't exist)
   and make sure this flag is respected wherever that logic lives or will live.
2. **A `requires_skill` reference field** on lessons that depend on a skill — pointing at the skill
   lesson's id. This is a simple reference, not a new relationship/linking system (don't build something
   like the past-papers `links.json` bidirectional index for this — a lesson either has zero or one
   `requires_skill` reference, much simpler than the past-paper many-to-many case).
3. **Retag the existing `term: "all"` entries** — the two Geography entries currently marked `term: "all"`
   (Gradient calculation, Map scale and distance) are exactly the kind of content this flag is for. Decide
   whether `term: "all"` itself should be replaced by this new flag, or whether they're orthogonal (a
   skill could still nominally have a term for curriculum-tracking purposes even though it's never
   scheduled by term) — check with real reasoning, don't just assume one subsumes the other.
4. **Identify which other seed entries should get tagged as skills** — cross-term ATP categories (skills
   that get taught throughout the year rather than in one term slot) are the natural candidates. Don't
   guess; check the DBE ATP sources already used for term verification (per the existing
   `atp_drift_check.py`/`_sources` convention) for which topics are explicitly cross-term, and tag only
   those with real evidence.
5. **Wire `requires_skill` on any topic that genuinely depends on a skill** — this needs real judgment
   per subject/topic (e.g. does "Quadratic Equations" depend on a general algebra-manipulation skill
   lesson?). Only tag where there's a real, defensible pedagogical dependency — don't tag broadly just to
   populate the field.

## Coordination with the LMS app side

A companion brief (`agent/lms/docs/skills-app-wiring-brief.md`) covers how the app surfaces
`requires_skill` — pre-session assessment skill-tagged questions, a soft (non-forcing) suggestion at
attendance-confirmation time. That's a different repo/session's work. This brief is scoped to the data
model and content-pipeline side only: the flag exists, the reference field exists, and both are populated
with real, evidenced values. Don't build the app-side UI/notification logic here.

## Deliverable

The `library-only`/`requires_skill` fields added to the schema, the two existing Geography `term: "all"`
entries correctly tagged, a real evidenced pass over the rest of the 215-row seed to tag any other
cross-term skills and their dependents, and confirmation that Level 0's scheduling logic (wherever it
currently or will live) actually respects the library-only flag. Report back with evidence — which entries
got tagged and why, cited against real ATP sources.
