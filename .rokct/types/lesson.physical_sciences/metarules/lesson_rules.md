# Lesson Rules — lesson.physical_sciences

Grounded in agent/replay/docs/supacharge-tech.md §4 "Content Production
Pipeline". One lesson-creation pass covers exactly one subtopic (physics or
chemistry, per the card) and produces all of the §4 output items.

## Script
- 15 minutes of teaching, written to be spoken aloud by the tutor persona.
- One `## Subtopic: <title>` heading per subtopic marker.
- The example problem from the job card must be worked in full, step by step,
  in the CAPS marking style: formula first, substitution shown explicitly,
  answer with correct SI unit and sensible significant figures.
- Only use formulas that appear on the official NSC Physical Sciences data
  sheet; name each formula before substituting into it.
- State the physical principle (e.g. Newton's second law, conservation of
  energy, Le Chatelier) before the mathematics that applies it.
- End with a short signoff in the tutor's voice.

## Tutor personas (same topic, different production — §4)
- **Grandmaster — formal**: fast reveal, sharp, formula first.
- **Big John — simplistic, lower grade logic**: slow reveal, messy,
  real world first (push the trolley, burn the fuel), formula last.
- Never blend the two voices in one script.

## Manim file
- Manim Community edition, one Scene class, whiteboard style.
- Free-body diagrams, circuit diagrams, energy bar charts, and molecular
  sketches are built up line by line alongside the working — never dropped
  in complete.
- Use MathTex for all equations and unit notation (mol·dm⁻³, m·s⁻²).

## Subtopic markers / MCQ / reel
- Same structural contracts as lesson.maths (see mcq_rules.md): sequential
  refs, contiguous timestamps totalling ~900 s, 3–5 predefined-answer MCQs
  per subtopic whose distractors are real learner errors (dropped negative
  signs, unit slips, inverted ratios, unbalanced equations).
- Reel clip: exactly 60 seconds, single best moment, hook in under 5 s.
