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

# Band-layout whiteboard scene for term-1-revision-design-skills-and-line-conventions (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/170/180/110/100/90 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Term1RevisionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Mechanisms of the Term
        self.write_rows(0, "Mechanisms of the Term", [
            "MA = load over effort; distance is the price",
            "Wedge: moving ramp; wheel and axle: spinning lever",
            "Gears: opposite ways; more teeth, slower, stronger",
            "Cam bobs; crank is a second-class lever",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Structures of the Term
        self.next_band(1)
        self.write_rows(1, "Structures of the Term", [
            "Pylon: lattice, X-braces, wide base",
            "Tension, compression, shear, torsion",
            "Truss: rafters C, tie beam and post T",
            "Beam, suspension, stayed, arch, cantilever; snap, bow, tip",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Design Skills and Drawing Conventions
        self.next_band(2)
        self.write_rows(2, "Design Skills and Drawing Conventions", [
            "IDMEC; brief, specs, constraints, sketches",
            "Dark, feint, dashed, chain",
            "Scale paper:real; mm outside, once, overall",
            "Working drawing, isometric, impression",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``More teeth means faster''",
            "``A vertical post is in compression''",
            "``Dimension the paper size''",
            "``Stiff means stable''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Gears, Cams and Cranks in a Minute
        self.next_band(4)
        self.write_rows(4, "Gears, Cams and Cranks in a Minute", [
            "Load over push",
            "Opposite ways; more teeth, slower",
            "10 into 30: third speed, triple force",
            "Cam bobs, crank turns",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Triangles, Trusses and Toppling
        self.next_band(5)
        self.write_rows(5, "Triangles, Trusses and Toppling", [
            "Pull, push, slice, twist",
            "Rafters pushed, tie beam pulled",
            "Triangles stiff, wide base stable",
            "Snapped, bowed, tipped",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): The Drawings You Must Be Able to Do
        self.next_band(6)
        self.write_rows(6, "The Drawings You Must Be Able to Do", [
            "Dark, feint, dashed, dash-dot",
            "1:2 is half; write real sizes",
            "mm, outside, arrows, once",
            "Flat, isometric, coloured",
        ], scale=0.9, box=1)

        last = Tex("Mechanisms trade distance for force, structures carry four forces and fail three ways, and design speaks in lines, scale and millimetres.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
