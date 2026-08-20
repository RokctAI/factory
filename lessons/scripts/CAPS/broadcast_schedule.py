# -*- coding: utf-8 -*-
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

"""Generate and PROVE the weekly live-broadcast grid.

THE MODEL (owner, 2026-07-29). A student picks the slot they normally attend
and keeps it - the same time every evening, the way you would keep a
regular class time. If they miss it, THE SAME LESSON comes round again
later that same evening. So:

    one lesson : one day : three airings (17:00, 18:30, 20:00)

If Maths is Monday, then Monday is Maths at 17:00, 18:30 and 20:00 for that
grade: the same lesson three times, not three different subjects. The
three airings are ONE lesson repeated.

WHEN: weekday evenings only - nobody attends extra classes in the morning,
they are at school. Each session is 60 minutes with a 30-minute gap after it
so the platform visibly does housekeeping between classes.

WHAT FALLS OUT: a grade has 5 weekday lesson-days, and there are exactly 5
units to place - because Maths and Mathematical Literacy share a day and a
slot. No student holds both (#29), so nobody can clash, and pairing them is
what makes all six subjects fit into five days. One live lesson per subject
per week, and a student attends one session per weekday evening at their
chosen time.

Saturday (from midday) and Sunday evening carry NO regular lesson: they are
the catch-up, revision and holiday-programme window. Saturday could host a
second lesson-day for two subjects later - noted, not assumed.

Every identity constraint holds: no duo is live twice (the three grades are
on three different subjects in any slot), no assistant is live twice
(different grades), no student can clash (their grade has one subject on air,
and the maths pair is two subjects no student holds together).

Run:  python lessons/scripts/CAPS/broadcast_schedule.py
"""
import json
import sys
from pathlib import Path

LESSONS = Path("lessons")
ROSTER = LESSONS / "tutors" / "roster.json"
OUT = LESSONS / "schedule" / "weekly_grid.json"

SESSION_MINUTES = 60
GAP_MINUTES = 30

# The three airing times. Every lesson airs at all three, on its
# own day - so a student attends whichever one suits them and can
# still catch the lesson later that evening if they miss it.
AIRING_TIMES = ["17:00", "18:30", "20:00"]
LESSON_DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]

# Reserved: no regular lesson airs here. Catch-up, revision, holidays.
RESERVED_SLOTS = {
    "Sat": ["12:00", "13:30", "15:00", "16:30", "18:00", "19:30"],
    "Sun": ["18:00"],
}

GRADES = [10, 11, 12]
MATHS_PAIR = ["maths", "maths_literacy"]


def load_duos():
    return json.loads(ROSTER.read_text(encoding="utf-8"))["subjects"]


def units(subjects):
    """What occupies a lesson-day. The maths pair is ONE unit: both tracks air
    together, in the same slots, because no student holds both."""
    singles = sorted(s for s in subjects if s not in MATHS_PAIR)
    return [sorted(MATHS_PAIR)] + [[s] for s in singles]


def build(duos, subjects):
    unit_list = units(subjects)
    if len(unit_list) != len(LESSON_DAYS):
        raise SystemExit(f"{len(unit_list)} units but {len(LESSON_DAYS)} "
                         f"lesson-days: every unit needs exactly one day")
    airings = []
    for day_idx, day in enumerate(LESSON_DAYS):
        for grade_idx, grade in enumerate(GRADES):
            unit = unit_list[(day_idx + grade_idx) % len(unit_list)]
            for airing_no, time in enumerate(AIRING_TIMES, start=1):
                for subject in unit:
                    airings.append({
                        "day": day, "time": time, "airing": airing_no,
                        "subject": subject, "grade": grade, "lesson": 1,
                        "paired_track": len(unit) > 1,
                        "expert": duos[subject]["expert"],
                        "simplifier": duos[subject]["simplifier"],
                    })
    return airings, unit_list


def check_duo_conflicts(airings):
    """A subject - therefore its duo - at most once in any (day, time)."""
    seen, bad = {}, []
    for a in airings:
        key = (a["day"], a["time"], a["subject"])
        if key in seen:
            bad.append(f"{a['day']} {a['time']} {a['subject']}: "
                       f"G{seen[key]} and G{a['grade']}")
        seen[key] = a["grade"]
    return bad


def check_grade_slots(airings):
    """A grade has ONE subject on air per slot, or exactly the two maths
    tracks. Anything else puts the grade's assistant in the wrong room."""
    per, bad = {}, []
    for a in airings:
        per.setdefault((a["day"], a["time"], a["grade"]), []).append(a["subject"])
    for (day, time, grade), subs in per.items():
        if len(subs) == 1:
            continue
        if sorted(subs) != sorted(MATHS_PAIR):
            bad.append(f"{day} {time} G{grade}: {subs}")
    return bad


def check_one_day_per_subject(airings):
    """THE PROMISE THE MODEL MAKES: a grade's lesson in a subject lives on ONE
    day, airing at all three times. If a subject were spread over two
    days, 'the slot you normally attend' would stop meaning anything."""
    days, times, bad = {}, {}, []
    for a in airings:
        key = (a["grade"], a["subject"])
        days.setdefault(key, set()).add(a["day"])
        times.setdefault(key, set()).add(a["time"])
    for key, d in sorted(days.items()):
        if len(d) != 1:
            bad.append(f"G{key[0]} {key[1]} spread over {sorted(d)}")
        if times[key] != set(AIRING_TIMES):
            bad.append(f"G{key[0]} {key[1]} misses an airing: {sorted(times[key])}")
    return bad


def check_student_load(airings):
    """A student takes one maths track plus the four others: they should have
    exactly one attendable session per weekday evening, at whichever time
    they choose."""
    bad = []
    for grade in GRADES:
        for track in MATHS_PAIR:
            basket = {track} | {a["subject"] for a in airings
                                if a["subject"] not in MATHS_PAIR}
            for time in AIRING_TIMES:
                for day in LESSON_DAYS:
                    mine = {a["subject"] for a in airings
                            if a["grade"] == grade and a["day"] == day
                            and a["time"] == time and a["subject"] in basket}
                    if len(mine) > 1:
                        bad.append(f"G{grade}/{track} {day} {time}: {mine}")
    return bad


def main(argv):
    duos = load_duos()
    subjects = sorted(duos)
    airings, unit_list = build(duos, subjects)

    checks = (("duo double-bookings", check_duo_conflicts(airings)),
              ("illegal grade doublings", check_grade_slots(airings)),
              ("subjects not on a single day", check_one_day_per_subject(airings)),
              ("student clashes", check_student_load(airings)))

    print(f"{len(airings)} airings/week | {len(LESSON_DAYS)} lesson-days x "
          f"{len(AIRING_TIMES)} airings, {len(GRADES)} grades")
    print(f"Session {SESSION_MINUTES} min + {GAP_MINUTES} min housekeeping gap")
    print(f"Units placed: {len(unit_list)} "
          f"({'+'.join(unit_list[0])} share a day) -> one live lesson per "
          f"subject per week")
    print("A student attends ONE session per weekday evening, at the time "
          "they choose.")
    for label, errs in checks:
        print(f"{label}: {len(errs)}")
        for e in errs[:4]:
            print("   ", e)

    if any(errs for _, errs in checks):
        print("\nNOT WRITTEN - the grid fails its own constraints.")
        return 1

    grid = {
        "_comment": [
            "Weekly live-broadcast grid. Generated by",
            "lessons/scripts/CAPS/broadcast_schedule.py - do not hand-edit.",
            "ONE LESSON : ONE DAY : THREE AIRINGS. A student picks the",
            "time they normally attend and keeps it; if they miss it the SAME",
            "lesson comes round again later that evening. The three airings",
            "are three buses, not three lessons.",
            "Weekday evenings only - students are at school by day. Each slot",
            "is a 60-minute session plus a 30-minute housekeeping gap.",
            "Maths and Maths Literacy share a day and a slot: no student holds",
            "both (#29), so nobody clashes, and pairing them is what fits six",
            "subjects into five evenings.",
            "Saturday and Sunday evening carry no regular lesson - catch-up,",
            "revision and the holiday programme live there.",
        ],
        "session_minutes": SESSION_MINUTES,
        "gap_minutes": GAP_MINUTES,
        "airing_times": AIRING_TIMES,
        "lesson_days": LESSON_DAYS,
        "reserved_slots": RESERVED_SLOTS,
        "grades": GRADES,
        "paired_tracks": MATHS_PAIR,
        "lessons_per_subject_per_week": 1,
        "airings_per_lesson": len(AIRING_TIMES),
        "student_live_sessions_per_week": len(LESSON_DAYS),
        "verified": {"duo_double_bookings": 0, "illegal_grade_doublings": 0,
                     "subjects_split_across_days": 0, "student_clashes": 0},
        "airings": sorted(airings, key=lambda a: (LESSON_DAYS.index(a["day"]),
                                                  a["airing"], a["grade"],
                                                  a["subject"])),
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(grid, indent=2) + "\n", encoding="utf-8")
    print(f"\nWritten {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
