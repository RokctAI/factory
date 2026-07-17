# Task Brief: Independent AI Cross-Check Before the Human Accuracy Gate

> Self-contained brief for a fresh session. Read in full; should not require the conversation that
> produced it. Follow-on to `lesson-pipeline-levels-0-4-brief.md` and
> `lesson-organization-and-tutor-audit-brief.md` (both confirmed done, verified against real data —
> six lesson subjects live: Maths, Physical Sciences, Economics, Geography, Mathematical Literacy,
> Accounting). This brief addresses a real gap: the human approving content accuracy at Level 4 is not a
> subject-matter teacher and cannot personally verify correctness across six different subjects. Rather
> than skip verification, insert an independent AI review pass before content reaches the human gate.

## The problem, precisely

Level 4's human-approval gate ("Approve content accuracy for ... (human gate 3)") currently asks a
non-teacher to approve subject content they can't personally verify. This isn't a process failure to
patch around — it's a real gap in what the gate can actually guarantee. The existing Level 3 checks
(word count, Manim scene structure, MCQ format/uniqueness, subtopic timestamp sanity, and — for maths —
a real computed answer-key verifier) catch structural and, for maths, some correctness issues. They don't
catch subject content errors in Physical Sciences, Economics, Geography, Mathematical Literacy, or
Accounting.

## What to build

Add a new automated review step — call it "Level 3.5" or fold it into Level 3, whichever fits the
existing workflow structure better once you've read it — that runs an **independent** AI pass over each
lesson's content before it reaches the human gate. "Independent" means:

1. **A different call than the one that generated the content.** Don't reuse Jules' own session or the
   same prompt context that produced the lesson — a model reviewing its own output for errors is a weak
   check (it tends to confirm its own reasoning). Use a fresh Groq/Jules call (or a different model
   entirely if one's available) with a prompt whose explicit job is finding errors, not defending the
   content. Check `.rokct/skills/agent_delegation/scripts/call_groq.py` and how Level 3's existing checks
   invoke things, to follow the established calling convention rather than inventing a new one.

2. **Scoped review criteria per subject**, since "check this for errors" is too vague to be useful:
   - Physical Sciences: unit consistency, formula correctness, whether the worked example's arithmetic
     is actually right (mirror the rigor of the existing maths answer-key verifier where the check *can*
     be computed programmatically — e.g. F=ma style substitutions — falling back to AI review only where
     it can't).
   - Economics: whether the described market mechanism (shift direction, equilibrium reasoning) is
     internally consistent and matches standard economic theory, not just "sounds plausible."
   - Geography: whether stated formulas/conversions (gradient, map-scale) and worked answers are
     numerically correct — this is programmatically checkable the same way the maths verifier is, prefer
     that over AI review where possible.
   - Mathematical Literacy / Accounting: arithmetic correctness of any worked calculations (tariffs, VAT,
     interest, reconciliation figures) — again prefer a real computed check over AI judgment wherever the
     underlying math is checkable, same philosophy as the existing quadratic-equation verifier. Reserve
     AI review for the parts that genuinely aren't computable (e.g. whether context/format is
     CAPS-appropriate).

   In short: **default to real computed verification wherever the content is checkable** (this is more
   trustworthy than an AI opinion and cheaper to run), and use the independent AI pass specifically for
   the parts that can't be reduced to a computable check (conceptual/theoretical correctness, whether an
   explanation is genuinely sound pedagogy, not just structurally complete).

3. **Clear pass/fail/flag output on the job card.** Add fields to the card schema (mirroring how
   `rules_status`/`expansion_requested` already work) — something like `crosscheck_status` and
   `crosscheck_notes` — so the human reviewer at Level 4 sees a concrete report ("Independent review found:
   [specific issues or 'no issues found']") rather than approving blind. This changes what the human is
   actually being asked to do: not "is this correct" (which they can't answer), but "given this
   independent check found X, do you want to proceed" — a question they *can* meaningfully answer.

4. **Fail-closed on ambiguity.** If the cross-check step itself errors out (API failure, malformed
   response), the card should land in a state that blocks Level 4 approval until the check actually runs
   successfully — don't let a failed check silently look like a passed one. Mirror the fail-closed
   pattern already used elsewhere in this pipeline (e.g. how a failed Level 3 check currently blocks
   progression) rather than inventing a new failure mode.

## What NOT to do

- Don't replace the human gate entirely — the AI cross-check is a second opinion presented *to* the human,
  not a replacement for human judgment. The human's job becomes "read the independent review and decide,"
  not "personally verify subject accuracy from scratch."
- Don't build one giant generic "check this for errors" prompt across all six subjects — that's exactly
  the kind of vague check that produces false confidence. Scope it per subject as described above.
- Don't skip the "prefer real computed checks over AI judgment" principle just because AI review is easier
  to build generically — the existing maths answer-key verifier is trusted specifically *because* it's a
  real computation, not an LLM opinion. Extend that pattern wherever the content allows it before falling
  back to AI review.

## Deliverable

The cross-check step running for real content in at least 2-3 different subjects (not just maths, since
that's already covered by the existing verifier), with at least one deliberately-corrupted test case per
subject category (computed-check subjects: a wrong-answer test, same pattern as the existing maths
corruption test; AI-review subjects: a deliberately-wrong conceptual claim) proving the check actually
catches errors rather than always passing. Report back with the evidence per subject, matching the rigor
already established in this project's other verification work — don't just report "built and running."
