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

# Band-layout whiteboard scene for multiplying-three-digit-by-two-digit-numbers (Part 1 Expert
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


class MultiplyingThreeDigitByTwoDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Multiplying by Tens and by One Digit
        self.write_rows(0, "Multiplying by Tens and by One Digit", [
            "345 times 8: 2 400 + 320 + 40",
            "345 times 20 is 690 times 10",
            "That is 6 900",
            "70 times 60 is 4 200",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): The Grid Method
        self.next_band(1)
        self.write_rows(1, "The Grid Method", [
            "Split both numbers by place",
            "345: 300, 40, 5 and 28: 20, 8",
            "Six products, then add",
            "345 times 28 is 9 660",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Long Multiplication in Columns
        self.next_band(2)
        self.write_rows(2, "Long Multiplication in Columns", [
            "144 times 4 is 576",
            "144 times 20 is 2 880",
            "576 + 2 880 = 3 456",
            "Estimate 345 times 28: about 9 000",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``345 times 20 is 690''",
            "``300 times 20 plus 45 times 8''",
            "``Second row with no zero: 3 450''",
            "``No estimate needed''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Times Ten, Times One Digit
        self.next_band(4)
        self.write_rows(4, "Times Ten, Times One Digit", [
            "Times 10: digits move one place left",
            "345 times 20 is 6 900",
            "300 times 8 is 2 400",
            "345 times 8 is 2 760",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Six Boxes
        self.next_band(5)
        self.write_rows(5, "Six Boxes", [
            "Six boxes: 3 parts times 2 parts",
            "Every part times every part",
            "126 times 35: 3 780 + 630",
            "Total R4 410",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Two Rows, Then Add
        self.next_band(6)
        self.write_rows(6, "Two Rows, Then Add", [
            "Row one: times the units",
            "Row two: 0 first, times the tens",
            "Add the rows: 3 456",
            "Estimate to check",
        ], scale=0.9, box=1)

        last = Tex("Split by place value, multiply every part by every part, keep the zero for the tens, and estimate to check.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
