#!/usr/bin/env python3
# Licensed under the MIT License.
# Copyright 2026 RokctAI
"""Factory-side helpers for the lesson.* job family (Levels 0-4).

Lesson jobs share the factory's job-card state machine (status changes go
through .rokct/skills/agent_delegation/scripts/update_status.py, locks through
lock_job.py) but their card creation, prompt construction, and content checks
live here, in the factory repo, so the book.*/film.* pipeline is untouched.

Content requirements are grounded in agent/replay/docs/supacharge-tech.md
section 4 "Content Production Pipeline":
  - the Prompt Template defines the input fields (Subject, Grade, Topic,
    Subtopic, Example problem, Tutor, Prior knowledge) and the seven items a
    lesson-creation pass must produce;
  - "How A Lesson Is Created" adds comprehension check questions to that list
    and puts a human content-accuracy review (our Level 4) before production.

MCQ / subtopic data shapes match what the shipped Dart consumers parse:
  - McqQuestion.fromJson (agent/lms/dart/.../lesson_models.dart): id,
    question, options[], correct_index, optional time_limit_seconds,
    optional class_stat;
  - subtopic_end TrackEvents carrying a `ref` and an `exercise` MCQ batch
    (agent/lms/dart/templates/routes/lms_route_pages.dart ReplayLessonEngine,
    agent/replay/dart/.../audio_sync.dart).
Level 6 (Manim/VibeVoice production + manifest assembly) is out of scope and
belongs to a future brief; lesson cards stop at status: evaluated.
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

PENDING_DIR = Path(".rokct/agent/jobs/pending")
RUNNING_DIR = Path(".rokct/agent/jobs/running")
DONE_DIR = Path(".rokct/agent/jobs/done")
SEED_PATH = Path("lessons/curriculum/caps_seed.json")
DRAFTS_DIR = Path("lessons/drafts")

TUTOR_GRANDMASTER = "Grandmaster — formal"
TUTOR_BIG_JOHN = "Big John — simplistic, lower grade logic"

CONTENT_FILES = {
    "script_path": "script.md",
    "manim_path": "manim_scene.py",
    "subtopics_path": "subtopics.json",
    "mcq_data_path": "mcq.json",
    "comprehension_check_path": "comprehension_check.json",
    "reel_brief_path": "reel_clip.json",
    "mandy_transcript_path": "mandy_qa_transcript.md",
}


# --- card field helpers (same conventions as the protocol's job_manager) ---

def read_card(path):
    return Path(path).read_text(encoding="utf-8")


def write_card(path, content):
    Path(path).write_text(content, encoding="utf-8")


def get_field(content, field):
    match = re.search(rf"^{field}:[ \t]*(.*)", content, re.MULTILINE)
    return match.group(1).split("#")[0].strip() if match else ""


def set_field(content, field, value):
    if re.search(rf"^{field}:", content, re.MULTILINE):
        return re.sub(rf"^{field}:.*", f"{field}: {value}", content, flags=re.MULTILINE)
    parts = content.rsplit("---", 1)
    return f"{parts[0]}{field}: {value}\n---{parts[1]}"


def set_block_field(content, field, block_text):
    """Replace a frontmatter field (and any indented block) with a YAML
    literal block scalar."""
    lines = content.split("\n")
    start = None
    for i, line in enumerate(lines):
        if re.match(rf"^{field}:", line):
            start = i
            break
    block_lines = [f"{field}: |"] + [f"  {l}" for l in block_text.strip().split("\n")]
    if start is None:
        for i in range(len(lines) - 1, -1, -1):
            if lines[i].strip() == "---":
                return "\n".join(lines[:i] + block_lines + lines[i:])
        return content + "\n" + "\n".join(block_lines)
    end = start + 1
    while end < len(lines) and (lines[end].startswith("  ") or lines[end].strip() == ""):
        if lines[end].strip() == "---":
            break
        end += 1
    return "\n".join(lines[:start] + block_lines + lines[end:])


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "_", str(text).lower()).strip("_")


def entry_hash(entry):
    """Deterministic per-combination hash so reseeding never duplicates."""
    key = f"{entry['type']}|{entry['subject']}|{entry['grade']}|{entry['topic']}|{entry['subtopic']}"
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:6]


def guardrail_for_grade(grade):
    grade = int(grade)
    if grade <= 3:
        return "age_under_6"
    if grade <= 7:
        return "age_6_12"
    return "age_13_17"


# --- Level 0: seed job cards from the CAPS curriculum list ---

def cmd_seed(args):
    if not SEED_PATH.exists():
        print(f"Error: seed file {SEED_PATH} not found.")
        return 1
    seed = json.loads(SEED_PATH.read_text(encoding="utf-8"))
    entries = [e for e in seed.get("entries", []) if e.get("type") == args.type]
    if not entries:
        print(f"No seed entries for type {args.type}.")
        return 0

    PENDING_DIR.mkdir(parents=True, exist_ok=True)
    existing = set()
    for d in (PENDING_DIR, RUNNING_DIR, DONE_DIR):
        if d.exists():
            for f in d.glob("*.md"):
                m = re.search(r"_([0-9a-f]{6})\.md$", f.name)
                if m:
                    existing.add(m.group(1))

    created = 0
    for entry in entries:
        if created >= args.limit:
            break
        h = entry_hash(entry)
        if h in existing:
            continue
        slug = slugify(f"{entry['subject']}_g{entry['grade']}_{entry['topic']}_{entry['subtopic']}")[:60]
        card_id = f"{slug}_{h}"
        theme = f"{entry['subject']} Grade {entry['grade']}: {entry['topic']} - {entry['subtopic']}"
        now = datetime.now()
        card = f"""<!-- CARD RULES
     This card is the source of truth for this job.
     Status field controls pipeline progression.
     All status changes must go through update_status.py.
     Direct edits to status field will be rejected by the state machine.
-->
---
id: {card_id}
theme: {theme}
type: {entry['type']}
subject: {entry['subject']}
grade: {entry['grade']}
topic: {entry['topic']}
subtopic: {entry['subtopic']}
tutor: {entry.get('tutor', '')}
example_problem: {entry.get('example_problem', '')}
prior_knowledge: {entry.get('prior_knowledge', '')}
metarules: .rokct/types/{entry['type']}/metarules
guardrail: {guardrail_for_grade(entry['grade'])}
idea:
idea_status:
concept:
concept_status:
rules_status:
lesson_name:
lesson_path:
script_path:
manim_path:
subtopics_path:
mcq_data_path:
comprehension_check_path:
reel_brief_path:
mandy_transcript_path:
status: theme_generated
created: {now.strftime('%Y-%m-%d')}
last_updated: {now.strftime('%Y-%m-%d')}
session_id:
session_started:
attempts: 0
last_error:
loop_iterations: 0
max_iterations: 10
---
"""
        filename = f"{slug}_{entry['type']}_{h}.md"
        write_card(PENDING_DIR / filename, card)
        print(f"Created lesson job card: {filename}")
        existing.add(h)
        created += 1

    print(f"Seeded {created} lesson card(s) for {args.type}.")
    return 0


# --- prompts (Level 1 tutor/plan capture, Level 2 content generation) ---

def build_level1_prompt(card):
    subject = get_field(card, "subject")
    grade = get_field(card, "grade")
    topic = get_field(card, "topic")
    subtopic = get_field(card, "subtopic")
    tutor = get_field(card, "tutor")
    example = get_field(card, "example_problem")
    prior = get_field(card, "prior_knowledge")

    tutor_line = (
        f"The tutor persona is already fixed: {tutor}. Repeat it verbatim."
        if tutor
        else f"Choose the better-suited tutor persona for this audience: [{TUTOR_GRANDMASTER}] or [{TUTOR_BIG_JOHN}]."
    )
    return f"""You are planning one Supacharge lesson (South African CAPS curriculum).
Subject: {subject}
Grade: {grade}
Topic: {topic}
Subtopic: {subtopic}
{tutor_line}
{"An example problem is already fixed: " + example + ". Repeat it verbatim." if example else "Propose one example problem suited to this grade and subtopic."}
{"Prior knowledge assumptions are already fixed: " + prior + ". Repeat them verbatim." if prior else "State the prior knowledge a student needs before this lesson."}

Reply in exactly this format, nothing else:
TUTOR: <one of: {TUTOR_GRANDMASTER} | {TUTOR_BIG_JOHN}>
EXAMPLE_PROBLEM: <one problem on a single line>
PRIOR_KNOWLEDGE: <one line>
LESSON_ANGLE:
<3-6 lines: how this 15-minute lesson should unfold for this tutor persona — hook, teaching beats, where the example problem lands>"""


def build_level2_prompt(card, card_file):
    """The Jules content-generation prompt.

    The input block and the numbered Produce list are the Prompt Template from
    agent/replay/docs/supacharge-tech.md §4, verbatim, filled with this card's
    values — plus comprehension check questions, which §4's canonical
    "How A Lesson Is Created" output list includes.
    """
    card_id = get_field(card, "id")
    subject = get_field(card, "subject")
    grade = get_field(card, "grade")
    topic = get_field(card, "topic")
    subtopic = get_field(card, "subtopic")
    tutor = get_field(card, "tutor") or TUTOR_GRANDMASTER
    example = get_field(card, "example_problem")
    prior = get_field(card, "prior_knowledge")
    lesson_dir = f"lessons/drafts/{card_id}"

    return f"""TASK: Generate the full content for one Supacharge lesson.

Subject: [{subject}]
Grade: [{grade}]
Topic: [{topic}]
Subtopic: [{subtopic}]
Example problem: [{example}]
Tutor: [{tutor}]
Prior knowledge: [{prior}]

Produce:
1. Lesson script — tutor voice, 15 minutes teaching
2. Manim Python file — whiteboard style, step by step
3. Subtopic markers with timestamps
4. MCQ questions per subtopic (3 to 5, predefined answers)
5. Nervous student Mandy audio script (if needed)
6. TikTok clip script — 60 seconds from best moment
7. Mandy Q&A transcript for post-session
Also produce comprehension check questions (item 5 of the canonical output
list in agent/replay/docs/supacharge-tech.md §4 "How A Lesson Is Created").

Follow the lesson idea already approved on the job card {card_file} (idea
block) and the metarules under .rokct/types/lesson.maths/metarules/.

Write the files into {lesson_dir}/ exactly as follows:
- {lesson_dir}/script.md — the lesson script in the tutor's voice, with a
  '## Subtopic: <title>' heading per subtopic.
- {lesson_dir}/manim_scene.py — Manim Community Python file, whiteboard
  style, one step at a time, mirroring the script's teaching beats.
- {lesson_dir}/subtopics.json — {{"subtopics": [{{"ref": "subtopic_1",
  "title": "...", "start_seconds": 0, "end_seconds": 210}}, ...]}} — refs
  sequential, times in seconds, contiguous, total close to 900 (15 minutes).
- {lesson_dir}/mcq.json — {{"subtopics": [{{"ref": "subtopic_1", "title":
  "...", "questions": [{{"id": "subtopic_1_q1", "question": "...",
  "options": ["...", "...", "...", "..."], "correct_index": 0,
  "time_limit_seconds": 30}}, ...]}}]}} — 3 to 5 questions per subtopic,
  refs matching subtopics.json, correct_index 0-based. These keys are a
  contract with the shipped app (McqQuestion.fromJson in lms_sdk); do not
  rename them.
- {lesson_dir}/comprehension_check.json — {{"questions": [{{"id": "cc1",
  "question": "...", "expected_answer": "..."}}, ...]}} — end-of-lesson
  comprehension check.
- {lesson_dir}/mandy_nervous_script.md — only if needed: short reassurance
  script Mandy can speak to a nervous student for this subtopic.
- {lesson_dir}/reel_clip.json — the 60-second TikTok clip script, JSON only,
  schema: {{"element_type": "lesson_reel", "lesson_id": "{card_id}",
  "lesson_title": "...", "hook_text": "...", "hook_source_file":
  "script.md", "clip_script": "...", "visual_style": "...", "mood": "...",
  "pacing": "...", "call_to_action": "...", "platform": "tiktok",
  "duration_seconds": 60, "guardrail_applied": "{get_field(card, 'guardrail')}"}}.
  Pick the single best moment of the lesson, same hook discipline as the
  factory's book reel briefs.
- {lesson_dir}/mandy_qa_transcript.md — Mandy post-session Q&A transcript:
  likely student questions on this subtopic with Mandy's answers.

Then update the job card {card_file}:
- fill lesson_name (short human title) and lesson_path ({lesson_dir}),
- fill script_path, manim_path, subtopics_path, mcq_data_path,
  comprehension_check_path, reel_brief_path, mandy_transcript_path with the
  paths above,
- write a 'concept: |' block summarising the teaching approach (angle,
  pacing, where the example problem lands),
- set status to 'concept_generated'.
Do not modify any other job card, and do not touch books/ or film/."""


def cmd_prompt(args):
    card = read_card(args.file)
    if args.level == 1:
        print(build_level1_prompt(card))
    elif args.level == 2:
        print(build_level2_prompt(card, args.file.replace("\\", "/")))
    else:
        print(f"Error: no prompt builder for level {args.level}.")
        return 1
    return 0


# --- Level 1: apply the Groq plan output to the card ---

def cmd_plan(args):
    card = read_card(args.file)
    content = args.content

    def take(tag):
        m = re.search(rf"^{tag}:[ \t]*(.+)$", content, re.MULTILINE)
        return m.group(1).strip() if m else ""

    tutor = take("TUTOR")
    example = take("EXAMPLE_PROBLEM")
    prior = take("PRIOR_KNOWLEDGE")
    angle_match = re.search(r"^LESSON_ANGLE:\s*$(.*)", content, re.MULTILINE | re.DOTALL)
    angle = angle_match.group(1).strip() if angle_match else ""

    if not (tutor and example and prior and angle):
        print("Error: Groq plan output missing one of TUTOR / EXAMPLE_PROBLEM / PRIOR_KNOWLEDGE / LESSON_ANGLE.")
        return 1
    if TUTOR_GRANDMASTER.split(" ")[0].lower() not in tutor.lower() and "john" not in tutor.lower():
        print(f"Error: unrecognised tutor persona: {tutor}")
        return 1

    # Seeded values win; Groq only fills gaps.
    if not get_field(card, "tutor"):
        card = set_field(card, "tutor", tutor)
    if not get_field(card, "example_problem"):
        card = set_field(card, "example_problem", example)
    if not get_field(card, "prior_knowledge"):
        card = set_field(card, "prior_knowledge", prior)
    card = set_block_field(card, "idea", angle)
    card = set_field(card, "idea_status", "pending")
    card = set_field(card, "last_updated", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    write_card(args.file, card)
    print(f"Level 1 plan captured on {args.file} (idea_status: pending).")
    return 0


# --- Levels 3/4: content checks and evaluation ---

def _load_json(path, errors, label):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"{label}: cannot parse {path}: {e}")
        return None


def run_checks(card, card_file):
    """Structural + pedagogical sanity checks for Level 3.

    Deliberately modest for v1 (per the task brief): existence and shape of
    the seven §4 content items, MCQ answer-key sanity, subtopic/timestamp
    consistency. Returns (errors, warnings).
    """
    errors, warnings = [], []

    lesson_path = get_field(card, "lesson_path")
    if not lesson_path:
        return ([f"lesson_path not set on {card_file}"], warnings)
    base = Path(lesson_path)
    if not base.exists():
        return ([f"lesson content directory missing: {lesson_path}"], warnings)

    paths = {}
    for field in CONTENT_FILES:
        p = get_field(card, field)
        if not p:
            errors.append(f"card field {field} is empty")
            continue
        if not Path(p).exists():
            errors.append(f"{field} points at a missing file: {p}")
            continue
        paths[field] = Path(p)
    if errors:
        return (errors, warnings)

    # Script: non-trivial, subtopic-structured, in scope for 15 minutes.
    script = paths["script_path"].read_text(encoding="utf-8")
    words = len(script.split())
    if words < 300:
        errors.append(f"script.md too short to be a 15-minute lesson ({words} words)")
    elif words < 900:
        warnings.append(f"script.md is short for 15 minutes of teaching ({words} words)")

    # Manim file: a Community-edition scene.
    manim = paths["manim_path"].read_text(encoding="utf-8")
    if "class" not in manim or "Scene" not in manim:
        errors.append("manim_scene.py does not define a Manim Scene class")

    # Subtopic markers with timestamps.
    subs = _load_json(paths["subtopics_path"], errors, "subtopics")
    mcq = _load_json(paths["mcq_data_path"], errors, "mcq")
    if subs is not None:
        entries = subs.get("subtopics", [])
        if not entries:
            errors.append("subtopics.json has no subtopics")
        prev_end = 0
        refs = []
        for s in entries:
            ref = s.get("ref")
            refs.append(ref)
            if not ref or not s.get("title"):
                errors.append(f"subtopic entry missing ref/title: {s}")
                continue
            try:
                start, end = float(s["start_seconds"]), float(s["end_seconds"])
            except (KeyError, TypeError, ValueError):
                errors.append(f"subtopic {ref}: start_seconds/end_seconds missing or non-numeric")
                continue
            if end <= start:
                errors.append(f"subtopic {ref}: end_seconds <= start_seconds")
            if start < prev_end:
                errors.append(f"subtopic {ref}: overlaps previous subtopic")
            prev_end = end
        if len(refs) != len(set(refs)):
            errors.append("subtopics.json has duplicate refs")
        if entries and not (600 <= prev_end <= 1500):
            warnings.append(f"total lesson duration {prev_end:.0f}s is far from the 15-minute target")

    # MCQ batches: 3-5 predefined-answer questions per subtopic, shaped for
    # McqQuestion.fromJson.
    if mcq is not None and subs is not None:
        sub_refs = {s.get("ref") for s in subs.get("subtopics", [])}
        mcq_refs = set()
        seen_ids = set()
        for batch in mcq.get("subtopics", []):
            ref = batch.get("ref")
            mcq_refs.add(ref)
            questions = batch.get("questions", [])
            if not 3 <= len(questions) <= 5:
                errors.append(f"mcq batch {ref}: {len(questions)} questions (must be 3-5)")
            for q in questions:
                qid = q.get("id")
                if not qid or qid in seen_ids:
                    errors.append(f"mcq {ref}: missing or duplicate question id: {qid}")
                seen_ids.add(qid)
                if not q.get("question"):
                    errors.append(f"mcq {qid}: empty question text")
                options = q.get("options", [])
                if len(options) < 2 or len(options) != len(set(map(str, options))):
                    errors.append(f"mcq {qid}: needs >=2 unique options")
                ci = q.get("correct_index")
                if not isinstance(ci, int) or not 0 <= ci < len(options):
                    errors.append(f"mcq {qid}: correct_index out of range")
                tls = q.get("time_limit_seconds", 30)
                if not isinstance(tls, int) or tls <= 0:
                    errors.append(f"mcq {qid}: invalid time_limit_seconds")
        if mcq_refs != sub_refs:
            errors.append(f"mcq refs {sorted(map(str, mcq_refs))} do not match subtopic refs {sorted(map(str, sub_refs))}")

    # Comprehension check questions.
    cc = _load_json(paths["comprehension_check_path"], errors, "comprehension_check")
    if cc is not None and not cc.get("questions"):
        errors.append("comprehension_check.json has no questions")

    # 60-second reel clip script (level6c reel-brief convention).
    reel = _load_json(paths["reel_brief_path"], errors, "reel_clip")
    if reel is not None:
        if reel.get("duration_seconds") != 60:
            errors.append("reel_clip.json duration_seconds must be 60")
        for key in ("hook_text", "clip_script", "platform"):
            if not reel.get(key):
                errors.append(f"reel_clip.json missing {key}")

    # Mandy post-session Q&A transcript.
    mandy = paths["mandy_transcript_path"].read_text(encoding="utf-8")
    if len(mandy.split()) < 50:
        errors.append("mandy_qa_transcript.md too short to be a usable Q&A transcript")

    return (errors, warnings)


def cmd_check(args):
    card = read_card(args.file)
    errors, warnings = run_checks(card, args.file)
    for w in warnings:
        print(f"WARN: {w}")
    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        card = set_field(card, "rules_status", "failed")
        card = set_field(card, "last_updated", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        write_card(args.file, card)
        return 1
    card = set_field(card, "rules_status", "passed")
    card = set_field(card, "last_updated", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    write_card(args.file, card)
    print(f"Level 3 checks passed for {args.file} ({len(warnings)} warning(s)).")
    return 0


def cmd_evaluate(args):
    """Level 4: final gate. Requires the human content-accuracy approval
    (concept_status: approved — supacharge-tech.md §4 step 3) and re-runs the
    Level 3 checks so nothing regressed between merge and approval."""
    card = read_card(args.file)
    if get_field(card, "concept_status") != "approved":
        print("Error: concept_status is not 'approved' — Level 4 requires the human content-accuracy approval.")
        return 1
    if get_field(card, "rules_status") != "passed":
        print("Error: rules_status is not 'passed' — Level 3 checks must pass first.")
        return 1
    errors, warnings = run_checks(card, args.file)
    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        return 1
    for w in warnings:
        print(f"WARN: {w}")
    print(f"Level 4 evaluation passed for {args.file}: content complete, checks green, human-approved.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Lesson pipeline helpers (Levels 0-4).")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("seed", help="Level 0: create lesson job cards from the CAPS seed list")
    p.add_argument("--type", required=True, help="Lesson type, e.g. lesson.maths")
    p.add_argument("--limit", type=int, default=1, help="Max cards to create this run")

    p = sub.add_parser("prompt", help="Print the agent prompt for a level")
    p.add_argument("--file", required=True)
    p.add_argument("--level", type=int, required=True, choices=[1, 2])

    p = sub.add_parser("plan", help="Level 1: apply Groq plan output to the card")
    p.add_argument("--file", required=True)
    p.add_argument("--content", required=True)

    p = sub.add_parser("check", help="Level 3: run content checks")
    p.add_argument("--file", required=True)

    p = sub.add_parser("evaluate", help="Level 4: final evaluation gate")
    p.add_argument("--file", required=True)

    args = parser.parse_args()
    handlers = {
        "seed": cmd_seed,
        "prompt": cmd_prompt,
        "plan": cmd_plan,
        "check": cmd_check,
        "evaluate": cmd_evaluate,
    }
    if args.command not in handlers:
        parser.print_help()
        sys.exit(1)
    sys.exit(handlers[args.command](args))


if __name__ == "__main__":
    main()
