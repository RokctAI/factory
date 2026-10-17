# voice_batch

Renders a tutor's standing lines (acknowledgements, greetings, sign-offs,
teaching snippets) in the tutor's consented cloned voice (kind `tutor`), or
the Grades R–3 activity-pack lines (kind `r3`), gates every line, and
commits the passing audio on a `rokct/` branch of the private voice repo
(`RokctAI/lessons`, under `voices/`), then opens (or notes the run on) a PR
from that branch into its `main` for the owner to listen and merge.
Workflow: [`.github/workflows/voice_batch.yml`](../.github/workflows/voice_batch.yml).

**Where things live (phase 2 of the repo split).** Voice audio, manifests,
QC logs and the reference WAVs moved from `RokctAI/agent` to
`RokctAI/lessons`. [`voice_paths.py`](voice_paths.py) is the one switch:
`VOICE_REPO` (default `RokctAI/lessons`) and `VOICE_ROOT` (default `voices`),
set by the workflows from the repository variables of the same names.

| agent (before)                                      | voice repo (now)                               |
|-----------------------------------------------------|------------------------------------------------|
| `lms/team/voice_refs/<x>.wav`                       | `voices/refs/<x>.wav`                          |
| `lms/dart/templates/assets/r3_packs/audio/<f>`      | `voices/r3/<f>`                                |
| `lms/team/{tutors,assistants}/CAPS/<id>/<audio>`    | `voices/team/{tutors,assistants}/CAPS/<id>/<audio>` |
| `lms/team/voices/samples/<f>`                       | `voices/samples/<f>`                           |

`<audio>` is the clips, `*.timings.json`, `<voice>_manifest*.json` and
`qc_failed.json`. Scripts, persona JSON, voice specs
(`lms/team/voices/*.voice.json`), `lms/team/scripts/` and the R-3 app
sources stay in agent and are read from an agent `main` checkout
(`--agent-root .agent`, read-only); the audio goes to the voice-repo
checkout (`--voice-root .voices`). Setting `VOICE_REPO=RokctAI/agent` and
`VOICE_ROOT=.` restores the old layout. The one-off
[`ci/migrate_voices_to_lessons.py`](ci/migrate_voices_to_lessons.py) copies
the existing files from an agent checkout into a lessons checkout (sha256
verified, paths inside manifests rewritten; `--check` only reports; it never
deletes anything from agent). Some names still say "agent" for history:
the batch field `agent_branch` (a branch of the voice repo),
`ci/push_agent.sh`, `ci/open_agent_pr.py`, `ci/resolve_agent_ref.sh`.

**Nothing identifying and no audio ever lands in this public repo.** The
reference clip, the line scripts and the rendered audio live only in the
private repos; this repo holds code plus a small batch JSON naming ids,
paths and a hash. The job has no artifact upload, caches only public model
weights, and logs/summaries show line ids and scores only.

## Trigger a batch

Commit one JSON to `voice_batches/inbox/` on `main` (one batch per push), or
run the workflow by hand ("Run workflow", `batch_path`):

```json
{
  "tutor": "tutor_001",
  "voice": "voice_a",
  "ref_path": "voices/refs/voice_a_ref.wav",
  "ref_sha256": "<sha256 of the reference in the voice repo>",
  "agent_branch": "rokct/<branch>",
  "categories": ["acknowledgements", "greetings", "signoffs", "teaching"],
  "lines": ["tutor_001/greetings/01", "tutor_001_sample_line"]
}
```

`lines` is optional: a subset of ids for a quick smoke batch. Only the
categories it touches get a job. `agent_branch` must start with `rokct/`
(CI-written branches only; never `main`).

Optional for both kinds: `f0_target_hz` and `f0_tolerance_hz`, the median-F0
gate (default 102 ± 8 Hz = 94–110 Hz, tuned to Voice A, so existing batches
behave exactly as before). Set them for any other voice.

### R–3 batches

```json
{
  "kind": "r3",
  "voice": "<voice>",
  "ref_path": "voices/refs/<voice>_ref.wav",
  "ref_sha256": "<sha256>",
  "agent_branch": "rokct/<branch>",
  "packs": "english_home_language.gradeR.term1.*",
  "lines": ["english_home_language.gradeR.term1.w01_sound_a.show"],
  "locale": "en",
  "f0_target_hz": 210,
  "f0_tolerance_hz": 25
}
```

`packs` (a pack-id glob or a list of globs), `lines` (app line keys) and
`locale` are optional. Without filters a batch renders every pack line of
every pack under `r3_packs/` (Grades R to 3, Terms 1-4, maths, English Home
Language and Life Skills, plus English First Additional Language Grades 1-3; more land on their own branches) plus the
4 default praise lines, split into 8 shard jobs (`R3_MAX_SHARDS`).
`tests/test_r3.py` derives the counts from the pack tree. A `packs` filter
leaves out the shared praise lines. `locale` only changes the praise lines (packs are English):
`af` renders the 4 Afrikaans praise lines as `<key>.af.mp3` with the
multilingual ASR model, which the app does not play yet.

Line keys match the app exactly (`r3_lines.py`, checked against
`r3_session_engine.dart` by `tests/test_r3.py` with `AGENT_ROOT`):
`<pack id>.show`, `.hints_0`/`.hints_1`, `.rounds_<i>_prompt|_praise|_story`,
`.beat_the_tutor_setup|_tutor_try|_win_line|_gentle_line`, and
`r3.r3_praise_{yes,great,clever,right}` (text read from the app's
translations, with a checked-in fallback).

**Phonics.** `r3_respellings.json` maps a line key (or an exact line text)
to a TTS-only text so the voice says the letter *sound*, not its name
("a as in ant" → "Ah, as in ant"). The pack text shown on screen never
changes. A respelled line is rendered from, and ASR-checked against, the
respelling, and is marked `needs_listen: true` in the manifest: a person
should listen before merging. `voice_batches/examples/r3_phonics_probe.json`
is a 6-line probe for this; it runs only if moved into `inbox/`.

Output: `voices/r3/<key>.mp3` in the voice repo (mono, 24 kHz,
64 kbps CBR, via lameenc or ffmpeg), which the app's `AssetTutorVoice` plays
as `assets/r3_packs/audio/<key>.mp3`, plus `r3_manifest.<voice>.json`
beside it (shards write `r3_manifest.<voice>.partNN.json`; the merge job
folds and removes them).
Re-running a batch is idempotent: lines whose text and reference are
unchanged are skipped; changed ones are re-rendered and overwrite the same
files.

## Pronunciations

`pronunciations.json` fixes how the voice says a word, for every batch kind
(tutor and r3). It ships empty; add entries as needed:

```json
{
  "words": {"Mahikeng": "mah-hee-KENG"},
  "ambiguous": {"<Name>": ["<variant 1>", "<variant 2>"]}
}
```

- `words`: every whole-word use of the word (any case) is spoken as the
  respelling.
- `ambiguous`: words, usually names, with more than one right pronunciation
  for the same spelling, with the known variants. The global list never
  touches them. A line that uses one must say which it means inline, or the
  batch fails with, e.g., `line tutor_009/greetings/01 uses '<Name>': write
  {{<Name>|<variant 1>}} or {{<Name>|<variant 2>}}`.
- Inline, in the line's script: `{{Thendo|TEN-doh}}`. The voice gets the
  part after the bar; the display text (manifest `text`) and the word check
  get the part before it. Inline always wins over the file, and any
  respelling is allowed, not only a listed variant.

Only the spoken text changes. The word check stays word-exact except for
the respelled words, which match 1 to N transcript words (N = the larger of
the word's and the respelling's word counts, plus one). A line with a
pronunciation records `tts_text` and `pronounced` in the manifest and is
marked `needs_listen`. Changing a pronunciation changes `render_sha256`, so
the next batch re-renders that line.

The r3 check runs in the plan job (the packs are here). Tutor scripts live
in the agent repo, so each render job checks them after checkout
(`batch.py --agent-root .agent`). The app shows the `samples.json` teaching
`script` on the tutor card, today through a hand-copied demo constant
(`kDemoTutorSnippets`); avoid inline markup in `samples.json`, or strip it
when that constant is re-copied. Greetings, acknowledgements and sign-offs
are never displayed.

R–3 phonics respellings stay in `r3_respellings.json` (whole-line); word
pronunciations apply after them.

**Audition.** A push to `main` that changes `pronunciations.json` (or a
manual run of `pronunciation_audition.yml` with a comma-separated `words`
list) renders one short clip per changed word and voice (every variant of
a changed ambiguous entry), so someone can listen and adjust. The clips go
to the voice repo's `rokct/pronunciation-audition` branch, never to this
repo: `voices/samples/pronunciation/<voice>/<word>--<respelling>.mp3`,
with `audition.json` beside them. Samples never ship in the app bundle.
No PR is opened. The carrier is
`<respelling>. <respelling>.`, one take, seeds 11/22/33 until a light QC
passes (0.4–8 s, not silent, similarity ≥ 0.75, and `qc.py`'s tail check:
last 50 ms ≤ -34 dB); no ASR check, since these are unusual words. Otherwise the
best take is kept and marked `passed: false`.

## What a run does

1. **plan** lists the changed batch, validates it (`batch.py`) and emits one
   matrix entry per category (tutor) or per shard (r3, at most 8).
2. **render** (one runner per category, in parallel): checks out agent main
   (scripts, read-only) and the voice repo's `rokct/` branch (references and
   this batch's audio folder), verifies the reference sha256 (fails on mismatch), installs CPU
   torch + the pinned VibeVoice fork, restores the model weights, then
   `run.py`:
   - splits each line into sentences (`textnorm.py`, `lines.py`: spoken
     text only, never markdown or metadata);
   - renders every sentence with seeds 11/22/33, one take at a time
     (`render_takes.py`, reusing the agent repo's `render_voices.py`); the
     prompt is the sentence plus a trailing ` ...` (`textnorm.tts_prompt`),
     because without it the model often stops on the last phoneme and the
     last word is clipped;
   - measures each take (`qc.py`): word-exact ASR, median F0, upward
     swings, speaker similarity to the reference, and the tail level (the
     last 50 ms relative to the loudest 10 ms frame); a take whose tail is
     above -34 dB ended mid-word and is never picked;
   - picks per sentence: median F0 closest to the target (default 102 Hz), then fewest swings,
     then higher similarity; stitches with 280–320 ms pauses and 12 ms
     fades; normalises to -20 dBFS, 24 kHz mono PCM_16;
   - gates the final file: median F0 in the batch's gate (default 94–110 Hz), similarity ≥ 0.88
     (≥ 5 s) or ≥ 0.83 (< 5 s), word-exact ASR, tail ≤ -34 dB;
   - lines not yet passing get seed 44, then 55; still failing = recorded
     as failed, audio not committed. A line rendered before the tail pad
     existed (no `tail_pad` in its manifest entry) is re-rendered;
   - writes `<voice>_manifest.<category>.json` and commits the passing
     clips + that manifest to the voice branch (`ci/push_agent.sh`, with
     rebase-and-retry because category jobs push concurrently).
3. **merge** folds the category manifests into `<voice>_manifest.json`
   (r3: the shard parts into `r3_manifest.<voice>.json`), then
   `ci/open_agent_pr.py` opens a ready-for-review PR from the voice branch
   into the voice repo's `main` if none is open, or leaves one comment on the open one with
   this run's pass/fail counts (counts and run URL only). Merging that PR
   publishes the audio on `main`.

## Long batches: time budget, checkpoints, continuations

A render job can run for hours (QC retry rounds). GitHub kills a job at 6 h, so
renders are resumable (`resume.py`):

- **Checkpoints.** `run.py` renders lines in chunks of `RENDER_CHUNK_LINES`
  (4). After each chunk it installs what passed, records lines that failed
  every seed round, writes the manifest and runs `push_agent.sh` (at most
  every `RENDER_PUSH_MINUTES`, 15). Before the first chunk it pushes the
  manifest with the job's lines listed as `remaining`.
- **Time budget.** Before each chunk and each seed round, `run.py` checks
  `RENDER_BUDGET_MINUTES` (300, or `vars.RENDER_BUDGET_MINUTES`), counted from
  the job's first step. A round that would end past it, estimated from the
  largest round so far, is not started. The job then stops cleanly, pushes
  what it has, and keeps the unfinished ids under `remaining` in its
  manifest. The step outputs are `incomplete=true` and `remaining=N`. The
  render job's `timeout-minutes` is 330, which leaves 30 min of margin and
  stays under 360.
- **Continuations.** The merge job counts `remaining` across the batch's
  manifests. If any line is left, it dispatches this workflow again with the
  same `batch_path`, `continuation` + 1 and the same `series`, at most 5
  times, using `GITHUB_TOKEN` with `actions: write`. The voice PR opens only
  when nothing is left, or when the cap is reached. Already-pushed lines are
  skipped. A line that failed every seed round is **final-failed**, never
  remaining: within one series it is not retried.
- **Concurrency.** A continuation queues behind the running run in the
  `voice-batch` group. GitHub keeps only one pending run per group, so a run
  queued after it, such as a push, a dispatch or the schedule, replaces it.
  The next scheduled run then picks the batch up again.

## Daily schedule

The workflow also runs every day at 01:23 UTC. The plan job checks out agent
main without audio (to build the lines) and the voice repo's main with only
its manifests, and runs `ci/scan_pending.sh`. For each batch in
`voice_batches/inbox/` (sorted), the scan fetches only the manifests of the
batch's voice branch, and `pending.py` counts the lines that are not done. A
line is done when it has a passed entry for the same text and reference, or
when it is final-failed. The first batch with lines left is rendered; the
next day's run picks the next one. If nothing is pending, the plan job ends
in about a minute, with no render jobs, no model download and no PR.

## Failed QC log

Every final-failed line is listed in a `qc_failed.json` beside its clips on
the voice branch (the private voice repo only). For a tutor or assistant
that is `voices/team/.../<id>/<clip dir>/qc_failed.json`. For r3 it is
`voices/r3/qc_failed.<voice>.json`, written by the merge job.
An entry holds:

- the line id and text;
- the failing gates and their values for every round (ASR word errors,
  loudness dB, lead-in ms, onset, clipping, F0, similarity, tail);
- the attempt count, the batch file, the run id and a UTC date.

When the line later passes, its entry is removed, and an empty file is
deleted. The voice PR has a short "Failed QC" table: ids, attempts and the
last round's failing gates. The public job summary gives only a one-line
count and the ids.

Output layout in the voice repo (each clip at its script's path relative to
the team folder in agent):
`voices/team/tutors/CAPS/<tutor>/<category>/NN.m4a`,
`.../samples/<sample id>.m4a`, `.../samples/sample_line.m4a`. Clips are AAC
48 kbps mono in an `.m4a` file (`aac.py`); the stitched WAV stays in the work
dir and its hash is kept as `wav_sha256`.

## Caches

The model weights entry is shared with `radio_ads.yml` (same path and key
format), so the two workflows reuse one ~5.6 GB entry instead of evicting
each other under the 10 GB repository limit. The word-check ASR model has its
own small cache. Takes, references and audio are never cached.

## Expected wall time (first run, per category job)

Setup ~8–12 min (install, cache restore or first download), then roughly
acknowledgements ~10 min, sign-offs ~20 min, teaching ~35 min, greetings
~45 min of rendering and QC for seeds 11/22/33; each extra seed round for
failing lines adds ~30%. Categories run in parallel, so a full tutor batch
takes about as long as the greetings job (~1 h). A 3-line smoke batch takes
~20 min.

## Lesson audio

[`.github/workflows/lesson_audio.yml`](../.github/workflows/lesson_audio.yml)
renders the session packages in `RokctAI/lessons` part by part. A lesson has
up to three speakers ([`lesson_lines.py`](lesson_lines.py)):

| Speaker | Lines (keys) |
|---|---|
| first tutor (expert) | `intro.md` (`intro`), `script.md` up to `# Part 2` (`segNN`, one per subtopic), the Tutor turns of the Q&A (`qaNN_answer`) |
| second tutor | `script.md` from `# Part 2` (`segNN`) |
| grade host | the asking turns of the Q&A (`qaNN_ask`), `assistant_nervous_script.md` (`nervous`) |

Each speaker renders as soon as THEIR voice is approved in
[`lesson_voices.json`](lesson_voices.json), whatever the others have
(owner, 2026-10-16), so CI keeps working and a lesson is done by the time
its last voice arrives. Voice A never renders Grade R–3, and two personas
of one `voice_family` never share a lesson (that part is skipped).
`lessons_enabled: false` in the syllabus switches a grade or topic off.

Every three hours the plan job packs pending parts into up to
`LESSON_AUDIO_JOBS` (6) jobs of one persona, about `LESSON_AUDIO_JOB_WORDS`
(4000) words each. A job renders with the batch render and QC above, but
one seed per round (11, 22, 33, 44, 55), and stops cleanly at the time
budget; the next run carries on.

Where things go:

- **MP3 stems** (mono 24 kHz 64 kbps): assets on a lessons pre-release per
  subject, grade and term, `stems-<subject>-<grade>-<term>`. Never in git,
  so the repo stays small. Each asset is
  `<topic>--<lesson>--<persona>--<key>.mp3`.
- **Records**, committed to lessons `main` with `[skip ci]` in the lesson
  folder, `voice/<persona>/`: `manifest.json` (passed lines with scores and
  their asset, failed lines, what is left, `complete`) and `qc_failed.json`.
- **`voice/<persona>/redo.json`**, written by hand: passed lines that sound
  wrong on listening, `{"redo": [{"key": "seg03", "sha256": "<the MP3's
  sha256 from manifest.json>", "note": "..."}]}`. The next run re-renders
  that key on seeds it has not had (+100 per rejection).
- **`animations.export.json`**: the lesson's Manim export (the `animations`
  job, once per scene change, [`lesson_animations.py`](lesson_animations.py)).

Release: `lesson_release_on_complete.yml` runs
[`lesson_release_prep.py`](lesson_release_prep.py) first. Once every
speaker's manifest is complete, it joins the tutors' segments into
`audio.mp3` + `timings.json` (exact subtopic bounds) and aligns the Manim
export into `animations.json`; the release then publishes them as usual.

## Local tests

```bash
python -m pytest voice_batch/tests                         # model-free
AGENT_ROOT=/path/to/agent python -m pytest voice_batch/tests   # + real line scripts and the app's Dart
```
