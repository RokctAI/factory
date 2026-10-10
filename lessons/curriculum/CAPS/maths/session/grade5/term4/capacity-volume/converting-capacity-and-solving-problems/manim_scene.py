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
        # --- Band 0 (subtopic_1): Litres to Millilitres and Back
        self.write_rows(0, "Litres to Millilitres and Back", [
            "1 l is 1 000 ml",
            "3 l is 3 000 ml",
            "2 l 250 ml is 2 250 ml",
            "4 500 ml is 4 l 500 ml",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Fractions of a Litre
        self.next_band(1)
        self.write_rows(1, "Fractions of a Litre", [
            "Half a litre: 500 ml",
            "Quarter: 250 ml",
            "Three quarters: 750 ml",
            "1 and 1/2 l is 1 500 ml",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Solving Capacity Problems
        self.next_band(2)
        self.write_rows(2, "Solving Capacity Problems", [
            "Bath 80 l, shower 20 l",
            "Saving: 60 l",
            "5 000 divided by 250 is 20",
            "Drip: 36 l a day",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3 l is 300 ml''",
            "``A quarter litre is 25 ml''",
            "``4 500 ml is 45 l''",
            "``Adding without converting''",
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
            "3 l: 3 000 ml",
            "4 500 ml: 4 l 500 ml",
            "Check the size",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Parts of a Litre
        self.next_band(5)
        self.write_rows(5, "Parts of a Litre", [
            "Parts of a litre",
            "Half: 500 ml",
            "Quarter: 250 ml",
            "Three quarters: 750 ml",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Save the Water
        self.next_band(6)
        self.write_rows(6, "Save the Water", [
            "Save the water",
            "Bath minus shower: 60 l",
            "20 glasses",
            "36 l a day from a drip",
        ], scale=0.9, box=1)

        last = Tex("Multiply or divide by 1 000, find fractions of 1 000 ml, and change every amount to the same unit before you solve.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
