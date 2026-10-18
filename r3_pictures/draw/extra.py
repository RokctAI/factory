from props import *
from nature import sun, cloud, tree, panel, ground
from maths import mini_kid
import roles
import objects  # noqa: F401
import animals  # noqa: F401
import nature  # noqa: F401

S = shadow

# ---- coverage pass: pictures the Grade R packs still showed as words ----------
alias('fire_pot', 'cooking_pot')
alias('spring_scene', 'spring_flowers')
alias('morning', 'morning_sunrise')
alias('spider_small_eight_legs', 'garden_spider')
alias('round_clock', 'clock')

art('gate', S(100, 184, 92), P('M10 96 L40 96 M10 140 L40 140 M160 96 L190 96 M160 140 L190 140', None, 8, f'stroke="{BROWN}"'),
    *[R(x, 70, 16, 112, TAN, rx=3) for x in (54, 76, 98, 120)], P('M50 84 L150 84 M50 156 L150 156 M54 152 L138 88', None, 9, f'stroke="{BROWN}"'),
    R(30, 50, 20, 132, BROWN, rx=4), R(150, 50, 20, 132, BROWN, rx=4), C(140, 120, 5, INK, 0))
art('bird_singing', g(-14, 24, .78, body('bird')), notes(140, 70), notes(168, 112, BLUE), P('M128 96 Q140 92 146 100', None, 4, 'opacity=".4"'))
art('fizzy_drink', S(100, 184, 50), R(62, 64, 76, 116, RED, rx=12), E(100, 64, 38, 10, '#C9CED8'), P('M62 104 Q100 92 138 104 L138 130 Q100 118 62 130 Z', WHITE, 0),
    P('M112 64 L126 20', None, 8), P('M112 64 L126 20', None, 3, f'stroke="{GOLD}"'), C(80, 40, 6, WHITE, 3), C(96, 22, 5, WHITE, 3), C(148, 44, 6, WHITE, 3), C(70, 16, 4, WHITE, 3))

# Fruit at the tap, dropped, or hidden behind the back.
APL = lambda x, y, r=13: apple(x, y, r)  # noqa: E731
art('child_washing_fruit', sink(132, 128, True, True), K(62, .8, ra=(66, -84)), APL(122, 112), C(106, 98, 4, SKY, 0), C(140, 100, 4, SKY, 0))
art('child_dropping_fruit', S(90, 182, 70), K(80, .85, ra=(40, -76), face_kind='open'), APL(134, 160, 16), P('M134 112 L134 132 M148 116 L148 134 M120 116 L120 134', None, 4, 'opacity=".45"'))
art('child_hiding_fruit', S(100, 182, 60), APL(124, 128, 14), K(100, .85, ra=(22, -60), la=(-4, -112)), P('M150 60 Q160 50 170 60', None, 4, 'opacity=".4"'))

art('street_shapes', R(10, 150, 180, 34, '#B9BFCC', rx=8), P('M24 167 L48 167 M86 167 L110 167 M148 167 L172 167', None, 4, f'stroke="{WHITE}"'),
    P('M14 70 L46 40 L78 70 Z', RED), R(20, 70, 52, 80, Y), R(32, 86, 28, 28, B),
    P('M96 150 L96 70', None, 6, f'stroke="{DGREY}"'), P('M87 36 L105 36 L118 49 L118 67 L105 80 L87 80 L74 67 L74 49 Z', RED), P('M84 58 L108 58', None, 5, f'stroke="{WHITE}"'),
    P('M124 140 L124 116 L136 100 L180 100 L190 116 L190 140 Z', GOLD), R(140, 106, 16, 12, B, rx=2), R(162, 106, 16, 12, B, rx=2), C(140, 142, 11, INK, 0), C(176, 142, 11, INK, 0), C(140, 142, 4, GREY, 0), C(176, 142, 4, GREY, 0))

art('floor', R(10, 14, 180, 70, '#FFF3D6', rx=12), R(10, 74, 180, 10, WHITE), P('M10 84 L190 84 L196 186 L4 186 Z', TAN),
    P('M54 84 L40 186 M100 84 L100 186 M146 84 L160 186 M8 120 L192 120 M6 154 L194 154', None, 4, f'stroke="{BROWN}" opacity=".7"'))
art('floor_half_covered', R(16, 36, 168, 128, CREAM, rx=6), *[R(20 + c * 40, 40 + r * 40, 40, 40, '#9AD8F5') for c in range(2) for r in range(3)],
    *[R(100 + c * 40, 40 + r * 40, 40, 40, None, extra='stroke-dasharray="6 9" opacity=".35"') for c in range(2) for r in range(3)])

# A class listening: three children at desks, one hand up, board behind.
art('class_listening', R(40, 12, 120, 44, DGREEN, rx=4), P('M56 28 L104 28 M56 42 L84 42', None, 4, f'stroke="{WHITE}"'),
    mini_kid(46, 160, 100, GOLD), mini_kid(100, 160, 100, RED, SKIN2), limb('M118 94 L130 46', RED, 10), C(130, 44, 7, SKIN2, 4), mini_kid(154, 160, 100, BLUE),
    *[R(x - 26, 140, 52, 12, TAN, rx=3) + P(f'M{x - 20} 152 L{x - 20} 184 M{x + 20} 152 L{x + 20} 184', None, 5) for x in (46, 100, 154)])

FLAME = P('M-30 0 Q-40 -40 -10 -70 Q-12 -40 6 -36 Q4 -66 30 -84 Q24 -50 40 -30 Q48 -8 30 0 Z', '#FF8A3D') + P('M-12 0 Q-18 -24 0 -40 Q4 -20 16 -16 Q22 -4 12 0 Z', GOLD, 4)
art('fire_burning_house', S(100, 186, 80), P('M20 100 L100 40 L180 100 Z', BROWN), R(34, 100, 132, 82, Y), R(88, 130, 26, 52, BROWN, rx=3), R(46, 116, 28, 26, '#FF8A3D', rx=3), R(128, 116, 28, 26, B, rx=3),
    g(60, 120, .6, FLAME), g(120, 70, 1, FLAME), cloud(70, 26, .35, '#B9BFCC'), cloud(150, 18, .3, '#B9BFCC'))
HAND = 'M-22 40 L-22 -6 L-30 -30 Q-32 -38 -24 -38 L-14 -16 L-14 -44 Q-14 -52 -7 -52 Q0 -52 0 -44 L0 -18 L2 -48 Q3 -56 10 -55 Q17 -54 16 -46 L14 -16 L20 -40 Q23 -47 29 -44 Q34 -41 32 -34 L24 4 L24 40 Z'
art('burnt_hand', g(84, 108, 1.7, P(HAND, SKIN3), E(2, 10, 12, 10, '#FF7A6B', 0)), P('M150 40 L166 30 M154 62 L174 60 M40 46 L24 34', None, 5, f'stroke="{RED}"'), g(160, 178, .5, FLAME))

art('afternoon', panel('#CDEBFF'), sun(146, 60, 22, face=False), ground(G, 150), P('M74 160 L20 172', None, 12, 'stroke="#1F2A44" opacity=".2"'), g(84, 158, .5, tree(0, 0)))

# Helpers: head and shoulders with their work hats.
def helper(x, s, skin, shirt, hat, hs='short'):
    return g(x, 186, s, P('M-46 0 Q-46 -92 0 -96 Q46 -92 46 0 Z', shirt), g(0, -128, 1.25, C(0, 0, 24, skin), hair(hs), face('smile')), hat)


art('community_helpers', helper(38, .72, SKIN2, B, roles.NURSE_CAP, 'bun'), helper(100, .72, SKIN1, NIGHT, roles.POLICE_CAP), helper(162, .72, SKIN3, RED, roles.FIRE_HAT))
art('police_nurse', S(100, 184, 90), AD(56, .82, shirt=NIGHT, pants=NIGHT, skin=SKIN2, hat=roles.POLICE_CAP), AD(146, .82, skin=SKIN2, shirt=B, pants=B, hairstyle='bun', skirt=True, hat=roles.NURSE_CAP))

BIN = R(132, 110, 46, 72, GREEN, rx=5) + R(126, 100, 58, 12, DGREEN, rx=4)
art('pick_up_litter', S(110, 184, 84), BIN, K(76, .85, ra=(58, -112)), P('M118 80 L132 76 L134 90 L120 94 Z', WHITE, 4))
art('drop_litter', S(100, 184, 84), K(76, .85, legs='walk', la=(-34, -50), face_kind='flat'), P('M124 154 L140 150 L142 164 L126 168 Z', WHITE, 4), P('M160 170 L176 168 L176 180 L160 180 Z', WHITE, 4), P('M100 128 Q114 138 120 150', None, 3, 'stroke-dasharray="3 7"'))
art('draw_on_wall', R(10, 10, 180, 140, '#F5E2C4', rx=16), P('M10 56 L190 56 M10 102 L190 102 M70 10 L70 56 M130 56 L130 102 M60 102 L60 150', None, 3, 'opacity=".25"'),
    P('M120 40 Q140 20 150 46 Q160 70 130 66 Q110 62 132 84', None, 6, f'stroke="{RED}"'), P('M146 90 L160 70 L172 92', None, 6, f'stroke="{BLUE}"'),
    K(86, .8, back=True, ra=(40, -150), la=(-34, -60)))

PICKET = lambda x, c: P(f'M{x - 9} 182 L{x - 9} 70 L{x} 56 L{x + 9} 70 L{x + 9} 182 Z', c)  # noqa: E731
RAILS = P('M10 94 L190 94 M10 148 L190 148', None, 10, f'stroke="{BROWN}"')
art('fence_pattern', S(100, 186, 90), RAILS, *[PICKET(24 + i * 22, RED if i % 2 == 0 else GOLD) for i in range(8)])
art('fence_plain', S(100, 186, 90), RAILS, *[PICKET(24 + i * 22, TAN) for i in range(8)])


def ladybird(spots):
    return (shadow(100, 176, 56) + P('M50 96 L30 86 M48 120 L26 120 M52 144 L32 156 M150 96 L170 86 M152 120 L174 120 M148 144 L168 156', None, 6) + C(100, 70, 24, INK, 0) +
            P('M40 124 Q40 66 100 66 Q160 66 160 124 Q160 172 100 172 Q40 172 40 124 Z', RED) + P('M100 66 L100 172', None, 5) +
            ''.join(C(x, y, 11, INK, 0) for x, y in spots) + C(92, 58, 4, WHITE, 0) + C(108, 58, 4, WHITE, 0))


art('ladybird_two_spots', ladybird([(72, 118), (128, 118)]))
art('ladybird_six_spots', ladybird([(74, 94), (126, 94), (64, 124), (136, 124), (76, 152), (124, 152)]))

GF = (P('M-20 0 L-20 40 M-6 0 L-6 40 M14 0 L14 40 M24 0 L24 40', None, 6) + E(2, -6, 30, 18, GOLD, 5) + P('M-22 -10 L-34 -70 L-20 -72 L-10 -14 Z', GOLD, 5) +
      E(-36, -76, 16, 10, GOLD, 5) + dot(-40, -78, 2.5) + P('M-34 -86 L-36 -96 M-26 -84 L-24 -94', None, 4) + C(4, -6, 5, BROWN, 0) + C(-14, 0, 4, BROWN, 0) + C(-26, -40, 4, BROWN, 0))
art('giraffes_four_left', S(100, 184, 92), *[g(x, 150, .85, GF) for x in (50, 91, 132, 173)])

art('box_three_faces', S(100, 184, 76), R(36, 80, 96, 96, TAN), P('M36 80 L76 40 L172 40 L132 80 Z', '#F5D9A8'), P('M132 80 L172 40 L172 136 L132 176 Z', '#C9965A'),
    P('M58 80 L98 40', None, 4, 'opacity=".3"'))

# ---- second look: clearer drivers, road, spit; edges and sizes -----------------
from scenes_b import CAR_SIDE  # noqa: E402
from maths import grid_pts, MEL  # noqa: E402

art('busy_road', R(10, 10, 180, 70, B, rx=20), R(10, 72, 180, 118, '#6D7380', rx=10), P('M20 132 L50 132 M80 132 L110 132 M140 132 L170 132', None, 6, 'stroke="#FFFFFF"'),
    g(6, 44, .46, CAR_SIDE.replace(DGREY, RED)), g(108, 44, .46, CAR_SIDE.replace(DGREY, GOLD)), g(54, 100, .46, CAR_SIDE.replace(DGREY, BLUE)))
art('spit', S(100, 184, 80), sink(122, 140, False), K(50, .78, ra=(26, -86), face_kind='open'),
    P('M62 92 Q92 92 112 136', None, 5, 'stroke="#9AD8F5" stroke-dasharray="2 9"'), C(112, 146, 6, WHITE, 3), C(124, 150, 4, WHITE, 3), P('M70 120 L82 96', None, 6, f'stroke="{B}"'))


def driver(skin, cap=''):
    return g(100, 84, .7, C(0, 0, 24, skin), hair('short'), face('smile')) + cap


art('bus_driver', S(100, 186, 76), R(30, 26, 140, 146, GOLD, rx=20), R(44, 44, 112, 66, B, rx=8, sw=0), P('M70 110 Q70 98 100 98 Q130 98 130 110 Z', BLUE),
    driver(SKIN1, P('M82 72 L84 60 Q100 54 116 60 L118 72 Z', BLUE, 4) + P('M78 72 L122 72', None, 5)), E(100, 108, 24, 6, None, 6), R(44, 44, 112, 66, None, rx=8),
    R(70, 30, 60, 10, WHITE, rx=3, sw=0), C(54, 138, 9, WHITE, 4), C(146, 138, 9, WHITE, 4), R(36, 154, 128, 12, DGREY, rx=4), R(44, 170, 22, 14, INK, rx=4), R(134, 170, 22, 14, INK, rx=4))
art('taxi_driver', S(100, 176, 86), R(84, 46, 40, 20, WHITE, rx=4), P('M92 56 L116 56', None, 4, f'stroke="{GOLD}"'), CAR_SIDE.replace(DGREY, GOLD),
    g(130, 92, .5, C(0, 0, 24, SKIN2), hair('short'), face('smile')), P('M20 126 L180 126', None, 8, 'stroke-dasharray="1 14"'))
art('people', S(100, 184, 92), mini_kid(46, 182, 160, GREEN, SKIN2), mini_kid(154, 182, 164, BLUE), mini_kid(100, 182, 104, GOLD, SKIN2))
art('boys_tall_short_six', S(100, 184, 92), *[mini_kid(x, 182, 130, c) for x, c in zip((30, 60, 90, 120), (GOLD, RED, BLUE, GREEN))], *[mini_kid(x, 182, 86, c, SKIN2) for x, c in zip((152, 180), (PU, ORANGE))])
art('elephants_six_two', *[g(x, y, .75, MEL) for x, y in grid_pts(6, 82, 100, 50, 2)], *[g(x, y, .75, MEL) for x, y in grid_pts(2, 164, 100, 56, 1)])
art('clouds', cloud(76, 70, .9), cloud(126, 128, .95, '#D9E6F5'))
art('climbing_stove', g(66, 44, .64, body('stove')), K(74, .7, y=156, legs='kick_l', la=(-40, -120), ra=(44, -100), face_kind='open'))
from maths import MDK  # noqa: E402
art('elephants_six_two', *[g(x, y, .62, MEL) for x, y in grid_pts(6, 66, 100, 50, 2)], P('M120 30 L120 170', None, 4, 'stroke-dasharray="4 10" opacity=".4"'), *[g(x, y, .62, MEL) for x, y in grid_pts(2, 162, 100, 54, 1)])
art('ducks_four_and_four', R(10, 80, 180, 106, '#9AD8F5', rx=20), *[g(x, y, .7, MDK) for x, y in grid_pts(4, 52, 134, 40, 2)], P('M100 92 L100 176', None, 4, 'stroke-dasharray="4 10" opacity=".4"'), *[g(x, y, .7, MDK) for x, y in grid_pts(4, 150, 134, 40, 2)])
art('kitchen', R(10, 10, 180, 180, '#FFF1D6', rx=26), g(12, 56, .52, body('stove')), g(84, 40, .6, body('fridge')), R(10, 10, 180, 180, None, rx=26))
art('mama_cooking', S(100, 182, 80), MAMA(60, .9, ra=(44, -110)), g(60, 182, .9, P('M44 -110 L60 -60', None, 6, f'stroke="{BROWN}"')), g(104, 100, .42, body('cooking_pot')))
