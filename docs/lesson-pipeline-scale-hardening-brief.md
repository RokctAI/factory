# Task Brief: Hardening for Scale (215 Seed Rows, Not 6)

> Self-contained brief for a fresh session. Read in full; should not require the conversation that
> produced it. The `lesson.*` pipeline is built, verified, and now seeded with 215 CAPS-aligned rows
> across Grades 10–12, all six subjects (Maths, Physical Sciences, Economics, Geography, Mathematical
> Literacy, Accounting), each source-traceable to real DBE Annual Teaching Plans with automated drift
> detection. Levels 0–3.5 (structural checks, computed answer-key/arithmetic verification, independent AI
> crosscheck) are all real and adversarially tested. This brief is not new features — it's hardening for
> the fact the pipeline is about to process ~36x more volume than what it's been tested against so far.

## 1. Root-cause the intermittent Lesson 3 failures

During crosscheck testing, Lesson 3 showed intermittent fast failures (3–4 seconds, dying before any
Groq round-trip could complete) — suspected GitHub-raw fetch flakiness in the runtime-fetched scripts, but
never actually confirmed. An ERR trap was left in the workflow to capture the failing command on next
occurrence, which was the right stopgap for low volume, but at 215 rows churning through the pipeline
this will fire far more often. Find and read the trap's captured output from any occurrences since it was
added (check `ai_delegation.md` or wherever it commits its findings), and actually root-cause this —
don't just keep re-diagnosing one-off recurrences as the queue grows. If it is GitHub-raw fetch flakiness,
consider whether these runtime-fetched scripts should retry with backoff, or whether a local cached copy
(mirroring how `.rokct/initiate.py` already caches `.rokct/skills/`) would eliminate the dependency on a
live fetch mid-workflow entirely.

## 2. A real, accurate progress dashboard

The original factory investigation (before any of this session's work) found the README's own dashboard
was stale and never actually updated by CI — `update_dashboard.py` existed but its output wasn't trusted.
Check whether that's still true now. With potentially 215 lessons moving through 6+ pipeline stages
simultaneously, "read the raw ledger/git log" doesn't scale as a way to answer "what needs my attention
right now." Build or fix a dashboard that answers, at a glance: how many cards are at each status
(pending_approval, concept_expanding, pending_concept_approval, evaluated, etc.), grouped by subject and
grade; which cards are stalled (failed/attempts near max_iterations) and need intervention; and how many
are sitting at a human-approval gate waiting on you specifically, since that's the actual bottleneck now
that content generation itself is proven. Doesn't need to be fancy — a regenerated README table or a
committed summary markdown file is fine, as long as it's actually current and actually queried by CI, not
aspirational.

## 3. Cost / rate-limit visibility

215 seed rows means potentially 215× (Level 0 theme calls + Level 1 Groq + Level 2 Jules session + Level
3.5 crosscheck Groq call) once the queue starts churning continuously at Level 0's 3-pending-per-subject
throttle. Determine: is there any existing spend or rate-limit visibility for the Groq/Jules API usage
this pipeline generates? If not, add basic tracking — even just logging each call's cost/token usage
somewhere queryable (the ledger, or a dedicated log) — so a misconfigured loop or an unexpectedly fast
churn rate is discoverable before it's a surprise bill or a rate-limit lockout mid-pipeline. Check whether
Groq/Jules have documented rate limits that 215 rows' worth of sustained throughput could actually hit,
and if so, whether Level 0's existing 3-pending-per-subject throttle is sufficient headroom or needs
tuning.

## What NOT to do

- Don't re-seed or expand the curriculum further — 215 rows is intentionally the current scope per the
  prior session's own reasoning (deep enough not to run dry, throttled enough not to flood approvals).
- Don't touch Level 6 (production) — still out of scope, still a separate future brief.
- Don't weaken the fail-closed guarantees on the crosscheck/human-gate work already verified — this brief
  is about operational visibility and robustness at scale, not changing what's already correctly gating
  content.

## Deliverable

Report back on all three: (1) the actual root cause of the Lesson 3 intermittent failures, with a real fix
or an explicit, evidenced conclusion that it's unfixable/acceptable and why; (2) a working, CI-verified
dashboard reflecting real pipeline state, with a screenshot/output sample as evidence; (3) whatever cost/
rate-limit tracking exists now, plus a clear answer on whether current throttling is safe at this scale.
Same evidence bar as the rest of this project — cite real data, don't just report "done."
