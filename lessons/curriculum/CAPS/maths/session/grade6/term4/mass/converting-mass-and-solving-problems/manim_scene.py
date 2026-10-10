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
        # --- Band 0 (subtopic_1): Kilograms to Grams
        self.write_rows(0, "Kilograms to Grams", [
            "1 kg = 1 000 g",
            "3,5 kg = 3 500 g",
            "1,25 kg = 1 250 g",
            "3/4 kg = 750 g",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Grams to Kilograms
        self.next_band(1)
        self.write_rows(1, "Grams to Kilograms", [
            "4 750 g = 4,75 kg",
            "4 750 g = 4 and 3/4 kg",
            "600 g = 0,6 kg = 3/5 kg",
            "250 g = 1/4 kg",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Solving Mass Problems
        self.next_band(2)
        self.write_rows(2, "Solving Mass Problems", [
            "12 times 250 g = 3 kg",
            "2,5 + 3 + 0,75 = 6,25 kg",
            "6 000 g divided by 8 = 750 g",
            "500 divided by 18: 27 crates",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3,5 kg = 350 g''",
            "``4 750 g = 47,5 kg''",
            "``3/4 kg = 75 g''",
            "``2,5 kg + 750 g = 752,5''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Kilograms to Grams: Multiply
        self.next_band(4)
        self.write_rows(4, "Kilograms to Grams: Multiply", [
            "Kilograms to grams",
            "Multiply by 1 000",
            "3,5 kg is 3 500 g",
            "3/4 kg is 750 g",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Grams to Kilograms: Divide
        self.next_band(5)
        self.write_rows(5, "Grams to Kilograms: Divide", [
            "Grams to kilograms",
            "Divide by 1 000",
            "4 750 g is 4,75 kg",
            "250 g is a quarter",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Same Unit, Then Solve
        self.next_band(6)
        self.write_rows(6, "Same Unit, Then Solve", [
            "Same unit, then solve",
            "Change first",
            "Add or share",
            "Check the remainder",
        ], scale=0.9, box=0)

        last = Tex("1 kg is 1 000 g: multiply to get grams, divide to get kilograms, and use the same unit before you calculate.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
