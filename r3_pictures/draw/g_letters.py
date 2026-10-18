# Letters: chunky letter tiles, digraph tiles and spelling-tile rows.
from kit import *
from content import words
import content
import string

for ch in string.ascii_lowercase:
    art('letter_' + ch, big_tile(ch))
    alias(ch, 'letter_' + ch)
for ch in 'bdmnptw':
    art('letter_capital_' + ch, big_tile(ch.upper()))
for ch in 'aftg':
    art(f'letter_{ch}_shape', big_tile(ch.upper(), col=WHITE))
for dg in content.table('g_letters:digraphs'):
    art('letter_' + dg, big_tile(dg))
for dg in content.table('g_letters:letters_tiles'):
    alias('letters_' + dg, 'letter_' + dg) if dg in ('ch', 'sh', 'th') else art('letters_' + dg, big_tile(dg))
for snd in content.table('g_letters:sounds'):
    nm = 'sound_' + snd
    if nm not in lib.ALL:
        art(nm, big_tile(snd))
    if snd not in ('sh', 'ch', 'th') and len(snd) > 1:
        alias(snd, nm)
for snd in content.table('g_letters:teams'):
    art('team_' + snd, big_tile(snd, col=Y))
art('letter_capital_t', big_tile('T'))
art('letters_ch_th', S(100, 180, 80), tile(words('g_letters:letters_ch_th.0'), 12, 50, 84, 84), tile(words('g_letters:letters_ch_th.1'), 104, 50, 84, 84), thing('chick', 54, 168, .22), thing('tongue', 146, 166, .2))
art('letters_s_a_t', S(100, 160, 80), tile_row(words('g_letters:letters_s_a_t', 3), y=66, hgt=64))
art('letters_s_a_t_p', S(100, 160, 84), tile_row(words('g_letters:letters_s_a_t_p', 4), y=66, hgt=60))
art('letters_sh_ship', big_tile(words('g_letters:letters_sh_ship'), 'ship'))
art('letters_wh_question', corner_tile(words('g_letters:letters_wh_question'), C(158, 148, 26, WHITE) + boxed(['?'], 132, 122, 52, 52, 30, pad=6, inset=3)))
art('letters_h_o_g_lines', R(14, 40, 172, 120, WHITE, rx=10), P('M24 76 L176 76 M24 116 L176 116', None, 3, f'stroke="{B}"'), P('M24 136 L176 136', None, 3, f'stroke="{PK}" stroke-dasharray="6 6"'), text(words('g_letters:letters_h_o_g_lines'), 100, 116, 46))
art('letters', S(100, 172, 80), tile('a', 18, 70, 52, 52), tile('b', 74, 60, 52, 52), tile('c', 130, 70, 52, 52), tile('A', 46, 118, 52, 52), tile('B', 102, 118, 52, 52))
art('small_and_capital_s', S(100, 178, 80), tile('s', 16, 82, 74, 74, col=Y, ink=BLUE), tile('S', 100, 40, 116 - 32, 116, col=B, ink=RED))
art('letter_layout', R(40, 14, 120, 172, WHITE, rx=6), P('M118 30 L148 30 M60 56 L104 56 M60 80 L148 80 M60 96 L148 96 M60 112 L148 112 M60 128 L130 128 M60 156 L110 156', None, 5, 'opacity=".5"'), C(134, 30, 14, None, 4, f'stroke="{RED}"'))
art('sound_wall', R(10, 20, 180, 150, '#F4E2C6', rx=8), tile(words('g_letters:sound_wall.0'), 20, 30, 50, 40, outline=False), tile(words('g_letters:sound_wall.1'), 76, 30, 50, 40, outline=False), tile(words('g_letters:sound_wall.2'), 132, 30, 50, 40, outline=False), tile(words('g_letters:sound_wall.3'), 20, 76, 50, 40, outline=False), tile(words('g_letters:sound_wall.4'), 76, 76, 50, 40, outline=False), tile(words('g_letters:sound_wall.5'), 132, 76, 50, 40, outline=False), tile(words('g_letters:sound_wall.6'), 20, 122, 50, 40, outline=False), tile(words('g_letters:sound_wall.7'), 76, 122, 50, 40, outline=False), tile(words('g_letters:sound_wall.8'), 132, 122, 50, 40, outline=False))
art('sound_bread', S(96, 176, 70), card(words('g_letters:sound_bread', 1), 16, 40, 150, 90), P('M60 104 L100 104', None, 6, f'stroke="{RED}"'), thing('bread', 156, 150, .36))
art('sound_read', S(96, 176, 70), card(words('g_letters:sound_read', 1), 16, 40, 150, 90), P('M66 104 L104 104', None, 6, f'stroke="{RED}"'), thing('book', 156, 150, .36))
# spelling tiles: tile_<word> and letter_tiles_<a_b_c>
for w in content.table('g_letters:tile_words'):
    art('tile_' + w, S(100, 140, 82), tile_row([w], y=60, hgt=70))
art('tile_shin_wrong', S(100, 140, 82), tile_row(words('g_letters:tile_shin_wrong', 1), y=60, hgt=70))
for nm in content.table('g_letters:letter_tiles'):
    parts = nm.split('_') if '_' in nm else list(nm)
    parts = ['' if p == 'gap' else p for p in parts]
    art('letter_tiles_' + nm, S(100, 150, 84), tile_row(parts, y=70, hgt=64))
for nm in content.table('g_letters:tiles_split'):
    art('tiles_' + nm, S(100, 150, 84), tile_row(nm.split('_'), y=70, hgt=64))
