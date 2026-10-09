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

# Band-layout whiteboard scene for faces-surfaces-and-making-3d-models (Part 1 Expert
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


class FacesSurfacesAndMaking3dModelsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Describing Objects by Their Faces
        self.write_rows(0, "Describing Objects by Their Faces", [
            "List the faces by shape",
            "Shoe box: 6 rectangles in pairs",
            "Tin: 2 flat, 1 curved",
            "Ball: 0 flat, 1 curved",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Sorting Objects by Surfaces
        self.next_band(1)
        self.write_rows(1, "Sorting Objects by Surfaces", [
            "Flat only: prisms and pyramids",
            "Curved only: spheres",
            "Both: cylinders",
            "Prisms stack, spheres roll",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Making Models from Cut-Out Polygons
        self.next_band(2)
        self.write_rows(2, "Making Models from Cut-Out Polygons", [
            "Cube: 6 squares taped at the edges",
            "Square pyramid: 1 square plus 4 triangles",
            "A net is the flat pattern",
            "A tube is a rolled rectangle",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A tin has 3 faces''",
            "``6 faces means it is a cube''",
            "``Any six squares fold into a cube''",
            "``3 triangles make a pyramid''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): List the Faces
        self.next_band(4)
        self.write_rows(4, "List the Faces", [
            "Box: 6 rectangles",
            "Pyramid: 1 square, 4 triangles",
            "Tin: 2 flat, 1 curved",
            "Ball: 0 flat, 1 curved",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Sort by Surface
        self.next_band(5)
        self.write_rows(5, "Sort by Surface", [
            "Flat only: box, pyramid",
            "Curved only: ball",
            "Both: tin",
            "Say why",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Build It
        self.next_band(6)
        self.write_rows(6, "Build It", [
            "6 squares fold into a cube",
            "1 square, 4 triangles: pyramid",
            "Flat pattern: a net",
            "Building proves the faces",
        ], scale=0.9, box=3)

        last = Tex("List the faces, count flat and curved, sort with a reason, and build the net to prove it.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
