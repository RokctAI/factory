from props import *
from nature import crescent, stars
import objects  # noqa: F401  (reused bodies)
import animals  # noqa: F401

S = shadow


def sc(slug, *parts):
    art(slug, *parts)


# ---- moving and doing -------------------------------------------------------
sc('child_running', S(100, 182, 56), K(legs='run', la=(-44, -76), ra=(40, -112), face_kind='open'), motion(44, 80))
sc('child_walking', S(100, 182, 50), K(legs='walk', la=(-30, -60), ra=(32, -66)))
sc('child_jumping', S(100, 184, 40), K(y=160, legs='jump', la=(-44, -150), ra=(44, -150), face_kind='open'), P('M70 176 Q100 166 130 176', None, 4, 'opacity=".4"'))
sc('child_jumping_desk', S(100, 184, 70), R(36, 124, 128, 14, TAN, rx=4), P('M48 138 L48 182 M152 138 L152 182', None, 8), K(y=120, s=.66, legs='jump', la=(-44, -150), ra=(44, -150), face_kind='open'))
sc('child_listening', S(100, 182, 50), K(la=(-34, -60), ra=(36, -130)), P('M150 70 Q160 80 150 90 M162 62 Q178 80 162 98', None, 5, f'stroke="{BLUE}"'))
sc('child_talking', S(100, 182, 50), K(x=84, face_kind='open', ra=(40, -80)), P('M130 30 L186 30 Q194 30 194 38 L194 66 Q194 74 186 74 L146 74 L134 86 L136 74 Q126 74 126 66 L126 38 Q126 30 134 30 Z', WHITE, 4), P('M140 44 L180 44 M140 58 L168 58', None, 4))
sc('child_shouting', S(100, 182, 50), K(x=90, face_kind='shout', la=(-34, -132), ra=(38, -132)), P('M150 40 L170 30 M154 60 L180 60 M150 80 L170 90 M40 40 L22 30', None, 6, f'stroke="{RED}"'))
alias('shout', 'child_shouting')
sc('child_sweeping', S(100, 182, 60), K(x=80, la=(20, -96), ra=(30, -70)), P('M98 76 L132 160', None, 12), P('M98 76 L132 160', None, 5, f'stroke="{TAN}"'), P('M116 156 L150 150 L162 182 L120 182 Z', GOLD, 4), C(176, 176, 3, DGREY, 0), C(186, 170, 3, DGREY, 0))
alias('sweep', 'child_sweeping')
sc('child_hiding', S(100, 182, 70), K(x=100, face_kind='smile'), R(30, 92, 140, 90, '#D9A066', rx=6), P('M30 110 L170 110', None, 5, 'stroke="#A0703A"'))
sc('child_sleeping', R(16, 110, 168, 40, '#9C6B3C', rx=8), R(20, 70, 20, 80, '#9C6B3C', rx=6), R(30, 88, 50, 26, WHITE, rx=12), g(60, 92, .55, C(0, 0, 30, SKIN1), face('sleep')),
    P('M80 96 Q130 80 182 96 L182 122 L80 122 Z', B), zzz(120, 46), S(100, 172, 80))
alias('sleep', 'child_sleeping')
alias('sleeping', 'child_sleeping')
sc('child_at_school', P('M110 40 L150 20 L190 40 L190 120 L110 120 Z', '#E8746A'), R(140, 84, 20, 36, BROWN, sw=0), P('M150 20 L150 4 L164 8 L150 12', None, 4), S(70, 182, 46), K(x=70, s=.95, la=(-34, -60), ra=(34, -60)), R(48, 84, 44, 48, RED, rx=8))
sc('child_brushing_teeth', S(100, 182, 50), K(ra=(14, -112), la=(-34, -60)), P('M14 -112 L60 -138', None, 0), g(100, 182, 1, P('M10 -112 L56 -140', None, 6, f'stroke="{B}"'), R(-6, -118, 18, 10, WHITE, rx=4)), C(122, 60, 5, WHITE, 3), C(132, 52, 4, WHITE, 3))
alias('brushing_teeth', 'child_brushing_teeth')
sc('child_body_parts', S(100, 182, 56), K(la=(-56, -110), ra=(56, -110)))
sc('child_waving_right', S(100, 182, 50), K(back=True, la=(-34, -60), ra=(44, -150)), P('M164 24 Q176 36 168 48 M174 14 Q192 36 178 56', None, 4, 'opacity=".5"'))
sc('girl_left_hand_up', S(100, 182, 50), GL(back=True, la=(-40, -150), ra=(32, -62)))
sc('girl_right_hand_up', S(100, 182, 50), GL(back=True, la=(-32, -62), ra=(40, -150)))
sc('kick_right_foot', S(100, 182, 60), K(x=86, back=True, legs='kick_r'), ball(150, 140, 14))
sc('kick_left_foot', S(100, 182, 60), K(x=114, back=True, legs='kick_l'), ball(50, 140, 14))
sc('ball_right', S(100, 182, 60), K(x=80, back=True), ball(152, 166, 16))
sc('ball_left', S(100, 182, 60), K(x=120, back=True), ball(48, 166, 16))
sc('runner_turn_right', S(100, 182, 50), K(x=80, back=True, legs='walk', la=(-40, -70), ra=(40, -110)), P('M120 120 Q160 120 160 70', None, 8, f'stroke="{GREEN}"'), P('M146 82 L160 64 L174 82', None, 8, f'stroke="{GREEN}"'))
sc('runner_turn_left', S(100, 182, 50), K(x=120, back=True, legs='walk', la=(-40, -110), ra=(40, -70)), P('M80 120 Q40 120 40 70', None, 8, f'stroke="{GREEN}"'), P('M26 82 L40 64 L54 82', None, 8, f'stroke="{GREEN}"'))
sc('hand_up', S(100, 182, 70), K(x=90, la=(-34, -60), ra=(36, -160)), R(110, 120, 80, 12, TAN, rx=4), P('M120 132 L120 182 M180 132 L180 182', None, 7))
sc('stand_on_chair', S(100, 182, 50), chair(100, 182, 1.1), K(y=132, s=.75, la=(-40, -130), ra=(40, -130), face_kind='open'))
sc('playing_soccer', P('M10 160 Q100 150 190 160 L190 190 L10 190 Z', G, 0), S(100, 182, 60), K(x=84, legs='kick_r', la=(-44, -80), ra=(36, -70)), ball(146, 146, 14))
alias('soccer', 'playing_soccer')
alias('children_sports', 'playing_soccer')
sc('netball', S(100, 182, 50), K(x=80, la=(-6, -158), ra=(18, -160), face_kind='open'), P('M150 182 L150 60', None, 8), E(136, 60, 20, 6, None, 6, f'stroke="{RED}"'), P('M118 62 L124 86 L136 90 L148 86 L154 62', None, 3), C(104, 18, 13, '#FFB347'))
sc('cricket', S(100, 182, 56), K(x=80, la=(26, -88), ra=(36, -84), hat=P('M-28 -146 Q-26 -176 0 -176 Q26 -176 28 -146 Z', WHITE)), P('M118 96 L170 30', None, 16), P('M118 96 L170 30', None, 8, f'stroke="{TAN}"'), C(178, 64, 8, RED))
sc('skipping', S(100, 182, 50), K(y=170, legs='jump', la=(-44, -76), ra=(44, -76)), P('M56 94 Q26 190 100 186 Q174 190 144 94', None, 4, f'stroke="{RED}"'))
sc('singing', S(100, 182, 50), K(x=88, face_kind='open', la=(-34, -60), ra=(34, -60)), notes(140, 60), notes(160, 120, ROSE))
sc('swimming_x', '')
del ALL['swimming_x']
alias('swimming', 'swimmer')
alias('running', 'child_running')

# ---- clean and dirty ----------------------------------------------------------
sc('clean_child', S(100, 182, 50), K(), P('M150 40 L156 52 L168 56 L156 60 L150 72 L144 60 L132 56 L144 52 Z M48 70 L52 78 L60 80 L52 82 L48 90 L44 82 L36 80 L44 78 Z', GOLD, 0))
MUD = '#8A5A2B'
sc('muddy_child', S(100, 182, 50), K(face_kind='sad'), *[C(x, y, r, MUD, 0) for x, y, r in [(86, 106, 9), (112, 124, 11), (92, 140, 7), (120, 96, 6), (110, 54, 6), (64, 120, 6), (130, 166, 6), (78, 170, 5)]])
sc('sticky_child', S(100, 182, 50), K(ra=(36, -80)), g(100, 182, 1, P('M36 -80 L40 -120', None, 5, f'stroke="{WHITE}"'), C(40, -132, 14, PK, 4)),
    P('M90 112 Q92 124 88 128 M110 108 Q112 120 108 124 M88 66 Q90 76 86 80', None, 6, f'stroke="{ROSE}"'))
sc('clean_hands', hands(100, 120, SKIN1), P('M100 30 L104 40 L114 44 L104 48 L100 58 L96 48 L86 44 L96 40 Z', GOLD, 0))
sc('muddy_hands', hands(100, 120, SKIN1, C(-6, 10, 10, MUD, 0) + C(8, -20, 6, MUD, 0) + C(-14, 30, 6, MUD, 0) + C(-8, -40, 5, MUD, 0)))
sc('painty_hands', hands(100, 120, SKIN1, C(-6, 10, 10, BLUE, 0) + C(8, -24, 7, RED, 0) + C(-10, 32, 7, GOLD, 0) + C(-8, -44, 5, GREEN, 0)))
sc('washing_hands', sink(100, 136, True, True), g(106, 104, .55, P('M-22 40 L-22 -6 L-30 -30 Q-32 -38 -24 -38 L-14 -16 L-14 -44 Q-14 -52 -7 -52 Q0 -52 0 -44 L0 -18 L2 -48 Q3 -56 10 -55 Q17 -54 16 -46 L14 -16 L20 -40 Q23 -47 29 -44 Q34 -41 32 -34 L24 4 L24 40 Z', SKIN1)), R(130, 120, 30, 16, PK, rx=6))
alias('wash', 'washing_hands')
sc('wet',
    hands(100, 120, SKIN1), *[P(f'M{x} {y} Q{x - 6} {y + 10} {x} {y + 14} Q{x + 6} {y + 10} {x} {y} Z', '#7EC8F2', 3) for x, y in [(60, 40), (100, 30), (140, 40), (80, 170), (124, 172)]])
sc('rub', hands(100, 120, SKIN1, C(0, 0, 8, WHITE, 3) + C(-10, 24, 6, WHITE, 3) + C(10, -30, 6, WHITE, 3)), P('M70 40 Q100 26 130 40 M130 40 L122 30 M130 40 L118 44', None, 5, f'stroke="{BLUE}"'))
sc('rinse', sink(100, 150, True), P('M106 40 L106 100', None, 10, 'stroke="#7EC8F2"'), R(70, 10, 74, 16, '#C9CED8', rx=6), g(100, 120, .5, hands(0, 0, SKIN1)), C(140, 100, 6, WHITE, 3), C(60, 108, 5, WHITE, 3))
sc('spit', S(100, 182, 60), sink(100, 150, False), g(70, 160, .6, kid(face_kind='open')), P('M100 74 Q120 90 116 120', None, 5, 'stroke="#9AD8F5" stroke-dasharray="2 8"'), R(136, 98, 20, 30, B, rx=4))
sc('eat', S(100, 182, 60), K(x=86, ra=(18, -112), face_kind='open'), g(86, 182, 1, P('M18 -112 L56 -90', None, 6, f'stroke="{GREY}"'), E(10, -114, 8, 5, GREY, 3)), plate(150, 150, 30, C(150, 144, 12, '#F2D6A0', 3)))
sc('eating_breakfast', R(110, 20, 76, 60, '#FFD9B3', rx=6), C(148, 70, 16, GOLD, 4), R(110, 20, 76, 60, None, rx=6), S(90, 182, 70), K(x=76, s=.9, ra=(30, -100)), R(20, 130, 170, 12, TAN, rx=4), P('M36 142 L36 182 M174 142 L174 182', None, 7), P('M110 110 Q110 130 140 130 Q170 130 170 110 Z', WHITE, 4))
sc('drinking_water', S(100, 182, 50), K(ra=(14, -116)), g(100, 182, 1, P('M8 -132 L30 -132 L26 -100 L12 -100 Z', '#9AD8F5', 4)))
sc('reading_book', S(100, 182, 56), K(la=(-20, -86), ra=(20, -86)), book(100, 96, 56, RED))
sc('watching_tv', tv(150, 110, 1), S(70, 182, 50), K(x=64, s=.9, back=True))
sc('too_much_tv', R(10, 10, 180, 180, NIGHT, rx=26), tv(140, 104, 1), P('M30 130 L106 130 L106 170 L30 170 Z', '#B86A5A'), g(66, 150, .56, kid(back=True)), zzz(36, 40), crescent(160, 40, 14), stars([(110, 30), (40, 150)], 6))
sc('too_many_sweets', S(100, 182, 70), K(x=56, face_kind='sad', la=(-30, -60), ra=(-6, -70)), *[g(x, y, .35, P('M50 104 L20 80 L24 128 Z M150 104 L180 80 L176 128 Z', c), C(100, 104, 48, c)) for x, y, c in [(84, 96, RED), (114, 104, GREEN), (96, 72, PURPLE), (122, 78, GOLD), (78, 122, B), (116, 126, PK)]])
sc('after_toilet', g(40, 14, .6, body('toilet')), sink(146, 120, True, True), P('M80 120 L104 120', None, 6), P('M98 112 L108 120 L98 128', None, 6))
sc('before_eating', sink(56, 110, True, True), P('M104 110 L120 110 M114 102 L122 110 L114 118', None, 6), plate(156, 140, 34, C(156, 132, 14, RED, 4)), P('M128 100 L132 74 M184 100 L180 74', None, 5, f'stroke="{GREY}"'))
sc('after_playing_sand', S(100, 182, 80), P('M10 176 Q30 120 100 116 Q170 120 190 176 Z', '#F5D08A'), K(y=180, s=.75, legs='sit', la=(-40, -50), ra=(40, -50)), C(60, 140, 3, '#D9A65A', 0), C(140, 150, 3, '#D9A65A', 0), P('M150 120 L150 160 L180 160 L176 136 Z', RED))
sc('listening_story', S(100, 182, 80), AD(x=60, s=.9, skin=SKIN3, shirt=ORANGE, hairstyle='long', skirt=True, la=(30, -96), ra=(46, -92), face_kind='open'), book(102, 98, 44, BLUE), K(x=150, s=.66, legs='sit', la=(-30, -50), ra=(30, -50)))
