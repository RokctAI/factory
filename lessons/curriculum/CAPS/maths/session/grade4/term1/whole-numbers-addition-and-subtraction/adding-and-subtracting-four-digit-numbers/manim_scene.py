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

# Band-layout whiteboard scene for adding-and-subtracting-four-digit-numbers (Part 1 Expert
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


class AddingAndSubtractingFourDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Column Addition with Carrying
        self.write_rows(0, "Column Addition with Carrying", [
            "Units under units, tens under tens",
            "Start from the units column",
            "8 plus 5 is 13: write 3, carry 1",
            "2 468 plus 1 795 is 4 263",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Column Subtraction with Exchanging
        self.next_band(1)
        self.write_rows(1, "Column Subtraction with Exchanging", [
            "Too small to subtract? Exchange",
            "1 ten becomes 10 units",
            "7 162 minus 5 324 is 1 838",
            "Check: add the answer back",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Subtracting Across Zeros
        self.next_band(2)
        self.write_rows(2, "Subtracting Across Zeros", [
            "Zeros: exchange from the thousands",
            "4 000 becomes 3, 9, 9 and 10",
            "Or do 3 999 minus 2 637, then add 1",
            "4 000 minus 2 637 is 1 363",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Start from the thousands''",
            "``Write 13 in the units column''",
            "``Too small? Swap the digits''",
            "``Exchange but keep the 6''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Add in Columns
        self.next_band(4)
        self.write_rows(4, "Add in Columns", [
            "Line up the columns",
            "Start with the units",
            "13: write 3, carry 1",
            "R4 263 altogether",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Take Away in Columns
        self.next_band(5)
        self.write_rows(5, "Take Away in Columns", [
            "Units first",
            "Too small? Exchange one from the left",
            "6 tens and 2 units become 5 tens and 12",
            "1 838 plus 5 324 is 7 162",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): When There Are Zeros
        self.next_band(6)
        self.write_rows(6, "When There Are Zeros", [
            "Zeros: exchange from the thousands",
            "4 000 is 3 999 plus 1",
            "3 999 minus 2 637 is 1 362",
            "Add the 1 back: 1 363",
        ], scale=0.9, box=1)

        last = Tex("Columns by place, units first, carry or exchange, then check by estimating or adding back.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
