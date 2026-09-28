# Radio ads factory

Put a JSON file in a folder, get a finished radio advert out: voiced with
the tutor persona voices (VibeVoice-1.5B, zero-shot cloning from a short
reference WAV), laid over a music bed with ducking, SFX placed, timed to
15/30/45/60 s and mastered to broadcast loudness (EBU R128: -23 LUFS,
-1 dBTP), delivered as WAV + MP3 with a JSON report.

```
inbox/kasi_corner_30.json  ->  out/kasi_corner_30/kasi_corner_30.mp3
                                                   kasi_corner_30.wav
                                                   report.json
                                                   ad.json   (copy of the input)
```

Listen first: [`samples/`](samples/) has two finished 30 s ads made from
[`examples/`](examples/).

## Setup (CPU is fine)

```bash
cd radio_ads
python3.11 -m venv venv && . venv/bin/activate
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
git clone https://github.com/vibevoice-community/VibeVoice.git vendor/VibeVoice
pip install -e vendor/VibeVoice
pip install -r requirements.txt           # pins transformers==4.51.3 (the pin matters)
huggingface-cli download microsoft/VibeVoice-1.5B    # 5.1 GB, MIT licence
```

Then fill `voices/` with the persona references, see
[`voices/README.md`](voices/README.md) (they are not in this repo).

`ffmpeg` is used for MP3, time-stretching (rubberband) and loudness
measurement; if there is no system ffmpeg the `imageio-ffmpeg` wheel in
`requirements.txt` provides a static one.

Microsoft removed VibeVoice's TTS code from its own repo; the community fork
above carries it, and the weights on Hugging Face are Microsoft's originals.

## Use

```bash
python make_ad.py examples/vuka_rides_30.json      # one ad -> out/vuka_rides_30/
python make_ad.py --validate my_ad.json             # check a file, no rendering
python make_ad.py --watch inbox/                    # the factory
```

**Watch mode** polls `inbox/` every 3 s. Every new or changed `*.json`
is rendered into `out/<id>/`, one at a time. A file that fails validation or
rendering is moved to `failed/` next to a `<name>.error.txt` saying why; fix
it and drop it back in. Editing a JSON already in the inbox re-renders it.
The model stays loaded between ads.

**Line cache.** Every rendered line is cached under `cache/tts/` by a hash
of (reference audio, text, engine settings, seed). Edit one line and re-run:
only that line is re-rendered; the mix, timing and mastering are redone in
seconds. In joint dialogue mode the whole conversation is one cache entry,
so any line change re-renders the dialogue.

Writing an ad: copy an example and read [`SCHEMA.md`](SCHEMA.md). The short
version:

```json
{
  "id": "vuka_rides_30", "client": "Vuka Rides", "duration_s": 30, "format": "single-voice",
  "cast": {"driver": {"voice": "tutor_008"}},
  "script": [
    {"speaker": "driver", "text": "Sawubona, Joburg! ...", "pause_after_s": 0.4},
    {"speaker": "driver", "text": "Vuka Rides. Wake up, book up, get going!"}
  ],
  "tag": {"speaker": "driver", "text": "Data costs apply.", "fast": true},
  "music": {"bed": "builtin:upbeat"},
  "sfx": [{"file": "builtin:hooter", "at_s": 0.15}],
  "output": {"loudness_lufs": -23, "true_peak_dbtp": -1}
}
```

## What happens to an ad

1. **Validate** (JSON Schema + semantic checks, a word-count estimate of
   whether it fits).
2. **Render** each line with VibeVoice-1.5B cloning the cast member's
   reference. Dialogue ads render the whole conversation in one multi-speaker
   pass, then faster-whisper word timestamps find where each line starts so
   it can be cut, paused and timed per line (falls back to per-line
   rendering if that fails).
3. **Clean** each line: trim silence, level to -20 LUFS.
4. **Fit** to `duration_s`: speed speech up by up to 8 % (pitch and
   formants preserved), then shrink pauses; report over/under.
5. **Mix**: music bed (file or built-in generated), sidechain-ducked under
   the voice, intro and fade-out; SFX at absolute times or anchored to lines.
6. **Master** to the loudness target with a look-ahead limiter holding the
   true-peak ceiling; write WAV (16-bit) and MP3 (192 kbps).
7. **Measure and check**: ffmpeg EBU R128 scan of the delivered files;
   faster-whisper transcribes the finished ad and each line, and the report
   gives word error rates so a garbled line is caught before it goes out.

## Report (`out/<id>/report.json`)

* `timing`: status (`fits` / `under by` / `over by`), actual duration,
  voice window, tempo applied, words per minute.
* `loudness.measured`: integrated LUFS, LRA and true peak of the WAV and the
  MP3 as measured by ffmpeg's `ebur128` filter.
* `lines[]`: speaker, voice, text, start/end, tempo, pause, cached or
  rendered (and how long it took), ASR transcript and WER.
* `render`: engine, mode actually used, joint-split details.
* `warnings`.

## Speed and limits (4-core CPU, no GPU)

* VibeVoice-1.5B on CPU renders at roughly 6-8x slower than real time and
  peaks at about 12.5 GB RAM: run one render at a time (watch mode does). The
  first model load on a fresh machine reads 5 GB from disk (took 8 min here);
  after that it loads in about 20 s. A 30 s ad takes about 4 minutes from
  cold, and about 20 s when every line is cached (remix, master, ASR check).
* **Delivery hints do not steer the voice.** VibeVoice has no style or
  emotion control; `delivery` is recorded for the humans. Punctuation and
  word choice are the real levers, plus `rate` per line and `seed` for a
  different take.
* **Pace comes from the reference.** The tutor references read at 120-190
  wpm; ads usually want brisker. Speeding up by more than ~8 % starts to
  sound processed; cut words instead.
* The persona voices are synthetic placeholders built for the tutor
  product; recast with consenting talent for real clients.
* Built-in music beds are simple procedural loops; use a licensed bed file
  for anything premium.

## Layout

```
make_ad.py              CLI (render / --validate / --watch)
adfactory/schema.py     loading, defaults, validation
adfactory/tts.py        VibeVoice engine + line cache
adfactory/align.py      faster-whisper: joint-dialogue split, word check
adfactory/bed.py        procedural music beds and SFX
adfactory/dsp.py        ffmpeg, stretch, ducking, limiter, loudness
adfactory/pipeline.py   the ad pipeline
adfactory/watch.py      inbox watcher
schema/ad.schema.json   JSON Schema
examples/               example ads
samples/                rendered example ads (mp3 + report)
voices/                 git-ignored reference voices (README explains)
tests/                  quick tests (no model needed)
```
