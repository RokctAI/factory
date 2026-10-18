from props import *
import objects  # noqa: F401
import animals  # noqa: F401
import nature  # noqa: F401
from nature import crescent, tree, FLOWER, flower_head

S = shadow
SQ = '#5B8DEF'
CTR = [RED, BLUE]


def grid_pts(n, cx=100, cy=100, gap=34, per_row=None):
    per_row = per_row or (n if n <= 3 else (2 if n == 4 else 3 if n <= 6 else 4 if n <= 8 else 5))
    rows = [per_row] * (n // per_row) + ([n % per_row] if n % per_row else [])
    pts = []
    for ri, cnt in enumerate(rows):
        y = cy + (ri - (len(rows) - 1) / 2) * gap
        for i in range(cnt):
            pts.append((cx + (i - (cnt - 1) / 2) * gap, y))
    return pts


PIPS = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
        5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}


def dice(n, cx=100, cy=100, size=120, fill=WHITE, pip=INK):
    h = size / 2
    out = R(cx - h, cy - h, size, size, fill, rx=size * .18)
    for px, py in PIPS[n]:
        out += C(cx + px * h * .55, cy + py * h * .55, size * .085, pip, 0)
    return out


def counters(groups, cy=100, r=13, gap=31, colors=CTR, split=36):
    """Rows of counters, one colour per group, groups side by side."""
    out = ''
    total_w = sum((n - 1) * gap for n in groups) + split * (len(groups) - 1)
    x = 100 - total_w / 2
    for gi, n in enumerate(groups):
        for i in range(n):
            out += C(x, cy, r, colors[gi % len(colors)], 4)
            x += gap
        x += split - gap
    return out


def counters2(groups, r=12, colors=CTR):
    """Two groups, each on its own small grid, left and right."""
    out = ''
    for gi, n in enumerate(groups):
        cx = 52 if gi == 0 else 148
        for x, y in grid_pts(n, cx, 100, 30, 2):
            out += C(x, y, r, colors[gi], 4)
    return out + P('M100 40 L100 160', None, 4, 'stroke-dasharray="4 10" opacity=".4"')


for n, w in [(2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six')]:
    art(f'dice_{w}', S(100, 176, 60), dice(n, 100, 100, 130))
    art(f'dots_{w}', R(30, 30, 140, 140, WHITE, rx=14), *[C(x, y, 13, RED, 0) for x, y in grid_pts(n, 100, 100, 40, 3 if n > 4 else 2)])

art('counters_five_and_three', counters2([5, 3]))
art('counters_four_and_two', counters2([4, 2]))
art('counters_four_and_four', counters2([4, 4]))
art('counters_five_and_two', counters2([5, 2]))
art('counters_six_take_two', *[C(x, y, 14, RED, 4) for x, y in grid_pts(4, 76, 100, 34, 2)], *[C(x, y, 14, BLUE, 4) for x, y in [(150, 82), (150, 118)]], P('M126 60 L176 140', None, 6, f'stroke="{RED}"'), P('M176 60 L126 140', None, 0))
art('counters_three_left', *[C(x, y, 15, RED, 4) for x, y in grid_pts(3, 100, 70, 40)], *[C(x, y, 15, GREY, 4, 'stroke-dasharray="4 6"') for x, y in grid_pts(3, 100, 130, 40)])
COIN = lambda x, y: C(x, y, 14, GOLD, 4) + C(x, y, 7, None, 3, 'stroke="#D9A21E"')  # noqa: E731
art('coins_six_and_two', R(20, 110, 110, 70, '#E8746A', rx=12), R(56, 100, 40, 10, INK, rx=4, sw=0), *[COIN(x, y) for x, y in grid_pts(6, 76, 60, 30, 3)], *[COIN(x, y) for x, y in [(160, 120), (160, 154)]], P('M140 100 L150 112', None, 0))
art('apples_three_plus_two', *[apple(x, y, 16) for x, y in grid_pts(3, 62, 104, 38, 1)], P('M110 104 L130 104 M120 94 L120 114', None, 6), *[apple(x, y, 16, GREEN) for x, y in grid_pts(2, 160, 104, 40, 1)])
art('balls_big_small_five', ball(50, 80, 24), ball(110, 80, 24), ball(46, 146, 13), ball(96, 146, 13), ball(146, 146, 13))
BAN = lambda x, y, s=.4: g(x, y, s, P('M-50 -20 Q-10 50 60 10 Q70 0 60 -10 Q0 20 -40 -36 Z', GOLD), P('M-50 -20 L-58 -32', None, 6, f'stroke="{BROWN}"'))  # noqa: E731
art('bananas_leftover_one', plate(56, 120, 40), plate(144, 120, 40), BAN(46, 112), BAN(66, 104), BAN(134, 112), BAN(154, 104), BAN(100, 166), C(100, 160, 30, None, 4, 'stroke-dasharray="6 6"'))
art('bananas_no_leftover', plate(56, 120, 40), plate(144, 120, 40), BAN(46, 112), BAN(66, 104), BAN(134, 112), BAN(154, 104))
art('no_leftover', plate(56, 110, 40), plate(144, 110, 40), apple(46, 100, 10), apple(66, 100, 10), apple(134, 100, 10), apple(154, 100, 10))
art('one_leftover', plate(56, 100, 40), plate(144, 100, 40), apple(46, 90, 10), apple(66, 90, 10), apple(134, 90, 10), apple(154, 90, 10), apple(100, 160, 12), C(100, 158, 22, None, 4, 'stroke-dasharray="6 6"'))
ORG = lambda x, y, r=13: C(x, y, r, '#FF9F2E', 4) + P(f'M{x} {y - r} L{x + 2} {y - r - 6}', None, 4, f'stroke="{GREEN}"')  # noqa: E731
art('oranges_six_shared', plate(56, 120, 42), plate(144, 120, 42), *[ORG(x, y) for x, y in [(40, 110), (60, 104), (76, 112)]], *[ORG(x, y) for x, y in [(128, 110), (148, 104), (164, 112)]])
art('oranges_two_shared', S(100, 182, 80), K(50, .62, ra=(40, -70)), GL(150, .62, la=(-40, -70)), ORG(76, 136, 12), ORG(124, 136, 12))
art('plates_two_two', plate(56, 120, 40), plate(144, 120, 40), apple(46, 108, 11), apple(68, 108, 11), apple(134, 108, 11), apple(156, 108, 11))
art('plates_three_one', plate(56, 120, 40), plate(144, 120, 40), apple(40, 110, 11), apple(60, 104, 11), apple(78, 112, 11), apple(144, 108, 11))
art('plates_three_and_four', *[plate(x, y, 22) for x, y in grid_pts(3, 54, 100, 34, 1)], *[plate(x, y, 22) for x, y in grid_pts(4, 146, 100, 36, 2)])
SPN = lambda x, y: g(x, y, .3, E(0, -40, 28, 36, '#C9CED8'), P('M0 0 L0 70', None, 18), P('M0 0 L0 70', None, 8, 'stroke="#C9CED8"'))  # noqa: E731
art('spoons_two_and_six', *[SPN(x, 92) for x in (26, 52)], *[SPN(x, y) for x, y in grid_pts(6, 140, 80, 26, 3)], P('M78 50 L78 150', None, 4, 'stroke-dasharray="4 10" opacity=".4"'))
SWT = lambda x, y, c=RED: g(x, y, .26, P('M50 104 L20 80 L24 128 Z M150 104 L180 80 L176 128 Z', c), C(100, 104, 48, c))  # noqa: E731
art('sweets_shared_three_each', plate(56, 120, 40), plate(144, 120, 40), *[SWT(x - 26, y - 27) for x, y in [(40, 112), (58, 104), (74, 114)]], *[SWT(x - 26, y - 27, GREEN) for x, y in [(128, 112), (146, 104), (162, 114)]])
PLAS = lambda x, y, used=False: g(x, y, 1, R(-22, -8, 44, 16, '#F2C6A0' if not used else GREY, rx=8, extra='stroke-dasharray="4 6"' if used else ''), R(-7, -6, 14, 12, WHITE, rx=2, sw=0))  # noqa: E731
art('plasters_none_left', S(100, 182, 80), K(50, .62, ra=(40, -70)), GL(150, .62, la=(-40, -70)), *[PLAS(x, y) for x, y in [(50, 30), (50, 52), (50, 74), (150, 30), (150, 52), (150, 74)]])
art('plasters_one_left', S(100, 182, 80), K(50, .62, ra=(40, -70)), GL(150, .62, la=(-40, -70)), *[PLAS(x, y) for x, y in [(50, 30), (50, 52), (50, 74), (150, 30), (150, 52), (150, 74)]], PLAS(100, 160))
art('bandages_four_left', *[PLAS(x, y) for x, y in grid_pts(4, 76, 100, 40, 1)], *[PLAS(x, y, True) for x, y in grid_pts(2, 150, 100, 40, 1)])
BRK = lambda x, y, c='#D9744A', dash='': R(x - 22, y - 11, 44, 22, c, rx=3, extra=dash)  # noqa: E731
art('bricks_seven_left', *[BRK(x, y) for x, y in grid_pts(7, 80, 100, 48, 3)][:7], *[BRK(x, y, GREY, 'stroke-dasharray="4 6"') for x, y in grid_pts(3, 166, 100, 40, 1)])
art('bricks_red_five', *[BRK(x, y) for x, y in grid_pts(5, 100, 80, 50, 3)], *[BRK(x, y, '#C9CED8') for x, y in [(50, 150), (100, 150), (150, 150)]][:2])
art('planks_five_left', *[R(30, y, 100, 14, '#D9A066', rx=4) for y in (40, 66, 92, 118, 144)], *[R(150, y, 30, 14, GREY, rx=4, extra='stroke-dasharray="4 6"') for y in (52, 80, 108, 136)])
art('loaves_one_left', g(56, 100, 1, P('M-34 20 Q-40 -26 0 -26 Q40 -26 34 20 Z', '#E8B060'), P('M-14 -16 L-8 6 M6 -16 L12 6', None, 4)), *[g(x, y, .5, P('M-34 20 Q-40 -26 0 -26 Q40 -26 34 20 Z', GREY, extra='stroke-dasharray="4 8"')) for x, y in [(130, 60), (160, 100), (130, 140)]])
art('seeds_seven_left', *[E(x, y, 9, 13, '#D9A066', 4) for x, y in grid_pts(7, 84, 100, 34, 3)], g(160, 110, .5, body('bird')))
NAIL = lambda x, y, c='#9AA1AE': P(f'M{x} {y - 30} L{x} {y + 26}', None, 6, f'stroke="{c}"') + R(x - 10, y - 36, 20, 8, c, rx=2, sw=0)  # noqa: E731
art('nails_eight_four_used', R(10, 150, 180, 30, '#D9A066', rx=4), *[NAIL(x, 80) for x in (30, 60, 90, 120)], *[R(x - 10, 144, 20, 8, '#9AA1AE', rx=2, sw=0) for x in (150, 170)], *[NAIL(x, 80) for x in (150, 176)][:0], *[R(x - 10, 144, 20, 8, '#9AA1AE', rx=2, sw=0) for x in (40, 80)][:0],
    *[R(x - 10, 142, 20, 8, '#9AA1AE', rx=2, sw=0) for x in (140, 160, 180)], R(110, 142, 20, 8, '#9AA1AE', rx=2, sw=0))
BKT = lambda x, y, full=True: g(x, y, .42, P('M-60 -50 Q0 -110 60 -50', None, 6), P('M-64 -50 L64 -50 L48 56 L-48 56 Z', '#C9CED8'), E(0, -50, 64, 14, '#7EC8F2' if full else '#8E98AE'))  # noqa: E731
art('buckets_three_full', *[BKT(x, 84) for x in (40, 100, 160)], *[BKT(x, 150, False) for x in (70, 130)])
art('buckets_full_empty', g(54, 110, .7, P('M-60 -50 Q0 -110 60 -50', None, 6), P('M-64 -50 L64 -50 L48 56 L-48 56 Z', '#C9CED8'), E(0, -50, 64, 14, '#7EC8F2')), g(146, 110, .7, P('M-60 -50 Q0 -110 60 -50', None, 6), P('M-64 -50 L64 -50 L48 56 L-48 56 Z', '#C9CED8'), E(0, -50, 64, 14, '#8E98AE')))
EL = body('elephant')
art('elephants_six_two', *[g(x - 18, y - 20, .19, EL) for x, y in grid_pts(6, 76, 100, 40, 3)], *[g(x - 18, y - 20, .19, EL) for x, y in grid_pts(2, 160, 100, 44, 1)], P('M126 50 L126 150', None, 4, 'stroke-dasharray="4 10" opacity=".4"'))
DK = body('duck')
art('ducks_four_and_four', R(10, 110, 180, 70, '#9AD8F5', rx=20), *[g(x - 20, y - 22, .22, DK) for x, y in grid_pts(4, 56, 112, 40, 2)], *[g(x - 20, y - 22, .22, DK) for x, y in grid_pts(4, 144, 112, 40, 2)])
art('duckling', shadow(100, 176, 50), g(0, 0, 1, body('duck').replace('#FFFFFF', '#FFE08A', 2)))
EGG = lambda x, y, r=10: E(x, y, r, r * 1.3, WHITE, 4)  # noqa: E731


def nest(eggs, cx=100, cy=120, s=1):
    inner = ''.join(EGG(x, y - 10, 11) for x, y in grid_pts(eggs, 0, -4, 24, 5)) if eggs else ''
    return g(cx, cy, s, inner, P('M-84 -10 Q-80 50 0 50 Q80 50 84 -10 Z', '#B5793E'), P('M-76 6 Q-40 20 0 12 Q40 20 76 6 M-64 28 Q-30 36 0 30 Q40 38 66 26', None, 4))


for n, w in [(0, 'empty'), (1, 'one_egg'), (2, 'two_eggs'), (3, 'three_eggs'), (5, 'five_eggs'), (6, 'six_eggs'), (10, 'ten_eggs')]:
    art(f'nest_{w}', S(100, 176, 80), nest(n))
art('two_nests_compare', g(0, 0, .5, nest(5, 100, 200)), g(100, 0, .5, nest(2, 100, 200)), S(100, 180, 90))
art('nests_six_four', g(0, 0, .5, nest(6, 100, 200)), g(100, 0, .5, nest(4, 100, 200)), S(100, 180, 90))
art('dino_eggs_ten', S(100, 180, 86), *[E(x, y, 12, 16, '#C9E8A9', 4) for x, y in grid_pts(10, 100, 100, 34, 5)], C(64, 88, 3, DGREEN, 0), C(132, 120, 3, DGREEN, 0))
BIRD = body('bird')


def tree_birds(n):
    pts = [(70, 70), (110, 60), (140, 84), (60, 104), (96, 100), (128, 116), (100, 132)][:n]
    return [tree(100, 190, 1.05)] + [g(x - 12, y - 12, .13, BIRD) for x, y in pts]


art('tree_three_birds', *tree_birds(3))
art('tree_seven_birds', *tree_birds(7))
art('birds_in_tree', *tree_birds(5))
BASKET = lambda x, n: g(x, 120, 1, *[g(px - 8, py - 8, .08, FLOWER, flower_head(100, 80, 24, c)) for (px, py), c in zip(grid_pts(n, 0, -34, 20, 3), [PK, GOLD, PU, B, RED, PK])], P('M-38 -16 L38 -16 L30 40 L-30 40 Z', TAN), P('M-34 0 L34 0 M-32 18 L32 18', None, 4))  # noqa: E731
art('baskets_same', BASKET(54, 3), BASKET(146, 3))
art('baskets_different', BASKET(54, 2), BASKET(146, 5))
POT = lambda x, n, s=1: g(x, 0, 1, *[g(px - 14, py - 14, .14, FLOWER, flower_head(100, 80, 24, c)) for (px, py), c in zip(grid_pts(n, 0, 96, 22, 4), [PK, GOLD, PU, RED, PK, GOLD, PU, RED])], P('M-34 130 L34 130 L26 180 L-26 180 Z', '#D9744A'))  # noqa: E731
art('pot_more_flowers', POT(54, 5), POT(146, 8))
SNK = lambda x, y: g(x, y, .3, P('M-60 0 Q-30 -30 0 0 T60 0', None, 26), P('M-60 0 Q-30 -30 0 0 T60 0', None, 14, f'stroke="{GREEN}"'), C(66, -4, 12, GREEN), dot(68, -8, 4))  # noqa: E731
art('grass_four_snakes', R(10, 40, 180, 140, G, rx=20), *[SNK(x, y) for x, y in [(60, 70), (130, 90), (70, 130), (140, 150)]], P('M20 180 L26 160 L32 180 M50 180 L56 164 L62 180 M150 180 L156 160 L162 180', None, 4, f'stroke="{DGREEN}"'))
art('rock_no_lizards', S(100, 176, 72), body('rock'), P('M40 60 L46 40 L52 60 M150 60 L156 44 L162 60', None, 0))
PEN = lambda x, y, ln, col=GOLD: g(x, y, 1, P(f'M0 0 L{ln} 0 L{ln + 18} 9 L{ln} 18 L0 18 Z', col), P(f'M{ln} 0 L{ln} 18', None, 4), P(f'M{ln + 12} 6 L{ln + 18} 9 L{ln + 12} 12', INK, 0), R(-10, 0, 12, 18, PK, rx=3))  # noqa: E731
art('pencil_long', S(100, 130, 80), PEN(26, 92, 128))
art('pencil_medium', S(100, 130, 60), PEN(52, 92, 78))
art('pencil_short', S(100, 130, 40), PEN(76, 92, 30))
art('pencils_short_four', *[PEN(64, y, 52, c) for y, c in zip((40, 74, 108, 142), (GOLD, RED, BLUE, GREEN))])
art('boys_tall_short_six', S(100, 182, 90), *[g(x, 182, .5, kid(shirt=c)) for x, c in zip((24, 56, 88, 120), (GOLD, RED, BLUE, GREEN))], *[g(x, 182, .34, kid(shirt=c, skin=SKIN2)) for x, c in zip((152, 180), (PU, ORANGE))])
BTN = lambda x, y, r, c=BLUE: C(x, y, r, c, 4) + dot(x - r * .3, y - r * .3, max(2, r * .15)) + dot(x + r * .3, y + r * .3, max(2, r * .15)) + dot(x - r * .3, y + r * .3, max(2, r * .15)) + dot(x + r * .3, y - r * .3, max(2, r * .15))  # noqa: E731
art('buttons_big_small_six', *[BTN(x, 70, 22) for x in (40, 100, 160)], *[BTN(x, 140, 13, RED) for x in (60, 100, 140)])
art('oval_buttons_three', P('M60 20 L140 20 L156 190 L44 190 Z', '#5BAA61'), P('M100 20 L100 190', None, 4), *[E(118, y, 10, 15, GOLD, 4) for y in (60, 110, 160)])
art('house_windows_four', S(100, 182, 84), P('M20 90 L100 30 L180 90 Z', RED), R(34, 90, 132, 90, Y), *[R(x, y, 28, 24, B, rx=3) for x, y in [(48, 102), (124, 102), (48, 142), (124, 142)]], R(88, 132, 26, 48, BROWN, rx=3))
art('flats_windows_ten', S(100, 186, 70), R(44, 14, 112, 170, '#C9B8E8', rx=6), *[R(x - 12, y - 10, 24, 20, B, rx=3) for x, y in grid_pts(10, 100, 92, 30, 2)][:10], P('M44 14 L156 14', None, 0))
art('floor_tiles_six', P('M30 60 L170 60 L190 170 L10 170 Z', '#F4E3C1'), P('M30 60 L170 60 L190 170 L10 170 Z M77 60 L70 170 M123 60 L130 170 M20 115 L180 115', None, 5))
art('roof_tiles_five', R(30, 120, 140, 60, Y), P('M10 120 L100 50 L190 120 Z', '#D9744A'), *[P(f'M{x - 18} {y} Q{x} {y + 16} {x + 18} {y}', None, 4) for x, y in [(70, 96), (100, 96), (130, 96), (86, 76), (114, 76)]])
art('street_doors_three', S(100, 186, 90), *[g(x, 0, 1, P('M-28 100 L0 76 L28 100 Z', c), R(-24, 100, 48, 80, Y), R(-9, 140, 18, 40, BROWN, rx=2)) for x, c in [(40, RED), (100, BLUE), (160, GREEN)]])
art('street_houses', S(100, 186, 90), *[g(x, 0, 1, P('M-28 100 L0 76 L28 100 Z', c), R(-24, 100, 48, 80, Y), R(-9, 140, 18, 40, BROWN, rx=2), R(-18, 110, 14, 14, B, rx=2), R(4, 110, 14, 14, B, rx=2)) for x, c in [(40, RED), (100, BLUE), (160, GREEN)]])
art('pegs_red_yellow', R(14, 60, 172, 80, '#E8D2A6', rx=10), *[C(36 + i * 32, 100, 12, RED if i % 2 == 0 else GOLD, 4) for i in range(5)])
art('pattern_copy_right', R(14, 60, 172, 80, '#E8D2A6', rx=10), *[C(36 + i * 32, 100, 12, RED if i % 2 == 0 else GOLD, 4) for i in range(5)])
art('pattern_copy_wrong', R(14, 60, 172, 80, '#E8D2A6', rx=10), *[C(36 + i * 32, 100, 12, c, 4) for i, c in enumerate([RED, RED, GOLD, GOLD, RED])])
art('peg_red', S(100, 170, 40), C(100, 96, 36, RED), R(88, 130, 24, 30, RED, rx=6))
art('peg_blue', S(100, 170, 40), C(100, 96, 36, BLUE), R(88, 130, 24, 30, BLUE, rx=6))
art('red_bead', S(100, 160, 40), C(100, 100, 40, RED), C(100, 100, 10, '#FFF8E7'))
art('blue_bead', S(100, 160, 40), C(100, 100, 40, BLUE), C(100, 100, 10, '#FFF8E7'))
art('pattern_red_blue_beads', P('M10 100 L190 100', None, 4), *[C(24 + i * 32, 100, 15, RED if i % 2 == 0 else BLUE) for i in range(5)], *[C(24 + i * 32, 100, 4, '#FFF8E7', 0) for i in range(5)], C(178, 100, 15, None, 4, 'stroke-dasharray="4 6"'))
art('red_block', S(100, 176, 60), P('M40 70 L120 50 L170 74 L90 96 Z', '#F08A7E'), P('M40 70 L90 96 L90 170 L40 146 Z', '#C9483C'), P('M90 96 L170 74 L170 148 L90 170 Z', RED))
SHAPE = {'circle': lambda c, x=100, y=100, s=1: C(x, y, 60 * s, c),
         'square': lambda c, x=100, y=100, s=1: R(x - 54 * s, y - 54 * s, 108 * s, 108 * s, c, rx=6),
         'triangle': lambda c, x=100, y=100, s=1: P(f'M{x} {y - 60 * s} L{x + 66 * s} {y + 52 * s} L{x - 66 * s} {y + 52 * s} Z', c)}
art('yellow_circle', SHAPE['circle'](GOLD))
art('yellow_triangle', SHAPE['triangle'](GOLD))
art('green_triangle', SHAPE['triangle'](GREEN))
art('orange_square', SHAPE['square']('#FF8A3D'))
art('square_big', SHAPE['square'](SQ, s=1.4))
art('square_small', SHAPE['square'](SQ, s=.6))
art('pattern_big_small_squares', SHAPE['square'](SQ, 40, 100, .5), SHAPE['square'](SQ, 96, 100, .26), SHAPE['square'](SQ, 148, 100, .5))
art('pattern_circle_square', SHAPE['circle'](RED, 30, 100, .3), SHAPE['square'](SQ, 72, 100, .32), SHAPE['circle'](RED, 116, 100, .3), SHAPE['square'](SQ, 160, 100, .32))
art('pattern_triangle_circle', SHAPE['triangle'](GREEN, 30, 100, .3), SHAPE['circle'](RED, 72, 100, .3), SHAPE['triangle'](GREEN, 116, 100, .3), SHAPE['circle'](RED, 160, 100, .3))
art('pattern_yellow_green_missing', SHAPE['triangle'](GOLD, 24, 104, .26), SHAPE['triangle'](GREEN, 62, 104, .26), SHAPE['triangle'](GOLD, 100, 104, .26), P('M122 118 L138 88 L154 118 Z', None, 4, 'stroke-dasharray="4 6"'), SHAPE['triangle'](GOLD, 176, 104, .26))
art('square_corners', SHAPE['square'](SQ, s=1.1), *[C(x, y, 9, RED, 4) for x, y in [(40, 40), (160, 40), (40, 160), (160, 160)]])
art('triangle_corners', SHAPE['triangle'](GREEN, 100, 104, 1.15), *[C(x, y, 9, RED, 4) for x, y in [(100, 35), (176, 164), (24, 164)]])
art('diamond', P('M100 20 L170 100 L100 180 L30 100 Z', '#FF8A3D'))
art('diamond_corners', P('M100 20 L170 100 L100 180 L30 100 Z', '#FF8A3D'), *[C(x, y, 9, RED, 4) for x, y in [(100, 20), (170, 100), (100, 180), (30, 100)]])
art('oval', E(100, 100, 50, 76, PURPLE))
alias('crescent', 'moon_crescent')
art('road_sign_diamond', S(100, 186, 30), P('M100 120 L100 186', None, 10), P('M100 14 L164 74 L100 134 L36 74 Z', GOLD), P('M100 30 L148 74 L100 118 L52 74 Z', None, 4))
art('cracker_square', S(100, 176, 60), R(40, 40, 120, 120, '#E8B060', rx=8), *[C(x, y, 4, '#C98A3E', 0) for x, y in grid_pts(9, 100, 100, 30, 3)])
art('flag_triangle', S(100, 186, 30), P('M60 20 L60 186', None, 8), P('M64 26 L164 62 L64 98 Z', RED))
art('wall_rectangle', R(20, 60, 160, 90, Y), P('M20 60 L180 60', None, 0))
art('step_rectangle', S(100, 170, 80), R(20, 110, 160, 50, '#C9CED8', rx=4), R(40, 80, 120, 30, '#DCE0E7', rx=4))
art('window_square', R(46, 46, 108, 108, B, rx=4), P('M100 46 L100 154 M46 100 L154 100', None, 6))
art('roof_triangle', P('M16 150 L100 50 L184 150 Z', '#D9744A'), P('M60 100 L140 100 M38 126 L162 126', None, 4))
alias('triangle_roof', 'roof_triangle')
alias('square_window', 'window_square')
art('sandwich_square', S(100, 176, 70), R(36, 50, 128, 116, '#F2D6A0', rx=10), R(46, 60, 108, 96, '#FCECCB', rx=6, sw=0), P('M40 150 Q70 140 100 150 Q130 160 160 148', None, 6, f'stroke="{GREEN}"'))
art('sandwich_triangle', S(100, 176, 70), P('M30 160 L170 160 L100 40 Z', '#F2D6A0'), P('M50 150 L150 150 L100 64 Z', '#FCECCB', 0), P('M40 156 Q70 146 100 156 Q130 166 160 154', None, 6, f'stroke="{GREEN}"'))
art('sandwich_heart', S(100, 176, 70), P('M100 70 Q100 36 136 36 Q172 36 168 76 Q164 118 100 166 Q36 118 32 76 Q28 36 64 36 Q100 36 100 70 Z', '#F2D6A0'), P('M100 84 Q100 54 132 54 Q156 56 152 80 Q148 110 100 148 Q52 110 48 80 Q44 56 68 54 Q100 54 100 84 Z', '#FCECCB', 0))
art('orange_slice', S(100, 170, 60), C(100, 100, 66, '#FF9F2E'), C(100, 100, 54, '#FFD08A', 0), P('M100 46 L100 154 M46 100 L154 100 M62 62 L138 138 M138 62 L62 138', None, 4, 'stroke="#FFFFFF"'))
art('face_cloth_square', S(100, 176, 60), R(40, 40, 120, 120, '#4DC3C3', rx=6), P('M40 140 L160 140', None, 6, f'stroke="{WHITE}"'))
art('tube_long', S(100, 130, 86), R(14, 82, 172, 36, '#9AD8F5', rx=18), E(168, 100, 8, 18, WHITE))
art('tube_short', S(100, 130, 40), R(60, 82, 80, 36, '#9AD8F5', rx=18), E(122, 100, 8, 18, WHITE))
art('tubes_ordered', R(20, 40, 160, 26, '#9AD8F5', rx=13), R(20, 87, 110, 26, '#9AD8F5', rx=13), R(20, 134, 60, 26, '#9AD8F5', rx=13))
art('tubes_mixed', R(20, 40, 110, 26, '#9AD8F5', rx=13), R(20, 87, 60, 26, '#9AD8F5', rx=13), R(20, 134, 160, 26, '#9AD8F5', rx=13))
art('tubes_two_rows', R(16, 60, 80, 26, '#9AD8F5', rx=13), R(104, 60, 80, 26, '#9AD8F5', rx=13), R(16, 114, 80, 26, '#9AD8F5', rx=13), R(104, 114, 80, 26, '#9AD8F5', rx=13))
CAT_SEG = lambda n, s=1: [C(40 + i * 26, 110 + (i % 2) * 6, 16, GREEN) for i in range(n)][::-1]  # noqa: E731


def caterpillar(n, x0=30):
    segs = ''.join(C(x0 + 20 + i * 24, 110 + (i % 2) * 5, 15, GREEN if i % 2 == 0 else '#9AD36B') for i in range(n, 0, -1))
    return segs + C(x0, 104, 19, GOLD) + eyes(x0, 100, 12, 3) + smile(x0, 110, 4, 3) + P(f'M{x0 - 6} 86 L{x0 - 10} 74 M{x0 + 6} 86 L{x0 + 10} 74', None, 4)


art('caterpillar_long', S(100, 136, 86), caterpillar(6, 24))
art('caterpillar_medium', S(100, 136, 60), caterpillar(4, 46))
art('caterpillar_short', S(100, 136, 40), caterpillar(2, 70))
art('caterpillars_three', g(0, -50, .9, caterpillar(6, 24)), g(0, 0, .9, caterpillar(4, 24)), g(0, 50, .9, caterpillar(2, 24)))
WORM = lambda x1, x2, y: P(f'M{x1} {y} Q{(x1 + x2) / 2} {y - 30} {x2} {y}', None, 24) + P(f'M{x1} {y} Q{(x1 + x2) / 2} {y - 30} {x2} {y}', None, 12, f'stroke="{PK}"') + C(x2 + 4, y - 4, 14, PK) + dot(x2 + 8, y - 8, 3)  # noqa: E731
art('worm_long', S(100, 140, 80), WORM(20, 160, 120))
art('worm_short', S(100, 140, 40), WORM(70, 120, 120))
art('snake_and_worm', g(0, -40, .9, P('M20 100 Q50 70 80 100 T140 100 T180 96', None, 24), P('M20 100 Q50 70 80 100 T140 100 T180 96', None, 12, f'stroke="{GREEN}"'), C(182, 92, 14, GREEN), dot(186, 88, 4)), WORM(80, 120, 160))
TIN = lambda x, w, h, base=170: R(x - w / 2, base - h, w, h, '#C9CED8', rx=6) + E(x, base - h, w / 2, w / 7, '#E2E5EB') + R(x - w / 2, base - h * .65, w, h * .35, RED, sw=0) + R(x - w / 2, base - h, w, h, None, rx=6)  # noqa: E731
art('tin_big', S(100, 176, 66), TIN(100, 110, 140))
art('tin_medium', S(100, 176, 50), TIN(100, 80, 100))
art('tin_small', S(100, 176, 34), TIN(100, 52, 64))
art('tins_three_sizes', S(100, 176, 90), TIN(44, 64, 110), TIN(112, 50, 80), TIN(164, 36, 52))
art('tin_can', S(100, 176, 56), TIN(100, 90, 120))
art('tin_can_rolling', P('M10 160 L190 120', None, 6), g(100, 116, 1, R(-50, -28, 100, 56, '#C9CED8', rx=6), E(50, 0, 12, 28, '#E2E5EB'), R(-50, -10, 100, 20, RED, sw=0), R(-50, -28, 100, 56, None, rx=6), rot=-13), P('M30 100 Q24 86 34 76', None, 5, f'stroke="{BLUE}"'))
art('big_ball', S(100, 182, 74), C(100, 104, 74, RED), P('M50 60 Q60 46 76 44', None, 8, 'stroke="#FFFFFF" opacity=".6"'))
art('small_ball', S(100, 172, 30), C(100, 146, 24, BLUE), P('M86 136 Q90 130 96 128', None, 5, 'stroke="#FFFFFF" opacity=".6"'))
art('red_ball', S(100, 178, 50), C(100, 120, 52, RED), P('M70 96 Q76 84 88 82', None, 7, 'stroke="#FFFFFF" opacity=".6"'))
BAG = lambda fill_h: (P('M60 70 Q60 40 100 40 Q140 40 140 70', None, 8) + R(40, 66, 120, 112, '#E8D2A6', rx=14) +
                      (R(44, 178 - fill_h, 112, fill_h - 4, '#B5793E', rx=10, sw=0) if fill_h else '') + R(40, 66, 120, 112, None, rx=14))  # noqa: E731
art('bag_empty', S(100, 182, 64), BAG(0))
art('bag_half', S(100, 182, 64), BAG(56))
art('bag_full', S(100, 182, 64), BAG(108))
art('ball_and_box', S(100, 182, 84), P('M10 170 L190 120', None, 6), ball(60, 136, 22), g(146, 116, 1, R(-24, -24, 48, 48, '#D9A066', rx=3), rot=-15))
art('roll', P('M10 100 L190 170', None, 6), g(116, 110, 1, C(0, 0, 26, RED)), P('M76 80 A40 40 0 0 1 140 64', None, 5, f'stroke="{BLUE}"'), P('M140 64 L126 60 M140 64 L136 78', None, 5, f'stroke="{BLUE}"'))
art('slide', P('M10 100 L190 170', None, 6), g(116, 116, 1, R(-26, -46, 52, 46, '#D9A066', rx=3), rot=21), motion(70, 62, 3, 10, 30))
art('heavy', S(100, 182, 74), P('M70 70 Q70 30 100 30 Q130 30 130 70', None, 14), P('M40 70 L160 70 L176 176 L24 176 Z', '#4A4F5E'), P('M70 110 L130 110', None, 0), P('M60 40 L44 26 M140 40 L156 26', None, 4, 'opacity=".5"'))
alias('light', 'balloon')
art('elephant_and_mouse', g(-14, 6, .75, body('elephant')), g(126, 120, .3, body('mouse')), S(100, 184, 86))
art('rock_and_pillow', g(-6, 30, .5, body('rock')), g(94, 30, .5, body('pillow')), S(100, 140, 86))
art('cow_and_calf', S(100, 184, 90), g(-20, 4, .7, SAMPLES['cow'].split('/>', 1)[1]), g(100, 70, .55, body('calf')))
art('hen_and_chick', S(100, 184, 90), g(-10, 20, .7, body('chicken')), g(120, 100, .4, body('chick')))
art('mothers_babies', g(0, 0, .5, body('chicken')), g(60, 50, .25, body('chick')), g(100, 0, .5, SAMPLES['cow'].split('/>', 1)[1]), g(150, 56, .25, body('calf')), g(10, 100, .5, SAMPLES['dog'].split('/>', 1)[1]), g(90, 120, .35, body('puppy')))

# ---- second pass: bigger, countable --------------------------------------------
art('apples_three_plus_two', *[apple(x, y, 20) for x, y in grid_pts(3, 56, 100, 46, 1)], P('M100 100 L124 100 M112 88 L112 112', None, 7), *[apple(x, y, 20, GREEN) for x, y in grid_pts(2, 158, 100, 50, 1)])
PB = lambda x, y, r, c: C(x, y, r, c) + P(f'M{x - r * .55:.1f} {y - r * .2:.1f} Q{x - r * .45:.1f} {y - r * .55:.1f} {x - r * .1:.1f} {y - r * .6:.1f}', None, 5, 'stroke="#FFFFFF" opacity=".6"')  # noqa: E731
art('balls_big_small_five', PB(56, 74, 30, RED), PB(136, 74, 30, BLUE), PB(44, 148, 18, GOLD), PB(100, 148, 18, GREEN), PB(156, 148, 18, PK))
BAN = lambda x, y, s=.62: g(x, y, s, P('M-50 -20 Q-10 50 60 10 Q70 0 60 -10 Q0 20 -40 -36 Z', GOLD), P('M-50 -20 L-58 -32', None, 6, f'stroke="{BROWN}"'))  # noqa: E731
art('bananas_leftover_one', plate(52, 96, 44), plate(148, 96, 44), BAN(44, 90), BAN(62, 76), BAN(140, 90), BAN(158, 76), BAN(100, 156))
art('bananas_no_leftover', plate(52, 110, 44), plate(148, 110, 44), BAN(44, 104), BAN(62, 90), BAN(140, 104), BAN(158, 90))
art('no_leftover', plate(52, 110, 44), plate(148, 110, 44), apple(40, 98, 14), apple(66, 98, 14), apple(136, 98, 14), apple(162, 98, 14))
art('one_leftover', plate(52, 90, 44), plate(148, 90, 44), apple(40, 78, 14), apple(66, 78, 14), apple(136, 78, 14), apple(162, 78, 14), apple(100, 156, 16))
art('plates_two_two', plate(52, 110, 44), plate(148, 110, 44), apple(38, 98, 14), apple(66, 98, 14), apple(134, 98, 14), apple(162, 98, 14))
art('plates_three_one', plate(52, 110, 44), plate(148, 110, 44), apple(32, 100, 13), apple(52, 92, 13), apple(72, 100, 13), apple(148, 98, 14))
art('oranges_six_shared', plate(52, 112, 46), plate(148, 112, 46), *[ORG(x, y, 15) for x, y in [(32, 102), (52, 92), (72, 102)]], *[ORG(x, y, 15) for x, y in [(128, 102), (148, 92), (168, 102)]])
art('plates_three_and_four', *[E(x, y, 22, 10, c, 4) for (x, y), c in zip(grid_pts(3, 44, 100, 40, 1), [B, B, B])], *[E(x, y, 22, 10, PK, 4) for x, y in grid_pts(4, 140, 100, 40, 2)],
    P('M88 50 L88 150', None, 4, 'stroke-dasharray="4 10" opacity=".4"'))
SPN = lambda x, y: g(x, y, .42, E(0, -40, 26, 34, '#C9CED8'), P('M0 0 L0 66', None, 16), P('M0 0 L0 66', None, 7, 'stroke="#C9CED8"'))  # noqa: E731
art('spoons_two_and_six', *[SPN(x, 96) for x in (22, 52)], *[SPN(x, y) for x, y in grid_pts(6, 140, 78, 30, 3)], P('M76 40 L76 160', None, 4, 'stroke-dasharray="4 10" opacity=".4"'))
SWT = lambda x, y, c=RED: g(x, y, .34, P('M50 104 L20 80 L24 128 Z M150 104 L180 80 L176 128 Z', c), C(100, 104, 48, c))  # noqa: E731
art('sweets_shared_three_each', plate(52, 112, 46), plate(148, 112, 46), *[SWT(x - 34, y - 35) for x, y in [(30, 104), (52, 92), (74, 104)]], *[SWT(x - 34, y - 35, GREEN) for x, y in [(126, 104), (148, 92), (170, 104)]])
PLAS = lambda x, y, used=False: g(x, y, 1, R(-26, -10, 52, 20, '#F2C6A0' if not used else GREY, rx=10, extra='stroke-dasharray="4 6"' if used else ''), R(-8, -7, 16, 14, WHITE, rx=2, sw=0))  # noqa: E731
FACE = lambda x, y, sk=SKIN1, hs='short': g(x, y, .55, C(0, 0, 24, sk), hair(hs), face('smile'))  # noqa: E731
art('plasters_none_left', R(14, 20, 80, 150, B, rx=14), R(106, 20, 80, 150, PK, rx=14), FACE(54, 46), FACE(146, 46, SKIN2, 'puffs'), *[PLAS(x, y) for x in (54, 146) for y in (88, 116, 144)])
art('plasters_one_left', R(14, 10, 80, 140, B, rx=14), R(106, 10, 80, 140, PK, rx=14), FACE(54, 36), FACE(146, 36, SKIN2, 'puffs'), *[PLAS(x, y) for x in (54, 146) for y in (76, 102, 128)], PLAS(100, 176))
art('bandages_four_left', *[PLAS(x, y) for x, y in grid_pts(4, 64, 100, 34, 1)], *[PLAS(x, y, True) for x, y in grid_pts(2, 150, 100, 34, 1)])
art('seeds_seven_left', *[E(x, y, 10, 14, '#D9A066', 4) for x, y in grid_pts(7, 70, 100, 36, 3)], g(120, 96, .4, body('bird')))
NAIL = lambda x, y: P(f'M{x} {y - 30} L{x} {y + 26}', None, 7, 'stroke="#9AA1AE"') + R(x - 12, y - 38, 24, 10, '#9AA1AE', rx=3)  # noqa: E731
art('nails_eight_four_used', *[NAIL(x, 70) for x in (34, 78, 122, 166)], R(10, 136, 180, 40, '#D9A066', rx=6), *[R(x - 12, 128, 24, 10, '#9AA1AE', rx=3) for x in (34, 78, 122, 166)])


def nest(eggs, cx=100, cy=120, s=1):
    back = P('M-86 -6 Q-80 -24 0 -24 Q80 -24 86 -6', '#8A5A2B')
    if eggs <= 5:
        pts = grid_pts(eggs, 0, -16, 30, 5)
    else:
        pts = grid_pts(eggs, 0, -30 if eggs > 6 else -24, 30 if eggs > 6 else 28, 5 if eggs > 6 else 3)
    inner = ''.join(E(x, y, 12 if eggs > 6 else 13, 16 if eggs > 6 else 17, WHITE, 4) for x, y in pts)
    front = P('M-88 -6 Q-84 48 0 48 Q84 48 88 -6 Q44 6 0 6 Q-44 6 -88 -6 Z', '#B5793E') + P('M-74 14 Q-40 26 0 20 Q40 26 74 14', None, 4)
    return g(cx, cy, s, back, inner, front)


for n, w in [(0, 'empty'), (1, 'one_egg'), (2, 'two_eggs'), (3, 'three_eggs'), (5, 'five_eggs'), (6, 'six_eggs'), (10, 'ten_eggs')]:
    art(f'nest_{w}', S(100, 176, 84), nest(n, 100, 124))
art('two_nests_compare', nest(5, 100, 66, .9), nest(2, 100, 156, .9))
art('nests_six_four', nest(6, 100, 66, .9), nest(4, 100, 156, .9))
SBIRD = lambda x, y, c=BLUE: g(x, y, 1, E(0, 0, 14, 11, c, 4), P('M-12 -2 L-22 2 L-12 6 Z', GOLD, 3), dot(-6, -3, 2.5), P('M10 -4 L20 -10 L18 4 Z', c, 3))  # noqa: E731


def tree_birds(n):
    pts = [(70, 64), (112, 52), (146, 80), (56, 100), (96, 92), (132, 114), (90, 124)][:n]
    cols = [BLUE, RED, GOLD, BLUE, RED, GOLD, BLUE]
    return [tree(100, 190, 1.05)] + [SBIRD(x, y, c) for (x, y), c in zip(pts, cols)]


art('tree_three_birds', *tree_birds(3))
art('tree_seven_birds', *tree_birds(7))
art('birds_in_tree', *tree_birds(5))
FL = lambda x, y, c: P(f'M{x} {y} L{x} {y + 30}', None, 5, f'stroke="{DGREEN}"') + C(x, y, 11, c, 4) + C(x, y, 4, GOLD, 0)  # noqa: E731
BASKET = lambda x, n: g(x, 0, 1, *[FL(px, py, c) for (px, py), c in zip(grid_pts(n, 0, 92, 26, 3), [PK, GOLD, PU, B, RED, PK])], P('M-44 110 L44 110 L36 172 L-36 172 Z', TAN), P('M-40 130 L40 130 M-38 150 L38 150', None, 4))  # noqa: E731
art('baskets_same', BASKET(52, 3), BASKET(148, 3))
art('baskets_different', BASKET(52, 2), BASKET(148, 5))
POT = lambda x, n: g(x, 0, 1, *[FL(px, py, c) for (px, py), c in zip(grid_pts(n, 0, 90, 24, 3 if n < 7 else 3), [PK, GOLD, PU, RED, PK, GOLD, PU, RED])], P('M-40 140 L40 140 L30 184 L-30 184 Z', '#D9744A'))  # noqa: E731
art('pot_more_flowers', POT(52, 5), POT(148, 8))


def caterpillar(n, x0=30, y=110):
    segs = ''.join(C(x0 + 20 + i * 22, y + (i % 2) * 5, 15, GREEN if i % 2 == 0 else '#9AD36B') for i in range(n, 0, -1))
    return segs + C(x0, y - 6, 19, GOLD) + eyes(x0, y - 10, 12, 3) + smile(x0, y, 4, 3) + P(f'M{x0 - 6} {y - 24} L{x0 - 10} {y - 36} M{x0 + 6} {y - 24} L{x0 + 10} {y - 36}', None, 4)


art('caterpillar_long', S(100, 136, 86), caterpillar(6, 32))
art('caterpillar_medium', S(100, 136, 60), caterpillar(4, 54))
art('caterpillar_short', S(100, 136, 40), caterpillar(2, 76))
art('caterpillars_three', caterpillar(6, 30, 54), caterpillar(4, 30, 108), caterpillar(2, 30, 162))
art('oval_buttons_three', S(100, 186, 60), g(0, 0, 1, body('warm_coat')), *[E(112, y, 9, 14, GOLD, 4) for y in (92, 124, 156)])
art('rock_and_pillow', g(-10, 16, .58, body('rock')), g(86, 22, .56, body('pillow')), S(100, 150, 90))
art('elephants_six_two', *[g(x - 22, y - 24, .23, EL) for x, y in grid_pts(6, 66, 100, 48, 2)], *[g(x - 22, y - 24, .23, EL) for x, y in grid_pts(2, 156, 100, 52, 1)], P('M112 40 L112 160', None, 4, 'stroke-dasharray="4 10" opacity=".4"'))
art('ducks_four_and_four', R(10, 100, 180, 86, '#9AD8F5', rx=20), *[g(x - 26, y - 28, .27, DK) for x, y in grid_pts(4, 54, 128, 46, 2)], *[g(x - 26, y - 28, .27, DK) for x, y in grid_pts(4, 146, 128, 46, 2)])
art('cow_and_calf', S(100, 184, 90), g(-24, 2, .72, SAMPLES['cow'].split('/>', 1)[1]), g(92, 52, .62, body('calf')))

# ---- compact units for big counts (keeps files small) -----------------------------
def mini_kid(x, base, h, shirt, skin=SKIN1):
    s = h / 100
    return g(x, base, s, limb('M-8 -30 L-9 0 M8 -30 L9 0', BLUE, 10), P('M-18 -66 Q0 -70 18 -66 L20 -28 L-20 -28 Z', shirt),
             C(0, -82, 18, skin), P('M-18 -84 Q-18 -102 0 -102 Q18 -102 18 -84 Q8 -94 0 -92 Q-8 -94 -18 -84 Z', HAIR, 4), dot(-6, -82, 3), dot(6, -82, 3))


art('boys_tall_short_six', S(100, 184, 92), *[mini_kid(x, 182, 150, c) for x, c in zip((22, 58, 94, 130), (GOLD, RED, BLUE, GREEN))], *[mini_kid(x, 182, 92, c, SKIN2) for x, c in zip((158, 184), (PU, ORANGE))])
MEL = (P('M-30 10 L-30 30 M-14 12 L-14 30 M14 12 L14 30 M28 10 L28 30', None, 9) + E(0, 0, 36, 24, '#B9BFCC') + C(-34, -12, 18, '#B9BFCC') +
       P('M-26 -22 Q-8 -30 -12 -6 Q-20 2 -28 -6', '#B9BFCC', 4) + P('M-48 -6 Q-56 14 -48 26', None, 7) + dot(-38, -16, 3))
art('elephants_six_two', *[g(x, y, .85, MEL) for x, y in grid_pts(6, 66, 100, 52, 2)], *[g(x, y, .85, MEL) for x, y in grid_pts(2, 158, 100, 56, 1)], P('M114 40 L114 160', None, 4, 'stroke-dasharray="4 10" opacity=".4"'))
MDK = P('M-24 0 Q-24 20 0 20 Q24 20 28 -2 Q14 4 6 -4 Q2 -16 -10 -16 Q-22 -16 -24 0 Z', WHITE) + C(-14, -20, 11, WHITE) + P('M-24 -20 L-34 -16 L-24 -13 Z', '#FF9F43', 3) + dot(-16, -22, 2.5)
art('ducks_four_and_four', R(10, 96, 180, 90, '#9AD8F5', rx=20), *[g(x, y, 1, MDK) for x, y in grid_pts(4, 54, 136, 50, 2)], *[g(x, y, 1, MDK) for x, y in grid_pts(4, 146, 136, 50, 2)])
art('mothers_babies', S(100, 184, 92), g(-12, 14, .55, body('chicken')), g(78, 100, .3, body('chick')), g(96, -4, .45, SAMPLES['cow'].split('/>', 1)[1]), g(140, 100, .35, body('calf')))
