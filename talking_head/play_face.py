"""Preview a face pack the way the app plays it: the base picture, the timing
file's mouth picture pasted into mouth_box with soft edges (a light fade between
pictures), and the eye pictures on blink frames. Any head movement is applied
AFTER the layers are put together, to the whole stack (base + eyes + mouth) as
one picture, so the eyes and mouth always move with the head and never slide. Writes PNG frames; mux the
line's own audio over them to watch.

  python play_face.py <face_dir> <category>/<line> <out_frames_dir> [--sway]"""
import os, sys, json
import numpy as np, cv2


def feather(h, w, r):
    m = np.ones((h, w), np.float32); m[:r] = m[-r:] = 0; m[:, :r] = m[:, -r:] = 0
    return cv2.GaussianBlur(m, (0, 0), r / 2)[..., None]


def sway(fr, t):
    """Gentle idle movement of the WHOLE composed picture (small tilt and drift)."""
    H, W = fr.shape[:2]
    A = cv2.getRotationMatrix2D((W / 2, H * 0.55), 0.8 * np.sin(2 * np.pi * t / 6.1), 1.0)
    A[0, 2] += 3 * np.sin(2 * np.pi * t / 5.3); A[1, 2] += 2 * np.sin(2 * np.pi * t / 3.7)
    return cv2.warpAffine(fr, A, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)


def main(face_dir, line, out, move=False):
    os.makedirs(out, exist_ok=True)
    F = json.load(open(os.path.join(face_dir, 'face.json')))
    L = json.load(open(os.path.join(face_dir, line + '.json')))
    rd = lambda f: cv2.imread(os.path.join(face_dir, f)).astype(np.float32)
    base = rd(F['base']); eyes = {k: rd(v) for k, v in F['eyes'].items()}
    mx0, my0, mx1, my1 = F['mouth_box']; ex0, ey0, ex1, ey1 = F['eyes_box']
    mm = feather(my1 - my0, mx1 - mx0, 10); em = feather(ey1 - ey0, ex1 - ex0, 8)
    blinks = {i: s for i, s in L['blinks']}; pics = {}; prev = None
    for i, k in enumerate(L['mouth']):
        cur = pics.setdefault(k, rd(f'm{k:03d}.webp'))
        m = cur if prev is None else 0.25 * prev + 0.75 * cur; prev = m
        fr = base.copy()
        fr[my0:my1, mx0:mx1] = fr[my0:my1, mx0:mx1] * (1 - mm) + m * mm
        fr[ey0:ey1, ex0:ex1] = fr[ey0:ey1, ex0:ex1] * (1 - em) + eyes[blinks.get(i, 'open')] * em
        if move:
            fr = sway(fr, i / L['fps'])
        cv2.imwrite(os.path.join(out, f'p_{i:05d}.png'), fr.clip(0, 255).astype(np.uint8))
    print(f'{len(L["mouth"])} frames')


if __name__ == '__main__':
    main(*sys.argv[1:4], move='--sway' in sys.argv)
