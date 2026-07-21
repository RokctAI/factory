#!/usr/bin/env python3
"""Lesson-compliance checker — the central CI gate for the content standards
established this cycle. FAILS the build (exit 1) on any violation; it does not
warn. Rules, all previously enforced ad hoc and now gated in one place:

  R1 PRIMITIVE VOCABULARY — every emitted primitive `type` in an
     animations.json must be one of the REAL whiteboard vocabulary
     (text/dot/circle/line/rect + camera_move/band_start/clear/fade_out), the
     set whiteboard_canvas.dart + the player actually render. NOT the stale
     replaysdk-spec.md list (mathtex/shape/graph/hand_overlay/transform);
     anything outside the real set is drift and fails.
  R2 NO GREETING/SIGNOFF in script text — greetings, self-introductions,
     handoffs and sign-offs are owned by tutor/assistant assets, never the
     lesson script. Reuses the structural detector from lesson_pipeline
     (roster-driven speaker names + framing shapes), not a phrase list.
  R3 NO BRACKETED STAGE DIRECTIONS in script text — narration is spoken
     verbatim by TTS, so "[adjusts glasses]" / "(points at board)" would be
     read aloud. Same structural detector (action-verb / speaker-named spans).
  R4 OPAQUE IDENTITY IDS ONLY — every tutor id field (persona card `id`, job
     card `tutor`, manifest profile.tutor / second_tutor.id / next_tutor) must
     match ^tutor_\\d+$: a permanent opaque id, never a name/slug. Catches any
     regression to name-derived ids.
     SCOPE NOTE: assistants (Mandy/Bianca) have NOT yet been migrated to
     opaque ids (that is a pending follow-up, parallel to the tutor id work),
     and manifest `bridge` still carries the host NAME per the current
     replaysdk-spec contract. R4 therefore gates TUTOR id fields only today;
     enforcing ^assistant_\\d+$ now would block the established contract.
     Extend ASSISTANT_ID_RE enforcement once assistants get opaque ids.
  R5 CAMERA EVENTS INLINE — camera_move/band_start events must live INSIDE the
     animations.json `primitives` array, never a sibling top-level `camera`
     key. This is the exact contract bug that shipped silently before (the app
     loads only `primitives`); this is its regression gate.

Usage:
  python lessons/scripts/lesson_compliance.py --all        # full-tree baseline
  python lessons/scripts/lesson_compliance.py <files...>    # CI changed-files
Exit 0 = compliant; 1 = one or more violations (printed, grouped by rule).
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lesson_pipeline import verify_no_session_framing  # R2 + R3 detector

# R1: the real render vocabulary. whiteboard_canvas.dart draws
# text/dot/circle/line/rect; the player handles camera_move/band_start (camera)
# and clear/fade_out (removal). Everything else renders as a marker dot = drift.
ALLOWED_PRIMITIVES = {
    "text", "dot", "circle", "line", "rect",
    "camera_move", "band_start", "clear", "fade_out",
}
CAMERA_TYPES = {"camera_move", "band_start"}

# R4: opaque id shapes.
TUTOR_ID_RE = re.compile(r"^tutor_\d+$")
ASSISTANT_ID_RE = re.compile(r"^assistant_\d+$")
# Manifest fields that carry a tutor id.
MANIFEST_TUTOR_ID_FIELDS = ("tutor", "next_tutor")  # profile.tutor, break.next_tutor


def _get_field(text, field):
    m = re.search(rf"^{field}:[ \t]*(.*)", text, re.MULTILINE)
    return m.group(1).split("#")[0].strip() if m else ""


# --- R2 + R3: script text ---

def check_script(path):
    text = Path(path).read_text(encoding="utf-8")
    out = []
    for err in verify_no_session_framing(text):
        # verify_no_session_framing tags stage directions vs session framing;
        # map to R3 vs R2 for the report.
        rule = "R3" if "stage direction" in err else "R2"
        out.append((rule, f"{path}: {err.split(' — ')[0]}"))
    return out


# --- R1 + R5: animations.json ---

def check_animations(path):
    out = []
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:
        return [("R1", f"{path}: not valid JSON: {e}")]
    prims = data.get("primitives", [])
    # R5: no sibling top-level camera array.
    if "camera" in data:
        out.append(("R5", f"{path}: camera events in a sibling top-level "
                          f"'camera' key ({len(data['camera'])}); they must be "
                          "inline camera_move primitives (the app reads only "
                          "'primitives')"))
    # R1: every primitive type in the allowed set.
    for i, p in enumerate(prims):
        t = p.get("primitive")
        if t not in ALLOWED_PRIMITIVES:
            out.append(("R1", f"{path}: primitive[{i}] type {t!r} not in the "
                              f"real whiteboard vocabulary {sorted(ALLOWED_PRIMITIVES)}"))
    # R5 (positive): if the scene pans, camera events must be present inline.
    if not any(p.get("primitive") in CAMERA_TYPES for p in prims):
        bands = {int(float(p.get("position", {}).get("y", 0)))
                 for p in prims if "position" in p}
        if len(bands) > 1:
            out.append(("R5", f"{path}: content spans {len(bands)} bands but no "
                              "inline camera_move/band_start events — the camera "
                              "cannot pan"))
    return out


# --- R4: opaque ids ---

def check_persona_card(path):
    text = Path(path).read_text(encoding="utf-8")
    oid = _get_field(text, "id")
    if not oid:
        return [("R4", f"{path}: persona card has no opaque `id` field")]
    if not TUTOR_ID_RE.match(oid):
        return [("R4", f"{path}: persona id {oid!r} is not an opaque tutor id "
                      "(^tutor_<n>$) — looks name/slug-derived")]
    return []


def check_job_card(path):
    text = Path(path).read_text(encoding="utf-8")
    if not _get_field(text, "type").startswith("lesson."):
        return []
    out = []
    tut = _get_field(text, "tutor")
    if tut and not TUTOR_ID_RE.match(tut):
        out.append(("R4", f"{path}: job card tutor {tut!r} is not an opaque "
                          "tutor id (^tutor_<n>$)"))
    return out


def check_manifest(path):
    out = []
    try:
        m = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:
        return [("R4", f"{path}: not valid JSON: {e}")]
    st = m.get("second_tutor")
    if isinstance(st, dict) and st.get("id") and not TUTOR_ID_RE.match(str(st["id"])):
        out.append(("R4", f"{path}: second_tutor.id {st['id']!r} is not opaque"))
    for tr in m.get("tracks", []):
        for f in MANIFEST_TUTOR_ID_FIELDS:
            v = tr.get(f)
            if v and not TUTOR_ID_RE.match(str(v)):
                out.append(("R4", f"{path}: track {tr.get('type')}.{f} {v!r} "
                                  "is not an opaque tutor id"))
    return out


RULE_TITLES = {
    "R1": "Primitive vocabulary (real whiteboard set only)",
    "R2": "No greeting/self-intro/sign-off in script text",
    "R3": "No bracketed stage directions in script text",
    "R4": "Opaque tutor identity ids only (^tutor_<n>$)",
    "R5": "Camera events inline in primitives (not a sibling key)",
}


def discover():
    """(scripts, animations, manifests, job_cards, persona_cards) in the tree."""
    scripts = sorted(Path("lessons").rglob("script.md"))
    animations = sorted(Path("lessons").rglob("animations.json")) + \
        sorted(Path(".").glob("**/animations.json"))
    manifests = sorted(Path("lessons").rglob("manifest.json"))
    job_cards = [p for p in sorted(Path(".rokct/agent/jobs").rglob("*.md"))
                 if "template" not in p.name]
    persona = sorted(Path("lessons/tutors").glob("*/tutor.md"))
    return scripts, list(dict.fromkeys(animations)), manifests, job_cards, persona


def run(paths):
    violations = []
    checked = {"script": 0, "animations": 0, "manifest": 0, "job_card": 0, "persona": 0}
    for p in paths:
        p = Path(p)
        if not p.is_file():
            continue
        name = p.name
        if name == "script.md":
            violations += check_script(p); checked["script"] += 1
        elif name == "animations.json":
            violations += check_animations(p); checked["animations"] += 1
        elif name == "manifest.json":
            violations += check_manifest(p); checked["manifest"] += 1
        elif p.match(".rokct/agent/jobs/*/*.md") and "template" not in name:
            violations += check_job_card(p); checked["job_card"] += 1
        elif p.parent.parent.name == "tutors" and name == "tutor.md":
            violations += check_persona_card(p); checked["persona"] += 1
    return violations, checked


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    if args == ["--all"]:
        scripts, animations, manifests, job_cards, persona = discover()
        paths = [*scripts, *animations, *manifests, *job_cards, *persona]
    else:
        paths = args

    violations, checked = run(paths)
    print("Lesson compliance —",
          ", ".join(f"{k}:{v}" for k, v in checked.items() if v))
    by_rule = {}
    for rule, msg in violations:
        by_rule.setdefault(rule, []).append(msg)
    for rule in ("R1", "R2", "R3", "R4", "R5"):
        msgs = by_rule.get(rule, [])
        if msgs:
            print(f"\n[{rule}] {RULE_TITLES[rule]} — {len(msgs)} violation(s):")
            for m in msgs[:40]:
                print(f"   {m}")
            if len(msgs) > 40:
                print(f"   ... and {len(msgs) - 40} more")
    if violations:
        print(f"\nFAIL: {len(violations)} compliance violation(s).")
        return 1
    print("\nPASS: all checked files compliant.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
