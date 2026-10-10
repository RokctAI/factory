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

# Band-layout whiteboard scene for volume-of-rectangular-prisms (Part 1 Expert
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


class VolumeOfRectangularPrismsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Packing and Filling
        self.write_rows(0, "Packing and Filling", [
            "Volume: space taken up",
            "Cubic centimetres",
            "1 000 cubic centimetres = 1 litre",
            "Pack it or fill it",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Layers and the Rule
        self.next_band(1)
        self.write_rows(1, "Layers and the Rule", [
            "One layer: 5 times 4 = 20",
            "Three layers: 60",
            "Volume = length times width times height",
            "Cube 4 cm: 64 cubic centimetres",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Packing Problems
        self.next_band(2)
        self.write_rows(2, "Packing Problems", [
            "Truck: 6 times 4 = 24 per layer",
            "24 times 3 = 72 crates",
            "60 divided by 20 = 3 cm high",
            "Tank: 200 000 cubic cm = 200 litres",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``5 + 4 + 3 = 12''",
            "``Volume = 5 times 4 = 20''",
            "``Count only the cubes you see''",
            "``Volume: 60 square centimetres''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Fill It Up
        self.next_band(4)
        self.write_rows(4, "Fill It Up", [
            "Fill it up",
            "Count cubes",
            "Cubic units",
            "1 litre = 1 000 cubic cm",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Layer by Layer
        self.next_band(5)
        self.write_rows(5, "Layer by Layer", [
            "Layer by layer",
            "20 in a layer",
            "3 layers",
            "60 cubes",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Pack the Truck
        self.next_band(6)
        self.write_rows(6, "Pack the Truck", [
            "Pack the truck",
            "24 crates a layer",
            "3 layers",
            "72 crates",
        ], scale=0.9, box=3)

        last = Tex("Volume of a rectangular prism: length times width gives one layer, and the height gives the number of layers.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
