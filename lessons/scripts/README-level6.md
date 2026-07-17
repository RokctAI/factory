# Level 6 Production — Feasibility & Cost

How Level-4-approved (`status: evaluated`) lesson cards become the ReplaySDK
asset triple the app downloads (`manifest.json`, `audio.mp3`,
`animations.json`), run as a **scheduled CI batch** rather than a persistent
VPS. Workflow: [`.github/workflows/lesson6_production.yml`](../../.github/workflows/lesson6_production.yml).

## Pipeline (supacharge-tech.md §4, steps 4–8)

1. **Manim → JSON primitives** — [`manim_exporter.py`](manim_exporter.py) runs
   the card's `manim_scene.py` through Manim's real update loop in `dry_run`
   mode (no ffmpeg, no frames) and serializes each on-screen mobject to a
   `ManimPrimitive.fromJson`-compatible dict (`primitive` type + normalized
   `position`/`from`/`to`). Manim outputs **JSON, never video** — the app's
   `ManimPlayer` renders these on-device (confirmed against the doc and
   `agent/lms/dart/.../manim_player.dart`).
2. **Audio** — [`lesson_manifest.py`](lesson_manifest.py) synthesizes the
   tutor narration from `script.md`. Backend is pluggable (`vibevoice` | `sapi`).
3. **Timestamp alignment + manifest** — subtopic boundaries (from
   `subtopics.json`) and animation-primitive times are scaled to the **real
   measured audio duration**, then assembled into the exact `ReplayManifest`
   shape `agent/replay/dart/.../manifest.dart` parses.
4. **Publish** — assets uploaded as a per-lesson **GitHub Release**; the URLs +
   sha256 + sizes are recorded on the card (matching `UpcomingSession.fromJson`).
5. **Status** — `evaluated → producing → produced` (added to the protocol's
   `ALLOWED_TRANSITIONS`; `produced` is terminal).

## Feasibility: are standard GitHub runners enough?

**Split answer, measured — not assumed.**

| Step | Standard `ubuntu-latest`? | Evidence |
|---|---|---|
| Manim JSON export | **Yes, trivially** | CPU-only; the exporter shims `Tex`/`MathTex` to Pango text, so **no TeX distribution** (Manim's heaviest dep) is needed. Local run: real 4-subtopic scene → 29 primitives in seconds. |
| Audio — `sapi` (espeak) | **Yes** | CPU-only OS TTS. Used to prove the whole loop with no GPU. Local run: 724 s of real MP3 from the actual script. |
| Audio — `vibevoice` | **No** | VibeVoice-1.5B is a ~3B-param BF16 model (~6 GB) and **requires a CUDA GPU** — the community fork notes Colab supports only the 1.5B model due to GPU memory, and there is no practical CPU inference path. Standard runners have **no GPU**. |

Standard `ubuntu-latest` = 4 vCPU / 16 GB (public repo), no GPU, 6 h job limit.
So everything **except the neural voice** runs on a standard runner today; the
CI workflow ships with `audio_backend=sapi` as the default so it is green on the
free tier, and swaps to `vibevoice` on a GPU runner for production audio.

## Fallback for production audio + cost vs a persistent VPS

Real per-minute / per-hour figures (Jan 2026):

| Option | Rate | Billing model |
|---|---|---|
| Standard Linux runner (`actions_linux`) | **$0.006/min** | per-job; free minutes on public repos |
| GitHub GPU runner (`linux_4_core_gpu`, NVIDIA T4 16 GB) | **$0.052/min** (~$3.12/hr) | per-job; Team/Enterprise plan required |
| On-demand cloud T4 (spot → on-demand) | **~$0.06–1.14/hr** | per-hour, spin up per batch |
| On-demand cloud A10 (spot → on-demand) | **~$0.09–1.77/hr** | per-hour, spin up per batch |
| Persistent GPU VPS (T4-class) | **~$200–720/mo** | 24/7 whether used or not |

VibeVoice-1.5B fits a single T4's 16 GB comfortably, so the natural fallback is
either GitHub's own `linux_4_core_gpu` runner (no separate infra — same Actions
mechanism, billed only while the batch runs) or a per-batch on-demand/spot GPU.

**Why batch wins:** production is human-gated and periodic. A weekly batch holds
the GPU for minutes-to-an-hour; a persistent VPS bills 24/7 while sitting idle
almost the entire week. Even at the GPU runner's $0.052/min, an hour-long weekly
batch is ~$3/week ≈ **~$13/month** vs **$200–720/month** for an always-on GPU
VPS — a 15–50× saving, before counting that the batch scales to zero between runs.

**Honest unknown:** VibeVoice's real-time factor on a T4 (how many GPU-minutes to
synthesize a 15-min lesson) has **not** been measured here — no GPU was available
in this environment. The first production run on a GPU runner should record it;
the per-lesson cost scales linearly with it, and even a pessimistic 2× RTF keeps
a lesson under ~$1.60 of GPU time.

## Proof produced in this environment

One real `evaluated` card —
`maths_g11_quadratic_equations_factoring_method_31d165` — taken end to end
with `--audio-backend sapi`:

- `audio.mp3` — **724 s**, valid MP3, synthesized from the real `script.md`.
- `animations.json` — **29 primitives** (27 text + 2 rect), exported from the
  real `manim_scene.py`, times scaled to the audio.
- `manifest.json` — **10 track events**, **validated by the real ReplaySDK
  `ManifestParser`** via [`agent/replay/dart/tool/validate_manifest.dart`](../../../agent/replay/dart/tool/validate_manifest.dart)
  (`dart run` — parse + every runtime accessor + contract checks pass).
