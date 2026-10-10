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

# Band-layout whiteboard scene for dividing-four-digit-by-three-digit-numbers (Part 1 Expert
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


class DividingFourDigitByThreeDigitNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Estimating and Building a Multiples Table
        self.write_rows(0, "Estimating and Building a Multiples Table", [
            "Estimate: 8 400 divided by 120 = 70",
            "Multiples of 124",
            "124, 248, 372, 496, 620",
            "744, 868, 992, 1 116",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Long Division Step by Step
        self.next_band(1)
        self.write_rows(1, "Long Division Step by Step", [
            "Divide, multiply, subtract, bring down",
            "843 minus 744 = 99",
            "Bring down 2: 992 = 124 times 8",
            "8 432 divided by 124 = 68",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Zeros and Remainders
        self.next_band(2)
        self.write_rows(2, "Zeros and Remainders", [
            "5 000 divided by 135 = 37 remainder 5",
            "Remainder smaller than the divisor",
            "6 150 divided by 205 = 30",
            "Check: 37 times 135 + 5 = 5 000",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``8 432 divided by 124 = 680''",
            "``6 150 divided by 205 = 3''",
            "``Remainder bigger than the divisor''",
            "``Checking without adding the remainder''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Guess, Then List
        self.next_band(4)
        self.write_rows(4, "Guess, Then List", [
            "Estimate first",
            "About 70",
            "List the multiples",
            "Look up the one that fits",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Divide, Multiply, Subtract, Bring Down
        self.next_band(5)
        self.write_rows(5, "Divide, Multiply, Subtract, Bring Down", [
            "Divide",
            "Multiply",
            "Subtract, bring down",
            "68 seats in each row",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Leftovers and Zeros
        self.next_band(6)
        self.write_rows(6, "Leftovers and Zeros", [
            "Leftovers: the remainder",
            "37 remainder 5",
            "Bring down a 0: write a 0",
            "30, not 3",
        ], scale=0.9, box=1)

        last = Tex("Estimate, list the multiples, then divide, multiply, subtract and bring down, and check by multiplying and adding the remainder.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
