# MCQ Rules — lesson.maths

Grounded in supacharge-tech.md §4 ("MCQ questions per subtopic (3 to 5,
predefined answers)") and the shipped app contract (McqQuestion.fromJson in
lms_sdk; subtopic_end exercise batches in ReplayLessonEngine).

- 3 to 5 questions per subtopic, every subtopic gets a batch.
- Predefined answers only: each question carries its options and a 0-based
  `correct_index`. No open-ended entries in mcq.json.
- Question ids unique across the lesson (`<subtopic_ref>_q<n>`).
- 4 options preferred, minimum 2, all distinct; distractors must be
  plausible mistakes for this grade (sign errors, swapped factors), not
  filler.
- `time_limit_seconds` defaults to 30; only raise it for genuinely longer
  working.
- Do not rename JSON keys: `id`, `question`, `options`, `correct_index`,
  `time_limit_seconds` are parsed by the app as-is.
- Comprehension check questions (comprehension_check.json) are the
  open-ended complement: short "explain it back" prompts with an
  `expected_answer` for the reviewer, not shown as MCQs.
