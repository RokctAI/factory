# A hand-drawn single-stroke print font for the R-3 pictures (school print:
# single-storey a and g). Units: baseline y=0, x-height -10, caps -14,
# ascenders -15, descenders +6. Each glyph: (advance, path, dots).
import re
from lib import INK, WHITE

def _ell(cx, cy, rx, ry):
    return f'M{cx-rx:g} {cy:g} A{rx:g} {ry:g} 0 1 0 {cx+rx:g} {cy:g} A{rx:g} {ry:g} 0 1 0 {cx-rx:g} {cy:g}'

BOWL = _ell(4.5, -5, 4.5, 5)
G = {
 'a': (11, BOWL + ' M9 -10 L9 0', []),
 'b': (11, 'M0 -15 L0 0 ' + BOWL, []),
 'c': (10, 'M8.6 -8 A4.5 5 0 1 0 8.6 -2', []),
 'd': (11, BOWL + ' M9 -15 L9 0', []),
 'e': (11, 'M0.4 -5 L9 -5 A4.5 5 0 1 0 7.8 -1.4', []),
 'f': (8, 'M7 -14.4 Q6 -15 4.6 -15 Q2 -15 2 -12 L2 0 M0 -10 L6 -10', []),
 'g': (11, BOWL + ' M9 -10 L9 2.5 Q9 6 4.5 6 Q2 6 0.6 4.6', []),
 'h': (11, 'M0 -15 L0 0 M0 -6 Q0 -10 4.5 -10 Q9 -10 9 -6 L9 0', []),
 'i': (4, 'M0 -10 L0 0', [(0, -14)]),
 'j': (6, 'M2.5 -10 L2.5 2.5 Q2.5 6 -0.5 5.6', [(2.5, -14)]),
 'k': (10, 'M0 -15 L0 0 M8 -10 L0 -4.4 M2.6 -6.2 L8.4 0', []),
 'l': (4, 'M0 -15 L0 0', []),
 'm': (16, 'M0 -10 L0 0 M0 -6.5 Q0 -10 3.5 -10 Q7 -10 7 -6.5 L7 0 M7 -6.5 Q7 -10 10.5 -10 Q14 -10 14 -6.5 L14 0', []),
 'n': (11, 'M0 -10 L0 0 M0 -6 Q0 -10 4.5 -10 Q9 -10 9 -6 L9 0', []),
 'o': (11, BOWL, []),
 'p': (11, 'M0 -10 L0 6 ' + BOWL, []),
 'q': (11, BOWL + ' M9 -10 L9 6', []),
 'r': (8, 'M0 -10 L0 0 M0 -5.5 Q0 -10 4.5 -10 L6.4 -10', []),
 's': (10, 'M8 -8.6 Q7 -10 4.4 -10 Q1 -10 1 -7.4 Q1 -5.4 4.5 -5 Q8.4 -4.6 8.4 -2.5 Q8.4 0 4.4 0 Q1.4 0 0.4 -1.6', []),
 't': (8, 'M2.5 -14 L2.5 -2.5 Q2.5 0 5 0 L6 0 M0 -10 L6 -10', []),
 'u': (11, 'M0 -10 L0 -4 Q0 0 4.5 0 Q9 0 9 -4 M9 -10 L9 0', []),
 'v': (11, 'M0 -10 L4.5 0 L9 -10', []),
 'w': (16, 'M0 -10 L3.5 0 L7 -8 L10.5 0 L14 -10', []),
 'x': (11, 'M0 -10 L9 0 M9 -10 L0 0', []),
 'y': (11, 'M0 -10 L4.6 -0.6 M9 -10 L3.6 3.6 Q2.6 6 0 5.6', []),
 'z': (11, 'M0 -10 L9 -10 L0 0 L9 0', []),
 'A': (12, 'M0 0 L5 -14 L10 0 M2 -5 L8 -5', []),
 'B': (12, 'M0 0 L0 -14 L5 -14 Q9 -14 9 -10.5 Q9 -7 5 -7 L0 -7 M5 -7 Q10 -7 10 -3.5 Q10 0 5 0 L0 0', []),
 'C': (12, 'M10 -12 Q8 -14 5.6 -14 Q0 -14 0 -7 Q0 0 5.6 0 Q8 0 10 -2', []),
 'D': (12, 'M0 0 L0 -14 L4 -14 Q10 -14 10 -7 Q10 0 4 0 Z', []),
 'E': (11, 'M9 -14 L0 -14 L0 0 L9 0 M0 -7 L7 -7', []),
 'F': (11, 'M9 -14 L0 -14 L0 0 M0 -7 L7 -7', []),
 'G': (12, 'M10 -12 Q8 -14 5.6 -14 Q0 -14 0 -7 Q0 0 5.6 0 Q10 0 10 -5 L10 -6 L6 -6', []),
 'H': (12, 'M0 -14 L0 0 M10 -14 L10 0 M0 -7 L10 -7', []),
 'I': (6, 'M2 -14 L2 0 M0 -14 L4 -14 M0 0 L4 0', []),
 'J': (10, 'M8 -14 L8 -4 Q8 0 4 0 Q0 0 0 -3', []),
 'K': (12, 'M0 -14 L0 0 M9.6 -14 L0 -5.6 M3.4 -8.4 L10 0', []),
 'L': (10, 'M0 -14 L0 0 L8 0', []),
 'M': (14, 'M0 0 L0 -14 L6 -5 L12 -14 L12 0', []),
 'N': (12, 'M0 0 L0 -14 L10 0 L10 -14', []),
 'O': (12, _ell(5, -7, 5, 7), []),
 'P': (12, 'M0 0 L0 -14 L5 -14 Q10 -14 10 -10 Q10 -6 5 -6 L0 -6', []),
 'Q': (12, _ell(5, -7, 5, 7) + ' M6 -3 L10.6 1', []),
 'R': (12, 'M0 0 L0 -14 L5 -14 Q10 -14 10 -10 Q10 -6 5 -6 L0 -6 M5 -6 L10 0', []),
 'S': (12, 'M9.6 -12 Q8 -14 5 -14 Q0.6 -14 0.6 -10.6 Q0.6 -7.6 5 -7 Q10 -6.4 10 -3.6 Q10 0 5 0 Q1.6 0 0 -2', []),
 'T': (12, 'M0 -14 L10 -14 M5 -14 L5 0', []),
 'U': (12, 'M0 -14 L0 -5 Q0 0 5 0 Q10 0 10 -5 L10 -14', []),
 'V': (12, 'M0 -14 L5 0 L10 -14', []),
 'W': (16, 'M0 -14 L3.5 0 L7 -10 L10.5 0 L14 -14', []),
 'X': (12, 'M0 -14 L10 0 M10 -14 L0 0', []),
 'Y': (12, 'M0 -14 L5 -7 L10 -14 M5 -7 L5 0', []),
 'Z': (12, 'M0 -14 L10 -14 L0 0 L10 0', []),
 '0': (11, _ell(4.5, -7, 4.5, 7), []),
 '1': (8, 'M0.6 -11 L4.4 -14 L4.4 0', []),
 '2': (11, 'M0.6 -11 Q1.2 -14 4.6 -14 Q9 -14 9 -10.4 Q9 -8 6 -5.4 L0 0 L9.4 0', []),
 '3': (11, 'M0.6 -12 Q2 -14 4.6 -14 Q9 -14 9 -10.5 Q9 -7 4.6 -7 Q9.6 -7 9.6 -3.5 Q9.6 0 4.6 0 Q1.6 0 0 -2', []),
 '4': (11, 'M7 0 L7 -14 L0 -4 L10 -4', []),
 '5': (11, 'M9 -14 L1.2 -14 L0.6 -8 Q2 -9 4.6 -9 Q9.6 -9 9.6 -4.5 Q9.6 0 4.6 0 Q1.6 0 0 -2', []),
 '6': (11, 'M8 -13 Q6.6 -14 4.6 -14 Q0 -14 0 -5 ' + _ell(4.5, -4.5, 4.5, 4.5), []),
 '7': (11, 'M0 -14 L9.6 -14 L3.6 0', []),
 '8': (11, _ell(4.5, -10.6, 3.6, 3.4) + ' ' + _ell(4.5, -3.6, 4.4, 3.6), []),
 '9': (11, _ell(4.5, -9.5, 4.5, 4.5) + ' M9 -9.5 L9 -4 Q9 0 4.4 0 Q1.8 0 0.4 -1.4', []),
 '.': (4, '', [(1, -0.4)]),
 ',': (4, 'M1.6 -0.6 L0.4 2.6', []),
 '?': (10, 'M0.6 -11 Q1.2 -14 4.6 -14 Q8.6 -14 8.6 -10.6 Q8.6 -8.2 5.6 -7 Q4.6 -6.6 4.6 -4.4', [(4.6, -0.4)]),
 '!': (4, 'M1 -14 L1 -4.4', [(1, -0.4)]),
 "'": (4, 'M1 -15 L1 -11', []),
 '"': (6, 'M1 -15 L1 -11 M4 -15 L4 -11', []),
 '-': (7, 'M0 -5 L5 -5', []),
 '+': (10, 'M0 -6 L8 -6 M4 -10 L4 -2', []),
 '*': (10, 'M0.6 -9.4 L7.4 -2.6 M7.4 -9.4 L0.6 -2.6', []),
 '%': (10, 'M0 -6 L8 -6', [(4, -10), (4, -2)]),
 '=': (10, 'M0 -8 L8 -8 M0 -4 L8 -4', []),
 '<': (10, 'M8 -10.4 L0 -6 L8 -1.6', []),
 '>': (10, 'M0 -10.4 L8 -6 L0 -1.6', []),
 ':': (4, '', [(1, -8), (1, -1)]),
 '/': (8, 'M0 1 L6 -15', []),
 '_': (12, 'M0 1.5 L10 1.5', []),
 '(': (6, 'M4 -15 Q0 -11 0 -5 Q0 1 4 5', []),
 ')': (6, 'M0 -15 Q4 -11 4 -5 Q4 1 0 5', []),
 '@': (14, _ell(6, -6, 3, 3.4) + ' M9 -9 L9 -4.4 Q9 -2 11 -2 Q13 -2 13 -6.6 Q13 -13 6 -13 Q-1 -13 -1 -6 Q-1 1 6.4 1 Q9 1 10.6 0', []),
 ' ': (5, '', []),
}
NUMS = re.compile(r'-?\d*\.?\d+')


def _shift(d, dx, dy=0):
    """Shift absolute M/L/Q/A path data by (dx, dy)."""
    out = []
    for cmd, args in re.findall(r'([MLQAZ])([^MLQAZ]*)', d):
        n = [float(v) for v in NUMS.findall(args)]
        if cmd == 'A':
            for i in range(0, len(n), 7):
                n[i + 5] += dx
                n[i + 6] += dy
        else:
            for i in range(0, len(n), 2):
                n[i] += dx
                n[i + 1] += dy
        out.append(cmd + ' '.join(f'{v:.1f}'.rstrip('0').rstrip('.') for v in n))
    return ' '.join(out)


def measure(s, track=0):
    w = 0
    for ch in s:
        w += G.get(ch, G['?'])[0] + track
    return max(0, w - 2 - track)


def glyph_run(s, track=0):
    """Path data and dots for a string set on one line from x=0."""
    ds, dots, x = [], [], 0
    for ch in s:
        adv, d, dt = G.get(ch, G['?'])
        if d:
            ds.append(_shift(d, x))
        dots += [(x + a, b) for a, b in dt]
        x += adv + track
    return ' '.join(ds), dots


def _num(v):
    return f'{v:.1f}'.rstrip('0').rstrip('.')


def text(s, x, y, size, col=INK, sw=None, anchor='middle', outline=False, fill=WHITE):
    """Draw s with its baseline at y, cap height size px. anchor: start,
    middle, end. outline=True draws chunky outlined letters (fill colour
    inside a dark rim)."""
    k = size / 14
    sw = sw or max(3.0, size * 0.17)
    tr = (sw + (6 if outline else 0)) / k * 0.45
    w = measure(s, tr) * k
    x0 = x - (w / 2 if anchor == 'middle' else w if anchor == 'end' else 0)
    d, dots = glyph_run(s, tr)
    t = f'translate({_num(x0)} {_num(y)}) scale({k:.3f})'
    if outline:
        inner = sw
        rim = sw + 6
        o = f'<g class="w" transform="{t}">'
        if d:
            o += f'<path d="{d}" stroke-width="{_num(rim / k)}"/>'
        for a, b in dots:
            o += f'<circle cx="{_num(a)}" cy="{_num(b)}" r="{_num(rim * .62 / k)}" fill="{INK}" stroke="none"/>'
        if d:
            o += f'<path d="{d}" stroke="{fill}" stroke-width="{_num(inner / k)}"/>'
        for a, b in dots:
            o += f'<circle cx="{_num(a)}" cy="{_num(b)}" r="{_num(inner * .62 / k)}" fill="{fill}" stroke="none"/>'
        return o + '</g>'
    o = f'<g class="w" transform="{t}" stroke="{col}" stroke-width="{_num(sw / k)}">'
    if d:
        o += f'<path d="{d}"/>'
    for a, b in dots:
        o += f'<circle cx="{_num(a)}" cy="{_num(b)}" r="{_num(sw * .62 / k)}" fill="{col}" stroke="none"/>'
    return o + '</g>'


def width(s, size, sw=None, outline=False):
    k = size / 14
    sw = sw or max(3.0, size * 0.17)
    return measure(s, (sw + (6 if outline else 0)) / k * 0.45) * k + sw


def fit(s, maxw, maxsize, outline=False):
    """The cap height that fits s into maxw px, at most maxsize."""
    size = maxsize
    while size > 6 and width(s, size, outline=outline) > maxw:
        size *= 0.95
    return size


def texts(items, size, col=INK, sw=None):
    """Several short centred strings [(s, x, baseline_y)], one word group
    each (fitfix keeps each inside its shape), sharing one stroke and
    scale."""
    if len(items) == 1:
        return text(*items[0], size, col=col, sw=sw)
    k = size / 14
    sw = sw or max(3.0, size * 0.17)
    tr = sw / k * 0.45
    o = ''
    for st, x, y in items:
        w = measure(st, tr) * k
        d, dots = glyph_run(st, tr)
        g = f'<g class="w" transform="translate({_num((x - w / 2) / k)} {_num(y / k)})">'
        if d:
            g += f'<path d="{d}"/>'
        for a, b in dots:
            g += f'<circle cx="{_num(a)}" cy="{_num(b)}" r="{_num(sw * .62 / k)}" fill="{col}" stroke="none"/>'
        o += g + '</g>'
    return f'<g transform="scale({k:.3f})" stroke="{col}" stroke-width="{_num(sw / k)}">' + o + '</g>'


# ------------------------------------------------------------ boxed words
# Size and place words by their real ink box (strokes, outline rim, dots,
# descenders), so they sit centred inside a shape with padding.
def ink_box(s, size, sw=None, outline=False):
    """(x0, top, x1, bottom) of s drawn by text(s, 0, 0, size,
    anchor='middle'), in px."""
    from fitfix import subpaths
    k = size / 14
    sw = sw or max(3.0, size * 0.17)
    tr = (sw + (6 if outline else 0)) / k * 0.45
    w = measure(s, tr) * k
    d, dots = glyph_run(s, tr)
    rim = (sw + 6) if outline else sw
    xs, ys = [], []
    for sp, _ in subpaths(d):
        for x, y in sp:
            xs += [x * k - rim / 2, x * k + rim / 2]
            ys += [y * k - rim / 2, y * k + rim / 2]
    for x, y in dots:
        r = rim * .62
        xs += [x * k - r, x * k + r]
        ys += [y * k - r, y * k + r]
    if not xs:
        return (-1, -1, 1, 1)
    return (min(xs) - w / 2, min(ys), max(xs) - w / 2, max(ys))


def pitch(boxes, size, lh=1.5, gap=4):
    """Baseline-to-baseline distance for stacked lines: lh x size, or more
    so one line's ink stays `gap` px clear of the next."""
    p = size * lh
    for a, b in zip(boxes, boxes[1:]):
        p = max(p, a[3] - b[1] + gap)
    return p


def fit_size(lines, w, h, maxsize, sw=None, outline=False, lh=1.5):
    """The biggest size (<= maxsize) at which every line fits w wide and
    the stack of lines fits h tall."""
    if isinstance(lines, str):
        lines = [lines]
    size = maxsize
    while size > 4:
        boxes = [ink_box(l, size, sw, outline) for l in lines]
        bw = max(b[2] - b[0] for b in boxes)
        bh = (len(lines) - 1) * pitch(boxes, size, lh) + boxes[-1][3] - boxes[0][1]
        if bw <= w and bh <= h:
            return size
        size *= 0.96
    return size


def boxed(lines, x, y, w, h, maxsize, pad=6, inset=3, col=INK, sw=None, outline=False, fill=WHITE, lh=1.5, size=None):
    """Lines of words centred in the box (x, y, w, h): `inset` is half the
    box's stroke, `pad` the gap from there to the ink."""
    if isinstance(lines, str):
        lines = [lines]
    m = inset + pad
    sz = size or fit_size(lines, w - 2 * m, h - 2 * m, maxsize, sw, outline, lh)
    boxes = [ink_box(l, sz, sw, outline) for l in lines]
    pt = pitch(boxes, sz, lh)
    top = boxes[0][1]
    bottom = (len(lines) - 1) * pt + boxes[-1][3]
    y0 = y + h / 2 - (top + bottom) / 2
    o = ''
    for i, (l, b) in enumerate(zip(lines, boxes)):
        o += text(l, x + w / 2 - (b[0] + b[2]) / 2, y0 + i * pt, sz, col=col, sw=sw, outline=outline, fill=fill)
    return o
