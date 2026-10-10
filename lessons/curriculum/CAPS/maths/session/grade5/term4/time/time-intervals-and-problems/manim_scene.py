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
        # --- Band 0 (subtopic_1): Units of Time and Converting
        self.write_rows(0, "Units of Time and Converting", [
            "60 seconds: 1 minute",
            "60 minutes: 1 hour",
            "24 hours: 1 day",
            "10 years: 1 decade",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Finding Time Intervals
        self.next_band(1)
        self.write_rows(1, "Finding Time Intervals", [
            "06:45 to 07:00: 15 minutes",
            "07:00 to 10:00: 3 hours",
            "10:00 to 10:20: 20 minutes",
            "Total: 3 hours 35 minutes",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Solving Time Problems
        self.next_band(2)
        self.write_rows(2, "Solving Time Problems", [
            "15:30 plus 2 hours: 17:30",
            "Plus 45 minutes: 18:15",
            "19:00 back 1 hour 30: 17:30",
            "1926 to 2026: 10 decades",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3 hours 75 minutes''",
            "``150 minutes is 1 hour 50''",
            "``17:75''",
            "``A decade is 100 years''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Know Your Units
        self.next_band(4)
        self.write_rows(4, "Know Your Units", [
            "Know your units",
            "60 seconds, 60 minutes",
            "24 hours, 7 days",
            "12 months, 10 years",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Count On
        self.next_band(5)
        self.write_rows(5, "Count On", [
            "Count on",
            "To the next hour",
            "Whole hours",
            "To the end time",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): When Does It End?
        self.next_band(6)
        self.write_rows(6, "When Does It End?", [
            "When does it end?",
            "Add the hours",
            "Then the minutes",
            "18:15",
        ], scale=0.9, box=1)

        last = Tex("Remember that time counts in 60s, count on to the next hour and then in whole hours, and check that every answer makes sense.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
