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
        # --- Band 0 (subtopic_1): Units and Benchmarks
        self.write_rows(0, "Units and Benchmarks", [
            "ml, l, kl",
            "1 000 ml = 1 l; 1 000 l = 1 kl",
            "Teaspoon 5 ml, tablespoon 15 ml",
            "Cup 250 ml: 4 cups = 1 l",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Measuring with Spoons, Cups and Jugs
        self.next_band(1)
        self.write_rows(1, "Measuring with Spoons, Cups and Jugs", [
            "200 ml split into 4 spaces: 50 ml",
            "Second mark after 400: 500 ml",
            "Read at eye level",
            "3 tablespoons = 45 ml",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Recording, Comparing and Ordering
        self.next_band(2)
        self.write_rows(2, "Recording, Comparing and Ordering", [
            "1,5 l = 1 500 ml",
            "1 500 ml is more than 1 250 ml",
            "750 ml; 1 800 ml; 2 l",
            "4 l + 250 ml = 4 250 ml",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Reading the jug from above''",
            "``1 250 ml is more than 1,5 l''",
            "``3 tablespoons = 3 ml''",
            "``A half-full 2 l bottle holds 2 l''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Millilitres, Litres, Kilolitres
        self.next_band(4)
        self.write_rows(4, "Millilitres, Litres, Kilolitres", [
            "Three units",
            "Small: ml",
            "Bottles: l",
            "Tanks: kl",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Eye Level
        self.next_band(5)
        self.write_rows(5, "Eye Level", [
            "Eye level",
            "Value of each mark",
            "Bend down",
            "Read the flat middle",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Same Unit, Then Compare
        self.next_band(6)
        self.write_rows(6, "Same Unit, Then Compare", [
            "Same unit, then compare",
            "1,5 l = 1 500 ml",
            "More than 1 250 ml",
            "Bottle holds more",
        ], scale=0.9, box=1)

        last = Tex("1 000 ml make 1 litre: read jugs at eye level and compare amounts in the same unit.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
