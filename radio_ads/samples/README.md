# Sample ads

Rendered from [`../examples/`](../examples/) on a 4-core CPU with no GPU.
Both businesses are made up for the demo.

| File | Format | Voices | Duration | Integrated | True peak | Cold render |
| --- | --- | --- | --- | --- | --- | --- |
| `vuka_rides_30.mp3` | single-voice, per-line | tutor_008 | 30.00 s | -23.0 LUFS | -4.8 dBTP | 227 s (model load 19 s + 5 lines 208 s) |
| `kasi_corner_30.mp3` | dialogue, joint 2-speaker + announcer tag | tutor_006, tutor_004, assistant_002 | 30.00 s | -23.0 LUFS | -5.2 dBTP | about 255 s (dialogue 194 s + tag 38 s + mix and ASR) |

Loudness and peak were measured on the MP3s with ffmpeg's `ebur128` filter
(true peak 4x oversampled). The `*.report.json` files are the pipeline
reports from the final remix. Every line came from the cache for that run,
so their `wall_time_s` (about 20 s) shows how long a remix takes, not a cold render.

## Word check (faster-whisper `small.en` on the MP3s)

* **vuka_rides_30** (WER 9 %): "Suboogonajoba still standing at the rank waiting for the taxi to fill up. With VUCA rides you book your seat on your phone and the taxi leaves on time. No more waiting. No more guessing. Just your seat, a fair fair, and a driver who knows the way. VUCA rides. Wake up, book up, get going. VUCA rides is a fictional service. Data costs apply."
* **kasi_corner_30** (WER 14 %): "Aishseephole, the whole street is out of bread again. Not at Kussy Corner, Gogo. Fresh loaves every morning at 6, still warm. And my airtime. My electricity. Airtime, electricity, even school stationery. All under one roof. How? Then why am I walking to town? Exactly, Gogo. Kussy Corner. Your shop around a corner. Casicornispasa is a fictional shop, made up for this demo."

All common English words come through. The remaining "errors" are SA
names and words an English recogniser does not know (Sawubona, Eish,
Sipho, Kasi, Hau, spaza) plus the homophone "fair fare". Listen to those
words yourself; the ASR score can't tell you if they are pronounced right.

## Speaker check (Resemblyzer, each line cut from the final mix vs each cast reference)

In the joint dialogue every line's closest reference was the right cast member
(gogo 0.69-0.73 to tutor_006, sipho 0.80-0.89 to tutor_004, announcer 0.78
to assistant_002). The joint pass did not swap or blend voices.
