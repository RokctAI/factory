from people import *


def K(x=100, s=1, y=182, **kw):
    return g(x, y, s, kid(**kw))


def GL(x=100, s=1, y=182, **kw):
    return g(x, y, s, girl(**kw))


def AD(x=100, s=1, y=182, **kw):
    d = dict(skin=SKIN1, shirt=BLUE, pants=NIGHT, hairstyle='short')
    d.update(kw)
    return g(x, y, s, person(**d))


def GOGO(x=100, s=1, y=182, **kw):
    d = dict(skin=SKIN2, shirt=PU, pants=PU, hairstyle='grey', skirt=True, glasses=True)
    d.update(kw)
    return g(x, y, s, person(**d))


def MAMA(x=100, s=1, y=182, **kw):
    d = dict(skin=SKIN2, shirt=GREEN, hairstyle='scarf', haircol=RED, skirt=True)
    d.update(kw)
    return g(x, y, s, person(**d))


def ball(cx, cy, r=14):
    return C(cx, cy, r, WHITE) + P(f'M{cx - r * .35:.1f} {cy - r * .2:.1f} L{cx:.1f} {cy - r * .5:.1f} L{cx + r * .35:.1f} {cy - r * .2:.1f} L{cx + r * .22:.1f} {cy + r * .3:.1f} L{cx - r * .22:.1f} {cy + r * .3:.1f} Z', INK, 0)


def apple(cx, cy, r=12, col=RED):
    return C(cx, cy, r, col, 4) + P(f'M{cx} {cy - r} L{cx + 2} {cy - r - 7}', None, 4, f'stroke="{BROWN}"')


def crayon(x, y, col=RED, rot=0, s=1):
    return g(x, y, s, P('M-6 -22 L6 -22 L6 14 L0 24 L-6 14 Z', col, 4), rot=rot)


def book(cx, cy, w=36, col=BLUE):
    h = w * .7
    return P(f'M{cx} {cy - h / 2 + 4} Q{cx - w / 4} {cy - h / 2 - 2} {cx - w / 2} {cy - h / 2 + 2} L{cx - w / 2} {cy + h / 2} Q{cx - w / 4} {cy + h / 2 - 4} {cx} {cy + h / 2 + 2} Q{cx + w / 4} {cy + h / 2 - 4} {cx + w / 2} {cy + h / 2} L{cx + w / 2} {cy - h / 2 + 2} Q{cx + w / 4} {cy - h / 2 - 2} {cx} {cy - h / 2 + 4} Z', col, 4) + P(f'M{cx} {cy - h / 2 + 4} L{cx} {cy + h / 2 + 2}', None, 3)


def plate(cx, cy, r=26, food=None):
    out = E(cx, cy, r, r * .4, WHITE, 4)
    if food:
        out += food
    return out


def sink(x=100, y=120, water=True, bubbles=False):
    out = P(f'M{x - 50} {y} L{x + 50} {y} Q{x + 46} {y + 40} {x} {y + 40} Q{x - 46} {y + 40} {x - 50} {y} Z', WHITE)
    out += P(f'M{x - 30} {y - 4} L{x - 30} {y - 56} Q{x - 30} {y - 66} {x - 20} {y - 66} L{x + 6} {y - 66} L{x + 6} {y - 54}', None, 10, 'stroke="#9AA1AE"')
    out += P(f'M{x - 30} {y - 4} L{x - 30} {y - 56} Q{x - 30} {y - 66} {x - 20} {y - 66} L{x + 6} {y - 66} L{x + 6} {y - 54}', None, 4, 'stroke="#C9CED8"')
    if water:
        out += P(f'M{x + 6} {y - 50} L{x + 6} {y - 10}', None, 8, 'stroke="#7EC8F2"')
    if bubbles:
        out += C(x - 18, y - 20, 7, WHITE, 3) + C(x + 26, y - 30, 9, WHITE, 3) + C(x + 30, y - 8, 5, WHITE, 3)
    return out


def hands(x=100, y=110, fill=SKIN1, marks=''):
    """Two open hands side by side, palms to us."""
    hand = 'M-22 40 L-22 -6 L-30 -30 Q-32 -38 -24 -38 L-14 -16 L-14 -44 Q-14 -52 -7 -52 Q0 -52 0 -44 L0 -18 L2 -48 Q3 -56 10 -55 Q17 -54 16 -46 L14 -16 L20 -40 Q23 -47 29 -44 Q34 -41 32 -34 L24 4 L24 40 Z'
    return g(x - 38, y, 1, P(hand, fill), marks and g(0, 0, 1, marks)) + g(x + 38, y, 1, P(hand, fill, extra='transform="scale(-1 1)"'), marks and g(0, 0, 1, marks))


def tv(x, y, s=1, on=True):
    return g(x, y, s, R(-40, -30, 80, 56, INK, rx=8, sw=0), R(-32, -22, 64, 40, '#7EC8F2' if on else '#4A4F5E', rx=4, sw=0),
             P('M-14 26 L-20 40 M14 26 L20 40', None, 5), P('M-20 -46 L0 -30 L20 -46', None, 4))


def door(x, y, w=60, h=110, col=BROWN, open_=False):
    if open_:
        return R(x, y, w, h, INK, rx=4, sw=0) + P(f'M{x} {y} L{x - w * .5} {y + 10} L{x - w * .5} {y + h - 10} L{x} {y + h} Z', col) + dot(x - w * .4, y + h / 2, 4, GOLD)
    return R(x, y, w, h, col, rx=4) + dot(x + w - 12, y + h / 2, 5, GOLD)


def bubble(x, y, r=20):
    return C(x, y, r, WHITE, 4)


def notes(x, y, col=PURPLE):
    return P(f'M{x} {y} L{x} {y - 24} L{x + 16} {y - 28} L{x + 16} {y - 6}', None, 4, f'stroke="{col}"') + E(x - 5, y, 6, 5, col, 0) + E(x + 11, y - 6, 6, 5, col, 0)


def zzz(x, y):
    return P(f'M{x} {y} L{x + 12} {y} L{x} {y + 12} L{x + 12} {y + 12} M{x + 18} {y - 22} L{x + 28} {y - 22} L{x + 18} {y - 12} L{x + 28} {y - 12}', None, 4)


def motion(x, y, n=3, gap=12, ln=24):
    return P(' '.join(f'M{x} {y + i * gap} L{x - ln} {y + i * gap}' for i in range(n)), None, 4, 'opacity=".45"')


def baby(cx, cy, s=1, face_kind='smile'):
    from people import face
    return g(cx, cy, s, E(0, 20, 26, 22, PK), C(0, -12, 20, SKIN3), g(0, -12, .8, face(face_kind)), P('M-4 -32 Q0 -40 6 -34', None, 4))


def bottle(x, y, s=1, col='#7BC47F', label=True):
    return g(x, y, s, P('M-18 -30 L-18 30 L18 30 L18 -30 Q18 -38 8 -40 L8 -54 L-8 -54 L-8 -40 Q-18 -38 -18 -30 Z', col),
             R(-10, -64, 20, 12, INK, rx=3, sw=0), C(0, 0, 9, WHITE, 3) if label else '')


def pills(x, y, s=1):
    return g(x, y, s, P('M-14 -20 L-14 24 L14 24 L14 -20 Z', WHITE), R(-16, -32, 32, 12, RED, rx=3), E(-26, 32, 7, 4, GOLD, 3), E(24, 30, 7, 4, GOLD, 3))


def chair(x, y, s=1, col=TAN):
    return g(x, y, s, P('M-26 -90 L-26 0 M26 -40 L26 0 M-26 -40 L26 -40', None, 8, f'stroke="{col}"'), P('M-26 -90 L-26 0 M26 -40 L26 0'), R(-32, -46, 64, 10, col, rx=3))


def gogo_glasses(x, y):
    return C(x - 9, y, 8, None, 4) + C(x + 9, y, 8, None, 4)
