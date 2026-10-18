# Shared building blocks for the Grades 1-3 pictures.
from props import *
from font import text, fit, width, boxed, fit_size, ink_box
import lib
import content

TILES = [Y, B, G, PK, PU, OR]
INKS = [RED, BLUE, DGREEN, ROSE, PURPLE, ORANGE]
S = shadow


def h(s):
    v = 0
    for c in s:
        v = (v * 31 + ord(c)) & 0x7fffffff
    return v


MISSING = {}


def thing(slug, x=100, y=100, s=1):
    """Another picture's body, scaled by s about its centre and moved so its
    centre lands at (x, y)."""
    if slug not in lib.ALL and slug not in lib.SAMPLES:
        MISSING[slug] = MISSING.get(slug, 0) + 1
        content.MISSING.add('picture:' + slug)
        return g(x - 100 * s, y - 100 * s, s, C(100, 100, 60, '#FF00FF'))
    return g(x - 100 * s, y - 100 * s, s, body(slug))


def tile(label, x, y, w, hgt, col=None, ink=None, outline=True, size=None, rx=None):
    i = h(label)
    col = col or TILES[i % 6]
    ink = ink or INKS[(i // 6) % 6]
    rx = rx if rx is not None else min(w, hgt) * .18
    # biggest outlined label that sits inside with padding, centred by ink
    pad = max(min(6, (min(w, hgt) - 6) * .2), min(w, hgt) * .1)
    mx = size or hgt * .62
    if outline and tile_cramped(label, w, hgt, mx):
        # a small tile: the outline rim would eat the letter, so dark ink
        return R(x, y, w, hgt, col, rx=rx) + boxed([label], x, y, w, hgt, mx, pad=pad, inset=3)
    return R(x, y, w, hgt, col, rx=rx) + boxed([label], x, y, w, hgt, mx, pad=pad, inset=3, outline=outline, fill=ink)


def tile_cramped(label, w, hgt, mx):
    """True when an outlined label would come out much smaller than plain."""
    pad = max(min(6, (min(w, hgt) - 6) * .2), min(w, hgt) * .1)
    m = 2 * (3 + pad)
    return fit_size([label], w - m, hgt - m, mx, outline=True) < .75 * fit_size([label], w - m, hgt - m, mx)


def corner_tile(label, corner, col=None, ink=None):
    """A big letter tile with a picture over its bottom-right corner; the
    letters sit in the part of the tile the corner leaves clear."""
    i = h(label)
    col = col or TILES[i % 6]
    ink = ink or INKS[(i // 6) % 6]
    return (S(96, 176, 70) + R(22, 22, 148, 148, col, rx=26.6)
            + boxed([label], 22, 22, 148, 100, 148 * .62, pad=10, inset=3, outline=True, fill=ink) + corner)


def big_tile(label, corner=None, col=None, ink=None):
    if corner:
        return corner_tile(label, thing(corner, 156, 150, .36), col, ink)
    return S(100, 180, 70) + tile(label, 26, 26, 148, 148, col, ink)


def tile_row(parts, y=72, hgt=56, gap=8, maxw=176, cols=None):
    n = len(parts)
    ws = [max(hgt, width(p, hgt * .5, outline=True) + 22) if p else hgt for p in parts]
    tot = sum(ws) + gap * (n - 1)
    k = min(1, maxw / tot)
    ws = [w * k for w in ws]
    hh = hgt * k
    x = 100 - (sum(ws) + gap * k * (n - 1)) / 2
    out = ''
    # one style for the whole row: outlined, or plain dark ink when any
    # tile is too small for the outline rim
    ol = not any(tile_cramped(p, w, hh, hh * .62) for p, w in zip(parts, ws) if p)
    for i, (p, w) in enumerate(zip(parts, ws)):
        if p:
            out += tile(p, x, y + (hgt - hh) / 2, w, hh, col=(cols[i] if cols else None), size=hh * .62, outline=ol, ink=None if ol else INK)
        else:
            out += R(x, y + (hgt - hh) / 2, w, hh, WHITE, rx=hh * .18, sw=4, extra='stroke-dasharray="8 8"')
        x += w + gap * k
    return out


def card(lines, x=20, y=50, w=160, hgt=100, col=WHITE, size=None, ink=INK, rx=12):
    """A paper card with lines of text, centred inside with padding."""
    pad = max(min(6, (min(w, hgt) - 6) * .2), min(w, hgt) * .1)
    return R(x, y, w, hgt, col, rx=rx) + boxed(lines, x, y, w, hgt, size or 40, pad=pad, inset=3, col=ink)


def wrap(words, maxchars):
    lines, cur = [], ''
    for wd in words:
        if cur and len(cur) + 1 + len(wd) > maxchars:
            lines.append(cur); cur = wd
        else:
            cur = (cur + ' ' + wd).strip()
    if cur:
        lines.append(cur)
    return lines


def badge_cross(cx=160, cy=40):
    return C(cx, cy, 22, WHITE) + P(f'M{cx-10} {cy-10} L{cx+10} {cy+10} M{cx+10} {cy-10} L{cx-10} {cy+10}', None, 7, f'stroke="{RED}"')


def badge_tick(cx=160, cy=40):
    return C(cx, cy, 22, WHITE) + P(f'M{cx-11} {cy} L{cx-3} {cy+9} L{cx+12} {cy-9}', None, 7, f'stroke="{DGREEN}"')


def arrow(x1, y1, x2, y2, col=INK, sw=6):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    l = 12
    p1 = (x2 - l * math.cos(a - .5), y2 - l * math.sin(a - .5))
    p2 = (x2 - l * math.cos(a + .5), y2 - l * math.sin(a + .5))
    return P(f'M{x1:.0f} {y1:.0f} L{x2:.0f} {y2:.0f} M{p1[0]:.0f} {p1[1]:.0f} L{x2:.0f} {y2:.0f} L{p2[0]:.0f} {p2[1]:.0f}', None, sw, f'stroke="{col}"' if col != INK else '')


def bubble_say(x, y, w, hgt, tail=(0, 0), col=WHITE):
    tx, ty = tail
    return P(f'M{x+14} {y} L{x+w-14} {y} Q{x+w} {y} {x+w} {y+14} L{x+w} {y+hgt-14} Q{x+w} {y+hgt} {x+w-14} {y+hgt} L{x+w*.45:.0f} {y+hgt} L{tx} {ty} L{x+w*.3:.0f} {y+hgt} L{x+14} {y+hgt} Q{x} {y+hgt} {x} {y+hgt-14} L{x} {y+14} Q{x} {y} {x+14} {y} Z', col)


def grid_of(slug, n, box=(14, 20, 172, 160), maxs=.5):
    """n copies of a picture in a grid inside box."""
    import math
    x0, y0, w, hh = box
    cols = math.ceil(math.sqrt(n * w / hh))
    rows = math.ceil(n / cols)
    cell = min(w / cols, hh / rows)
    s = min(maxs, cell / 200 * 1.1)
    out = ''
    for i in range(n):
        r, c = divmod(i, cols)
        inrow = min(cols, n - r * cols)
        cx = x0 + w / 2 + (c - (inrow - 1) / 2) * cell
        cy = y0 + hh / 2 + (r - (rows - 1) / 2) * cell
        out += thing(slug, cx, cy, s)
    return out


def _n(v):
    return f'{round(v, 1):g}'


def mini(kind, x, y, r=10, col=None):
    """Tiny one- or two-element icons for counting pictures (r is the radius)."""
    X = lambda v: _n(x + v * r)
    Y = lambda v: _n(y + v * r)
    sw = _n(max(2.5, r * .35))
    if kind == 'bird':
        return (P(f'M{X(-1)} {Y(0)}Q{X(-1)} {Y(-1)} {X(0)} {Y(-1)}Q{X(1)} {Y(-1)} {X(1)} {Y(0)}L{X(1.5)} {Y(.2)}L{X(1)} {Y(.5)}Q{X(0)} {Y(1.1)} {X(-1)} {Y(.4)}L{X(-1.6)} {Y(-.3)}Z', col or BLUE, sw)
                + C(X(.4), Y(-.35), _n(r * .14), INK, 0))
    if kind == 'cup':
        return P(f'M{X(-.8)} {Y(-.8)}H{X(.8)}L{X(.6)} {Y(.9)}H{X(-.6)}ZM{X(.8)} {Y(-.4)}Q{X(1.4)} {Y(-.3)} {X(.7)} {Y(.4)}', col or WHITE, sw)
    if kind == 'nest':
        return P(f'M{X(-1.2)} {Y(-.2)}Q{X(0)} {Y(.6)} {X(1.2)} {Y(-.2)}Q{X(1)} {Y(.9)} {X(0)} {Y(.9)}Q{X(-1)} {Y(.9)} {X(-1.2)} {Y(-.2)}Z', col or '#B5834F', sw)
    if kind == 'apple':
        return C(X(0), Y(.1), _n(r * .9), col or RED, sw) + P(f'M{X(0)} {Y(-.8)}L{X(.2)} {Y(-1.2)}', None, sw)
    if kind == 'egg':
        return E(X(0), Y(0), _n(r * .75), _n(r), col or CREAM, sw)
    if kind == 'ball':
        return C(X(0), Y(0), _n(r), col or RED, sw)
    if kind == 'star':
        pts = ' '.join(f'{X(math.cos(math.radians(-90 + i * 36)) * (1 if i % 2 == 0 else .45))} {Y(math.sin(math.radians(-90 + i * 36)) * (1 if i % 2 == 0 else .45))}' for i in range(10))
        return P('M' + pts + 'Z', col or GOLD, sw)
    if kind == 'flower':
        return C(X(0), Y(0), _n(r * .9), col or ROSE, sw) + C(X(0), Y(0), _n(r * .35), GOLD, sw)
    if kind == 'fish':
        return P(f'M{X(-1)} {Y(0)}Q{X(0)} {Y(-1)} {X(.8)} {Y(0)}Q{X(0)} {Y(1)} {X(-1)} {Y(0)}ZM{X(.8)} {Y(0)}L{X(1.4)} {Y(-.6)}V{Y(.6)}Z', col or FISH, sw)
    if kind == 'sweet':
        return C(X(0), Y(0), _n(r * .7), col or ROSE, sw) + P(f'M{X(-.7)} {Y(0)}L{X(-1.4)} {Y(-.5)}V{Y(.5)}ZM{X(.7)} {Y(0)}L{X(1.4)} {Y(-.5)}V{Y(.5)}Z', col or ROSE, sw)
    if kind == 'leaf':
        return P(f'M{X(-1)} {Y(.8)}Q{X(-1)} {Y(-1)} {X(1)} {Y(-1)}Q{X(1)} {Y(.8)} {X(-1)} {Y(.8)}Z', col or GREEN, sw)
    if kind == 'block':
        return R(X(-.9), Y(-.9), _n(r * 1.8), _n(r * 1.8), col or Y, sw=sw)
    if kind == 'bun':
        return P(f'M{X(-1)} {Y(.5)}Q{X(-1)} {Y(-.8)} {X(0)} {Y(-.8)}Q{X(1)} {Y(-.8)} {X(1)} {Y(.5)}Z', col or '#E3A75F', sw)
    raise KeyError(kind)


import math


def num_sentence(tokens, x=14, y=60, w=172, hgt=84, col=WHITE, maxsize=30, blank=Y):
    """A number sentence on a card as a row of tokens: numbers and signs
    are words, None is a blank box. Neighbours keep a gap, and the row is
    scaled to fit inside the card's padding, centred."""
    m = 3 + 6
    def lay(s):
        gap = max(5, s * .4)
        items = []
        for t in tokens:
            if t is None:
                items.append(('box', s * 1.25 + 4, s * 1.6 + 4))
            else:
                b = ink_box(t, s)
                items.append(('w', b[2] - b[0], b[3] - b[1], b))
        tw = sum(it[1] for it in items) + gap * (len(items) - 1)
        th = max(it[2] for it in items)
        return items, gap, tw, th
    s = maxsize
    while s > 6:
        items, gap, tw, th = lay(s)
        if tw <= w - 2 * m and th <= hgt - 2 * m:
            break
        s *= .97
    items, gap, tw, th = lay(s)
    out = R(x, y, w, hgt, col, rx=12)
    cx = x + (w - tw) / 2
    cy = y + hgt / 2
    for t, it in zip(tokens, items):
        if it[0] == 'box':
            bw, bh = it[1] - 4, it[2] - 4
            out += R(round(cx + 2, 1), round(cy - bh / 2, 1), round(bw, 1), round(bh, 1), blank, rx=4, sw=4)
        else:
            b = it[3]
            # place the ink box's left edge at cx and its middle on cy
            out += text(t, cx - b[0] - (b[2] - b[0]) / 2 + (b[2] - b[0]) / 2, cy - (b[1] + b[3]) / 2, s)
        cx += it[1] + gap
    return out
