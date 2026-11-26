"""Find the files for one team-member line.
  python line_text.py <agent_root> <voice_root> <persona> <line> <out_text>
  python line_text.py --list <agent_root> <persona>
  python line_text.py --portrait <agent_root> <persona>
--list prints the lines that get a face pack: a tutor's greetings and sign-offs,
or an assistant's (host's) intro, sign-off and handover lines.
<line> is '<category>/<NN>' (greetings/01, signoffs/02, acknowledgements/01) or
'samples/sample_line'. Prints '<portrait>\\t<audio>' and writes the spoken text
to <out_text> (never to the log: this repo is public)."""
import sys, os, json, glob


def main(agent, voices, persona, line, out_text):
    kind = 'tutors' if persona.startswith('tutor_') else 'assistants'
    team = os.path.join(agent, 'lms/team', kind, 'CAPS', persona)
    portrait = os.path.join(team, 'appearance/renders/card_1080x1440.webp')
    if line == 'samples/sample_line':
        text = json.load(open(os.path.join(team, 'samples/sample_line.animations.json')))['spoken_text']
    else:
        text = open(os.path.join(team, line + '.md'), encoding='utf-8').read()
    audio = None
    for root in (os.path.join(voices, 'team', kind, 'CAPS', persona), team):
        hits = sorted(glob.glob(os.path.join(root, line + '.*')))
        hits = [h for h in hits if h.rsplit('.', 1)[1] in ('m4a', 'mp3', 'wav')]
        if hits:
            audio = hits[0]; break
    for need, what in ((portrait, 'portrait'), (audio, 'voice audio')):
        if not need or not os.path.exists(need):
            sys.exit(f'{persona} {line}: no {what} found')
    open(out_text, 'w', encoding='utf-8').write(text.strip())
    print(f'{portrait}\t{audio}')


FACE_LINES = {'tutors': ('greetings', 'signoffs'), 'assistants': ('intro', 'signoff', 'handover')}


def list_lines(agent, persona):
    kind = 'tutors' if persona.startswith('tutor_') else 'assistants'
    team = os.path.join(agent, 'lms/team', kind, 'CAPS', persona)
    for cat in FACE_LINES[kind]:
        for f in sorted(glob.glob(os.path.join(team, cat, '*.md'))):
            print(f'{cat}/{os.path.basename(f)[:-3]}')


def portrait(agent, persona):
    kind = 'tutors' if persona.startswith('tutor_') else 'assistants'
    p = os.path.join(agent, 'lms/team', kind, 'CAPS', persona, 'appearance/renders/card_1080x1440.webp')
    if not os.path.exists(p):
        sys.exit(f'{persona}: no portrait found')
    print(p)


if __name__ == '__main__':
    if sys.argv[1] == '--list':
        list_lines(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == '--portrait':
        portrait(sys.argv[2], sys.argv[3])
    else:
        main(*sys.argv[1:6])
