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

# Band-layout whiteboard scene for adding-and-subtracting-five-digit-numbers (Part 1 Expert
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


class AddingAndSubtractingFiveDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Adding in Columns with Carrying
        self.write_rows(0, "Adding in Columns with Carrying", [
            "Line up units under units",
            "Start with the units, carry over 9",
            "24 586 + 18 937 = 43 523",
            "Estimate: 25 000 + 19 000 = 44 000",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Subtracting in Columns with Exchanging
        self.next_band(1)
        self.write_rows(1, "Subtracting in Columns with Exchanging", [
            "Top digit too small: exchange",
            "6 minus 7: exchange a ten, 16 minus 7",
            "24 586 minus 18 937 is 5 649",
            "Check: 18 937 + 5 649 = 24 586",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Subtracting Across Zeros and Adding Many Numbers
        self.next_band(2)
        self.write_rows(2, "Subtracting Across Zeros and Adding Many Numbers", [
            "50 000 minus 23 476",
            "49 999 minus 23 476 is 26 523, add 1",
            "The answer is 26 524",
            "12 345 + 23 456 + 4 789 = 40 590",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Line up numbers on the left''",
            "``Smaller from bigger: 14 451''",
            "``0 minus 6 is 6: 33 476''",
            "``No check needed''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Line Up and Carry
        self.next_band(4)
        self.write_rows(4, "Line Up and Carry", [
            "Units under units",
            "Start on the right",
            "Carry when a column passes 9",
            "36 254 + 27 819 = 64 073",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Exchange When You Need To
        self.next_band(5)
        self.write_rows(5, "Exchange When You Need To", [
            "Top digit too small? Exchange",
            "1 ten becomes 10 units",
            "24 586 minus 18 937 is 5 649",
            "Add back to check",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Zeros and Long Lists
        self.next_band(6)
        self.write_rows(6, "Zeros and Long Lists", [
            "50 000 minus 23 476",
            "Use 49 999, then add 1",
            "26 524",
            "Line up long lists on the right",
        ], scale=0.9, box=1)

        last = Tex("Line up on the right, carry and exchange place by place, and check every answer with an estimate and the inverse.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
