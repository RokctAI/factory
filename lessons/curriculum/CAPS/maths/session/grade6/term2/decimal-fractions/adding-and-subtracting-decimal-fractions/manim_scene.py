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

# Band-layout whiteboard scene for adding-and-subtracting-decimal-fractions (Part 1 Expert
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


class AddingAndSubtractingDecimalFractionsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Adding Decimals
        self.write_rows(0, "Adding Decimals", [
            "Line up the commas",
            "2,8 becomes 2,80",
            "3,45 + 2,80 = 6,25",
            "R16,99 + R24,50 + R32,75 = R74,24",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Subtracting Decimals
        self.next_band(1)
        self.write_rows(1, "Subtracting Decimals", [
            "10 becomes 10,00",
            "10,00 minus 6,25 = 3,75",
            "R100,00 minus R74,24 = R25,76",
            "5,30 minus 2,46 = 2,84",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Estimating and Checking
        self.next_band(2)
        self.write_rows(2, "Estimating and Checking", [
            "Estimate: 17 + 25 + 33 = 75",
            "R74,24 is close to R75",
            "Check: 25,76 + 74,24 = 100",
            "Check: 6,25 minus 2,8 = 3,45",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3,45 + 2,8 = 3,73''",
            "``5,3 minus 2,46 = 3,16''",
            "``0,8 + 0,5 = 0,13''",
            "``10 minus 6,25 = 4,25''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Commas in a Line
        self.next_band(4)
        self.write_rows(4, "Commas in a Line", [
            "Commas in a line",
            "Units under units",
            "Tenths under tenths",
            "Fill gaps with zeros",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Take Away with Zeros
        self.next_band(5)
        self.write_rows(5, "Take Away with Zeros", [
            "Take away with zeros",
            "10 is 10,00",
            "Borrow as usual",
            "3,75 km left",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Guess, Then Check
        self.next_band(6)
        self.write_rows(6, "Guess, Then Check", [
            "Guess, then check",
            "Estimate: about R75",
            "Exact: R74,24",
            "Add back to check",
        ], scale=0.9, box=1)

        last = Tex("Line up the commas, fill gaps with zeros, then add or subtract exactly as with whole numbers.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
