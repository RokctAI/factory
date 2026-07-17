# Task Brief: Level 6 Production — Manim/VibeVoice via CI, No Persistent VPS

> Self-contained brief for a fresh session. Read in full; should not require the conversation that
> produced it. This is the long-deferred "Level 6" of the lesson pipeline — every prior brief
> (`lesson-pipeline-levels-0-4-brief.md` and follow-ons) explicitly stopped before this step because it
> was assumed to need dedicated VPS infrastructure. New direction: it likely doesn't. Manim/VibeVoice
> rendering is a batch, offline process, not real-time — a scheduled/triggered CI job can do it instead of
> an always-on server, which is both cheaper and simpler to operate.

## What Level 6 must actually produce (confirmed spec, don't re-derive)

Per `agent/replay/docs/supacharge-tech.md` §4:
1. **Manim → JSON, never video.** "VPS runs Manim — exports animation JSON... App renders JSON locally via
   ReplaySDK ManimPlayer." The `.py` Manim scene file each `evaluated` lesson card already has
   (`lessons/<subject>/grade*/term*/<id>/manim_scene.py`) is the *source*; what ships to the app is JSON
   primitives (shapes, equations via KaTeX, transforms, timestamps) — `ManimPlayer` renders it client-side.
   Confirm your Manim installation is the Community Edition (`github.com/ManimCommunity/manim`, PyPI
   package `manim` — verify via `pip show manim`, the `Author` field should read "The Manim Community
   Developers"), matching the doc's explicit choice, not the original 3Blue1Brown `manimlib`/`manimgl`.
2. **VibeVoice generates the tutor audio** from the lesson script (`script.md`) — "Microsoft open source
   frontier voice AI... runs locally, MIT licensed, zero ongoing voice API cost" per the same doc section.
3. **Timestamps aligned, manifest assembled** — the Manim JSON's timeline and VibeVoice's audio need to
   line up, producing the actual manifest file `ManifestParser`/`TrackEvent`
   (`agent/replay/dart/lib/src/controllers/manifest_parser.dart`) already knows how to consume. Read that
   parser's expected format directly — the manifest this step produces must match it exactly, not a
   guessed shape.

## The architecture question — CI-triggered batch job, not a persistent VPS

Design and build a GitHub Actions workflow (mirroring the existing `factory` workflow conventions — job
cards, the ledger, `Initiate Protocol`) that:
1. Triggers on a schedule (weekly, matching the user's suggestion) and/or on-demand when a lesson card
   reaches `status: evaluated` (check whether an event-driven trigger is feasible given how job-card status
   transitions currently work, vs. purely time-based — your call, justify it).
2. For each `evaluated` card not yet processed through Level 6 (needs a new status value, e.g.
   `produced`/`published` — extend the state machine per the existing convention in
   `lessons/scripts/lesson_pipeline.py`'s `ALLOWED_TRANSITIONS`), runs Manim on `manim_scene.py` to produce
   JSON, runs VibeVoice on `script.md` to produce audio, aligns timestamps, assembles the manifest.
3. Commits/uploads the output somewhere real apps can actually fetch it from (determine what that
   location should be — check how `replay_sdk`'s asset store currently expects to find manifests/audio,
   don't invent a new distribution mechanism if one's already assumed).
4. Runs in a GitHub Actions runner (ephemeral, pay-per-minute, no idle cost) rather than a dedicated VPS —
   confirm Manim/VibeVoice can actually run within a standard GitHub-hosted runner's resource limits
   (check both projects' documented minimum requirements, especially VibeVoice's — voice model inference
   may need more RAM/compute than a standard runner provides; if so, this needs a self-hosted runner or a
   different execution target, don't assume a standard runner works without checking).

## What to actually do first

1. Confirm the Manim install is Community Edition (done — verify again if starting fresh).
2. Research VibeVoice's actual runtime requirements (model size, RAM, whether GPU is required or CPU
   inference is viable at acceptable speed/quality) — this determines whether "just run it in a GitHub
   Actions runner" is realistic or whether some minimal always-on compute is still needed after all. Report
   this honestly even if it complicates the "no VPS" premise — don't force a conclusion the evidence
   doesn't support.
3. Build a minimal end-to-end proof: run Manim on one real `evaluated` lesson's `manim_scene.py`, produce
   real JSON, inspect it against what `ManifestParser` expects. Do the same for VibeVoice on one real
   `script.md`. Prove the two pieces can actually be combined into a valid manifest before building the
   full CI workflow around it.
4. Only then build the actual GitHub Actions workflow, following the established `factory` conventions.

## What NOT to do

- Don't build this for the full seed backlog (215 rows) — pick 1-2 real `evaluated` lessons (the two
  original Grade 11 maths lessons are the obvious, most-verified candidates) to prove the pipeline works
  end to end before running it at scale.
- Don't guess at VibeVoice's resource requirements — verify them against its actual documentation/repo,
  since this is the one part of the "no VPS needed" premise that could genuinely be wrong.
- Don't invent a different manifest format than what `ManifestParser` already expects — read the real
  Dart code, don't guess the JSON shape.

## Deliverable

A real, working proof: one lesson's Manim scene → real JSON, one lesson's script → real VibeVoice audio,
combined into a manifest matching `ManifestParser`'s actual expected format — plus an honest, evidenced
answer on whether GitHub Actions' standard runners are sufficient for VibeVoice or whether some minimal
persistent compute is still needed. If the CI-only approach holds up, build the actual scheduled workflow;
if it doesn't for VibeVoice specifically, say so clearly and scope what minimal infrastructure would
actually be needed instead of forcing the "no VPS" answer.
