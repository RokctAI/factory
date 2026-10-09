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

# Band-layout whiteboard scene for revision-of-shape-data-and-measurement (Part 1 Expert
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


class RevisionOfShapeDataAndMeasurementSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Shapes, Objects, Symmetry and Tessellations
        self.write_rows(0, "Shapes, Objects, Symmetry and Tessellations", [
            "Hexagon 6 sides, octagon 8",
            "Cube: 6 square faces",
            "Rectangle 2 lines, square 4",
            "No gaps, no overlaps",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Data Handling and Probability
        self.next_band(1)
        self.write_rows(1, "Data Handling and Probability", [
            "12 + 8 + 5 + 15 = 40",
            "Scale from 0, equal steps",
            "Soccer 15, picnic 5: 10 more",
            "Coin 2 outcomes, dice 6",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Measurement: Time, Units, Perimeter, Area and Volume
        self.next_band(2)
        self.write_rows(2, "Measurement: Time, Units, Perimeter, Area and Volume", [
            "08:15 to 10:40: 2 h 25 min",
            "1 km = 1 000 m, 1 kg = 1 000 g, 1 l = 1 000 ml",
            "Perimeter: 8 + 5 + 8 + 5 = 26 m",
            "Area 12 squares, volume 12 cubes",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Rectangle: 4 lines of symmetry''",
            "``Bar graph scale starts at 5''",
            "``8 m by 5 m: perimeter 13 m''",
            "``Area is the distance around''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Shapes and Objects
        self.next_band(4)
        self.write_rows(4, "Shapes and Objects", [
            "Hexagon: 6 sides",
            "Cube: 6 square faces",
            "Square: 4 lines of symmetry",
            "No gaps, no overlaps",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Count, Graph and Guess
        self.next_band(5)
        self.write_rows(5, "Count, Graph and Guess", [
            "Tally in fives",
            "Total checks the count",
            "Bar graph from 0",
            "Coin: 2 outcomes, dice: 6",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Measure It
        self.next_band(6)
        self.write_rows(6, "Measure It", [
            "Hours, then minutes",
            "1 000 small make 1 big",
            "Perimeter: around the edge",
            "Area: squares, volume: cubes",
        ], scale=0.9, box=2)

        last = Tex("Name it by its properties, check data by its total, and give every measurement its unit.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
