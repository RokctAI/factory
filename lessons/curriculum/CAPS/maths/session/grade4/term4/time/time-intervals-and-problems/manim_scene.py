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

# Band-layout whiteboard scene for time-intervals-and-problems (Part 1 Expert
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


class TimeIntervalsAndProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Units of Time
        self.write_rows(0, "Units of Time", [
            "60 s = 1 min, 60 min = 1 h",
            "24 h = 1 day, 7 days = 1 week",
            "12 months = 1 year, 10 years = 1 decade",
            "100 min = 1 h 40 min",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Finding Intervals Between Clock Times
        self.next_band(1)
        self.write_rows(1, "Finding Intervals Between Clock Times", [
            "07:45 to 08:00: 15 min",
            "08:00 to 13:00: 5 h",
            "13:00 to 13:30: 30 min",
            "School day: 5 h 45 min",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Longer Intervals and Time Problems
        self.next_band(2)
        self.write_rows(2, "Longer Intervals and Time Problems", [
            "1994 to 2026: 32 years",
            "10 weeks = 70 days",
            "45 min + 25 min = 1 h 10 min",
            "Mark it on a number line",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``10:35 minus 06:50 is 385''",
            "``100 minutes is 1 hour''",
            "``3 hours 70 minutes''",
            "``Interval when asked for end time''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Units That Fit Together
        self.next_band(4)
        self.write_rows(4, "Units That Fit Together", [
            "60, 60, 24, 7",
            "12 months, 10 years",
            "Big to small: multiply",
            "Small to big: group",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Start to Finish
        self.next_band(5)
        self.write_rows(5, "Start to Finish", [
            "Jump to the next hour",
            "Whole hours",
            "The last bit",
            "Add the jumps",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Years, Weeks and Mixed Problems
        self.next_band(6)
        self.write_rows(6, "Years, Weeks and Mixed Problems", [
            "1994 to 2026: 32 years",
            "10 weeks: 70 days",
            "60 minutes make an hour",
            "4 h 10 min in all",
        ], scale=0.9, box=2)

        last = Tex("60, 60, 24, 7, 12, 10: count on in friendly steps, and turn 60 minutes into an hour.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
