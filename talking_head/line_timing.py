"""Time a new line against a member's existing face pack, with no new drawing:
the voice picks, frame by frame, the shared mouth picture whose shape numbers
are closest. Takes seconds, so a member's pictures can be drawn once (even from
stand-in speech, before they have a voice) and every real line added later.

  python line_timing.py <face_dir> <voice audio> <text file> <category>/<line> [--style normal|clear]
Writes <face_dir>/<category>/<line>.json and adds the line to face.json.
The pack must have shape numbers (face.json 'mouth_shapes'). The voice file is
only read."""
import os, sys, json, argparse, subprocess, tempfile
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from timeline import mouth_params
from align import align
from face_pack import blink_frames

FPS = 25


def shape_track(voice, text, style):
    """Mouth shape numbers per frame (as still_head.py makes them) for one line."""
    with tempfile.TemporaryDirectory() as t:
        wav = os.path.join(t, 'v16k.wav')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', voice, '-ac', '1', '-ar', '16000', wav], check=True)
        letters = align(wav, text)
        inf = sf.info(wav)
        P, _ = mouth_params(letters, wav, inf.frames / inf.samplerate, FPS, clear=style == 'clear')
    return P


def pick(P, shapes, style, stay=0.08):
    """Closest picture per frame; keep the last one when it is almost as close (less flicker)."""
    S = np.array(shapes, float)
    w = np.array([1 / 95, 1 / 1.5, 1 / 1.5]) if style == 'clear' else np.array([1 / 70, 1, 1])
    seq, prev = [], None
    for p in P:
        d = np.sqrt((((S - p) * w) ** 2).sum(1)); j = int(np.argmin(d))
        if prev is not None and d[prev] <= d[j] + stay:
            j = prev
        seq.append(j); prev = j
    return seq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('face_dir'); ap.add_argument('voice'); ap.add_argument('text'); ap.add_argument('line')
    ap.add_argument('--style', choices=('normal', 'clear'), default='normal')
    a = ap.parse_args()
    fj = os.path.join(a.face_dir, 'face.json'); F = json.load(open(fj))
    if not F.get('mouth_shapes'):
        raise SystemExit('this pack has no shape numbers; remake it with pack_persona.py from face_pack.py --params packs')
    P = shape_track(a.voice, open(a.text, encoding='utf-8').read(), a.style)
    seq = pick(P, F['mouth_shapes'], a.style)
    out = os.path.join(a.face_dir, a.line + '.json'); os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump({'fps': FPS, 'mouth': seq, 'blinks': blink_frames(len(seq), FPS)}, open(out, 'w'), separators=(',', ':'))
    F['lines'] = sorted(set(F.get('lines', [])) | {a.line})
    json.dump(F, open(fj, 'w'), indent=1)
    print(f'{a.line}: {len(seq)} frames, {len(set(seq))} of {len(F["mouth_shapes"])} pictures used')


if __name__ == '__main__':
    main()
