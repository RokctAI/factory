# Lesson Rules — lesson.maths

Grounded in agent/replay/docs/supacharge-tech.md §4 "Content Production
Pipeline". One lesson-creation pass covers exactly one subtopic and produces
all of the §4 output items — no partial passes.

## Script
- 15 minutes of teaching, written to be spoken aloud by the tutor persona.
- One `## Subtopic: <title>` heading per subtopic marker.
- The example problem from the job card must be worked in full, step by step.
- End with a short signoff in the tutor's voice.

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
