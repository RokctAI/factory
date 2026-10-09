# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for clocks-stopwatches-and-calendars (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/160/160/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ClocksStopwatchesAndCalendarsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=box_color)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(42)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Seconds and Stopwatches
        self.write_rows(0, "Seconds and Stopwatches", [
            "60 seconds = 1 minute",
            "Stopwatch 00:15: 15 seconds",
            "Shortest time wins",
            "2 min 45 s = 165 s",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Reading a Calendar
        self.next_band(1)
        self.write_rows(1, "Reading a Calendar", [
            "7 days in a week, 12 months",
            "30 days: September, April, June, November",
            "365 days, leap year 366",
            "24/09/2026: day, month, year",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Using a Calendar to Count and Plan
        self.next_band(2)
        self.write_rows(2, "Using a Calendar to Count and Plan", [
            "Down a column: 7 days later",
            "1 March Sunday: 22 March Sunday",
            "24 March is a Tuesday",
            "Date and time together",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Longest time wins''",
            "``2 min 45 s = 245 s''",
            "``Every month has 30 days''",
            "``Count every single day''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Ready, Set, Stop
        self.next_band(4)
        self.write_rows(4, "Ready, Set, Stop", [
            "60 seconds in a minute",
            "Start, stop, read",
            "Shortest time wins",
            "2 min 45 s = 165 s",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Months and Days
        self.next_band(5)
        self.write_rows(5, "Months and Days", [
            "12 months, 7-day weeks",
            "30: Sep, Apr, Jun, Nov",
            "February: 28 or 29",
            "Leap year: 366 days",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Count in Weeks
        self.next_band(6)
        self.write_rows(6, "Count in Weeks", [
            "Down a row: 7 days",
            "Count in sevens",
            "Sundays: 1, 8, 15, 22, 29",
            "Date and time",
        ], scale=0.9, box=1)

        last = Tex("60 seconds in a minute, shortest time wins, thirty days for September, April, June and November, and count in sevens.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
