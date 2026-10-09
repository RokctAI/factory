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

# Band-layout whiteboard scene for multiplying-two-digit-numbers (Part 1 Expert
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


class MultiplyingTwoDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Two-Digit by One-Digit
        self.write_rows(0, "Two-Digit by One-Digit", [
            "24 is 20 plus 4",
            "6 times 20 is 120, 6 times 4 is 24",
            "120 plus 24 is 144",
            "Estimate: 25 times 6 is 150",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): The Grid Method for Two-Digit by Two-Digit
        self.next_band(1)
        self.write_rows(1, "The Grid Method for Two-Digit by Two-Digit", [
            "Break both: 20 plus 3, 10 plus 4",
            "Four cells: 200, 30, 80, 12",
            "200 plus 30 plus 80 plus 12 is 322",
            "Two cells only gives a wrong 212",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Bigger Grids and Choosing the Easier Way
        self.next_band(2)
        self.write_rows(2, "Bigger Grids and Choosing the Easier Way", [
            "36 times 25: 600, 120, 150, 30",
            "Total 900 bricks",
            "25 times 4 is 100, times 9 is 900",
            "Line up partial products by place",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``24 times 6 is 24''",
            "``23 times 14 needs two products''",
            "``6 times 20 is 12''",
            "``Add products without columns''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Split the Number, Then Add
        self.next_band(4)
        self.write_rows(4, "Split the Number, Then Add", [
            "Split 24 into 20 and 4",
            "6 times 20 is 120",
            "6 times 4 is 24",
            "120 plus 24 is 144",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): The Grid for Two Numbers
        self.next_band(5)
        self.write_rows(5, "The Grid for Two Numbers", [
            "Split both numbers",
            "Four boxes, four products",
            "200, 30, 80, 12",
            "Add them: 322",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Big Walls and Smart Shortcuts
        self.next_band(6)
        self.write_rows(6, "Big Walls and Smart Shortcuts", [
            "600, 120, 150, 30",
            "900 bricks",
            "25 times 4 is 100",
            "Line up the products",
        ], scale=0.9, box=2)

        last = Tex("Split into tens and units, multiply every part, add the products, and estimate to check.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
