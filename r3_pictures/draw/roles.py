from people import *

# Hats and props in person-local units (feet y=0, head centre y=-128, r=30).
CHEF_HAT = P('M-26 -146 Q-44 -170 -24 -180 Q-14 -200 4 -190 Q24 -200 30 -180 Q48 -168 26 -146 Z', WHITE) + R(-26, -152, 52, 12, WHITE, rx=3)
POLICE_CAP = P('M-30 -146 L-26 -166 Q0 -176 26 -166 L30 -146 Z', NIGHT) + P('M-34 -146 L34 -146', None, 7) + C(0, -158, 5, GOLD, 0)
NURSE_CAP = P('M-22 -152 L-18 -170 L18 -170 L22 -152 Z', WHITE) + P('M0 -166 L0 -156 M-5 -161 L5 -161', None, 3, f'stroke="{RED}"')
FIRE_HAT = P('M-34 -142 Q-34 -180 0 -180 Q34 -180 34 -142 Z', RED) + P('M-40 -142 L40 -142', None, 8) + R(-8, -172, 16, 16, GOLD, rx=3)
HARD_HAT = P('M-32 -146 Q-32 -180 0 -180 Q32 -180 32 -146 Z', GOLD) + P('M-38 -146 L38 -146', None, 7)
PILOT_CAP = P('M-30 -148 L-28 -168 Q0 -176 28 -168 L30 -148 Z', NIGHT) + P('M-34 -148 L34 -148', None, 7, f'stroke="{INK}"') + P('M-8 -160 L8 -160', None, 4, f'stroke="{GOLD}"')
POST_CAP = P('M-30 -148 Q-28 -176 0 -176 Q28 -176 30 -148 Z', RED) + P('M10 -148 L40 -144', None, 6)
CROWN = P('M-24 -150 L-28 -180 L-12 -164 L0 -184 L12 -164 L28 -180 L24 -150 Z', GOLD) + C(0, -166, 4, RED, 0)
GRAD = P('M-30 -160 L0 -172 L30 -160 L0 -148 Z', INK) + P('M24 -158 L28 -142', None, 4, f'stroke="{GOLD}"')


def who(slug, *parts, sh=60):
    art(slug, shadow(100, 182, sh), *parts)


def at(*parts, x=100, s=1, y=182):
    return g(x, y, s, *parts)


who('child', at(kid()))
who('brother', at(kid(shirt=GREEN, pants=NIGHT, skin=SKIN2)))
who('sister', at(girl(shirt=PU, skin=SKIN1)))
who('mama', at(person(skin=SKIN2, shirt=GREEN, hairstyle='scarf', haircol=RED, skirt=True)))
alias('mom', 'mama')
who('teacher', at(person(skin=SKIN3, shirt=ORANGE, hairstyle='long', skirt=True, ra=(56, -116)), P('M56 -116 L84 -164', None, 6, f'stroke="{BROWN}"'), R(-90, -110, 50, 40, DGREEN, rx=4)))
who('principal', at(person(skin=SKIN2, shirt=NIGHT, pants=NIGHT, hairstyle='bald', glasses=True, la=(-36, -66), ra=(30, -66)), P('M0 -104 L0 -60', None, 6, f'stroke="{RED}"'), R(-56, -78, 30, 36, BROWN, rx=4)))
who('mkhulu', at(person(skin=SKIN2, shirt=TAN, pants=BROWN, hairstyle='grey', glasses=True, ra=(40, -60)), P('M40 -60 L46 0 M40 -60 Q40 -76 52 -74', None, 6, f'stroke="{BROWN}"')))
who('grown_up', at(person(skin=SKIN1, shirt=BLUE, pants=NIGHT, hairstyle='short')))
who('baker', at(person(skin=SKIN3, shirt=WHITE, pants=GREY, la=(-34, -70), ra=(34, -70), hat=CHEF_HAT)), R(-44, -80, 88, 14, BROWN, rx=7), P('M-34 -80 Q-34 -100 -14 -100 L-14 -80 M14 -80 Q14 -100 34 -100 L34 -80', '#E8B060', 4))
who('chef', at(person(skin=SKIN2, shirt=WHITE, pants=GREY, ra=(40, -110), hat=CHEF_HAT), P('M40 -110 L60 -150', None, 6, f'stroke="{GREY}"'), E(66, -158, 10, 12, GREY)))
who('school_cook', at(person(skin=SKIN2, shirt=WHITE, pants=BLUE, hairstyle='scarf', haircol=BLUE, skirt=True, la=(-34, -74), ra=(34, -74)), P('M-44 -82 L44 -82 L36 -40 L-36 -40 Z', '#8E98AE'), P('M-14 -96 Q-20 -110 -12 -120 M6 -96 Q0 -110 8 -120', None, 4, 'opacity=".4"')))
who('nurse', at(person(skin=SKIN2, shirt=B, pants=B, hairstyle='bun', skirt=True, hat=NURSE_CAP), P('M-6 -80 L6 -80 M0 -86 L0 -74', None, 4, f'stroke="{RED}"')))
who('doctor', at(person(skin=SKIN1, shirt=WHITE, pants=NIGHT, hairstyle='short', glasses=True), P('M-14 -104 Q-20 -70 0 -66 Q20 -70 14 -104', None, 4), C(0, -66, 6, GREY, 3)))
who('dentist', at(person(skin=SKIN3, shirt=WHITE, pants=B, hairstyle='bun', ra=(40, -110)), P('M40 -110 L50 -150', None, 5), C(52, -156, 6, GREY, 3), P('M-14 -112 L14 -112 L12 -96 L-12 -96 Z', B, 3)))
who('paramedic', at(person(skin=SKIN2, shirt=GREEN, pants=GREEN, hairstyle='short', la=(-34, -70)), R(-62, -86, 40, 32, WHITE, rx=4), P('M-42 -78 L-42 -62 M-50 -70 L-34 -70', None, 4, f'stroke="{RED}"'), P('M-26 -80 L26 -80', None, 5, f'stroke="{GOLD}"')))
who('police_officer', at(person(skin=SKIN2, shirt=NIGHT, pants=NIGHT, hat=POLICE_CAP), C(12, -88, 5, GOLD, 0)))
who('firefighter', at(person(skin=SKIN1, shirt=RED, pants=RED, ra=(42, -108), hat=FIRE_HAT), P('M-26 -70 L26 -70 M-26 -56 L26 -56', None, 4, f'stroke="{GOLD}"'), P('M42 -108 Q70 -130 84 -100', None, 9, f'stroke="{GOLD}"'), P('M90 -96 L100 -84 M88 -86 L94 -72', None, 4, f'stroke="{BLUE}"')))
who('builder', at(person(skin=SKIN2, shirt='#FF8A3D', pants=BLUE, ra=(40, -70), hat=HARD_HAT), P('M40 -70 L44 -110', None, 7, f'stroke="{BROWN}"'), R(30, -126, 30, 16, GREY, rx=3)))
who('farmer', at(person(skin=SKIN1, shirt=GREEN, pants=BLUE, ra=(40, -60), hat=P('M-44 -146 L44 -146', None, 7) + P('M-26 -146 Q-24 -176 0 -176 Q24 -176 26 -146 Z', GOLD)), P('M40 -10 L40 -150 M28 -150 L52 -150 M30 -150 L28 -166 M40 -150 L40 -168 M50 -150 L52 -166', None, 5, f'stroke="{BROWN}"')))
who('pilot', at(person(skin=SKIN3, shirt=WHITE, pants=NIGHT, hairstyle='short', hat=PILOT_CAP), P('M-26 -96 L-16 -96 M16 -96 L26 -96', None, 6, f'stroke="{GOLD}"'), P('M0 -104 L0 -60', None, 5, f'stroke="{NIGHT}"')))
who('postman', at(person(skin=SKIN2, shirt=B, pants=NIGHT, hat=POST_CAP, la=(-36, -60)), P('M-26 -102 L26 -50', None, 6, f'stroke="{BROWN}"'), R(-60, -76, 40, 36, BROWN, rx=6), R(-54, -86, 26, 16, WHITE, rx=2)))
who('bus_driver', at(person(skin=SKIN1, shirt=BLUE, pants=NIGHT, hat=POLICE_CAP.replace(NIGHT, BLUE), la=(-30, -76), ra=(30, -76)), C(0, -70, 28, None, 8), C(0, -70, 6, INK, 0)))
who('taxi_driver', at(person(skin=SKIN2, shirt=GOLD, pants=NIGHT, la=(-30, -76), ra=(30, -76)), C(0, -70, 28, None, 8), C(0, -70, 6, INK, 0)), P('M130 30 L190 30 L180 56 L140 56 Z', GOLD))
who('scholar_patrol', at(person(skin=SKIN2, shirt='#FF8A3D', pants=BLUE, hairstyle='puffs', ra=(42, -120)), P('M-24 -100 L24 -50 M24 -100 L-24 -50', None, 5, f'stroke="{GOLD}"'), P('M42 -120 L48 -60', None, 6), C(48, -142, 22, RED), P('M36 -142 L60 -142', None, 6, f'stroke="{WHITE}"')))
who('swimmer', P('M10 120 Q30 110 50 120 T90 120 T130 120 T170 120 T200 120 L200 190 L10 190 Z', '#9AD8F5', 0), at(kid(la=(-60, -150), ra=(40, -110), face_kind='open'), y=210),
    P('M10 120 Q30 110 50 120 T90 120 T130 120 T170 120 T200 120', None, 6, f'stroke="{BLUE}"'), sh=0)
who('queen', at(person(skin=SKIN2, shirt=PURPLE, pants=PURPLE, hairstyle='long', skirt=True, hat=CROWN, ra=(40, -60)), P('M40 -60 L44 -120', None, 6, f'stroke="{GOLD}"'), C(44, -126, 8, RED, 4)))
who('scientist_digging', at(person(skin=SKIN1, shirt=TAN, pants=BROWN, hairstyle='short', glasses=True, la=(10, -60), ra=(36, -70), hat=HARD_HAT.replace(GOLD, CREAM)), x=70),
    P('M106 112 L150 176', None, 7, f'stroke="{BROWN}"'), P('M136 168 L166 162 L170 182 L144 186 Z', GREY, 4), P('M120 182 Q150 160 190 176', '#C99A6B'), P('M150 172 L176 172 M156 180 L170 166 M156 166 L170 180', None, 4, f'stroke="{WHITE}"'), sh=40)
who('stranger', at(person(skin=SKIN1, shirt=DGREY, pants=NIGHT, hairstyle='short', face_kind='flat', hat=P('M-44 -146 L44 -146', None, 7) + P('M-28 -146 Q-26 -178 0 -178 Q26 -178 28 -146 Z', INK))),
    P('M-14 -128 L14 -128', None, 0), g(100, 182, 1, R(-22, -136, 18, 10, INK, rx=3, sw=0), R(4, -136, 18, 10, INK, rx=3, sw=0)), C(160, 50, 20, WHITE), P('M152 44 Q152 34 160 34 Q168 34 168 42 Q168 48 160 52 L160 56', None, 5), dot(160, 64, 3))
who('unknown_lady', at(person(skin=SKIN3, shirt=PK, pants=NIGHT, hairstyle='long', haircol='#C9773E', skirt=True, face_kind='flat', hat=P('M-24 -136 L-4 -136 M4 -136 L24 -136', None, 9))), C(160, 50, 20, WHITE), P('M152 44 Q152 34 160 34 Q168 34 168 42 Q168 48 160 52 L160 56', None, 5), dot(160, 64, 3))
who('people', at(person(skin=SKIN2, shirt=GREEN, hairstyle='scarf', haircol=RED, skirt=True), x=56, s=.82), at(person(skin=SKIN1, shirt=BLUE, hairstyle='short'), x=146, s=.86), at(kid(skin=SKIN2), x=100, s=.6), sh=84)
