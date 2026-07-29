# -*- coding: utf-8 -*-
"""Generate and PROVE the weekly live-broadcast grid.

The scarce resource is the DUO, not the timeslot: one Expert + one Simplifier
hold a subject across every grade, and they appear in the same session (expert
before the break, simplifier after). So "no tutor is live twice at once"
reduces to one rule - A SUBJECT NEVER HAS TWO AIRINGS IN THE SAME SLOT. Model
each subject as its own channel and the rule stops being a check you can
forget and becomes the shape of the grid.

Owner-given facts:
  * a duo holds its subject across all 3 grades (10-12);
  * each grade-subject gets 3 lessons per week;
  * each lesson airs in 3 timeslots (same day - morning/afternoon/evening);
  * the platform broadcasts every day.

The second constraint is the STUDENT's: a student must be able to attend all
their subjects. With three airings per lesson they need one airing per subject
that clashes with nothing else they take - a system of distinct
representatives. This script proves one exists for every realistic basket,
by matching, rather than assuming it.

Run:  python lessons/scripts/broadcast_schedule.py
      python lessons/scripts/broadcast_schedule.py --ceiling   # grade capacity
"""
import json
import sys
from itertools import combinations
from pathlib import Path

LESSONS = Path("lessons")
ROSTER = LESSONS / "tutors" / "roster.json"
OUT = LESSONS / "schedule" / "weekly_grid.json"

# A session is the 5-minute assistant open plus the lesson; an hour holds it
# with changeover. Six slots is an after-school broadcast day.
SLOT_TIMES = ["14:00", "15:00", "16:00", "17:00", "18:00", "19:00"]
SESSION_MINUTES = 60

# Sunday carries no regular broadcasts: it is the catch-up/holiday-programme
# day and the buffer when a week slips.
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
LESSON_DAYS = {"early": ["Mon", "Wed", "Fri"], "late": ["Tue", "Thu", "Sat"]}

GRADES = [10, 11, 12]
LESSONS_PER_WEEK = 3
REPEATS_PER_LESSON = 3

# Two interleaved bands so a subject can carry two grades in one day without
# ever overlapping itself, and so not every subject airs the same grade at the
# same hour (which would leave a student unable to attend more than one).
BAND_A = [0, 2, 4]
BAND_B = [1, 3, 5]

# Grade -> which days its lessons land on. Grades 10 and 11 share the early
# days (one on each band); grade 12 takes the late days. The late days'
# second band is deliberately empty - that is where a 4th grade goes.
GRADE_PLAN = {10: ("early", "primary"),
              11: ("early", "secondary"),
              12: ("late", "primary")}


def load_subjects():
    data = json.loads(ROSTER.read_text(encoding="utf-8"))
    return sorted(data["subjects"]), data["subjects"]


def build(subjects, duos):
    """One airing = {day, slot, subject, grade, lesson}. Deterministic."""
    airings = []
    for idx, subject in enumerate(subjects):
        primary = BAND_A if idx % 2 == 0 else BAND_B
        secondary = BAND_B if idx % 2 == 0 else BAND_A
        bands = {"primary": primary, "secondary": secondary}
        for grade, (day_set, band_name) in GRADE_PLAN.items():
            days = LESSON_DAYS[day_set]
            band = bands[band_name]
            for lesson_no, day in enumerate(days, start=1):
                for repeat_no, slot in enumerate(band, start=1):
                    airings.append({
                        "day": day,
                        "slot": slot,
                        "time": SLOT_TIMES[slot],
                        "subject": subject,
                        "grade": grade,
                        "lesson": lesson_no,
                        "repeat": repeat_no,
                        "expert": duos[subject]["expert"],
                        "simplifier": duos[subject]["simplifier"],
                    })
    return airings


def check_tutor_conflicts(airings):
    """THE constraint: a subject (therefore its duo) may hold at most one
    airing in any (day, slot)."""
    seen, clashes = {}, []
    for a in airings:
        key = (a["day"], a["slot"], a["subject"])
        if key in seen:
            clashes.append((key, seen[key], (a["grade"], a["lesson"])))
        seen[key] = (a["grade"], a["lesson"])
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
                    problems.append(f"{subject} G{grade} lesson {lesson}: "
                                    f"{n} airings (expected {REPEATS_PER_LESSON})")
    return problems


def _matches(basket, slots_by_subject):
    """Can the student attend every subject in [basket]? Bipartite matching
    of subject -> slot (Hopcroft-Karp is overkill for six subjects)."""
    assign = {}

    def try_one(subject, blocked):
        for slot in slots_by_subject[subject]:
            if slot in blocked:
                continue
            blocked.add(slot)
            holder = assign.get(slot)
            if holder is None or try_one(holder, blocked):
                assign[slot] = subject
                return True
        return False

    for subject in basket:
        if not try_one(subject, set()):
            return False
    return True


def check_student_baskets(airings, subjects):
    """A student must be able to attend everything they take, on every day
    those subjects air. Maths and Maths Literacy are mutually exclusive
    (product decision #29), so no basket holds both."""
    failures = []
    core, lit = "maths", "maths_literacy"
    others = [s for s in subjects if s not in (core, lit)]
    baskets = []
    for maths_choice in (core, lit):
        for size in range(1, len(others) + 1):
            for rest in combinations(others, size):
                baskets.append((maths_choice,) + rest)

    for grade in GRADES:
        day_set, _ = GRADE_PLAN[grade]
        for day in LESSON_DAYS[day_set]:
            slots_by_subject = {}
            for subject in subjects:
                slots_by_subject[subject] = sorted(
                    a["slot"] for a in airings if a["subject"] == subject
                    and a["grade"] == grade and a["day"] == day)
            for basket in baskets:
                if not _matches(list(basket), slots_by_subject):
                    failures.append(f"G{grade} {day}: {', '.join(basket)}")
    return failures, len(baskets)


def ceiling_report(subjects):
    """How many grades one duo per subject can carry before it must be live
    twice at once. This is the arithmetic behind 'adding a lower grade needs
    NEW teachers'."""
    per_subject_capacity = len(DAYS) * len(SLOT_TIMES)
    per_grade_demand = LESSONS_PER_WEEK * REPEATS_PER_LESSON
    max_grades = per_subject_capacity // per_grade_demand
    lines = [
        f"One subject channel: {len(DAYS)} broadcast days x "
        f"{len(SLOT_TIMES)} slots = {per_subject_capacity} airings/week.",
        f"One grade costs {LESSONS_PER_WEEK} lessons x "
        f"{REPEATS_PER_LESSON} repeats = {per_grade_demand} airings/week.",
        f"So ONE DUO CAN CARRY AT MOST {max_grades} GRADES.",
        f"  grades 10-12 (3): {3 * per_grade_demand}/{per_subject_capacity} - fits",
        f"  adding grade 9 (4): {4 * per_grade_demand}/{per_subject_capacity} - "
        f"{'fits, no slack' if 4 * per_grade_demand <= per_subject_capacity else 'DOES NOT FIT'}",
        f"  adding grades 8-9 (5): {5 * per_grade_demand}/{per_subject_capacity} - "
        f"{'fits' if 5 * per_grade_demand <= per_subject_capacity else 'DOES NOT FIT - a SECOND duo per subject is required'}",
        "",
        "The late days' second band is left empty on purpose: that is where a",
        "4th grade lands without touching grades 10-12.",
    ]
    return lines


def main(argv):
    subjects, duos = load_subjects()
    airings = build(subjects, duos)

    clashes = check_tutor_conflicts(airings)
    coverage = check_coverage(airings, subjects)
    basket_failures, basket_count = check_student_baskets(airings, subjects)

    print(f"{len(airings)} airings/week across {len(subjects)} subjects, "
          f"{len(GRADES)} grades.")
    print(f"Tutor double-bookings: {len(clashes)}")
    for c in clashes[:5]:
        print("   ", c)
    print(f"Coverage problems: {len(coverage)}")
    for c in coverage[:5]:
        print("   ", c)
    print(f"Student baskets tested: {basket_count} per grade-day; "
          f"unattendable: {len(basket_failures)}")
    for f in basket_failures[:5]:
        print("   ", f)

    print("\n--- grade ceiling ---")
    for line in ceiling_report(subjects):
        print(line)

    if "--ceiling" in argv:
        return 0
    if clashes or coverage or basket_failures:
        print("\nNOT WRITTEN - the grid does not satisfy its own constraints.")
        return 1

    grid = {
        "_comment": [
            "Weekly live-broadcast grid. Generated by",
            "lessons/scripts/broadcast_schedule.py - do not hand-edit.",
            "The DUO is the scarce resource: one Expert + Simplifier hold a",
            "subject across all grades and share a session, so the rule is",
            "'a subject never has two airings in one slot'. Each subject is",
            "its own channel, which makes that structural.",
            "Sunday carries no regular broadcasts (catch-up, holiday",
            "programme, and slip buffer).",
        ],
        "session_minutes": SESSION_MINUTES,
        "slot_times": SLOT_TIMES,
        "days": DAYS,
        "grades": GRADES,
        "lessons_per_week_per_grade_subject": LESSONS_PER_WEEK,
        "repeats_per_lesson": REPEATS_PER_LESSON,
        "verified": {
            "tutor_double_bookings": 0,
            "coverage_problems": 0,
            "unattendable_student_baskets": 0,
            "baskets_tested_per_grade_day": basket_count,
        },
        "airings": sorted(airings, key=lambda a: (DAYS.index(a["day"]),
                                                  a["slot"], a["subject"])),
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(grid, indent=2) + "\n", encoding="utf-8")
    print(f"\nWritten {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
