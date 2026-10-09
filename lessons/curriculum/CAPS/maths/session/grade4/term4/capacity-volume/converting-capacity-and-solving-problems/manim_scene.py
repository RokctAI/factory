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

# Band-layout whiteboard scene for converting-capacity-and-solving-problems (Part 1 Expert
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


class ConvertingCapacityAndSolvingProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Changing Litres and Millilitres
        self.write_rows(0, "Changing Litres and Millilitres", [
            "1 l = 1 000 ml",
            "2 l 400 ml = 2 400 ml",
            "4 600 ml = 4 l 600 ml",
            "1 l 50 ml = 1 050 ml",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Fractions of a Litre
        self.next_band(1)
        self.write_rows(1, "Fractions of a Litre", [
            "Half a litre: 500 ml",
            "A quarter: 250 ml",
            "Three quarters: 750 ml",
            "One and a half: 1 500 ml",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Solving Capacity Problems
        self.next_band(2)
        self.write_rows(2, "Solving Capacity Problems", [
            "2 500 ml + 750 ml = 3 250 ml",
            "5 000 ml - 1 800 ml = 3 200 ml",
            "12 times 250 ml = 3 l",
            "5 l fills 20 cups of 250 ml",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1 l 50 ml = 1 500 ml''",
            "``A quarter litre is 25 ml''",
            "``Answer: 2 l 1 250 ml''",
            "``The answer is 3 250''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): A Thousand Millilitres
        self.next_band(4)
        self.write_rows(4, "A Thousand Millilitres", [
            "Times 1 000",
            "2 l 400 ml is 2 400 ml",
            "4 600 ml is 4 l 600 ml",
            "Watch the zeros",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Half and Quarter Litres
        self.next_band(5)
        self.write_rows(5, "Half and Quarter Litres", [
            "Half: 500 ml",
            "Quarter: 250 ml",
            "Three quarters: 750 ml",
            "One and a half: 1 500 ml",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Capacity Stories
        self.next_band(6)
        self.write_rows(6, "Capacity Stories", [
            "Millilitres first",
            "Add, take away",
            "Times, share",
            "Answer with a unit",
        ], scale=0.9, box=0)

        last = Tex("1 000 ml in a litre: change to millilitres, calculate, change back, and write the unit.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
