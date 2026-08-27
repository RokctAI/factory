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

# Licensed under the MIT License.
# Copyright 2026 ROKCT INTELLIGENCE (PTY) LTD
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
import os
import re
import sys
from datetime import datetime
from pathlib import Path

_SCRIPTS_DIR = str(Path(__file__).resolve().parent)
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)
import assistant_registry  # assistant name<->opaque-id mapping (both team layouts)

PENDING_DIR = Path(".rokct/agent/jobs/pending")
RUNNING_DIR = Path(".rokct/agent/jobs/running")
DONE_DIR = Path(".rokct/agent/jobs/done")
# Topic source of truth: the curated DBE ATP syllabus files. caps_seed.json
# is retired - load_seed_entries() flattens these directly, plus the
# hand-curated skill definition files (not derivable from ATPs) under
# CAPS/{subject}/skills/{grade}/{skillname}.json. Syllabus topics link
# skills via an optional requires_skills: [<skill_ref>] field.
CAPS_DIR = Path("lessons/curriculum/CAPS")

CAPS_TYPE_BY_FOLDER = {
    "maths": "lesson.maths",
    "mathematical_literacy": "lesson.maths_literacy",
    "physical_sciences": "lesson.physical_sciences",
    "economics": "lesson.economics",
    "geography": "lesson.geography",
    "accounting": "lesson.accounting",
}

# ATP topics that are pacing entries, not teachable lesson content.
NON_LESSON_TOPIC_RE = re.compile(
    r"(?i)revision|revise|examination|exam\b|control test|controlled test|"
    r"consolidation|assessment|remediation|discussion|admin\b|prior knowledge"
)

# CAPS school terms. "unknown" is for topics that could not be verified
# against a real CAPS/ATP source — never guess a term. Term-independent
# skills topics (e.g. Geography mapwork) are NOT a term value: they carry
# `category: skill` instead (see the Skills convention below) and leave
# term empty.
VALID_TERMS = {"1", "2", "3", "4", "unknown"}

# --- Skills convention ---
# A skill is NOT taught like a lesson (owner decision, 2026-07-27). A lesson
# teaches for the first time: 15-minute arc, seven content items, broadcast-
# schedulable. A skill REFRESHES prerequisite knowledge for a student about
# to start a lesson that requires it, so its content is the review format:
#   diagnostic.json  1-2 skip-ahead check questions (nail them -> go
#                    straight into the lesson)
#   script.md        compressed method recap, SKILL_SCRIPT_MIN/MAX_WORDS -
#                    method only, no first-teaching build-up
#   mcq.json         2-5 exit-check questions (flat list, not per-subtopic)
#   manim_scene.py   optional single scene
# No reel, no assistant Q&A, no comprehension_check, no subtopics segmentation.
# Where a syllabus lesson already teaches the content, the skill definition
# file records it in covered_by (list of {grade, topic, subtopic}) - deep
# review defers to that lesson in the Library instead of re-teaching, which
# also makes per-grade "advanced variant" skills unnecessary: extra depth is
# expressed as a LATER skill in the requires_skills chain, not a variant.
# Skills stay library-only: never a live broadcast slot. Schema:
#   category: skill          on the skill lesson's card (absent = standard,
#                            broadcast-schedulable lesson)
#   skill_ref: <subject>.<slug>   stable reference id on the skill card,
#                            e.g. geography.gradient_calculation — card ids
#                            embed content hashes, skill_ref survives
#                            reseeding and is what everything else points at
#   requires_skills: <ref>[, <ref>]   on any lesson card that needs the
#                            skill first (app side: pre-session assessment
#                            tags a skill-check question; attendance
#                            confirmation offers a non-forcing "review this
#                            skill first?" suggestion)
# Content lives at lessons/<subject>/grade<g>/skills/<id>/ — grade-scoped
# (CAPS assesses the same skill at different depths per grade) but with no
# false term claim. Skill DEFINITIONS live at
# lessons/curriculum/CAPS/{subject}/skills/{grade}/{skillname}.json;
# `lesson_pipeline.py skills-index` validates the graph (the generated
# lessons/skills_index.json artifact is retired).
CATEGORY_SKILL = "skill"

# §4 asks for "15 minutes teaching"; at a spoken pace that is well over a
# thousand words, but scripts interleave whiteboard beats, so 900 is the
# floor below which a script cannot plausibly fill the session.
SCRIPT_MIN_WORDS = 900

TUTOR_GRANDMASTER = "Grandmaster — formal"
TUTOR_BIG_JOHN = "Big John — simplistic, lower grade logic"

# Tutor persona cards (lessons/tutors/): every subject has an Expert +
# Simplifier duo (supacharge-characters.md §1) and the same duo spans all
# grades of a subject. roster.json maps subject -> duo so a different duo
# can be attached per subject later without touching this code. The legacy
# constants above stay as the fallback when the roster is unavailable.
# NOTE: the cards deliberately live under lessons/, NOT .rokct/ — CI
# automation blanket-adds/commits .rokct/ from stale checkouts and silently
# deleted the cards twice when they lived at .rokct/tutors/.
#
# CROSS-REPO: the team data (tutor persona cards, assistant assets, rosters)
# now lives in the RokctAI/agent repo under lms/team/. Set TEAM_ROOT to that
# directory in a checkout (e.g. TEAM_ROOT=.agent-checkout/lms/team) and the
# tutors/assistants resolve to $TEAM_ROOT/tutors/CAPS and
# $TEAM_ROOT/assistants/CAPS. When TEAM_ROOT is unset we fall back to the
# old in-repo layout so nothing breaks for anyone still running it.
_TEAM_ROOT = os.environ.get("TEAM_ROOT", "").strip()
if _TEAM_ROOT:
    TUTORS_DIR = Path(_TEAM_ROOT) / "tutors" / "CAPS"
    ASSISTANTS_DIR = Path(_TEAM_ROOT) / "assistants" / "CAPS"
else:
    TUTORS_DIR = Path("lessons/tutors")
    ASSISTANTS_DIR = Path("lessons/assistants")

CONTENT_FILES = {
    # The tutor's topic intro, recorded as its own segment (owner decision
    # 2026-07-28). A GREETING is persona-only and topic-blind; the INTRO is
    # the same tutor saying what today's lesson is about. Separate files
    # because they are separate recordings: the greeting is assigned per
    # lesson from the tutor's fixed pool, the intro is authored per lesson.
    "intro_path": "intro.md",
    "script_path": "script.md",
    "manim_path": "manim_scene.py",
    "subtopics_path": "subtopics.json",
    "mcq_data_path": "mcq.json",
    "comprehension_check_path": "comprehension_check.json",
    "reel_brief_path": "reel_clip.json",
    "assistant_qa_transcript_path": "assistant_qa_transcript.md",
}

# §4's Prompt Template item 5 is "Nervous student Mandy audio script (if
# needed)" — optional by spec, but when produced it must be tracked on the
# card like every other content item.
OPTIONAL_CONTENT_FILES = {
    "assistant_nervous_script_path": "assistant_nervous_script.md",
}

# Review format for category: skill cards (see the Skills convention above).
SKILL_CONTENT_FILES = {
    "script_path": "script.md",              # method recap
    "diagnostic_path": "diagnostic.json",    # skip-ahead check
    "mcq_data_path": "mcq.json",             # exit check
}
SKILL_OPTIONAL_CONTENT_FILES = {
    "manim_path": "manim_scene.py",
}
# A recap is 2-5 minutes spoken: enough to restate the method and walk the
# worked examples, short enough that it stays a refresher. The MAX is as
# deliberate as the MIN - a skill drifting toward lesson length is being
# authored wrong.
SKILL_SCRIPT_MIN_WORDS = 250
SKILL_SCRIPT_MAX_WORDS = 700


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


# --- paired dual-tutor lessons (docs/paired-dual-tutor-lessons-design.md) ---
#
# A seed row carrying tutors: ["expert", "simplifier"] expands into TWO job
# cards sharing pair_id (= the base entry hash) with pair_role primary /
# secondary. Option B: the secondary NEVER regenerates the Manim scene — its
# Level 2 pass receives the primary's manim_scene.py byte-identical, writes
# its own intro/script/reel in the simplifier's voice, keeps the primary's
# subtopic refs/titles (own timings), and copies mcq.json +
# comprehension_check.json unchanged. Level 3 hard-fails a drifted pair
# (scene hash, example_problem, MCQ ids/correct answers). The primary is
# always the subject's EXPERT in v1; pair_id never reaches the app — the
# app joins the two sessions on topic metadata + different tutor.

PAIR_ROLES = ("primary", "secondary")
# v1 contract: the expert generates the scene, the simplifier reuses it.
PAIR_TUTOR_ROLES = ("expert", "simplifier")


def pair_member_hash(entry, role, tutor_id):
    """Card hash for one member of a paired seed row. The primary keeps the
    base entry hash (so backlog accounting still counts the row as opened);
    the secondary's hash is salted with its role + tutor id so the two cards
    get distinct ids/filenames while sharing pair_id = the base hash."""
    if role == "primary":
        return entry_hash(entry)
    key = (f"{entry['type']}|{entry['subject']}|{entry['grade']}|"
           f"{entry['topic']}|{entry['subtopic']}|{role}|{tutor_id}")
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:6]


def _subtopic_name(sub):
    """Syllabus subtopic entries are plain strings, or objects
    {"name": ..., "tutors": [...]} when a single subtopic is paired."""
    return sub.get("name", "") if isinstance(sub, dict) else sub


def guardrail_for_grade(grade):
    grade = int(grade)
    if grade <= 3:
        return "age_under_6"
    if grade <= 7:
        return "age_6_12"
    return "age_13_17"


def normalize_term(value):
    v = str(value).strip().lower() if value not in (None, "") else "unknown"
    return v if v in VALID_TERMS else "unknown"


def content_dir(subject, grade, term, card_id, category=""):
    """RETIRED (2026-08): the grouped pipeline output tree
    lessons/<subject>/grade<g>/{term<t>|skills}/<card_id>/ (the "junior"
    tree) was deleted — every lesson it held has a senior equivalent in the
    CAPS session tree (lessons/curriculum/CAPS/<subject>/session/...), which
    is authored by direct in-context sessions, not by job-card prompts.

    This function is kept (rather than deleted) so any code path that would
    have written lesson content into the retired layout fails loudly here,
    at the point the path would be minted, instead of silently recreating
    the tree. Working a card-driven lesson again requires deliberately
    choosing a new output convention first.
    """
    raise SystemExit(
        "lesson_pipeline.content_dir: the junior lesson tree "
        "(lessons/<subject>/grade<g>/...) was retired and deleted in 2026-08; "
        "card-driven lesson output has no target layout any more. Lesson "
        "content is authored directly in the CAPS session tree "
        "(lessons/curriculum/CAPS/<subject>/session/...). "
        f"Refusing to mint a path for card {card_id!r} "
        f"({subject} grade {grade} term {term} category {category or 'lesson'})."
    )


def find_duplicate_card(subject, grade, topic, subtopic, tutor=None):
    """Structural duplicate check: an existing card (pending/running/done)
    with the same (subject, grade, topic, subtopic) tuple, regardless of how
    its theme string is worded. Returns the matching card path or None.

    `tutor` (opaque id) makes the check tutor-aware and is passed ONLY when
    seeding a member of a paired row: the pair's two cards intentionally
    share the tuple, so a card carrying a DIFFERENT tutor id is the pair
    sibling, not a duplicate. A tuple match with the same tutor — or with no
    tutor recorded yet (a legacy unpaired card Level 1 has not assigned) —
    still blocks. Callers seeding normal rows omit it: behaviour unchanged."""
    def norm(s):
        return re.sub(r"\s+", " ", str(s)).strip().lower()

    target = (norm(subject), str(grade).strip(), norm(topic), norm(subtopic))
    for d in (PENDING_DIR, RUNNING_DIR, DONE_DIR):
        if not d.exists():
            continue
        for f in d.glob("*.md"):
            if f.name.startswith("template"):
                continue
            card = f.read_text(encoding="utf-8")
            if not get_field(card, "type").startswith("lesson."):
                continue
            existing = (
                norm(get_field(card, "subject")),
                get_field(card, "grade").strip(),
                norm(get_field(card, "topic")),
                norm(get_field(card, "subtopic")),
            )
            if existing == target:
                if tutor is not None:
                    card_tutor = get_field(card, "tutor")
                    if card_tutor and card_tutor != tutor:
                        continue  # pair sibling, not a duplicate
                return f
    return None


# --- Level 0: seed job cards from the CAPS syllabus files ---

def load_caps_skills():
    """Skill definition files: CAPS/{subject}/skills/{grade}/{skillname}.json
    -> {skill_ref: definition dict}. Skills are editorial (prerequisite
    knowledge units), not derivable from the ATPs, so each is its own
    hand-written file."""
    skills = {}
    for folder, lesson_type in sorted(CAPS_TYPE_BY_FOLDER.items()):
        for sf in sorted((CAPS_DIR / folder / "skills").glob("grade*/*.json")):
            data = json.loads(sf.read_text(encoding="utf-8"))
            data["type"] = lesson_type
            data["source"] = sf.as_posix()
            skills[data["skill_ref"]] = data
    return skills


def load_seed_entries():
    """Flatten lessons/curriculum/CAPS/{subject}/syllabus/{grade}.json into
    seed-shaped rows (one per teachable subtopic), then append the skill
    definitions from CAPS/{subject}/skills/. Topics matching
    NON_LESSON_TOPIC_RE or carrying no subtopics are pacing entries, never
    lesson rows. Topic-level requires_skills links pass through to rows.

    Paired dual-tutor rows: a `tutors` field passes through like
    prior_knowledge. Topic-level `tutors` applies to every subtopic of that
    topic; a single subtopic pairs alone by using the object form
    {"name": <subtopic>, "tutors": ["expert", "simplifier"]} (plain-string
    subtopics stay exactly as before)."""
    entries = []
    for folder, lesson_type in sorted(CAPS_TYPE_BY_FOLDER.items()):
        for gf in sorted((CAPS_DIR / folder / "syllabus").glob("grade*.json")):
            data = json.loads(gf.read_text(encoding="utf-8"))
            for term in data.get("terms", []):
                for topic in term.get("topics", []):
                    subs = topic.get("subtopics") or []
                    if not subs or NON_LESSON_TOPIC_RE.search(topic["name"]):
                        continue
                    for sub in subs:
                        row = {
                            "type": lesson_type,
                            "subject": data["subject"],
                            "grade": data["grade"],
                            "term": str(term["term"]),
                            "topic": topic["name"],
                            "subtopic": _subtopic_name(sub),
                            "source": gf.as_posix(),
                        }
                        if topic.get("prior_knowledge"):
                            row["prior_knowledge"] = topic["prior_knowledge"]
                        if topic.get("requires_skills"):
                            row["requires_skills"] = list(topic["requires_skills"])
                        tutors = (sub.get("tutors") if isinstance(sub, dict)
                                  else None) or topic.get("tutors")
                        if tutors:
                            row["tutors"] = list(tutors)
                        entries.append(row)
    for ref, sk in sorted(load_caps_skills().items()):
        row = {
            "type": sk["type"],
            "subject": sk["subject"],
            "grade": sk["grade"],
            "topic": sk.get("topic", "Skills"),
            "subtopic": sk.get("name", ref),
            "category": CATEGORY_SKILL,
            "skill_ref": ref,
            "source": sk["source"],
        }
        for field in ("example_problem", "prior_knowledge", "tutor", "tutor_style",
                       "requires_skills"):
            if sk.get(field):
                row[field] = sk[field]
        entries.append(row)
    return entries


def _stem(w):
    # Light suffix stripping so "completing"/"complete", "equations"/
    # "equation" compare equal in the semantic duplicate guard.
    for suf in ("ing", "es", "ed"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            w = w[: -len(suf)]
            break
    if w.endswith("s") and len(w) > 3:
        w = w[:-1]
    if w.endswith("e") and len(w) > 4:
        w = w[:-1]
    return w


_TOKEN_STOPWORDS = {
    "the", "a", "an", "of", "and", "or", "to", "in", "on", "for", "with",
    "using", "use", "incl", "including", "etc", "vs", "via", "per", "by",
}


def _content_tokens(*parts):
    text = " ".join(str(p) for p in parts).lower()
    return {
        _stem(t)
        for t in re.findall(r"[a-z]+", text)
        if len(t) > 2 and t not in _TOKEN_STOPWORDS
    }


def _fuzzy_covered(entry, card_tokens, tutor=None):
    """True when an existing card's (topic + subtopic) content words overlap
    this entry's enough to call it the same lesson. Cards opened from the
    retired hand-written seed word topics differently from the ATP text, so
    the exact-tuple check alone would re-open them.

    `tutor` (opaque id) is passed ONLY when seeding a member of a paired row:
    the pair sibling overlaps 100% by construction, so an existing card with
    a DIFFERENT tutor id is exempt. Same tutor — or no tutor recorded yet —
    still covers. Normal rows omit it: behaviour unchanged."""
    key = (entry["type"], str(entry["grade"]))
    toks = _content_tokens(entry["topic"], entry["subtopic"])
    if not toks:
        return False
    for old, old_tutor in card_tokens.get(key, []):
        if tutor is not None and old_tutor and old_tutor != tutor:
            continue  # pair sibling territory, not coverage
        inter = len(toks & old)
        union = len(toks | old)
        smaller = min(len(toks), len(old))
        if union and inter / union >= 0.5:
            return True
        if smaller and inter / smaller >= 0.7:
            return True
    return False


def cmd_seed(args):
    if not CAPS_DIR.exists():
        print(f"Error: syllabus directory {CAPS_DIR} not found.")
        return 1
    entries = [e for e in load_seed_entries() if e.get("type") == args.type]
    if getattr(args, "category", None):
        entries = [e for e in entries
                   if str(e.get("category", "")).strip().lower() == args.category.lower()]
    if not entries:
        print(f"No syllabus entries for type {args.type}.")
        return 0

    PENDING_DIR.mkdir(parents=True, exist_ok=True)
    existing = set()
    card_tokens = {}
    pair_roles = {}
    for d in (PENDING_DIR, RUNNING_DIR, DONE_DIR):
        if d.exists():
            for f in d.glob("*.md"):
                m = re.search(r"_([0-9a-f]{6})\.md$", f.name)
                if m:
                    existing.add(m.group(1))
                if f.name.startswith("template"):
                    continue
                card = read_card(f)
                pid = get_field(card, "pair_id")
                if pid:
                    pair_roles.setdefault(pid, set()).add(
                        get_field(card, "pair_role"))
                ctype = get_field(card, "type")
                if ctype.startswith("lesson."):
                    card_tokens.setdefault(
                        (ctype, get_field(card, "grade").strip()), []
                    ).append((
                        _content_tokens(get_field(card, "topic"), get_field(card, "subtopic")),
                        get_field(card, "tutor"),
                    ))

    created = 0
    for entry in entries:
        if created >= args.limit:
            break
        if entry.get("tutors"):
            created += _seed_pair_row(entry, existing, card_tokens, pair_roles)
            continue
        h = entry_hash(entry)
        if h in existing:
            continue
        if _fuzzy_covered(entry, card_tokens):
            print(
                f"SEMANTIC DUPLICATE SKIPPED: ({entry['subject']}, grade {entry['grade']}, "
                f"{entry['topic']}, {entry['subtopic']}) overlaps an existing card"
            )
            continue
        # Structural duplicate check on the (subject, grade, topic, subtopic)
        # tuple — the hash above only dedups identical seed rows; this catches
        # reworded rows and any future non-seed topic source.
        dup = find_duplicate_card(entry["subject"], entry["grade"], entry["topic"], entry["subtopic"])
        if dup:
            print(
                f"DUPLICATE SKIPPED: ({entry['subject']}, grade {entry['grade']}, "
                f"{entry['topic']}, {entry['subtopic']}) already has card {dup.name}"
            )
            continue
        slug = slugify(f"{entry['subject']}_g{entry['grade']}_{entry['topic']}_{entry['subtopic']}")[:60]
        card_id = f"{slug}_{h}"
        theme = f"{entry['subject']} Grade {entry['grade']}: {entry['topic']} - {entry['subtopic']}"
        category = str(entry.get("category", "")).strip().lower()
        skill_ref = str(entry.get("skill_ref", "")).strip()
        requires_skills = entry.get("requires_skills", [])
        # Resolve the seed's tutor to (opaque id, style). A seed row may carry
        # either the split fields (tutor: <id>, tutor_style: <style>) or a
        # legacy 'Name — style' label; either resolves to the id + style via
        # the subject's roster duo, never by re-deriving a slug from a name.
        tutor_id, tutor_style = resolve_seed_tutor(entry)
        # Lessons get an assigned greeting/sign-off variant; skills are
        # reviews (no session framing), so their refs stay empty.
        if category == CATEGORY_SKILL:
            greeting_ref = signoff_ref = ack_ref = ""
        else:
            greeting_ref = assign_tutor_variant(tutor_id, "greetings", h)
            signoff_ref = assign_tutor_variant(tutor_id, "signoffs", h)
            ack_ref = assign_ack_variant(
                tutor_id, h,
                is_expert_tutor(entry.get("type", ""),
                                entry.get("subject", ""), tutor_id))
        if category == CATEGORY_SKILL:
            # Skills are term-independent; a term on a skill row is a
            # contradiction, and a skill without a stable ref is unlinkable.
            if not skill_ref:
                print(f"ERROR: skill seed entry missing skill_ref: {entry['subtopic']}")
                continue
            if str(entry.get("term", "")).strip():
                print(f"ERROR: skill seed entry must not carry a term: {entry['subtopic']}")
                continue
            term = ""
        else:
            term = normalize_term(entry.get("term"))
            if term == "unknown" and str(entry.get("term", "")).strip().lower() not in ("", "unknown"):
                print(f"WARN: seed entry has invalid term {entry.get('term')!r}; recording 'unknown'")
        card = _render_seed_card(entry, card_id, theme, term, category,
                                 skill_ref, requires_skills, tutor_id,
                                 tutor_style, greeting_ref, signoff_ref,
                                 ack_ref)
        filename = f"{slug}_{entry['type']}_{h}.md"
        write_card(PENDING_DIR / filename, card)
        print(f"Created lesson job card: {filename}")
        existing.add(h)
        created += 1

    print(f"Seeded {created} lesson card(s) for {args.type}.")
    return 0


def _render_seed_card(entry, card_id, theme, term, category, skill_ref,
                      requires_skills, tutor_id, tutor_style, greeting_ref,
                      signoff_ref, ack_ref, pair_id="", pair_role=""):
    """The Level 0 job-card template. pair_id/pair_role are empty on every
    card except the two members of a paired dual-tutor row."""
    now = datetime.now()
    return f"""<!-- CARD RULES
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
term: {term}
category: {category}
skill_ref: {skill_ref}
requires_skills: {', '.join(requires_skills)}
topic: {entry['topic']}
subtopic: {entry['subtopic']}
tutor: {tutor_id}
tutor_style: {tutor_style}
pair_id: {pair_id}
pair_role: {pair_role}
greeting_ref: {greeting_ref}
signoff_ref: {signoff_ref}
ack_ref: {ack_ref}
example_problem: {entry.get('example_problem', '')}
prior_knowledge: {entry.get('prior_knowledge', '')}
metarules: .rokct/types/{entry['type']}/metarules
guardrail: {guardrail_for_grade(entry['grade'])}
idea:
idea_status: approved
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
assistant_qa_transcript_path:
assistant_nervous_script_path:
expansion_requested:
crosscheck_status:
crosscheck_notes:
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


def _seed_pair_row(entry, existing, card_tokens, pair_roles):
    """Expand one paired seed row (tutors: ["expert", "simplifier"]) into two
    job cards sharing pair_id, and return how many cards were created.

    v1 contract (docs/paired-dual-tutor-lessons-design.md): the primary is
    ALWAYS the subject's expert — the scene author — and the secondary the
    simplifier; a row ordering them any other way is rejected, never
    reinterpreted. Both cards use the SHARED base hash for greeting/sign-off/
    acknowledgement assignment so the never-both-tutors ack rule keeps
    holding across the pair. Re-running seed fills in a missing member
    without ever duplicating the other."""
    label = (f"({entry['subject']}, grade {entry['grade']}, "
             f"{entry['topic']}, {entry['subtopic']})")
    tutors = [str(t).strip().lower() for t in entry.get("tutors", [])]
    if tutors != list(PAIR_TUTOR_ROLES):
        print(f"ERROR: paired seed row {label} must carry tutors: "
              f"{list(PAIR_TUTOR_ROLES)} exactly (the expert is always the "
              f"primary in v1); got {entry.get('tutors')!r}")
        return 0
    if str(entry.get("category", "")).strip().lower() == CATEGORY_SKILL:
        print(f"ERROR: paired seed row {label} is a skill — pairs are "
              "standard lessons only")
        return 0

    # Both members already on disk (pair_roles is scanned from the existing
    # cards' pair_id/pair_role fields) -> nothing to seed. This must
    # short-circuit BEFORE roster resolution so a re-run without TEAM_ROOT
    # (e.g. CI) stays silent instead of erroring on an unresolvable roster
    # it does not need.
    pair_id = entry_hash(entry)
    if set(PAIR_ROLES) <= pair_roles.get(pair_id, set()):
        return 0

    roster_entry = load_roster().get("subjects", {}).get(
        roster_key_for(entry.get("type", ""), entry.get("subject", "")), {})
    members = []
    for role, roster_role in zip(PAIR_ROLES, PAIR_TUTOR_ROLES):
        tid = roster_entry.get(roster_role, "")
        ptext = load_tutor_card(tid) if tid else ""
        if not (tid and ptext):
            print(f"ERROR: paired seed row {label}: cannot resolve the "
                  f"subject's {roster_role} from the tutor roster "
                  f"({TUTORS_DIR}/roster.json — is TEAM_ROOT set?); a pair "
                  "is never seeded with an unresolved tutor")
            return 0
        members.append((role, tid, persona_style_tag(ptext)))

    term = normalize_term(entry.get("term"))
    if term == "unknown" and str(entry.get("term", "")).strip().lower() not in ("", "unknown"):
        print(f"WARN: seed entry has invalid term {entry.get('term')!r}; recording 'unknown'")
    slug = slugify(f"{entry['subject']}_g{entry['grade']}_{entry['topic']}_{entry['subtopic']}")[:60]
    theme = f"{entry['subject']} Grade {entry['grade']}: {entry['topic']} - {entry['subtopic']}"

    created = 0
    for role, tutor_id, tutor_style in members:
        h = pair_member_hash(entry, role, tutor_id)
        if h in existing:
            continue
        # The duplicate guards run tutor-aware for pair members only: the
        # sibling shares the tuple/tokens by construction and must not block.
        if _fuzzy_covered(entry, card_tokens, tutor=tutor_id):
            print(f"SEMANTIC DUPLICATE SKIPPED: {label} [{role}] overlaps an "
                  "existing card with this tutor")
            continue
        dup = find_duplicate_card(entry["subject"], entry["grade"],
                                  entry["topic"], entry["subtopic"],
                                  tutor=tutor_id)
        if dup:
            print(f"DUPLICATE SKIPPED: {label} [{role}] already has card {dup.name}")
            continue
        # Variant assignment uses the SHARED pair hash: assign_ack_variant's
        # which-of-the-duo derivation only coordinates when both cards feed
        # it the same hash.
        greeting_ref = assign_tutor_variant(tutor_id, "greetings", pair_id)
        signoff_ref = assign_tutor_variant(tutor_id, "signoffs", pair_id)
        ack_ref = assign_ack_variant(tutor_id, pair_id, role == "primary")
        card_id = f"{slug}_{h}"
        card = _render_seed_card(entry, card_id, theme, term, "", "",
                                 entry.get("requires_skills", []), tutor_id,
                                 tutor_style, greeting_ref, signoff_ref,
                                 ack_ref, pair_id=pair_id, pair_role=role)
        filename = f"{slug}_{entry['type']}_{h}.md"
        write_card(PENDING_DIR / filename, card)
        print(f"Created lesson job card: {filename} (pair {pair_id}, {role})")
        existing.add(h)
        created += 1
    return created


# --- tutor persona cards ---
#
# GREETING / SIGN-OFF CONVENTION (owner decisions 2026-07-28)
# Each tutor owns 3 greeting and 3 sign-off variants; every lesson card is
# ASSIGNED one of each (see assign_tutor_variant) so separately recorded
# audio still plays as one continuous session.
# The variants are LESSON-AGNOSTIC by rule - any lesson of that tutor's
# subject must be able to use any variant unchanged. Therefore a variant
# carries NO:
#   * tutor name, real name or title - the assistant introduces the tutor
#     by name, so a greeting that self-introduces would say it twice (and
#     display names are freely renamable behind the opaque tutor ids);
#   * reference to another tutor;
#   * topic, prop, example or grade specific to one lesson;
#   * presumption of the lesson TYPE - no "before you calculate", no
#     ledger columns, no map, no weather. Every subject has theory topics
#     with none of those, and a variant must survive landing on one.
# What a variant DOES carry: that tutor's voice, and subject-level flavour
# only (a tutor's subject never changes).
#
# A GREETING IS NOT AN INTRODUCTION (owner, 2026-07-28). The greeting is
# arrival framing - how this tutor works, nothing about today. Saying what
# today's lesson covers is the INTRO, a separate per-lesson recording
# (intro.md). Never preview content in a variant: the assignment is
# deterministic, but a variant must still read correctly in front of any
# lesson of that subject, as if it had been picked at random.
#
# ONE TUTOR'S TURN IN A SESSION, in order:
#   assistant intro (names the tutor) -> GREETING (pool, topic-blind)
#   -> INTRO (per lesson, topic-aware) -> TEACHING (script.md)
#   -> [assistant five-minute warning; sometimes an ACKNOWLEDGEMENT from the
#      pool, after which the tutor teaches on to the end]
#   -> [FIRST TUTOR ONLY: the Q&A duet - assistant_qa_transcript.md, where
#      the assistant puts the session's questions to the tutor and the tutor
#      answers. The tutor CANNOT sign off before it (owner, 2026-07-28)]
#   -> SIGN-OFF (pool)
# The duo splits this across the break: expert before, simplifier after -
# so the Q&A belongs to the EXPERT's card and never the simplifier's.
# assistant_nervous_script.md sits outside this timeline entirely: it is
# played conditionally by the app when a student needs it, not in sequence.
# The sign-off is ALWAYS the normal one - an interruption never lands there
# (owner correction, 2026-07-28). See assign_ack_variant for the frequency
# and the never-both-tutors rule.
#
# HOW AN INTERRUPTION IS ASSEMBLED (owner, 2026-07-28): the tutor track is
# never recorded with silence for the assistant to speak into. The player
# PAUSES the tutor audio, plays the assistant clip in full, plays the
# acknowledgement if this lesson has one, then RESUMES the tutor track from
# the same instant. So a tutor recording is always one continuous take, and
# an assistant clip's duration costs nothing but a pause - which is also
# why nothing in the lesson script may react to the clock.


def load_roster():
    path = TUTORS_DIR / "roster.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def load_tutor_card(slug):
    # Each tutor is a directory now: lessons/tutors/<slug>/tutor.md holds the
    # persona card, with greetings/ and signoffs/ alongside it (the greeting
    # and sign-off are assistant/tutor-owned assets, NOT lesson-script
    # content). The legacy flat lessons/tutors/<slug>.md is still read as a
    # fallback so nothing breaks mid-migration.
    path = TUTORS_DIR / slug / "tutor.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    legacy = TUTORS_DIR / f"{slug}.md"
    return legacy.read_text(encoding="utf-8") if legacy.exists() else ""


def tutor_asset_dir(slug, kind):
    """Directory of a tutor's in-voice variant assets. kind is 'greetings'
    or 'signoffs'; each holds numbered *.md variants spoken by that tutor."""
    return TUTORS_DIR / slug / kind


def assistant_asset_dir(assistant_id, line):
    """Directory of an assistant's variants for ONE standing line. `line` is
    the line's family/name pair as the manifest names it —
    'timekeeping/five_min_warning', 'intro/new', 'handover/into_break',
    'signoff/session_end' — and the directory holds that line's numbered
    *.md variants, exactly as a tutor's greetings/ holds theirs."""
    return ASSISTANTS_DIR / assistant_id / line


def load_tutor_variants(slug, kind):
    """The in-voice variant texts for a tutor (greetings/signoffs), sorted by
    filename so ordering is deterministic."""
    d = tutor_asset_dir(slug, kind)
    if not d.is_dir():
        return []
    return [p.read_text(encoding="utf-8").strip()
            for p in sorted(d.glob("*.md"))]


def is_expert_tutor(type_str, subject, tutor_id):
    """True when this tutor is the EXPERT half of the subject's duo (the one
    who teaches before the break). Roster lookup by opaque id, never by name
    or style."""
    entry = load_roster().get("subjects", {}).get(
        roster_key_for(type_str, subject), {})
    return bool(tutor_id) and entry.get("expert") == tutor_id


# Roughly one lesson in four has a tutor answer the clock out loud - often
# enough to feel like a real room, rare enough that it never becomes a tic.
ACK_ONE_IN = 4


def assign_ack_variant(tutor_id, h, is_expert):
    """The tutor's reply to the assistant's FIVE-MINUTE WARNING, or '' when
    this tutor doesn't answer it in this lesson (owner decision 2026-07-28).

    The assistant calls the time in every lesson; the tutor only sometimes
    says something back, then teaches on to the end and closes with the
    NORMAL sign-off - an interruption never lands at the sign-off.

    Two structural constraints:
      * RARE - about one lesson in ACK_ONE_IN;
      * NEVER BOTH TUTORS of the same lesson. A lesson is taught by the
        subject's duo (expert before the break, simplifier after) and both
        cards share one entry_hash, so the same hash also decides WHICH of
        the two answers - the other stays silent by construction.
    Only the five-minute warning is ever answered; halfway and wrap-up stay
    the assistant's alone."""
    n = int(h, 16)
    if (n // 13) % ACK_ONE_IN != 0:
        return ""
    if bool((n // 17) % 2) != is_expert:
        return ""
    return assign_tutor_variant(tutor_id, "acknowledgements", h)


def _assign_variant(d, owner_id, kind, h, occurrence=0):
    """The shared variant picker behind assign_tutor_variant and
    assign_assistant_variant: one of the *.md files in `d`, chosen from the
    entry hash so re-seeding never reshuffles, returned as the ref
    '<owner_id>/<kind>/<file>' ('' when the directory holds no variants).

    `occurrence` walks the picked index forward for a line spoken more than
    once in the SAME lesson (the five-minute warning, once per tutor block):
    successive occurrences land on different variants whenever the line has
    more variants than occurrences, so a repeat never sounds like a repeat."""
    files = sorted(d.glob("*.md")) if d.is_dir() else []
    if not files:
        return ""
    n = int(h, 16)
    idx = n % len(files) if kind == "greetings" else (n // 7) % len(files)
    return f"{owner_id}/{kind}/{files[(idx + occurrence) % len(files)].name}"


def assign_tutor_variant(tutor_id, kind, h):
    """Deterministically assign one of a tutor's greeting/sign-off variants
    to a lesson (owner decision 2026-07-28: every lesson carries an ASSIGNED
    greeting_ref + signoff_ref so the separate audio files still flow as one
    session). Derived from the entry hash so re-seeding never reshuffles
    assignments; greeting and sign-off use different derivations so a lesson
    doesn't always pair variant N with variant N. Returns a ref relative to
    lessons/tutors/, e.g. 'tutor_001/greetings/02.md', or '' if the tutor
    has no variants."""
    return _assign_variant(tutor_asset_dir(tutor_id, kind), tutor_id, kind, h)


def assign_assistant_variant(assistant_id, line, h, occurrence=0):
    """The assistant/host counterpart of assign_tutor_variant: which variant
    of one standing line (`line` = 'timekeeping/five_min_warning',
    'intro/new', ...) this lesson uses.

    The host's framing lines repeat far more than a tutor's — the
    five-minute warning alone lands once per tutor block, and every lesson
    of every grade carries the same timekeeping set — so they need the same
    never-a-tic treatment the tutor refs already get (see
    assign_ack_variant). Same picker, same entry hash, same
    never-reshuffled guarantee. Returns '<assistant_id>/<line>/<file>', or
    '' when the line has no variants authored — the caller then keeps the
    single fixed ref, which is the layout in use until the variants are
    written."""
    return _assign_variant(assistant_asset_dir(assistant_id, line),
                           assistant_id, line, h, occurrence)


def roster_key_for(type_str, subject):
    """roster.json subject key from a lesson.* type suffix
    (lesson.maths_literacy -> maths_literacy), falling back to the subject
    name. The subject-name path is a lookup key, NOT a tutor id derivation."""
    if type_str.startswith("lesson."):
        return type_str.split(".", 1)[1]
    return subject.lower().replace(" ", "_")


def card_roster_key(card):
    """roster.json subject key for a job card."""
    return roster_key_for(get_field(card, "type"), get_field(card, "subject"))


def _duo_for_key(key):
    entry = load_roster().get("subjects", {}).get(key, {})
    duo = []
    for role in ("expert", "simplifier"):
        text = load_tutor_card(entry.get(role, ""))
        if text:
            duo.append((entry[role], text))
    return duo


def subject_duo(card):
    """[(slug, persona card text)] for this card's subject, Expert first."""
    return _duo_for_key(card_roster_key(card))


def subject_duo_for(type_str, subject):
    """subject_duo from a raw type/subject (seed rows, before a card exists)."""
    return _duo_for_key(roster_key_for(type_str, subject))


# Tutor identity is carried as separate fields on the persona card and job
# card, never as one conflated "Name — style" string:
#   id           — a PERMANENT ARBITRARY opaque id (tutor_XXX) with zero
#                  relation to any name; the ONLY key code matches/stores on.
#   display_name — the human-readable character name (freely renamable).
#   style        — the short teaching-style descriptor (formal / simplistic).
#   legacy_slug  — the old name-derived slug, kept read-only as a migration
#                  breadcrumb; never matched on, delete once nothing refs it.
# The persona DIRECTORY is still named by the legacy slug (lessons/tutors/
# <slug>/) for readability — that is a file path, not an identity; matching
# is on `id` only.

def persona_id(text):
    """The persona's PERMANENT opaque id (tutor_XXX) — arbitrary, unrelated to
    any name, assigned once. This is the only identity key. `legacy_slug` on
    the card is a read-only migration breadcrumb, never matched on."""
    return get_field(text, "id")


def persona_display_name(text):
    return get_field(text, "display_name") or get_field(text, "pipeline_label").split("—")[0].strip()


def persona_style_tag(text):
    return get_field(text, "style")


def persona_label(text):
    """Human-readable 'DisplayName — style' label, DERIVED from the split
    fields (used for prompts/logs only, never as an identity key)."""
    dn, st = persona_display_name(text), persona_style_tag(text)
    return f"{dn} — {st}" if dn and st else get_field(text, "pipeline_label")


def persona_style(text):
    """The long actionable teaching-philosophy section (for the L1 prompt) —
    distinct from the short `style` descriptor tag above."""
    m = re.search(r"^## Style / teaching philosophy.*?\n(.*?)(?=^## |\Z)",
                  text, re.MULTILINE | re.DOTALL)
    return " ".join(m.group(1).split()) if m else ""


def resolve_seed_tutor(entry):
    """(opaque tutor id, style) for a seed row. Accepts a split row
    (tutor: <tutor_XXX>, tutor_style: <style>) or a legacy 'Name — style'
    label / bare slug in `tutor`; all resolve to the opaque id via the
    subject's roster duo. ('', '') when the row names no tutor. Never derives
    an id from a display name."""
    raw = str(entry.get("tutor", "")).strip()
    if not raw:
        return "", ""
    duo = subject_duo_for(entry.get("type", ""), entry.get("subject", ""))
    slug, ptext = match_persona(duo, raw) if duo else (None, "")
    if slug:
        return persona_id(ptext), str(entry.get("tutor_style", "")).strip() or persona_style_tag(ptext)
    # Unresolvable against a roster (e.g. no duo) — pass the raw value through
    # only if it already looks like a bare id, else keep it for a human to fix.
    return raw, str(entry.get("tutor_style", "")).strip()


def match_persona(duo, tutor):
    """(dir_slug, card text) for the duo member the job card's `tutor` refers
    to. The returned dir_slug is for FILE PATHS only (lessons/tutors/<slug>/);
    identity is the opaque persona_id.

    Matches on the opaque id (tutor_XXX) — exact equality, no name or slug
    derivation. Falls back to the legacy dir-slug or display-name only for
    un-migrated cards. (None, "") when nothing matches."""
    t = (tutor or "").strip()
    for slug, text in duo:                       # opaque id — the real key
        if persona_id(text) and t == persona_id(text):
            return slug, text
    for slug, text in duo:                        # legacy: bare dir-slug
        if t == slug or t == get_field(text, "legacy_slug"):
            return slug, text
    low = t.lower()
    for slug, text in duo:                        # legacy 'Name — style'
        name = persona_display_name(text).lower()
        if name and name in low:
            return slug, text
    return None, ""


# --- prompts (Level 1 tutor/plan capture, Level 2 content generation) ---

def build_level1_prompt(card):
    subject = get_field(card, "subject")
    grade = get_field(card, "grade")
    term = get_field(card, "term")
    if get_field(card, "category") == CATEGORY_SKILL:
        term = "term-independent skill (library lesson, taught on demand)"
    topic = get_field(card, "topic")
    subtopic = get_field(card, "subtopic")
    tutor = get_field(card, "tutor")
    example = get_field(card, "example_problem")
    prior = get_field(card, "prior_knowledge")

    duo = subject_duo(card)
    allowed = " | ".join(persona_label(t) for _, t in duo) if duo \
        else f"{TUTOR_GRANDMASTER} | {TUTOR_BIG_JOHN}"

    if tutor:
        tutor_line = f"The tutor persona is already fixed: {tutor}. Repeat it verbatim in the TUTOR line."
    elif duo:
        # Both personas serve every FET grade — the difference is teaching
        # style, not level. Naming the style trade-off per persona (from
        # the card, not a generic blurb) is what stops the model defaulting
        # to the Expert for every Grade 11/12 card.
        options = "\n".join(
            f"- {persona_label(t)} ({get_field(t, 'title')}): {persona_style(t)}"
            for _, t in duo)
        tutor_line = f"""Choose the tutor persona from this subject's duo. Supacharge publishes
lessons in BOTH voices across Grades 10-12 — neither persona is the default,
and both teach every grade:
{options}
Judge THIS subtopic's teaching-style fit only. A Grade 11 or 12 topic with a
strong real-world anchor is a Simplifier lesson; abstraction-heavy formal
precision is an Expert lesson."""
    else:
        # Legacy fallback: roster unavailable — the original Maths duo.
        tutor_line = f"""Choose the tutor persona. Supacharge publishes lessons in BOTH voices across
Grades 10-12 — neither persona is the default, and both teach every grade:
- {TUTOR_GRANDMASTER}: fast reveal, sharp, formula first. Best when the
  subtopic is abstract or procedural and rewards exam-style precision.
- {TUTOR_BIG_JOHN}: slow reveal, messy, real world first. Best when the
  subtopic has a natural everyday anchor (money, movement, weather, prices,
  maps) or commonly confuses students on first contact — he builds intuition
  with concrete pictures before any symbols.
Judge THIS subtopic's teaching-style fit only. A Grade 11 or 12 topic with a
strong real-world anchor is a Big John lesson; abstraction-heavy symbol
manipulation is a Grandmaster lesson."""
    return f"""You are planning one Supacharge lesson (South African CAPS curriculum).
Subject: {subject}
Grade: {grade}
Term: {term}
Topic: {topic}
Subtopic: {subtopic}
{tutor_line}
{"An example problem is already fixed: " + example + ". Repeat it verbatim." if example else "Propose one example problem suited to this grade and subtopic."}
{"Prior knowledge assumptions are already fixed: " + prior + ". Repeat them verbatim." if prior else "State the prior knowledge a student needs before this lesson."}

Reply in exactly this format, nothing else:
TUTOR: <exactly one of: {allowed}>
TUTOR_REASON: <one line: why this persona's teaching style fits this subtopic>
EXAMPLE_PROBLEM: <one problem on a single line>
PRIOR_KNOWLEDGE: <one line>
LESSON_ANGLE:
<3-6 lines: how this 15-minute lesson should unfold for this tutor persona — hook, teaching beats, where the example problem lands>"""


class PairNotReadyError(RuntimeError):
    """A paired secondary card's Level 2 pass was requested before its
    primary's content exists — the sequencing rule, not a soft warning."""


def find_pair_member(pair_id, role):
    """(path, card text) of the pair member holding `role`, or (None, '')."""
    if not pair_id:
        return None, ""
    for d in (PENDING_DIR, RUNNING_DIR, DONE_DIR):
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name.startswith("template"):
                continue
            c = f.read_text(encoding="utf-8")
            if (get_field(c, "type").startswith("lesson.")
                    and get_field(c, "pair_id") == pair_id
                    and get_field(c, "pair_role") == role):
                return f, c
    return None, ""


def pair_ready(card):
    """(ok, message) — whether lesson2 may run this card. Non-secondary
    cards are always ready; a pair_role: secondary card is ready only once
    its primary's card shows a lesson_path with manim_scene.py present
    (i.e. the primary's concept PR is merged), because the secondary's
    Level 2 pass copies that scene byte-identical instead of regenerating."""
    if get_field(card, "pair_role") != "secondary":
        return True, "not a paired secondary card"
    pair_id = get_field(card, "pair_id")
    if not pair_id:
        return False, "pair_role is secondary but pair_id is empty"
    primary_file, primary = find_pair_member(pair_id, "primary")
    if primary_file is None:
        return False, f"no primary card found for pair {pair_id}"
    lesson_path = get_field(primary, "lesson_path")
    if not lesson_path:
        return False, (f"primary {primary_file.name} has no lesson_path yet "
                       "— its concept PR has not merged")
    scene = Path(lesson_path) / "manim_scene.py"
    if not scene.exists():
        return False, f"primary scene not on disk yet: {scene}"
    return True, f"primary scene present: {scene}"


def cmd_pair_ready(args):
    """Exit 0 when lesson2 may run this card, 1 when a paired secondary must
    keep waiting for its primary's scene."""
    ok, msg = pair_ready(read_card(args.file))
    print(("READY: " if ok else "NOT READY: ") + msg)
    return 0 if ok else 1


def build_level2_prompt(card, card_file):
    """The Jules content-generation prompt.

    The input block and the numbered Produce list are the Prompt Template from
    agent/replay/docs/supacharge-tech.md §4, verbatim, filled with this card's
    values — plus comprehension check questions, which §4's canonical
    "How A Lesson Is Created" output list includes.

    A paired secondary card gets the Option B variant prompt instead: the
    primary's scene is fixed content to copy, never to regenerate. Raises
    PairNotReadyError when the primary's content is not merged yet — the
    lesson2 sequencing rule is enforced here, not just in the workflow.
    """
    if get_field(card, "pair_role") == "secondary":
        return build_level2_secondary_prompt(card, card_file)
    card_id = get_field(card, "id")
    subject = get_field(card, "subject")
    grade = get_field(card, "grade")
    category = get_field(card, "category")
    if category == CATEGORY_SKILL:
        term = "term-independent skill (library lesson, taught on demand)"
    else:
        term = get_field(card, "term") or "unknown"
    topic = get_field(card, "topic")
    subtopic = get_field(card, "subtopic")
    tutor = get_field(card, "tutor") or TUTOR_GRANDMASTER
    example = get_field(card, "example_problem")
    prior = get_field(card, "prior_knowledge")
    lesson_dir = content_dir(subject, grade, get_field(card, "term"), card_id, category)

    # Embed the selected tutor's full persona card so the script reflects
    # the established character instead of Jules re-deriving the voice from
    # the bare tutor label each session.
    slug, persona_card = match_persona(subject_duo(card), tutor)
    persona_block = ""
    if persona_card:
        persona_block = f"""
TUTOR PERSONA CARD (lessons/tutors/{slug}/tutor.md) — every tutor-voiced item
(script, reel clip) must be written in exactly this established character;
do not re-derive or soften the voice:
--- persona card start ---
{persona_card.strip()}
--- persona card end ---
"""

    return f"""TASK: Generate the full content for one Supacharge lesson.

Subject: [{subject}]
Grade: [{grade}]
Term: [{term}]
Topic: [{topic}]
Subtopic: [{subtopic}]
Example problem: [{example}]
Tutor: [{tutor}]
Prior knowledge: [{prior}]
{persona_block}
Produce:
1. Lesson script — tutor voice, 15 minutes teaching
2. Manim Python file — whiteboard style, step by step
3. Subtopic markers with timestamps
4. MCQ questions per subtopic (3 to 5, predefined answers)
5. Nervous-student assistant audio script (if needed; Mandy or Bianca - the lesson's assigned assistant)
6. TikTok clip script — 60 seconds from best moment
7. Assistant Q&A transcript for post-session
Also produce comprehension check questions (item 5 of the canonical output
list in agent/replay/docs/supacharge-tech.md §4 "How A Lesson Is Created").

Follow the lesson idea already approved on the job card {card_file} (idea
block) and the metarules under {get_field(card, 'metarules') or '.rokct/types/' + get_field(card, 'type') + '/metarules'}/.

Write the files into {lesson_dir}/ exactly as follows:
- {lesson_dir}/intro.md — the tutor's spoken topic intro, 2-4 sentences in
  that tutor's register, framing what today's topic is and why it matters.
  This is a SEPARATE RECORDING from the script and from the greeting, and
  it is the only one of the three that knows the topic. It plays while the
  player shows the topic full-screen; the whiteboard starts afterwards (the
  scene's opening wait beat below times this — the two must match). No
  greeting, no self-introduction: the assistant has already named the tutor
  and the tutor's own greeting has already played.

- {lesson_dir}/script.md — the lesson script in the tutor's voice, with a
  '## Subtopic: <title>' heading per subtopic. Opens straight into the
  first subtopic — the framing lives in intro.md above. TEACHING CONTENT
  ONLY.

  Greeting, handover, sign-off and timekeeping content ALREADY EXISTS as
  separate assets and is spoken from them, never from your script:
    * tutor greetings/sign-offs — lessons/tutors/<slug>/greetings/ and
      .../signoffs/ (in-voice variants for every tutor); the card's
      greeting_ref/signoff_ref fields name the ONE assigned variant this
      lesson opens and closes with (assigned at seed time, hash-derived).
      A greeting NEVER mentions the topic — that is intro.md's whole job
    * the tutor's reply to the assistant's five-minute warning —
      lessons/tutors/<slug>/acknowledgements/, named by the card's ack_ref
      when this lesson has one (usually empty). The teaching continues
      normally afterwards, so your script must not react to the clock and
      must not trail off: write it as if the warning never came
    * host intro/handover/sign-off/timekeeping —
      lessons/assistants/mandy/ and lessons/assistants/bianca/
  So the script must contain:
    * NO greeting or welcome, of any wording;
    * NO self-introduction — do not name the tutor speaking, and do not
      name ANY other tutor or host (that is cross-promotion/handoff);
    * NO platform mentions, NO handoffs, NO goodbyes or sign-offs;
    * NO bracketed or parenthetical stage directions and NO physical-action
      description ("[adjusts his glasses]", "(points at the board)") — the
      narration is spoken verbatim by TTS, so a stage direction is read
      aloud to the student. Parentheses carrying maths are fine.
  Topic framing IS wanted: "Today we'll be learning about X" is teaching.

  NEVER LEAVE DEAD AIR FOR ANOTHER SPEAKER. Your recording is continuous;
  when the assistant speaks over a lesson (the five-minute warning, an
  exercise break) the player PAUSES the tutor track for exactly as long as
  the assistant's clip runs and then resumes it — it does not play your
  silence underneath. So: no gaps left for anyone, no [pause] directions,
  and no reacting to a clock your script cannot see. Write it as one
  uninterrupted lesson.

  Question lead-ins ARE teaching flow, and the tutor DOES know the
  questions: you are authoring mcq.json in the same pass, so at the end of
  each subtopic that has MCQs write one brief lead-in in the tutor's own
  register that points at what is actually being asked ("Two of these next
  ones are about the sign — watch it carefully"). What the tutor must NEVER
  state or imply is HOW LONG the student gets: no seconds, no "quickly",
  no "you've got a minute". The timer is the player's business
  (time_limit_seconds in mcq.json), and a spoken duration would contradict
  it the moment either changes.
  These rules are enforced at Level 3 by structural pattern checks (not a
  keyword list): a script that breaks them fails the gate.
- {lesson_dir}/manim_scene.py — Manim Community Python file, whiteboard
  style, one step at a time, mirroring the script's teaching beats.
  INTRO BEAT (mandatory): the scene MUST open with self.wait(...) sized to
  roughly 4-5%% of the scene's total duration, BEFORE the first Write —
  this is the topic-display window: the player keeps the topic full-screen
  while the script's spoken intro runs, and the Level 6 assembler measures
  the first primitive's time to publish the topic_display duration. A scene
  that writes to the board at t=0 breaks the topic beat.
  BAND LAYOUT (mandatory): subclass MovingCameraScene and lay content out
  in sequential vertical BANDS along a long virtual canvas — band k is one
  frame-height, shifted DOWN * config.frame_height * k. One band per
  step/worked example; every worked example starts a fresh band. Content
  NEVER overwrites a previous band's space and there is NO FadeOut/Transform
  lifecycle — old work stays on the canvas; at each band transition play
  self.camera.frame.animate.move_to(DOWN * config.frame_height * k) so the
  viewport moves to clean space. Size content large and legible for a
  phone framed full-screen (scale >= 1.1 even for tiny expressions like
  "2 x 2 = ?"; at most ~5 short lines per band). See the two reference
  scenes under lessons/curriculum/CAPS/maths/session/grade11/term1/
  equations-and-inequalities/*/manim_scene.py.
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
- {lesson_dir}/assistant_nervous_script.md — only if needed: short reassurance
  script the lesson's assistant (Mandy or Bianca) can speak to a nervous student for this subtopic. If you
  create this file, you MUST also set the card's assistant_nervous_script_path
  field to its path; if you do not create it, leave the field empty.
- {lesson_dir}/reel_clip.json — the 60-second TikTok clip script, JSON only,
  schema: {{"element_type": "lesson_reel", "lesson_id": "{card_id}",
  "lesson_title": "...", "hook_text": "...", "hook_source_file":
  "script.md", "clip_script": "...", "visual_style": "...", "mood": "...",
  "pacing": "...", "call_to_action": "...", "platform": "tiktok",
  "duration_seconds": 60, "guardrail_applied": "{get_field(card, 'guardrail')}"}}.
  Pick the single best moment of the lesson, same hook discipline as the
  factory's book reel briefs.
- {lesson_dir}/assistant_qa_transcript.md — the Q&A DUET, and only for the
  FIRST tutor of a session (the subject's expert; the simplifier's card must
  not have one). It plays after the teaching and BEFORE the tutor's
  sign-off — the tutor cannot leave with questions outstanding.
  The assistant raises questions that COME UP A LOT at this point in the
  topic. Never write it as though a student asked during this session: the
  session is one-way, nobody can ask, and the shipped player carries the
  same honesty rule (BreakQuestion in lms_sdk).
  3 to 5 exchanges, each shaped exactly like this:

      ### subtopic_2 — Timing differences
      **Assistant:** Why do outstanding cheques still matter if everyone
      pays by EFT now?
      **Tutor:** <the answer, in the same voice as the lesson>

  The '### <ref> — <title>' line names the part of the lesson the question
  belongs to; ref and title must match subtopics.json exactly, because the
  player DISPLAYS that on screen while the assistant reads the question —
  which is why the spoken question can stay short.
  The assistant's question is at most {QA_QUESTION_MAX_WORDS} words: one
  crisp question, not a student's rambling story. Put the context on the
  screen line, never in the speech. The tutor's answer carries the weight.
  CHOOSE ONLY QUESTIONS THAT DO NOT NEED TO BE SEEN (owner, 2026-07-28).
  There is no animation in the Q&A: the question stays on the board and the
  student listens. Screening test before you write an exchange — if
  answering it properly would need the student to WATCH something being
  worked out, do not use that question at all. That is teaching, it costs
  session time, and it belongs in the lesson script or in a skill.
  Good Q&A shapes: why does this rule hold, when does it not apply, what
  changes if a condition flips, what do students most often confuse this
  with. Bad Q&A shapes: "work this one out", "show me how you'd do X".
  So no board work, no "let me show you", no reference to anything drawn.
  Both parts are recorded separately, so: no display names anywhere (use
  the {{tutor}} placeholder if the assistant must address the tutor — names
  are renamable and this audio is not re-cut when they change), no
  greetings, no sign-off, and no duration talk.

Then update the job card {card_file}:
- fill lesson_name (short human title) and lesson_path ({lesson_dir}),
- fill script_path, manim_path, subtopics_path, mcq_data_path,
  comprehension_check_path, reel_brief_path, assistant_qa_transcript_path (and
  assistant_nervous_script_path if produced) with the paths above,
- write a 'concept: |' block summarising the teaching approach (angle,
  pacing, where the example problem lands),
- set status to 'concept_generated'.
Do not modify any other job card, and do not touch books/ or film/."""


def build_level2_secondary_prompt(card, card_file):
    """Option B content generation for a paired SECONDARY card
    (docs/paired-dual-tutor-lessons-design.md): the primary's manim_scene.py
    is embedded as fixed copy-verbatim content, mcq.json and
    comprehension_check.json are copied byte-identical, subtopic refs/titles
    are the primary's (own timings), and only intro/script/reel are authored
    — in the secondary persona. No assistant_qa_transcript.md: the Q&A duet
    belongs to the expert's (primary) card.

    Raises PairNotReadyError when any required primary artifact is missing."""
    ok, msg = pair_ready(card)
    if not ok:
        raise PairNotReadyError(
            f"secondary card {get_field(card, 'id')} cannot run Level 2 yet: {msg}")
    _, primary = find_pair_member(get_field(card, "pair_id"), "primary")
    primary_dir = get_field(primary, "lesson_path")
    scene_path = Path(primary_dir) / "manim_scene.py"
    scene_text = scene_path.read_text(encoding="utf-8")

    missing = [str(Path(primary_dir) / n)
               for n in ("subtopics.json", "mcq.json", "comprehension_check.json")
               if not (Path(primary_dir) / n).exists()]
    if missing:
        raise PairNotReadyError(
            f"secondary card {get_field(card, 'id')} cannot run Level 2 yet: "
            f"primary content incomplete — missing {', '.join(missing)}")
    try:
        primary_subs = json.loads(
            (Path(primary_dir) / "subtopics.json").read_text(encoding="utf-8"))
    except ValueError as e:
        raise PairNotReadyError(
            f"primary subtopics.json unparseable ({e}) — fix the primary first")
    ref_lines = "\n".join(
        f"  - {s.get('ref')}: {s.get('title')}"
        for s in primary_subs.get("subtopics", []))

    card_id = get_field(card, "id")
    subject = get_field(card, "subject")
    grade = get_field(card, "grade")
    term = get_field(card, "term") or "unknown"
    topic = get_field(card, "topic")
    subtopic = get_field(card, "subtopic")
    tutor = get_field(card, "tutor")
    # The example problem is written ONCE and shared by contract — the
    # primary's value is authoritative for both cards.
    example = get_field(primary, "example_problem") or get_field(card, "example_problem")
    prior = get_field(card, "prior_knowledge")
    lesson_dir = content_dir(subject, grade, get_field(card, "term"), card_id,
                             get_field(card, "category"))

    slug, persona_card = match_persona(subject_duo(card), tutor)
    persona_block = ""
    if persona_card:
        persona_block = f"""
TUTOR PERSONA CARD (lessons/tutors/{slug}/tutor.md) — every tutor-voiced item
(intro, script, reel clip) must be written in exactly this established
character; do not re-derive or soften the voice:
--- persona card start ---
{persona_card.strip()}
--- persona card end ---
"""

    return f"""TASK: Generate the SECOND voice of a paired Supacharge lesson.

This card is the pair_role: secondary member of a dual-tutor pair. The
primary (expert) lesson already exists and is the structural source of
truth: same learning objectives, same example problem, same animations,
same questions with the same answers. You author ONLY the simplifier-voiced
audio artifacts around that fixed structure. Do not regenerate, rebalance
or "improve" any of the fixed content — Level 3 hard-fails the pair on any
drift.

Subject: [{subject}]
Grade: [{grade}]
Term: [{term}]
Topic: [{topic}]
Subtopic: [{subtopic}]
Example problem: [{example}]
Tutor: [{tutor}]
Prior knowledge: [{prior}]
{persona_block}
FIXED CONTENT — copy, never edit:

1. {lesson_dir}/manim_scene.py — write the file below BYTE-IDENTICAL (the
   pacing difference comes free at Level 6, which rescales the same
   primitives to this tutor's slower audio; the visuals must not fork):
--- primary scene start ({scene_path}) ---
{scene_text}
--- primary scene end ---

2. {lesson_dir}/mcq.json — copy {primary_dir}/mcq.json byte-identical.
   Same questions, same options, same correct answers — the "same answers"
   requirement is structural, not re-generated.

3. {lesson_dir}/comprehension_check.json — copy
   {primary_dir}/comprehension_check.json byte-identical.

CONTENT TO AUTHOR — in this tutor's own voice:

4. {lesson_dir}/subtopics.json — the SAME refs and titles as the primary,
   in the same order (identical objectives), with YOUR OWN timings sized to
   this tutor's pacing: {{"subtopics": [{{"ref": ..., "title": ...,
   "start_seconds": ..., "end_seconds": ...}}]}} — contiguous, starting at
   0, total close to 900 seconds. The primary's refs and titles are:
{ref_lines}

5. {lesson_dir}/intro.md — the tutor's spoken topic intro, 2-4 sentences in
   this tutor's register, framing what today's topic is and why it matters.
   No greeting, no self-introduction: the assistant has already named the
   tutor and the tutor's own greeting has already played.

6. {lesson_dir}/script.md — the lesson script in this tutor's voice, with a
   '## Subtopic: <title>' heading per subtopic using EXACTLY the titles
   above, teaching the same objectives and the same example problem
   [{example}] with the same mathematics and the same final answers — but
   built this tutor's way (concrete pictures and everyday anchors before
   symbols). It narrates the SAME whiteboard animation, so the teaching
   beats must follow the scene's board steps in order. TEACHING CONTENT
   ONLY, opening straight into the first subtopic. The same hard rules as
   every lesson script apply (Level 3 enforces them structurally):
   * NO greeting, welcome, or self-introduction of any wording;
   * NO naming any tutor or host, NO platform mentions, NO handoffs,
     goodbyes or sign-offs (greeting/sign-off audio already exists as
     assigned tutor assets on this card);
   * NO bracketed/parenthetical stage directions or physical-action
     description — TTS reads narration verbatim (parentheses carrying
     maths are fine);
   * NO dead air, [pause] directions, or reacting to the clock; write one
     uninterrupted lesson;
   * question lead-ins at MCQ subtopic ends ARE wanted, in this tutor's
     register, pointing at what the copied questions actually ask — but
     NEVER state or imply how long the student gets.

7. {lesson_dir}/reel_clip.json — the 60-second TikTok clip script, JSON
   only, same schema as every lesson reel: {{"element_type": "lesson_reel",
   "lesson_id": "{card_id}", "lesson_title": "...", "hook_text": "...",
   "hook_source_file": "script.md", "clip_script": "...", "visual_style":
   "...", "mood": "...", "pacing": "...", "call_to_action": "...",
   "platform": "tiktok", "duration_seconds": 60, "guardrail_applied":
   "{get_field(card, 'guardrail')}"}}. Pick this script's own best moment.

DO NOT create {lesson_dir}/assistant_qa_transcript.md. The Q&A duet belongs
to the FIRST tutor of the session (the expert — the primary card); the
simplifier's card never has one. Leave the card's
assistant_qa_transcript_path field empty.

Then update the job card {card_file}:
- fill lesson_name (short human title) and lesson_path ({lesson_dir}),
- fill script_path, manim_path, subtopics_path, mcq_data_path,
  comprehension_check_path, reel_brief_path with the paths above (leave
  assistant_qa_transcript_path empty),
- set example_problem to exactly [{example}] if it differs — the pair
  shares one example problem by contract,
- write a 'concept: |' block summarising how this voice teaches the shared
  structure (angle, pacing, where the example problem lands),
- set status to 'concept_generated'.
Do not modify the primary's lesson files or card, any other job card, or
books/ or film/."""


def cmd_prompt(args):
    card = read_card(args.file)
    if args.level == 1:
        print(build_level1_prompt(card))
    elif args.level == 2:
        try:
            print(build_level2_prompt(card, args.file.replace("\\", "/")))
        except PairNotReadyError as e:
            print(f"Error: {e}")
            return 1
    elif args.level == 3:
        print(build_expansion_prompt(card, args.file.replace("\\", "/")))
    else:
        print(f"Error: no prompt builder for level {args.level}.")
        return 1
    return 0


def cmd_mark_expansion(args):
    """Record that the single permitted expansion pass has been requested."""
    card = read_card(args.file)
    if get_field(card, "expansion_requested"):
        print("Error: expansion already requested for this card.")
        return 1
    card = set_field(card, "expansion_requested", "1")
    card = set_field(card, "last_updated", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    write_card(args.file, card)
    print(f"Expansion pass recorded on {args.file}.")
    return 0


# --- Level 1: apply the Groq plan output to the card ---

def cmd_plan(args):
    card = read_card(args.file)
    content = args.content

    def take(tag):
        m = re.search(rf"^{tag}:[ \t]*(.+)$", content, re.MULTILINE)
        return m.group(1).strip() if m else ""

    tutor = take("TUTOR")
    tutor_reason = take("TUTOR_REASON")
    example = take("EXAMPLE_PROBLEM")
    prior = take("PRIOR_KNOWLEDGE")
    angle_match = re.search(r"^LESSON_ANGLE:\s*$(.*)", content, re.MULTILINE | re.DOTALL)
    angle = angle_match.group(1).strip() if angle_match else ""
    if tutor_reason:
        angle = f"Tutor choice: {tutor_reason}\n{angle}"

    if not (tutor and example and prior and angle):
        print("Error: Groq plan output missing one of TUTOR / EXAMPLE_PROBLEM / PRIOR_KNOWLEDGE / LESSON_ANGLE.")
        return 1
    duo = subject_duo(card)
    tutor_style = ""
    if duo:
        slug, ptext = match_persona(duo, tutor)
        if not slug:
            valid = " | ".join(persona_label(t) for _, t in duo)
            print(f"Error: tutor persona '{tutor}' is not in this subject's duo ({valid}).")
            return 1
        tutor = persona_id(ptext)            # store the opaque id, not a slug/label
        tutor_style = persona_style_tag(ptext)
    elif TUTOR_GRANDMASTER.split(" ")[0].lower() not in tutor.lower() and "john" not in tutor.lower():
        print(f"Error: unrecognised tutor persona: {tutor}")
        return 1

    # Seeded values win; Groq only fills gaps.
    if not get_field(card, "tutor"):
        card = set_field(card, "tutor", tutor)
    if tutor_style and not get_field(card, "tutor_style"):
        card = set_field(card, "tutor_style", tutor_style)
    if not get_field(card, "example_problem"):
        card = set_field(card, "example_problem", example)
    if not get_field(card, "prior_knowledge"):
        card = set_field(card, "prior_knowledge", prior)
    card = set_block_field(card, "idea", angle)
    # Gate 1 (manual idea approval) retired for lesson cards by owner
    # decision 2026-07-17: lesson ideas flow straight to Level 2. Gates 2
    # (concept approval / Jules PR merge) and 4 (evaluation) remain human.
    # Book/film types keep their gate-1 behaviour — this pipeline is
    # lesson.*-only.
    card = set_field(card, "idea_status", "approved")
    card = set_field(card, "last_updated", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    write_card(args.file, card)
    print(f"Level 1 plan captured on {args.file} (idea_status: approved — gate 1 retired for lessons).")
    return 0


# --- answer-key verification (lightweight, maths-family) ---
#
# Wrong-answer MCQs are a known LLM failure mode. Where a question is simple
# enough to compute programmatically, verify that correct_index points at the
# computed answer and fail Level 3 on any mismatch. Questions outside these
# recognisable forms are skipped, never guessed at:
#   - quadratic ax²+bx+c=0: number of real solutions (discriminant)
#   - quadratic with rational roots: solve, match the option listing them
#   - factored form (px+q)(rx+s)=0 in the question: roots
#   - "factors as" questions: expand each factored option, compare
#   - "expanding (x+a)(x+b)" questions: compare expansion strings
#   - pure-arithmetic "value of <expr>" with all-numeric options

import math
from fractions import Fraction


def _compact(s):
    """Normalise LaTeX/unicode maths text to a compact comparable form."""
    s = str(s)
    s = s.replace("−", "-").replace(" ", " ")
    s = s.replace("$", "").replace("\\", "").replace("{", "").replace("}", "")
    s = re.sub(r"\s+", "", s)
    s = s.replace("x^2", "x²")
    return s


def _num_forms(fr):
    """Textual forms a Fraction may take inside an option string."""
    forms = set()
    if fr.denominator == 1:
        forms.add(str(fr.numerator))
    else:
        forms.add(f"{fr.numerator}/{fr.denominator}")
        dec = fr.numerator / fr.denominator
        if abs(dec - round(dec, 3)) < 1e-12:
            forms.add(repr(round(dec, 3)).rstrip("0").rstrip("."))
    return forms


def _contains_number(text, fr):
    for form in _num_forms(fr):
        # A positive value must not match inside a negative one (the "4"
        # in "-4"), and no form may match inside a longer number/fraction.
        lookbehind = r"(?<![\d./])" if form.startswith("-") else r"(?<![-\d./])"
        if re.search(lookbehind + re.escape(form) + r"(?![\d./])", text):
            return True
    return False


def _coeff(g, default=1):
    if g in ("", "+", None):
        return default
    if g == "-":
        return -default
    return int(g)


def _parse_quadratic(compact):
    m = re.search(r"([+-]?\d*)x²([+-]\d*)x([+-]\d+)", compact)
    if not m:
        return None
    return (_coeff(m.group(1)), _coeff(m.group(2)), int(m.group(3)))


def _parse_factored(compact):
    m = re.search(r"\((\d*)x([+-]\d+)\)\((\d*)x([+-]\d+)\)", compact)
    if not m:
        return None
    return (_coeff(m.group(1)), int(m.group(2)), _coeff(m.group(3)), int(m.group(4)))


def _rational_roots(a, b, c):
    disc = b * b - 4 * a * c
    if disc < 0:
        return None
    s = math.isqrt(disc)
    if s * s != disc:
        return None
    return sorted({Fraction(-b + s, 2 * a), Fraction(-b - s, 2 * a)})


def _match_root_options(options, roots):
    """Indexes of options containing every root (and no spurious extras)."""
    hits = []
    for i, opt in enumerate(options):
        c = _compact(opt)
        if all(_contains_number(c, r) for r in roots):
            hits.append(i)
    return hits


def _expected_index(question, options):
    """Return (index, how) when the answer is computable, else None."""
    q = _compact(question)
    opts = [_compact(o) for o in options]

    # "How many (real) solutions/roots does ax²+bx+c=0 have?"
    if re.search(r"howmany(real)?(solutions|roots)", q, re.IGNORECASE):
        quad = _parse_quadratic(q)
        if quad:
            a, b, c = quad
            disc = b * b - 4 * a * c
            n = 2 if disc > 0 else (1 if disc == 0 else 0)
            words = {0: ("0", "none", "zero"), 1: ("1", "one"), 2: ("2", "two")}[n]
            hits = [i for i, o in enumerate(opts) if o.lower() in words]
            if len(hits) == 1:
                return hits[0], f"discriminant={disc} -> {n} solutions"
        return None

    # "factors as" -> expand each factored option, compare to the quadratic
    if "factorsas" in q.replace(" ", "").lower() or "factorises" in q.lower() or "factorizes" in q.lower():
        quad = _parse_quadratic(q)
        if quad:
            hits = []
            for i, o in enumerate(opts):
                f = _parse_factored(o)
                if f and (f[0] * f[2], f[0] * f[3] + f[1] * f[2], f[1] * f[3]) == quad:
                    hits.append(i)
            if len(hits) == 1:
                return hits[0], "expanded factored options"
        return None

    # "expanding (px+q)(rx+s)" -> compose the product string
    if "expand" in q.lower():
        f = _parse_factored(q)
        if f:
            p, qq, r, s = f
            a, b, c = p * r, p * s + qq * r, qq * s
            expected = f"{'' if a == 1 else a}x²{'+' if b >= 0 else ''}{b}x{'+' if c >= 0 else ''}{c}"
            hits = [i for i, o in enumerate(opts) if expected in o]
            if len(hits) == 1:
                return hits[0], f"expansion {expected}"
        return None

    # Roots of a factored equation in the question: (px+q)(rx+s)=0
    f = _parse_factored(q)
    if f and "=0" in q:
        p, qq, r, s = f
        roots = sorted({Fraction(-qq, p), Fraction(-s, r)})
        hits = _match_root_options(options, roots)
        if len(hits) == 1:
            return hits[0], f"roots of factored form: {[str(x) for x in roots]}"
        return None

    # Solve/roots of a standard-form quadratic with rational roots
    if re.search(r"solve|roots|solutions", q, re.IGNORECASE):
        quad = _parse_quadratic(q)
        if quad and "=0" in q:
            roots = _rational_roots(*quad)
            if roots:
                hits = _match_root_options(options, roots)
                if len(hits) == 1:
                    return hits[0], f"quadratic roots: {[str(x) for x in roots]}"
        return None

    # Pure-arithmetic "value of <expr>" with all-numeric options
    m = re.search(r"valueof(.+?)[?？]", q, re.IGNORECASE)
    if m:
        expr = m.group(1).replace("²", "**2").replace("³", "**3")
        expr = expr.replace("×", "*").replace("·", "*").replace("^", "**")
        if re.fullmatch(r"[\d+\-*/(). ]+", expr.replace("**", "*")):
            try:
                value = eval(expr, {"__builtins__": {}}, {})
            except Exception:
                return None
            numeric = []
            for o in opts:
                if re.fullmatch(r"[-+]?\d+(\.\d+)?", o):
                    numeric.append(float(o))
                else:
                    return None
            hits = [i for i, v in enumerate(numeric) if abs(v - value) < 1e-9]
            if len(hits) == 1:
                return hits[0], f"arithmetic: {m.group(1)} = {value}"
    return None


def verify_answer_keys(mcq):
    """Programmatically verify computable MCQ answer keys.

    Returns (errors, verified) — errors on any computed-answer mismatch,
    verified = list of (question_id, how) that were confirmed correct.
    """
    errors, verified = [], []
    for batch in mcq.get("subtopics", []):
        for qn in batch.get("questions", []):
            options = qn.get("options", [])
            ci = qn.get("correct_index")
            if not options or not isinstance(ci, int) or not 0 <= ci < len(options):
                continue  # structural checks report these separately
            result = _expected_index(qn.get("question", ""), options)
            if result is None:
                continue
            idx, how = result
            if idx == ci:
                verified.append((qn.get("id"), how))
            else:
                errors.append(
                    f"answer key mismatch on {qn.get('id')}: computed answer is "
                    f"option {idx} ({options[idx]!r}) but correct_index is {ci} "
                    f"({options[ci]!r}) [{how}]"
                )
    return errors, verified


# --- arithmetic-identity verification (all subjects) ---
#
# The metarules require every worked example to show explicit substitution
# and arithmetic ("Formula. Substitution. Answer."), so lesson text is full
# of fully-numeric statements like "R120 + 450 × R1,85 = R952,50" or
# "300 / 4 500 = 1:15". Recompute every such statement and fail Level 3 on
# any mismatch — the same real-computation philosophy as the maths
# answer-key verifier, extended to Physical Sciences, Geography,
# Mathematical Literacy, Accounting and Economics worked arithmetic.
# Statements containing symbols/variables are skipped, never guessed at.

_IDENT_NUM = r"[0-9][0-9\s .,]*"


def _sa_number(tok):
    """Parse a South African formatted number: space/nbsp thousands,
    comma or point decimals. Returns float or None."""
    t = tok.replace(" ", " ").strip()
    t = re.sub(r"\s+", "", t)
    if "," in t and "." not in t:
        # ',ddd' groups are thousands ("1,200", "4,500"); a lone comma with
        # any other digit count is an SA decimal ("0,01", "1,85").
        if re.fullmatch(r"-?\d{1,3}(,\d{3})+", t):
            t = t.replace(",", "")
        elif t.count(",") == 1:
            t = t.replace(",", ".")
        else:
            return None
    elif "," in t and "." in t:
        t = t.replace(",", "")
    if not re.fullmatch(r"-?\d+(\.\d+)?", t):
        return None
    return float(t)


def _identity_normalize(text):
    """Normalise lesson text so numeric identities become parseable."""
    t = str(text)
    t = t.replace("−", "-").replace("−", "-").replace("–", "-")
    t = t.replace("×", "*").replace("·", "*").replace("÷", "/")
    t = t.replace("²", "^2").replace("³", "^3")
    t = t.replace("≈", "=")
    t = re.sub(r"\\frac\{([^{}]+)\}\{([^{}]+)\}", r"((\1)/(\2))", t)
    t = t.replace("\\times", "*").replace("\\cdot", "*")
    t = t.replace("$", " ")
    # currency and percent are presentation, not maths
    t = re.sub(r"(?i)\bR\s?(?=\d)", "", t)
    t = t.replace("%", " ")
    # word operators between numbers ("4.5 multiplied by 1,000")
    t = re.sub(r"(?i)\bmultiplied\s+by\b", "*", t)
    t = re.sub(r"(?i)\bdivided\s+by\b", "/", t)
    t = re.sub(r"(?i)(?<=\d)\s+plus\s+(?=[\d(])", " + ", t)
    t = re.sub(r"(?i)(?<=\d)\s+minus\s+(?=[\d(])", " - ", t)
    # unit words directly after a number are presentation, not maths
    t = re.sub(
        r"(?i)(?<=\d)\s*(meters?|metres?|kilometres?|kilometers?|litres?|"
        r"liters?|kWh|rands?|newtons?|volts?|amperes?|ohms?|joules?|watts?|"
        r"units?|kilograms?|percent)\b",
        " ",
        t,
    )
    return t


def _eval_arithmetic(expr):
    """Evaluate a pure-arithmetic expression (SA number format, + - * / ^ π).
    Returns float or None if anything non-arithmetic is present."""
    e = expr.strip().rstrip("=").strip()
    e = e.replace("π", f"({math.pi})").replace("\\pi", f"({math.pi})")
    # normalise each number token to python format
    def repl(m):
        v = _sa_number(m.group(0))
        return "None" if v is None else repr(v)
    e2 = re.sub(_IDENT_NUM, repl, e)
    e2 = e2.replace("^", "**")
    if "None" in e2 or not re.fullmatch(r"[0-9eE.+\-*/() ]+", e2.replace("**", "*")):
        return None
    try:
        return float(eval(e2, {"__builtins__": {}}, {}))
    except Exception:
        return None


def _numbers_match(computed, stated_text):
    stated = _eval_arithmetic(stated_text)
    if stated is None:
        return None
    if computed == stated:
        return True
    tol = max(0.01, abs(stated) * 0.005)
    if abs(computed - stated) <= tol:
        return True
    # accept when the computed value rounds to the stated precision
    m = re.search(r"\.(\d+)$", repr(stated))
    dp = len(m.group(1)) if m else 0
    return round(computed, dp) == round(stated, dp)


def verify_arithmetic_identities(text, label):
    """Find fully-numeric `expr = value` statements and recompute them.
    Returns (errors, verified_count). Skips anything containing letters or
    unsupported symbols — never guesses."""
    errors, verified = [], 0
    t = _identity_normalize(text)
    # candidate: operator-bearing numeric expression = numeric value/ratio
    pattern = re.compile(
        rf"({_IDENT_NUM}(?:[+\-*/^()\s]+{_IDENT_NUM})+)\s*=\s*"
        rf"(1\s*:\s*{_IDENT_NUM}|\(?{_IDENT_NUM}(?:\s*/\s*{_IDENT_NUM})?\)?)"
    )
    for m in pattern.finditer(t):
        lhs_text, rhs_text = m.group(1), m.group(2).rstrip().rstrip(",.;:")
        # guard: reject only when letters/symbols are DIRECTLY adjacent to
        # the statement (algebra like "= 5a"); words after intervening
        # whitespace are prose. The RHS match may absorb trailing
        # whitespace, so anchor on its last non-whitespace character.
        rhs_clean = m.group(2).rstrip().rstrip(",.;:")
        start = m.start()
        end = m.start(2) + len(rhs_clean)
        before = t[start - 1:start]
        after = t[end:end + 1]
        if re.match(r"[A-Za-z_π\\]", before) or re.match(r"[A-Za-z_π\\^]", after):
            continue
        if not re.search(r"[+\-*/^]", lhs_text):
            continue
        computed = _eval_arithmetic(lhs_text)
        if computed is None:
            continue
        ratio = re.fullmatch(r"1\s*:\s*(" + _IDENT_NUM + r")", rhs_text.strip())
        if ratio:
            x = _sa_number(ratio.group(1))
            if x is None or computed == 0:
                continue
            ok = _numbers_match(1.0 / computed if computed > 1 else computed, f"1/{x}")
            # gradient convention: VI/HE = 1:x means x = HE/VI = 1/computed
            ok = ok or _numbers_match(computed, f"1/{x}")
            if not ok:
                errors.append(
                    f"arithmetic mismatch in {label}: '{lhs_text.strip()} = {rhs_text.strip()}' "
                    f"— computed {computed:.6g}, which is not 1:{x:g}"
                )
            else:
                verified += 1
            continue
        ok = _numbers_match(computed, rhs_text)
        if ok is None:
            continue
        if not ok:
            errors.append(
                f"arithmetic mismatch in {label}: '{lhs_text.strip()} = {rhs_text.strip()}' "
                f"— recomputed left side is {computed:.6g}"
            )
        else:
            verified += 1
    return errors, verified


# --- Levels 3/4: content checks and evaluation ---

def _load_json(path, errors, label):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"{label}: cannot parse {path}: {e}")
        return None


# --- Skills: registry, validation, generated index ---

def _all_lesson_cards():
    for d in (PENDING_DIR, RUNNING_DIR, DONE_DIR):
        if d.exists():
            for f in sorted(d.glob("*.md")):
                c = f.read_text(encoding="utf-8")
                if get_field(c, "type").startswith("lesson."):
                    yield f, c



def parse_requires_skills(card):
    return [r.strip() for r in get_field(card, "requires_skills").split(",") if r.strip()]


def cmd_skills_index(args):
    """Validate the skills graph against the CAPS skill definition files.
    (The generated lessons/skills_index.json artifact is retired - the app
    side is being rebuilt on the CAPS files directly.)

    Validation (exit 1 on any violation):
    - every CAPS skill file has a unique, non-empty skill_ref
    - every requires_skills entry - on syllabus topics AND on job cards -
      resolves to a defined skill
    - every category: skill job card's skill_ref is a defined skill
    - a skill does not require itself
    """
    errors = []
    defined = {}
    for folder in sorted(CAPS_TYPE_BY_FOLDER):
        for sf in sorted((CAPS_DIR / folder / "skills").glob("grade*/*.json")):
            data = json.loads(sf.read_text(encoding="utf-8"))
            ref = str(data.get("skill_ref", "")).strip()
            if not ref:
                errors.append(f"{sf}: skill file missing skill_ref")
            elif ref in defined:
                errors.append(f"{sf}: duplicate skill_ref '{ref}' (also in {defined[ref]})")
            else:
                defined[ref] = sf.as_posix()
                if data.get("requires_skills") and ref in data["requires_skills"]:
                    errors.append(f"{sf}: skill requires itself ({ref})")

    edges = 0
    # skill -> skill prerequisites must resolve, and covered_by pointers must
    # name a real syllabus topic/subtopic (deep review defers to that lesson).
    for folder in sorted(CAPS_TYPE_BY_FOLDER):
        for sf in sorted((CAPS_DIR / folder / "skills").glob("grade*/*.json")):
            data = json.loads(sf.read_text(encoding="utf-8"))
            for ref in data.get("requires_skills", []) or []:
                edges += 1
                if ref not in defined:
                    errors.append(f"{sf}: requires_skills '{ref}' does not match any skill file")
            for ptr in data.get("covered_by", []) or []:
                gf = CAPS_DIR / folder / "syllabus" / f"grade{ptr.get('grade')}.json"
                if not gf.exists():
                    errors.append(f"{sf}: covered_by names missing syllabus file {gf}")
                    continue
                syl = json.loads(gf.read_text(encoding="utf-8"))
                # A topic name can recur across terms (e.g. PS gr10
                # "Quantitative aspects of chemical change" in T2 and T3) -
                # the pointer resolves if ANY occurrence carries the subtopic.
                hits = [topic for term in syl.get("terms", [])
                        for topic in term.get("topics", [])
                        if topic["name"] == ptr.get("topic")]
                if not hits:
                    errors.append(f"{sf}: covered_by topic not in grade{ptr.get('grade')} syllabus: {ptr.get('topic')!r}")
                elif not any(ptr.get("subtopic") in
                             [_subtopic_name(s) for s in (h.get("subtopics") or [])]
                             for h in hits):
                    errors.append(f"{sf}: covered_by subtopic not under that topic: {ptr.get('subtopic')!r}")
    for folder in sorted(CAPS_TYPE_BY_FOLDER):
        for gf in sorted((CAPS_DIR / folder / "syllabus").glob("grade*.json")):
            data = json.loads(gf.read_text(encoding="utf-8"))
            for term in data.get("terms", []):
                for topic in term.get("topics", []):
                    for ref in topic.get("requires_skills", []) or []:
                        edges += 1
                        if ref not in defined:
                            errors.append(
                                f"{gf}: topic '{topic['name']}' requires_skills "
                                f"'{ref}' does not match any skill file")

    for path, c in _all_lesson_cards():
        if get_field(c, "category") == CATEGORY_SKILL:
            ref = get_field(c, "skill_ref")
            if ref and ref not in defined:
                errors.append(f"{path.name}: skill card's skill_ref '{ref}' has no CAPS skill file")
        for ref in parse_requires_skills(c):
            edges += 1
            if ref not in defined:
                errors.append(f"{path.name}: requires_skills '{ref}' does not match any skill file")

    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        return 1
    print(f"skills: {len(defined)} defined, {edges} requirement edge(s), graph OK")
    return 0


# Session-framing signatures (teaching-content-only rule): the platform's
# player supplies all session framing, so a lesson script must not carry
# self-introductions, platform mentions, Mandy/host references, handoffs or
# goodbyes. IMPORTANT SCOPE: pedagogical transitions in the tutor's voice
# are teaching flow and MUST pass — especially the question lead-ins the
# script is required to include at MCQ subtopic ends ("Pause here and try a
# few quick questions on this before we continue"). None of these patterns
# can match such lead-ins: they target framing vocabulary (names, platform,
# greetings, farewells), not pause/question/continue language.
# Session framing is matched STRUCTURALLY, not by chasing individual phrases.
# Each rule targets the *shape* of a greeting / self-introduction / handoff /
# sign-off / stage direction, so a new wording Jules invents is caught by the
# same rule rather than needing a new signature added after it ships.
#
# Greetings, sign-offs, handovers and timekeeping lines are owned by
# tutor/assistant assets (lessons/tutors/<slug>/{greetings,signoffs}/ and
# lessons/assistants/<host>/...). A lesson script is pure subtopic teaching
# content. Question lead-ins at MCQ boundaries ARE teaching flow and must not
# match — every rule below is checked against them in the test suite.
FRAMING_SIGNATURES = (
    # --- self-introduction by TITLE. 'the' and 'big' are deliberately NOT
    #     titles here: "This is the critical move" / "the big idea" are
    #     ordinary teaching lines, and real self-intros ("I am the Algebra
    #     Grandmaster", "Big John here") are caught by the roster-driven
    #     speaker-name rule instead. ---
    (r"\b(?:i'?m|i am|this is|it'?s)\s+(?:mr|mrs|ms|miss|dr|prof|professor|uncle|aunty|aunt|bra|ranger)\b",
     "tutor self-introduction (titled name)"),
    (r"\b(?:my name is|they call me|call me|you can call me)\b",
     "tutor self-introduction"),
    # --- session greeting: welcome/hello aimed at the room ---
    (r"\b(?:welcome|hello|hi|greetings|good\s+(?:morning|afternoon|evening))\b[\s,!.]*(?:back\b|everyone\b|everybody\b|all\b|to\b|learners\b|students\b|class\b)",
     "session greeting"),
    # A bare greeting standing as its own sentence — at line start or after a
    # sentence terminator ("Numbers never lie. Welcome.") — which the
    # phrase-with-object rule above deliberately does not reach.
    (r"(?:^|(?<=[.!?])\s)\s*(?:welcome|hello|hi|greetings)\s*[.!](?:\s|$)",
     "session greeting"),
    # --- platform reference ---
    (r"\bsupacharge\b", "platform mention"),
    # --- handoff to another speaker (name-free shapes only; naming a
    #     speaker is caught by the roster-driven rule in _speaker_errors) ---
    (r"\bhand(?:ing|s|ed)?\s+(?:you\s+|it\s+|this\s+|things\s+|over\s+)?(?:over|back)?\s*to\b",
     "handoff"),
    (r"\btake\s+(?:it\s+)?from\s+here\b", "handoff"),
    # NOTE: a bare "back to you" is NOT a handoff signature — real teaching
    # uses it ("the bank owes that money back to you"). Handoffs that matter
    # either use "hand over to" or name the speaker (roster rule).
    # --- sign-off: leave-taking of any wording ---
    (r"\b(?:goodbye|good\s?bye|farewell|bye for now)\b", "goodbye/sign-off"),
    (r"\bsee\s+you\s+(?:next|in\s+the\s+next|tomorrow|soon|later|again|then)\b",
     "goodbye/sign-off"),
    (r"\b(?:that'?s|that is)\s+(?:all|it)\s+(?:for\s+)?(?:today|now|this\s+lesson)\b",
     "goodbye/sign-off"),
    (r"\buntil\s+(?:next\s+time|we\s+meet|then)\b", "goodbye/sign-off"),
    (r"\bthanks?\s+for\s+(?:watching|joining|listening|being here|your time)\b",
     "goodbye/sign-off"),
    (r"\b(?:signing off|stepping out|catch you (?:next|later))\b", "goodbye/sign-off"),
    (r"\b(?:enjoy the (?:break|rest)|take a (?:short )?break)\b", "break/handover framing"),
)

# Bracketed or parenthetical stage directions and physical-action description.
# Found in real produced narration ("[Prof Mokoena adjusts his glasses]") —
# TTS reads them aloud verbatim. Matched by SHAPE: a line that is entirely a
# bracketed aside, or contains a bracketed span describing action rather than
# maths. Inline maths/parenthetical arithmetic must NOT match, so the
# parenthetical rule requires the span to start with a verb-ish word and
# contain no digits or maths operators.
# A bracketed/parenthesised span is a STAGE DIRECTION when it describes
# physical action or names the speaker — not merely because it is in
# brackets. "(rounded to one decimal place)" and "(6/2 = 3)" are teaching;
# "(he points at the board)" and "[pauses for effect]" are not. The delimiter
# shape alone is not the signal; the acted-out verb is.
#
# NOTE: *asterisk* spans are deliberately NOT treated as stage directions.
# Every asterisk span in the existing corpus was an emphasised term
# ("*Total Fixed Costs*"), never a direction, and the narration extractor
# strips the asterisk characters so only the words are spoken.
STAGE_DIRECTION_SPANS = (
    (r"^\s*[\[\(][^\]\)]{4,}[\]\)]\s*$", "whole-line stage direction"),
    (r"\[[^\]]{4,}\]", "bracketed stage direction"),
    (r"\([^)\n]{4,}\)", "parenthetical stage direction"),
)

ACTION_WORDS = (
    r"\b(?:point|points|pointing|walk|walks|walking|gestur\w+|adjust|adjusts|"
    r"adjusting|tap|taps|tapping|smil\w+|laugh\w+|chuckl\w+|grin\w+|wink\w+|"
    r"sigh\w+|paus\w+|look|looks|looking|turn|turns|turning|lean\w+|nod\w+|"
    r"stand\w+|sits?|sitting|hold\w+|pick\w+ up|wav\w+|step\w+|glanc\w+|"
    r"face|faces|facing|beam\w+|shrug\w+|breath\w+|appear|appears|appearing)\b"
)


def _is_stage_direction(span):
    """True when a bracketed/parenthesised span describes physical action or
    names a speaker, rather than clarifying the maths."""
    inner = span.strip("()[]*").strip()
    if not inner:
        return False
    if re.search(ACTION_WORDS, inner, re.IGNORECASE):
        return True
    if re.search(r"\b(?:he|she|they)\s+\w+", inner, re.IGNORECASE):
        return True
    return any(re.search(rf"\b{re.escape(name)}\b", inner, re.IGNORECASE)
               for name in speaker_names())


_SPEAKER_NAMES_CACHE = None


def speaker_names():
    """Every on-air speaker name — tutors (persona label name + real name)
    and assistant hosts — read from the real asset directories. Naming any
    of them in narration is self-introduction, handoff or cross-promotion,
    all of which belong to tutor/assistant assets rather than a script.
    Deriving the set from data means a new tutor is covered the day their
    card lands, with no signature to remember to add."""
    global _SPEAKER_NAMES_CACHE
    if _SPEAKER_NAMES_CACHE is not None:
        return _SPEAKER_NAMES_CACHE
    names = set()
    if TUTORS_DIR.is_dir():
        for d in TUTORS_DIR.iterdir():
            if not d.is_dir():
                continue
            text = load_tutor_card(d.name)
            if not text:
                continue
            dn = persona_display_name(text)
            if dn:
                names.add(dn)
            real = get_field(text, "real_name")
            if real:
                names.add(real.strip())
    # Assistant host display names come from the registry (roster-backed,
    # name-keyed OR opaque-id layout, embedded fallback covering all three
    # hosts) — never from the directory basenames, which under the opaque-id
    # layout are assistant_<n>, not names.
    names.update(assistant_registry.all_display_names())
    _SPEAKER_NAMES_CACHE = {n for n in names if len(n) > 2}
    return _SPEAKER_NAMES_CACHE


def _speaker_errors(line, n):
    errors = []
    for name in sorted(speaker_names()):
        if re.search(rf"\b{re.escape(name)}\b", line, re.IGNORECASE):
            errors.append(
                f"script.md:{n}: session framing (speaker named: {name}) — "
                "self-introduction, handoff and cross-promotion are tutor+"
                "assistant assets; scripts are teaching content only")
            break
    return errors


def verify_no_session_framing(script):
    """Error strings for session-framing and stage-direction violations in a
    lesson script. Case-insensitive; reports line numbers. Markdown headings
    are skipped (subtopic titles like 'Summary and Sign-off' describe
    structure, not spoken audio — the narration extractor drops headings)."""
    errors = []
    for n, line in enumerate(script.splitlines(), 1):
        if line.lstrip().startswith("#"):
            continue
        errors.extend(_speaker_errors(line, n))
        for pattern, label in FRAMING_SIGNATURES:
            m = re.search(pattern, line, re.IGNORECASE)
            if m:
                errors.append(
                    f"script.md:{n}: session framing ({label}): '{m.group(0).strip()}' — "
                    "greetings/sign-offs/handovers are tutor+assistant assets; "
                    "scripts are teaching content only")
        for pattern, label in STAGE_DIRECTION_SPANS:
            m = re.search(pattern, line)
            if m and _is_stage_direction(m.group(0)):
                errors.append(
                    f"script.md:{n}: stage direction ({label}): '{m.group(0).strip()}' — "
                    "narration is spoken verbatim by TTS; describe no physical action")
    return errors


# The assistant READS the question aloud while the player shows the subtopic
# it belongs to, so the spoken line stays short and the context lives on the
# screen (owner, 2026-07-28: the first produced transcripts had 60-word
# student monologues in the assistant's mouth).
QA_QUESTION_MAX_WORDS = 25
QA_MIN_EXCHANGES = 3
QA_MAX_EXCHANGES = 5
# Session-format transcripts (asks labeled with the assistant's display
# name) have no on-screen subtopic heading, so the spoken turn itself
# carries the class context and gets a wider cap: measured over the 366
# shipped session transcripts, the longest ask is 59 words.
QA_SESSION_QUESTION_MAX_WORDS = 60
QA_HEADING_RE = re.compile(r"^###\s+(\S+)\s+—\s+(.+?)\s*$", re.MULTILINE)


def _check_qa_transcript(path, sub_refs, errors, warnings):
    """The Q&A duet, in either accepted format:

    - card/authoring format: '### <subtopic_ref> — <title>' then one
      '**Assistant:**' question and one '**Tutor:**' answer per exchange;
    - session format (the shipped session transcripts): asks labeled with
      the assistant's DISPLAY NAME from assistant_registry (**Thandi:** /
      **Bianca:** / **Mandy:**), '**Tutor:**' answers, exchanges separated
      by '***', no subtopic headings.
    """
    text = path.read_text(encoding="utf-8")
    heads = QA_HEADING_RE.findall(text)
    ask_label_re = "|".join(
        [re.escape(n) for n in sorted(assistant_registry.all_display_names())]
        + ["Assistant"])
    asks = re.findall(rf"^\*\*({ask_label_re}):\*\*\s*(.+?)(?=^\*\*|\Z)",
                      text, re.MULTILINE | re.DOTALL)
    answers = re.findall(r"^\*\*Tutor:\*\*", text, re.MULTILINE)
    # Display-name asks mark the session format, which carries no headings.
    session_format = any(label != "Assistant" for label, _q in asks)
    if not heads and not session_format:
        errors.append("assistant_qa_transcript.md has no '### <subtopic_ref> "
                      "— <title>' heading; the player needs it to show which "
                      "part of the lesson each question belongs to")
    if not (QA_MIN_EXCHANGES <= len(asks) <= QA_MAX_EXCHANGES):
        errors.append(f"assistant_qa_transcript.md has {len(asks)} assistant "
                      f"question(s); expected {QA_MIN_EXCHANGES}-{QA_MAX_EXCHANGES}")
    if len(asks) != len(answers):
        errors.append(f"assistant_qa_transcript.md: {len(asks)} question(s) "
                      f"but {len(answers)} tutor answer(s) — each question "
                      "must be answered")
    if heads and len(heads) != len(asks):
        errors.append("assistant_qa_transcript.md: every exchange needs its "
                      "own subtopic heading")
    for ref, _title in heads:
        if sub_refs and ref not in sub_refs:
            errors.append(f"assistant_qa_transcript.md references unknown "
                          f"subtopic {ref!r}")
    for label, q in asks:
        cap = (QA_QUESTION_MAX_WORDS if label == "Assistant"
               else QA_SESSION_QUESTION_MAX_WORDS)
        n = len(q.split())
        if n > cap:
            errors.append(f"assistant_qa_transcript.md: spoken question is "
                          f"{n} words (max {cap}) — put the "
                          f"context on the subtopic heading, not in the "
                          f"speech: {' '.join(q.split()[:8])}...")
    if re.search(r"^\*\*Student:\*\*", text, re.MULTILINE):
        errors.append("assistant_qa_transcript.md has a '**Student:**' turn — "
                      "the duet is assistant-asks/tutor-answers; the student "
                      "is the audience, not a recorded voice")
    return errors


def _check_flat_mcqs(data, label, lo, hi, errors):
    """Shape-check a flat question list {questions: [...]} against
    McqQuestion.fromJson: id, question, options[], correct_index in range."""
    if data is None:
        return
    questions = data.get("questions", [])
    if not lo <= len(questions) <= hi:
        errors.append(f"{label}: {len(questions)} questions (must be {lo}-{hi})")
    seen = set()
    for q in questions:
        qid = q.get("id")
        if not qid or qid in seen:
            errors.append(f"{label}: missing or duplicate question id: {qid}")
        seen.add(qid)
        if not q.get("question"):
            errors.append(f"{label} {qid}: empty question text")
        opts = q.get("options", [])
        if len(opts) < 2:
            errors.append(f"{label} {qid}: fewer than 2 options")
        ci = q.get("correct_index")
        if not isinstance(ci, int) or not 0 <= ci < max(len(opts), 1):
            errors.append(f"{label} {qid}: correct_index missing or out of range")


def _run_skill_checks(card, base, warnings):
    """Review-format checks for category: skill cards (see the Skills
    convention): diagnostic + compressed recap + exit check, bounded length,
    and none of the lesson-only content items."""
    errors = []

    paths = {}
    for field, default_name in SKILL_CONTENT_FILES.items():
        p = get_field(card, field)
        target = Path(p) if p else base / default_name
        if not target.exists():
            errors.append(f"skill review item missing: {field} ({target})")
            continue
        paths[field] = target

    # Optional single scene: tracked when produced, produced only when tracked.
    for field, default_name in SKILL_OPTIONAL_CONTENT_FILES.items():
        p = get_field(card, field)
        on_disk = base / default_name
        if p and not Path(p).exists():
            errors.append(f"{field} points at a missing file: {p}")
        elif not p and on_disk.exists():
            errors.append(f"{on_disk} exists but the card's {field} field is empty")
        elif p:
            manim = Path(p).read_text(encoding="utf-8")
            if "class" not in manim or "Scene" not in manim:
                errors.append("manim_scene.py does not define a Manim Scene class")

    # Lesson-only items are format violations on a skill.
    for field, name in CONTENT_FILES.items():
        if field in SKILL_CONTENT_FILES or field in SKILL_OPTIONAL_CONTENT_FILES:
            continue
        if get_field(card, field) or (base / name).exists():
            errors.append(
                f"{name} does not belong on a skill - skills use the review "
                "format (diagnostic + recap + exit check), not the lesson form")

    if errors:
        return (errors, warnings)

    script = paths["script_path"].read_text(encoding="utf-8")
    words = len(script.split())
    if words < SKILL_SCRIPT_MIN_WORDS:
        errors.append(
            f"skill recap too short ({words} words, minimum {SKILL_SCRIPT_MIN_WORDS})")
    if words > SKILL_SCRIPT_MAX_WORDS:
        errors.append(
            f"skill recap too long ({words} words, maximum {SKILL_SCRIPT_MAX_WORDS}) - "
            "a skill drifting toward lesson length is being authored wrong; "
            "deep teaching belongs to the covered_by lesson")
    errors.extend(verify_no_session_framing(script))

    _check_flat_mcqs(_load_json(paths["diagnostic_path"], errors, "diagnostic"),
                     "diagnostic", 1, 2, errors)
    _check_flat_mcqs(_load_json(paths["mcq_data_path"], errors, "exit check"),
                     "exit check", 2, 5, errors)
    return (errors, warnings)


def _mcq_key_signature(mcq):
    """The parts of an MCQ set the pairing contract fixes: every question's
    (subtopic ref, id, correct_index), in order. Wording/options may not
    drift either (the files are copied byte-identical), but ids + correct
    answers are the §4 'same answers' requirement, checked explicitly."""
    return [(b.get("ref"), q.get("id"), q.get("correct_index"))
            for b in mcq.get("subtopics", [])
            for q in b.get("questions", [])]


def pair_checks(card):
    """Level 3 pairing gate (docs/paired-dual-tutor-lessons-design.md §2).

    Every card gets its pair fields validated; a pair_role: secondary card
    is additionally checked against its primary: Manim scene byte-identical
    (sha256), example_problem identical, MCQ ids and correct answers
    identical. A drifted pair member hard-fails, never advances."""
    errors = []
    pair_id = get_field(card, "pair_id")
    pair_role = get_field(card, "pair_role")
    if pair_role and pair_role not in PAIR_ROLES:
        errors.append(f"pair_role must be one of {list(PAIR_ROLES)}, got {pair_role!r}")
        return errors
    if pair_role and not pair_id:
        errors.append(f"pair_role is {pair_role} but pair_id is empty")
        return errors
    if pair_id and not pair_role:
        errors.append(f"pair_id {pair_id} set but pair_role is empty")
        return errors
    if pair_role != "secondary":
        return errors

    primary_file, primary = find_pair_member(pair_id, "primary")
    if primary_file is None:
        errors.append(f"pair {pair_id}: no primary card exists for this secondary")
        return errors

    # Scene reuse is the whole point of Option B: byte-identical, verified
    # by hash, never by trusting the copy instruction.
    primary_dir = get_field(primary, "lesson_path")
    own_scene = get_field(card, "manim_path")
    primary_scene = Path(primary_dir) / "manim_scene.py" if primary_dir else None
    if primary_scene is None or not primary_scene.exists():
        errors.append(f"pair {pair_id}: primary {primary_file.name} has no "
                      "manim_scene.py on disk — the secondary cannot have "
                      "been generated from it")
    elif own_scene and Path(own_scene).exists():
        own_sha = hashlib.sha256(Path(own_scene).read_bytes()).hexdigest()
        prim_sha = hashlib.sha256(primary_scene.read_bytes()).hexdigest()
        if own_sha != prim_sha:
            errors.append(
                f"pair {pair_id}: manim_scene.py differs from the primary's "
                f"(sha256 {own_sha[:12]}… vs {prim_sha[:12]}…) — the secondary "
                "reuses the primary's scene byte-identical, never a fork")
    # (a missing secondary scene is reported by the standard content checks)

    if get_field(card, "example_problem").strip() != get_field(primary, "example_problem").strip():
        errors.append(
            f"pair {pair_id}: example_problem differs from primary "
            f"{primary_file.name} — the pair shares one example problem by contract")

    own_mcq_path = get_field(card, "mcq_data_path")
    prim_mcq_path = get_field(primary, "mcq_data_path")
    if own_mcq_path and prim_mcq_path and Path(own_mcq_path).exists() and Path(prim_mcq_path).exists():
        own_mcq = _load_json(own_mcq_path, errors, "pair mcq (secondary)")
        prim_mcq = _load_json(prim_mcq_path, errors, "pair mcq (primary)")
        if own_mcq is not None and prim_mcq is not None:
            own_sig = _mcq_key_signature(own_mcq)
            prim_sig = _mcq_key_signature(prim_mcq)
            if own_sig != prim_sig:
                diffs = [f"{a} != {b}" for a, b in zip(own_sig, prim_sig) if a != b]
                if len(own_sig) != len(prim_sig):
                    diffs.append(f"{len(own_sig)} vs {len(prim_sig)} questions")
                errors.append(
                    f"pair {pair_id}: MCQ ids/correct answers differ from the "
                    f"primary's ({'; '.join(diffs[:4])}) — same questions, same "
                    "answers is structural for a pair")
    elif prim_mcq_path and not own_mcq_path:
        pass  # secondary's missing mcq field is reported by the standard checks
    elif not prim_mcq_path:
        errors.append(f"pair {pair_id}: primary {primary_file.name} has no "
                      "mcq_data_path to compare against")

    return errors


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

    # Paired dual-tutor cards: validate the pair fields and, on a secondary,
    # the no-drift contract against its primary (hard errors).
    errors.extend(pair_checks(card))

    # Skills use the review format, not the seven-item lesson form.
    if get_field(card, "category") == CATEGORY_SKILL:
        return _run_skill_checks(card, base, warnings)

    # Every lesson must carry an assigned greeting + sign-off variant of its
    # tutor (owner decision 2026-07-28) and the ref must resolve on disk —
    # the assembler concatenates greeting audio + lesson audio + sign-off
    # audio, so a dangling ref is a broken session, not a cosmetic gap.
    for field in ("greeting_ref", "signoff_ref"):
        ref = get_field(card, field)
        if not ref:
            errors.append(f"card field {field} is empty (lessons require an "
                          f"assigned tutor variant)")
        elif not (TUTORS_DIR / ref).exists():
            errors.append(f"{field} points at a missing tutor asset: {ref}")
    # ack_ref is deliberately OPTIONAL — empty means this tutor doesn't answer
    # the five-minute call in this lesson (most lessons, and always the other
    # half of the duo). Set-but-dangling is still a broken session.
    ack = get_field(card, "ack_ref")
    if ack and not (TUTORS_DIR / ack).exists():
        errors.append(f"ack_ref points at a missing tutor asset: {ack}")

    # The Q&A duet belongs to the FIRST tutor of the session only (owner,
    # 2026-07-28) — the expert teaches before the break and answers the
    # session's questions before signing off; the simplifier follows the
    # break and has none.
    first_tutor = is_expert_tutor(get_field(card, "type"),
                                  get_field(card, "subject"),
                                  get_field(card, "tutor"))
    required = dict(CONTENT_FILES)
    if not first_tutor:
        required.pop("assistant_qa_transcript_path", None)
        if get_field(card, "assistant_qa_transcript_path"):
            errors.append("assistant_qa_transcript_path is set on a "
                          "second-tutor card: the Q&A belongs to the first "
                          "tutor of the session only")

    paths = {}
    for field in required:
        p = get_field(card, field)
        if not p:
            errors.append(f"card field {field} is empty")
            continue
        if not Path(p).exists():
            errors.append(f"{field} points at a missing file: {p}")
            continue
        paths[field] = Path(p)

    # Optional items: tracked when produced, produced only when tracked.
    for field, default_name in OPTIONAL_CONTENT_FILES.items():
        p = get_field(card, field)
        on_disk = base / default_name
        if p and not Path(p).exists():
            errors.append(f"{field} points at a missing file: {p}")
        elif not p and on_disk.exists():
            errors.append(
                f"{on_disk} exists but the card's {field} field is empty — "
                "content must be tracked on the job card"
            )
    if errors:
        return (errors, warnings)

    # Script: non-trivial, subtopic-structured, in scope for 15 minutes.
    # Length shortfalls are tagged expandable: the Level 3 workflow re-prompts
    # Jules once to expand before hard-failing (see cmd_check).
    script = paths["script_path"].read_text(encoding="utf-8")
    words = len(script.split())
    if words < SCRIPT_MIN_WORDS:
        errors.append(
            f"[expandable] script.md too short for 15 minutes of teaching "
            f"({words} words, minimum {SCRIPT_MIN_WORDS})"
        )

    framing_errors = verify_no_session_framing(script)
    errors.extend(framing_errors)

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

    # The Q&A duet (first tutor only — the field is absent on the other card).
    if "assistant_qa_transcript_path" in paths:
        _check_qa_transcript(
            paths["assistant_qa_transcript_path"],
            {s.get("ref") for s in (subs or {}).get("subtopics", [])},
            errors, warnings)

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

        key_errors, verified = verify_answer_keys(mcq)
        errors.extend(key_errors)
        if verified:
            print(f"Answer keys verified programmatically: {len(verified)}")
            for qid, how in verified:
                print(f"  {qid}: {how}")


    # Comprehension check questions.
    cc = _load_json(paths["comprehension_check_path"], errors, "comprehension_check")
    if cc is not None and not cc.get("questions"):
        errors.append("comprehension_check.json has no questions")

    # Recompute every explicit numeric identity in the teaching text —
    # covers worked arithmetic in all six subjects.
    ident_total = 0
    ident_sources = [("script", script)]
    if mcq is not None:
        for batch in mcq.get("subtopics", []):
            for qn in batch.get("questions", []):
                ident_sources.append((
                    f"mcq {qn.get('id')}",
                    str(qn.get("question", "")) + " " + " ".join(map(str, qn.get("options", []))),
                ))
    if cc is not None:
        for qn in cc.get("questions", []):
            ident_sources.append((f"comprehension {qn.get('id')}", str(qn.get("expected_answer", ""))))
    for label, text in ident_sources:
        ident_errors, ident_verified = verify_arithmetic_identities(text, label)
        errors.extend(ident_errors)
        ident_total += ident_verified
    if ident_total:
        print(f"Arithmetic identities recomputed and verified: {ident_total}")

    # 60-second reel clip script (level6c reel-brief convention).
    reel = _load_json(paths["reel_brief_path"], errors, "reel_clip")
    if reel is not None:
        if reel.get("duration_seconds") != 60:
            errors.append("reel_clip.json duration_seconds must be 60")
        for key in ("hook_text", "clip_script", "platform"):
            if not reel.get(key):
                errors.append(f"reel_clip.json missing {key}")

    # Mandy post-session Q&A transcript (first tutor only — the field is
    # absent on the second-tutor card by the roster rules above).
    if "assistant_qa_transcript_path" in paths:
        mandy = paths["assistant_qa_transcript_path"].read_text(encoding="utf-8")
        if len(mandy.split()) < 50:
            errors.append("assistant_qa_transcript.md too short to be a usable Q&A transcript")

    # Skills schema consistency (see the Skills convention at the top of
    # this file): a skill card must carry its stable ref, a non-skill card
    # must not, and every requires_skills entry must resolve.
    category = get_field(card, "category")
    skill_ref = get_field(card, "skill_ref")
    if category == CATEGORY_SKILL and not skill_ref:
        errors.append("category is skill but skill_ref is empty")
    if skill_ref and category != CATEGORY_SKILL:
        errors.append(f"skill_ref '{skill_ref}' set but category is not 'skill'")
    reqs = parse_requires_skills(card)
    if reqs:
        defined = load_caps_skills()
        for ref in reqs:
            if ref not in defined:
                errors.append(f"requires_skills '{ref}' does not match any skill definition file")
            elif ref == skill_ref:
                errors.append(f"card requires itself ({ref})")

    # Linked past-paper worked examples: if this lesson has been linked to a
    # real past-paper question (past_papers.py), verify the link here — the
    # payoff of the bidirectional index. A wrong link (the subtopic does not
    # teach the question's method) or a memo answer our recomputation
    # disagrees with is a real content error, so it fails Level 3.
    if get_field(card, "past_paper_examples"):
        pp_errors = verify_linked_past_papers(get_field(card, "id"))
        errors.extend(pp_errors)

    return (errors, warnings)


def verify_linked_past_papers(lesson_id):
    """Bridge to past_papers.py's verifier so Level 3 can validate a lesson's
    linked past-paper worked examples. Returns a list of error strings. Never
    raises — a missing index or unimportable module is reported, not fatal."""
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "past_papers", str(Path(__file__).with_name("past_papers.py")))
        pp = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pp)
    except Exception as e:  # pragma: no cover - defensive
        return [f"could not load past_papers verifier: {e}"]

    if not pp.LINKS_PATH.exists():
        return [f"card lists past_paper_examples but {pp.LINKS_PATH} is missing"]

    links = json.loads(pp.LINKS_PATH.read_text("utf-8"))
    back = links.get("lessons", {}).get(lesson_id, [])
    if not back:
        return [f"card lists past_paper_examples but no link recorded for {lesson_id}"]

    errors = []
    for b in back:
        paper_path = pp.PP_ROOT / pp._paper_rel(b["paper_id"])
        paper = json.loads(paper_path.read_text("utf-8"))
        q = next((x for x in paper["questions"] if x["ref"] == b["question"]), None)
        if q is None:
            errors.append(f"linked past-paper question {b['question']} not found in {paper_path}")
            continue
        lessons = pp.load_lessons(paper["subject"], paper["grade"])
        lesson = next((l for l in lessons if l["id"] == lesson_id), None)
        method = q["solution_method"]
        if not (lesson and lesson["methods"].get(method) == b["subtopic_ref"]):
            errors.append(
                f"past-paper link {b['paper_id']}:{q['ref']} claims subtopic "
                f"{b['subtopic_ref']} teaches '{method}', but it does not")
        computed = pp.recompute(q["ref"], paper)
        if q.get("checkable") and computed is not None:
            memo = pp.parse_memo_roots(q["memo_answer"])
            if computed != memo:
                errors.append(
                    f"past-paper {q['ref']}: recomputed answer {sorted(computed)} "
                    f"disagrees with memo {sorted(memo)}")
    if not errors:
        print(f"Past-paper links verified: {len(back)} worked example(s)")
    return errors


def cmd_check(args):
    """Exit codes: 0 = pass; 1 = hard fail; 2 = only failure is an
    expandable script-length shortfall and no expansion has been requested
    yet — the Level 3 workflow should re-prompt Jules once instead of
    stalling the card on a fixable length issue."""
    card = read_card(args.file)
    errors, warnings = run_checks(card, args.file)
    for w in warnings:
        print(f"WARN: {w}")

    # Evaluated cards are archived history: report (useful for re-auditing a
    # lesson, e.g. after linking a past-paper worked example) but never
    # rewrite rules_status/last_updated on them — the state machine is done
    # with these cards.
    if get_field(card, "status").startswith("evaluated"):
        for e in errors:
            print(f"FAIL: {e}")
        print("Card is evaluated (archived) — read-only check, card not modified.")
        return 1 if errors else 0

    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        only_expandable = all(e.startswith("[expandable]") for e in errors)
        not_yet_expanded = not get_field(card, "expansion_requested")
        if only_expandable and not_yet_expanded:
            card = set_field(card, "rules_status", "expanding")
            rc = 2
            print("Script length is the only failure and no expansion has been "
                  "requested yet — eligible for one Jules expansion pass.")
        else:
            card = set_field(card, "rules_status", "failed")
            rc = 1
        card = set_field(card, "last_updated", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        write_card(args.file, card)
        return rc
    card = set_field(card, "rules_status", "passed")
    card = set_field(card, "last_updated", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    write_card(args.file, card)
    print(f"Level 3 checks passed for {args.file} ({len(warnings)} warning(s)).")
    return 0


def build_expansion_prompt(card, card_file):
    """One-shot Jules re-prompt: expand the existing script to length without
    regenerating the rest of the lesson."""
    card_id = get_field(card, "id")
    tutor = get_field(card, "tutor") or TUTOR_GRANDMASTER
    script_path = get_field(card, "script_path")
    subtopics_path = get_field(card, "subtopics_path")
    return f"""TASK: Expand an existing Supacharge lesson script that is too short.

The lesson content for job card {card_file} is complete and reviewed except
that {script_path} does not fill the required 15 minutes of teaching
(minimum {SCRIPT_MIN_WORDS} words; aim for 1200-1800).

Expand {script_path} IN PLACE, in the existing tutor's voice ({tutor}):
- Keep every existing '## Subtopic:' heading and the existing teaching
  sequence — deepen each subtopic (fuller working, an extra example or
  common-mistake discussion per subtopic, richer transitions), do not bolt
  new subtopics on.
- Keep the worked example and all of its mathematics exactly as it is.
- If the pacing changes, adjust the timestamps in {subtopics_path} so the
  subtopics stay contiguous and total close to 900 seconds; keep every ref
  unchanged.
- Do NOT modify mcq.json, comprehension_check.json, reel_clip.json, the
  Mandy files, the Manim file (unless a timestamp comment references the
  script), or any job card field other than last_updated. Do not touch the
  status or gate fields on {card_file}.

This is the single permitted expansion pass for {card_id}; if the script
still falls short of {SCRIPT_MIN_WORDS} words it will be failed for human
attention, so expand it properly."""


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
    crosscheck = get_field(card, "crosscheck_status")
    if crosscheck not in ("passed", "failed"):
        print(
            "Error: the independent AI crosscheck has not recorded a verdict "
            f"(crosscheck_status is {crosscheck or 'empty'}) — Level 4 is "
            "blocked until it runs successfully (fail-closed)."
        )
        return 1
    if crosscheck == "failed":
        print("NOTE: the independent review recorded issues (see crosscheck_notes); "
              "the human reviewer approved with that report in view.")
    errors, warnings = run_checks(card, args.file)
    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        return 1
    for w in warnings:
        print(f"WARN: {w}")
    print(f"Level 4 evaluation passed for {args.file}: content complete, checks green, human-approved.")
    return 0


# --- Level 3.5: independent AI cross-check before the human gate ---
#
# The Level 4 human is not a subject teacher; this pass gives them a concrete
# independent report to decide on. Independence: the review runs as a fresh
# Groq call (llama family) with an error-finding prompt — a different model
# and context from the Jules session that generated the content. Computed
# checks (answer keys, arithmetic identities) remain the primary trust
# anchor; this pass covers what cannot be reduced to a computation.

REVIEW_CRITERIA = {
    "physical_sciences": """- Unit consistency: every quantity carries correct SI units; unit algebra in
  worked examples is right (N = kg·m·s⁻², mol·dm⁻³ etc.).
- Formula correctness: every formula matches the official NSC Physical
  Sciences data sheet form; no invented or mis-stated relations.
- Worked-example arithmetic and substitutions are actually correct.
- Directions/signs and physical reasoning (e.g. what net force means,
  equilibrium conditions, Le Chatelier direction) match standard physics
  and chemistry.""",
    "economics": """- Market mechanisms are internally consistent and match standard economic
  theory: shift vs movement along a curve, shift direction for the stated
  cause, resulting equilibrium price AND quantity direction, elastic vs
  inelastic classification, normal vs inferior goods.
- Any calculation (elasticity, multiplier, CPI) is arithmetically right.
- Graph descriptions match the mechanism described in the text.""",
    "geography": """- Formulas and conversions (gradient = VI/HE, map scale, unit conversions)
  are stated and applied correctly; answers in correct NSC formats (1:x).
- Physical-process descriptions (cyclone stages, fluvial processes,
  atmospheric circulation) are factually correct for the Southern
  Hemisphere where hemisphere matters.
- Worked mapwork arithmetic is actually correct.""",
    "maths_literacy": """- All worked arithmetic (tariffs, VAT at 15%, interest, measurement) is
  correct, including the 15/115 extraction for VAT-inclusive amounts.
- Rounding follows CAPS conventions (money to 2 decimals; round UP for
  materials/containers) and the final answer is stated in context with
  real units.
- The context and documents used are realistic and CAPS-appropriate.""",
    "accounting": """- Double-entry logic is correct: what is debited and credited, and why.
- Prescribed formats are respected (which side outstanding items enter a
  bank reconciliation, statement line order, ledger account structure).
- All figures are arithmetically consistent and traceable to the given
  information; totals and balancing figures are right.
- VAT arithmetic uses the correct 15% / 15-115 relationships.""",
    "maths": """- Every algebraic step follows from the previous one; no sign errors,
  invalid operations, or wrong formula statements.
- Definitions and theorems are stated correctly for the CAPS syllabus.
- MCQ distractor explanations (if any) do not accidentally assert
  falsehoods as true.""",
}


def build_review_prompt(card):
    subject = get_field(card, "subject")
    grade = get_field(card, "grade")
    topic = get_field(card, "topic")
    subtopic = get_field(card, "subtopic")
    subject_key = slugify(subject)
    if subject_key == "mathematical_literacy":
        subject_key = "maths_literacy"
    criteria = REVIEW_CRITERIA.get(subject_key, REVIEW_CRITERIA["maths"])

    script = Path(get_field(card, "script_path")).read_text(encoding="utf-8")[:7000]
    mcq = json.loads(Path(get_field(card, "mcq_data_path")).read_text(encoding="utf-8"))
    qa_lines = []
    for batch in mcq.get("subtopics", []):
        for qn in batch.get("questions", []):
            opts = qn.get("options", [])
            ci = qn.get("correct_index", 0)
            marked = "; ".join(
                f"[CORRECT] {o}" if i == ci else str(o) for i, o in enumerate(opts)
            )
            qa_lines.append(f"Q ({qn.get('id')}): {qn.get('question')}\n   Options: {marked}")
    cc = json.loads(Path(get_field(card, "comprehension_check_path")).read_text(encoding="utf-8"))
    for qn in cc.get("questions", []):
        qa_lines.append(f"Comprehension ({qn.get('id')}): {qn.get('question')}\n   Expected answer: {qn.get('expected_answer')}")
    qa_text = "\n".join(qa_lines)[:5000]

    return f"""You are an independent subject-matter reviewer for South African CAPS/NSC
lesson content. You did NOT write this lesson. Your only job is to find
genuine subject-content errors before this lesson reaches students — you are
rewarded for catching real errors and penalised for inventing nitpicks.
Style, tone, and length are NOT your concern; another process handles those.

Lesson under review: {subject} Grade {grade} — {topic}: {subtopic}

Check specifically:
{criteria}

=== LESSON SCRIPT ===
{script}

=== QUESTIONS AND MARKED ANSWERS ===
{qa_text}

Reply in EXACTLY this format and nothing else:
VERDICT: PASS or FAIL
ISSUES:
- <each genuine subject-content error, with where it occurs and why it is wrong>
Write "- none" under ISSUES if you found no genuine errors. FAIL only for
real content errors (wrong facts, wrong arithmetic, wrong mechanism, wrong
answer marked correct), never for style or brevity."""


def _parse_review(text):
    """Strict verdict parsing — anything malformed is an error (fail-closed)."""
    m = re.search(r"^\s*VERDICT:\s*(PASS|FAIL)\s*$", text, re.MULTILINE | re.IGNORECASE)
    if not m:
        return None, []
    verdict = m.group(1).upper()
    issues = re.findall(r"^\s*-\s+(.+)$", text.split("ISSUES:", 1)[-1], re.MULTILINE)
    issues = [i.strip() for i in issues if i.strip().lower() not in ("none", "none.")]
    return verdict, issues


def cmd_crosscheck(args):
    """Run the independent AI review and record the result on the card.

    Exit codes: 0 = review ran and a verdict was recorded (passed or
    failed); 1 = the check itself could not run or returned garbage — the
    card is marked crosscheck_status: error, which blocks Level 4
    (fail-closed: a broken check never looks like a passed one)."""
    card = read_card(args.file)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    def record(status, notes):
        c = read_card(args.file)
        c = set_field(c, "crosscheck_status", status)
        c = set_block_field(c, "crosscheck_notes", notes[:1800])
        c = set_field(c, "last_updated", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        write_card(args.file, c)

    try:
        prompt = build_review_prompt(card)
    except Exception as e:
        record("error", f"[{now}] crosscheck could not assemble content: {e}")
        print(f"Error: could not assemble review content: {e}")
        return 1

    if args.ai_response_file:
        # test hook: parse a canned response instead of calling the API
        response = Path(args.ai_response_file).read_text(encoding="utf-8")
    else:
        import subprocess
        # Routed through the logged wrapper: 429s are retried with backoff
        # and recorded (with run/job identity) in api_usage.jsonl.
        proc = subprocess.run(
            [sys.executable, "lessons/scripts/CAPS/api_call_logged.py",
             "--api", "groq", "--job-id", get_field(card, "id") or "",
             "groq", "--prompt", prompt],
            capture_output=True, text=True, encoding="utf-8", errors="replace",
        )
        response = (proc.stdout or "").strip()
        if proc.returncode != 0 or not response or "Error:" in response:
            record("error", f"[{now}] independent review call failed: "
                            f"{(response or proc.stderr or 'no output')[:400]}")
            print("Error: independent review call failed (fail-closed).")
            return 1

    verdict, issues = _parse_review(response)
    if verdict is None:
        record("error", f"[{now}] review response had no parseable VERDICT: {response[:400]}")
        print("Error: review response malformed (fail-closed).")
        return 1

    status = "passed" if verdict == "PASS" else "failed"
    lines = [f"[{now}] Independent AI review (fresh Groq/llama call, not the generating agent): {verdict}"]
    if issues:
        lines += [f"- {i}" for i in issues]
    else:
        lines.append("- no issues found")
    record(status, "\n".join(lines))
    print(f"Crosscheck recorded: {status}" + (f" ({len(issues)} issue(s))" if issues else ""))
    return 0


# --- pipeline dashboard ---

DASHBOARD_PATH = Path("lessons/DASHBOARD.md")

# Pipeline order for the status matrix columns.
STATUS_ORDER = [
    "theme_generated", "pending_approval", "concept_expanding",
    "concept_generated", "pending_concept_approval", "evaluated",
    "stalled", "failed", "declined",
]


def _load_all_cards():
    cards = []
    for d, bucket in ((PENDING_DIR, "pending"), (RUNNING_DIR, "running"), (DONE_DIR, "done")):
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            if f.name.startswith("template"):
                continue
            c = f.read_text(encoding="utf-8")
            if not get_field(c, "type").startswith("lesson."):
                continue
            cards.append({
                "file": f, "bucket": bucket,
                "id": get_field(c, "id"), "subject": get_field(c, "subject"),
                "grade": get_field(c, "grade"),
                "term": "skills" if get_field(c, "category") == CATEGORY_SKILL
                        else get_field(c, "term"),
                "topic": get_field(c, "topic"), "subtopic": get_field(c, "subtopic"),
                "status": get_field(c, "status"), "idea_status": get_field(c, "idea_status"),
                "concept_status": get_field(c, "concept_status"),
                "crosscheck": get_field(c, "crosscheck_status"),
                "attempts": int(get_field(c, "attempts") or 0),
                "max_iterations": int(get_field(c, "max_iterations") or 10),
                "expansion": get_field(c, "expansion_requested"),
                "pair_id": get_field(c, "pair_id"),
                "pair_role": get_field(c, "pair_role"),
            })
    return cards


def cmd_dashboard(args):
    """Regenerate lessons/DASHBOARD.md from the actual job cards and the
    CAPS syllabus backlog."""
    cards = _load_all_cards()
    seed_entries = load_seed_entries() if CAPS_DIR.exists() else []
    seeded_hashes = set()
    for d in (PENDING_DIR, RUNNING_DIR, DONE_DIR):
        if d.exists():
            for f in d.glob("*.md"):
                m = re.search(r"_([0-9a-f]{6})\.md$", f.name)
                if m:
                    seeded_hashes.add(m.group(1))

    lines = [
        "# Lesson Pipeline Dashboard",
        "",
        f"*Generated {datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC by "
        "`lesson_pipeline.py dashboard` (regenerated hourly by Lesson 0 and on "
        "seed pushes — if this timestamp is old, check the Lesson 0 workflow).*",
        "",
    ]

    # 1. Needs-you-now queue: the human-approval bottleneck.
    gates = []
    for c in cards:
        if c["bucket"] == "done":
            continue
        if c["status"] == "pending_approval" and c["idea_status"] != "approved":
            gates.append((c, "approve the lesson idea (`idea_status: approved`)"))
        elif c["status"] == "pending_concept_approval" and c["concept_status"] != "approved":
            note = " — **independent crosscheck FAILED, read crosscheck_notes first**" if c["crosscheck"] == "failed" else ""
            gates.append((c, f"review content accuracy (`concept_status: approved`){note}"))
    lines += [f"## Waiting on you ({len(gates)})", ""]
    if gates:
        lines.append("| Card | Subject | Action |")
        lines.append("|---|---|---|")
        for c, action in gates:
            lines.append(f"| `{c['id']}` | {c['subject']} G{c['grade']} | {action} |")
    else:
        lines.append("Nothing — the pipeline is not blocked on a human gate.")
    lines.append("")

    # 2. Attention: stalled / failed / crosscheck errors / retry-worn cards.
    attention = []
    for c in cards:
        reasons = []
        if c["status"] in ("stalled", "failed", "declined"):
            reasons.append(f"status {c['status']}")
        if c["crosscheck"] == "error":
            reasons.append("crosscheck error (blocked, fail-closed)")
        if c["attempts"] >= 3:
            reasons.append(f"attempts {c['attempts']}")
        if c["expansion"]:
            reasons.append("script expansion pass used")
        if reasons and c["bucket"] != "done":
            attention.append((c, "; ".join(reasons)))
    lines += [f"## Needs intervention ({len(attention)})", ""]
    if attention:
        lines.append("| Card | Subject | Why |")
        lines.append("|---|---|---|")
        for c, why in attention:
            lines.append(f"| `{c['id']}` | {c['subject']} G{c['grade']} | {why} |")
    else:
        lines.append("No stalled, failed or blocked cards.")
    lines.append("")

    # 3. Status matrix by subject.
    subjects = sorted({c["subject"] for c in cards})
    live_statuses = [s for s in STATUS_ORDER
                     if any(c["status"] == s for c in cards)]
    lines += ["## Cards by status and subject", ""]
    lines.append("| Subject | " + " | ".join(live_statuses) + " | total |")
    lines.append("|---|" + "---|" * (len(live_statuses) + 1))
    for s in subjects:
        row = [s]
        subj_cards = [c for c in cards if c["subject"] == s]
        for st in live_statuses:
            row.append(str(sum(1 for c in subj_cards if c["status"] == st) or ""))
        row.append(str(len(subj_cards)))
        lines.append("| " + " | ".join(row) + " |")
    totals = ["**All**"]
    for st in live_statuses:
        totals.append(f"**{sum(1 for c in cards if c['status'] == st)}**")
    totals.append(f"**{len(cards)}**")
    lines.append("| " + " | ".join(totals) + " |")
    lines.append("")

    # 3b. Paired dual-tutor cards, one line per pair (both members' state
    # at a glance — a secondary waits for its primary by design).
    pairs = {}
    for c in cards:
        if c["pair_id"]:
            pairs.setdefault(c["pair_id"], {})[c["pair_role"] or "?"] = c
    lines += [f"## Pairs ({len(pairs)})", ""]
    if pairs:
        for pid in sorted(pairs):
            members = pairs[pid]
            parts = []
            for role in PAIR_ROLES:
                m = members.get(role)
                parts.append(f"{role} `{m['id']}` ({m['status']})" if m
                             else f"{role} **MISSING**")
            lines.append(f"- pair `{pid}`: " + " / ".join(parts))
    else:
        lines.append("No paired dual-tutor cards yet.")
    lines.append("")

    # 4. Syllabus backlog per subject/grade.
    from collections import Counter
    seed_total = Counter()
    seed_used = Counter()
    for e in seed_entries:
        key = (e["subject"], str(e["grade"]))
        seed_total[key] += 1
        if entry_hash(e) in seeded_hashes:
            seed_used[key] += 1
    lines += ["## Syllabus backlog (topics not yet opened as cards)", ""]
    lines.append("| Subject | Grade | Opened | Remaining |")
    lines.append("|---|---|---|---|")
    for key in sorted(seed_total):
        s, g = key
        lines.append(f"| {s} | {g} | {seed_used[key]} | {seed_total[key] - seed_used[key]} |")
    lines.append(f"\nSyllabus rows total: {sum(seed_total.values())}; opened: "
                 f"{sum(seed_used.values())}; remaining: "
                 f"{sum(seed_total.values()) - sum(seed_used.values())}.")
    lines.append("")

    # 5. Evaluated lessons ready for the future Level 6.
    done = [c for c in cards if c["status"] == "evaluated"]
    lines += [f"## Evaluated (Level 4 complete, awaiting Level 6): {len(done)}", ""]
    for c in done:
        lines.append(f"- `{c['id']}` — {c['subject']} G{c['grade']} term {c['term']}")
    lines.append("")

    # 6. API usage (written by the shared delegate; committed by the
    # lesson workflows). Groq free tier: 30 RPM / 1 000 req/day / 12k TPM /
    # 100k tokens/day; Jules free: 15 tasks/day (Pro: 100/day).
    usage_path = Path(".rokct/agent/log/api_usage.jsonl")
    lines += ["## API usage (Groq/Jules)", ""]
    if usage_path.exists():
        from datetime import timedelta
        cutoff = (datetime.utcnow() - timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%SZ")
        day = {"groq_calls": 0, "groq_tokens": 0, "jules_sessions": 0}
        total = {"groq_calls": 0, "groq_tokens": 0, "jules_sessions": 0}
        for raw in usage_path.read_text(encoding="utf-8").splitlines():
            try:
                r = json.loads(raw)
            except ValueError:
                continue
            recent = r.get("ts", "") >= cutoff
            if r.get("api") == "groq":
                total["groq_calls"] += 1
                total["groq_tokens"] += r.get("total_tokens") or 0
                if recent:
                    day["groq_calls"] += 1
                    day["groq_tokens"] += r.get("total_tokens") or 0
            elif r.get("api") == "jules":
                total["jules_sessions"] += 1
                if recent:
                    day["jules_sessions"] += 1
        lines.append("| Window | Groq calls | Groq tokens | Jules sessions |")
        lines.append("|---|---|---|---|")
        lines.append(f"| Last 24 h | {day['groq_calls']} | {day['groq_tokens']} | {day['jules_sessions']} |")
        lines.append(f"| All time | {total['groq_calls']} | {total['groq_tokens']} | {total['jules_sessions']} |")
        lines.append("")
        lines.append("Documented limits — Groq free tier: 30 req/min, 1 000 req/day, "
                     "12k tokens/min, **100k tokens/day**; Jules free: **15 tasks/day** "
                     "(Google AI Pro: 100/day). A lesson consumes ~2 Groq calls "
                     "(~4-5k tokens) and 1-2 Jules sessions.")
    else:
        lines.append("No usage recorded yet — the log starts with the first "
                     "Groq/Jules call after the delegate's usage logging deployed.")
    lines.append("")

    # 6b. Cost / rate-limit visibility (scale-hardening brief section 3),
    # rendered by the standalone module. Prices come ONLY from the
    # API_PRICE_TABLE env config — nothing is hardcoded here.
    try:
        import api_cost_report
        lines += api_cost_report.render_dashboard_section(usage_path)
    except Exception as e:  # never let reporting break the dashboard
        lines += ["## Cost / rate-limits", "", f"Section unavailable: {e}", ""]

    out = "\n".join(lines)
    DASHBOARD_PATH.write_text(out, encoding="utf-8")
    print(f"Dashboard written to {DASHBOARD_PATH}: {len(cards)} cards, "
          f"{len(gates)} at human gates, {len(attention)} need intervention.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Lesson pipeline helpers (Levels 0-4).")
    sub = parser.add_subparsers(dest="command")

    p = sub.add_parser("seed", help="Level 0: create lesson job cards from the CAPS syllabus")
    p.add_argument("--type", required=True, help="Lesson type, e.g. lesson.maths")
    p.add_argument("--limit", type=int, default=1, help="Max cards to create this run")
    p.add_argument("--category", default=None,
                   help="Only seed rows of this category (e.g. 'skill' - skill rows "
                        "load after topic rows, so opening skills needs this filter)")

    p = sub.add_parser("prompt", help="Print the agent prompt for a level (3 = script expansion)")
    p.add_argument("--file", required=True)
    p.add_argument("--level", type=int, required=True, choices=[1, 2, 3])

    p = sub.add_parser("pair-ready", help="Exit 0 when lesson2 may run this card; 1 while a paired secondary waits for its primary's scene")
    p.add_argument("--file", required=True)

    p = sub.add_parser("mark-expansion", help="Record the single permitted script-expansion pass")
    p.add_argument("--file", required=True)

    p = sub.add_parser("plan", help="Level 1: apply Groq plan output to the card")
    p.add_argument("--file", required=True)
    p.add_argument("--content", required=True)

    p = sub.add_parser("check", help="Level 3: run content checks")
    p.add_argument("--file", required=True)

    p = sub.add_parser("evaluate", help="Level 4: final evaluation gate")
    p.add_argument("--file", required=True)

    sub.add_parser("dashboard", help="Regenerate lessons/DASHBOARD.md from real card data")

    sub.add_parser("skills-index", help="Validate the skills graph and regenerate lessons/skills_index.json")

    p = sub.add_parser("crosscheck", help="Level 3.5: independent AI review; records crosscheck_status/notes")
    p.add_argument("--file", required=True)
    p.add_argument("--ai-response-file", help="Test hook: parse this canned response instead of calling the API")

    p = sub.add_parser("check-duplicate", help="Exit 1 if a card already exists for (subject, grade, topic, subtopic)")
    p.add_argument("--subject", required=True)
    p.add_argument("--grade", required=True)
    p.add_argument("--topic", required=True)
    p.add_argument("--subtopic", required=True)

    args = parser.parse_args()
    def cmd_check_duplicate(a):
        dup = find_duplicate_card(a.subject, a.grade, a.topic, a.subtopic)
        if dup:
            print(f"DUPLICATE: ({a.subject}, grade {a.grade}, {a.topic}, {a.subtopic}) already has card {dup}")
            return 1
        print("No existing card for this (subject, grade, topic, subtopic).")
        return 0

    handlers = {
        "seed": cmd_seed,
        "prompt": cmd_prompt,
        "pair-ready": cmd_pair_ready,
        "plan": cmd_plan,
        "check": cmd_check,
        "evaluate": cmd_evaluate,
        "check-duplicate": cmd_check_duplicate,
        "mark-expansion": cmd_mark_expansion,
        "crosscheck": cmd_crosscheck,
        "dashboard": cmd_dashboard,
        "skills-index": cmd_skills_index,
    }
    if args.command not in handlers:
        parser.print_help()
        sys.exit(1)
    sys.exit(handlers[args.command](args))


if __name__ == "__main__":
    main()
