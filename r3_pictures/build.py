#!/usr/bin/env python3
"""Draw the kids-mode (R-3) pictures as SVG files.

    python3 r3_pictures/build.py \\
        --slugs  <agent>/lms/dart/test/r3_pack_picture_slugs.json \\
        --text   <lessons>/r3_picture_text.json \\
        --existing <agent>/lms/dart/templates/assets/r3_pictures \\
        --out    /tmp/r3_pictures_out

Inputs (neither lives in this public repo; see README.md):
  --slugs     the pack picture slugs ({grade: [slug]} or {slug: [grade]})
  --text      the words the pictures print ({"text": {key: words}})
  --existing  a folder (or a text file of slugs) of pictures already drawn;
              those slugs are not written again
Output: one <slug>.svg per new drawing in --out, and with --manifest a JSON
of what was drawn, the alias map (slug -> drawn slug) and the tutor-thing
map. Every SVG goes through the fit pass (draw/fitfix.py) unless --no-fix;
--check also runs the fit and overlap checks and fails on any problem.
"""
import argparse
import importlib
import json
import os
import re
import sys
import xml.dom.minidom

HERE = os.path.dirname(os.path.abspath(__file__))
DRAW = os.path.join(HERE, 'draw')

# The Grade R drawings (already in the app): loaded first so the new
# scenes can reuse their bodies; they are not written.
BASE = 'people props roles animals objects nature scenes_a scenes_b spatial maths misc extra tutor_scenes'.split()
# The Grades 1-3 modules, in build order (later ones reuse earlier ones).
MODULES = ('g_emoji g_letters g_numbers g_shapes g_maths g_text n01 t01 n02 t02 n03 t03 n278 n04 t04 '
           'n05 t05 n06 t06 n07 t07 t08 t09').split()
MAX_BYTES = 6000


def existing_slugs(path):
    if not path:
        return set()
    if os.path.isdir(path):
        return {f[:-4] for f in os.listdir(path) if f.endswith('.svg')}
    with open(path, encoding='utf-8') as f:
        return {ln.strip()[:-4] if ln.strip().endswith('.svg') else ln.strip() for ln in f if ln.strip()}


def build(slugs=None, text=None, out=None, existing=None, modules=None, only=None, fix=True, check=False, log=print, trace=None):
    """Draw; returns a report dict. Imports the drawing modules fresh.
    trace(s) is called with every string the pictures print (for tests)."""
    for m in list(sys.modules):
        if m in BASE or m in MODULES or m in ('lib', 'content', 'font', 'kit', 'mkit', 'sk', 'fitfix', 'numwords'):
            del sys.modules[m]
    if DRAW not in sys.path:
        sys.path.insert(0, DRAW)
    import content
    content.load(slugs, text)
    import lib
    import fitfix
    if trace:
        import font
        _run = font.glyph_run

        def glyph_run(s, track=0):
            trace(s)
            return _run(s, track)
        font.glyph_run = glyph_run
    for m in BASE:
        importlib.import_module(m)
    before = set(lib.ALL)
    lib.ALIAS.clear()
    for m in modules or MODULES:
        importlib.import_module(m)
    skip = existing_slugs(existing)
    new = {k: v for k, v in lib.ALL.items() if k not in before}
    ren = {}
    for slug in list(new):
        nm = re.sub('[^a-z0-9]+', '_', slug).strip('_')
        if nm != slug:
            ren[slug] = nm
            if nm not in new:
                new[nm] = new[slug]
            del new[slug]
    skipped = {s: k for s, k in content.SKIPPED.items()}
    for a, b in ren.items():
        if a in skipped:
            skipped[b] = skipped[a]
    problems, seen, written = [], {}, []
    if out:
        os.makedirs(out, exist_ok=True)
    for slug, body in sorted(new.items()):
        if slug in skip:
            continue
        if slug in skipped:
            continue
        if body in seen:
            lib.ALIAS[slug] = seen[body]
            continue
        seen[body] = slug
        s = lib.svg(body) + '\n'
        if fix:
            s, _ = fitfix.fix(s)
        if out and (only is None or any(slug.startswith(o) for o in only)):
            with open(os.path.join(out, slug + '.svg'), 'w', encoding='utf-8') as f:
                f.write(s)
        written.append(slug)
        try:
            xml.dom.minidom.parseString(s)
        except Exception as e:  # noqa: BLE001
            problems.append(('xml', slug, str(e)))
        if len(s) > MAX_BYTES:
            problems.append(('size', slug, len(s)))
        if check:
            for b in fitfix.check(s):
                problems.append(('fit', slug, b))
            for b in fitfix.overlaps(s):
                problems.append(('overlap', slug, b))
    for a, b in ren.items():
        lib.ALIAS[a] = lib.ALIAS.get(b, b)
    for a in list(lib.ALIAS):
        t = lib.ALIAS[a]
        for _ in range(5):
            t = lib.ALIAS.get(t, t)
        lib.ALIAS[a] = t
    import kit
    tutor = getattr(sys.modules.get('t09'), 'T', {})
    rep = {'drawn': written, 'alias': dict(lib.ALIAS), 'tutor_thing': tutor,
           'needs_text': skipped, 'absent_tables': sorted(content.ABSENT),
           'missing_pictures': dict(kit.MISSING), 'problems': problems}
    log(f'{len(written)} new drawings, {len(lib.ALIAS)} aliases, {len(skipped)} need text')
    for p in problems:
        log(*p)
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--slugs', required=True, help='pack picture slugs JSON (private)')
    ap.add_argument('--text', help='picture words JSON (private); without it, pictures with words are skipped')
    ap.add_argument('--out', required=True, help='folder for the SVG files')
    ap.add_argument('--existing', help='folder or slug list of pictures already drawn (not written again)')
    ap.add_argument('--modules', help='comma list of drawing modules (default: all, in order)')
    ap.add_argument('--only', help='comma list of slug prefixes to write (others are still drawn for reuse)')
    ap.add_argument('--manifest', help='write drawn/alias/tutor_thing/needs_text JSON here')
    ap.add_argument('--no-fix', action='store_true', help='skip the fit pass (draw/fitfix.py)')
    ap.add_argument('--check', action='store_true', help='run the fit and overlap checks on every SVG; fail on any')
    a = ap.parse_args(argv)
    rep = build(a.slugs, a.text, a.out, a.existing, a.modules.split(',') if a.modules else None,
                set(a.only.split(',')) if a.only else None, not a.no_fix, a.check)
    if a.manifest:
        with open(a.manifest, 'w', encoding='utf-8') as f:
            json.dump(rep, f, indent=0, sort_keys=True)
    if rep['needs_text']:
        print('needs text:', len(rep['needs_text']), 'pictures (see --manifest needs_text)')
    if rep['missing_pictures']:
        print('MISSING', sorted(rep['missing_pictures'].items(), key=lambda x: -x[1]))
    fails = {'xml', 'fit', 'overlap'} if a.check else {'xml'}
    return 1 if any(p[0] in fails for p in rep['problems']) else 0


if __name__ == '__main__':
    sys.exit(main())
