# -*- coding: utf-8 -*-
"""Generate and PROVE the weekly live-broadcast grid.

WHEN (owner, 2026-07-29): nobody attends extra classes in the morning - they
are at school. Weekday evenings only, and the weekend starts at midday. Each
session is followed by a gap so the platform looks like it is doing
housekeeping between classes, so a slot is a 90-minute cycle around a
60-minute session.

THE RULE: at any moment each grade has exactly one session on air, and the
three grades are on three different subjects. That satisfies every identity
constraint at once - no duo live twice (different subjects), no assistant
live twice (different grades, #35), no student clash (their grade has one
session per slot).

THE ONE EXCEPTION, and it is free capacity rather than a compromise: a student
holds Maths OR Mathematical Literacy, never both (#29). So those two subjects
can air SIMULTANEOUSLY for the same grade and no student can ever be in both.
Pairing them recovers a whole subject's worth of slots, which is what makes
2 lessons x 2 repeats fit at all. The cost is that the grade's assistant is on
air twice in a paired slot - invisible to any individual student, and
plausible because the assistant is an AI host, not a human teacher.

VOLUME: 6 subjects x 2 lessons/week x 2 repeats = 24 airings per grade, but
the maths pair shares slots, so 20 SLOTS per grade against 22 available.
A student takes 5 subjects (one maths track), so their week is 10 live
sessions with a choice of two times for each.

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
GAP_MINUTES = 30          # visible housekeeping between sessions

# Weekday evenings only; the weekend opens at midday because students are
# free. Sunday keeps a single evening slot - the rest of Sunday stays clear
# for catch-up and the holiday programme.
DAY_SLOTS = {
    "Mon": ["17:00", "18:30", "20:00"],
    "Tue": ["17:00", "18:30", "20:00"],
    "Wed": ["17:00", "18:30", "20:00"],
    "Thu": ["17:00", "18:30", "20:00"],
    "Fri": ["17:00", "18:30", "20:00"],
    "Sat": ["12:00", "13:30", "15:00", "16:30", "18:00", "19:30"],
    "Sun": ["18:00"],
}

GRADES = [10, 11, 12]
LESSONS_PER_WEEK = 2
REPEATS_PER_LESSON = 2

# The two maths tracks share a slot; every other subject needs its own.
MATHS_PAIR = ["maths", "maths_literacy"]


def load_duos():
    return json.loads(ROSTER.read_text(encoding="utf-8"))["subjects"]


def timeline():
    """Every slot of the week in order: (index, day, time)."""
    out = []
    for day, times in DAY_SLOTS.items():
        for t in times:
            out.append((len(out), day, t))
    return out


def units(subjects):
    """What competes for a slot: the maths pair counts as ONE unit because it
    occupies one slot, the other subjects one unit each."""
    singles = [s for s in subjects if s not in MATHS_PAIR]
    return [list(MATHS_PAIR)] + [[s] for s in singles]


def build(duos, subjects):
    slots = timeline()
    unit_list = units(subjects)
    n_units = len(unit_list)
    airings_per_unit = LESSONS_PER_WEEK * REPEATS_PER_LESSON
    needed = n_units * airings_per_unit
    if needed > len(slots):
        raise SystemExit(f"{needed} slots needed per grade, {len(slots)} exist")

    airings = []
    for grade_idx, grade in enumerate(GRADES):
        # Count each unit's appearances so far, to number lesson and repeat.
        seen = {u: 0 for u in range(n_units)}
        for slot_idx, day, time in slots[:needed]:
            unit = (slot_idx + grade_idx) % n_units
            n = seen[unit]
            seen[unit] += 1
            lesson_no = n // REPEATS_PER_LESSON + 1
            repeat_no = n % REPEATS_PER_LESSON + 1
            for subject in unit_list[unit]:
                airings.append({
                    "day": day, "slot": slot_idx, "time": time,
                    "subject": subject, "grade": grade,
                    "lesson": lesson_no, "repeat": repeat_no,
                    "paired_track": len(unit_list[unit]) > 1,
                    "expert": duos[subject]["expert"],
                    "simplifier": duos[subject]["simplifier"],
                })
    return airings, len(slots), needed


def check_duo_conflicts(airings):
    """A subject - therefore its duo - at most once per slot."""
    seen, clashes = {}, []
    for a in airings:
        key = (a["slot"], a["subject"])
        if key in seen:
            clashes.append(f"{a['day']} {a['time']} {a['subject']}: "
                           f"G{seen[key]} and G{a['grade']}")
        seen[key] = a["grade"]
    return clashes


def check_grade_slots(airings):
    """A grade may hold ONE session per slot, or exactly two when they are the
    two maths tracks (the documented exception). Anything else means the
    grade's assistant is in rooms she has no business being in."""
    per, bad = {}, []
    for a in airings:
        per.setdefault((a["slot"], a["grade"]), []).append(a["subject"])
    for (slot, grade), subs in per.items():
        if len(subs) == 1:
            continue
        if sorted(subs) != sorted(MATHS_PAIR):
            bad.append(f"slot {slot} G{grade}: {subs}")
    return bad


def check_student_clashes(airings):
    """No student may face two of their own subjects at once. A grade's only
    doubling is maths + maths literacy, which no student holds together."""
    per, bad = {}, []
    for a in airings:
        per.setdefault((a["slot"], a["grade"]), []).append(a["subject"])
    for (slot, grade), subs in per.items():
        attendable = [s for s in subs if s not in MATHS_PAIR]
        # One maths track is attendable by any given student, plus any
        # non-maths subject in the same slot would be a real clash.
        if len(attendable) > 1 or (attendable and any(s in MATHS_PAIR for s in subs)):
            bad.append(f"slot {slot} G{grade}: {subs}")
    return bad


def check_coverage(airings, subjects):
    problems = []
    for subject in subjects:
        for grade in GRADES:
            for lesson in range(1, LESSONS_PER_WEEK + 1):
                n = sum(1 for a in airings if a["subject"] == subject
                        and a["grade"] == grade and a["lesson"] == lesson)
                if n != REPEATS_PER_LESSON:
                    problems.append(f"{subject} G{grade} L{lesson}: {n} "
                                    f"(expected {REPEATS_PER_LESSON})")
    return problems


def main(argv):
    duos = load_duos()
    subjects = sorted(duos)
    airings, total_slots, used = build(duos, subjects)

    duo_clashes = check_duo_conflicts(airings)
    grade_bad = check_grade_slots(airings)
    student_bad = check_student_clashes(airings)
    coverage = check_coverage(airings, subjects)

    print(f"{len(airings)} airings/week | {used} of {total_slots} slots used "
          f"per grade ({total_slots - used} spare)")
    print(f"Session {SESSION_MINUTES} min + {GAP_MINUTES} min housekeeping gap")
    print(f"Volume: {LESSONS_PER_WEEK} lesson(s)/subject/week x "
          f"{REPEATS_PER_LESSON} repeats; a student takes 5 subjects -> "
          f"{5 * LESSONS_PER_WEEK} live sessions/week")
    for label, errs in (("duo double-bookings", duo_clashes),
                        ("illegal grade doublings", grade_bad),
                        ("student clashes", student_bad),
                        ("coverage problems", coverage)):
        print(f"{label}: {len(errs)}")
        for e in errs[:4]:
            print("   ", e)

    if "--ceiling" in argv:
        per_grade_capacity = total_slots
        print(f"\nA grade has {per_grade_capacity} slots/week. One unit "
              f"(subject, or the maths pair) costs "
              f"{LESSONS_PER_WEEK * REPEATS_PER_LESSON}.")
        print(f"So a grade supports "
              f"{per_grade_capacity // (LESSONS_PER_WEEK * REPEATS_PER_LESSON)} "
              f"units; we use {len(units(subjects))}.")
        print("Adding a grade adds a concurrent stream, not hours: it needs "
              "one more distinct subject per slot.")
        return 0

    if duo_clashes or grade_bad or student_bad or coverage:
        print("\nNOT WRITTEN - the grid fails its own constraints.")
        return 1

    grid = {
        "_comment": [
            "Weekly live-broadcast grid. Generated by",
            "lessons/scripts/broadcast_schedule.py - do not hand-edit.",
            "Weekday evenings only (students are at school by day); weekend",
            "opens at midday; one Sunday evening slot. Each slot is a",
            "90-minute cycle: a 60-minute session plus a visible",
            "housekeeping gap.",
            "THE RULE: one session per grade per slot, three grades on three",
            "different subjects - so no duo and no assistant is ever live",
            "twice and no student can clash.",
            "THE EXCEPTION: maths and maths literacy air in the SAME slot for",
            "a grade. No student holds both (#29), so nobody can clash, and",
            "pairing them recovers a subject's worth of slots - which is what",
            "makes 2 lessons x 2 repeats fit. The grade's assistant is on air",
            "twice in those slots: invisible to any one student, and",
            "plausible because she is an AI host, not a human teacher.",
        ],
        "session_minutes": SESSION_MINUTES,
        "gap_minutes": GAP_MINUTES,
        "day_slots": DAY_SLOTS,
        "grades": GRADES,
        "lessons_per_week_per_grade_subject": LESSONS_PER_WEEK,
        "repeats_per_lesson": REPEATS_PER_LESSON,
        "paired_tracks": MATHS_PAIR,
        "slots_used_per_grade": used,
        "slots_available_per_grade": total_slots,
        "student_live_sessions_per_week": 5 * LESSONS_PER_WEEK,
        "verified": {"duo_double_bookings": 0, "illegal_grade_doublings": 0,
                     "student_clashes": 0, "coverage_problems": 0},
        "airings": sorted(airings, key=lambda a: (a["slot"], a["grade"],
                                                  a["subject"])),
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(grid, indent=2) + "\n", encoding="utf-8")
    print(f"\nWritten {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
