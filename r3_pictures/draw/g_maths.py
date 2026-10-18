# Maths pictures: money, sticks, beads, counters, fractions, graphs, measuring.
from mkit import *
from content import pack
from content import words
from numwords import U, words_to_int
from g_shapes import clock, shp
from font import texts

NW = dict(U)
# chocolate bars
for nm, n, k in [('bar_halves', 2, 0), ('bar_thirds', 3, 0), ('bar_quarters', 4, 0)]:
    art(nm, S(100, 160, 80), frac_rect(n, n, 24, 64, 152, 76))
for nm, k in [('bar_one_fifth', 1), ('bar_two_fifths', 2), ('bar_four_fifths', 4)]:
    art(nm, S(100, 160, 80), frac_rect(5, k, 18, 64, 164, 72, col=BLUE, light=WHITE))
art('bar_graph_fruit', chart_bars([4, 7, 3, 5], ['apple', 'banana', 'orange', 'grapes']))
art('bar_graph_pets', chart_bars([6, 4, 2], ['dog', 'cat', 'fish']))
art('bar_graph_transport', chart_bars([7, 3, 5, 2], ['child', 'bus', 'taxi', 'car']))
RB = [RED, BLUE]
art('beads_eight_five', beads([RED] * 8 + [BLUE] * 5))
art('beads_four_one', beads([RED] * 4 + [BLUE]))
art('beads_eleven', beads([GOLD] * 11))
art('beads_fifteen', beads([GREEN] * 10 + [PURPLE] * 5, r=8))
art('beads_twenty', beads(([RED] * 5 + [BLUE] * 5) * 2, r=6))
art('beads_mixed', beads([RED, GOLD, BLUE, BLUE, GREEN, RED, PURPLE, GOLD]))
art('beads_pattern', beads([RED, GOLD, BLUE] * 3))
art('beads_red_blue', beads(RB * 4))
art('beads_red_blue_blue', beads([RED, BLUE, BLUE] * 3))
art('bundles_six_tens', sticks_pic(6, 0))
art('sticks', S(100, 176, 72), *[P(f'M{30 + i * 3} {170 - i * 6} L{170 - i * 2} {120 + i * 4}', None, 10) + P(f'M{30 + i * 3} {170 - i * 6} L{170 - i * 2} {120 + i * 4}', None, 5, f'stroke="{TAN if i % 2 else BROWN}"') for i in range(8)])
art('sticks_99', sticks_pic(9, 9, maxw=184))
art('sticks_five_loose', sticks_pic(0, 5))
art('sticks_five_tens', sticks_pic(5, 0))
art('sticks_four_tens_one_crossed', sticks_pic(4, 0, cross_t=1))
art('sticks_seven_bundles', sticks_pic(7, 0))
art('sticks_three_bundles', sticks_pic(3, 0))
art('sticks_two_tens', sticks_pic(2, 0))
for sl in pack(r'sticks_([a-z]+)_tens?_([a-z]+)', lambda m: m[1] in NW and m[2] in NW):
    p = sl.split('_')
    art(sl, sticks_pic(NW[p[1]], NW[p[3]]))
for sl in pack(r'sticks_\d+_plus_\d+'):
    a, b = int(sl.split('_')[1]), int(sl.split('_')[3])
    art(sl, sticks_pic(a // 10, a % 10, y=56, hh=56), text('+', 100, 108, 22), sticks_pic(b // 10, b % 10, y=150, hh=56))
art('sticks_67_minus_23', sticks_pic(6, 7, cross_t=2, cross_o=3, maxw=184))
art('sticks_80_minus_10', sticks_pic(8, 0, cross_t=1))
# calendars
art('calendar_month', calendar(words('g_maths:calendar_month'), 2, 31))
art('calendar_15_wednesday', calendar(words('g_maths:calendar_15_wednesday'), 2, 31, {15: Y}))
art('calendar_3_to_10', calendar(words('g_maths:calendar_3_to_10'), 1, 30, {3: G, 10: PK}))
art('calendar_june', calendar(words('g_maths:calendar_june'), 1, 30, col=BLUE))
art('calendar_month_saturdays', calendar(words('g_maths:calendar_month_saturdays'), 3, 30, {d: B for d in (3, 10, 17, 24)}))
art('calendar_two_weeks', calendar(words('g_maths:calendar_two_weeks'), 0, 14, {d: Y for d in range(1, 15)}, rows=2, hh=110, y=44))
art('calendar_week_row', calendar(words('g_maths:calendar_week_row'), 0, 7, {d: G for d in range(1, 8)}, rows=1, hh=80, y=60))
art('calendar_week_party_friday', R(10, 56, 180, 90, WHITE, rx=8), *[text(d, 10 + 25.7 * (i + .5), 80, 10, sw=2) + P(f'M{10 + 25.7 * (i + 1):.0f} 64 V138', None, 3, 'opacity=".4"') for i, d in enumerate(words('g_maths:calendar_week_party_friday.days', 7))],
    thing('balloon', 10 + 25.7 * 4.5, 116, .16))
art('calendar_tomorrow', calendar(words('g_maths:calendar_tomorrow'), 2, 14, {8: Y, 9: PK}, rows=2, hh=110, y=44), arrow(78, 30, 116, 30))
art('calendar_year', R(10, 20, 180, 160, WHITE, rx=10), *[R(18 + (i % 4) * 43, 30 + (i // 4) * 49, 36, 40, TILES[i % 6], rx=4, sw=3) for i in range(12)], texts([(m, 36 + (i % 4) * 43, 55 + (i // 4) * 49) for i, m in enumerate(words('g_maths:calendar_year.months', 12))], 8, sw=2))
# money
art('coin', S(100, 172, 56), coin('r5', 100, 104, 62))
for k in ['20c', '50c', 'r1', 'r2', 'r5']:
    art('coin_' + k, S(100, 172, 56), coin(k, 100, 104, 62))
alias('r1_coin', 'coin_r1')
art('coin_r5_note_r10', S(100, 170, 80), coin('r5', 46, 104, 34), note(10, 128, 104, 100))
for sl, ks in {'coins_10_2': None, 'coins_10_5': None, 'coins_5_5': ['r5', 'r5'], 'coins_20c_three': ['20c'] * 3, 'coins_50c_50c': ['50c', '50c'], 'coins_50c_two': ['50c', '50c'],
               'coins_r1_four': ['r1'] * 4, 'coins_r2_four': ['r2'] * 4, 'coins_r2_r2': ['r2', 'r2'], 'coins_r2_r2_r1': ['r2', 'r2', 'r1'], 'coins_r5_r2': ['r5', 'r2'], 'coins_r5_r5': ['r5', 'r5'], 'coins_r5_two': ['r5', 'r5'],
               'coins_cents': ['50c', '20c', '10c']}.items():
    if ks:
        art(sl, S(100, 160, 80), coins_row(ks))
art('coins_10_2', S(100, 170, 80), note(10, 66, 104, 96), coin('r2', 152, 104, 30))
art('coins_10_5', S(100, 170, 80), note(10, 66, 104, 96), coin('r5', 152, 104, 30))
art('coins_and_note', S(100, 176, 84), coin('r1', 40, 70, 24), coin('r2', 96, 70, 26), coin('r5', 154, 70, 28), note(10, 100, 140, 110))
art('ten_rand_notes_row', *[note(10, 52 + (i % 3) * 48, 50 + (i // 3) * 48, 64) for i in range(9)])
for v in (10, 20, 50):
    art(f'note_r{v}', S(100, 160, 80), note(v, 100, 104, 160))
art('note_r20_coin_r5', S(100, 170, 80), note(20, 72, 104, 110), coin('r5', 160, 104, 26))
alias('rand_note', 'note_r10')
for v in [2, 4, 6, 8, 14, 15, 20, 22, 30, 32, 80]:
    art(f'price_r{v}', S(100, 160, 70), price_tag(f'R{v}'))
art('money_10_10_5', S(100, 172, 84), note(10, 56, 80, 84), note(10, 144, 80, 84), coin('r5', 100, 140, 26))
art('money_r10_r5_r2', S(100, 172, 84), note(10, 64, 100, 90), coin('r5', 136, 100, 22), coin('r2', 176, 100, 18))
art('money_20_halved', S(100, 172, 84), note(10, 56, 100, 76), P('M100 60 L100 140', None, 5, 'stroke-dasharray="6 8"'), note(10, 144, 100, 76))
art('money_20_four_children', note(20, 100, 50, 100), *[thing('child', 28 + i * 48, 140, .4) for i in range(4)])
art('toy_money', S(100, 170, 80), note(10, 76, 96, 100), coin('r1', 150, 120, 24), coin('r2', 128, 70, 20))
alias('toy_coin', 'coin_r1')
# counters
art('counters_one_red_two_blue', counters([RED, BLUE, BLUE], r=22))
art('counters_two_and_one', counters([RED, RED, BLUE], r=22))
art('counters_six_two', counters([RED] * 6 + [BLUE] * 2, r=14))
art('counters_six_take_four', counters([RED] * 6, cross=4, r=15))
art('counters_three_take_one', counters([RED] * 3, cross=1, r=22))
art('counters_twelve_take_two', counters([RED] * 12, cross=2, r=14, rows=2))
art('counters_sixteen_take_six', counters([RED] * 16, cross=6, r=12, rows=2))
# groups
def groups(a, b, unit=None):
    o = ''
    cols = a if a <= 3 else 2
    rows = -(-a // cols)
    cw, ch = 176 / cols, 168 / rows
    for i in range(a):
        r_, c_ = divmod(i, cols)
        cx, cy = 12 + cw * (c_ + .5), 16 + ch * (r_ + .5)
        rr = min(cw, ch) * .44
        o += C(cx, cy, rr, CREAM, 4)
        for j in range(b):
            ang = math.radians(360 * j / b - 90)
            d = 0 if b == 1 else rr * .5
            o += C(cx + d * math.cos(ang), cy + d * math.sin(ang), rr * (.3 if b <= 3 else .22), RED, 3)
    return o
for sl in pack(r'groups_([a-z]+)_of_([a-z]+)', lambda m: m[1] in NW and m[2] in NW):
    p = sl.split('_')
    art(sl, groups(NW[p[1]], NW[p[3]]))
# fractions as groups
art('half', S(100, 176, 70), frac_circle(2, 1), text('1/2', 160, 46, 18))
art('quarter', S(100, 176, 70), frac_circle(4, 1), text('1/4', 160, 46, 18))
art('half_moon', R(16, 16, 168, 168, NIGHT, rx=18), C(100, 100, 56, '#4A5683', 4), P('M100 44 A56 56 0 0 1 100 156 Z', '#F2C94C', 4))
art('half full', S(100, 182, 46), P('M60 30 L140 30 L130 176 L70 176 Z', '#EAF6FD'), P('M66 103 L134 103 L130 173 L70 173 Z', B, 0), P('M60 30 L140 30 L130 176 L70 176 Z'), P('M66 103 L134 103', None, 4))
def half_tree(side):
    t = P('M100 186 L100 150', None, 12, f'stroke="{BROWN}"') + P('M100 150 Q40 150 46 110 Q30 80 60 62 Q64 26 100 22 Z', GREEN)
    return t
art('half_tree', S(100, 186, 50), half_tree(0), P('M100 10 L100 190', None, 3, 'stroke-dasharray="8 8"'))
art('half_tree_match', S(100, 186, 50), '<g transform="translate(200 0) scale(-1 1)">' + half_tree(0) + '</g>')
art('half_tree_wrong', S(100, 186, 50), P('M100 186 L100 150', None, 12, f'stroke="{BROWN}"'), P('M100 150 L160 150 L150 60 L100 40 Z', GREEN))
# jugs
art('jug_full', S(100, 182, 60), jug(.92))
art('jug_half', S(100, 182, 60), jug(.5))
art('jug_quarter', S(100, 182, 60), jug(.25))
art('jug_500ml', S(100, 182, 60), jug(.5), text('1 l', 128, 52, 11), text(words('g_maths:jug_500ml'), 132, 112, 11))
art('jug_half_litre', S(100, 182, 60), jug(.5), text('1 l', 128, 52, 11))
cup = lambda x, y, s=.3: thing('cup', x, y, s)
art('jug_four_cups', S(100, 182, 84), g(-30, 0, 1, jug(1, cx=100, hh=110, w=70)), *[cup(150, 30 + i * 40, .2) for i in range(4)])
art('jug_six_cups', S(100, 182, 84), g(-36, 0, 1, jug(1, cx=100, hh=110, w=70)), *[cup(136 + (i % 2) * 36, 40 + (i // 2) * 46, .2) for i in range(6)])
art('ten cups', grid_of('cup', 10, maxs=.3))
art('measuring_tools', S(100, 182, 84), g(-44, 20, .7, jug(.6)), R(110, 40, 76, 18, Y, rx=3), P(''.join(f'M{118 + i * 10} 40 v{8 if i % 2 else 12}' for i in range(7)), None, 3),
    balance('', '', 0).replace('M70 182', 'M70 182') and g(96, 70, .55, balance(C(0, -14, 12, RED), R(-12, -24, 24, 24, Y, sw=4), 0)))
# pictographs
art('pictograph_fruit', pictograph([4, 2, 3], ['apple', 'banana', 'orange'], GOLD))
art('pictograph_fruit_sold', pictograph([3, 6, 2], ['apple', 'banana', 'orange'], GOLD))
art('pictograph_pets', pictograph([5, 3, 2], ['dog', 'cat', 'fish'], GOLD))
art('pictograph_key_two', pictograph([3, 2], ['netball', 'playing_soccer'], GOLD))
art('pictograph_weather', pictograph([6, 3, 2], ['sunny', 'rainy', 'cloudy'], '#FFD25A'))
art('pictograph_birthdays', pictograph([2, 4, 1], ['cake', 'balloon', 'gift'], PK))
# rulers
def ruler(start=0, y=120, x0=20, n=8, step=19):
    o = R(x0 - 8, y, step * n + 16, 44, Y, rx=4)
    for i in range(n + 1):
        o += P(f'M{x0 + i * step} {y} v14', None, 3)
    return o + texts([(str(i + start), x0 + i * step, y + 34) for i in range(n + 1)], 10, sw=2)
art('ruler_from_zero', S(100, 176, 84), ruler(0))
art('ruler_from_one', S(100, 176, 84), ruler(1))
art('ruler_pencil_8cm', S(100, 176, 84), ruler(0), R(20, 96, 140, 16, GOLD, rx=3, sw=4), P('M160 96 L176 104 L160 112 Z', CREAM, 4), R(14, 96, 10, 16, PK, rx=2, sw=4))
art('ruler_crayon_6cm', S(100, 176, 84), ruler(0), R(20, 94, 100, 18, RED, rx=3, sw=4), P('M120 94 L134 103 L120 112 Z', RED, 4))
art('ruler_clip_3cm', S(100, 176, 84), ruler(0), P('M24 92 L72 92 Q82 92 82 102 Q82 112 72 112 L30 112 Q22 112 22 104 Q22 98 30 98 L68 98', None, 5, f'stroke="{DGREY}"'))
# scales
blk = lambda n: ''.join(R(-30 + (i % 4) * 15, -15 - (i // 4) * 15, 14, 14, Y, sw=3) for i in range(n))
art('scale_brick_feather', balance(R(-26, -26, 52, 26, RED, rx=2), g(0, -8, .4, body('feather')), 1))
art('scale_apple_down_leaf_up', balance(C(0, -16, 16, RED), g(0, -10, .3, body('leaf')), 1))
art('scale_apples_seven_blocks', balance(g(0, -20, .3, body('bag_full')), blk(7), 0))
art('scale_book_five_blocks', balance(g(0, -14, .4, body('book')), blk(5), 0))
art('scale_side_down', balance(R(-20, -30, 40, 30, NIGHT, rx=3), R(-14, -16, 28, 16, Y, rx=3), 1), P('M38 150 l0 26 M30 168 l8 10 l8 -10', None, 5, f'stroke="{RED}"'))
art('scale_side_up', balance(R(-20, -30, 40, 30, NIGHT, rx=3), R(-14, -16, 28, 16, Y, rx=3), 1), P('M162 112 l0 -26 M154 94 l8 -10 l8 10', None, 5, f'stroke="{RED}"'))
art('scale_potatoes_3kg', S(100, 184, 70), R(40, 100, 120, 80, RED, rx=10), C(100, 140, 30, WHITE), P('M100 140 L118 124', None, 5), text(words('g_maths:scale_potatoes_3kg'), 100, 172, 10, sw=2),
    P('M50 100 L150 100 L140 86 L60 86 Z', GREY), *[E(70 + i * 20, 72 - (i % 2) * 8, 14, 11, '#C99A5B', 4) for i in range(4)])
# sums
def sumcard(expr):
    sz = fit(expr, 160, 40)
    return S(100, 160, 80) + R(14, 60, 172, 84, WHITE, rx=12) + text(expr, 100, 102 + sz / 2, sz)
OPS = {'plus': '+', 'minus': '-', 'times': '*', 'div': '%'}
for sl in pack(r'sum_\d+_(plus|minus|times|div)_\d+'):
    _, a, op, b = sl.split('_')
    art(sl, sumcard(f'{a} {OPS[op]} {b}'))
# tallies
art('tally_five_bundle', S(100, 160, 60), tally(5, 64, 76))
art('tally_four', S(100, 160, 60), tally(4, 76, 76))
art('tally_six', S(100, 160, 60), tally(6, 60, 76))
art('tally_netball_soccer', R(10, 30, 180, 140, WHITE, rx=10), thing('netball', 40, 70, .26), tally(6, 74, 50), thing('playing_soccer', 40, 136, .26), tally(9, 74, 114, col=INK))
art('tally_red_cars_eight', R(10, 40, 180, 120, WHITE, rx=10), thing('car', 44, 100, .3), tally(8, 86, 76))
art('tally_soccer_seven', R(10, 40, 180, 120, WHITE, rx=10), thing('ball', 44, 100, .3), tally(7, 86, 76))
art('tally_walk_twelve', R(10, 40, 180, 120, WHITE, rx=10), thing('child_running', 40, 100, .3), tally(12, 72, 76))
# ten frames and sticks of ten
art('ten_frame_seven_dots', S(100, 150, 80), ten_frame(7, 25, 70))
art('ten_frame_seven_three', S(100, 150, 80), ten_frame(7, 25, 70, n2=3))
art('ten_frame_nine_plus_seven', ten_frame(9, 25, 30, n2=1), ten_frame(6, 25, 110, col=BLUE))
art('ten_frame_ten_six', ten_frame(10, 25, 30), ten_frame(6, 25, 110, col=BLUE))
art('ten_frames_tens', *[ten_frame(10, 12 + (i % 2) * 92, 30 + (i // 2) * 76, 84) for i in range(4)])
def tenstick(n_ones, x0=None):
    o = cube_stack(10, 60, 180, 16, B)
    o += ''.join(R(96 + (i % 3) * 22, 164 - (i // 3) * 22, 18, 18, Y, sw=3) for i in range(n_ones))
    return o
for sl in pack(r'ten_stick_and_([a-z]+)', lambda m: m[1] in NW):
    art(sl, tenstick(NW[sl[14:]]))
art('ten_sticks_sixteen', tenstick(6))
art('double_ten_frame_11', ten_frame(10, 25, 30), ten_frame(1, 25, 110))
art('double_ten_frame_14', ten_frame(10, 25, 30), ten_frame(4, 25, 110))
art('double_ten_frame_15_5', ten_frame(10, 25, 30), ten_frame(5, 25, 110, col=BLUE))
