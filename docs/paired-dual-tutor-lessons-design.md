# Paired Dual-Tutor Lessons — Design (queued, not yet implemented)

> Status: DESIGN — queued behind the in-flight batch work. Defines the pairing
> mechanism supacharge-tech.md §4 promises ("Grandmaster and Big John cover
> identical learning objectives with the same example problem, sharing base
> Manim animations but different styling/pacing/audio"). Nothing in the
> current pipeline pairs two cards today; this document is the ground truth
> for the implementation pass. The point-2 decision below was reported to the
> owner before broad implementation.

## Decision on point 2: REUSE the scene, don't regenerate (Option B)

The second card's Level 2 pass does NOT regenerate the Manim scene. It
receives the primary card's `manim_scene.py` verbatim as fixed content and
generates only the persona-voiced artifacts around it:

- `script.md` — the secondary tutor's own voice/register (the real work)
- `subtopics.json` — same refs and titles (identical objectives), own timings
- `mcq.json` — copied from the primary (same questions, same correct answers
  — the §4 "same answers" requirement is structural, not re-generated)
- `manim_scene.py` — byte-identical copy of the primary's

Why B over regenerating with a "match this structure" constraint:

1. **It is what the doc says.** "Sharing base Manim animations but different
   styling/pacing/audio" describes reuse, not parallel regeneration.
2. **Visual parity of the actual math is guaranteed**, not hoped for. Two
   independent Jules passes can each make different small errors; a copied
   scene cannot diverge.
3. **Different pacing already falls out of the existing pipeline for free.**
   Level 6 rescales every animation primitive to the real audio duration
   per card (`anim_scale` in lesson_manifest.py). Big John's slower audio
   automatically stretches the same primitives over more time — that IS the
   "different pacing" promise, with zero new mechanism.
4. **Cheaper and safer.** Session 2 writes a script, not a scene; Level 3's
   scene checks and the answer-key verifier run against content already
   verified once; crosscheck effort halves.

Allowance: "different styling" (colors/emphasis per persona) is a Level 6 /
player concern (persona style tokens at render time), not a scene fork. If a
simplifier lesson genuinely needs a different visual beat, that is a NEW
unpaired lesson, not a pair member.

## 1. Seed schema

One row, both tutors — the pair is authored once so nothing can drift:

```json
{
  "type": "lesson.maths",
  "subject": "Maths", "grade": 12,
  "topic": "Finance, growth and decay", "subtopic": "Compound growth",
  "example_problem": "...",              // written ONCE, shared by contract
  "prior_knowledge": "...",
  "tutors": ["expert", "simplifier"]     // NEW — roster roles, not names
}
```

Seeding expands this into TWO job cards (existing single-tutor rows are
untouched; `tutors` absent = today's behaviour):

- card A: `tutor: <expert label>`,     `pair_id: <slug>_<hash>`, `pair_role: primary`
- card B: `tutor: <simplifier label>`, `pair_id: <same>`,        `pair_role: secondary`

`pair_id` is derived from (subject, grade, topic, subtopic) the same way card
hashes are — deterministic, reseed-safe. `pair_role: primary` = generates the
scene (the formal/expert version by default); `secondary` = reuses it.

## 2. Generation flow

Both cards flow Levels 0–6 independently (own gates, own production, own
release) with ONE sequencing rule:

- lesson2 skips a `pair_role: secondary` card until its primary's card shows
  `lesson_path` with a present `manim_scene.py` (i.e. primary's concept PR is
  merged). The secondary's Level 2 prompt then embeds: the primary's scene
  (as fixed, copy-verbatim content), the primary's subtopics refs/titles, the
  shared mcq.json, and the secondary persona card.
- Level 3 gains a pairing check for secondary cards: scene file hash equals
  the primary's, `example_problem` identical, MCQ ids/correct answers
  identical. A drifted pair member fails, never advances.

## 3. Visibility

- Ledger rows and the dashboard show `pair_id` for pair members; the
  dashboard groups a matched set on one line ("pair <id>: primary produced /
  secondary concept_expanding").

## 4. App side — CONFIRMED, no follow-up needed

lms_sdk already models this: `cross_tutor_test.dart` exercises
`TopicLinkResolver.alternateFor` (next same-topic session by the OTHER
tutor), the §9 signoff cross-promo, and "both tutors keep their version of
the same topic" in the library. Pair resolution is by matching topic metadata
+ different tutor across sessions — exactly what paired cards emit. The
factory-side `pair_id` never needs to reach the app; topic/subtopic/tutor
already carry the join.

## Out of scope

- Retrofitting existing single-tutor lessons into pairs (a pair starts from a
  paired seed row).
- Persona style tokens in the player (Level 6/app concern, separate work).
