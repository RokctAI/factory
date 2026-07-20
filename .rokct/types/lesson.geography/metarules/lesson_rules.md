# Lesson Rules — lesson.geography

Grounded in agent/replay/docs/supacharge-tech.md §4 "Content Production
Pipeline". One lesson-creation pass covers exactly one subtopic and produces
all of the §4 output items.

## Script
- 15 minutes of teaching, written to be spoken aloud by the tutor persona.
- One `## Subtopic: <title>` heading per subtopic marker.
- Mapwork calculations (scale, distance, gradient, vertical exaggeration,
  magnetic declination) are worked in full, step by step: formula first,
  conversion of units shown explicitly (cm → m → km), answer stated in the
  NSC answer format (e.g. gradient as 1:15).
- Process topics (cyclones, fluvial processes, settlement) are taught as a
  labelled-diagram narrative: describe what the learner should be seeing at
  each stage while the diagram builds.
- Use South African place-based examples wherever CAPS does (Western Cape
  winter rainfall, Highveld anticyclonic conditions, Gauteng urban
  hierarchy).
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
- **Grandmaster — formal**: fast reveal, sharp, terminology first.
- **Big John — simplistic, lower grade logic**: slow reveal, real world
  first (the weather you felt this week, the taxi route through town),
  terminology named last.
- Never blend the two voices in one script.

## Manim file
- Manim Community edition, one Scene class, whiteboard style.
- Geography is diagram-led: cross-sections, synoptic-chart symbols, cyclone
  stage diagrams, and river profiles are constructed element by element in
  sync with the script — never shown complete at once.
- Use MathTex for mapwork calculations and ratios.

## Subtopic markers / MCQ / reel
- Same structural contracts as lesson.maths (see mcq_rules.md): sequential
  refs, contiguous timestamps totalling ~900 s, 3–5 predefined-answer MCQs
  per subtopic whose distractors are real learner errors (inverted ratios,
  wrong unit conversions, hemisphere/rotation confusion on cyclones).
- Reel clip: exactly 60 seconds, single best moment, hook in under 5 s.
