"""Turn one talking line (still-head LivePortrait + MuseTalk lips + sharpening) into
the pictures the app plays, instead of a video:

  <out>/base.webp          the face with the mouth at rest (median of the line)
  <out>/eyes_open.webp     eye-area pictures for blinks, drawn by LivePortrait on
  <out>/eyes_half.webp     that same base so they line up exactly
  <out>/eyes_shut.webp
  <out>/m000.webp ...      distinct mouth-area pictures (near-duplicates merged)
  <out>/timing.json        fps, the two boxes, which mouth picture each frame
                           shows, and the blink frames

The app shows base.webp, pastes the frame's mouth picture into mouth_box and the
eye picture into eyes_box (soft edges), in step with the line's audio.

The mouth box starts just below the nostrils: starting higher made the nose
move oddly (Ray, 2026-11-20).

  python face_pack.py lips.mp4 out_dir [--params params.npy] [--merge 3.5]
--params stores each mouth picture's shape numbers (timing.json 'shapes'), so
line_timing.py can later time new lines against the same pictures.
Needs LP_SRC (LivePortrait, used for the face points and the eye pictures)."""
import os, sys, json, argparse
import numpy as np, cv2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LP = os.environ.get('LP_SRC', '')


def read_frames(path):
    cap = cv2.VideoCapture(path); fps = cap.get(cv2.CAP_PROP_FPS) or 25; F = []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        F.append(f)
    return np.stack(F), fps


def face_points(img):
    sys.path.insert(0, LP)
    from src.utils.face_analysis_diy import FaceAnalysisDIY
    fa = FaceAnalysisDIY(name='buffalo_l', root=os.path.join(LP, 'pretrained_weights/insightface'),
                         providers=['CPUExecutionProvider'])
    fa.prepare(ctx_id=-1, det_size=(512, 512))
    f = fa.get(img)
    if not f:
        raise SystemExit('no face found in the base picture')
    return f[0]['kps'] if isinstance(f[0], dict) else f[0].kps


def mouth_box(F, base, top):
    """Where the frames really change (largest moving blob), from `top` down."""
    d = np.percentile(np.abs(F.astype(np.int16) - base[None].astype(np.int16)).sum(3), 90, axis=0)
    d[:top] = 0
    m = cv2.morphologyEx((d > 70).astype(np.uint8), cv2.MORPH_CLOSE, np.ones((15, 15), np.uint8))
    n, _, st, _ = cv2.connectedComponentsWithStats(m)
    if n < 2:
        raise SystemExit('the mouth never moves in this clip')
    k = 1 + int(np.argmax(st[1:, 4])); x0, y0, w, h = st[k, :4]
    H, W = base.shape[:2]; s = W / 584.          # margins were tuned on a 584-wide face
    return [int(max(0, x0 - 30 * s)), int(top), int(min(W, x0 + w + 30 * s)), int(min(H, y0 + h + 55 * s))]


def eye_pictures(base_path, kps, out):
    from lpcore import Face
    from timeline import BLINK
    f = Face(base_path)
    R = {'open': f.render(), **{k: f.render(**v) for k, v in BLINK.items()}}
    R = {k: cv2.cvtColor(v, cv2.COLOR_RGB2BGR) for k, v in R.items()}
    d = np.abs(R['shut'].astype(int) - R['open']).sum(2)
    eye_y = int(kps[:2, 1].mean()); nose_y = int(kps[2, 1])
    d[:max(0, eye_y - (nose_y - eye_y))] = 0; d[nose_y:] = 0
    ys, xs = np.nonzero(d > 40)
    p = 14; H, W = d.shape
    box = [int(max(0, xs.min() - p)), int(max(0, ys.min() - p)), int(min(W, xs.max() + p)), int(min(nose_y, ys.max() + p))]
    for k, im in R.items():
        cv2.imwrite(os.path.join(out, f'eyes_{k}.webp'), im[box[1]:box[3], box[0]:box[2]], [cv2.IMWRITE_WEBP_QUALITY, 90])
    return box


def blink_frames(n, fps, first=1.2, every=3.4):
    """Blink pattern (half, shut, shut, half) roughly every few seconds."""
    from timeline import blink_track
    t = np.arange(first, n / fps - 0.3, every)
    tr = blink_track(n / fps, fps, times=tuple(t))
    return [[i, s] for i, s in enumerate(tr[:n]) if s]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('clip'); ap.add_argument('out')
    ap.add_argument('--params', help="still_head.py's params.npy: store each picture's mouth shape numbers")
    ap.add_argument('--merge', type=float, default=3.5,
                    help='how different two mouth pictures must be to keep both (higher = fewer pictures)')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    F, fps = read_frames(a.clip)
    base = np.median(F, 0).astype(np.uint8)
    base_png = os.path.join(a.out, '.base.png'); cv2.imwrite(base_png, base)
    cv2.imwrite(os.path.join(a.out, 'base.webp'), base, [cv2.IMWRITE_WEBP_QUALITY, 90])
    kps = face_points(base)
    nose_y, mouth_y = kps[2, 1], kps[3:5, 1].mean()
    top = int(nose_y + 0.45 * (mouth_y - nose_y))          # just under the nostrils
    box = mouth_box(F, base, top)
    P = F[:, box[1]:box[3], box[0]:box[2]]
    small = lambda im: cv2.resize(im, (48, 36), interpolation=cv2.INTER_AREA).astype(float)
    kept, ks, seq = [], [], []
    for im in P:
        s = small(im)
        if ks:
            dd = [np.abs(s - k).mean() for k in ks]; j = int(np.argmin(dd))
            if dd[j] < a.merge:
                seq.append(j); continue
        kept.append(im); ks.append(s); seq.append(len(kept) - 1)
    for i, im in enumerate(kept):
        cv2.imwrite(os.path.join(a.out, f'm{i:03d}.webp'), im, [cv2.IMWRITE_WEBP_QUALITY, 85])
    eyes = eye_pictures(base_png, kps, a.out)
    os.remove(base_png)
    shapes = None
    if a.params:
        Q = np.load(a.params)[:len(seq)]; sq = np.array(seq[:len(Q)])
        shapes = [np.round(Q[sq == j].mean(0), 2).tolist() if (sq == j).any() else None for j in range(len(kept))]
    timing = {'fps': round(fps, 3), 'size': [int(base.shape[1]), int(base.shape[0])],
              'mouth_box': box, 'eyes_box': eyes, 'mouth': seq, 'blinks': blink_frames(len(F), fps)}
    if shapes:
        timing['shapes'] = shapes
    json.dump(timing, open(os.path.join(a.out, 'timing.json'), 'w'), separators=(',', ':'))
    kb = sum(os.path.getsize(os.path.join(a.out, f)) for f in os.listdir(a.out)) / 1024
    print(f'{len(F)} frames -> {len(kept)} mouth pictures, {kb:.0f} KB in all')


if __name__ == '__main__':
    main()
