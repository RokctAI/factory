# Drawing helpers for the R-3 pictures. Every shape is written by hand;
# these helpers only save typing the shared outline attributes.
INK = '#1F2A44'
Y, B, G, PK, PU, OR = '#FFE08A', '#B8E6FF', '#C8F2C2', '#FFC9DE', '#E2D4FF', '#FFD2B0'
GOLD, BUSY, ORANGE, FISH, TAN, BROWN, CREAM = '#FFD25A', '#FFC23D', '#F2A65A', '#FFB347', '#E9B872', '#9C6B3C', '#FFF3DE'
RED, BLUE, ROSE, GREY, WHITE, MOONY = '#E8574A', '#5B8DEF', '#E86A8C', '#E2E3DE', '#FFFFFF', '#F2C94C'
GREEN, DGREEN, PURPLE, DGREY, SKY = '#6CC46C', '#3E9B4F', '#9B7BE0', '#9AA1AE', '#7EC8F2'
SKIN1, SKIN2, SKIN3 = '#C68B59', '#8D5A3B', '#F1C27D'
HAIR = '#3B2A1E'
NIGHT = '#34416B'

import content

ALL = {}


def art(slug, *parts):
    content.settle(slug)
    ALL[slug] = ''.join(parts)


def svg(body):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">'
            '<g fill="none" stroke="#1F2A44" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">'
            + body + '</g></svg>')


def _a(fill, sw, extra):
    s = ''
    if fill is not None:
        s += f' fill="{fill}"'
    if sw is not None:
        s += ' stroke="none"' if sw == 0 else f' stroke-width="{sw}"'
    return s + (' ' + extra if extra else '')


def P(d, fill=None, sw=None, extra=''):
    return f'<path d="{d}"{_a(fill, sw, extra)}/>'


def C(cx, cy, r, fill=None, sw=None, extra=''):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}"{_a(fill, sw, extra)}/>'


def E(cx, cy, rx, ry, fill=None, sw=None, extra=''):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}"{_a(fill, sw, extra)}/>'


def R(x, y, w, h, fill=None, rx=0, sw=None, extra=''):
    r = f' rx="{rx}"' if rx else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}"{r}{_a(fill, sw, extra)}/>'


def dot(cx, cy, r=5, fill=INK):
    return C(cx, cy, r, fill, 0)


def shadow(cx=100, cy=182, rx=60, ry=7):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#1F2A44" stroke="none" opacity=".12"/>'


def g(tx, ty, s, *parts, rot=None):
    """Place parts drawn on the 200 box at (tx,ty) scaled by s, keeping the
    outline about 6 wide on screen."""
    t = f'translate({tx:g} {ty:g})' + (f' rotate({rot:g})' if rot else '') + (f' scale({s:g})' if s != 1 else '')
    sw = '' if s == 1 else f' stroke-width="{round(6 / s, 1):g}"'
    return f'<g transform="{t}"{sw}>' + ''.join(parts) + '</g>'


def limb(d, fill, w=12):
    """A thick limb with a dark outline: ink underneath, color on top."""
    return P(d, None, w + 10) + P(d, None, w, f'stroke="{fill}"')


def smile(cx, cy, w=8, sw=None):
    return P(f'M{cx - w} {cy} Q{cx} {cy + w * .8} {cx + w} {cy}', sw=sw)


def eyes(cx, cy, gap=16, r=5):
    return dot(cx - gap / 2, cy, r) + dot(cx + gap / 2, cy, r)


def cross(cx, cy, r=14):
    """A red 'no' cross badge."""
    return (C(cx, cy, r + 4, WHITE) +
            P(f'M{cx - r / 2} {cy - r / 2} L{cx + r / 2} {cy + r / 2} M{cx + r / 2} {cy - r / 2} L{cx - r / 2} {cy + r / 2}', None, 6, f'stroke="{RED}"'))


def tick(cx, cy, r=14):
    return (C(cx, cy, r + 4, WHITE) +
            P(f'M{cx - r / 2} {cy} L{cx - r / 8} {cy + r / 2.2} L{cx + r / 1.7} {cy - r / 2}', None, 6, f'stroke="{DGREEN}"'))


ALIAS = {}


def alias(name, target):
    ALIAS[name] = target


def body(slug):
    """A drawing's shapes without its ground shadow, for reuse in scenes."""
    b = ALL[slug]
    if b.startswith('<ellipse') and 'opacity=".12"' in b.split('/>', 1)[0]:
        b = b.split('/>', 1)[1]
    return b


import glob as _glob
import os as _os
import re as _re

SAMPLES = {}
for _f in _glob.glob(_os.path.join(_os.path.dirname(__file__), 'samples', '*.svg')):
    _s = open(_f).read()
    SAMPLES[_os.path.basename(_f)[:-4]] = _re.sub(r'^<svg[^>]*>|</svg>\s*$', '', _s.strip())


def body(slug):  # noqa: F811  (samples too)
    content.uses(slug)
    if slug not in ALL and slug not in SAMPLES:
        # drawn only when the packs name it: this picture waits for it
        content.MISSING.add('picture:' + slug)
        return ''
    b = ALL[slug] if slug in ALL else SAMPLES[slug]
    first = b.split('/>', 1)[0]
    if b.startswith('<ellipse') and 'opacity=".12"' in first:
        b = b.split('/>', 1)[1]
    return b
