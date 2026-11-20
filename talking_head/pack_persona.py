"""Merge one team member's line packs into ONE shared picture set (Ray's idea,
2026-11-20): every greeting and sign-off reuses the same mouth pictures, and each
line keeps only a small timing file that picks which picture shows when.

Every line is drawn from the same portrait with the head held still, so their
base pictures match; the first line's base and eye pictures become the shared
ones. Each line's mouth pictures are placed on that base, cut to one common
mouth box, and near-duplicates across ALL lines are merged.

  python pack_persona.py <lines_dir> <face_dir> [--merge 3.5] [--no-lines]
--no-lines is for stand-in speech (a member with no voice yet): only the shared
pictures and their shape numbers are kept; line_timing.py adds real lines later.
<lines_dir> holds <category>/<line>/ folders made by face_pack.py. Writes:
  <face_dir>/base.webp, eyes_open|half|shut.webp, m000.webp ...
  <face_dir>/face.json                    size, mouth_box, eyes_box, line list
  <face_dir>/<category>/<line>.json       fps, mouth (picture per frame), blinks"""
import os, sys, json, glob, shutil, argparse
import numpy as np, cv2


def feather(h, w, r=10):
    m = np.ones((h, w), np.float32); m[:r] = m[-r:] = 0; m[:, :r] = m[:, -r:] = 0
    return cv2.GaussianBlur(m, (0, 0), r / 2)[..., None]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('lines_dir'); ap.add_argument('face_dir')
    ap.add_argument('--merge', type=float, default=3.5)
    ap.add_argument('--no-lines', action='store_true',
                    help='stand-in speech: keep only the shared pictures, no per-line timing files')
    a = ap.parse_args()
    lines = sorted(os.path.relpath(os.path.dirname(t), a.lines_dir)
                   for t in glob.glob(os.path.join(a.lines_dir, '*', '*', 'timing.json')))
    if not lines:
        raise SystemExit('no line packs found')
    os.makedirs(a.face_dir, exist_ok=True)
    first = os.path.join(a.lines_dir, lines[0])
    for f in ('base.webp', 'eyes_open.webp', 'eyes_half.webp', 'eyes_shut.webp'):
        shutil.copy(os.path.join(first, f), os.path.join(a.face_dir, f))
    T = {ln: json.load(open(os.path.join(a.lines_dir, ln, 'timing.json'))) for ln in lines}
    base = cv2.imread(os.path.join(a.face_dir, 'base.webp')).astype(np.float32)
    boxes = np.array([T[ln]['mouth_box'] for ln in lines])
    box = [int(boxes[:, 0].min()), int(boxes[:, 1].max()), int(boxes[:, 2].max()), int(boxes[:, 3].max())]
    # top edge: the LOWEST line top, so no shared picture reaches up into the nose
    x0, y0, x1, y1 = box
    small = lambda im: cv2.resize(im, (48, 36), interpolation=cv2.INTER_AREA).astype(float)
    kept, ks, sh = [], [], []   # sh: shape numbers seen for each shared picture
    for ln in lines:
        t = T[ln]; d = os.path.join(a.lines_dir, ln)
        own = cv2.imread(os.path.join(d, 'base.webp')).astype(np.float32)
        diff = float(np.abs(own - base).mean())
        bx0, by0, bx1, by1 = t['mouth_box']; fm = feather(by1 - by0, bx1 - bx0)
        remap = {}
        for i in sorted(set(t['mouth'])):
            pic = cv2.imread(os.path.join(d, f'm{i:03d}.webp')).astype(np.float32)
            full = base.copy(); full[by0:by1, bx0:bx1] = full[by0:by1, bx0:bx1] * (1 - fm) + pic * fm
            cut = full[y0:y1, x0:x1].clip(0, 255).astype(np.uint8); s = small(cut)
            if ks:
                dd = [np.abs(s - k).mean() for k in ks]; j = int(np.argmin(dd))
                if dd[j] < a.merge:
                    remap[i] = j
                    if t.get('shapes') and t['shapes'][i]: sh[j].append(t['shapes'][i])
                    continue
            kept.append(cut); ks.append(s); remap[i] = len(kept) - 1
            sh.append([t['shapes'][i]] if t.get('shapes') and t['shapes'][i] else [])
        if a.no_lines:
            print(f'{ln}: {len(set(t["mouth"]))} own pictures, base difference {diff:.1f}, shared set now {len(kept)}')
            continue
        out = os.path.join(a.face_dir, ln + '.json'); os.makedirs(os.path.dirname(out), exist_ok=True)
        json.dump({'fps': t['fps'], 'mouth': [remap[i] for i in t['mouth']], 'blinks': t['blinks']},
                  open(out, 'w'), separators=(',', ':'))
        print(f'{ln}: {len(set(t["mouth"]))} own pictures, base difference {diff:.1f}, shared set now {len(kept)}')
    for i, im in enumerate(kept):
        cv2.imwrite(os.path.join(a.face_dir, f'm{i:03d}.webp'), im, [cv2.IMWRITE_WEBP_QUALITY, 85])
    t0 = T[lines[0]]
    # each shared picture's shape numbers (mean of the lines' pictures merged into it), for line_timing.py
    shapes = [np.round(np.mean(v, 0), 2).tolist() if v else None for v in sh]
    if any(v is None for v in shapes):
        shapes = None
    json.dump({'size': t0['size'], 'mouth_box': box, 'eyes_box': t0['eyes_box'], 'base': 'base.webp',
               'eyes': {k: f'eyes_{k}.webp' for k in ('open', 'half', 'shut')}, 'mouth_pictures': len(kept),
               'mouth_shapes': shapes, 'lines': [] if a.no_lines else lines}, open(os.path.join(a.face_dir, 'face.json'), 'w'), indent=1)
    kb = sum(os.path.getsize(p) for p in glob.glob(os.path.join(a.face_dir, '**', '*'), recursive=True)
             if os.path.isfile(p)) / 1024
    print(f'{len(lines)} lines -> {len(kept)} shared mouth pictures, {kb:.0f} KB in all')


if __name__ == '__main__':
    main()
