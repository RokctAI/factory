# Maths drawing helpers: coins, notes, sticks, beads, ten-frames, jugs, scales.
from kit import *
from font import texts
import math

COPPER, SILVER, NOTEG, NOTEB, NOTER = '#E3A94B', '#D7DBE0', '#9BD48A', '#D9B48A', '#EE9A8A'


def coin(kind, cx, cy, r=24):
    """kind: 10c 20c 50c r1 r2 r5"""
    k = kind.lower()
    if k.endswith('c'):
        o = C(cx, cy, r, COPPER) + C(cx, cy, r * .78, None, 2, 'opacity=".4"')
        lab = k
    else:
        o = C(cx, cy, r, SILVER) + (C(cx, cy, r * .8, None, r * .22, f'stroke="{GOLD}"') + C(cx, cy, r * .68, SILVER, 2) if k == 'r5' else C(cx, cy, r * .78, None, 2, 'opacity=".4"'))
        lab = 'R' + k[1:]
    sz = fit(lab, r * 1.3, r * .7)
    return o + text(lab, cx, cy + sz / 2, sz, sw=max(2, r * .1))


def note(val, cx, cy, w=84):
    hh = w * .5
    col = {10: NOTEG, 20: NOTEB, 50: NOTER, 100: B, 200: OR}.get(val, NOTEG)
    o = R(cx - w / 2, cy - hh / 2, w, hh, col, rx=4) + C(cx + w * .34, cy, hh * .24, None, 2, 'opacity=".5"')
    lab = f'R{val}'
    sz = fit(lab, w * .58, hh * .38)
    return o + text(lab, cx - w * .12, cy + sz / 2, sz, sw=max(2, hh * .07))


def coins_row(kinds, cy=104, r=None):
    n = len(kinds)
    r = r or min(34, 170 / n / 2.3)
    gap = r * 2.3
    x0 = 100 - gap * (n - 1) / 2
    return ''.join(coin(k, x0 + i * gap, cy, r) for i, k in enumerate(kinds))


def price_tag(lab, cx=100, cy=100, s=1):
    return g(cx, cy, s, P('M-70 -40 L50 -40 L80 0 L50 40 L-70 40 Z', Y), C(52, 0, 7, WHITE, 4), P('M58 0 Q76 -30 92 -40', None, 3),
             text(lab, -12, 13, fit(lab, 110, 36)))


def stick(x, y1, y2, col=TAN):
    return P(f'M{x:.1f} {y1:.1f} L{x:.1f} {y2:.1f}', None, 9) + P(f'M{x:.1f} {y1:.1f} L{x:.1f} {y2:.1f}', None, 4, f'stroke="{col}"')


def bundle(cx, cy, hh=70, crossed=False):
    o = ''
    for i in range(-4, 5):
        o += P(f'M{cx + i * 2.4:.1f} {cy - hh / 2} L{cx + i * 2.4:.1f} {cy + hh / 2}', None, 2.6, f'stroke="{TAN}"')
    o = R(cx - 13, cy - hh / 2, 26, hh, TAN, rx=4) + P(''.join(f'M{cx + i * 5.2:.1f} {cy - hh / 2 + 4}V{cy + hh / 2 - 4}' for i in range(-2, 3)), None, 2, 'opacity=".4"')
    o += R(cx - 16, cy - 6, 32, 12, RED, rx=3, sw=4)
    if crossed:
        o += P(f'M{cx - 20} {cy - 26} L{cx + 20} {cy + 26} M{cx + 20} {cy - 26} L{cx - 20} {cy + 26}', None, 6, f'stroke="{RED}"')
    return o


def sticks_pic(tens, ones, y=100, hh=70, cross_t=0, cross_o=0, x0=None, maxw=176):
    bw, lw = 34, 12
    tot = tens * bw + (14 if tens and ones else 0) + ones * lw
    k = min(1, maxw / max(tot, 1))
    bw *= k; lw *= k
    x = (x0 if x0 is not None else 100 - tot * k / 2) + bw / 2
    o = ''
    for i in range(tens):
        o += g(x, y, k, bundle(0, 0, hh, i >= tens - cross_t)) if k != 1 else bundle(x, y, hh, i >= tens - cross_t)
        x += bw
    x += (14 * k if tens and ones else 0) - bw / 2 + lw / 2
    for i in range(ones):
        o += stick(x, y - hh / 2, y + hh / 2)
        if i >= ones - cross_o:
            o += P(f'M{x - 7:.1f} {y - 10} L{x + 7:.1f} {y + 10}', None, 5, f'stroke="{RED}"')
        x += lw
    return o


def beads(cols, y=100, x1=14, x2=186, r=None):
    n = len(cols)
    r = r or min(14, (x2 - x1) / n / 2.1)
    o = P(f'M{x1 - 4} {y} L{x2 + 4} {y}', None, 4)
    gap = (x2 - x1) / n
    for i, c in enumerate(cols):
        o += C(x1 + gap * (i + .5), y, r, c, 4)
    return o


def ten_frame(n, x, y, w=150, col=RED, n2=0, col2=BLUE):
    hh = w * .4
    o = R(x, y, w, hh, WHITE, rx=6, sw=4) + P(f'M{x} {y + hh / 2:.1f} L{x + w} {y + hh / 2:.1f}' + ''.join(f'M{x + w * i / 5:.1f} {y} L{x + w * i / 5:.1f} {y + hh:.1f}' for i in range(1, 5)), None, 3)
    for i in range(n + n2):
        r_, c_ = divmod(i, 5)
        o += C(x + w / 10 + c_ * w / 5, y + hh / 4 + r_ * hh / 2, hh / 4 - 5, col if i < n else col2, 3)
    return o


def counters(cols, cross=0, y=100, r=16, x1=20, x2=180, rows=1):
    n = len(cols)
    per = -(-n // rows)
    gap = min(r * 2.6, (x2 - x1) / per)
    o = ''
    for i, c in enumerate(cols):
        rr, cc = divmod(i, per)
        inrow = min(per, n - rr * per)
        cx = 100 + (cc - (inrow - 1) / 2) * gap
        cy = y + (rr - (rows - 1) / 2) * r * 2.6
        o += C(cx, cy, r, c)
        if i >= n - cross:
            o += P(f'M{cx - r} {cy - r} L{cx + r} {cy + r} M{cx + r} {cy - r} L{cx - r} {cy + r}', None, 5, f'stroke="{INK}"')
    return o


def jug(level, cx=100, by=176, hh=130, w=90, marks=4, label=None):
    """A measuring jug filled to level (0..1)."""
    x0, x1 = cx - w / 2, cx + w / 2
    top = by - hh
    o = P(f'M{x1 - 4} {top + 20} Q{x1 + 34} {top + 26} {x1 + 30} {top + 60} Q{x1 + 26} {top + 86} {x1 - 4} {top + 86}', None, 8)
    o += P(f'M{x0} {top} L{x1} {top} L{x1 - 6} {by} L{x0 + 6} {by} Z', '#EAF6FD')
    if level > 0:
        ly = by - (hh - 8) * level
        o += P(f'M{x0 + 6 - (by - ly) * 0:.1f} {ly:.1f} L{x1 - 6:.1f} {ly:.1f} L{x1 - 6} {by - 3} L{x0 + 6} {by - 3} Z', '#FFB347', 0)
    o += P(f'M{x0} {top} L{x1} {top} L{x1 - 6} {by} L{x0 + 6} {by} Z')
    o += P(''.join(f'M{x0 + 8} {by - (hh - 8) * i / marks:.1f} h16' for i in range(1, marks + 1)), None, 3)
    return o


def balance(left, right, tilt=0, ly=None):
    """A balance scale; tilt>0 means the left side is down. left/right are bodies at
    pan centres (0,0) local, drawn above the pan."""
    a = tilt * 12
    lx, rx = 100 - 62, 100 + 62
    lyy = 90 + a
    ryy = 90 - a
    o = P('M70 182 L130 182 M100 182 L100 70', None, 8) + R(66, 176, 68, 10, BROWN, rx=4)
    o += P(f'M{lx} {lyy} L{rx} {ryy}', None, 8) + C(100, 90, 7, GOLD, 4)
    for x, yy, b in ((lx, lyy, left), (rx, ryy, right)):
        o += P(f'M{x} {yy} L{x - 26} {yy + 40} M{x} {yy} L{x + 26} {yy + 40}', None, 3)
        o += P(f'M{x - 36} {yy + 40} L{x + 36} {yy + 40} Q{x} {yy + 60} {x - 36} {yy + 40} Z', GREY, 5)
        o += g(x, yy + 40, 1, b)
    return o


def cube_stack(n, x, by, s=14, col=Y):
    return ''.join(R(x, by - (i + 1) * s, s, s, col, sw=3) for i in range(n))


def chart_bars(vals, icons, maxv=None, cols=None):
    maxv = maxv or max(vals)
    n = len(vals)
    w = 150 / n
    o = P('M28 20 L28 160 L186 160', None, 5)
    for i, v in enumerate(vals):
        hh = 126 * v / maxv
        x = 34 + i * w + w * .15
        o += R(x, 160 - hh, w * .7, hh, (cols or INKS)[i % 6], rx=3, sw=4)
        o += thing(icons[i], x + w * .35, 178, .14)
    o += P(''.join(f'M22 {160 - 126 * j / maxv:.0f} h6' for j in range(1, maxv + 1)), None, 3)
    return o


def pictograph(rows, icons, unit, maxc=None):
    n = len(rows)
    hh = 160 / n
    o = R(10, 14, 180, 172, WHITE, rx=10)
    for i, (v, ic) in enumerate(zip(rows, icons)):
        y = 22 + i * hh + hh / 2
        o += thing(ic, 32, y, hh / 200 * .8)
        o += P(f'M54 {22 + i * hh:.0f} L54 {22 + (i + 1) * hh:.0f}', None, 3, 'opacity=".4"')
        step = min(hh * .9, 124 / max(1, maxc or max(rows)))
        r = step * .4
        o += ''.join(C(round(70 + j * step, 1), round(y, 1), round(r, 1), unit, 3) for j in range(v))
        o += P(''.join(f'M{70 + j * step - r * .45:.1f} {y + r * .1:.1f}q{r * .45:.1f} {r * .5:.1f} {r * .9:.1f} 0' for j in range(v)), None, 2.5)
    return o


def tally(n, x, y, hh=46, col=INK):
    o = ''
    xx = x
    for i in range(n):
        if i % 5 == 4:
            o += P(f'M{xx - 4 * 10 - 6:.0f} {y + hh - 8} L{xx + 2:.0f} {y + 8}', None, 6, f'stroke="{RED}"')
            xx += 16
        else:
            o += P(f'M{xx:.0f} {y} L{xx:.0f} {y + hh}', None, 6)
            xx += 10
    return o


def frac_rect(n, shaded, x=30, y=60, w=140, hh=80, col=BROWN, light='#C98B4E'):
    o = R(x, y, w, hh, light, rx=6)
    for i in range(shaded):
        o += R(x + w * i / n, y, w / n, hh, col, sw=0)
    o += R(x, y, w, hh, None, rx=6)
    o += P(''.join(f'M{x + w * i / n:.1f} {y} V{y + hh}' for i in range(1, n)), None, 5)
    return o


def frac_circle(n, shaded, cx=100, cy=100, r=66, col=BLUE, light=WHITE):
    o = C(cx, cy, r, light)
    for i in range(shaded):
        a1 = math.radians(-90 + 360 * i / n)
        a2 = math.radians(-90 + 360 * (i + 1) / n)
        large = 1 if 360 / n > 180 else 0
        o += P(f'M{cx} {cy} L{cx + r * math.cos(a1):.1f} {cy + r * math.sin(a1):.1f} A{r} {r} 0 {large} 1 {cx + r * math.cos(a2):.1f} {cy + r * math.sin(a2):.1f} Z', col, 0)
    o += C(cx, cy, r)
    if n > 1:
        o += P(''.join(f'M{cx} {cy} L{cx + r * math.cos(math.radians(-90 + 360 * i / n)):.1f} {cy + r * math.sin(math.radians(-90 + 360 * i / n)):.1f}' for i in range(n)), None, 5)
    return o


def calendar(title, first=0, days=30, marks=None, x=14, y=14, w=172, hh=172, col=RED, rows=None):
    """A month page: title bar, a 7-column grid of numbered days."""
    marks = marks or {}
    o = R(x, y, w, hh, WHITE, rx=8) + R(x, y, w, 30, col, rx=8) + R(x, y + 22, w, 8, col, sw=0) + P(f'M{x} {y + 30} h{w}', None, 5)
    o += text(title, x + w / 2, y + 22, 15, col=WHITE, sw=3.4)
    cw = (w - 12) / 7
    nrows = rows or -(-(first + days) // 7)
    rh = (hh - 38) / nrows
    nums = []
    for d in range(1, days + 1):
        i = first + d - 1
        r_, c_ = divmod(i, 7)
        if r_ >= nrows:
            break
        cx, cy = round(x + 6 + cw * (c_ + .5), 1), round(y + 34 + rh * (r_ + .5), 1)
        if d in marks:
            o += C(cx, cy, round(min(cw, rh) * .46, 1), marks[d], 3)
        nums.append((str(d), cx, cy + 4))
    return o + texts(nums, 9, sw=2)
