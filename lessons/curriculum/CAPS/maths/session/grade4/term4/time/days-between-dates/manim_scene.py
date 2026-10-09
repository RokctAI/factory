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

# Band-layout whiteboard scene for days-between-dates (Part 1 Expert
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


class DaysBetweenDatesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Days Within One Month
        self.write_rows(0, "Days Within One Month", [
            "3 March to 10 March: 7 days",
            "Count the jumps",
            "12 May to 25 May: 13 days",
            "Including both days: one more",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Days Across Months
        self.next_band(1)
        self.write_rows(1, "Days Across Months", [
            "To the end of the month",
            "Add whole months",
            "Add days into the last month",
            "20 April to 15 May: 10 + 15 = 25",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Days Across the New Year
        self.next_band(2)
        self.write_rows(2, "Days Across the New Year", [
            "9 Dec to 31 Dec: 22 days",
            "Plus 14 days to 14 January",
            "Total 36 days",
            "Estimate: about 30 days a month",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3 to 10 March is 8 days''",
            "``Every month has 30 days''",
            "``Skip the end of April''",
            "``Stop at 31 December''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Same Month
        self.next_band(4)
        self.write_rows(4, "Same Month", [
            "Subtract the dates",
            "Count jumps",
            "10 minus 3: 7 days",
            "25 minus 12: 13 days",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Across Months
        self.next_band(5)
        self.write_rows(5, "Across Months", [
            "End of the month first",
            "Whole months next",
            "Days into the last month",
            "Add them up",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Into the New Year
        self.next_band(6)
        self.write_rows(6, "Into the New Year", [
            "To 31 December",
            "Into January",
            "22 + 14 = 36",
            "Estimate to check",
        ], scale=0.9, box=2)

        last = Tex("Count the jumps: to the end of the month, whole months, then into the last month.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
