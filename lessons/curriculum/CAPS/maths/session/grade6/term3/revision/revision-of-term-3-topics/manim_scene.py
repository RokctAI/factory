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

# Band-layout whiteboard scene for revision-of-term-3-topics (Part 1 Expert
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


class RevisionOfTerm3TopicsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Length, Perimeter, Area and Volume
        self.write_rows(0, "Length, Perimeter, Area and Volume", [
            "1,25 km = 1 250 m",
            "Sandpit: perimeter 20 m",
            "Sandpit: area 24 square metres",
            "Tower: 3 times 2 times 2 = 12 cubes",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): 2D Shapes, Angles and Symmetry
        self.next_band(1)
        self.write_rows(1, "2D Shapes, Angles and Symmetry", [
            "Stop sign: regular octagon, 8 lines",
            "Rectangle: 2 lines of symmetry",
            "Slide: acute; corners: right",
            "Fountain: radius 3 m, diameter 6 m",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Transformations and 3D Objects
        self.next_band(2)
        self.write_rows(2, "Transformations and 3D Objects", [
            "Hexagons tessellate",
            "Map: every length times 5",
            "Pyramid: 5 faces, 5 vertices, 8 edges",
            "8 poles, 5 joints",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1,25 km = 125 m''",
            "``Sandpit area: 20 square metres''",
            "``Rectangle diagonals are mirror lines''",
            "``A square-based pyramid has 4 faces''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Measure It Right
        self.next_band(4)
        self.write_rows(4, "Measure It Right", [
            "Measure it right",
            "1 250 m",
            "20 m around",
            "24 square metres inside",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Sides, Angles, Mirrors
        self.next_band(5)
        self.write_rows(5, "Sides, Angles, Mirrors", [
            "Sides, angles, mirrors",
            "Octagon: 8 lines",
            "Slide: acute",
            "Diameter: 6 m",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Moves and Solids
        self.next_band(6)
        self.write_rows(6, "Moves and Solids", [
            "Moves and solids",
            "Hexagons tessellate",
            "Map: times 5",
            "Pyramid: 5, 5, 8",
        ], scale=0.9, box=3)

        last = Tex("Use the right unit for every measurement, and describe shapes by their sides, angles, symmetry, faces, vertices and edges.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
