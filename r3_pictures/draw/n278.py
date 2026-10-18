# Extra wrong-answer pictures (lessons#278).
from sk import *


art('hive', body('beehive'))
art('jam', body('jar'))
art('jet', sky(B, B, 200), P('M20 110 L150 96 Q186 96 190 104 Q186 112 150 112 Z', WHITE), P('M90 102 L60 50 L80 50 L120 100 Z M90 108 L66 156 L86 156 L120 108 Z', BLUE), P('M24 108 L14 80 L30 80 L44 106 Z', BLUE), *[C(130 + i * 12, 103, 3, SKY, 2) for i in range(3)], P('M10 140 q20 -6 40 0', None, 4, 'stroke="#FFFFFF"'))
art('librarian', S(100, 186, 86), R(120, 30, 70, 150, TAN, rx=4), P('M120 80 h70 M120 130 h70', None, 4), *[R(126 + i * 12, 44 + (i % 2) * 6, 10, 36 - (i % 2) * 6, c, sw=3) for i, c in enumerate((RED, BLUE, GREEN, GOLD, PURPLE))], *[R(126 + i * 12, 94, 10, 36, c, sw=3) for i, c in enumerate((GOLD, ROSE, BLUE, RED, GREEN))], holding('teacher', 'book', 64, 186, .85, arms='give', ts=.2))
art('lid', S(100, 160, 70), E(100, 120, 76, 20, RED), P('M24 120 L24 106 Q100 80 176 106 L176 120', RED), E(100, 104, 76, 20, '#F08A80'), R(84, 76, 32, 18, RED, rx=6))
art('lip', S(100, 172, 70), P('M24 100 Q60 60 100 84 Q140 60 176 100 Q140 150 100 146 Q60 150 24 100 Z', '#E86A8C'), P('M24 100 Q100 116 176 100', None, 5))
art('map', S(100, 176, 80), P('M20 40 L72 26 L128 44 L180 30 L180 160 L128 174 L72 156 L20 170 Z', '#FFF3DE'), P('M72 26 V156 M128 44 V174', None, 4), P('M40 130 Q80 120 96 90 T160 70', None, 4, f'stroke="{RED}" stroke-dasharray="8 6"'), P('M150 60 l16 16 M166 60 l-16 16', None, 5, f'stroke="{RED}"'), thing('tree', 50, 70, .14))
art('nut', S(100, 176, 60), P('M100 30 Q150 30 150 100 Q150 170 100 170 Q50 170 50 100 Q50 30 100 30 Z', '#C98B4E'), P('M100 30 V170 M66 70 Q100 90 134 70 M60 120 Q100 140 140 120', None, 4, 'opacity=".5"'))
art('pan', S(100, 170, 80), E(80, 110, 64, 22, GREY), P('M16 110 L16 128 Q80 160 144 128 L144 110', '#3A3A3A'), E(80, 110, 64, 22, '#6A6A6A'), P('M144 116 L196 102', None, 12), P('M144 116 L196 102', None, 5, f'stroke="{BROWN}"'))
art('pig', S(100, 176, 76), E(100, 116, 70, 48, PK), P('M50 76 L44 48 L72 66 Z M150 76 L156 48 L128 66 Z', PK), E(100, 122, 22, 15, '#F7A8C4'), dot(92, 122, 4), dot(108, 122, 4), eyes(100, 96, 40, 6), P('M40 160 v14 M76 162 v14 M124 162 v14 M160 160 v14', None, 9), P('M168 106 q16 -6 10 10 q-6 10 8 6', None, 4))
art('rat', S(100, 172, 80), P('M30 130 Q40 80 100 84 Q150 86 170 120 Q150 150 100 150 Q50 150 30 130 Z', DGREY), C(140, 84, 16, DGREY), C(140, 84, 7, PK, 3), dot(162, 118, 4), C(174, 124, 5, PK, 3), P('M30 130 Q4 150 20 170 Q40 186 60 176', None, 5), P('M168 128 l18 -4 M168 134 l18 4', None, 3))
art('rug', S(100, 168, 86), R(20, 60, 160, 90, RED, rx=6), R(36, 76, 128, 58, GOLD, rx=4, sw=4), P('M100 84 L130 105 L100 126 L70 105 Z', BLUE, 4), P('M20 70 h-10 M20 90 h-10 M20 110 h-10 M20 130 h-10 M180 70 h10 M180 90 h10 M180 110 h10 M180 130 h10', None, 4))
art('vet', S(100, 186, 86), who_('woman', 70, 186, .9, shirt=WHITE, arms='give'), P('M56 90 Q60 120 76 120', None, 4, f'stroke="{DGREY}"'), thing('dog', 150, 156, .3), hearts(150, 90, 1))
art('wig', S(100, 176, 70), P('M40 130 Q20 40 100 36 Q180 40 160 130 Q150 160 140 150 Q140 90 100 90 Q60 90 60 150 Q50 160 40 130 Z', GOLD), P('M70 60 q10 20 30 10 q20 10 30 -10', None, 4, 'opacity=".5"'), E(100, 166, 40, 8, GREY))
art('yak', S(100, 178, 80), P('M40 90 Q60 60 120 66 Q170 70 170 110 L170 140 Q100 156 40 140 Z', BROWN), P('M40 140 L40 160 M70 146 V166 M130 146 V166 M160 140 V160', None, 9), P('M40 90 Q20 96 24 122 Q30 140 50 130', '#7A4A2A'), P('M28 92 Q10 80 18 64 M48 86 Q60 70 52 58', None, 6, f'stroke="{CREAM}"'), dot(34, 108, 4), P('M50 140 l4 12 M80 146 l2 12 M110 146 l2 12 M140 144 l4 12', None, 4, f'stroke="{BROWN}"'))
