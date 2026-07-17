# Task Brief: Tutor Persona Cards for the Lesson Pipeline

> Self-contained brief for a fresh session. Read in full; should not require the conversation that
> produced it. The `lesson.*` pipeline is built and working (see `lesson-pipeline-levels-0-4-brief.md`,
> `lesson-organization-and-tutor-audit-brief.md`, `lesson-ai-crosscheck-brief.md` — all done and verified).
> This brief adds a missing piece: right now a job card's `tutor:` field is just a bare string
> (`tutor: Grandmaster — formal`) with no canonical reference backing it, so each Jules session
> generating a lesson script re-derives "what does Grandmaster sound like" from scratch rather than
> working from a consistent, reusable character profile.

## The real design, already documented — read this first

`agent/replay/docs/supacharge-characters.md` §1 "The Tutor Characters" is the canonical source. Key
facts already established there, don't re-derive or contradict them:

- **Default model**: every subject gets the same two-character formula — **Expert** (teaches correctly and
  formally) + **Simplifier** (teaches the logic underneath, everyday language). This is the default for
  *every* subject, not just Maths.
- Named examples given: Maths = Grandmaster (real name Mr Zulu) + Big John; Physical Science = Ms Dlamini
  ("Science Queen") + a Simplifier; Accounting = Prof Mokoena ("Numbers Never Lie") + a Simplifier;
  English/Life Sciences have partial examples. Geography, Economics, Mathematical Literacy don't have
  named characters yet in the doc — check whether they need them invented (following the same formula) or
  whether generic "Expert"/"Simplifier" placeholders are acceptable until named.
- **Same tutors span all grades in a subject** — confirmed both by the doc (Big John's origin story is
  literally teaching *Grade 12* content to a *Grade 5* student) and by the user's explicit decision this
  session: the default duo stays constant across Grade 10/11/12 for a subject. A subject *can* get an
  additional/different duo attached if deliberately decided later — support that as an override, not a
  requirement.
- Each character has: real name (if any), subject, style description, a title, a TikTok hook line, and a
  clear "who they're for" positioning (Grandmaster = students who want to excel; Big John = students who
  struggle). Four character-design images are specified (neutral, smiling, thinking, signoff gesture) —
  that's app/asset production, not this brief's concern, but the *textual* profile (style, voice, bio) is.

## What to build

A **tutor persona card** per character — a file (mirroring the existing `.rokct/types/lesson.<subject>/`
metarules convention structurally, but tutor-scoped, not subject-scoped, since a tutor can span multiple
grades within a subject and potentially attach to more than one subject) containing at minimum:

- Name, real name (if any), title
- Subject(s) they're attached to (supporting the "can attach an additional duo to a subject" extensibility
  the user wants — a tutor isn't hardcoded to exactly one subject in the data model, even if today's
  default is one duo per subject)
- Style/teaching philosophy (the Expert-vs-Simplifier description from the source doc, expanded with
  concrete guidance Jules can actually act on — e.g. Grandmaster: "formula first, then application,
  precise technical notation, fast pacing"; Big John: "logic first, everyday analogies, patient, slower
  reveals")
- Bio (for eventual student-facing display, matching `TutorProfile.bio` in `agent/lms/dart/lib/src/domain/models/tutor_models.dart`
  — check that Dart model's fields for what the app side already expects, so the factory-side card and the
  eventual app-facing tutor profile don't drift into incompatible shapes)
- Voice characteristics — a placeholder section for now (pace, tone, register) since actual VibeVoice
  voice generation is Level 6 (still unbuilt), but capture what's known/decided now so Level 6 has
  something real to work from later rather than starting blank
- TikTok hook line(s), per `supacharge-characters.md` §2 (useful for the reel-clip content item Level 2
  already generates)

## Wire it into the pipeline

1. Level 0/1's tutor-selection logic (fixed in a prior session to reason about teaching-style fit rather
   than defaulting to Grandmaster always — check `lesson-organization-and-tutor-audit-brief.md`'s evidence
   for how that currently works) should select from the actual defined tutor cards for that subject, not
   an unconstrained free-text choice between two hardcoded names.
2. Level 2's Jules prompt (concept expansion — the step that generates the actual script, Manim scene,
   etc.) should include the selected tutor's full persona card content, not just the bare `tutor:` field
   string, so the generated script actually reflects the character's established voice consistently
   across lessons rather than Jules reinventing "what does Grandmaster sound like" per session.
3. Default every subject that doesn't yet have a named duo to a generic Expert/Simplifier pair using the
   same formula, rather than leaving subjects without a name un-attachable to any tutor — check which of
   the six live subjects (Maths, Physical Sciences, Economics, Geography, Mathematical Literacy,
   Accounting) currently lack a named character per the source doc, and either invent names following the
   established formula (real-name/title/TikTok-hook pattern) or use clearly-labeled generic placeholders —
   your call, but be consistent and don't silently leave a gap.

## What NOT to do

- Don't grade-lock tutors — this was explicitly decided against this session. Same duo spans all grades
  in a subject by default.
- Don't touch the app-side Dart `TutorProfile`/`SeededTutorCatalog` in `agent/lms/dart` directly — this
  brief is about factory-side content generation having a real character reference, not about changing the
  app's tutor-discovery UI. If the two should eventually share data, note that as a follow-up, don't
  merge them in this pass.
- Don't invent voice/audio specifics that would conflict with Level 6 when it's eventually built — keep
  the voice-characteristics section as documented intent, not a hard technical spec, since VibeVoice
  integration doesn't exist yet.

## Deliverable

A tutor persona card per character (at least the four named in the source doc, plus a decision — invented
names or generic placeholders — for the remaining subjects), wired into Level 1's selection and Level 2's
Jules prompt so a real lesson generation demonstrably uses the card's content (show the actual prompt
that got sent to Jules for a test lesson, with the persona card content visibly included). Report back
with evidence, same rigor as the rest of this project's work.
