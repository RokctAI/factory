# Shapes with friendly faces, and analog / digital clocks at given times.
from kit import *
from content import pack
from content import words
from numwords import U, words_to_int
import math
import content


def sface(cx, cy, k=1):
    return eyes(cx, cy - 4 * k, 22 * k, 5 * k) + smile(cx, cy + 8 * k, 9 * k, 4 if k >= .8 else None) + E(cx - 20 * k, cy + 8 * k, 6 * k, 4 * k, '#FFB0A8', 0) + E(cx + 20 * k, cy + 8 * k, 6 * k, 4 * k, '#FFB0A8', 0)


def shp(kind, cx=100, cy=100, sz=120, col=None, face=True, dashed=False, fill=True):
    col = col or {'circle': BLUE, 'square': RED, 'triangle': GREEN, 'rectangle': GOLD, 'oval': PURPLE}[kind]
    r = sz / 2
    f = col if fill else WHITE
    ex = 'stroke-dasharray="10 10"' if dashed else ''
    if kind == 'circle':
        o = C(cx, cy, r, f, extra=ex)
    elif kind == 'square':
        o = R(cx - r, cy - r, sz, sz, f, rx=sz * .08, extra=ex)
    elif kind == 'rectangle':
        o = R(cx - r * 1.3, cy - r * .7, sz * 1.3, sz * .7, f, rx=sz * .06, extra=ex)
    elif kind == 'oval':
        o = E(cx, cy, r * 1.25, r * .8, f, extra=ex)
    else:
        o = P(f'M{cx:.0f} {cy - r:.0f} L{cx + r * 1.1:.0f} {cy + r * .8:.0f} L{cx - r * 1.1:.0f} {cy + r * .8:.0f} Z', f, extra=ex)
        cy += r * .25
    if face:
        o += sface(cx, cy, sz / 120)
    return o


for k in ['circle', 'square', 'triangle', 'rectangle', 'oval']:
    art(k, S(100, 180, 64), shp(k))
alias('circle_shape', 'circle')
alias('round', 'circle')
art('shapes_three', S(100, 176, 84), shp('circle', 44, 130, 62), shp('triangle', 100, 70, 58), shp('square', 156, 130, 58))
alias('shapes_triangle_square_circle', 'shapes_three')
art('triangle_big', S(100, 182, 70), shp('triangle', 100, 96, 140))
art('triangle_outline', S(100, 180, 64), shp('triangle', fill=False, face=False))
art('rectangle_outline', S(100, 180, 64), shp('rectangle', fill=False, face=False))
art('red_square', S(100, 180, 64), shp('square', col=RED, face=False))
art('blue_square', S(100, 180, 64), shp('square', col=BLUE, face=False))
art('four_sides', S(100, 176, 80), shp('square', 60, 100, 70, face=False), shp('rectangle', 148, 100, 56, face=False), text('4', 100, 176, 26))
art('three_sides', S(100, 176, 80), shp('triangle', 60, 96, 70, face=False), shp('triangle', 146, 100, 56, col=GOLD, face=False), text('3', 100, 176, 26))
art('straight', S(100, 176, 80), shp('square', 56, 100, 66, face=False), shp('triangle', 146, 96, 66, face=False))
art('curved', S(100, 176, 80), shp('circle', 56, 100, 70, face=False), shp('oval', 146, 100, 54, face=False))
art('wavy', P('M14 100 Q36 60 58 100 T102 100 T146 100 T190 100', None, 18), P('M14 100 Q36 60 58 100 T102 100 T146 100 T190 100', None, 8, f'stroke="{BLUE}"'))
art('zigzag', P('M14 130 L44 70 L74 130 L104 70 L134 130 L164 70 L188 118', None, 18), P('M14 130 L44 70 L74 130 L104 70 L134 130 L164 70 L188 118', None, 8, f'stroke="{RED}"'))
art('cylinder', S(100, 180, 56), P('M50 50 L50 150 Q100 174 150 150 L150 50', GOLD), E(100, 50, 50, 16, '#FFE7A8'), P('M50 150 Q100 174 150 150'))
art('cube', S(100, 180, 64), P('M40 70 L110 70 L110 170 L40 170 Z', RED), P('M40 70 L70 40 L140 40 L110 70 Z', '#F08A80'), P('M110 70 L140 40 L140 140 L110 170 Z', '#C9463B'))
art('box_ball_cylinder', S(100, 178, 84), thing('box', 40, 120, .4), thing('ball', 100, 120, .4), g(130, 70, .45, P('M50 50 L50 150 Q100 174 150 150 L150 50', GOLD), E(100, 50, 50, 16, '#FFE7A8'), P('M50 150 Q100 174 150 150')))
art('y_shape', S(100, 180, 60), P('M20 30 L100 100 L20 170 M100 100 L190 100', None, 46), P('M20 30 L100 100 L20 170 M100 100 L190 100', None, 34, f'stroke="{DGREEN}"'), P('M14 46 L76 100 L14 154 Z', GOLD, 5))
for kind, sides in (('row_mixed_shapes', ['circle', 'square', 'triangle', 'triangle', 'circle']),):
    pass

# ---- clocks
def hands_at(cx, cy, r, h, m, only=None, red=None):
    ma = math.radians(m * 6 - 90)
    ha = math.radians((h % 12) * 30 + m * .5 - 90)
    o = ''
    if only != 'long':
        col = RED if red == 'short' else INK
        o += P(f'M{cx} {cy} L{cx + r * .5 * math.cos(ha):.1f} {cy + r * .5 * math.sin(ha):.1f}', None, r * .13, f'stroke="{col}"' if col != INK else '')
    if only != 'short':
        col = RED if red == 'long' else INK
        o += P(f'M{cx} {cy} L{cx + r * .78 * math.cos(ma):.1f} {cy + r * .78 * math.sin(ma):.1f}', None, r * .08, f'stroke="{col}"' if col != INK else '')
    return o + C(cx, cy, r * .08, INK, 0)


def clockface(cx=100, cy=104, r=72, col=WHITE, rim=B, nums=True):
    o = C(cx, cy, r + 8, rim) + C(cx, cy, r, col, 4)
    ticks = ''
    for i in range(12):
        a = math.radians(i * 30 - 90)
        r1 = r * (.86 if i % 3 else .8)
        ticks += f'M{cx + r1 * math.cos(a):.1f} {cy + r1 * math.sin(a):.1f} L{cx + r * .94 * math.cos(a):.1f} {cy + r * .94 * math.sin(a):.1f} '
    o += P(ticks, None, max(2, r * .045))
    if nums:
        sz = r * .2
        for n in (12, 3, 6, 9):
            a = math.radians(n * 30 - 90)
            o += text(str(n), cx + r * .62 * math.cos(a), cy + r * .62 * math.sin(a) + sz / 2, sz, sw=max(2, r * .045))
    return o


def clock(h, m, cx=100, cy=104, r=72, **kw):
    return clockface(cx, cy, r, nums=r > 40) + hands_at(cx, cy, r, h, m, **kw)


def clock_pic(h, m, **kw):
    return S(100, 190, 56) + clock(h, m, **kw)


def parse_time(sl):
    t = sl.replace("o'clock", 'oclock').replace(' ', '_')
    if t.startswith('clock_'):
        t = t[6:]
    p = t.split('_')
    def num(w):
        return int(w) if w.isdigit() else U.get(w)
    try:
        if p[-1] == 'oclock' and len(p) == 2:
            return num(p[0]), 0
        if p[:2] == ['half', 'past']:
            return num(p[2]), 30
        if p[:2] == ['quarter', 'past']:
            return num(p[2]), 15
        if p[:2] == ['quarter', 'to']:
            return num(p[2]) - 1, 45
    except Exception:
        return None
    return None


BAD = sorted(content.SLUGS)
for sl in sorted(BAD):
    tm = parse_time(sl)
    if tm and tm[0] is not None:
        art(sl, clock_pic(*tm))
art('clock_round', S(100, 190, 56), clockface(), hands_at(100, 104, 72, 10, 10))
art('oclock', S(100, 190, 56), clock(3, 0, cy=86, r=60), card(words('g_shapes:oclock', 1), 40, 156, 120, 36, col=Y, size=16))
art('half_past', S(100, 190, 56), clock(2, 30, cy=86, r=60), card(words('g_shapes:half_past', 1), 34, 156, 132, 36, col=B, size=16))
art('quarter_past', S(100, 190, 56), clock(4, 15, cy=86, r=60), card(words('g_shapes:quarter_past', 1), 24, 156, 152, 36, col=G, size=15))
art('quarter_to', S(100, 190, 56), clock(4, 45, cy=86, r=60), card(words('g_shapes:quarter_to', 1), 30, 156, 140, 36, col=PK, size=15))
art('clock_15_minutes', S(100, 190, 56), clockface(nums=False), P('M100 104 L100 37 A67 67 0 0 1 167 104 Z', '#FFD25A', 0, 'opacity=".45"'), clockface(nums=True)[clockface(nums=False).__len__():], hands_at(100, 104, 72, 12, 15))
for nm, (a, b) in {'clocks_twelve_to_half_past': ((12, 0), (12, 30)), 'clocks_eight_to_one': ((8, 0), (1, 0)), 'clocks_three_to_five': ((3, 0), (5, 0)), 'clocks_two_to_four': ((2, 0), (4, 0))}.items():
    art(nm, S(100, 160, 84), clock(*a, cx=50, cy=100, r=36), arrow(92, 100, 112, 100), clock(*b, cx=150, cy=100, r=36))
alias('two hours', 'clocks_two_to_four')
for nm in pack(r'digital_\d+_\d\d'):
    hh, mm = nm.split('_')[1:]
    art(nm, S(100, 156, 80), R(20, 60, 160, 84, NIGHT, rx=14), R(32, 72, 136, 60, '#20304F', rx=8, sw=4), text(f'{hh}:{mm}', 100, 120, 40, col='#7CF29A', sw=7), P('M60 144 L50 156 M140 144 L150 156', None, 7))
art('hand_long', S(100, 190, 56), clockface(), hands_at(100, 104, 72, 2, 0, red='long'))
art('hand_short', S(100, 190, 56), clockface(), hands_at(100, 104, 72, 2, 0, red='short'))
for n in ('three', 'six', 'nine', 'twelve'):
    art('hand_points_' + n, S(100, 190, 56), clockface(), hands_at(100, 104, 72, 0, U[n] * 5 % 60, only='long'))
art('midnight', R(10, 10, 180, 180, NIGHT, rx=16), C(150, 46, 18, '#F2C94C', 4), C(158, 40, 15, NIGHT, 0), clock(12, 0, 92, 108, 62))
art('time', S(100, 190, 56), clock(10, 10))
for nm, hr in (('poster_time_nine', 9), ('poster_time_three', 3)):
    art(nm, S(100, 186, 64), R(30, 14, 140, 168, Y, rx=6), card(words('g_shapes:L140', 1), 42, 24, 116, 34, col=WHITE, size=17), clock(hr, 0, 100, 104, 40), text(words('g_shapes:poster_time.clock').format(hr=hr), 100, 167, 13))
