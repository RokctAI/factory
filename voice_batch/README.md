# voice_batch

Renders a tutor's standing lines (acknowledgements, greetings, sign-offs,
teaching snippets) in the tutor's consented cloned voice, gates every line,
and commits the passing audio beside its script on a `claude/` branch of the
private `RokctAI/agent` repo. Workflow: [`.github/workflows/voice_batch.yml`](../.github/workflows/voice_batch.yml).

**Nothing identifying and no audio ever lands in this public repo.** The
reference clip, the line scripts and the rendered audio live only in the
private agent repo; this repo holds code plus a small batch JSON naming ids,
paths and a hash. The job has no artifact upload, caches only public model
weights, and logs/summaries show line ids and scores only.

## Trigger a batch

Commit one JSON to `voice_batches/inbox/` on `main` (one batch per push), or
run the workflow by hand ("Run workflow", `batch_path`):

```json
{
  "tutor": "tutor_001",
  "voice": "voice_a",
  "ref_path": "lms/team/voice_refs/voice_a_ref.wav",
  "ref_sha256": "<sha256 of the reference in the agent branch>",
  "agent_branch": "claude/<branch>",
  "categories": ["acknowledgements", "greetings", "signoffs", "teaching"],
  "lines": ["tutor_001/greetings/01", "tutor_001_sample_line"]
}
```

`lines` is optional: a subset of ids for a quick smoke batch. Only the
categories it touches get a job. `agent_branch` must start with `claude/`.
Re-running a batch is idempotent: lines whose text and reference are
unchanged are skipped; changed ones are re-rendered and overwrite the same
files.

## What a run does

1. **plan** lists the changed batch, validates it (`batch.py`) and emits one
   matrix entry per category.
2. **render** (one runner per category, in parallel): checks out the agent
   branch, verifies the reference sha256 (fails on mismatch), installs CPU
   torch + the pinned VibeVoice fork, restores the model weights, then
   `run.py`:
   - splits each line into sentences (`textnorm.py`, `lines.py`: spoken
     text only, never markdown or metadata);
   - renders every sentence with seeds 11/22/33, one take at a time
     (`render_takes.py`, reusing the agent repo's `render_voices.py`);
   - measures each take (`qc.py`): word-exact ASR, median F0, upward
     swings, speaker similarity to the reference;
   - picks per sentence: median F0 closest to 102 Hz, then fewest swings,
     then higher similarity; stitches with 280–320 ms pauses and 12 ms
     fades; normalises to -20 dBFS, 24 kHz mono PCM_16;
   - gates the final file: median F0 94–110 Hz, similarity ≥ 0.88
     (≥ 5 s) or ≥ 0.83 (< 5 s), word-exact ASR;
   - lines not yet passing get seed 44, then 55; still failing = recorded
     as failed, audio not committed;
   - writes `<voice>_manifest.<category>.json` and commits the passing
     WAVs + that manifest to the agent branch (`ci/push_agent.sh`, with
     rebase-and-retry because category jobs push concurrently).
3. **merge** folds the category manifests into `<voice>_manifest.json`.

Output layout in the agent repo (audio beside its script):
`lms/team/tutors/CAPS/<tutor>/<category>/NN.wav`,
`.../samples/<sample id>.wav`, `.../samples/sample_line.wav`.

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

## Local tests

```bash
python -m unittest voice_batch/tests/test_voice_batch.py        # model-free
AGENT_ROOT=/path/to/agent python -m unittest voice_batch/tests/test_voice_batch.py   # + real line scripts
```
