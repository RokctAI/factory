"""Letters with times -> mouth-shape (viseme) track, plus a blink schedule."""
import json, numpy as np
VIS = {  # name: LivePortrait expression edit
 'rest': {},
 'mbp':  dict(aaa=-10),             # lips pressed: m b p
 'small':dict(aaa=22),              # most consonants: t d s n k g r h z y c j x
 'ee':   dict(eee=12, aaa=28),      # e i
 'aa':   dict(aaa=70),              # a
 'oh':   dict(woo=10, aaa=45),      # o
 'oo':   dict(woo=16, aaa=12),      # u w q
 'fv':   dict(eee=8, aaa=4),        # f v
 'l':    dict(aaa=38),              # l
 'sh':   dict(woo=9, aaa=16),       # sh ch j - lips pushed forward, teeth near
 'th':   dict(aaa=20, eee=5),       # th - tongue between teeth
}
DIGRAPH = {'sh':'sh', 'ch':'sh', 'th':'th', 'ph':'fv', 'wh':'oo', 'oo':'oo', 'ee':'ee'}
def clear_vis(scale=1.5):
    """'Clear' mouth set for Grade R-3: wider, rounder, more teeth, lips firmly shut on m/b/p."""
    out = {}
    for k, v in VIS.items():
        w = {kk: vv*scale for kk, vv in v.items()}
        if 'aaa' in w: w['aaa'] = min(w['aaa'], 95)   # wider than this looks stretched on a photo
        if k == 'mbp': w = dict(aaa=-14)
        out[k] = w
    return out
CH = {}
for c in 'mbp': CH[c]='mbp'
for c in 'tdsnkgrhzycjx': CH[c]='small'
for c in 'ei': CH[c]='ee'
CH['a']='aa'; CH['o']='oh'
for c in 'uwq': CH[c]='oo'
for c in 'fv': CH[c]='fv'
CH['l']='l'
BLINK = {'half': dict(blink=-9), 'shut': dict(blink=-20)}

def merge_digraphs(chars):
    out, i = [], 0
    while i < len(chars):
        if i+1 < len(chars) and chars[i][0]+chars[i+1][0] in DIGRAPH and chars[i+1][1]-chars[i][2] < 0.05:
            out.append([chars[i][0]+chars[i+1][0], chars[i][1], chars[i+1][2]]); i += 2
        else: out.append(chars[i]); i += 1
    return out

def mouth_track(chars, dur, fps, gap=0.14, min_hold=0.0):
    n = int(np.ceil(dur*fps)); track = ['rest']*n
    segs = []
    chars = merge_digraphs(chars)
    for i,(c,s,e) in enumerate(chars):
        e = max(e, s + min_hold)
        nxt = chars[i+1][1] if i+1 < len(chars) else e+0.08
        end = nxt if nxt - e < gap else e + 0.06   # hold into the next letter unless a pause
        segs.append((DIGRAPH.get(c) or CH.get(c,'small'), s-0.03, end-0.03))  # mouth leads the sound slightly
    for v,s,e in segs:
        for f in range(max(0,int(s*fps)), min(n,int(np.ceil(e*fps)))): track[f]=v
    return track

def blink_track(dur, fps, times=(1.5, 4.35, 6.3)):
    n = int(np.ceil(dur*fps)); tr = [None]*n
    for t in times:
        f = int(t*fps)
        for k,st in enumerate(['half','shut','shut','half']):
            if 0 <= f+k < n: tr[f+k] = st
    return tr

# ---- v2: mouth follows the voice's loudness; letters only pick the shape ----
SHAPE = {  # openness weight, ee spread, oo rounding
 'rest':(0.0,0,0), 'mbp':(None,0,0), 'small':(0.45,0,0), 'ee':(0.55,12,0), 'aa':(1.0,0,0), 'oh':(0.8,0,10),
 'oo':(0.3,0,16), 'fv':(0.12,8,0), 'l':(0.5,0,0), 'sh':(0.3,0,9), 'th':(0.35,5,0)}
def loudness(wav_path, n, fps):
    import soundfile as sf
    y, sr = sf.read(wav_path)
    if y.ndim > 1: y = y.mean(1)
    hop = sr / fps; out = np.zeros(n)
    for i in range(n):
        seg = y[int(i*hop):int((i+1)*hop)]
        out[i] = np.sqrt(np.mean(seg**2)) if len(seg) else 0
    db = 20*np.log10(out/ (out.max()+1e-9) + 1e-9)
    return np.clip((db + 32) / 26, 0, 1)          # -32 dB -> shut, -6 dB and up -> fully open
def mouth_params(chars, wav_path, dur, fps, clear=False):
    from scipy.ndimage import gaussian_filter1d
    n = int(np.ceil(dur*fps))
    shapes = mouth_track(chars, dur, fps, min_hold=0.08 if clear else 0)
    loud = loudness(wav_path, n, fps)
    loud = np.concatenate([loud[1:], loud[-1:]])  # mouth leads the sound by one frame
    loud = gaussian_filter1d(loud, 0.8)
    top = 95 if clear else 70; k = 1.5 if clear else 1.0
    P = np.zeros((n, 3))
    for i, s in enumerate(shapes):
        w, ee, oo = SHAPE[s]
        if w is None: P[i] = (-12, 0, 0); continue
        if s == 'rest': w = 0.35                    # between words: still follow any sound there
        o = loud[i] ** 0.8
        P[i] = (top * w * o, k * ee * (0.5 + 0.5*o), k * oo * (0.5 + 0.5*o))
    return gaussian_filter1d(P, 0.9, axis=0), shapes
