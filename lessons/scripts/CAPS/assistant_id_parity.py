#!/usr/bin/env python3
# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Assistant opaque-id parity check — proves the id migration changes no
observable behavior (same spirit as the lesson_slug parity check).

Given TWO team roots — one on the legacy name-keyed assistant layout
(directories thandi/bianca/mandy + v1 roster.json) and one on the opaque-id
layout (assistant_001..003 + v2 roster) — verifies:

  (a) GRADE JOIN — each grade resolves to the same display name and slug
      under both layouts;
  (b) ALIASES — every alias (canonical id, slug, display name, assistant_gNN)
      resolves to exactly one canonical id, identically under both layouts;
  (c) BANNED SPEAKERS — lesson_pipeline.speaker_names() (the R2/R3
      banned-speaker set) is identical under both layouts, and under the
      name-keyed layout matches the legacy directory-basename derivation
      exactly (the pre-migration behavior);
  (d) MANIFESTS — for a sample of manifests: every `bridge` value is
      byte-identical to the git baseline (the field is untouched), and
      wherever `bridge_id` appears it is consistent with `bridge` via the
      alias map. Also exercises lesson_manifest.build_tracks under both
      roots to prove `bridge` still emits its pre-migration value and
      `bridge_id` emits the same canonical id either way.

Usage:
  python3 lessons/scripts/CAPS/assistant_id_parity.py \
      --old-root <team_root_v1> --new-root <team_root_v2> \
      [--baseline-ref origin/main] [--manifest-sample 25]

Exit 0 = full parity; 1 = any check failed. speaker_names()/build_tracks
read TEAM_ROOT at import, so per-root probes run in subprocesses.
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from assistant_registry import ASSISTANT_ID_RE, load_registry

FAILURES = []


def report(ok, label, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILURES.append(label)
    return ok


def probe(team_root, code):
    """Run `code` in a subprocess with TEAM_ROOT set; return parsed JSON."""
    env = dict(os.environ, TEAM_ROOT=str(team_root))
    r = subprocess.run([sys.executable, "-c", code], env=env,
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"probe failed under TEAM_ROOT={team_root}:\n{r.stderr}")
    return json.loads(r.stdout.strip().splitlines()[-1])


SPEAKERS_CODE = f"""
import json, sys
sys.path.insert(0, {str(Path(__file__).parent)!r})
import lesson_pipeline as lp
print(json.dumps(sorted(lp.speaker_names())))
"""

LEGACY_SPEAKERS_CODE = f"""
import json, sys
sys.path.insert(0, {str(Path(__file__).parent)!r})
import lesson_pipeline as lp
names = set()
if lp.TUTORS_DIR.is_dir():
    for d in lp.TUTORS_DIR.iterdir():
        if not d.is_dir():
            continue
        text = lp.load_tutor_card(d.name)
        if not text:
            continue
        dn = lp.persona_display_name(text)
        if dn:
            names.add(dn)
        real = lp.get_field(text, "real_name")
        if real:
            names.add(real.strip())
assistants = lp.ASSISTANTS_DIR
if assistants.is_dir():
    names.update(d.name.capitalize() for d in assistants.iterdir() if d.is_dir())
else:
    names.update(("Mandy", "Bianca"))
print(json.dumps(sorted(n for n in names if len(n) > 2)))
"""

BUILD_TRACKS_CODE = f"""
import json, sys
sys.path.insert(0, {str(Path(__file__).parent)!r})
import lesson_manifest as lm
subtopics = {{"subtopics": [
    {{"ref": "s1", "start_seconds": 0, "end_seconds": 60}},
    {{"ref": "s2", "start_seconds": 60, "end_seconds": 120}}]}}
out = {{}}
for grade in (10, 11, 12):
    tracks = lm.build_tracks(
        subtopics, {{}}, {{}}, {{"id": "tutor_001"}}, {{"id": "tutor_002"}},
        1.0, 120.0, "Topic", 0.0, split_ref="s2", grade=grade)
    br = [t for t in tracks if t["type"] == "break_start"][0]
    out[str(grade)] = {{"bridge": br.get("bridge"), "bridge_id": br.get("bridge_id")}}
print(json.dumps(out))
"""


def check_grade_join(old, new):
    for g in (10, 11, 12):
        oid, nid = old.assistant_for_grade(g), new.assistant_for_grade(g)
        report(oid is not None and oid == nid,
               f"(a) grade {g}: same canonical id under both layouts",
               f"old={oid} new={nid}")
        report(old.display_name(oid) is not None
               and old.display_name(oid) == new.display_name(nid),
               f"(a) grade {g}: same display name",
               f"old={old.display_name(oid)} new={new.display_name(nid)}")
        report(old.slug(oid) is not None and old.slug(oid) == new.slug(nid),
               f"(a) grade {g}: same slug",
               f"old={old.slug(oid)} new={new.slug(nid)}")


def check_aliases(old, new):
    oa, na = old.aliases(), new.aliases()
    report(oa == na, "(b) alias maps identical under both layouts",
           f"{len(oa)} aliases" if oa == na else
           f"only-old={sorted(set(oa) - set(na))} only-new={sorted(set(na) - set(oa))} "
           f"diff={ {k: (oa.get(k), na.get(k)) for k in set(oa) | set(na) if oa.get(k) != na.get(k)} }")
    for reg, label in ((old, "old"), (new, "new")):
        amap = reg.aliases()
        bad = {a: i for a, i in amap.items() if not ASSISTANT_ID_RE.match(i)}
        report(not bad, f"(b) every {label}-layout alias resolves to one "
                        "canonical opaque id", f"{len(amap)} aliases" if not bad else str(bad))
        for aid, info in reg.assistants.items():
            expected = {aid, info["slug"], info["display_name"].lower(),
                        f"assistant_g{info['grade']}"}
            got = {a for a, i in amap.items() if i == aid}
            report(expected <= got,
                   f"(b) {label}: {aid} reachable via id/slug/name/gNN aliases",
                   f"missing={expected - got}" if not expected <= got else
                   ",".join(sorted(got)))


def check_speakers(old_root, new_root):
    s_old = probe(old_root, SPEAKERS_CODE)
    s_new = probe(new_root, SPEAKERS_CODE)
    legacy = probe(old_root, LEGACY_SPEAKERS_CODE)
    report(s_old == s_new, "(c) banned-speaker set identical under both layouts",
           f"{len(s_old)} names" if s_old == s_new else
           f"only-old={sorted(set(s_old) - set(s_new))} only-new={sorted(set(s_new) - set(s_old))}")
    report(s_old == legacy, "(c) name-keyed layout: banned set matches the "
                            "legacy directory-basename derivation exactly",
           f"{len(legacy)} names" if s_old == legacy else
           f"only-legacy={sorted(set(legacy) - set(s_old))} only-now={sorted(set(s_old) - set(legacy))}")


def check_manifests(old, new, old_root, new_root, baseline_ref, sample):
    manifests = sorted(Path("lessons").rglob("manifest.json"))[:sample]
    checked_bridge = 0
    ok_all = True
    for p in manifests:
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except ValueError:
            continue
        base = subprocess.run(
            ["git", "show", f"{baseline_ref}:{p.as_posix()}"],
            capture_output=True, text=True)
        base_bridges = []
        if base.returncode == 0:
            try:
                base_bridges = [t.get("bridge") for t in
                                json.loads(base.stdout).get("tracks", [])
                                if "bridge" in t]
            except ValueError:
                pass
        bridges = [t.get("bridge") for t in data.get("tracks", [])
                   if "bridge" in t]
        if base.returncode == 0 and bridges != base_bridges:
            ok_all = report(False, f"(d) {p}: bridge values changed vs "
                            f"{baseline_ref}", f"{base_bridges} -> {bridges}")
        for t in data.get("tracks", []):
            br, bid = t.get("bridge"), t.get("bridge_id")
            if br is not None or bid is not None:
                checked_bridge += 1
            if bid is not None:
                if not ASSISTANT_ID_RE.match(str(bid)):
                    ok_all = report(False, f"(d) {p}: bridge_id {bid!r} not opaque")
                if br and str(br) != "assistant":
                    for reg, label in ((old, "old"), (new, "new")):
                        if reg.canonical_id(br) != bid:
                            ok_all = report(
                                False, f"(d) {p}: bridge {br!r} inconsistent "
                                f"with bridge_id {bid!r} under {label} alias map")
    report(ok_all, f"(d) sampled {len(manifests)} manifest(s): bridge "
                   "unchanged vs baseline; bridge/bridge_id consistent",
           f"{checked_bridge} bridge-carrying track(s)")
    # Emission probe: build_tracks under both roots.
    e_old = probe(old_root, BUILD_TRACKS_CODE)
    e_new = probe(new_root, BUILD_TRACKS_CODE)
    report(e_old == e_new, "(d) build_tracks emits identical bridge/bridge_id "
                           "under both layouts", json.dumps(e_old))
    for g in ("10", "11", "12"):
        report(e_old[g]["bridge"] == "assistant",
               f"(d) grade {g}: emitted bridge value unchanged "
               "(pre-migration placeholder)", e_old[g]["bridge"])
        report(e_old[g]["bridge_id"] == old.assistant_for_grade(int(g)),
               f"(d) grade {g}: emitted bridge_id is the grade host's "
               "canonical id", str(e_old[g]["bridge_id"]))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--old-root", required=True,
                    help="team root on the name-keyed (v1) layout")
    ap.add_argument("--new-root", required=True,
                    help="team root on the opaque-id (v2) layout")
    ap.add_argument("--baseline-ref", default="origin/main",
                    help="git ref for the untouched-bridge comparison")
    ap.add_argument("--manifest-sample", type=int, default=25)
    args = ap.parse_args()

    old = load_registry(args.old_root)
    new = load_registry(args.new_root)
    print(f"old root: {args.old_root}")
    print(f"new root: {args.new_root}\n")
    check_grade_join(old, new)
    check_aliases(old, new)
    check_speakers(args.old_root, args.new_root)
    check_manifests(old, new, args.old_root, args.new_root,
                    args.baseline_ref, args.manifest_sample)
    print(f"\n{'PARITY OK' if not FAILURES else 'PARITY BROKEN'}: "
          f"{len(FAILURES)} failure(s)")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
