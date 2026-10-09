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

# Band-layout whiteboard scene for measuring-and-recording-capacity (Part 1 Expert
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


class MeasuringAndRecordingCapacitySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Millilitres and Litres
        self.write_rows(0, "Millilitres and Litres", [
            "1 l = 1 000 ml",
            "Teaspoon 5 ml, tablespoon 15 ml",
            "Measuring cup 250 ml",
            "ml for small, l for large",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Estimating and Measuring with Spoons, Cups and Jugs
        self.next_band(1)
        self.write_rows(1, "Estimating and Measuring with Spoons, Cups and Jugs", [
            "Estimate, then measure",
            "3 teaspoons = 1 tablespoon",
            "4 cups of 250 ml = 1 l",
            "Halfway from 600 to 800: 700 ml",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Recording, Comparing and Ordering Capacity
        self.next_band(2)
        self.write_rows(2, "Recording, Comparing and Ordering Capacity", [
            "Record: number and unit",
            "1 l = 1 000 ml, more than 750 ml",
            "200 ml, 330 ml, 500 ml, 1 l, 2 l",
            "1 l 500 ml = 1 500 ml",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A teaspoon holds 5 l''",
            "``Read the jug from above''",
            "``750 ml is more than 1 l''",
            "``Each small mark is 1 ml''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Small and Big Amounts
        self.next_band(4)
        self.write_rows(4, "Small and Big Amounts", [
            "ml: small amounts",
            "l: big amounts",
            "1 l = 1 000 ml",
            "Teaspoon 5 ml, cup 250 ml",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Fill, Pour and Count
        self.next_band(5)
        self.write_rows(5, "Fill, Pour and Count", [
            "Guess first",
            "3 teaspoons: 1 tablespoon",
            "4 cups: 1 litre",
            "Read at eye level",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Which Holds More
        self.next_band(6)
        self.write_rows(6, "Which Holds More", [
            "Write the unit",
            "Same unit first",
            "1 l beats 750 ml",
            "Smallest to biggest",
        ], scale=0.9, box=2)

        last = Tex("1 000 ml in a litre: estimate, measure at eye level, write the unit, and compare in the same unit.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
