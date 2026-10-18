# Numbers: a big friendly numeral with that many dots, or base-ten blocks.
from kit import *
from content import pack
from content import words
from numwords import *

NUMCOL = [RED, BLUE, DGREEN, ORANGE, PURPLE, ROSE, '#2BA6A0', GOLD, '#C46A2C', BLUE]


def dots_row(n, y=148, r=8, col=None):
    """Up to 20 dots in ten-frames."""
    out = ''
    frames = 1 if n <= 10 else 2
    fw, fh = (130, 52) if frames == 1 else (84, 36)
    for f in range(frames):
        x0 = 100 - (fw * frames + 10 * (frames - 1)) / 2 + f * (fw + 10)
        out += R(x0, y - fh / 2, fw, fh, WHITE, rx=6, sw=4)
        out += P(f'M{x0} {y} L{x0+fw} {y}' + ''.join(f' M{x0+fw*i/5:.1f} {y-fh/2} L{x0+fw*i/5:.1f} {y+fh/2}' for i in range(1, 5)), None, 2, 'opacity=".35"')
        k = min(10, n - f * 10)
        for i in range(max(0, k)):
            rr, cc = divmod(i, 5)
            out += C(x0 + fw / 10 + cc * fw / 5, y - fh / 4 + rr * fh / 2, fh / 4 - 4, col or RED, 3)
    return out


def _n(v):
    return f'{v:.1f}'.rstrip('0').rstrip('.')


def blocks(n, y=124, hh=52):
    hu, te, on = n // 100, n // 10 % 10, n % 10
    fl, fg, rd, rg, cb = [], [], [], [], []
    parts = []
    if hu:
        cols = 3 if hu > 4 else hu if hu < 3 else 2
        rows = -(-hu // cols)
        s = min(16, (hh - 3 * (rows - 1)) / rows)
        parts.append(('h', cols * (s + 3) - 3, (hu, cols, s)))
    if te:
        w = 7 if hu else 10
        parts.append(('t', te * (w + 4) - 4, (te, w)))
    if on:
        cs = 9 if hu else 12
        cols = 3 if on > 4 else 2 if on > 1 else 1
        parts.append(('o', cols * (cs + 3) - 3, (on, cols, cs)))
    tot = sum(p[1] for p in parts) + 14 * (len(parts) - 1)
    x = 100 - tot / 2
    box = lambda X, Y, W, H: f'M{_n(X)} {_n(Y)}h{_n(W)}v{_n(H)}h{_n(-W)}Z'
    for kind, w, a in parts:
        if kind == 'h':
            k, cols, s = a
            for i in range(k):
                r, c = divmod(i, cols)
                X, YY = x + c * (s + 3), y + r * (s + 3)
                fl.append(box(X, YY, s, s))
                fg.append(f'M{_n(X)} {_n(YY + s / 2)}h{_n(s)}M{_n(X + s / 2)} {_n(YY)}v{_n(s)}')
        elif kind == 't':
            k, rw = a
            for i in range(k):
                X = x + i * (rw + 4)
                rd.append(box(X, y, rw, hh))
                rg.append(''.join(f'M{_n(X)} {_n(y + hh * j / 5)}h{_n(rw)}' for j in range(1, 5)))
        else:
            k, cols, cs = a
            for i in range(k):
                r, c = divmod(i, cols)
                cb.append(box(x + c * (cs + 3), y + hh - (r + 1) * (cs + 3) + 3, cs, cs))
        x += w + 14
    out = ''
    if fl:
        out += P(''.join(fl), B, 3) + P(''.join(fg), None, 1.5, 'opacity=".5"')
    if rd:
        out += P(''.join(rd), G, 3) + P(''.join(rg), None, 1.5, 'opacity=".5"')
    if cb:
        out += P(''.join(cb), Y, 3)
    return out


def numeral(n, mirror=False):
    s = str(n)
    col = NUMCOL[n % 10]
    if n > 999:
        sz = fit(s, 168, 70, outline=True)
        return S(100, 170, 70) + R(14, 50, 172, 110, WHITE, rx=14) + text(s, 100, 105 + sz / 2, sz, outline=True, fill=col)
    sz = fit(s, 160, 74, outline=True)
    t = text(s, 100, 92, sz, outline=True, fill=col)
    if mirror:
        t = f'<g transform="translate(200 0) scale(-1 1)">{t}</g>'
    under = dots_row(n, 148, col=col) if n <= 20 else blocks(n, 118, 56)
    return S(100, 186, 70) + t + under


NUMS = set()
import content
ALLBAD = sorted(content.SLUGS)
for sl in ALLBAD:
    if sl.isdigit():
        NUMS.add(int(sl))
    elif sl.startswith('numeral_') and sl[8:].isdigit():
        NUMS.add(int(sl[8:]))
for n in sorted(NUMS | set(range(0, 21))):
    if n in (10111, 9910):
        continue
    art(f'numeral_{n}', numeral(n))
    alias(str(n), f'numeral_{n}')
for n in range(0, 21):
    alias(int_to_words(n), f'numeral_{n}')
for t in (30, 40, 50, 60, 70, 80, 90):
    alias(int_to_words(t), f'numeral_{t}') if f'numeral_{t}' in lib.ALL else None
art('numeral_9910', numeral(9910))
alias('9910', 'numeral_9910')
art('numeral_3_backwards', numeral(3, mirror=True))
art('numeral_7_backwards', numeral(7, mirror=True))
alias('numeral_3_correct', 'numeral_3')
alias('numeral_7_correct', 'numeral_7')


def name_card(words, col=WHITE):
    lines = wrap(words.split(), 12)
    return S(100, 176, 76) + card(lines, 14, 40, 172, 120, col=col)


for sl in ALLBAD:
    t = sl.replace('-', ' ').replace('_', ' ')
    if sl.startswith('name_') and words_to_int(t[5:]) is not None:
        art(sl, name_card(t[5:], CREAM))
    elif ' ' in sl or '-' in sl:
        n = words_to_int(t)
        if n is not None and n not in range(0, 21) and sl not in lib.ALL:
            art(sl, name_card(t, CREAM))
art('name_capital_zama', S(100, 176, 76), card(words('g_numbers:name_capital_zama', 1), 14, 50, 172, 100, col=CREAM))
art('name_lower_zama', S(100, 176, 76), card(words('g_numbers:name_lower_zama', 1), 14, 50, 172, 100, col=CREAM))
art('numeral_10000', numeral(10000))
art('10111', S(100, 182, 50), R(56, 16, 88, 162, NIGHT, rx=14), R(64, 32, 72, 116, B, rx=4, sw=4), text('10111', 100, 98, fit('10111', 64, 22)), dot(100, 164, 6, GREY))
# ordinals: a rosette with the ordinal
ORDS = content.table('g_numbers:ordinals')
for i, (w, o) in enumerate(ORDS.items()):
    col = [GOLD, GREY, '#E0A060', BLUE, GREEN, ROSE, PURPLE, ORANGE, RED, '#2BA6A0'][i]
    art(w, S(100, 186, 40), P('M80 120 L62 186 L82 176 L94 192 L100 130 Z M120 120 L138 186 L118 176 L106 192 L100 130 Z', RED, 5),
        P(''.join(f'{"M" if j == 0 else "L"}{100 + (60 if j % 2 == 0 else 50) * __import__("math").cos(j * 3.14159 / 12):.0f} {86 + (60 if j % 2 == 0 else 50) * __import__("math").sin(j * 3.14159 / 12):.0f} ' for j in range(24)) + 'Z', col),
        C(100, 86, 40, WHITE), text(o, 100, 86 + fit(o, 64, 30) / 2, fit(o, 64, 30)))
alias('8th', 'eighth')
# counting phrases
art('one two three four five', S(100, 150, 84), tile_row(['1', '2', '3', '4', '5'], y=70, hgt=56))
art('seven eight nine ten', S(100, 150, 84), tile_row(['7', '8', '9', '10'], y=70, hgt=60))
art('numerals_0_to_9', S(100, 170, 84), tile_row(['0', '1', '2', '3', '4'], y=40, hgt=54), tile_row(['5', '6', '7', '8', '9'], y=104, hgt=54))
art('numerals_seven_eight', S(100, 170, 84), text('7', 56, 110, 80, outline=True, fill=NUMCOL[7]), text('8', 144, 110, 80, outline=True, fill=NUMCOL[8]), dots_row(0, 300) , *[C(26 + i * 21, 150, 7, NUMCOL[7], 3) for i in range(0)])
for nm, (te, on) in {'four tens and three ones': (4, 3), 'nine tens and six ones': (9, 6), 'one ten and five ones': (1, 5)}.items():
    art(nm, S(100, 170, 70), blocks(te * 10 + on, 60, 90))
for k in pack(r'flard_\d+'):
    n = int(k[6:])
    art(k, S(100, 176, 80), R(14, 30, 172, 140, WHITE, rx=14), blocks(n, 62, 80))
