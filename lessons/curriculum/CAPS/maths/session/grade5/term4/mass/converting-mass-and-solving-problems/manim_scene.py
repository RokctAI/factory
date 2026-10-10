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

# Band-layout whiteboard scene for converting-mass-and-solving-problems (Part 1 Expert
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


class ConvertingMassAndSolvingProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Kilograms to Grams and Back
        self.write_rows(0, "Kilograms to Grams and Back", [
            "1 kg is 1 000 g",
            "3 kg is 3 000 g",
            "1 kg 50 g is 1 050 g",
            "4 600 g is 4 kg 600 g",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Fractions of a Kilogram
        self.next_band(1)
        self.write_rows(1, "Fractions of a Kilogram", [
            "Half a kilogram: 500 g",
            "Quarter: 250 g",
            "Three quarters: 750 g",
            "2 and 1/2 kg is 2 500 g",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Solving Mass Problems
        self.next_band(2)
        self.write_rows(2, "Solving Mass Problems", [
            "2 500 divided by 500 is 5",
            "1 000 minus 350 is 650 g",
            "12 times 75 is 900 g",
            "2 400 + 1 750 = 4 150 g",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3 kg is 300 g''",
            "``A quarter kilogram is 25 g''",
            "``1 kg 50 g is 150 g''",
            "``1 minus 350''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Times or Divide by 1 000
        self.next_band(4)
        self.write_rows(4, "Times or Divide by 1 000", [
            "Times or divide by 1 000",
            "3 kg: 3 000 g",
            "4 600 g: 4 kg 600 g",
            "Check the size",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Parts of a Kilogram
        self.next_band(5)
        self.write_rows(5, "Parts of a Kilogram", [
            "Parts of a kilogram",
            "Half: 500 g",
            "Quarter: 250 g",
            "Three quarters: 750 g",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Bake and Calculate
        self.next_band(6)
        self.write_rows(6, "Bake and Calculate", [
            "Bake and calculate",
            "5 batches",
            "650 g left",
            "900 g of muffins",
        ], scale=0.9, box=1)

        last = Tex("Multiply or divide by 1 000, find fractions of 1 000 g, and change every mass to grams before you solve.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
