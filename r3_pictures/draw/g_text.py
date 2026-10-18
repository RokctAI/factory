# Word cards, sentence strips and other printed cards, with their exact words.
from mkit import *
from content import words
from font import texts
import content

BAD = sorted(content.SLUGS)
CARDCOL = [WHITE, '#FFF6D8', '#EAF6FF', '#EEFBEA', '#FFF0F5', '#F4EEFF']


def word_card(word, col=None, ink=INK):
    col = col or CARDCOL[h(word) % 6]
    band = TILES[h(word) % 6]
    sz = fit(word, 150, 44)
    return S(100, 168, 78) + R(14, 52, 172, 104, col, rx=14) + R(14, 52, 172, 18, band, rx=8, sw=0) + R(14, 52, 172, 104, None, rx=14) + text(word, 100, 104 + sz / 2 - (4 if any(c in 'gjpqy' for c in word) else 0) + 6, sz, col=ink)


def strip(line, col='#FFFFFF', y=100):
    lines = wrap(line.split(' '), 13) if len(line) > 15 else [line]
    n = len(lines)
    sz = min(min(fit(l, 164, 28) for l in lines), 28 if n < 3 else 22)
    hh = 30 + sz * 1.7 * n
    out = S(100, y + hh / 2 + 14, 84) + R(10, y - hh / 2, 180, hh, col, rx=10)
    out += P(f'M24 {y - hh / 2 + 10} h152', None, 3, f'stroke="{B}" opacity=".7"')
    lh = sz * 1.7
    y0 = y - lh * (n - 1) / 2 + sz / 2
    for i, l in enumerate(lines):
        out += text(l, 100, y0 + i * lh, sz)
    return out


W = content.table('g_text:words')
for sl in BAD:
    if sl.startswith('word_') and sl not in ('word_building_cat', 'word_cards_i_the_is', 'word_family_houses', 'word_family_tree'):
        k = sl[5:]
        art(sl, word_card(W.get(k, k.replace('_', ' '))))
art('word_building_cat', S(100, 176, 84), tile_row(words('g_text:word_building_cat', 3), y=40, hgt=60), arrow(100, 108, 100, 128), thing('cat', 100, 150, .26))
art('word_cards_i_the_is', S(100, 180, 60), g(50, -14, .5, body('word_i')), g(50, 40, .5, body('word_the')), g(50, 94, .5, body('word_is')))
art('word_family_houses', S(100, 182, 84), g(0, 0, 1, P('M10 90 L52 54 L94 90 Z', RED), R(18, 90, 68, 86, Y)), g(0, 0, 1, P('M106 90 L148 54 L190 90 Z', BLUE), R(114, 90, 68, 86, Y)),
    texts([(words('g_text:word_family_houses.0'), 52, 112), (words('g_text:word_family_houses.1'), 52, 136), (words('g_text:word_family_houses.2'), 52, 160), (words('g_text:word_family_houses.3'), 148, 112), (words('g_text:word_family_houses.4'), 148, 136), (words('g_text:word_family_houses.5'), 148, 160)], 13))
art('word_family_tree', S(100, 184, 60), P('M92 184 L96 120 L104 120 L108 184 Z', BROWN), P('M30 120 Q14 70 50 50 Q70 10 110 18 Q160 14 170 60 Q194 96 160 122 Z', GREEN),
    texts([(words('g_text:word_family_tree.0'), 70, 64), (words('g_text:word_family_tree.1'), 128, 56), (words('g_text:word_family_tree.2'), 100, 98), (words('g_text:word_family_tree.3'), 146, 98), (words('g_text:word_family_tree.4'), 54, 104)], 12))
art('word', S(100, 168, 78), word_card(words('g_text:word')))
T = dict(content.table('g_text:cards'))
for m in content.table('g_text:months'):
    T['card_' + m] = [m.capitalize()]
NUMW = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8}
for sl in BAD:
    p = sl.split('_')
    if p[0] == 'card' and len(p) == 4 and p[1] in NUMW and p[2] in ('plus', 'minus'):
        T[sl] = [f"{NUMW[p[1]]} {'+' if p[2] == 'plus' else '-'} {NUMW[p[3]]}"]
    if p[0] == 'card' and len(p) == 2 and p[1].isdigit():
        T[sl] = [p[1]]
for sl, lines in T.items():
    sz = min(fit(l, 150, 40) for l in lines)
    art(sl, S(100, 170, 80), card(lines, 14, 46, 172, 112, col=CARDCOL[h(sl) % 6], size=sz))
art('card', S(100, 180, 70), P('M40 40 L100 52 L100 176 L40 164 Z', PK), P('M100 52 L160 40 L160 164 L100 176 Z', WHITE), P('M130 92 Q120 80 112 90 Q106 100 130 120 Q154 100 148 90 Q140 80 130 92 Z', RED, 4))
for sl, nums in {'cards_16_13': ['16', '13'], 'cards_230_302_320': ['320', '230', '302'], 'cards_600_10_8': ['600', '10', '8'], 'cards_600_18_0': ['600', '18', '0'],
                 'cards_60_10_8': ['60', '10', '8'], 'cards_900_4': ['900', '4'], 'cards_900_40': ['900', '40'], 'cards_90_4': ['90', '4']}.items():
    art(sl, S(100, 150, 84), tile_row(nums, y=70, hgt=64, cols=[WHITE] * 3))
art('dialogue_gogo_zola', thing('gogo', 40, 140, .5), thing('child', 160, 140, .5), bubble_say(8, 14, 104, 44, (40, 76)), text(words('g_text:dialogue_gogo_zola.0'), 60, 42, 11), bubble_say(96, 50, 96, 40, (150, 96)), text(words('g_text:dialogue_gogo_zola.1'), 144, 76, 12))
art('dialogue_mama_sipho', thing('mama', 40, 140, .5), thing('child', 160, 140, .5), bubble_say(8, 14, 108, 44, (40, 76)), text(words('g_text:dialogue_mama_sipho.0'), 62, 42, 11), bubble_say(90, 50, 104, 40, (150, 96)), text(words('g_text:dialogue_mama_sipho.1'), 142, 76, 12))
art('dialogue_shop', thing('shop', 46, 140, .5), thing('child', 160, 140, .5), bubble_say(8, 14, 120, 44, (46, 86)), text(words('g_text:dialogue_shop.0'), 68, 42, 12), bubble_say(96, 60, 96, 36, (150, 98)), text(words('g_text:dialogue_shop.1'), 144, 84, 11))
for sl, t in content.table('g_text:headings').items():
    art(sl, S(100, 168, 80), R(14, 60, 172, 90, WHITE, rx=10), R(14, 60, 172, 90, None, rx=10), text(t, 100, 112, fit(t, 150, 28)), P('M30 132 h140', None, 6, f'stroke="{GOLD}"'))
LINES = content.table('g_text:lines')
for sl, t in LINES.items():
    art(sl, strip(t, '#FFFDF3'))
art('list', S(100, 180, 70), R(40, 20, 120, 160, WHITE, rx=8), P('M60 52 h80 M60 84 h70 M60 116 h76 M60 148 h60', None, 5, 'opacity=".55"'), *[dot(54, y, 5) for y in (52, 84, 116, 148)])
for sl in BAD:
    if sl.startswith('list_') and sl[5].isdigit():
        art(sl, S(100, 150, 84), tile_row(sl[5:].split('_'), y=70, hgt=60, cols=[WHITE] * 3))
art('list_heading', S(100, 186, 60), R(36, 14, 128, 172, WHITE, rx=8), R(48, 26, 104, 34, Y, rx=6, sw=4), text(words('g_text:list_heading'), 100, 50, 15), P('M54 84 h80 M54 112 h70 M54 140 h76 M54 168 h50', None, 5, 'opacity=".45"'))
art('list_last_item', S(100, 186, 60), R(36, 14, 128, 172, WHITE, rx=8), P('M54 44 h80 M54 76 h70 M54 108 h76', None, 5, 'opacity=".45"'), R(48, 132, 104, 34, Y, rx=6, sw=4), text(words('g_text:list_last_item'), 100, 156, 15))
art('list_wild_animals', S(100, 186, 60), R(30, 14, 140, 172, WHITE, rx=8), texts([(words('g_text:list_wild_animals.0'), 100, 44)], 15), P('M44 54 h112', None, 4), texts([(words('g_text:list_wild_animals.1'), 100, 88), (words('g_text:list_wild_animals.2'), 100, 120), (words('g_text:list_wild_animals.3'), 100, 152)], 13))
art('list_with_commas', strip(words('g_text:list_with_commas')))
art('list_without_commas', strip(words('g_text:list_without_commas')))
for sl, mk in {'mark_comma': ',', 'mark_comma_small': ',', 'mark_exclaim': '!', 'mark_exclamation': '!', 'mark_full_stop': '.', 'mark_question': '?'}.items():
    art(sl, S(100, 180, 70), R(26, 26, 148, 148, TILES[h(sl) % 6], rx=26), text(mk, 100, 140, 90 if mk not in '.,' else 110, outline=True, fill=INKS[h(sl) % 6]))
alias('full_stop', 'mark_full_stop')
alias('question_mark', 'mark_question')
alias('exclamation_mark', 'mark_exclamation')
alias('comma', 'mark_comma')
for sl, vals in {'notes_100_20': [100, 20], 'notes_100_50': [100, 50], 'notes_50_20_20_10': [50, 20, 20, 10], 'notes_50_50': [50, 50], 'notes_r10_r20': [10, 20], 'notes_two_r10': [10, 10], 'notes_r10_three': [10, 10, 10]}.items():
    n = len(vals)
    if n <= 2:
        art(sl, S(100, 176, 84), *[note(v, 100, 64 + i * 72, 130) for i, v in enumerate(vals)])
    elif n == 3:
        art(sl, S(100, 176, 84), *[note(v, 100, 44 + i * 56, 110) for i, v in enumerate(vals)])
    else:
        art(sl, S(100, 176, 84), *[note(v, 56 + (i % 2) * 88, 70 + (i // 2) * 64, 80) for i, v in enumerate(vals)])
art('notes_50_times_6', *[note(50, 56 + (i % 2) * 88, 44 + (i // 2) * 56, 80) for i in range(6)])
art('notes_and_coins', S(100, 176, 84), note(50, 64, 64, 96), note(20, 136, 100, 96), coin('r5', 50, 146, 20), coin('50c', 96, 152, 16))
art('notes_r10_four_coin_r5', *[note(10, 60 + (i % 2) * 80, 52 + (i // 2) * 52, 74) for i in range(4)], coin('r5', 100, 166, 20))
S_ = content.table('g_text:sentences')
for sl, t in S_.items():
    art(sl, strip(t))
art('strip', S(100, 160, 84), R(10, 70, 180, 60, '#FFFDF3', rx=8), P('M24 100 h152', None, 4, 'opacity=".35"'))
for sl, t in content.table('g_text:titles').items():
    lines = wrap(t.split(), 10)
    sz = min(min(fit(l, 90, 20) for l in lines), 20)
    art(sl, S(100, 186, 60), R(36, 14, 128, 168, TILES[h(sl) % 6], rx=8), P('M48 14 V182', None, 4, 'opacity=".3"'), R(52, 40, 100, 26 + 30 * len(lines), WHITE, rx=6, sw=4),
        *[text(l, 102, 66 + i * 30, sz) for i, l in enumerate(lines)])
art('title_page', S(100, 186, 76), P('M20 40 L100 50 L100 176 L20 166 Z', WHITE), P('M100 50 L180 40 L180 166 L100 176 Z', WHITE), text(words('g_text:title_page.0'), 140, 92, 12), text(words('g_text:title_page.1'), 140, 112, 12), thing('kitten', 140, 144, .2))
SIGNS = {'sign_equal': '=', 'sign_equals': '=', 'sign_greater_than': '>', 'sign_less_than': '<', 'sign_minus': '-', 'sign_plus': '+'}
for sl, sg in SIGNS.items():
    art(sl, S(100, 180, 70), R(26, 26, 148, 148, TILES[h(sl) % 6], rx=26), text(sg, 100, 150, 120, outline=True, fill=INKS[h(sl) % 6]))
art('line up', *[thing('child', 34 + i * 44, 120, .44) for i in range(4)])

