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
- End with a short signoff in the tutor's voice.

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
