# -*- coding: utf-8 -*-
"""Generate and PROVE the weekly live-broadcast grid.

THE SHAPE (owner, 2026-07-29): at any moment exactly one session per grade is
on air - three grades, three concurrent sessions, always three DIFFERENT
subjects. That single rule satisfies both identity constraints at once:

  * no duo is ever live twice, because the three concurrent sessions are
    three different subjects and a duo owns one subject;
  * no assistant is ever live twice, because the three sessions are three
    different grades and an assistant owns one grade (#35);
  * and no student can ever clash, because their grade has exactly ONE
    session per slot - there is nothing to choose between.

Other owner-given facts:
  * broadcasts run 6 days a week (no Sunday);
  * each grade-subject gets 3 lessons per week, each airing in 3 timeslots;
  * a session is ~60 minutes. The old 10-minute office-hours tail is GONE -
    it was replaced by the in-session MCQs - so an hourly slot holds a
    session with changeover.

Structure that falls out of it: the six subjects split into two disjoint
triples, one triple per day, alternating. Within a day the three grades
rotate through that triple, so grade i takes subject (slot + i) mod 3 - which
puts each grade's three subjects at slots 3 apart and never lets two grades
sit on the same subject in one slot.

Run:  python lessons/scripts/broadcast_schedule.py
      python lessons/scripts/broadcast_schedule.py --ceiling
"""
import json
import sys
from pathlib import Path

LESSONS = Path("lessons")
ROSTER = LESSONS / "tutors" / "roster.json"
OUT = LESSONS / "schedule" / "weekly_grid.json"

SESSION_MINUTES = 60
# Nine hourly slots. The window is the one genuinely open parameter - it
# depends on whether students are home during school hours (Supacharge as
# plan B, #28) or at school and catching up afterwards. Change FIRST_HOUR
# alone; nothing else in the grid depends on it.
FIRST_HOUR = 8
SLOTS_PER_DAY = 9
SLOT_TIMES = [f"{FIRST_HOUR + i:02d}:00" for i in range(SLOTS_PER_DAY)]

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]  # Sunday: catch-up/buffer
GRADES = [10, 11, 12]
LESSONS_PER_WEEK = 3
REPEATS_PER_LESSON = 3

# The two disjoint triples. Maths and Maths Literacy are deliberately in
# DIFFERENT triples: a student holds exactly one of them (#29), so splitting
# them spreads each student's week instead of stacking it.
TRIPLES = [
    ["maths", "physical_sciences", "accounting"],
    ["maths_literacy", "economics", "geography"],
]


def load_duos():
    return json.loads(ROSTER.read_text(encoding="utf-8"))["subjects"]


def build(duos):
    """One airing = one grade's session in one slot. Deterministic."""
    airings = []
    for day_idx, day in enumerate(DAYS):
        triple = TRIPLES[day_idx % len(TRIPLES)]
        # Which lesson of the week this is for that triple: the triple comes
        # round on days 0,2,4 (or 1,3,5), so lesson 1, 2, 3 in order.
        lesson_no = day_idx // len(TRIPLES) + 1
        for slot in range(SLOTS_PER_DAY):
            for grade_idx, grade in enumerate(GRADES):
                subject = triple[(slot + grade_idx) % len(triple)]
                airings.append({
                    "day": day,
                    "slot": slot,
                    "time": SLOT_TIMES[slot],
                    "subject": subject,
                    "grade": grade,
                    "lesson": lesson_no,
                    "repeat": slot // len(triple) + 1,
                    "expert": duos[subject]["expert"],
                    "simplifier": duos[subject]["simplifier"],
                })
    return airings


def check_duo_conflicts(airings):
    """A subject - therefore its duo - may hold at most one airing per slot."""
    seen, clashes = {}, []
    for a in airings:
        key = (a["day"], a["slot"], a["subject"])
        if key in seen:
            clashes.append(f"{a['day']} {a['time']} {a['subject']}: "
                           f"G{seen[key]} and G{a['grade']} at once")
        seen[key] = a["grade"]
    return clashes


def check_assistant_conflicts(airings):
    """A grade - therefore its assistant (#35) - may hold at most one airing
    per slot. This is what the previous grid got wrong: it put three
    same-grade sessions in one slot and needed one assistant in three rooms."""
    seen, clashes = {}, []
    for a in airings:
        key = (a["day"], a["slot"], a["grade"])
        if key in seen:
            clashes.append(f"{a['day']} {a['time']} G{a['grade']}: "
                           f"{seen[key]} and {a['subject']} at once")
        seen[key] = a["subject"]
    return clashes


def check_coverage(airings, subjects):
    """Every grade-subject: 3 lessons, each airing exactly 3 times."""
    problems = []
    for subject in subjects:
        for grade in GRADES:
            for lesson in range(1, LESSONS_PER_WEEK + 1):
                n = sum(1 for a in airings if a["subject"] == subject
                        and a["grade"] == grade and a["lesson"] == lesson)
                if n != REPEATS_PER_LESSON:
                    problems.append(f"{subject} G{grade} L{lesson}: {n} airings "
                                    f"(expected {REPEATS_PER_LESSON})")
    return problems


def check_student_clashes(airings):
    """A student can attend everything they take iff their grade never has
    two sessions in one slot - which check_assistant_conflicts already
    proves. Asserted separately because it is a different promise to a
    different person, and it is the one the owner actually cares about."""
    per = {}
    for a in airings:
        per.setdefault((a["grade"], a["day"], a["slot"]), []).append(a["subject"])
    return [f"G{g} {d} slot {s}: {subs}" for (g, d, s), subs in per.items()
            if len(subs) > 1]


def ceiling_report(subjects):
    grade_capacity = SLOTS_PER_DAY * len(DAYS)
    grade_demand = len(subjects) * LESSONS_PER_WEEK * REPEATS_PER_LESSON
    subject_capacity = SLOTS_PER_DAY * len(DAYS)
    subject_demand_per_grade = LESSONS_PER_WEEK * REPEATS_PER_LESSON
    return [
        f"A GRADE's timeline: {SLOTS_PER_DAY} slots x {len(DAYS)} days = "
        f"{grade_capacity} airings/week.",
        f"A grade needs {len(subjects)} subjects x {LESSONS_PER_WEEK} lessons "
        f"x {REPEATS_PER_LESSON} repeats = {grade_demand}.",
        f"  -> {grade_demand}/{grade_capacity} - "
        f"{'EXACTLY FULL' if grade_demand == grade_capacity else 'fits'}. Every "
        f"slot of every day carries one session for each grade.",
        "",
        f"A SUBJECT's timeline: same {subject_capacity} airings/week, and each "
        f"grade costs {subject_demand_per_grade}.",
        f"  -> one duo could carry "
        f"{subject_capacity // subject_demand_per_grade} grades before running "
        f"out of slots.",
        "",
        "So adding a grade adds a CONCURRENT STREAM, not more hours: at each",
        f"slot one more grade airs, needing one more distinct subject. With "
        f"{len(subjects)} subjects the hard ceiling is {len(subjects)} grades.",
        "Grades 8-9 would make 5 streams against 6 subjects - schedulable",
        "WITHOUT new duos. CORRECTION to the earlier entry, which claimed a",
        "second duo per subject was mandatory: that was an artefact of the",
        "old 6-slot two-band grid, not a real limit. Giving lower grades",
        "their own teachers remains a pedagogical choice (a register for",
        "14-year-olds), not a scheduling necessity.",
    ]


def main(argv):
    duos = load_duos()
    subjects = sorted(duos)
    flat = [s for t in TRIPLES for s in t]
    assert sorted(flat) == subjects, (
        f"TRIPLES must cover every subject exactly once: {flat} vs {subjects}")

    airings = build(duos)
    duo_clashes = check_duo_conflicts(airings)
    asst_clashes = check_assistant_conflicts(airings)
    coverage = check_coverage(airings, subjects)
    student = check_student_clashes(airings)

    print(f"{len(airings)} airings/week - {len(GRADES)} concurrent streams x "
          f"{SLOTS_PER_DAY} slots x {len(DAYS)} days")
    print(f"Session {SESSION_MINUTES} min, slots {SLOT_TIMES[0]}-"
          f"{int(SLOT_TIMES[-1][:2]) + 1:02d}:00, no Sunday")
    for label, errs in (("duo double-bookings", duo_clashes),
                        ("assistant double-bookings", asst_clashes),
                        ("coverage problems", coverage),
                        ("student clashes", student)):
        print(f"{label}: {len(errs)}")
        for e in errs[:4]:
            print("   ", e)

    print("\n--- capacity ---")
    for line in ceiling_report(subjects):
        print(line)

    if "--ceiling" in argv:
        return 0
    if duo_clashes or asst_clashes or coverage or student:
        print("\nNOT WRITTEN - the grid fails its own constraints.")
        return 1

    grid = {
        "_comment": [
            "Weekly live-broadcast grid. Generated by",
            "lessons/scripts/broadcast_schedule.py - do not hand-edit.",
            "THE RULE: at any moment exactly one session per grade is on air,",
            "always three different subjects. That alone means no duo is live",
            "twice (different subjects), no assistant is live twice (different",
            "grades, #35), and no student can clash (their grade has exactly",
            "one session per slot).",
            "Sunday carries no broadcast: catch-up, holiday programme, buffer.",
            "The 10-minute office-hours tail is gone - replaced by in-session",
            "MCQs - which is why an hourly slot holds a session.",
        ],
        "session_minutes": SESSION_MINUTES,
        "slot_times": SLOT_TIMES,
        "days": DAYS,
        "grades": GRADES,
        "subject_triples_by_day": {d: TRIPLES[i % len(TRIPLES)]
                                   for i, d in enumerate(DAYS)},
        "lessons_per_week_per_grade_subject": LESSONS_PER_WEEK,
        "repeats_per_lesson": REPEATS_PER_LESSON,
        "verified": {"duo_double_bookings": 0, "assistant_double_bookings": 0,
                     "coverage_problems": 0, "student_clashes": 0},
        "airings": sorted(airings, key=lambda a: (DAYS.index(a["day"]),
                                                 a["slot"], a["grade"])),
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(grid, indent=2) + "\n", encoding="utf-8")
    print(f"\nWritten {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
