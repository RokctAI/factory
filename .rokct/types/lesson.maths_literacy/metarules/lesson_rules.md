# Lesson Rules — lesson.maths_literacy

Grounded in agent/replay/docs/supacharge-tech.md §4 "Content Production
Pipeline". One lesson-creation pass covers exactly one subtopic and produces
all of the §4 output items.

## Script
- 15 minutes of teaching, written to be spoken aloud by the tutor persona.
- One `## Subtopic: <title>` heading per subtopic marker.
- Mathematical Literacy is CONTEXT-FIRST by curriculum design: every
  quantity lives in a real document or situation (a municipal bill, a till
  slip, a bank statement, a floor plan) — never teach the bare formula
  before the context that needs it.
- The example problem from the job card must be worked in full with every
  step shown: reading the values out of the context, the substitution, the
  arithmetic, and a final answer IN CONTEXT with real units (rands, kWh,
  litres) — NSC ML marking awards the interpretation sentence.
- Apply CAPS ML rounding discipline: money to two decimals, and round UP
  when buying materials or containers regardless of the decimal.
- Formulae are given, not derived — state them plainly and move to use.
- **No greeting, self-introduction, sign-off or goodbye.** These are owned
  by tutor and assistant assets (`lessons/tutors/<slug>/greetings|signoffs/`,
  `lessons/assistants/<host>/`), which already exist — never generate them
  into a lesson script. Naming any tutor or host (including the tutor
  speaking) is self-introduction, handoff or cross-promotion and is banned
  with them. Topic framing IS allowed and expected: "Today we'll be learning
  about X" is teaching, not identity framing.
- **No bracketed or parenthetical stage directions, and no physical-action
  description.** Narration is spoken verbatim by TTS, so a line like
  "[the tutor adjusts his glasses]" or "(points at the board)" is read aloud
  to the student. Describe no gestures, movements, camera framing or facial
  expressions. Parentheses carrying maths — "(6/2 = 3)", "(m/s^2)" — are
  fine.
- Question lead-ins at MCQ boundaries ARE teaching flow and belong in the
  script (e.g. "Pause here and try a few quick questions before we
  continue"); the audio is continuous and the player pauses at the exercise
  moment.

## Tutor personas (same topic, different production — §4)
- **Grandmaster — formal**: fast reveal, sharp, procedure first.
- **Big John — simplistic, lower grade logic**: slow reveal, messy, real
  world first — a natural fit for many ML contexts, but choose per subtopic.
- Never blend the two voices in one script.

## Manim file
- Manim Community edition, one Scene class, whiteboard style.
- Recreate the source document on the board (tariff table, till slip,
  statement) and highlight the values as the script reads them out; build
  each calculation line by line.
- Use MathTex for calculations; keep currency formatting South African
  (R1 234,56).

## Subtopic markers / MCQ / reel
- Same structural contracts as lesson.maths (see mcq_rules.md): sequential
  refs, contiguous timestamps totalling ~900 s, 3–5 predefined-answer MCQs
  per subtopic whose distractors are real learner errors (wrong rounding
  direction, VAT added instead of extracted, unit conversion slips).
- Reel clip: exactly 60 seconds, single best moment, hook in under 5 s.
