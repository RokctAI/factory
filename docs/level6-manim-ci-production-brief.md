# Task Brief: Level 6 Production — Manim/VibeVoice via Scheduled CI, Not a Persistent VPS

> Self-contained brief for a fresh session. Read in full; should not require the conversation that
> produced it. Levels 0-4 (content generation + human approval) are done and verified across all six
> subjects. Level 6 (turning approved content into the actual JSON manifest + audio the app consumes) was
> previously deferred as needing "real new VPS infrastructure." This brief proposes and scopes a cheaper,
> architecturally-consistent alternative: run Manim/VibeVoice as a **scheduled CI job**, not an always-on
> render server, since the actual per-lesson compute is periodic and bounded, not real-time.

## Ground truth — confirm before building

Per `agent/replay/docs/supacharge-tech.md` §4: Manim **outputs JSON primitives, not video** — the app
renders animation primitives locally via `ReplaySDK`'s `ManimPlayer` (Canvas/WebGL), synced to audio
timestamps. This was always the design; nothing here contradicts it. The only open question was *where*
Manim/VibeVoice actually run to produce that JSON+audio. Confirm this understanding against the doc
directly before building anything — don't take this brief's paraphrase as the final word.

## The proposed approach

Instead of a persistent VPS running Manim/VibeVoice as a service, run them as a **scheduled GitHub Actions
job** (same mechanism as every other level in this pipeline — `level0_theme_generation.yml`,
`lesson0_topic_selection.yml`, etc.) that:

1. Scans for lesson job cards at `status: evaluated` (Level 4 approved, not yet produced) — or however
   many exist since the lesson pipeline is already live.
2. For each: runs Manim against the card's `manim_scene.py` to produce the JSON primitive export, and
   runs VibeVoice against `script.md` (using the tutor persona card's voice characteristics, per
   `tutor-persona-cards-brief.md`'s work) to produce the tutor audio.
3. Aligns timestamps between the audio and the JSON primitives (per the manifest-assembly step already
   described in the doc) into the final manifest the app actually consumes.
4. Uploads the finished manifest + audio to wherever the app fetches lesson content from (check what
   storage/CDN mechanism `replay_sdk`'s `AssetStore` already expects — don't invent a new one).
5. Advances the job card's status past `evaluated` to a real "produced"/"published" state, and moves it
   to wherever produced content should live (mirroring the `pending/`→`done/` archiving pattern already
   established).

Run this weekly (or on-demand via `workflow_dispatch`, or triggered by a card reaching `evaluated` —
decide which cadence fits, but weekly batch is the concrete starting point proposed) rather than
continuously, since content approval is human-gated and won't produce a constant stream needing real-time
processing.

## What to actually determine and build

1. **Feasibility check first**: does GitHub Actions' standard runner have enough compute/time budget to
   run Manim rendering (even JSON-only export, not video encoding) and VibeVoice TTS within a job's time
   limits? Manim's JSON-export mode is lighter than full video rendering, but VibeVoice (per the doc, a
   real neural TTS model) may have real GPU/memory requirements standard runners don't have. Determine
   this concretely — check VibeVoice's actual resource requirements (`github.com/microsoft/VibeVoice`) —
   before assuming a standard runner works. If it doesn't, a small on-demand cloud instance spun up only
   for the CI job's duration (still cheaper than a persistent VPS) is the fallback, not defeat of the
   whole approach.
2. **Build the CI workflow** implementing the pipeline above, following the established conventions
   (Initiate Protocol step, job-card status transitions via `update_status.py`, ledger updates).
3. **Manifest assembly**: build the actual script/tooling that aligns Manim's JSON output with VibeVoice's
   audio timestamps into the manifest format `replay_sdk`'s `ManifestParser`/`AudioSync` already expect —
   read those Dart files for the exact expected shape, don't guess at the format.
4. **Storage/delivery**: determine and wire up where the finished manifest+audio actually needs to land
   for the app to fetch it — this is a real infrastructure decision (S3/CDN/GitHub Releases/something
   else) that should be made with real cost/reliability tradeoffs stated, not defaulted silently.

## What NOT to do

- Don't build a persistent VPS render service — that's the expensive alternative this brief exists to
  avoid, unless the feasibility check concretely proves CI-based batch rendering can't work.
- Don't re-litigate whether Manim outputs video or JSON — settled, JSON only, per the doc.
- Don't touch Levels 0-4 or the past-papers linking work (separate brief) — this is production
  infrastructure only.

## Deliverable

A working scheduled CI job that takes at least one real `evaluated` lesson card through to a finished,
correctly-formatted manifest + audio, with an honest, evidenced answer on whether standard GitHub Actions
runners are sufficient or a fallback (small on-demand instance) is needed — and real cost comparison
against a persistent VPS if that fallback is required. Report back with evidence: the actual generated
manifest, confirmation it matches what `ManifestParser` expects, and real compute-time/cost figures from
the CI run.
