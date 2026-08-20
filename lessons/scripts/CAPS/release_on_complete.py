#!/usr/bin/env python3
# Copyright (c) 2026 RokctAI
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

"""Release-on-folder-complete — the session-tree release path.

The lesson FOLDER is the contract. A session package under
lessons/curriculum/CAPS/<subject>/session/<grade>/<term>/<topic>/<subtopic>/
is COMPLETE when it holds the 9 content files:

    script.md, intro.md, mcq.json, subtopics.json, manim_scene.py,
    assistant_qa_transcript.md, assistant_nervous_script.md,
    comprehension_check.json, reel_clip.json

PLUS audio.mp3 at the same relative path under the AUDIO ROOT (--audio-root;
defaults to the lesson folder itself). When a complete package passes
compliance, this script assembles the ReplaySDK asset triple
(manifest.json / audio.mp3 / animations.json) and publishes it as a GitHub
Release on the AGENT repo (tag `lesson-<slug>`) — released lessons live in
the private agent repo as the shipped-content home; only the backend fetches
release assets, so private asset URLs are fine. No job cards, no manual
approval step: the older card-tree lessons keep their Level 6 batch path
untouched.

AUDIO ACQUISITION (deliberately isolated in acquire_audio): today audio.mp3
is hand-placed under the audio root (the TTS engine is still being chosen).
A future generation step slots into acquire_audio without touching the rest
of the assembly, at which point both derived assets live only in the
release and no audio file needs placing anywhere.

ANIMATIONS belong to the release, not the folder: they are exported from
the package's manim_scene.py at release time, exactly as Level 6 does
(manim_exporter.export_scene + lesson_manifest.align_animations). The scene
is read from --scene-root (defaults to the lesson folder; parameterized so
scene placement can move repos without touching the assembly). Guarded edge
cases only: an animations.json already sitting in the folder is used
verbatim as an override (escape hatch, not the main path), and a package
unexpectedly missing its scene releases with an empty timeline plus a loud
warning.

intro.md is REQUIRED for completeness but not consumed by manifest
assembly: it is the tutor's separate spoken-intro recording (played over
the manifest's topic_display beat), same as on the card path today.

SEGMENT TIMINGS with a pre-placed single audio.mp3:
  * default: subtopic bounds are apportioned across the measured audio
    duration (ffprobe) proportionally to each script segment's narration
    character count;
  * override: an optional timings.json next to audio.mp3 supplies exact
    per-segment bounds in seconds, one entry per script segment in order —
    either [{"start": 0.0, "end": 142.5}, ...] or [[0.0, 142.5], ...].

TUTORS: the roster's subject duo (TEAM_ROOT, agent repo checkout) — expert
leads. A `# Part 2` heading in script.md marks the simplifier's takeover;
the subtopic that starts Part 2 becomes the split ref, gated through the
same two_part_split/resolve_tutor_pair logic the card path uses. A script
with no Part 2 heading releases as a single-voice lesson.

IDEMPOTENT: a package whose release tag already exists on the release repo
is skipped, so re-runs and overlapping triggers never double-publish.

Usage:
  python lessons/scripts/CAPS/release_on_complete.py --dry-run       # scan only
  python lessons/scripts/CAPS/release_on_complete.py --max-releases 5
Exit 0 = clean (including nothing to do); 1 = at least one attempted
release failed (compliance, assembly, or publish error).
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import assistant_registry
import check_mojibake
import lesson_compliance
import lesson_manifest as lm
from lesson_pipeline import CAPS_TYPE_BY_FOLDER, persona_id, subject_duo_for

SESSION_ROOT = Path("lessons/curriculum/CAPS")
RELEASE_REPO = "RokctAI/agent"  # shipped-content home (decision log #50)
LEDGER = Path(".rokct/agent/log/ledger.md")

REQUIRED_FILES = (
    "script.md", "intro.md", "mcq.json", "subtopics.json", "manim_scene.py",
    "assistant_qa_transcript.md", "assistant_nervous_script.md",
    "comprehension_check.json", "reel_clip.json",
)
AUDIO_FILE = "audio.mp3"

SUBJECT_DISPLAY = {
    "maths": "Maths",
    "mathematical_literacy": "Mathematical Literacy",
    "physical_sciences": "Physical Sciences",
    "economics": "Economics",
    "geography": "Geography",
    "accounting": "Accounting",
}

PART2_RE = re.compile(r"^#\s*Part\s*2\b", re.IGNORECASE | re.MULTILINE)
SUBTOPIC_HEADING_RE = re.compile(r"^\s*##\s*Subtopic\s*:", re.IGNORECASE)


class ReleaseError(Exception):
    """A package that should release cannot — reported, run continues."""


# --- discovery + identity ---

def discover_folders(root):
    """Session-package folders under <root>/<subject>/session/..., sorted for
    deterministic scan order. A folder is a session package if it carries a
    subtopics.json (the completeness check happens separately)."""
    return sorted(p.parent for p in root.glob("*/session/*/*/*/*/subtopics.json"))


def audio_path(folder, root, audio_root):
    """Where this package's audio.mp3 must sit: the same relative path under
    the audio root, or the folder itself when no audio root is configured.
    The audio root points at a checkout of the repo audio is dropped in
    (the agent repo, per the shipped-content layout)."""
    if audio_root:
        return Path(audio_root) / folder.relative_to(root) / AUDIO_FILE
    return folder / AUDIO_FILE


def missing_files(folder, root, audio_root):
    """Names still missing before this package is complete."""
    missing = [n for n in REQUIRED_FILES if not (folder / n).is_file()]
    if not audio_path(folder, root, audio_root).is_file():
        missing.append(AUDIO_FILE)
    return missing


def lesson_identity(folder, root):
    """Identity derived from the folder path — the path IS the metadata.
    <root>/<subject>/session/grade<N>/term<N>/<topic-slug>/<subtopic-slug>"""
    rel = folder.relative_to(root).parts
    subject_key, _session, grade_part, term_part, topic_slug, subtopic_slug = rel
    grade = int(re.sub(r"\D", "", grade_part) or 0)
    lesson_id = f"{subject_key}_g{grade}_{topic_slug}_{subtopic_slug}"

    def display(slug):
        return slug.replace("-", " ").title()

    return {
        "subject_key": subject_key,
        "subject": SUBJECT_DISPLAY.get(subject_key,
                                       subject_key.replace("_", " ").title()),
        "type": CAPS_TYPE_BY_FOLDER.get(subject_key, f"lesson.{subject_key}"),
        "grade": grade,
        "term": re.sub(r"\D", "", term_part) or term_part,
        "topic": display(topic_slug),
        "subtopic": display(subtopic_slug),
        # The knowledge-bite join key (decision #52): the leaf directory
        # name IS the session-tree lesson slug the bites index is keyed by
        # — carried verbatim, never re-derived from a display name.
        "lesson_slug": subtopic_slug,
        "id": lesson_id,
        "tag": f"lesson-{lesson_id}",
    }


# --- audio ---

def acquire_audio(src, out_dir):
    """Place audio.mp3 in the out dir and return its measured duration.

    This is the audio-acquisition seam: today it just copies the hand-placed
    audio.mp3 from the audio root (the TTS engine is still being chosen).
    When audio generation moves into CI, the generated source slots in HERE
    and nothing else in the assembly changes."""
    dst = out_dir / AUDIO_FILE
    shutil.copyfile(src, dst)
    return audio_duration_seconds(dst)


def audio_duration_seconds(mp3_path):
    """Measured duration via ffprobe (present wherever ffmpeg is — the same
    package Level 6 already installs for its wav->mp3 encode)."""
    exe = shutil.which("ffprobe")
    if not exe:
        raise ReleaseError("ffprobe not found on PATH (apt-get install ffmpeg)")
    out = subprocess.run(
        [exe, "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(mp3_path)],
        capture_output=True, text=True, check=True).stdout.strip()
    seconds = float(out)
    if seconds <= 0:
        raise ReleaseError(f"{mp3_path}: ffprobe measured no duration")
    return seconds


# --- animations (release-owned, not folder-owned) ---

def build_animations(folder, scene_dir, out_dir, audio_seconds):
    """animations.json for the release: exported from the package's
    manim_scene.py and aligned to the real audio, exactly as Level 6 does.
    Folder override and empty-timeline fallback are guarded edge cases (see
    module docstring). Returns the payload."""
    anim_path = out_dir / "animations.json"
    override = folder / "animations.json"
    if override.is_file():  # escape hatch: use the hand-placed file verbatim
        print(f"  [anim] override: using {override} verbatim")
        shutil.copyfile(override, anim_path)
        return json.loads(anim_path.read_text(encoding="utf-8"))
    scene = scene_dir / "manim_scene.py"
    if scene.is_file():
        from manim_exporter import export_scene
        anim = export_scene(str(scene), str(anim_path))
        anim, _scale, camera_count = lm.align_animations(
            anim, anim_path, audio_seconds)
        print(f"  [anim] exported {len(anim['primitives'])} primitives "
              f"(camera_move inlined x{camera_count})")
        return anim
    # Every session package carries a scene; reaching here means something
    # is off — release an empty timeline (exporter's exact shape, parses in
    # the app, passes R1/R5) but say so loudly.
    print(f"  [warn] {scene} missing — releasing an EMPTY animation timeline")
    anim = {"version": "1", "scene": "",
            "duration_seconds": round(audio_seconds, 2), "primitives": []}
    anim_path.write_text(json.dumps(anim, indent=2), encoding="utf-8")
    return anim


# --- segment timings ---

def load_timings(audio_file, n_segments):
    """Exact per-segment bounds from an optional timings.json next to the
    audio, or None. Accepts [{"start": s, "end": e}, ...] or [[s, e], ...];
    entry count must match the script's segment count."""
    path = audio_file.parent / "timings.json"
    if not path.is_file():
        return None
    data = json.loads(path.read_text(encoding="utf-8"))
    bounds = []
    for entry in data:
        if isinstance(entry, dict):
            bounds.append((float(entry["start"]), float(entry["end"])))
        else:
            s, e = entry
            bounds.append((float(s), float(e)))
    if len(bounds) != n_segments:
        raise ReleaseError(
            f"timings.json has {len(bounds)} entries but the script has "
            f"{n_segments} segments")
    return bounds


def apportion_bounds(segments, audio_seconds):
    """Default bounds: the measured total duration split proportionally to
    each segment's narration character count."""
    weights = [max(len(text), 1) for _idx, text in segments]
    total = float(sum(weights))
    bounds, cursor = [], 0.0
    for w in weights:
        span = audio_seconds * w / total
        bounds.append((round(cursor, 2), round(cursor + span, 2)))
        cursor += span
    if bounds:  # pin the last boundary to the exact audio end
        bounds[-1] = (bounds[-1][0], round(audio_seconds, 2))
    return bounds


# --- break questions ---

SPEAKER_RE = re.compile(r"^\*\*([A-Z][\w ]*):\*\*\s*(.+?)\s*$")


def extract_session_break_questions(transcript_md, limit=lm.MAX_BREAK_QUESTIONS):
    """Student questions for the break board. Session transcripts label the
    turns with the assistant's DISPLAY NAME (e.g. **Thandi:**) instead of
    the card format's **Student:** — transcripts carry names, never opaque
    ids, and the known names come from assistant_registry (roster-backed,
    either team layout). The shared extractor (lm.extract_break_questions)
    accepts both the card labels and the registry display names; this
    wrapper adds one compat fallback — any non-Tutor speaker's turns, for a
    transcript naming a host the roster no longer lists — reduced to their
    question sentences (the board shows the question while the answer is
    spoken from the audio)."""
    questions = lm.extract_break_questions(transcript_md, limit)
    if questions:
        return questions
    assistant_labels = {n.lower()
                        for n in assistant_registry.all_display_names()}
    turns = []
    for line in transcript_md.splitlines():
        m = SPEAKER_RE.match(line.strip())
        if not m or m.group(1).strip().lower() == "tutor":
            continue
        turns.append((m.group(1).strip().lower(), m.group(2)))
    named = [t for t in turns if t[0] in assistant_labels]
    out = []
    for _speaker, raw in (named or turns):
        text = re.sub(r"[*_`]", "", raw).strip()
        sentences = re.findall(r"[^.?!]*\?", text)
        q = " ".join(s.strip() for s in sentences).strip() or text
        if q:
            out.append({"question": q})
        if len(out) >= limit:
            break
    return out


# --- tutors ---

def detect_split_ref(script_md, subtopics):
    """The subtopic ref where the simplifier takes over: the first
    `## Subtopic:` after the `# Part 2` heading. None = single voice."""
    m = PART2_RE.search(script_md)
    if not m:
        return None
    before = script_md[:m.start()]
    count = sum(1 for line in before.splitlines()
                if SUBTOPIC_HEADING_RE.match(line))
    subs = subtopics.get("subtopics", [])
    if 0 < count < len(subs):
        return subs[count].get("ref")
    return None


def resolve_tutors(ident, subtopics, script_md):
    """(first, second, split_ref) via the same roster/duo logic as the card
    path — a minimal card text is synthesized from the path identity so
    lesson_manifest.resolve_tutor_pair/two_part_split run unchanged."""
    duo = subject_duo_for(ident["type"], ident["subject"])
    if not duo:
        raise ReleaseError(
            f"no roster duo for {ident['type']} — is TEAM_ROOT set to the "
            "agent checkout's lms/team?")
    lead_id = persona_id(duo[0][1])  # expert leads (Part 1)
    split_ref = detect_split_ref(script_md, subtopics)
    card_text = (f"type: {ident['type']}\n"
                 f"subject: {ident['subject']}\n"
                 f"tutor: {lead_id}\n")
    if split_ref:
        card_text += f"{lm.SECOND_TUTOR_FIELD}: {split_ref}\n"
    first, second = lm.resolve_tutor_pair(card_text, lead_id)
    split_ref = lm.two_part_split(card_text, subtopics)  # validates the ref
    if second and not split_ref:
        second = None  # never announce a tutor who never speaks
    return first, second, split_ref


# --- checks ---

def check_clean(paths, label):
    """Mojibake + compliance over `paths`; raise ReleaseError on any hit."""
    for p in paths:
        hits = check_mojibake.check_file(p)
        if hits:
            n, line = hits[0]
            raise ReleaseError(f"mojibake in {p}:{n}: {line[:80]}")
    violations, _warnings, _checked = lesson_compliance.run(paths)
    if violations:
        rule, msg = violations[0]
        raise ReleaseError(
            f"{label} compliance: {len(violations)} violation(s), first "
            f"[{rule}] {msg}")


def validate_manifest_replaysdk(manifest_path):
    """Best-effort ReplaySDK ManifestParser validation, same tool Level 6
    invokes. Returns True (passed), False (failed) or None (tool/dart not
    available — skipped, matching Level 6's conditional behavior)."""
    for dart_dir in (Path("agent/replay/dart"), Path(".agent-checkout/replay/dart")):
        tool = dart_dir / "tool" / "validate_manifest.dart"
        if tool.is_file() and shutil.which("dart"):
            r = subprocess.run(
                ["dart", "run", "tool/validate_manifest.dart",
                 str(Path(manifest_path).resolve())],
                cwd=dart_dir, capture_output=True, text=True)
            if r.returncode != 0:
                print(r.stdout + r.stderr)
            return r.returncode == 0
    return None


# --- assembly ---

def assemble(folder, ident, audio_file, scene_dir, out_dir):
    """Build manifest.json / audio.mp3 / animations.json in out_dir from a
    complete package. Mirrors the card path's manifest assembly with the
    identity read from the path and the audio measured, not synthesized."""
    subtopics = json.loads((folder / "subtopics.json").read_text("utf-8"))
    mcq = json.loads((folder / "mcq.json").read_text("utf-8"))
    comprehension = json.loads(
        (folder / "comprehension_check.json").read_text("utf-8"))
    script_md = (folder / "script.md").read_text("utf-8")

    out_dir.mkdir(parents=True, exist_ok=True)
    audio_seconds = acquire_audio(audio_file, out_dir)
    anim = build_animations(folder, scene_dir, out_dir, audio_seconds)

    segments = lm.split_script_into_segments(script_md)
    if not segments:
        raise ReleaseError("script produced no narration segments")
    bounds = load_timings(audio_file, len(segments)) or \
        apportion_bounds(segments, audio_seconds)
    subs = subtopics.get("subtopics", [])
    segment_bounds = bounds if len(bounds) == len(subs) else None
    if segment_bounds is None:
        print(f"  [warn] {len(bounds)} segment(s) vs {len(subs)} subtopics — "
              "falling back to the proportional subtopic stretch")

    first, second, split_ref = resolve_tutors(ident, subtopics, script_md)
    break_questions = (extract_session_break_questions(
        (folder / "assistant_qa_transcript.md").read_text("utf-8"))
        if second else [])

    intended = subs[-1]["end_seconds"] if subs else audio_seconds
    scale = audio_seconds / intended if intended else 1.0
    topic_display_seconds = min(
        (p["time"] for p in anim.get("primitives", [])), default=0.0)

    tracks = lm.build_tracks(
        subtopics, mcq, comprehension, first, second, scale, audio_seconds,
        ident["topic"], topic_display_seconds, split_ref=split_ref,
        break_questions=break_questions, segment_bounds=segment_bounds,
        grade=ident["grade"])

    questions = {q["id"]: q for b in mcq.get("subtopics", [])
                 for q in b.get("questions", []) if q.get("id")}
    cc_bank = {q["id"]: q
               for q in comprehension.get("questions", []) if q.get("id")}

    manifest = {
        "version": "1",
        "session_id": ident["id"],
        "subject": ident["subject"],
        "grade": ident["grade"],
        "topic": ident["topic"],
        # Explicit #52 join key (see lesson_manifest's module docstring):
        # the app's knowledge-bite offer prefers this over re-deriving a
        # slug from subtopic/topic display names. Already-published
        # releases lack it (tags are idempotent-skipped); the app's
        # derived-key fallback covers those until re-released.
        "lesson_slug": ident["lesson_slug"],
        "lesson_number": 1,
        "door_close_seconds": lm.DOOR_CLOSE_SECONDS,
        "scheduled_at": datetime.now(timezone.utc)
                        .replace(microsecond=0).isoformat(),
        "audio": {
            "lesson": "audio.mp3",
            "format": "mp3",
            "duration_seconds": int(round(audio_seconds)),
            "engine": "preplaced",  # provenance; ignored by parser
        },
        "assets": ["animations.json"],
        **({"second_tutor": second} if second else {}),
        "tracks": tracks,
        **({"questions": questions} if questions else {}),
        **({"comprehension_check": cc_bank} if cc_bank else {}),
    }
    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"  [manifest] {len(tracks)} tracks, audio {audio_seconds:.1f}s "
          f"-> {manifest_path}")
    return manifest_path


# --- release ---

def release_exists(tag, repo):
    r = subprocess.run(["gh", "release", "view", tag, "--repo", repo],
                       capture_output=True, text=True)
    return r.returncode == 0


def create_release(tag, repo, ident, out_dir):
    subprocess.run(
        ["gh", "release", "create", tag, "--repo", repo,
         "--title", f"Lesson assets: {ident['id']}",
         "--notes", f"Released on folder complete "
                    f"(manifest/audio/animations) for {ident['id']}.",
         str(out_dir / "manifest.json"), str(out_dir / "audio.mp3"),
         str(out_dir / "animations.json")],
        check=True)


def append_ledger(ident, base_url, run_id):
    """Committed record of what was released — same row format as the other
    levels' ledger entries."""
    theme = (f"{ident['subject']} Grade {ident['grade']}: "
             f"{ident['topic']} - {ident['subtopic']}")
    row = (f"| {ident['id']} | {ident['type']} | {theme} | released | "
           f"release_on_complete | ROC-{run_id} | {base_url}/manifest.json | "
           f"{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} |\n")
    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(row)


# --- main ---

def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(SESSION_ROOT),
                    help="curriculum root to scan")
    ap.add_argument("--audio-root", default="",
                    help="root that holds audio.mp3 at each package's "
                         "relative path (an agent-repo checkout dir); "
                         "empty = the lesson folder itself")
    ap.add_argument("--scene-root", default="",
                    help="root that holds manim_scene.py at each package's "
                         "relative path; empty = the lesson folder itself "
                         "(scenes live in factory today)")
    ap.add_argument("--filter", default="",
                    help="only folders whose path contains this substring")
    ap.add_argument("--max-releases", type=int, default=5,
                    help="stop after releasing this many lessons")
    ap.add_argument("--release-repo", default=RELEASE_REPO,
                    help="owner/repo the GitHub Releases are created on")
    ap.add_argument("--out-root", default=".rokct/tmp/release_on_complete",
                    help="working directory for assembled assets")
    ap.add_argument("--dry-run", action="store_true",
                    help="scan and report what WOULD release; no assembly, "
                         "no gh calls required")
    args = ap.parse_args()

    root = Path(args.root)
    run_id = os.environ.get("GITHUB_RUN_ID", "local")
    have_gh = bool(shutil.which("gh"))

    folders = [f for f in discover_folders(root)
               if not args.filter or args.filter in str(f)]
    print(f"[scan] {len(folders)} session package(s) under {root}"
          f"{' matching ' + repr(args.filter) if args.filter else ''}")
    print(f"[scan] audio root: {args.audio_root or '(lesson folder)'}  "
          f"scene root: {args.scene_root or '(lesson folder)'}")

    complete, incomplete = [], 0
    for folder in folders:
        if missing_files(folder, root, args.audio_root):
            incomplete += 1
        else:
            complete.append(folder)
    print(f"[scan] complete: {len(complete)}  incomplete: {incomplete} "
          f"(complete = {len(REQUIRED_FILES)} content files + {AUDIO_FILE} "
          "under the audio root)")

    if args.dry_run:
        for folder in complete:
            ident = lesson_identity(folder, root)
            if have_gh:
                state = (" [release exists — would skip]"
                         if release_exists(ident["tag"], args.release_repo)
                         else " [would release]")
            else:
                state = " [would release — existence check skipped, no gh]"
            print(f"  {ident['tag']}{state}  <- {folder}")
        if not complete:
            print("[dry-run] nothing would release today.")
        return 0

    if not have_gh:
        print("[error] releasing needs the gh CLI on PATH (use --dry-run "
              "for a local scan)")
        return 1

    released, failed = [], []
    for folder in complete:
        if len(released) >= args.max_releases:
            print(f"[stop] reached --max-releases={args.max_releases}")
            break
        ident = lesson_identity(folder, root)
        tag = ident["tag"]
        if release_exists(tag, args.release_repo):
            print(f"[skip] {tag}: release already exists on {args.release_repo}")
            continue
        print(f"[release] {tag} <- {folder}")
        try:
            # Corrupted or non-compliant content must never reach a release:
            # every package file is checked before any asset is built.
            audio_file = audio_path(folder, root, args.audio_root)
            scene_dir = (Path(args.scene_root) / folder.relative_to(root)
                         if args.scene_root else folder)
            check_clean(sorted(p for p in folder.iterdir() if p.is_file()),
                        "package")
            out_dir = Path(args.out_root) / ident["id"]
            shutil.rmtree(out_dir, ignore_errors=True)
            manifest_path = assemble(folder, ident, audio_file, scene_dir,
                                     out_dir)
            check_clean([out_dir / "animations.json", manifest_path],
                        "assembled")
            verdict = validate_manifest_replaysdk(manifest_path)
            if verdict is False:
                raise ReleaseError("manifest failed ManifestParser validation")
            if verdict is None:
                print("  [validate] ReplaySDK validator not available — skipped")
            create_release(tag, args.release_repo, ident, out_dir)
            base = (f"https://github.com/{args.release_repo}"
                    f"/releases/download/{tag}")
            append_ledger(ident, base, run_id)
            released.append(ident["id"])
        except (ReleaseError, subprocess.CalledProcessError,
                FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            print(f"  [fail] {tag}: {e}")
            failed.append(ident["id"])

    print(f"[done] released: {released or 'none'}  failed: {failed or 'none'}")
    gh_output = os.environ.get("GITHUB_OUTPUT")
    if gh_output:
        with open(gh_output, "a", encoding="utf-8") as f:
            f.write(f"released_ids={' '.join(released)}\n")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
