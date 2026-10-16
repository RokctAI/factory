# Ad JSON format

Machine-readable schema: [`schema/ad.schema.json`](schema/ad.schema.json)
(JSON Schema 2020-12). Check files with:

```bash
python make_ad.py --validate examples/*.json
```

The validator runs the JSON Schema first, then checks what a schema can't:
every speaker is in `cast`, the `format` matches the script, reference
audio / music / SFX files exist, SFX anchors point at real lines, and a
rough word-count estimate says whether the script will fit the spot.

Relative paths are looked up next to the ad JSON first, then in `radio_ads/`.

## Minimal ad

```json
{
  "id": "my_first_ad",
  "client": "Acme",
  "duration_s": 30,
  "format": "single-voice",
  "cast": {"host": {"voice": "tutor_008"}},
  "script": [
    {"speaker": "host", "text": "Hello Joburg! ..."}
  ]
}
```

Everything else has a default.

## Top level

| Field | Required | Meaning |
| --- | --- | --- |
| `id` | yes | Output folder name, `out/<id>/`. `a-z 0-9 - _`. |
| `client` | yes | Who the ad is for. Recorded in the report. |
| `title`, `notes` | | Free text. |
| `duration_s` | yes | `15`, `30`, `45` or `60`. The delivered file is exactly this long (unless the read cannot fit, see Timing). |
| `format` | yes | `single-voice`: one voice for the whole script (the tag may be a second voice). `dialogue`: two or more speakers talking to each other. `spot`: jingle-less announcer spot, any cast, each line rendered separately. |
| `cast` | yes | `role -> voice`. See Cast. |
| `script` | yes | Ordered list of lines. See Script. |
| `tag` | | End tag / legal read. See Tag. |
| `music` | | Music bed. Default: built-in `corporate` bed. |
| `sfx` | | Sound effects. |
| `timing` | | How to fit the read to `duration_s`. |
| `render` | | Speech engine settings. |
| `output` | | File formats and loudness. |

## Cast

```json
"cast": {
  "gogo":  {"voice": "tutor_006"},
  "sipho": {"voice": "tutor_004", "gain_db": -1},
  "host":  {"ref": "voices/my_recording.wav"}
}
```

* `voice`: a persona id from the tutor voice specs (`tutor_001`..`tutor_012`,
  `assistant_001`..`assistant_003`), resolved to `voices/<id>.wav`. See
  [`voices/README.md`](voices/README.md) for how to fill that folder.
* `ref`: any reference WAV to clone instead.
* `gain_db`: level trim for this voice (every line is first levelled to
  -20 LUFS, so this is only for taste).

## Script

```json
{"speaker": "gogo", "text": "Eish, Sipho! The whole street is out of bread again!",
 "pause_after_s": 0.25, "delivery": "exasperated, comic", "rate": 1.0}
```

| Field | Default | Meaning |
| --- | --- | --- |
| `speaker` | | A key of `cast`. |
| `text` | | What is said. Up to 600 characters. Punctuation is the main lever on the read: `!` and `?` lift it, full stops give the short beat between phrases. |
| `pause_after_s` | 0.25 | Silence after the line (0-5 s). |
| `delivery` | | Direction for the read. Recorded in the report. **The engine has no style control**, so this does not change the audio; it documents intent (and tells a human what to re-take). |
| `rate` | 1.0 | Tempo for this line after rendering, pitch preserved (0.8-1.3). |
| `gain_db` | 0 | Level trim for this line. |

## Tag (end tag / legal read)

```json
"tag": {"speaker": "announcer", "text": "Ts and Cs apply.", "fast": true, "gap_before_s": 0.35}
```

Rendered on its own after the script. `fast: true` sets `rate` to 1.2
unless you give one (max 1.4) and exempts the tag from any slow-down.
`gain_db` defaults to -1 so the tag sits slightly under the body copy.

## Music

```json
"music": {"bed": "builtin:upbeat", "seed": 1, "level_db": -6, "duck_db": -12,
          "intro_s": 1.2, "outro_min_s": 1.0, "fade_in_s": 0.3, "fade_out_s": 1.5}
```

| Field | Default | Meaning |
| --- | --- | --- |
| `bed` | `builtin:corporate` | `none`, `builtin:upbeat`, `builtin:calm`, `builtin:corporate`, or a path to an audio file (looped with a crossfade if too short). |
| `seed` | 1 | Variation of the built-in bed (arp direction, chord rotation). |
| `level_db` | -6 | Bed loudness relative to the voice when nobody speaks (intro, outro). |
| `duck_db` | -12 | Extra reduction while someone speaks, so the default bed sits 18 dB under the voice (sidechain ducking: fast attack, 0.35 s release, 0.12 s look-ahead so the bed dips before the first syllable). |
| `intro_s` | 1.2 | Music alone before the first word. |
| `outro_min_s` | 1.0 | Minimum music after the last word. Spare time goes here. |
| `fade_in_s`, `fade_out_s` | 0.3, 1.5 | Bed fades. The bed ends exactly at `duration_s`. |

Built-in beds are synthesised with numpy (additive pads and plucks, sine
bass, synthetic kick/hat/clap): no samples, no licences.

| Style | Feel |
| --- | --- |
| `upbeat` | 112 BPM, D major I-V-vi-IV, four-on-the-floor kick, off-beat hats, claps, 8th-note arp. |
| `calm` | 72 BPM, F major maj7 chords, soft pad and slow plucks, no drums. |
| `corporate` | 100 BPM, C major I-vi-IV-V, piano-ish plucks, light kick and shaker. |

With `"bed": "none"` there is no intro/outro music; the voice starts at 0.2 s.

## SFX

```json
"sfx": [
  {"file": "builtin:hooter", "at_s": 0.15, "gain_db": -4},
  {"file": "sfx/door.wav", "segment": 1, "anchor": "start", "offset_s": -0.35, "gain_db": -8}
]
```

Place each effect either at an absolute time (`at_s`) or relative to a line
(`segment`: 0-based script index, `-1` for the tag; `anchor`: `start` or
`end`; `offset_s`). Anchored effects follow their line when the read is
re-timed. `gain_db` is relative to the voice's loudness. Built-ins:
`builtin:ding` (shop bell), `builtin:hooter` (minibus-taxi hoot),
`builtin:whoosh`.

## Timing

```json
"timing": {"fit": "speed_up", "max_stretch": 0.08, "compress_pauses": true}
```

The voice window is `duration_s - intro_s - outro_min_s`. After rendering:

* `fit: "speed_up"` (default): if speech + pauses exceed the window, speed
  all speech up (pitch preserved, rubberband) by at most `max_stretch`
  (default 8 %). If still long and `compress_pauses`, shrink the pauses (to
  no less than half).
* `fit: "both"`: also slow a short read down by up to `max_stretch`.
* `fit: "none"`: never change the read; just report.

The report's `timing.status` is `fits`, `under by X s` (the music tail
fills it) or `over by X s`. An over-long ad is still delivered, just longer
than `duration_s`: cut words and re-run (only the edited lines re-render).

## Render

```json
"render": {"engine": "vibevoice", "model": "microsoft/VibeVoice-1.5B", "mode": "auto",
           "cfg_scale": 1.3, "ddpm_steps": 10, "seed": 7}
```

* `mode`: `joint` renders a whole dialogue in one VibeVoice pass (all
  speakers, natural turn-taking), then speech recognition finds the line
  boundaries so each line can still be paused, re-timed and reported.
  `per_line` renders each line alone. `auto` = joint for `dialogue`,
  per-line otherwise. If a joint render can't be split cleanly the
  pipeline falls back to per-line and says so in the report.
* `seed`: VibeVoice's diffusion head is random; a fixed seed makes renders
  repeatable. Change it to get a different take.
* `engine: "dummy"` replaces speech with tones of the estimated length, for
  testing mixes without the model.

## Output

```json
"output": {"formats": ["wav", "mp3"], "sample_rate": 44100, "channels": 2,
           "loudness_lufs": -23, "true_peak_dbtp": -1, "mp3_bitrate_kbps": 192}
```

Default is EBU R128 broadcast: **-23 LUFS integrated, -1 dBTP true peak**.
For streaming use `-16` (or `-14`). The master is gain-normalised with a
look-ahead limiter to hold the true-peak ceiling, and the MP3 gets a final
trim so it also measures on target. WAV is 16-bit PCM.
