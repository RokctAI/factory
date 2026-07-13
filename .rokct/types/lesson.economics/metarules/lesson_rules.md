# Lesson Rules — lesson.economics

Grounded in agent/replay/docs/supacharge-tech.md §4 "Content Production
Pipeline". One lesson-creation pass covers exactly one subtopic and produces
all of the §4 output items.

## Script
- 15 minutes of teaching, written to be spoken aloud by the tutor persona.
- One `## Subtopic: <title>` heading per subtopic marker.
- The example problem from the job card must be worked in full: if it is a
  calculation (elasticity, multiplier, CPI/inflation, exchange rates), show
  formula, substitution, and answer with units (R, %, index points); if it
  is a graph question, narrate the construction of the graph axis by axis,
  curve by curve, shift by shift.
- Use South African context in every example (rand values, SARB, Stats SA
  figures described generically — never invent precise current statistics).
- Define every economics term the first time it is used, in CAPS phrasing.
- End with a short signoff in the tutor's voice.

## Tutor personas (same topic, different production — §4)
- **Grandmaster — formal**: fast reveal, sharp, definition and formula first.
- **Big John — simplistic, lower grade logic**: slow reveal, real world
  first (spaza shop, taxi fare, grocery prices), theory named last.
- Never blend the two voices in one script.

## Manim file
- Manim Community edition, one Scene class, whiteboard style.
- Economics is graph-led: demand/supply axes drawn first, curves added one
  at a time, shifts animated as movements with old and new equilibria
  labelled. Circular-flow and market-structure diagrams built up
  component by component.
- Label every axis, curve, and equilibrium point; use MathTex for formulas.

## Subtopic markers / MCQ / reel
- Same structural contracts as lesson.maths (see mcq_rules.md): sequential
  refs, contiguous timestamps totalling ~900 s, 3–5 predefined-answer MCQs
  per subtopic whose distractors are real learner errors (shift vs movement
  along a curve, elastic vs inelastic reversed, nominal vs real confusion).
- Reel clip: exactly 60 seconds, single best moment, hook in under 5 s.
