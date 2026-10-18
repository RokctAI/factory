from props import *
import objects  # noqa: F401
import animals  # noqa: F401
from nature import tree, crescent, stars, sun, cloud, flower_head, FLOWER

S = shadow


def sb(slug):
    return SAMPLES[slug].split('/>', 1)[1] if SAMPLES[slug].startswith('<ellipse') else SAMPLES[slug]


CAT = sb('cat')
DOG = sb('dog')
OWL = body('owl')

# ---- where is it? -----------------------------------------------------------
CHAIR = chair(100, 182, 1.5, TAN)
art('ball_on_chair', S(100, 184, 50), CHAIR, C(100, 96, 18, RED), P('M90 88 Q92 82 98 80', None, 4, 'stroke="#FFFFFF" opacity=".6"'))
art('ball_under_chair', S(100, 184, 50), CHAIR, C(100, 164, 16, RED), P('M90 158 Q92 152 98 150', None, 4, 'stroke="#FFFFFF" opacity=".6"'))
art('ball_next_to_chair', S(100, 184, 70), chair(80, 182, 1.5, TAN), C(164, 164, 16, RED), P('M154 158 Q156 152 162 150', None, 4, 'stroke="#FFFFFF" opacity=".6"'))
HOUSE = P('M24 110 L100 46 L176 110 Z', RED) + R(38, 110, 124, 70, Y) + R(88, 136, 26, 44, BROWN, rx=3) + R(52, 124, 24, 22, B, rx=3) + R(126, 124, 24, 22, B, rx=3)
art('cat_on_roof', S(100, 184, 80), g(0, 10, 1, HOUSE), g(66, -6, .34, CAT))
TABLE = R(20, 96, 160, 16, BROWN, rx=5) + P('M36 112 L36 182 M164 112 L164 182', None, 10)
art('cat_under_table', S(100, 184, 84), TABLE, g(66, 122, .34, CAT))
art('owl_on_branch', R(10, 10, 180, 180, NIGHT, rx=26), P('M10 130 L190 120', None, 14, f'stroke="{BROWN}"'), P('M10 130 L190 120', None, 0), g(54, 26, .48, OWL), crescent(160, 50, 20), stars([(30, 40)], 7))
art('owl_under_branch', R(10, 10, 180, 180, NIGHT, rx=26), P('M10 60 L190 50', None, 14, f'stroke="{BROWN}"'), g(54, 84, .48, OWL), crescent(160, 30, 14), stars([(30, 30)], 7))
art('bird_next_to_moon', R(10, 10, 180, 180, NIGHT, rx=26), C(70, 100, 46, Y), C(56, 86, 7, MOONY, 0), C(84, 118, 9, MOONY, 0), g(116, 66, .32, body('bird')))
TRUNK = P('M88 186 L92 100 L112 100 L116 186 Z', BROWN)
TOP = P('M44 90 Q34 50 66 40 Q74 6 106 10 Q138 0 146 34 Q172 46 160 80 Q166 110 130 108 Q100 120 72 108 Q40 112 44 90 Z', GREEN)
art('dog_in_front_of_tree', S(100, 186, 84), TRUNK, TOP, g(52, 80, .55, DOG))
art('dog_behind_tree', S(100, 186, 84), P('M126 168 Q156 160 160 132', None, 10), P('M126 168 Q156 160 160 132', None, 4, 'stroke="#E9B872"'), P('M70 186 L76 100 L128 100 L134 186 Z', BROWN), TOP, P('M70 170 Q60 172 58 184', None, 0))
art('girl_in_front_of_house', S(100, 184, 86), g(0, -10, .9, HOUSE), GL(100, .62, y=186))
art('girl_behind_house', S(100, 184, 86), GL(160, .5, y=150), g(0, 0, .9, HOUSE))
art('lion_left_elephant_right', S(100, 184, 92), g(-8, 40, .55, body('lion')), g(92, 40, .55, body('elephant')))

# ---- in a line ------------------------------------------------------------------
DINO = body('dinosaur')


DGREYF = '#D5D9E0'
LIZ = body('lizard')
TORT = body('tortoise')


def pick(i, idx):
    return GOLD if i == idx else (None if idx is None else DGREYF)


for name, idx in [('dinos_in_line', None), ('dino_first', 0), ('dino_middle', 1), ('dino_last', 2)]:
    # walking left: the first one is at the front (left), sizes big to small
    parts = []
    for i, (x, s) in enumerate([(4, .4), (72, .33), (130, .27)]):
        c = pick(i, idx)
        parts.append(g(x, 170 - 186 * s, s, DINO.replace('#7FCB8C', c) if c else DINO))
    art(name, S(100, 174, 90), P('M10 172 L190 172', None, 4, 'opacity=".3"'), *parts)
for name, idx in [('lizards_in_line', None), ('lizard_second', 1), ('lizard_fourth', 3), ('lizard_sixth', 5)]:
    parts = []
    for i in range(6):
        c = pick(i, idx)
        parts.append(g(4 + (i % 3) * 64, 20 + (i // 3) * 84, .3, LIZ.replace('#9AD36B', c) if c else LIZ))
    art(name, *parts)
for name, idx in [('tortoise_race', None), ('tortoise_first', 0), ('tortoise_second', 1), ('tortoise_third', 2)]:
    parts = [P('M28 14 L28 190', None, 8, 'stroke-dasharray="10 10"')]
    for i in range(3):
        c = pick(i, idx)
        parts.append(g(26 + i * 48, 4 + i * 60, .3, TORT.replace('#7DAF5A', c) if c else TORT))
    art(name, *parts)
# ---- same on both sides --------------------------------------------------------
MID = P('M100 14 L100 186', None, 3, 'stroke-dasharray="6 8" opacity=".5"')
art('butterfly_symmetrical', S(100, 182, 40), body('butterfly'), MID)
art('butterfly_odd_wings', S(100, 182, 40), P('M100 96 Q60 30 28 50 Q14 80 54 104 Q20 130 46 156 Q72 168 100 120 Z', PK), P('M100 96 Q124 70 140 80 Q146 100 124 110 Q138 130 124 140 Q110 140 100 120 Z', B),
    C(56, 72, 10, PURPLE, 0), C(60, 136, 8, GOLD, 0), E(100, 110, 9, 36, INK, 0), P('M96 76 Q86 52 76 48 M104 76 Q114 52 124 48', None, 4))
art('butterfly_half', S(100, 182, 40), P('M100 96 Q60 30 28 50 Q14 80 54 104 Q20 130 46 156 Q72 168 100 120 Z', PK), C(56, 72, 10, PURPLE, 0), C(60, 136, 8, GOLD, 0), E(100, 110, 9, 36, INK, 0),
    P('M104 60 L170 60 L170 170 L104 170 Z', None, 4, 'stroke-dasharray="6 8" opacity=".5"'))
art('wing_match', P('M60 96 Q100 30 132 50 Q146 80 106 104 Q140 130 114 156 Q88 168 60 120 Z', PK), C(104, 72, 10, PURPLE, 0), C(100, 136, 8, GOLD, 0))
art('wing_different', P('M60 96 Q80 70 100 80 Q106 100 84 110 Q98 130 84 140 Q70 140 60 120 Z', B), C(84, 96, 5, RED, 0))
art('ladybird_symmetrical', S(100, 176, 56), body('ladybird'), MID)
art('leaf_symmetrical', S(100, 182, 46), body('leaf'), MID)
art('flower_half', S(100, 184, 44), P('M100 110 L100 180', None, 14), P('M100 110 L100 180', None, 6, f'stroke="{GREEN}"'),
    P('M100 50 Q70 30 62 60 Q40 70 56 90 Q44 112 70 112 Q80 132 100 116 Z', PK), C(100, 80, 16, GOLD), P('M104 40 L150 40 L150 130 L104 130 Z', None, 4, 'stroke-dasharray="6 8" opacity=".5"'))
art('flower_half_match', P('M70 50 Q100 30 108 60 Q130 70 114 90 Q126 112 100 112 Q90 132 70 116 Z', PK))
art('flower_half_wrong', P('M70 70 Q90 60 92 80 Q100 90 70 100 Z', B), P('M70 50 L70 130', None, 0))
art('face_symmetrical', C(100, 100, 74, Y), eyes(100, 86, 52, 8), smile(100, 120, 30), C(56, 110, 9, PK, 0), C(144, 110, 9, PK, 0), MID)
HOUSE_S = P('M24 100 L100 36 L176 100 Z', RED) + R(38, 100, 124, 80, Y) + R(88, 130, 24, 50, BROWN, rx=3)
art('house_symmetrical', S(100, 184, 80), HOUSE_S, R(52, 116, 26, 24, B, rx=3), R(122, 116, 26, 24, B, rx=3), MID)
art('house_odd_windows', S(100, 184, 80), HOUSE_S, R(48, 112, 22, 20, B, rx=3), R(48, 144, 22, 20, B, rx=3))
art('house_half', S(100, 184, 80), P('M24 100 L100 36 L100 100 Z', RED), R(38, 100, 62, 80, Y), R(52, 116, 26, 24, B, rx=3), R(88, 130, 12, 50, BROWN), P('M104 36 L176 100 L162 100 L162 180 L104 180 Z', None, 4, 'stroke-dasharray="6 8" opacity=".5"'))
art('house_half_match', P('M50 36 L126 100 L50 100 Z', RED), R(50, 100, 62, 80, Y), R(72, 116, 26, 24, B, rx=3), R(50, 130, 12, 50, BROWN))
art('house_half_wrong', P('M50 60 L110 100 L50 100 Z', B), R(50, 100, 50, 80, PK), C(76, 140, 12, WHITE, 4))
art('house_missing_door', S(100, 184, 80), P('M24 100 L100 36 L176 100 Z', RED), R(38, 100, 124, 80, Y), R(52, 116, 26, 24, B, rx=3), R(122, 116, 26, 24, B, rx=3), R(88, 130, 24, 50, '#FFF8E7', rx=3, extra='stroke-dasharray="6 6"'))
art('house_missing_roof', S(100, 184, 80), P('M24 100 L100 36 L176 100 Z', '#FFF8E7', 4, 'stroke-dasharray="8 8"'), R(38, 100, 124, 80, Y), R(52, 116, 26, 24, B, rx=3), R(122, 116, 26, 24, B, rx=3), R(88, 130, 24, 50, BROWN, rx=3))
art('house_missing_window', S(100, 184, 80), HOUSE_S, R(52, 116, 26, 24, B, rx=3), R(122, 116, 26, 24, '#FFF8E7', rx=3, extra='stroke-dasharray="5 5"'))
art('house_one_door', S(100, 184, 80), HOUSE_S, R(52, 116, 26, 24, B, rx=3), R(122, 116, 26, 24, B, rx=3))
art('house_two_doors', S(100, 184, 80), P('M24 100 L100 36 L176 100 Z', RED), R(38, 100, 124, 80, Y), R(54, 130, 24, 50, BROWN, rx=3), R(122, 130, 24, 50, BROWN, rx=3), R(88, 110, 24, 22, B, rx=3))
art('house_roof', S(100, 184, 80), HOUSE_S, R(52, 116, 26, 24, B, rx=3), R(122, 116, 26, 24, B, rx=3), P('M24 100 L100 36 L176 100 Z', None, 8, f'stroke="{GOLD}" stroke-opacity=".9"'))
art('shape_house', S(100, 184, 80), P('M30 96 L100 30 L170 96 Z', '#FF8A3D'), R(44, 96, 112, 84, '#5B8DEF'), R(86, 120, 28, 60, GOLD))
art('church_symmetrical', S(100, 186, 70), P('M100 6 L100 30 M90 16 L110 16', None, 6), P('M60 84 L100 30 L140 84 Z', BLUE), R(50, 84, 100, 96, WHITE), P('M86 180 L86 140 Q100 120 114 140 L114 180 Z', BROWN), P('M62 100 L78 100 L78 126 L62 126 Z M122 100 L138 100 L138 126 L122 126 Z', B, 4), MID)
art('shack_odd', S(100, 184, 80), P('M30 84 L170 70 L170 92 L30 102 Z', '#9AA1AE'), R(38, 96, 124, 84, '#C9B27E'), P('M60 96 L60 180 M100 96 L100 180 M140 96 L140 180', None, 4, 'opacity=".4"'), R(52, 116, 30, 26, B, rx=3), R(110, 124, 30, 56, BROWN, rx=3))
art('rondavel', S(100, 184, 76), P('M20 90 L100 24 L180 90 Z', '#E8C27A'), P('M40 66 L160 66 M60 50 L140 50', None, 4, 'stroke="#B8923A"'), R(34, 90, 132, 90, WHITE, rx=6), P('M86 180 L86 132 Q100 118 114 132 L114 180 Z', BROWN))
art('rondavel_symmetrical', S(100, 184, 76), body('rondavel'), R(46, 112, 22, 20, B, rx=3), R(132, 112, 22, 20, B, rx=3), MID)
art('hut', S(100, 184, 76), P('M16 100 L100 26 L184 100 Z', '#D9B36A'), P('M40 80 L160 80 M64 58 L136 58', None, 4, 'stroke="#A88440"'), R(36, 100, 128, 80, '#C98A4C', rx=4), P('M86 180 L86 136 Q100 122 114 136 L114 180 Z', INK))
art('flats', S(100, 186, 70), R(44, 14, 112, 170, '#C9B8E8', rx=6), *[R(x, y, 26, 20, B, rx=3) for x in (58, 116) for y in (30, 64, 98)], R(86, 140, 28, 44, BROWN, rx=3))
alias('flat', 'flats')
art('flats_odd', S(100, 186, 70), R(44, 14, 112, 170, '#C9B8E8', rx=6), *[R(x, y, 26, 20, B, rx=3) for x, y in [(58, 30), (58, 64), (58, 98), (116, 30)]], R(86, 140, 28, 44, BROWN, rx=3))
art('kinds_of_homes', g(0, 0, .5, body('hut')), g(100, 0, .5, body('flats')), g(0, 96, .5, body('rondavel')), g(100, 96, .5, HOUSE))
art('houses_street', S(100, 186, 90), g(0, -8, .5, HOUSE), g(100, -8, .5, body('hut')), g(50, 86, .5, HOUSE.replace(RED, BLUE)))

# ---- places -------------------------------------------------------------------
def bld(slug, roof, wall, sign, extra=''):
    art(slug, S(100, 186, 86), P('M14 80 L100 24 L186 80 Z', roof), R(24, 80, 152, 100, wall), R(84, 124, 32, 56, BROWN, rx=3), R(36, 98, 34, 26, B, rx=3), R(130, 98, 34, 26, B, rx=3), sign, extra)


bld('school', '#E8746A', Y, P('M100 24 L100 4 L116 9 L100 14', None, 4), R(84, 60, 32, 14, WHITE, rx=3))
bld('clinic', B, WHITE, C(100, 58, 14, WHITE, 4) + P('M100 50 L100 66 M92 58 L108 58', None, 5, f'stroke="{RED}"'))
bld('post_office', '#E8746A', CREAM, R(84, 50, 32, 22, WHITE, rx=2) + P('M84 52 L100 64 L116 52', None, 3), R(140, 140, 22, 40, RED, rx=4))
bld('shop', GREEN, CREAM, R(60, 52, 80, 20, GOLD, rx=4) + P('M24 80 L176 80', None, 0), R(36, 136, 34, 20, RED, rx=2))
alias('spaza_shop', 'shop')
art('community_buildings', g(0, 0, .5, body('school')), g(100, 0, .5, body('clinic')), g(0, 96, .5, body('shop')), g(100, 96, .5, body('post_office')))
art('classroom', R(10, 10, 180, 180, '#FFF1D6', rx=26), R(40, 30, 120, 70, DGREEN, rx=6), P('M60 54 L90 54 M60 72 L120 72', None, 4, 'stroke="#FFFFFF"'), R(30, 130, 60, 10, TAN, rx=3), R(110, 130, 60, 10, TAN, rx=3), P('M36 140 L36 176 M84 140 L84 176 M116 140 L116 176 M164 140 L164 176', None, 6), R(10, 10, 180, 180, None, rx=26))
art('kitchen', R(10, 10, 180, 180, '#FFF1D6', rx=26), g(10, 40, .6, body('stove')), g(100, 30, .7, body('fridge')), R(10, 10, 180, 180, None, rx=26))
art('bathroom', R(10, 10, 180, 180, '#E3F4FF', rx=26), g(0, 40, .62, body('toilet')), g(70, 80, .6, P('M20 70 L180 70 L170 120 Q160 150 100 150 Q40 150 30 120 Z', WHITE), P('M150 70 L150 40 L170 40', None, 6)), R(10, 10, 180, 180, None, rx=26))
art('bedroom', R(10, 10, 180, 180, '#EFE7FF', rx=26), g(10, 40, .8, body('bed')), R(130, 30, 40, 40, B, rx=4), P('M150 30 L150 70 M130 50 L170 50', None, 4), R(10, 10, 180, 180, None, rx=26))
art('farm', R(10, 10, 180, 180, B, rx=26), P('M10 120 Q100 106 190 120 L190 164 Q190 190 164 190 L36 190 Q10 190 10 164 Z', G), P('M40 120 L40 70 L80 44 L120 70 L120 120 Z', RED), P('M66 120 L66 92 L94 92 L94 120 Z', WHITE), g(120, 100, .32, SAMPLES['cow'].split('/>', 1)[1]), R(10, 10, 180, 180, None, rx=26))
art('zoo', R(10, 10, 180, 180, G, rx=26), g(30, 30, .7, body('giraffe')), P('M20 110 L180 110 M20 150 L180 150 M40 100 L40 180 M80 100 L80 180 M120 100 L120 180 M160 100 L160 180', None, 6, f'stroke="{BROWN}"'), R(10, 10, 180, 180, None, rx=26))
art('game_park', R(10, 10, 180, 180, '#FFE9B8', rx=26), sun(150, 50, 16, face=False), g(-10, 40, .55, body('elephant')), g(80, 20, .6, body('giraffe')), P('M10 160 Q100 150 190 160', None, 4, 'opacity=".4"'), R(10, 10, 180, 180, None, rx=26))
art('savanna_animals', R(10, 10, 180, 180, '#FFE9B8', rx=26), g(-6, 70, .5, body('lion')), g(90, 70, .5, body('zebra')), g(70, 6, .45, body('giraffe')), R(10, 10, 180, 180, None, rx=26))
art('waterhole_animals', R(10, 10, 180, 180, '#FFE9B8', rx=26), E(100, 150, 80, 24, '#7EC8F2'), g(-10, 40, .5, body('elephant')), g(96, 40, .5, body('zebra')), R(10, 10, 180, 180, None, rx=26))
art('dinosaur_scene', R(10, 10, 180, 180, '#FFE9B8', rx=26), P('M120 90 L140 30 L160 90 Z', '#C98A4C'), P('M134 46 Q140 36 146 46', None, 0), g(-6, 50, .6, body('dinosaur')), P('M10 170 L190 170', None, 4, 'opacity=".3"'), R(10, 10, 180, 180, None, rx=26))
art('fossil_bones', R(10, 60, 180, 130, '#D9A066', rx=20), P('M40 110 Q80 90 120 110 Q150 126 170 110', None, 10, f'stroke="{WHITE}"'), *[P(f'M{x} 104 L{x - 4} 132 M{x} 104 L{x + 6} 80', None, 7, f'stroke="{WHITE}"') for x in (60, 84, 108, 132)], C(170, 104, 12, WHITE), P('M10 60 L190 60', None, 0))

# ---- second pass ------------------------------------------------------------------
MIRROR = '<g transform="translate(200 0) scale(-1 1)">{}</g>'
for name, idx in [('dinos_in_line', None), ('dino_first', 0), ('dino_middle', 1), ('dino_last', 2)]:
    parts = []
    for i, (x, s) in enumerate([(0, .52), (84, .4), (146, .3)]):
        c = pick(i, idx)
        d = DINO.replace('#7FCB8C', c) if c else DINO
        parts.append(g(x, 176 - 184 * s, s, MIRROR.format(d)))
    art(name, S(100, 176, 92), *parts)
LZ = lambda c: (P('M14 0 Q40 -6 60 2 Q74 8 86 4', None, 14) + P('M14 0 Q40 -6 60 2 Q74 8 86 4', None, 6, f'stroke="{c}"') +  # noqa: E731
                P('M26 -8 L20 -18 M26 8 L20 18 M48 -8 L54 -18 M48 8 L54 18', None, 5) + E(10, 0, 12, 9, c, 4) + dot(6, -3, 2.5))
for name, idx in [('lizards_in_line', None), ('lizard_second', 1), ('lizard_fourth', 3), ('lizard_sixth', 5)]:
    parts = [P('M10 150 L190 150', None, 4, 'opacity=".3"')]
    for i in range(6):
        c = pick(i, idx) or '#9AD36B'
        parts.append(g(8 + i * 31, 100 + (8 if i % 2 else 0), .62, LZ(c)))
    art(name, *parts)
    if idx is not None:
        ALL[name] += P(f'M{8 + idx * 31 + 10} 74 l-8 -14 h16 Z', RED, 3)
for name, idx in [('tortoise_race', None), ('tortoise_first', 0), ('tortoise_second', 1), ('tortoise_third', 2)]:
    parts = [P('M22 14 L22 190', None, 8, 'stroke-dasharray="10 10"'), P('M22 70 L190 70 M22 130 L190 130', None, 3, 'opacity=".25"')]
    for i in range(3):
        c = pick(i, idx)
        parts.append(g(14 + i * 38, -14 + i * 60, .44, TORT.replace('#7DAF5A', c) if c else TORT))
    art(name, *parts)
CROC = body('crocodile')
art('croc_third', ''.join([P('M22 14 L22 190', None, 8, 'stroke-dasharray="10 10"'), P('M22 70 L190 70 M22 130 L190 130', None, 3, 'opacity=".25"'),
                             g(14, -14, .44, TORT), g(40, 100, .9, LZ('#9AD36B')), g(76, 82, .56, CROC.replace('#6CBF6C', GOLD))]))
LEFT_FLOWER = 'M100 50 Q70 30 62 60 Q40 70 56 90 Q44 112 70 112 Q80 132 100 116 Z'
art('flower_half_match', g(-36, 0, 1, MIRROR.format(P(LEFT_FLOWER, PK) + P('M100 64 A16 16 0 0 0 100 96 Z', GOLD))))
art('flower_half_wrong', P('M64 60 L120 40 L104 84 L136 100 L64 120 Z', B), P('M64 70 L64 110', None, 0))
LEFT_HOUSE = P('M24 100 L100 36 L100 100 Z', RED) + R(38, 100, 62, 80, Y) + R(52, 116, 26, 24, B, rx=3)
art('house_half_match', g(-40, 0, 1, MIRROR.format(LEFT_HOUSE)))
art('house_half_wrong', P('M60 100 L120 60 L120 100 Z', B), R(60, 100, 60, 80, PK), C(90, 140, 14, WHITE, 4))
art('wing_match', g(-30, -4, 1.1, MIRROR.format(P('M100 96 Q60 30 28 50 Q14 80 54 104 Q20 130 46 156 Q72 168 100 120 Z', PK) + C(56, 72, 10, PURPLE, 0) + C(60, 136, 8, GOLD, 0))))
art('wing_different', g(20, 0, 1.4, P('M40 96 Q60 70 80 80 Q86 100 64 110 Q78 130 64 140 Q50 140 40 120 Z', B), C(64, 96, 5, RED, 0)))
art('girl_behind_house', S(100, 184, 86), GL(126, .6, y=150, la=(-40, -150)), g(0, 6, .9, HOUSE))
art('waterhole_animals', R(10, 10, 180, 180, '#FFE9B8', rx=26), E(100, 150, 80, 24, '#7EC8F2'), g(4, 44, .46, body('elephant')), g(100, 46, .46, body('zebra')), R(10, 10, 180, 180, None, rx=26))
