# Task Brief: Link Real Past Papers to Lesson Content

> Self-contained brief for a fresh session. Read in full; should not require the conversation that
> produced it. Follow-on to the "ground content in real past papers" idea noted (not scoped) in
> `lesson-pipeline-levels-0-4-brief.md`. Real, free CAPS/NSC-aligned South African past exam papers exist
> (Testpapers, SA Exam Papers, WCED ePortal, the DBE's own site) — this brief scopes actually using them.

## The goal

For each subject/grade (matching the lesson pipeline's existing 215-row `caps_seed.json` coverage), fetch
real past exam papers per year, identify which questions correspond to which already-built lesson
topic/subtopic, and attach each matched question to that lesson as a **real past-paper worked example**
— complete with its own Manim animation solving it — while keeping a durable, bidirectional link between
the source paper and the lesson so a verification pass can trace either direction (paper → which lessons
used its questions; lesson → which real papers back its examples).

## What to actually build

1. **Paper sourcing**: fetch real past papers per subject/grade/year from a source already confirmed free
   and usable (Testpapers, SA Exam Papers, WCED ePortal — verify current terms of use/robots.txt before
   scraping any of them, same diligence already applied to the Musina tender scraper). Store the source
   papers (PDF or extracted text) somewhere sensible — check if `lessons/curriculum/` or a new
   `lessons/past_papers/` directory fits the existing structure better.
2. **Question extraction + topic matching**: parse each paper into individual questions, then match each
   question to the closest existing lesson topic/subtopic in `caps_seed.json`'s subject/grade/topic
   taxonomy — this is a real content-understanding task, likely needing an AI pass (Groq/Jules, same
   mechanism the rest of this pipeline already uses) rather than pure keyword matching, since past-paper
   question phrasing won't exactly match topic names. Don't force a match if none is genuinely close —
   an unmatched question should be recorded as unmatched, not forced onto the nearest topic.
3. **New content item per matched question**: a real past-paper worked example — the question text (with
   proper attribution: paper source, year, question number), a Manim animation solving it (same
   convention as the lesson's own `manim_scene.py`), and the link back to the source paper. This is
   additive to the existing 7 content items (per `supacharge-tech.md` §4), not a replacement for any of
   them — decide where it lives in the job-card/content-file structure (a new field/file alongside
   `script.md`/`manim_scene.py`/etc., matching the existing `lessons/<subject>/<grade>/<term>/<id>/`
   layout).
4. **Bidirectional linking, durable and queryable**: the lesson's content should reference which real
   paper(s)/question(s) back its examples, and there should be a way to go the other direction — given a
   paper, find which lessons used which of its questions. A simple structured index (JSON/markdown table)
   is probably sufficient; don't over-engineer this into a database unless there's real evidence of scale
   requiring it.
5. **Verification hook**: whatever pass currently checks lesson content for correctness (Level 3's
   structural checks, the Level 3.5 independent AI crosscheck) should be able to look up a lesson's linked
   past-paper source when verifying — this is the actual payoff of the bidirectional link, not just a nice
   metadata addition.

## What NOT to do

- Don't scrape past papers without checking each source's actual terms of use first — same diligence
  standard as everything else touching external sites in this codebase.
- Don't force-match every question to a topic — an honest "no good match" beats a wrong one, especially
  since this feeds verification.
- Don't retrofit this into all 215 existing seed rows at once — start with a small, real test (one
  subject/grade/year) and prove the fetch→match→link→verify loop works end to end before scaling up.
- Don't duplicate content generation — this is about *sourcing real examples and linking them*, not
  regenerating lesson scripts/content that already exists.

## Deliverable

A working fetch→match→link pipeline proven on at least one real subject/grade/year of past papers, with
at least one lesson that now has a real, attributed, animated past-paper worked example, and a
demonstrated bidirectional lookup (paper→lesson, lesson→paper) working. Report back with evidence — the
actual matched question, its source citation, and the generated example — not just "built."
