# talking_head

Talking, blinking faces for team members, made on CPU from their one approved
portrait and their approved voice lines. The app gets **pictures and a timing
file, not video**: it plays the line's own audio and swaps mouth pictures on a
still base picture, with eye pictures for blinks.

## One line

`make_face_pack.sh <portrait> <voice> <text> <out dir> [normal|clear]`

1. `align.py`: lines the text up with the voice (torchaudio MMS_FA).
2. `still_head.py` + `lpcore.py`: LivePortrait draws the face with the head held
   still; only jaw and lips move (letters pick the shape, loudness sets how open).
   `clear` is the Grade R-3 mouth: wider, rounder, held longer.
3. MuseTalk v1.5 redraws the lips from the voice.
4. `sharpen.py`: GFPGAN v1.4 sharpens the lower face only, so the mouth is not
   blurry when shown large.
5. `face_pack.py`: keeps the distinct mouth pictures (cut below the nostrils),
   a median base picture, eye pictures (open, half, shut) and `timing.json`.

The voice file is only read, never changed.

## One member

`pack_persona.py <lines dir> <face dir>` merges every line into one shared set
of mouth pictures, so all greetings and sign-offs reuse the same pictures and
each line keeps only a small timing file:

```
face.json                 size, mouth_box, eyes_box, line list
base.webp, eyes_*.webp, m000.webp ...
<category>/<line>.json    fps, mouth (picture per frame), blinks
```

There is one pack per style (`normal` and `clear`).

`play_face.py <face dir> <category>/<line> <out frames> [--sway]` previews a
line the way the app plays it. Any head movement is applied to the whole
composed picture, so eyes and mouth always move with the head.

Members with no voice yet get pictures only (`--no-lines`): their portrait
speaks a few stand-in lines and no timing files are kept. Their real lines are
drawn once their voice exists. Timing real lines against stand-in pictures was
tried and dropped: the mouth drifted off the words.

## Running it

```
source <(bash talking_head/setup.sh ~/.talking_head | sed 's/^/export /')
```

`.github/workflows/face_pack.yml` (manual run: persona, style, lines) makes a
member's pack (from their own voice, or pictures only from the stand-in lines
when they have no voice yet) and opens a pull request in the private voice repo next to their
voices (`voices/team/<kind>/CAPS/<persona>/face/<style>/`). Nothing is
committed here. Logs carry names, counts and sizes only.

**Speed:** about 6 s of CPU per frame (LivePortrait ~3.5 s, GFPGAN ~2.8 s,
plus MuseTalk), so roughly 15-25 minutes per 6-second line.

**Engines** (pinned in `setup.sh`):
- LivePortrait (KwaiVGI); face detector InsightFace buffalo_l.
- MuseTalk v1.5 (TMElyralab); its mmpose face finder is replaced by
  `musetalk_preprocessing.py`, because mmpose does not build on current Python.
- GFPGAN v1.4 (Apache-2.0), installed without basicsr; `sharpen.py` loads its
  network files directly.
