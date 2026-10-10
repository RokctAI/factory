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

# Band-layout whiteboard scene for calendars-and-time-intervals (Part 1 Expert
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


class CalendarsAndTimeIntervalsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Reading Calendars
        self.write_rows(0, "Reading Calendars", [
            "7 days a week, 12 months a year",
            "30 days: April, June, September, November",
            "1 Sept Monday, so 22 Sept Monday",
            "24 September: Wednesday",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Intervals in Hours, Minutes and Seconds
        self.next_band(1)
        self.write_rows(1, "Intervals in Hours, Minutes and Seconds", [
            "07:30 to 08:00: 30 minutes",
            "08:00 to 14:00: 6 hours",
            "14:00 to 14:15: 15 minutes",
            "Total: 6 hours 45 minutes",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Years, Decades and Centuries
        self.next_band(2)
        self.write_rows(2, "Years, Decades and Centuries", [
            "Decade: 10 years",
            "Century: 100 years",
            "1918 to 2018: one century",
            "1994 to 2024: three decades",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``14:15 minus 07:30 = 6 h 85 min''",
            "``Every month has 30 days''",
            "``A decade is 100 years''",
            "``February always has 28 days''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Find the Day
        self.next_band(4)
        self.write_rows(4, "Find the Day", [
            "Find the day",
            "Jump by 7",
            "Monday, Monday, Monday",
            "Then Wednesday",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Count On
        self.next_band(5)
        self.write_rows(5, "Count On", [
            "Count on",
            "To the next hour",
            "Whole hours",
            "Minutes left",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Long Stretches
        self.next_band(6)
        self.write_rows(6, "Long Stretches", [
            "Long stretches",
            "Decade: 10",
            "Century: 100",
            "Millennium: 1 000",
        ], scale=0.9, box=2)

        last = Tex("Count on through the clock and the calendar: 60 minutes an hour, 7 days a week, 10 years a decade.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
