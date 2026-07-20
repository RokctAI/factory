# Lesson Rules — lesson.maths

Grounded in agent/replay/docs/supacharge-tech.md §4 "Content Production
Pipeline". One lesson-creation pass covers exactly one subtopic and produces
all of the §4 output items — no partial passes.

## Script
- 15 minutes of teaching, written to be spoken aloud by the tutor persona.
- One `## Subtopic: <title>` heading per subtopic marker.
- The example problem from the job card must be worked in full, step by step.
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
  real world first.
- Never blend the two voices in one script.

## Manim file
- Manim Community edition (`from manim import ...`), one Scene class.
- Whiteboard style: build the working line by line, step by step, mirroring
  the script's teaching beats — no decorative animation.
- Use MathTex for equations (KaTeX renders them on device).

## Subtopic markers
- `subtopics.json` refs are sequential (`subtopic_1`, `subtopic_2`, ...),
  timestamps in seconds, contiguous, totalling close to 900 seconds.
- These refs are the join key for MCQ batches and the future Level 6
  manifest's subtopic_start/subtopic_end events — keep them stable.

## Reel clip
- Exactly 60 seconds, single best moment of the lesson, JSON only,
  following the factory's reel-brief hook discipline: the hook must stop
  the scroll in under 5 seconds; no summary, no theme explanation.
