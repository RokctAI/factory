# Scene kit: people in poses, spatial compositions, sequences, badges.
from mkit import *
from font import texts
from g_text import word_card, strip

ARMS = {'down': ((-34, -60), (34, -60)), 'up': ((-44, -134), (44, -134)), 'wave': ((-34, -60), (46, -140)), 'out': ((-56, -96), (56, -96)),
        'hold': ((-24, -76), (24, -76)), 'point': ((-34, -60), (64, -104)), 'hip': ((-30, -66), (30, -66)), 'give': ((-34, -60), (60, -90)),
        'chest': ((-12, -92), (12, -92)), 'face': ((-14, -118), (14, -118)), 'mouth': ((-34, -60), (8, -112)), 'ear': ((-34, -60), (28, -128)),
        'clap': ((-6, -104), (6, -104)), 'reach': ((-34, -60), (40, -150)), 'carry': ((-30, -100), (30, -100))}
CH = {
    'boy': dict(skin=SKIN1, shirt=GOLD, pants=BLUE, hairstyle='short'),
    'girl': dict(skin=SKIN2, shirt=ROSE, pants=PK, hairstyle='puffs', skirt=True),
    'sipho': dict(skin=SKIN2, shirt=GREEN, pants=NIGHT, hairstyle='short'),
    'zola': dict(skin=SKIN2, shirt=PURPLE, pants=PU, hairstyle='puffs', skirt=True),
    'neo': dict(skin=SKIN1, shirt=BLUE, pants=NIGHT, hairstyle='cap', haircol=RED),
    'thandi': dict(skin=SKIN2, shirt=ORANGE, pants=OR, hairstyle='bun', skirt=True),
    'lebo': dict(skin=SKIN1, shirt='#2BA6A0', pants=G, hairstyle='long', skirt=True),
    'jabu': dict(skin=SKIN2, shirt=RED, pants=BLUE, hairstyle='short'),
    'man': dict(skin=SKIN2, shirt=BLUE, pants=NIGHT, hairstyle='short'),
    'woman': dict(skin=SKIN2, shirt=GREEN, pants=G, hairstyle='scarf', haircol=RED, skirt=True),
    'mama': dict(skin=SKIN2, shirt=GREEN, hairstyle='scarf', haircol=RED, skirt=True),
    'gogo': dict(skin=SKIN2, shirt=PU, pants=PU, hairstyle='grey', skirt=True, glasses=True),
    'mkhulu': dict(skin=SKIN2, shirt=TAN, pants=BROWN, hairstyle='grey', glasses=True),
    'teacher': dict(skin=SKIN3, shirt=ORANGE, hairstyle='long', skirt=True),
    'tutor': dict(skin=SKIN1, shirt=PURPLE, pants=NIGHT, hairstyle='bun', glasses=True),
}
KIDS = {'boy', 'girl', 'sipho', 'zola', 'neo', 'thandi', 'lebo', 'jabu'}


def who_(c='boy', x=100, y=182, s=None, arms='down', legs='stand', face='smile', flip=False, **kw):
    d = dict(CH[c])
    d.update(kw)
    la, ra = ARMS[arms] if isinstance(arms, str) else arms
    if flip:
        la, ra = (-ra[0], ra[1]), (-la[0], la[1])
    s = s if s is not None else (.92 if c in KIDS else 1.05)
    return g(x, y, s, person(la=la, ra=ra, legs=legs, face_kind=face, **d))


def hand_pos(c='boy', x=100, y=182, s=None, arms='down', side='r', flip=False):
    s = s if s is not None else (.92 if c in KIDS else 1.05)
    la, ra = ARMS[arms]
    if flip:
        la, ra = (-ra[0], ra[1]), (-la[0], la[1])
    hx, hy = ra if side == 'r' else la
    return x + hx * s, y + hy * s


def holding(c, slug, x=100, y=182, s=None, arms='give', ts=.3, side='r', dx=0, dy=-10, flip=False, **kw):
    hx, hy = hand_pos(c, x, y, s, arms, side, flip)
    return who_(c, x, y, s, arms, flip=flip, **kw) + thing(slug, hx + dx, hy + dy, ts)


def sky(ground=G, skyc=B, hz=140):
    return R(0, 0, 200, hz, skyc, sw=0) + R(0, hz, 200, 200 - hz, ground, sw=0)


def room(wall='#FFF1D6', floor='#E8C99A', hz=140):
    return R(0, 0, 200, hz, wall, sw=0) + R(0, hz, 200, 200 - hz, floor, sw=0) + P(f'M0 {hz} H200', None, 4)


def night(hz=150):
    return R(0, 0, 200, hz, NIGHT, sw=0) + R(0, hz, 200, 200 - hz, '#2E5A3A', sw=0) + C(160, 40, 16, '#F2C94C', 4) + dot(40, 30, 3, WHITE) + dot(90, 50, 3, WHITE) + dot(120, 20, 3, WHITE)


def framed(*parts, col=WHITE):
    return R(8, 8, 184, 184, col, rx=16) + ''.join(parts) + R(8, 8, 184, 184, None, rx=16)


def pair(a, b, s=.5, y=104, gap=0, sh=True):
    return (S(100, 100 + 100 * s + 22, 86) if sh else '') + thing(a, 52 - gap, y, s) + thing(b, 148 + gap, y, s)


def trio(a, b, c, s=.36, y=104):
    return S(100, y + 100 * s + 8, 88) + thing(a, 36, y, s) + thing(b, 100, y, s) + thing(c, 164, y, s)


def quad(a, b, c, d, s=.42):
    return thing(a, 54, 54, s) + thing(b, 146, 54, s) + thing(c, 54, 146, s) + thing(d, 146, 146, s)


def steps(slugs, s=None, y=104):
    n = len(slugs)
    s = s or min(.5, 1.8 / n / 1.1 * .5)
    gap = 196 / n
    o = ''
    for i, sl in enumerate(slugs):
        cx = 2 + gap * (i + .5)
        o += thing(sl, cx, y, s)
        if i < n - 1:
            o += arrow(cx + gap * .32, y, cx + gap * .68, y, sw=4)
    return o


def row_of(slug, n, hi=None, s=None, y=110):
    s = s or min(.4, 180 / n / 200 * 1.2)
    gap = 184 / n
    o = ''
    for i in range(n):
        cx = 8 + gap * (i + .5)
        if hi is not None and i == hi:
            o += C(cx, y, gap * .5, '#FFE08A', 0, 'opacity=".9"')
        o += thing(slug, cx, y, s)
    return o


def rel(a, b, how, sa=.36, sb=.7):
    """Picture a placed relative to a bigger picture b."""
    o = S(100, 186, 76)
    bx, by = 100, 112
    if how == 'behind':
        return o + thing(a, 120, 92, sa) + thing(b, bx, by, sb)
    o += thing(b, bx, by, sb)
    pos = {'on': (100, by - 70 * sb - 30 * sa * 2), 'under': (100, 170), 'in': (100, by), 'in_front': (86, 156), 'next': (178, 150),
           'left': (24, 150), 'right': (176, 150), 'above': (100, 26), 'over': (100, 26), 'below': (100, 176)}[how]
    if how == 'in':
        return o + thing(a, pos[0], pos[1], sa * .8)
    return o + thing(a, pos[0], pos[1], sa)


def nope(*parts):
    return ''.join(parts) + badge_cross(162, 38)


def yep(*parts):
    return ''.join(parts) + badge_tick(162, 38)


def say(c, words, x=100, s=None, bx=None, by=14, bw=None, arms='down', **kw):
    """A person with a speech bubble holding words."""
    lines = wrap(words.split(), 12)
    m = 3 + 6
    sz = fit_size(lines, (bw or 150) - 2 * m, 999, 18)
    boxes = [ink_box(l, sz) for l in lines]
    bw = bw or max(b[2] - b[0] for b in boxes) + 2 * m + 6
    bh = (len(lines) - 1) * sz * 1.5 + boxes[-1][3] - boxes[0][1] + 2 * m + 4
    bx = bx if bx is not None else max(6, min(194 - bw, x - bw / 2 + 20))
    o = who_(c, x, 186, s, arms, **kw)
    o += bubble_say(bx, by, bw, bh, (x + 6, by + bh + 22))
    return o + boxed(lines, bx, by, bw, bh, sz, pad=6, inset=3)


def bubble_words(lines, x, y, w, hh, tail, size=16):
    """A speech bubble with its words centred inside, clear of the edge."""
    return bubble_say(x, y, w, hh, tail) + boxed(lines, x, y, w, hh, size, pad=6, inset=3)


def think(x, y, w, hh, inner):
    return E(x, y, w / 2, hh / 2, WHITE) + C(x - w * .3, y + hh * .62, 7, WHITE, 4) + C(x - w * .4, y + hh * .82, 4, WHITE, 3) + inner


def hearts(x, y, n=2):
    return ''.join(P(f'M{x + i * 18} {y + 8} Q{x + i * 18 - 12} {y} {x + i * 18 - 6} {y - 6} Q{x + i * 18} {y - 8} {x + i * 18} {y - 2} Q{x + i * 18} {y - 8} {x + i * 18 + 6} {y - 6} Q{x + i * 18 + 12} {y} {x + i * 18} {y + 8} Z', RED, 3) for i in range(n))


def label_under(slug, words, s=.62):
    return thing(slug, 100, 80, s) + R(14, 148, 172, 40, WHITE, rx=10) + boxed([words], 14, 148, 172, 40, 22, pad=6, inset=3)


def sign_post(words, col=Y, x=100, y=60, w=140):
    lines = wrap(words.split(), 12)
    sz = fit_size(lines, w - 18, 999, 20)
    boxes = [ink_box(l, sz) for l in lines]
    hh = (len(lines) - 1) * sz * 1.5 + boxes[-1][3] - boxes[0][1] + 22
    o = P(f'M{x} {y + hh} L{x} 182', None, 8) + R(x - w / 2, y, w, hh, col, rx=8)
    o += boxed(lines, x - w / 2, y, w, hh, sz, pad=6, inset=3)
    return S(x, 184, 40) + o


def peg(c, x, y=182, hh=100, arms='down', face='smile'):
    """A compact child for crowds: about 450 bytes, same outline and face."""
    d = CH[c]
    k = hh / 100
    r = lambda v: int(round(v))
    X = lambda v: r(x + v * k)
    Y = lambda v: r(y + v * k)
    w = lambda v: round(max(2, v * k), 1)
    sk = d['skin']
    o = P(f'M{X(-6)} {Y(-30)}L{X(-7)} {Y(-2)}M{X(6)} {Y(-30)}L{X(7)} {Y(-2)}', None, w(9))
    sx = 19 if d.get('skirt') else 15
    o += P(f'M{X(-13)} {Y(-62)}L{X(13)} {Y(-62)}L{X(sx)} {Y(-26)}L{X(-sx)} {Y(-26)}Z', d['shirt'], w(5))
    ax = {'down': None, 'up': (-22, -90, 22, -90), 'wave': (-18, -34, 24, -88), 'out': (-30, -62, 30, -62), 'give': (-18, -34, 32, -56)}[arms]
    if ax:
        a = f'M{X(-12)} {Y(-58)}L{X(ax[0])} {Y(ax[1])}M{X(12)} {Y(-58)}L{X(ax[2])} {Y(ax[3])}'
        o += P(a, None, w(11)) + P(a, None, w(5), f'stroke="{sk}"')
    hy = -78
    o += C(X(0), Y(hy), r(16 * k), sk, w(5))
    hc = d.get('haircol', HAIR) if d.get('hairstyle') != 'grey' else '#D9DCE3'
    o += P(f'M{X(-16)} {Y(hy - 2)}Q{X(-16)} {Y(hy - 18)} {X(0)} {Y(hy - 18)}Q{X(16)} {Y(hy - 18)} {X(16)} {Y(hy - 2)}Q{X(0)} {Y(hy - 11)} {X(-16)} {Y(hy - 2)}Z', hc, w(4))
    if d.get('hairstyle') == 'puffs':
        o += C(X(-16), Y(hy - 12), r(6 * k), hc, w(4)) + C(X(16), Y(hy - 12), r(6 * k), hc, w(4))
    if face == 'sad':
        m = f'M{X(-6)} {Y(hy + 10)}Q{X(0)} {Y(hy + 5)} {X(6)} {Y(hy + 10)}'
    elif face == 'flat':
        m = f'M{X(-5)} {Y(hy + 8)}H{X(5)}'
    else:
        m = f'M{X(-6)} {Y(hy + 6)}Q{X(0)} {Y(hy + 12)} {X(6)} {Y(hy + 6)}'
    o += P(f'M{X(-6)} {Y(hy)}h0M{X(6)} {Y(hy)}h0' + m, None, w(4.5))
    return o


def peg_row(n, hi=None, y=176, hh=None, names=('boy', 'girl', 'sipho', 'zola', 'neo', 'thandi', 'lebo', 'jabu')):
    gap = 196 / n
    hh = hh or min(110, gap * 3.4)
    o = S(100, y + 2, 92)
    for i in range(n):
        cx = r1(2 + gap * (i + .5))
        if hi is not None and i == hi:
            o += E(cx, r1(y - hh * .5), r1(max(gap * .5, hh * .3)), r1(hh * .56), '#FFE08A', 0)
            o += P(f'M{cx} {r1(y - hh * 1.32)} V{r1(y - hh * 1.06)} M{r1(cx - 8)} {r1(y - hh * 1.14)} L{cx} {r1(y - hh * 1.06)} L{r1(cx + 8)} {r1(y - hh * 1.14)}', None, 6, f'stroke="{RED}"')
        o += peg(names[i % len(names)], cx, y, hh)
    return o


def r1(v):
    return round(v, 1)
