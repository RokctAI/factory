"""LivePortrait pass with the head held still: only the jaw and lips move, driven by
the voice (letters pick the shape, loudness sets how open). No blinks, sway or
smile, so every frame lines up with one fixed picture and only the mouth area
changes. Blinks are added later as eye pictures.

  python still_head.py --portrait card.webp --letters letters.json --wav voice16k.wav --out frames/ [--style clear]
--style clear is the Grade R-3 mouth (Ray, 2026-11-20: a separate pack per style).
Writes frames/f_00000.png ... at 25 fps, cropped to the head-and-shoulders 3:4 box,
and frames/params.npy (the mouth shape numbers of each frame)."""
import os, sys, json, argparse
import numpy as np, cv2, soundfile as sf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lpcore import Face
from timeline import mouth_params

FPS = 25


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--portrait', required=True)
    ap.add_argument('--letters', required=True, help='align.py output')
    ap.add_argument('--wav', required=True, help='16 kHz mono copy of the voice line')
    ap.add_argument('--out', required=True)
    ap.add_argument('--style', choices=('normal', 'clear'), default='normal',
                    help="'clear' = Grade R-3: wider, rounder mouth shapes held longer")
    ap.add_argument('--width', type=int, default=480, help='output width (3:4); 480 = phone size')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    inf = sf.info(a.wav); dur = inf.frames / inf.samplerate
    P, _ = mouth_params(json.load(open(a.letters)), a.wav, dur, FPS, clear=a.style == 'clear')
    f = Face(a.portrait)
    x0, y0, x1, y1 = f.view_box()
    W = a.width // 2 * 2; H = int(W * 4 / 3) // 2 * 2
    for i in range(len(P)):
        im = f.render(aaa=P[i, 0], eee=P[i, 1], woo=P[i, 2])[y0:y1, x0:x1]
        im = cv2.resize(im, (W, H), interpolation=cv2.INTER_AREA)
        cv2.imwrite(os.path.join(a.out, f'f_{i:05d}.png'), cv2.cvtColor(im, cv2.COLOR_RGB2BGR))
    np.save(os.path.join(a.out, 'params.npy'), P)   # mouth shape per frame, for face_pack.py --params
    print(f'frames {len(P)}')


if __name__ == '__main__':
    main()
