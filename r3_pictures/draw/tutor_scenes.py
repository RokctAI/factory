from props import *
import objects  # noqa: F401
import animals  # noqa: F401
import nature  # noqa: F401
import maths  # noqa: F401
import spatial  # noqa: F401
import misc  # noqa: F401
from nature import sun, cloud, crescent, stars, tree
from maths import grid_pts

S = shadow

# The tutor on her own (replaces the bare emoji).
art('tutor', S(100, 182, 56), g(100, 182, 1, tutor(ra=(44, -120))))


# Things those pictures need that no pack names directly.
art('grey_clouds', R(10, 10, 180, 180, '#C9D3E3', rx=26), cloud(82, 76, 1, '#9AA4B8'), cloud(118, 128, .9, '#AEB8CC'))
SBIRD = lambda x, y, c=BLUE: g(x, y, 1, E(0, 0, 16, 12, c, 4), P('M-14 -2 L-25 2 L-14 6 Z', GOLD, 3), dot(-7, -3, 2.5), P('M11 -4 L22 -11 L20 4 Z', c, 3))  # noqa: E731
BD = lambda x, y, s=1, rot=None: g(x, y, s, P('M8 -4 L22 -14 L20 4 Z', BLUE, 3), E(0, 2, 15, 12, BLUE, 4), C(-12, -8, 9, BLUE, 4), P('M-20 -9 L-28 -6 L-20 -3 Z', GOLD, 3), dot(-13, -10, 2.2), P('M-2 0 Q6 8 12 0', None, 3), rot=rot)  # noqa: E731
art('birds_three_five', R(12, 30, 74, 140, B, rx=14), R(98, 30, 90, 140, B, rx=14), *[BD(52, y, .85) for y in (62, 100, 138)], *[BD(x, y, .75) for x, y in [(124, 56), (164, 78), (124, 100), (164, 122), (124, 144)]])
FLY = lambda x, y: g(x, y, 1, P('M-16 0 Q-4 -18 0 0 Q4 -18 16 0', None, 5))  # noqa: E731
art('birds_six_two_fly', P('M10 160 L190 160', None, 8, f'stroke="{BROWN}"'), *[BD(x, 142, .8) for x in (34, 78, 122, 166)], BD(70, 50, .9, rot=-20), BD(140, 40, .9, rot=-20), P('M96 90 Q104 74 96 66 M160 76 Q168 62 160 56', None, 3, 'stroke-dasharray="3 6"'))
art('house_circle_roof', S(100, 184, 76), C(100, 70, 48, RED), R(40, 100, 120, 80, Y), R(88, 130, 24, 50, BROWN, rx=3), R(52, 116, 24, 22, B, rx=3), R(124, 116, 24, 22, B, rx=3))
CUP = lambda x, y, c=B: g(x, y, 1, P('M-14 -14 L14 -14 L11 14 L-11 14 Z', c, 4), P('M14 -8 Q24 -6 22 4 Q20 10 12 8', None, 4))  # noqa: E731
art('cups_five_and_two', *[CUP(x, y) for x, y in grid_pts(5, 64, 100, 40, 2)], *[CUP(x, y, PK) for x, y in grid_pts(2, 160, 100, 44, 1)], P('M118 50 L118 150', None, 4, 'stroke-dasharray="4 10" opacity=".4"'))
HIP = E(0, 0, 22, 14, '#A99BC9', 4) + C(-20, -8, 12, '#A99BC9', 4) + dot(-22, -12, 2.5) + P('M-14 14 L-14 20 M14 14 L14 20', None, 6)
art('hippos_eight_and_two', R(10, 40, 180, 130, '#9AD8F5', rx=18), *[g(x, y, 1, HIP) for x, y in grid_pts(8, 74, 100, 40, 3)][:8], *[g(x, y, 1, HIP) for x, y in grid_pts(2, 162, 100, 46, 1)])
IC = lambda x, y, eaten=False: g(x, y, .9, P('M-20 0 L0 50 L20 0 Z', '#E8B060', 5), C(0, -10, 22, PK if not eaten else '#FFF8E7', 5, 'stroke-dasharray="5 6"' if eaten else ''))  # noqa: E731
art('ice_creams_four_one_eaten', *[IC(x, 84) for x in (30, 76, 122)], IC(168, 84, True))
LET = lambda x, y, gone=False: R(x - 22, y - 15, 44, 30, WHITE if not gone else '#FFF8E7', rx=3, extra='stroke-dasharray="5 6"' if gone else '') + P(f'M{x - 22} {y - 13} L{x} {y + 2} L{x + 22} {y - 13}', None, 3)  # noqa: E731
art('letters_six_two_given', *[LET(x, y) for x, y in grid_pts(4, 70, 100, 50, 2)], *[LET(x, y, True) for x, y in grid_pts(2, 160, 100, 44, 1)])
art('paint_yellow_blue', S(100, 176, 80), R(20, 90, 64, 80, GOLD, rx=10), P('M100 130 L120 130 M110 120 L110 140', None, 6), R(126, 90, 64, 80, BLUE, rx=10))
art('shampoo_toothbrush', g(-20, 10, .75, body('shampoo')), g(120, 60, .6, P('M0 120 L40 0', None, 14), P('M0 120 L40 0', None, 6, f'stroke="{B}"'), R(26, -14, 30, 22, WHITE, rx=6)))
art('wet_towel', S(100, 186, 60), R(40, 30, 120, 130, '#4DC3C3', rx=8), P('M40 130 L160 130', None, 6, f'stroke="{WHITE}"'), *[P(f'M{x} {y} Q{x - 6} {y + 10} {x} {y + 14} Q{x + 6} {y + 10} {x} {y} Z', '#7EC8F2', 3) for x, y in [(60, 168), (100, 172), (140, 166)]])
art('taxi_windows_six', S(100, 172, 86), P('M14 150 L14 70 Q14 50 34 50 L166 50 Q186 50 186 74 L186 150 Z', WHITE), R(14, 108, 172, 18, GOLD, sw=0), P('M14 150 L14 70 Q14 50 34 50 L166 50 Q186 50 186 74 L186 150 Z'),
    *[R(x, 62, 22, 30, B, rx=3) for x in (26, 52, 78, 104, 130, 156)], C(50, 154, 16, INK, 0), C(150, 154, 16, INK, 0))
art('penguin_flying', R(10, 10, 180, 180, B, rx=26), cloud(56, 48, .45), g(28, 74, .68, body('penguin'), rot=-30), P('M30 150 L56 136 M44 172 L70 156 M24 124 L44 114', None, 5, 'opacity=".45"'))
art('lion_in_house', S(100, 184, 86), P('M16 96 L100 30 L184 96 Z', RED), R(30, 96, 140, 84, Y), g(60, 90, .4, body('lion')))
art('dino_at_shop', R(10, 20, 180, 40, '#E8746A', rx=8), P('M30 20 L30 60 M70 20 L70 60 M110 20 L110 60 M150 20 L150 60', None, 5, 'stroke="#FFFFFF"'), R(20, 60, 160, 120, CREAM), g(30, 70, .55, body('dinosaur')))
art('paper_house', S(100, 184, 80), P('M30 96 L100 36 L170 96 Z', WHITE), R(40, 96, 120, 84, WHITE), P('M60 120 L140 120 M60 140 L140 140 M60 160 L120 160', None, 3, f'stroke="{B}"'), P('M150 60 Q170 50 180 66', None, 4, 'opacity=".4"'))

# Scenes where the tutor herself does the (wrong) thing.
TU = lambda x=60, s=.8, y=182, **k: g(x, y, s, tutor(**k))  # noqa: E731
art('tutor_lifts_feather', S(100, 182, 70), TU(80, .9, la=(-30, -150), ra=(30, -150), face_kind='sad'), g(60, -8, .4, body('feather')), P('M40 70 L28 60 M40 90 L24 90 M160 70 L172 60', None, 4, 'opacity=".5"'))
art('tutor_litter', S(100, 182, 70), TU(70, .9, ra=(50, -60)), g(132, 150, 1, P('M-14 -10 L10 -14 L16 8 L-8 14 Z', WHITE, 4)), g(168, 172, 1, P('M-10 -6 L8 -10 L12 6 L-6 10 Z', WHITE, 4)))
art('tutor_on_seat', S(100, 182, 86), chair(64, 182, .8), g(64, 186, .66, tutor(legs='sit', la=(-30, -50), ra=(30, -50))), g(148, 182, .8, person(skin=SKIN2, shirt=PU, pants=PU, hairstyle='grey', skirt=True, face_kind='sad', ra=(40, -60))), P('M180 120 L184 182', None, 5, f'stroke="{BROWN}"'))
art('tutor_on_swing', S(100, 182, 86), P('M20 20 L100 20 M40 20 L40 120 M80 20 L80 120', None, 5), R(30, 118, 60, 8, BROWN, rx=3), g(60, 146, .55, tutor(legs='sit', la=(-20, -110), ra=(20, -110), face_kind='open')), K(150, .7, face_kind='sad'))
art('tutor_seesaw_alone', S(100, 182, 84), P('M84 182 L100 150 L116 182 Z', RED), P('M20 170 L180 130', None, 12, f'stroke="{BROWN}"'), g(44, 166, .55, tutor(legs='sit')), P('M140 120 L170 120', None, 0))
art('tutor_shorts_snow', R(10, 10, 180, 180, '#D9E6F5', rx=26), P('M10 160 Q100 146 190 160 L190 164 Q190 190 164 190 L36 190 Q10 190 10 164 Z', WHITE), g(100, 180, .85, tutor(shirt=GOLD, pants=BLUE, face_kind='sad')),
    *[C(x, y, 4, WHITE, 0) for x, y in [(40, 40), (160, 50), (30, 110), (170, 120), (60, 70)]])
art('tutor_shouting', S(100, 182, 60), TU(90, .95, face_kind='shout', la=(-34, -130), ra=(36, -130)), P('M150 40 L170 30 M154 60 L180 60 M150 80 L170 90', None, 6, f'stroke="{RED}"'))
art('tutor_sleeps_morning', R(110, 14, 76, 60, '#FFD9B3', rx=6), sun(148, 70, 16, face=False), R(110, 14, 76, 60, None, rx=6), R(16, 120, 168, 40, '#9C6B3C', rx=8), R(30, 98, 50, 26, WHITE, rx=12),
    g(60, 100, .55, C(0, 0, 30, SKIN1), face('sleep'), C(0, -34, 12, HAIR, 4)), P('M80 106 Q130 90 182 106 L182 132 L80 132 Z', PU), zzz(100, 50))
art('tutor_winter_jacket', R(10, 10, 180, 180, B, rx=26), sun(160, 46, 18, face=False), P('M10 160 Q100 146 190 160 L190 164 Q190 190 164 190 L36 190 Q10 190 10 164 Z', G), g(96, 182, .85, tutor(shirt=BLUE, face_kind='sad')),
    P('M58 96 L134 96 M58 120 L134 120', None, 4), P('M40 150 L40 120 M30 140 L40 130 L50 140', None, 0), C(40, 150, 7, PK, 4))
art('tutor_flower_ear', S(100, 182, 60), TU(90, .95, la=(-34, -60), ra=(36, -130)), g(90, 182, .95, P('M36 -130 L36 -100', None, 4, f'stroke="{GREEN}"'), C(44, -138, 9, PK, 4)), P('M150 70 Q160 80 150 90', None, 4, 'opacity=".5"'))
art('tutor_socks_hands', S(100, 182, 60), TU(100, .95, la=(-46, -140), ra=(46, -140), face_kind='open'), g(100, 182, .95, R(-56, -166, 20, 30, RED, rx=8), R(36, -166, 20, 30, RED, rx=8)))
art('tutor_left_hand', S(100, 182, 60), g(100, 182, 1, tutor(back=True, la=(-44, -150), ra=(34, -60))))
art('tutor_fire_phone', S(100, 182, 60), TU(70, .9, ra=(22, -116), face_kind='open'), g(70, 182, .9, R(14, -134, 14, 26, INK, rx=3, sw=0)), g(110, 70, .45, body('fire')))
art('tutor_messy_toys', S(100, 182, 84), TU(60, .85, la=(-34, -130), ra=(36, -130), face_kind='open'), R(116, 156, 22, 22, RED, rx=3), C(160, 166, 12, BLUE, 4), crayon(140, 140, GREEN, 70, .8), R(150, 120, 20, 20, GOLD, rx=3), C(110, 132, 8, PK, 4))
