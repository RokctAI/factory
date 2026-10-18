from lib import *

# A person drawn in local units: feet at y=0, head top near y=-150,
# centred on x=0. Place with g(x, y, scale, *person(...)).


def face(kind, cx=0, cy=0):
    f = ''
    if kind == 'sleep':
        f += P(f'M{cx - 13} {cy - 2} Q{cx - 8} {cy + 3} {cx - 3} {cy - 2} M{cx + 3} {cy - 2} Q{cx + 8} {cy + 3} {cx + 13} {cy - 2}', sw=4)
        f += P(f'M{cx - 4} {cy + 12} Q{cx} {cy + 14} {cx + 4} {cy + 12}', sw=4)
        return f
    f += eyes(cx, cy - 2, 16, 4)
    if kind == 'smile':
        f += P(f'M{cx - 7} {cy + 9} Q{cx} {cy + 15} {cx + 7} {cy + 9}', sw=4)
    elif kind == 'sad':
        f += P(f'M{cx - 7} {cy + 14} Q{cx} {cy + 8} {cx + 7} {cy + 14}', sw=4)
    elif kind == 'open':
        f += E(cx, cy + 12, 5, 6, INK, 0)
    elif kind == 'shout':
        f += E(cx, cy + 12, 7, 8, INK, 0) + P(f'M{cx - 15} {cy - 10} L{cx - 4} {cy - 6} M{cx + 15} {cy - 10} L{cx + 4} {cy - 6}', sw=4)
    elif kind == 'angry':
        f += P(f'M{cx - 7} {cy + 14} Q{cx} {cy + 8} {cx + 7} {cy + 14}', sw=4) + P(f'M{cx - 15} {cy - 11} L{cx - 4} {cy - 6} M{cx + 15} {cy - 11} L{cx + 4} {cy - 6}', sw=4)
    elif kind == 'flat':
        f += P(f'M{cx - 6} {cy + 11} L{cx + 6} {cy + 11}', sw=4)
    return f


def hair(style, col=HAIR, cx=0, cy=0):
    if style == 'short':
        return P(f'M{cx - 24} {cy - 2} Q{cx - 26} {cy - 28} {cx} {cy - 28} Q{cx + 26} {cy - 28} {cx + 24} {cy - 2} Q{cx + 12} {cy - 16} {cx} {cy - 14} Q{cx - 12} {cy - 16} {cx - 24} {cy - 2} Z', col, 4)
    if style == 'bun':
        return C(cx, cy - 30, 11, col, 4) + hair('short', col, cx, cy)
    if style == 'puffs':
        return C(cx - 24, cy - 18, 11, col, 4) + C(cx + 24, cy - 18, 11, col, 4) + hair('short', col, cx, cy)
    if style == 'long':
        return P(f'M{cx - 24} {cy + 22} Q{cx - 32} {cy - 30} {cx} {cy - 28} Q{cx + 32} {cy - 30} {cx + 24} {cy + 22} L{cx + 20} {cy - 2} Q{cx} {cy - 18} {cx - 20} {cy - 2} Z', col, 4)
    if style == 'cap':
        return P(f'M{cx - 24} {cy - 8} Q{cx} {cy - 38} {cx + 24} {cy - 8} Z', col, 4) + P(f'M{cx + 10} {cy - 9} L{cx + 36} {cy - 6}', None, 5)
    if style == 'scarf':  # head wrap (doek)
        return P(f'M{cx - 26} {cy - 2} Q{cx - 28} {cy - 34} {cx} {cy - 32} Q{cx + 28} {cy - 34} {cx + 26} {cy - 2} Q{cx} {cy - 14} {cx - 26} {cy - 2} Z', col, 4) + C(cx + 20, cy - 28, 7, col, 4)
    if style == 'grey':
        return P(f'M{cx - 24} {cy - 2} Q{cx - 26} {cy - 28} {cx} {cy - 28} Q{cx + 26} {cy - 28} {cx + 24} {cy - 2} Q{cx} {cy - 16} {cx - 24} {cy - 2} Z', '#D9DCE3', 4)
    if style == 'bald':
        return P(f'M{cx - 24} {cy} Q{cx - 26} {cy - 14} {cx - 18} {cy - 16} M{cx + 24} {cy} Q{cx + 26} {cy - 14} {cx + 18} {cy - 16}', None, 5, 'stroke="#D9DCE3"')
    return ''


def person(skin=SKIN1, shirt=BLUE, pants=NIGHT, hairstyle='short', haircol=HAIR,
           la=(-34, -60), ra=(34, -60), face_kind='smile', legs='stand', skirt=False,
           back=False, hat='', glasses=False):
    out = ''
    # legs
    if legs == 'stand':
        L = ['M-10 -42 L-12 -4', 'M10 -42 L12 -4']
    elif legs == 'walk':
        L = ['M-8 -42 L-22 -4', 'M8 -42 L18 -4']
    elif legs == 'run':
        L = ['M-6 -42 Q-26 -30 -34 -12', 'M6 -42 Q14 -20 30 -8']
    elif legs == 'sit':
        L = ['M-10 -42 L-26 -42 L-26 -6', 'M10 -42 L-6 -42 L-6 -6']
    elif legs == 'kick_r':  # kicks with the leg on the viewer's right
        L = ['M-10 -42 L-12 -4', 'M10 -42 Q28 -30 42 -32']
    elif legs == 'kick_l':
        L = ['M-10 -42 Q-28 -30 -42 -32', 'M10 -42 L12 -4']
    elif legs == 'jump':
        L = ['M-10 -42 Q-24 -30 -14 -16', 'M10 -42 Q24 -30 14 -16']
    else:
        L = []
    if L:
        out += limb(' '.join(L), pants if not skirt else skin, 13)
    # shoes
    feet = {'stand': [(-13, -2), (13, -2)], 'walk': [(-24, -2), (19, -2)], 'run': [(-36, -12), (32, -6)],
            'sit': [(-30, -4), (-10, -4)], 'kick_r': [(-13, -2), (46, -32)], 'kick_l': [(-46, -32), (13, -2)],
            'jump': [(-16, -14), (16, -14)]}.get(legs, [])
    for fx, fy in feet:
        out += E(fx, fy, 10, 6, INK, 0)
    # body
    if skirt:
        out += P('M-20 -104 L20 -104 L36 -38 L-36 -38 Z', shirt)
    else:
        out += P('M-24 -104 Q0 -110 24 -104 L26 -40 L-26 -40 Z', shirt)
        out += P('M-26 -54 L26 -54 L26 -40 L-26 -40 Z', pants, 5)
    # arms: from shoulders to hands (one path for both)
    ad = ''
    for (sx, (hx, hy)) in ((-20, la), (20, ra)):
        mx = (sx + hx) / 2 + (-6 if hx < sx else 6)
        my = (-98 + hy) / 2
        ad += f'M{sx} -98 Q{mx:g} {my:g} {hx} {hy} '
    out += limb(ad.strip(), shirt, 12)
    out += C(la[0], la[1], 7, skin, 4) + C(ra[0], ra[1], 7, skin, 4)
    # head (drawn for r=24 at the origin, then scaled up)
    hd = C(0, 0, 24, skin)
    if back:
        hd += P('M-24 4 Q-26 -26 0 -26 Q26 -26 24 4 Q24 20 0 22 Q-24 20 -24 4 Z', haircol if hairstyle not in ('grey', 'bald') else '#D9DCE3', 4)
        if hairstyle == 'puffs':
            hd += C(-24, -18, 11, haircol, 4) + C(24, -18, 11, haircol, 4)
        if hairstyle == 'bun':
            hd += C(0, -30, 11, haircol, 4)
    else:
        hd += hair(hairstyle, haircol) + face(face_kind)
        if glasses:
            hd += C(-8, -2, 7, None, 3) + C(8, -2, 7, None, 3) + P('M-1 -2 L1 -2', None, 3)
    out += g(0, -128, 1.25, hd)
    out += hat
    return out


# Shared characters
def kid(**k):
    d = dict(skin=SKIN1, shirt=GOLD, pants=BLUE, hairstyle='short')
    d.update(k)
    return person(**d)


def girl(**k):
    d = dict(skin=SKIN2, shirt=ROSE, pants=PK, hairstyle='puffs', skirt=True)
    d.update(k)
    return person(**d)


def tutor(**k):
    """The tutor: one consistent grown-up, bun, purple top, glasses."""
    d = dict(skin=SKIN1, shirt=PURPLE, pants=NIGHT, hairstyle='bun', glasses=True)
    d.update(k)
    return person(**d)
