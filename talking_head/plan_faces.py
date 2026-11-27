"""Plan a face-pack run: which lines each member's pictures are drawn from.

  python plan_faces.py <agent_files> <voice_files> <personas> <standin> [lines]
<agent_files> / <voice_files>: file lists of the agent and voice repos (git ls-tree
-r --name-only), so nothing large is downloaded. <personas>: comma list or 'all'
(every member with a portrait). <standin>: '<persona>:<line>,<line>' for members
with no voice yet. [lines]: own lines to use (default: all greetings/sign-offs or
intro/sign-off/handover lines).

Prints JSON {"draw": [{persona, line, who}], "personas": [{persona, own}]}. A member whose own
lines have audio is drawn from those lines (who = the member); otherwise from the
stand-in lines (who = the stand-in), and their pack keeps pictures only."""
import sys, json, re
from line_text import FACE_LINES

AUDIO = ('m4a', 'mp3', 'wav')
CARD = 'appearance/renders/card_1080x1440.webp'


def kind(p):
    return 'tutors' if p.startswith('tutor_') else 'assistants'


def main(agent_files, voice_files, personas, standin, lines=''):
    A = set(open(agent_files).read().split('\n')); V = set(open(voice_files).read().split('\n'))
    if personas == 'all':
        ps = sorted({m.group(2) for f in A if (m := re.match(rf'lms/team/(tutors|assistants)/CAPS/([a-z]+_\d+)/{CARD}$', f))})
    else:
        ps = [p.strip() for p in personas.split(',') if re.fullmatch(r'(tutor|assistant)_\d+', p.strip())]

    def has_audio(p, line):
        roots = (f'voices/team/{kind(p)}/CAPS/{p}/', f'lms/team/{kind(p)}/CAPS/{p}/')
        return any(r + f'{line}.{e}' in (V if r.startswith('voices') else A) for r in roots for e in AUDIO)

    def own_lines(p):
        if lines:
            return [l.strip() for l in lines.split(',') if l.strip()]
        base = f'lms/team/{kind(p)}/CAPS/{p}/'
        return sorted(f[len(base):-3] for f in A if f.startswith(base) and f.endswith('.md')
                      and f[len(base):].split('/')[0] in FACE_LINES[kind(p)] and f.count('/') == base.count('/') + 1)

    who_s, _, s_lines = standin.partition(':')
    draw, keep = [], []
    for p in ps:
        if f'lms/team/{kind(p)}/CAPS/{p}/{CARD}' not in A:
            print(f'{p}: no portrait, skipped', file=sys.stderr); continue
        voiced = [l for l in own_lines(p) if has_audio(p, l)]
        if voiced:
            draw += [{'persona': p, 'line': l, 'who': p} for l in voiced]
        elif who_s and s_lines:
            draw += [{'persona': p, 'line': l.strip(), 'who': who_s} for l in s_lines.split(',') if l.strip()]
        else:
            print(f'{p}: no voice yet and no stand-in set, skipped', file=sys.stderr); continue
        keep.append({'persona': p, 'own': bool(voiced)})
        print(f'{p}: {"own voice" if voiced else "stand-in, pictures only"}, '
              f'{sum(d["persona"] == p for d in draw)} lines', file=sys.stderr)
    print(json.dumps({'draw': draw, 'personas': keep}, separators=(',', ':')))


if __name__ == '__main__':
    main(*sys.argv[1:])
