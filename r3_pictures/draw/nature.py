import math
from lib import *


def sun(cx, cy, r, face=True, rays=True):
    out = ''
    if rays:
        d = ''
        for i in range(8):
            a = i * math.pi / 4
            d += f'M{cx + math.cos(a) * (r + 10):.0f} {cy + math.sin(a) * (r + 10):.0f} L{cx + math.cos(a) * (r + 24):.0f} {cy + math.sin(a) * (r + 24):.0f} '
        out += P(d, None, 6, f'stroke="{GOLD}"')
    out += C(cx, cy, r, GOLD)
    if face and r >= 20:
        out += eyes(cx, cy - r * .15, r * .6, max(3, r * .1)) + smile(cx, cy + r * .2, r * .3, 4)
    return out


def cloud(cx, cy, s=1, fill=WHITE):
    return g(cx, cy, s, P('M-50 20 Q-70 20 -66 0 Q-62 -18 -42 -14 Q-36 -40 -8 -38 Q16 -50 30 -26 Q56 -32 60 -8 Q74 6 60 20 Z', fill))


def tree(cx, base, s=1, leaf=GREEN, fruit=None):
    t = (P('M-10 0 L-8 -60 L8 -60 L10 0 Z', BROWN) +
         P('M-56 -80 Q-66 -120 -34 -130 Q-26 -164 6 -160 Q38 -170 46 -136 Q72 -124 60 -90 Q66 -60 30 -62 Q0 -50 -28 -60 Q-60 -56 -56 -80 Z', leaf))
    if fruit:
        t += C(-24, -100, 7, fruit, 4) + C(16, -124, 7, fruit, 4) + C(30, -86, 7, fruit, 4)
    return g(cx, base, s, t)


def stars(pts, r=8):
    out = ''
    for x, y in pts:
        out += P(f'M{x} {y - r} L{x + r * .3:.1f} {y - r * .3:.1f} L{x + r} {y} L{x + r * .3:.1f} {y + r * .3:.1f} L{x} {y + r} L{x - r * .3:.1f} {y + r * .3:.1f} L{x - r} {y} L{x - r * .3:.1f} {y - r * .3:.1f} Z', GOLD, 0)
    return out


def crescent(cx, cy, r, fill=Y):
    return P(f'M{cx + r * .3:.0f} {cy - r} A{r} {r} 0 1 0 {cx + r * .9:.0f} {cy + r * .55:.0f} A{r * .8:.0f} {r * .8:.0f} 0 1 1 {cx + r * .3:.0f} {cy - r} Z', fill)


def panel(fill):
    """A rounded sky scene card."""
    return R(10, 10, 180, 180, fill, rx=26)


def ground(fill=G, y=150):
    return P(f'M10 {y} Q100 {y - 14} 190 {y} L190 164 Q190 190 164 190 L36 190 Q10 190 10 164 Z', fill)


FLOWER = (P('M100 110 L100 180', None, 14) + P('M100 110 L100 180', None, 6, f'stroke="{GREEN}"') +
          P('M100 150 Q130 130 146 144 Q128 166 100 156', GREEN, 4))


def flower_head(cx, cy, r, col=PK, mid=GOLD):
    out = ''
    for i in range(6):
        a = i * math.pi / 3
        out += C(cx + math.cos(a) * r, cy + math.sin(a) * r, r * .8, col, 5)
    return out + C(cx, cy, r * .75, mid, 5)


art('flower', shadow(100, 184, 44), FLOWER, flower_head(100, 80, 24))
art('sun_x', '')
del ALL['sun_x']
art('yellow_sun', sun(100, 100, 46))
art('sunny', panel(B), sun(100, 96, 40))
art('sun_high', panel(B), sun(100, 62, 30), ground())
art('sunrise', panel('#FFD9B3'), sun(100, 150, 40, face=False), ground(G, 150))
art('morning_sunrise', panel('#FFD9B3'), sun(70, 140, 34), ground(G, 150), cloud(146, 60, .6))
art('sun_rising', ALL['morning_sunrise'])
art('afternoon_sun', panel(B), sun(100, 60, 34), ground(), cloud(46, 120, .5), cloud(160, 116, .45))
art('evening', panel('#F7A980'), P('M10 120 L190 120', None, 0), sun(130, 138, 30, face=False), ground('#7FB77E', 140), P('M30 50 L40 50', None, 0), stars([(40, 40)], 6))
art('night_sky', panel(NIGHT), crescent(84, 92, 46), stars([(150, 50), (160, 130), (40, 40), (52, 160), (130, 168)], 9))
art('night_moon', panel(NIGHT), crescent(96, 80, 42), stars([(150, 60), (40, 50), (156, 136)], 8), ground('#3E6B4F', 150))
art('day_sky', panel(B), sun(140, 62, 28), cloud(64, 104, .7), cloud(130, 146, .5))
art('moon_stars', ALL['night_sky'])
art('moon_full', panel(NIGHT), C(100, 100, 56, Y), C(80, 86, 9, MOONY, 0), C(118, 120, 12, MOONY, 0), C(122, 78, 6, MOONY, 0), stars([(36, 40), (166, 160)], 7))
art('moon_crescent', panel(NIGHT), crescent(90, 100, 56), stars([(36, 40), (166, 160), (160, 48)], 7))
art('crescents_unit', '')
del ALL['crescents_unit']
art('day_night_sky', R(10, 10, 90, 180, B, rx=26), R(100, 10, 90, 180, NIGHT, rx=26), P('M76 10 L124 10 L124 190 L76 190 Z', None, 0),
    R(80, 10, 40, 180, B, sw=0), R(100, 10, 30, 180, NIGHT, sw=0), R(10, 10, 180, 180, None, rx=26), P('M100 10 L100 190'),
    sun(54, 80, 22, face=False), crescent(140, 84, 26), stars([(170, 140), (124, 150)], 7))
art('morning_and_night', R(10, 10, 180, 180, '#FFD9B3', rx=26), P('M10 100 L190 100 L190 164 Q190 190 164 190 L36 190 Q10 190 10 164 Z', NIGHT),
    sun(100, 70, 20, face=False), crescent(90, 146, 24), stars([(150, 130), (50, 160)], 7), P('M10 100 L190 100'))
art('day_sequence', R(10, 40, 56, 120, '#FFD9B3', rx=12), sun(38, 130, 14, face=False), R(72, 40, 56, 120, B, rx=12), sun(100, 74, 14, face=False),
    R(134, 40, 56, 120, '#F7A980', rx=12), sun(162, 140, 12, face=False), R(10, 40, 56, 120, None, rx=12), R(72, 40, 56, 120, None, rx=12), R(134, 40, 56, 120, None, rx=12))
art('cloud', shadow(100, 170, 50), cloud(100, 104, 1.3))
art('clouds', cloud(70, 70, 1), cloud(132, 130, 1.1, '#D9E6F5'))
art('cloudy', panel(B), sun(140, 60, 24, face=False), cloud(88, 92, 1.1), cloud(126, 140, .9, '#D9E6F5'))
RAIN = P('M50 120 L42 144 M80 124 L72 148 M110 120 L102 144 M140 124 L132 148 M66 154 L58 178 M96 156 L88 180 M126 154 L118 178', None, 6, f'stroke="{BLUE}"')
art('rain', RAIN, cloud(96, 84, 1.3, '#C9D3E3'))
art('rain_cloud', ALL['rain'])
art('rainy', panel(B), RAIN, cloud(96, 84, 1.3, '#AEB8CC'))
art('windy', panel(B), P('M24 70 Q100 60 130 70 Q160 80 150 54 Q140 36 124 52 M20 104 Q100 96 160 104 Q186 108 180 130 Q170 146 156 132 M30 140 Q80 134 110 140', None, 7, 'stroke="#FFFFFF"'),
    g(144, 118, .5, P('M-10 -40 Q30 -60 40 -10 Q0 0 -10 -40 Z', GREEN)), g(46, 166, .4, P('M-10 -40 Q30 -60 40 -10 Q0 0 -10 -40 Z', '#E9874A')))
art('rainbow', shadow(100, 170, 70),
    P('M20 160 A80 80 0 0 1 180 160', None, 16, f'stroke="{RED}"'), P('M36 160 A64 64 0 0 1 164 160', None, 16, 'stroke="#FFB347"'),
    P('M52 160 A48 48 0 0 1 148 160', None, 16, f'stroke="{GOLD}"'), P('M68 160 A32 32 0 0 1 132 160', None, 16, f'stroke="{GREEN}"'),
    cloud(34, 156, .55), cloud(166, 156, .55))
art('snow', panel('#D9E6F5'), P('M30 160 Q100 140 170 160 L190 190 L10 190 Z', WHITE),
    *[P(f'M{x} {y - 9} L{x} {y + 9} M{x - 8} {y - 5} L{x + 8} {y + 5} M{x + 8} {y - 5} L{x - 8} {y + 5}', None, 4, f'stroke="{BLUE}"') for x, y in [(50, 50), (110, 40), (160, 80), (70, 104), (140, 126), (40, 140)]])
SNOWMAN = (C(0, -40, 44, WHITE) + C(0, -110, 30, WHITE) + eyes(0, -116, 18, 4) + P('M0 -106 L20 -102 L0 -98 Z', '#FF8A3D', 3) +
           P('M-30 -130 L30 -130 L22 -136 L22 -166 L-22 -166 L-22 -136 Z', INK, 0) + dot(0, -54, 5) + dot(0, -34, 5) +
           P('M-40 -60 L-72 -84 M40 -60 L72 -84', None, 6, f'stroke="{BROWN}"') + P('M-26 -86 Q0 -76 26 -86', None, 10, f'stroke="{RED}"'))
art('snowman', shadow(100, 184, 54), g(100, 180, 1, SNOWMAN))
art('snowmen', shadow(100, 184, 84), g(56, 180, .7, SNOWMAN), g(146, 180, .6, SNOWMAN))
art('winter_snow', panel('#D9E6F5'), P('M10 150 Q100 130 190 150 L190 164 Q190 190 164 190 L36 190 Q10 190 10 164 Z', WHITE), g(120, 160, .55, SNOWMAN), tree(52, 160, .55, '#D9E6F5'),
    *[C(x, y, 4, WHITE, 0) for x, y in [(40, 40), (90, 30), (150, 50), (170, 100), (30, 100), (100, 80)]])
art('winter', ALL['winter_snow'])
art('spring_flowers', panel(B), ground(G, 140), g(16, 34, .5, FLOWER, flower_head(100, 80, 24)), g(68, 22, .55, FLOWER, flower_head(100, 80, 24, GOLD, RED)), g(110, 34, .5, FLOWER, flower_head(100, 80, 24, PU)))
art('spring', ALL['spring_flowers'])
art('autumn_leaves', panel('#FFE8C8'), *[g(x, y, .45, P('M-40 0 Q-36 -50 0 -60 Q36 -50 40 0 Q20 30 0 40 Q-20 30 -40 0 Z', c), P('M0 -60 L0 40', None, 4)) for x, y, c in [(60, 60, '#E9874A'), (130, 80, RED), (80, 140, GOLD), (150, 150, BROWN)]])
art('summer', panel(B), sun(150, 54, 26), P('M10 140 Q100 126 190 140 L190 164 Q190 190 164 190 L36 190 Q10 190 10 164 Z', '#FFE08A'),
    P('M60 150 L60 70', None, 6), P('M20 76 Q60 30 100 76 Z', RED), P('M40 76 Q60 40 80 76', None, 4))
art('summer_winter_line', R(10, 10, 90, 180, B, rx=26), R(100, 10, 90, 180, '#D9E6F5', rx=26), R(80, 10, 40, 180, B, sw=0), R(100, 10, 30, 180, '#D9E6F5', sw=0),
    R(10, 10, 180, 180, None, rx=26), P('M100 10 L100 190'), sun(54, 60, 18, face=False),
    g(22, 90, .36, P('M64 40 L44 50 L22 82 L46 98 L58 84 L58 168 L142 168 L142 84 L154 98 L178 82 L156 50 L136 40 Q100 62 64 40 Z', GOLD)),
    *[P(f'M{x} {y - 9} L{x} {y + 9} M{x - 8} {y - 5} L{x + 8} {y + 5} M{x + 8} {y - 5} L{x - 8} {y + 5}', None, 4, f'stroke="{BLUE}"') for x, y in [(130, 40), (170, 60), (150, 90)]],
    g(110, 104, .36, P('M36 130 Q36 52 100 52 Q164 52 164 130 Z', RED), R(30, 124, 140, 34, WHITE, rx=12), C(100, 44, 14, WHITE)))
art('hot', shadow(100, 186, 40), sun(140, 54, 22, face=False), R(70, 30, 30, 120, WHITE, rx=15), C(85, 158, 24, RED), R(79, 70, 12, 90, RED, sw=0), P('M100 60 L110 60 M100 84 L110 84 M100 108 L110 108', None, 4))
art('cold', shadow(100, 186, 40), R(70, 30, 30, 120, WHITE, rx=15), C(85, 158, 24, BLUE), R(79, 120, 12, 40, BLUE, sw=0), P('M100 60 L110 60 M100 84 L110 84 M100 108 L110 108', None, 4),
    P('M150 30 L150 74 M131 41 L169 63 M169 41 L131 63', None, 6, f'stroke="{BLUE}"'))
art('leaf', shadow(100, 182, 46), P('M100 20 Q170 60 150 130 Q130 176 100 176 Q70 176 50 130 Q30 60 100 20 Z', GREEN), P('M100 40 L100 186 M100 80 L130 64 M100 110 L136 92 M100 140 L132 122 M100 80 L70 64 M100 110 L64 92 M100 140 L68 122', None, 4))
art('leaves', *[g(x, y, .5, P('M100 20 Q170 60 150 130 Q130 176 100 176 Q70 176 50 130 Q30 60 100 20 Z', c), P('M100 40 L100 176', None, 4)) for x, y, c in [(10, 40, GREEN), (90, 20, DGREEN), (50, 90, '#9AD36B')]])
art('leaf_symmetrical', ALL['leaf'])
art('leaf_torn', shadow(100, 182, 46), P('M100 20 Q170 60 150 130 Q130 176 100 176 L100 150 L80 140 L96 120 L70 104 L90 86 L66 70 L100 40 Z', GREEN),
    P('M100 40 L100 186 M100 80 L130 64 M100 110 L136 92 M100 140 L132 122', None, 4))
art('new_leaves', shadow(100, 184, 50), P('M100 182 L100 70', None, 14), P('M100 182 L100 70', None, 6, f'stroke="{BROWN}"'),
    *[g(x, y, .32, P('M100 20 Q170 60 150 130 Q130 176 100 176 Q70 176 50 130 Q30 60 100 20 Z', '#9AD36B'), rot=r) for x, y, r in [(96, 30, 30), (110, 80, 60), (96, 120, -60), (80, 56, -40)]],
    C(100, 60, 8, PK, 4), C(70, 110, 7, PK, 4), C(134, 96, 7, PK, 4))
art('blossoms', shadow(100, 184, 50), P('M100 182 L100 90 M100 120 L60 70 M100 110 L146 60', None, 12), P('M100 182 L100 90 M100 120 L60 70 M100 110 L146 60', None, 5, f'stroke="{BROWN}"'),
    *[flower_head(x, y, 9, PK, WHITE) for x, y in [(60, 66), (100, 84), (146, 56), (80, 100), (124, 86)]])
art('tree', shadow(100, 184, 60), tree(100, 182, 1))
alias('trees', 'tree')
art('tree_leaves', shadow(100, 184, 60), tree(100, 182, 1, DGREEN), *[g(x, y, .2, P('M100 20 Q170 60 150 130 Q130 176 100 176 Q70 176 50 130 Q30 60 100 20 Z', '#9AD36B')) for x, y in [(60, 50), (100, 40), (120, 70), (70, 80)]])
art('tree_bark', R(30, 10, 140, 180, '#9C6B3C', rx=20), P('M60 20 Q50 60 64 100 Q76 140 60 180 M100 16 Q110 60 96 100 Q86 140 104 184 M140 20 Q130 60 146 100 Q156 140 140 180', None, 6, 'stroke="#6B4423"'),
    P('M70 60 L84 64 M120 120 L134 124 M80 150 L92 152', None, 5, 'stroke="#6B4423"'), R(30, 10, 140, 180, None, rx=20))
art('roots', ground('#C99A6B', 40), P('M100 40 L100 100 M100 70 Q70 90 54 130 M100 70 Q130 90 146 130 M100 100 Q90 130 96 170 M100 90 Q120 120 120 160 M70 100 L44 100 M130 100 L160 96', None, 6, f'stroke="{CREAM}"'),
    P('M100 40 L100 14', None, 10, f'stroke="{GREEN}"'), P('M100 24 Q76 6 62 20 Q80 34 100 24 Z M100 24 Q124 6 138 20 Q120 34 100 24 Z', GREEN, 4))
art('stem', shadow(100, 184, 40), P('M100 180 Q90 120 100 30', None, 16), P('M100 180 Q90 120 100 30', None, 6, f'stroke="{GREEN}"'),
    P('M96 110 Q60 90 52 108 Q70 124 96 116 Z M100 70 Q136 50 146 68 Q128 84 100 76 Z', '#9AD36B', 4))
art('seed', shadow(100, 170, 50), E(100, 110, 36, 52, '#D9A066', extra='transform="rotate(30 100 110)"'), P('M86 80 Q100 110 110 140', None, 4))
art('soil', R(10, 50, 180, 140, '#9C6B3C', rx=26), P('M10 70 Q100 40 190 70', None, 0), C(50, 100, 5, '#6B4423', 0), C(110, 130, 6, '#6B4423', 0), C(150, 90, 5, '#6B4423', 0), C(80, 160, 5, '#6B4423', 0), C(150, 156, 4, '#6B4423', 0),
    P('M100 50 L100 20', None, 10, f'stroke="{GREEN}"'), P('M100 30 Q78 12 64 26 Q82 40 100 30 Z', GREEN, 4))
art('sand', shadow(100, 180, 80), P('M10 176 Q30 100 100 96 Q170 100 190 176 Z', '#F5D08A'), C(70, 140, 3, '#D9A65A', 0), C(120, 130, 3, '#D9A65A', 0), C(100, 156, 3, '#D9A65A', 0), C(150, 156, 3, '#D9A65A', 0),
    P('M130 96 L150 40 L168 46 L148 102', '#5B8DEF'), P('M40 106 L36 80 Q50 70 64 80 L60 106', RED))
art('puddle', shadow(100, 170, 0), P('M20 140 Q16 110 60 112 Q90 96 130 108 Q186 108 180 140 Q176 166 120 162 Q80 172 50 162 Q22 160 20 140 Z', '#9AD0F0'), P('M60 130 Q80 124 100 130', None, 4, 'stroke="#FFFFFF"'),
    C(150, 132, 8, None, 3, f'stroke="{WHITE}"'))
art('river', panel(G), P('M60 10 Q30 60 80 100 Q130 140 90 190 L150 190 Q190 140 140 100 Q90 60 120 10 Z', '#7EC8F2'), P('M80 40 Q90 50 100 40 M110 120 Q120 130 130 120', None, 4, 'stroke="#FFFFFF"'), R(10, 10, 180, 180, None, rx=26))
art('clean_water', shadow(100, 184, 56), P('M50 40 L150 40 L136 178 L64 178 Z', WHITE), P('M54 74 L146 74 L136 178 L64 178 Z', '#9AD8F5', 0), P('M50 40 L150 40 L136 178 L64 178 Z'),
    P('M82 100 L86 150', None, 5, 'stroke="#FFFFFF"'), P('M150 28 L158 18 M166 44 L178 42', None, 4, f'stroke="{GOLD}"'))
art('muddy_water', shadow(100, 184, 56), P('M50 40 L150 40 L136 178 L64 178 Z', WHITE), P('M54 74 L146 74 L136 178 L64 178 Z', '#9C7A4E', 0), P('M50 40 L150 40 L136 178 L64 178 Z'),
    C(84, 120, 5, '#6B4423', 0), C(110, 148, 6, '#6B4423', 0), C(116, 100, 4, '#6B4423', 0))
art('fire', shadow(100, 184, 60), P('M50 176 L150 150 M50 150 L150 176', None, 14, f'stroke="{BROWN}"'),
    P('M100 20 Q150 70 146 120 Q144 164 100 166 Q56 164 54 120 Q52 90 76 70 Q80 100 92 100 Q84 60 100 20 Z', '#FF8A3D'),
    P('M100 80 Q126 110 124 136 Q120 158 100 158 Q80 158 78 136 Q78 116 100 80 Z', GOLD, 0))
art('web', R(10, 10, 180, 180, '#E6EEF8', rx=26),
    P('M100 100 L20 20 M100 100 L180 20 M100 100 L20 180 M100 100 L180 180 M100 100 L100 14 M100 100 L100 186 M100 100 L14 100 M100 100 L186 100', None, 3),
    P('M100 40 L142 58 L160 100 L142 142 L100 160 L58 142 L40 100 L58 58 Z M100 66 L124 76 L134 100 L124 124 L100 134 L76 124 L66 100 L76 76 Z M100 86 L110 90 L114 100 L110 110 L100 114 L90 110 L86 100 L90 90 Z', None, 3),
    R(10, 10, 180, 180, None, rx=26))
art('globe_torch', panel(NIGHT), P('M10 76 L80 92 L80 108 L10 124 Z', '#FFE9A8', 0), R(4, 86, 26, 28, GREY, rx=4), C(124, 100, 52, BLUE),
    P('M98 66 Q114 76 106 96 Q96 110 112 124 M140 60 Q150 80 138 96 Q130 116 150 130', None, 0), P('M100 64 Q120 74 110 96 Q100 110 116 128 Q108 140 96 136 Q80 120 84 100 Q86 80 100 64 Z M146 66 Q164 80 168 106 Q160 112 150 104 Q140 90 146 66 Z', GREEN, 4),
    P('M124 48 L124 40 M70 100 L78 100', None, 0), P('M76 100 A52 52 0 0 0 124 152', None, 0), P('M124 152 A52 52 0 0 1 124 48 Z', '#1F2A44', 0, 'opacity=".35"'),
    P('M160 34 A70 70 0 0 1 186 70', None, 5, f'stroke="{GOLD}"'), P('M186 70 L180 56 M186 70 L172 66', None, 5, f'stroke="{GOLD}"'))
art('turn', shadow(100, 186, 56), C(100, 100, 60, BLUE), P('M76 60 Q96 70 88 94 Q78 112 96 130 Q86 146 72 138 Q52 120 58 96 Q62 70 76 60 Z M128 56 Q156 70 158 102 Q146 110 134 98 Q122 80 128 56 Z', GREEN, 4),
    P('M30 150 A80 80 0 0 0 170 150', None, 6, f'stroke="{RED}"'), P('M170 150 L172 132 M170 150 L154 144', None, 6, f'stroke="{RED}"'))
art('sky', panel(B), cloud(70, 70, .8), cloud(140, 130, .7), g(120, 54, .3, P('M0 0 Q20 -20 40 0 Q60 -20 80 0', None, 18)))
art('sky_fly', panel(B), cloud(60, 60, .6), g(66, 66, .62, P('M70 80 Q40 50 20 70 Q40 90 70 90 Z M110 80 Q140 50 160 70 Q140 90 110 90 Z', B), E(90, 96, 30, 22, '#4A5568'), C(64, 90, 14, '#4A5568'), C(58, 86, 5, RED, 0)))
art('day', ALL['day_sky'])
art('night', ALL['night_sky'])
