# Lesson Rules — lesson.accounting

Grounded in agent/replay/docs/supacharge-tech.md §4 "Content Production
Pipeline". One lesson-creation pass covers exactly one subtopic and produces
all of the §4 output items.

## Script
- 15 minutes of teaching, written to be spoken aloud by the tutor persona.
- One `## Subtopic: <title>` heading per subtopic marker.
- Accounting is FORMAT-DISCIPLINED: CAPS/NSC marking is anchored to the
  prescribed formats (ledger account with debit and credit sides, bank
  reconciliation statement layout, financial statement line order, budget
  schedules). Teach the format explicitly and fill it in the prescribed
  order — a right number in the wrong place loses the mark.
- The example problem from the job card must be worked in full: name each
  source document or given figure, show where it enters the format, show
  the arithmetic, and balance/total visibly at the end.
- Keep the double-entry logic audible: for every entry, say what is debited,
  what is credited, and why.
- Where the ATP integrates ethics/internal control for the topic (it almost
  always does), close the subtopic with one concrete control or ethics
  point — one sentence, not a lecture.
- End with a short signoff in the tutor's voice.

## Tutor personas (same topic, different production — §4)
- **Grandmaster — formal**: fast reveal, sharp, format first.
- **Big John — simplistic, lower grade logic**: slow reveal, real world
  first (the spaza's cash box, the statement from the bank envelope),
  format named last. Choose per subtopic.
- Never blend the two voices in one script.

## Manim file
- Manim Community edition, one Scene class, whiteboard style.
- Draw the prescribed format's skeleton first (T-account rails, statement
  headings), then post each figure into it in sync with the script; totals
  and balancing lines animate last.
- South African currency formatting (R1 234,56); brackets for negatives.

## Subtopic markers / MCQ / reel
- Same structural contracts as lesson.maths (see mcq_rules.md): sequential
  refs, contiguous timestamps totalling ~900 s, 3–5 predefined-answer MCQs
  per subtopic whose distractors are real learner errors (debit/credit
  reversed, VAT extracted with 15% of the inclusive amount, outstanding
  items on the wrong side of the reconciliation).
- Reel clip: exactly 60 seconds, single best moment, hook in under 5 s.
