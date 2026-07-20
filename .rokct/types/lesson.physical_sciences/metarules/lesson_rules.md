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
