from props import *
import objects  # noqa: F401
import animals  # noqa: F401
import nature  # noqa: F401
from nature import sun, cloud, tree, flower_head, FLOWER

S = shadow


def sb(slug):
    return SAMPLES[slug].split('/>', 1)[1] if SAMPLES[slug].startswith('<ellipse') else SAMPLES[slug]


# ---- faces ------------------------------------------------------------------------
FACE_O = lambda fill: C(100, 100, 78, fill)  # noqa: E731
art('face_angry', FACE_O('#FFB0A0'), eyes(100, 92, 52, 7), P('M58 70 L86 82 M142 70 L114 82', None, 7), P('M70 140 Q100 118 130 140', None, 6), P('M150 40 L160 30 M164 52 L178 48', None, 5, f'stroke="{RED}"'))
art('face_scared', FACE_O('#E2D4FF'), C(74, 90, 12, WHITE, 4), C(126, 90, 12, WHITE, 4), dot(74, 90, 5), dot(126, 90, 5), P('M60 64 Q74 54 88 62 M112 62 Q126 54 140 64', None, 5), E(100, 136, 14, 18, INK, 0),
    P('M30 70 Q24 90 32 100 M170 70 Q176 90 168 100', None, 4, 'opacity=".5"'))
art('face_sleepy', FACE_O(B), P('M60 90 Q74 100 88 90 M112 90 Q126 100 140 90', None, 6), E(100, 132, 8, 10, INK, 0), zzz(150, 30))
art('face_worried', FACE_O(OR), eyes(100, 90, 52, 7), P('M60 70 L84 64 M140 70 L116 64', None, 5), P('M72 136 Q86 126 100 136 Q114 146 128 136', None, 6))
art('cry', FACE_O(B), P('M60 86 Q74 76 88 86 M112 86 Q126 76 140 86', None, 6), E(100, 132, 18, 14, INK, 0),
    P('M68 96 Q60 120 66 150 M132 96 Q140 120 134 150', None, 10, f'stroke="{BLUE}"'))
art('yawn', FACE_O(Y), P('M60 88 Q74 96 88 88 M112 88 Q126 96 140 88', None, 6), E(100, 134, 18, 24, INK, 0), E(100, 144, 10, 8, ROSE, 0), P('M150 120 Q170 116 172 136', None, 0))
alias('happy_face', 'face_happy')
alias('sad_face', 'face_sad')
alias('angry_face', 'face_angry')
alias('scared_face', 'face_scared')
alias('sleepy_face', 'face_sleepy')
alias('worried_face', 'face_worried')

# ---- signs and lights -----------------------------------------------------------------
THUMB = 'M60 90 L84 90 L104 40 Q110 26 122 32 Q130 38 126 56 L120 84 L156 84 Q170 86 166 100 L156 150 Q152 162 138 162 L60 162 Z'
art('thumbs_up', S(100, 182, 60), P(THUMB, '#F1C27D'), R(30, 86, 30, 80, BLUE, rx=6), P('M124 112 L160 112 M124 136 L156 136', None, 4))
art('thumbs_down', S(100, 182, 60), '<g transform="translate(0 196) scale(1 -1)">' + P(THUMB, '#F1C27D') + R(30, 86, 30, 80, BLUE, rx=6) + P('M124 112 L160 112 M124 136 L156 136', None, 4) + '</g>')
alias('good', 'thumbs_up')
alias('bad', 'thumbs_down')
art('danger_sign', S(100, 182, 70), P('M100 22 L180 160 L20 160 Z', GOLD), P('M100 62 L100 112', None, 12), C(100, 136, 7, INK, 0))
art('unsafe', S(100, 182, 70), P('M100 22 L180 160 L20 160 Z', RED), P('M100 62 L100 112', None, 12, f'stroke="{WHITE}"'), C(100, 136, 7, WHITE, 0))
art('safe', S(100, 182, 60), P('M100 20 L164 44 Q166 120 100 176 Q34 120 36 44 Z', GREEN), P('M70 96 L92 120 L132 74', None, 12, f'stroke="{WHITE}"'))
art('smiley_sign', S(100, 182, 60), P('M100 120 L100 186', None, 10), C(100, 76, 56, GOLD), eyes(100, 66, 36, 6), smile(100, 88, 20))
art('stop', S(100, 186, 30), P('M100 140 L100 186', None, 10), P('M72 16 L128 16 L168 56 L168 112 L128 152 L72 152 L32 112 L32 56 Z', RED), P('M80 28 L120 28 L156 64 L156 104 L120 140 L80 140 L44 104 L44 64 Z', None, 4, f'stroke="{WHITE}"'))
TL = lambda on: (R(64, 14, 72, 160, INK, rx=16, sw=0) + C(100, 48, 22, RED if on == 'r' else '#5A3030', 0) + C(100, 96, 22, '#FF9F2E' if on == 'o' else '#5A4630', 0) + C(100, 144, 22, GREEN if on == 'g' else '#2F4A34', 0))  # noqa: E731
art('traffic_light', S(100, 190, 40), TL('r').replace('#5A4630', '#FF9F2E').replace('#2F4A34', GREEN))
art('light_red', S(100, 190, 40), TL('r'))
art('light_orange', S(100, 190, 40), TL('o'))
art('light_green', S(100, 190, 40), TL('g'))

# ---- body -------------------------------------------------------------------------------
RING = lambda x, y, r=14: C(x, y, r, None, 6, f'stroke="{GOLD}"')  # noqa: E731
art('head', S(100, 182, 50), g(100, 120, 2.2, C(0, 0, 24, SKIN1), hair('short'), face('smile')), P('M76 168 Q100 186 124 168', None, 0))
art('neck', S(100, 186, 50), g(100, 236, 1.3, kid(skin=SKIN1)), RING(100, 104, 16))
art('elbow', S(100, 182, 50), K(la=(-50, -60), ra=(46, -130)), RING(140, 116, 15))
art('knee', S(100, 182, 50), K(), RING(87, 160, 14))
art('ankle', S(100, 182, 50), g(100, 182, 1, kid()), RING(113, 176, 12))
art('feet', S(100, 176, 70), P('M40 160 Q30 100 50 70 Q70 50 84 72 Q92 110 80 160 Q62 176 40 160 Z', '#F1C27D'), P('M160 160 Q170 100 150 70 Q130 50 116 72 Q108 110 120 160 Q138 176 160 160 Z', '#F1C27D'),
    *[C(x, y, 6, '#F1C27D', 4) for x, y in [(46, 60), (60, 52), (74, 56), (128, 56), (140, 52), (154, 60)]])
alias('fingers', 'hand')
art('tongue', C(100, 100, 74, Y), eyes(100, 80, 50, 7), P('M66 112 Q100 128 134 112', None, 6), P('M84 116 L84 146 Q100 166 116 146 L116 116 Z', ROSE), P('M100 122 L100 142', None, 4))
art('hair', S(100, 184, 60), g(100, 120, 2.1, C(0, 4, 24, SKIN2), P('M-30 6 Q-40 -34 -12 -34 Q0 -48 14 -34 Q40 -36 32 4 Q34 -14 18 -18 Q0 -26 -18 -18 Q-32 -14 -30 6 Z', HAIR, 4), face('smile', 0, 6)))
art('clean_teeth', P('M30 70 Q100 40 170 70 Q174 100 160 120 Q100 150 40 120 Q26 100 30 70 Z', ROSE), P('M48 74 L152 74 L148 104 L52 104 Z', WHITE, 4), P('M74 74 L74 104 M100 74 L100 104 M126 74 L126 104', None, 3),
    P('M150 36 L156 48 L168 52 L156 56 L150 68 L144 56 L132 52 L144 48 Z', GOLD, 0))
art('dirty_teeth', P('M30 70 Q100 40 170 70 Q174 100 160 120 Q100 150 40 120 Q26 100 30 70 Z', ROSE), P('M48 74 L152 74 L148 104 L52 104 Z', '#E8DFA8', 4), P('M74 74 L74 104 M100 74 L100 104 M126 74 L126 104', None, 3),
    C(62, 92, 5, '#8A6A2B', 0), C(112, 84, 6, '#8A6A2B', 0), C(138, 96, 4, '#8A6A2B', 0))
art('broken_tooth', S(100, 182, 46), P('M60 40 Q100 20 140 40 Q150 90 136 160 Q128 176 116 160 L108 120 L92 120 L84 160 Q72 176 64 160 Q50 90 60 40 Z', WHITE), P('M100 26 L92 60 L108 78 L96 110', None, 5))
alias('teeth', 'clean_teeth')
art('five_senses', g(0, 0, 1, C(40, 46, 26, WHITE), C(40, 46, 12, '#7A5230', 0), dot(40, 46, 5)), g(0, 0, 1, P('M150 24 Q178 24 176 52 Q174 70 160 72 Q154 74 156 64', '#F1C27D')),
    g(0, 0, 1, P('M100 70 Q92 100 86 116 Q100 124 114 116 Q108 100 100 70 Z', '#F1C27D')), g(0, 0, 1, P('M30 150 Q60 172 90 150', None, 6), P('M48 158 L48 176 Q60 184 72 176 L72 158', ROSE, 4)),
    g(118, 140, .5, P('M-22 40 L-22 -6 L-30 -30 Q-32 -38 -24 -38 L-14 -16 L-14 -44 Q-14 -52 -7 -52 Q0 -52 0 -44 L0 -18 L2 -48 Q3 -56 10 -55 Q17 -54 16 -46 L14 -16 L20 -40 Q23 -47 29 -44 Q34 -41 32 -34 L24 4 L24 40 Z', '#F1C27D')))
art('bird_parts', S(100, 180, 50), body('bird'), RING(30, 79, 12), RING(64, 168, 12), RING(124, 104, 16))
art('animal_coverings', g(0, 0, .5, sb('cat')), g(100, 0, .5, sb('fish')), g(40, 100, .5, body('crocodile')))
art('plant_parts', R(10, 130, 180, 60, '#C99A6B', rx=14), P('M100 130 L100 50', None, 14), P('M100 130 L100 50', None, 6, f'stroke="{GREEN}"'), P('M100 96 Q66 80 56 98 Q74 114 100 104 Z M100 80 Q136 62 146 80 Q128 96 100 88 Z', '#9AD36B', 4),
    flower_head(100, 40, 14), P('M100 136 Q80 156 66 176 M100 136 Q120 156 134 176 M100 136 L100 182', None, 5, f'stroke="{CREAM}"'))
art('reptiles_group', g(0, 0, .5, body('snake')), g(100, 0, .5, body('lizard')), g(0, 96, .5, body('crocodile')), g(100, 96, .5, body('tortoise')))
art('bees_on_flowers', g(0, 30, .6, FLOWER, flower_head(100, 80, 24)), g(80, 30, .6, FLOWER, flower_head(100, 80, 24, GOLD, RED)), g(30, 0, .32, body('bee')), g(110, 10, .3, body('bee')))
art('baby_birds', S(100, 176, 84), g(0, 30, 1, body('nest')), *[g(x, 60, 1, C(0, 30, 18, GOLD), P('M-8 28 L0 16 L8 28 Z', '#FF9F43', 3), dot(-6, 22, 3), dot(6, 22, 3)) for x in (64, 100, 136)])
art('opposites_chart', R(14, 14, 82, 82, B, rx=12), C(40, 56, 18, RED), C(76, 66, 8, RED), R(104, 14, 82, 82, PK, rx=12), sun(130, 54, 12, face=False), P('M166 36 L166 76 M154 44 L178 68 M178 44 L154 68', None, 4, f'stroke="{BLUE}"'),
    R(14, 104, 82, 82, G, rx=12), P('M40 170 L40 120 M30 130 L40 118 L50 130 M70 120 L70 170 M60 160 L70 172 L80 160', None, 5), R(104, 104, 82, 82, Y, rx=12),
    door(116, 118, 26, 56, BROWN, True), door(154, 118, 26, 56, BROWN))
art('safe_home', S(100, 184, 86), P('M20 96 L100 30 L180 96 Z', GREEN), R(34, 96, 132, 84, Y), R(86, 126, 28, 54, BROWN, rx=3), P('M100 40 Q100 34 104 34', None, 0), P('M100 60 Q100 52 108 52 Q116 52 116 60 Q116 68 100 78 Q84 68 84 60 Q84 52 92 52 Q100 52 100 60 Z', ROSE, 4))
art('can_fly', R(10, 10, 180, 180, B, rx=26), cloud(60, 60, .6), cloud(150, 150, .5), g(46, 30, .7, body('bird')), P('M30 150 L60 140', None, 0))
art('cannot_fly', R(10, 10, 180, 180, G, rx=26), P('M10 150 L190 150', None, 0), g(36, 10, .7, body('ostrich')))
art('six_legs', P('M60 80 L30 60 M56 100 L24 100 M60 120 L30 140 M140 80 L170 60 M144 100 L176 100 M140 120 L170 140', None, 7), E(100, 100, 44, 30, '#8FB8F5'), C(100, 56, 18, '#8FB8F5'), dot(94, 52, 3), dot(106, 52, 3))
art('eight_legs', P('M64 84 L28 64 M60 96 L22 92 M60 108 L22 116 M64 120 L30 144 M136 84 L172 64 M140 96 L178 92 M140 108 L178 116 M136 120 L170 144', None, 7), C(100, 102, 36, '#B9A5E6'), C(100, 58, 18, '#B9A5E6'), dot(94, 54, 3), dot(106, 54, 3))
art('same_both_sides', P('M100 50 Q100 30 124 30 Q150 30 150 60 Q150 100 100 150 Q50 100 50 60 Q50 30 76 30 Q100 30 100 50 Z', PK), P('M100 16 L100 184', None, 4, 'stroke-dasharray="6 8"'), P('M30 170 L60 170 M140 170 L170 170', None, 0))
alias('same', 'same_both_sides')
for name, col in [('red', RED), ('blue', BLUE), ('yellow', GOLD), ('green', GREEN), ('orange', '#FF8A3D'), ('pink', '#FF8FB8'), ('purple', PURPLE)]:
    art(f'colour_{name}', S(100, 176, 64), P('M100 30 Q140 26 160 56 Q184 90 160 130 Q140 168 98 164 Q52 168 36 130 Q20 92 44 58 Q64 30 100 30 Z', col), P('M64 64 Q72 52 86 50', None, 7, 'stroke="#FFFFFF" opacity=".5"'))
    if name != 'orange':  # 'orange' stays the fruit
        alias(name, f'colour_{name}')
alias('wild', 'lion')
alias('tame', 'dog')
alias('reptile', 'lizard')
alias('slow', 'snail')
alias('strong', 'wall')
alias('rough', 'tree_bark')
alias('soft', 'pillow')
alias('hard', 'rock')
alias('furry', 'fur')
alias('kind', 'heart')
alias('helping', 'helping_hands')
alias('fresh', 'fresh_apple')
alias('old', 'mkhulu')
alias('zero', 'nest_empty')
alias('round', 'circle')
alias('see', 'eye')
alias('hear', 'ear')
alias('smell', 'nose')
alias('treat', 'sweets')
alias('healthy', 'healthy_plate')
alias('lunch', 'lunchbox_healthy')
alias('long', 'pencil_long')
alias('short', 'pencil_short')
alias('poison', 'poison_bottle')
alias('bunny', 'rabbit')
alias('bug', 'ladybird')
alias('hen', 'chicken')
alias('baba', 'dad')
alias('quack_duck', 'duck')
alias('ladybird_six_legs', 'ladybird')
alias('beetle_six_legs', 'beetle')
alias('beetle_legs', 'beetle')
alias('spider_eight_legs', 'spider')
alias('spider_legs', 'spider')
alias('ant_legs', 'ant_six_legs')
alias('chicken_legs', 'chicken')
alias('mice', 'mouse')
alias('crescents', 'moon_crescent')
alias('ducklings', 'duckling')
# answers written as words with spaces
alias('clean water', 'clean_water')
alias('give seat', 'give_seat')
alias('give to an adult', 'give_adult')
alias('hand up', 'hand_up')
alias('pack away', 'pack_away')
alias('take turns', 'take_turns')
alias('morning and night', 'morning_and_night')
alias('earth turns', 'turn')
alias('a friend', 'good_friend')
alias('grown up', 'grown_up')
art('fast', S(100, 170, 70), g(0, 0, 1, body('shoe')), motion(30, 104, 3, 16, 26), P('M30 104 L30 104', None, 0))
art('dry', S(100, 182, 60), sun(150, 46, 22, face=False), R(30, 70, 110, 106, '#4DC3C3', rx=8), P('M30 150 L140 150 M30 162 L140 162', None, 6, f'stroke="{WHITE}"'))
art('animals', S(100, 182, 84), g(-10, 10, .6, sb('dog')), g(80, 20, .55, sb('cat')))
art('only_birthday', S(100, 182, 74), g(0, 20, .8, body('cake')), g(130, 60, .5, P('M0 0 L90 -30', None, 14), P('M0 0 L90 -30', None, 6, f'stroke="{B}"'), R(-14, -14, 30, 20, WHITE, rx=6), rot=-20))
art('doodle', R(30, 26, 140, 150, WHITE, rx=6), P('M50 120 Q60 50 90 80 T130 70 Q150 110 110 130 Q70 150 80 110 Q90 90 120 100', None, 6, f'stroke="{BLUE}"'), P('M60 150 Q80 140 100 154 T150 146', None, 6, f'stroke="{RED}"'), crayon(150, 60, GREEN, 30))
art('tap', S(100, 186, 40), P('M40 50 L120 50 Q140 50 140 70 L140 90', None, 22), P('M40 50 L120 50 Q140 50 140 70 L140 90', None, 12, 'stroke="#C9CED8"'), R(100, 26, 30, 14, '#C9CED8', rx=4), P('M114 40 L114 50', None, 6),
    P('M140 104 Q132 120 140 128 Q148 120 140 104 Z', '#7EC8F2', 4), P('M140 140 Q132 156 140 164 Q148 156 140 140 Z', '#7EC8F2', 4), R(20, 36, 20, 30, '#C9CED8', rx=4))
art('bun_and_hat', g(0, 30, .5, body('bun')), g(100, 30, .5, sb('hat')), S(100, 150, 90))
art('cat_hat', g(0, 30, .5, sb('cat')), g(100, 30, .5, sb('hat')), S(100, 150, 90))
art('chick_stick', g(0, 30, .5, body('chick')), g(100, 30, .5, P('M40 160 L160 40', None, 18), P('M40 160 L160 40', None, 8, f'stroke="{TAN}"'), P('M120 80 L150 90', None, 8, f'stroke="{TAN}"')), S(100, 150, 90))
art('dad_drum', S(100, 182, 84), AD(66, .9, ra=(40, -76), la=(10, -80)), g(140, 128, 1, R(-30, -20, 60, 50, RED, rx=6), E(0, -20, 30, 9, WHITE), P('M-30 0 L30 0 M-20 -12 L20 26 M20 -12 L-20 26', None, 3, f'stroke="{GOLD}"')))
art('dog_door', door(110, 40, 64, 142, BROWN), S(80, 184, 60), g(10, 74, .6, sb('dog')))
art('candle_burning', S(100, 182, 40), R(78, 80, 44, 96, WHITE, rx=6), P('M100 80 L100 66', None, 4), P('M100 64 Q80 44 100 20 Q120 44 100 64 Z', '#FF8A3D'), P('M100 58 Q92 46 100 34 Q108 46 100 58 Z', GOLD, 0))

# ---- body close-ups (the part is big, a gold ring marks it) ------------------------
LEGS = (P('M50 14 L150 14 L154 70 L106 70 L100 50 L94 70 L46 70 Z', BLUE) + limb('M74 70 L72 170 M126 70 L128 170', SKIN1, 34) +
        E(66, 176, 24, 12, INK, 0) + E(134, 176, 24, 12, INK, 0))
art('knee', LEGS, RING(73, 118, 20), RING(127, 118, 20))
art('ankle', LEGS, RING(72, 160, 16), RING(128, 160, 16))
art('elbow', P('M10 40 L70 40 L70 110 L10 110 Z', GOLD), limb('M60 76 L120 100 L150 40', SKIN1, 30), C(154, 34, 20, SKIN1), RING(120, 100, 22))
art('neck', P('M30 200 Q30 150 70 146 L130 146 Q170 150 170 200', GOLD), limb('M100 150 L100 112', SKIN1, 34), g(100, 76, 1.9, C(0, 0, 24, SKIN1), hair('short'), face('smile')), RING(100, 132, 20))
