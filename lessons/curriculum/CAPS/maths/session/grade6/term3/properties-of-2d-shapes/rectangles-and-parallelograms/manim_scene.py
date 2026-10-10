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

# Band-layout whiteboard scene for rectangles-and-parallelograms (Part 1 Expert
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


class RectanglesAndParallelogramsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Properties of Rectangles
        self.write_rows(0, "Properties of Rectangles", [
            "Rectangle: 4 right angles",
            "Opposite sides equal and parallel",
            "80 cm by 50 cm frame",
            "Square: special rectangle",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Properties of Parallelograms
        self.next_band(1)
        self.write_rows(1, "Properties of Parallelograms", [
            "Parallelogram: 2 pairs of parallel sides",
            "Opposite sides equal",
            "Opposite angles equal",
            "Push a rectangle: parallelogram",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Comparing Quadrilaterals
        self.next_band(2)
        self.write_rows(2, "Comparing Quadrilaterals", [
            "Every rectangle is a parallelogram",
            "Rhombus: 4 equal sides",
            "Trapezium: 1 pair of parallel sides",
            "Kite: equal sides next to each other",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A parallelogram has 4 right angles''",
            "``A rectangle is not a parallelogram''",
            "``A square is not a rectangle''",
            "``All 4 angles of a parallelogram are equal''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Square Corners
        self.next_band(4)
        self.write_rows(4, "Square Corners", [
            "Square corners",
            "4 right angles",
            "Opposite sides equal",
            "Opposite sides parallel",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Push It Over
        self.next_band(5)
        self.write_rows(5, "Push It Over", [
            "Push it over",
            "Same sides",
            "New angles",
            "Still a parallelogram",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): One Family
        self.next_band(6)
        self.write_rows(6, "One Family", [
            "One family",
            "Rectangle is a parallelogram",
            "Square is a rectangle",
            "Square is a rhombus",
        ], scale=0.9, box=1)

        last = Tex("A parallelogram has two pairs of parallel sides; a rectangle is a parallelogram with four right angles.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
