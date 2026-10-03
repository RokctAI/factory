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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Curved solids are drawn from circles,
# ellipses (a Circle subclass) and line segments. Bands cover all seven
# subtopics of the duo (Part 1 — Expert: subtopics 1-4; Part 2 —
# Simplifier: subtopics 5-7), with dwell time proportional to subtopics.json
# (220/230/230/230/190/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def cylinder(base_centre, r=1.0, h=2.2, tilt=0.35, color=WHITE):
    """Upright cylinder seen slightly from above: two ellipses and two sides."""
    top = base_centre + UP * h
    g = VGroup(
        Ellipse(width=2 * r, height=2 * r * tilt, color=color).move_to(top),
        Ellipse(width=2 * r, height=2 * r * tilt, color=color).move_to(base_centre),
        Line(base_centre + LEFT * r, top + LEFT * r, color=color),
        Line(base_centre + RIGHT * r, top + RIGHT * r, color=color),
    )
    return g


def sphere(centre, r=1.2, color=WHITE):
    """Outline circle plus an equator ellipse and a dot at the centre."""
    return VGroup(
        Circle(radius=r, color=color).move_to(centre),
        Ellipse(width=2 * r, height=0.6 * r, color=BLUE).move_to(centre),
        Dot(centre, color=YELLOW),
    )


class SpheresAndCylindersSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the cylinder
        title = Tex("The cylinder").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        cyl = cylinder(np.array([-4.8, -2.0, 0]), r=1.1, h=2.8)
        self.play(Create(cyl), run_time=2)
        r_line = Line(np.array([-4.8, 0.8, 0]), np.array([-3.7, 0.8, 0]), color=YELLOW)
        r_lab = MathTex("r = 3.5").scale(0.6).next_to(r_line, UP, buff=0.1)
        h_line = Line(np.array([-3.3, -2.0, 0]), np.array([-3.3, 0.8, 0]), color=GREEN)
        h_lab = MathTex("h = 10").scale(0.6).next_to(h_line, RIGHT, buff=0.1)
        self.play(Create(r_line), Write(r_lab), Create(h_line), Write(h_lab))
        rows = [
            "2 flat circular faces, 1 curved surface",
            "2 curved edges, 0 vertices",
            "Across, parallel to the base: a circle like the base",
            "Down through the axis: a rectangle 7 by 10",
            "At a slant: an ellipse",
        ]
        for i, r in enumerate(rows):
            m = Tex(r).scale(0.7).shift(RIGHT * 2.2 + UP * (1.6 - 0.75 * i))
            self.play(Write(m))
            self.wait(2.0)
        circ = MathTex(r"2\pi \times 3.5 \approx 21.99 \text{ cm}").scale(0.8).shift(RIGHT * 2.2 + DOWN * 2.4)
        self.play(Write(circ))
        self.play(Create(SurroundingRectangle(circ, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): the sphere
        self.next_band(1)
        b1_title = Tex("The sphere").scale(1.2).shift(band_shift(1) + UP * 3.0)
        self.play(Write(b1_title))
        self.wait(1.5)
        sp = sphere(band_shift(1) + LEFT * 4.6 + DOWN * 0.2, r=1.6)
        self.play(Create(sp), run_time=2)
        slice_line = Line(band_shift(1) + LEFT * 5.88 + UP * 0.76, band_shift(1) + LEFT * 3.32 + UP * 0.76, color=GREEN)
        self.play(Create(slice_line))
        s1 = Tex("Every point the same distance r from the centre").scale(0.7).shift(band_shift(1) + RIGHT * 2.2 + UP * 1.7)
        s2 = Tex("0 flat faces, 1 curved surface, 0 edges, 0 vertices").scale(0.7).shift(band_shift(1) + RIGHT * 2.2 + UP * 0.9)
        s3 = Tex("Every cross-section is a circle; through the centre: a great circle").scale(0.62).shift(band_shift(1) + RIGHT * 2.2 + UP * 0.1)
        s4 = MathTex(r"r = 10,\ 6 \text{ from centre: } \sqrt{10^2 - 6^2} = \sqrt{64} = 8").scale(0.75).shift(band_shift(1) + RIGHT * 2.2 + DOWN * 0.7)
        s5 = MathTex(r"\text{Equator: } 2\pi \times 6370 \approx 40\,024 \text{ km}").scale(0.75).shift(band_shift(1) + RIGHT * 2.2 + DOWN * 1.5)
        s6 = Tex("Hemisphere: 1 flat face, 1 curved surface, 1 edge").scale(0.7).shift(band_shift(1) + RIGHT * 2.2 + DOWN * 2.3)
        for m in (s1, s2, s3, s4, s5, s6):
            self.play(Write(m))
            self.wait(1.9)
        self.play(Create(SurroundingRectangle(s4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): comparison table
        self.next_band(2)
        b2_title = Tex("Flat faces, curved surfaces, edges, vertices").scale(1.0).shift(band_shift(2) + UP * 3.0)
        self.play(Write(b2_title))
        self.wait(1.5)
        table_rows = [
            "Cube: 6, 0, 12, 8",
            "Cylinder: 2, 1, 2, 0",
            "Cone: 1, 1, 1, 1 (the apex)",
            "Sphere: 0, 1, 0, 0",
            "Hemisphere: 1, 1, 1, 0",
        ]
        for i, r in enumerate(table_rows):
            m = Tex(r).scale(0.8).shift(band_shift(2) + LEFT * 3.0 + UP * (1.8 - 0.75 * i))
            self.play(Write(m))
            self.wait(1.8)
        c1 = Tex("Cylinder: a prism with a circular end").scale(0.7).shift(band_shift(2) + RIGHT * 3.4 + UP * 1.5)
        c2 = Tex("Cone: a pyramid with a circular base").scale(0.7).shift(band_shift(2) + RIGHT * 3.4 + UP * 0.7)
        c3 = MathTex(r"\text{Cylinder: } 0 - 2 + 3 = 1 \ne 2").scale(0.75).shift(band_shift(2) + RIGHT * 3.4 + DOWN * 0.1)
        c4 = Tex("Euler is for polyhedra only").scale(0.75).shift(band_shift(2) + RIGHT * 3.4 + DOWN * 0.9)
        for m in (c1, c2, c3, c4):
            self.play(Write(m))
            self.wait(2.0)
        self.play(Create(SurroundingRectangle(c4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): real objects, hollow pipe
        self.next_band(3)
        b3_title = Tex("Describing real objects").scale(1.15).shift(band_shift(3) + UP * 3.0)
        self.play(Write(b3_title))
        self.wait(1.5)
        outer = Circle(radius=1.6, color=WHITE).move_to(band_shift(3) + LEFT * 4.5)
        inner = Circle(radius=1.45, color=BLUE).move_to(band_shift(3) + LEFT * 4.5)
        self.play(Create(outer), Create(inner))
        ring_lab = Tex("Pipe cross-section: a ring").scale(0.6).move_to(band_shift(3) + LEFT * 4.5 + DOWN * 2.0)
        self.play(Write(ring_lab))
        p1 = Tex("Tank: cylinder, about 1.3 m across, 1.6 m high").scale(0.7).shift(band_shift(3) + RIGHT * 2.0 + UP * 1.6)
        p2 = Tex("Netball: sphere, diameter about 22 cm").scale(0.7).shift(band_shift(3) + RIGHT * 2.0 + UP * 0.8)
        p3 = MathTex(r"\text{Inner diameter} = 110 - 2 \times 5 = 100 \text{ mm}").scale(0.75).shift(band_shift(3) + RIGHT * 2.0 + UP * 0.0)
        p4 = Tex("Radii: outer 55, inner 50").scale(0.7).shift(band_shift(3) + RIGHT * 2.0 + DOWN * 0.8)
        for m in (p1, p2, p3, p4):
            self.play(Write(m))
            self.wait(2.2)
        self.play(Create(SurroundingRectangle(p3, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        e1 = Tex("A sphere is a circle").scale(0.8).shift(band_shift(4) + UP * 1.5)
        e2 = Tex("Cylinder: 3 faces and no edges").scale(0.8).shift(band_shift(4) + UP * 0.6)
        e3 = Tex("Tin 7 cm across, so r = 7").scale(0.8).shift(band_shift(4) + DOWN * 0.3)
        e4 = Tex("Every cross-section of a cylinder is a circle").scale(0.8).shift(band_shift(4) + DOWN * 1.2)
        e5 = Tex("Sphere: 1 face, 1 edge; cone: no vertex").scale(0.8).shift(band_shift(4) + DOWN * 2.1)
        for m in (e1, e2, e3, e4, e5):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.6)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the tin can
        self.next_band(5)
        b5_title = Tex("The tin can").scale(1.2).shift(band_shift(5) + UP * 2.8)
        self.play(Write(b5_title))
        self.wait(2)
        tin = cylinder(band_shift(5) + LEFT * 4.8 + DOWN * 1.8, r=0.9, h=2.4)
        self.play(Create(tin), run_time=2)
        t1 = Tex("Flat circle top and bottom, curved side").scale(0.8).shift(band_shift(5) + RIGHT * 1.8 + UP * 1.3)
        t2 = Tex("2 rims for edges, no corners").scale(0.8).shift(band_shift(5) + RIGHT * 1.8 + UP * 0.4)
        t3 = Tex("Say all four: 2, 1, 2, 0").scale(0.8).shift(band_shift(5) + RIGHT * 1.8 + DOWN * 0.5)
        t4 = Tex("Fat or thin, tall or short: still a cylinder").scale(0.8).shift(band_shift(5) + RIGHT * 1.8 + DOWN * 1.4)
        for m in (t1, t2, t3, t4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(t3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): the ball
        self.next_band(6)
        b6_title = Tex("The ball").scale(1.2).shift(band_shift(6) + UP * 2.8)
        self.play(Write(b6_title))
        self.wait(2)
        ball = sphere(band_shift(6) + LEFT * 4.6, r=1.4)
        self.play(Create(ball), run_time=2)
        u1 = Tex("One curved surface and nothing else").scale(0.8).shift(band_shift(6) + RIGHT * 1.8 + UP * 1.3)
        u2 = Tex("A circle is flat; a sphere you can hold").scale(0.8).shift(band_shift(6) + RIGHT * 1.8 + UP * 0.4)
        u3 = Tex("Half a ball: hemisphere, 1 face, 1 surface, 1 rim").scale(0.75).shift(band_shift(6) + RIGHT * 1.8 + DOWN * 0.5)
        u4 = Tex("Equator: about 40 000 km round").scale(0.8).shift(band_shift(6) + RIGHT * 1.8 + DOWN * 1.4)
        for m in (u1, u2, u3, u4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(u1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): slice it and see
        self.next_band(7)
        b7_title = Tex("Slice it and see").scale(1.2).shift(band_shift(7) + UP * 2.8)
        self.play(Write(b7_title))
        self.wait(2)
        sec1 = Circle(radius=0.7, color=BLUE).move_to(band_shift(7) + LEFT * 5.0 + UP * 0.8)
        sec2 = Rectangle(width=1.4, height=2.0, color=GREEN).move_to(band_shift(7) + LEFT * 3.0 + UP * 0.8)
        sec3 = Ellipse(width=1.8, height=0.9, color=ORANGE).move_to(band_shift(7) + LEFT * 0.8 + UP * 0.8)
        self.play(Create(sec1), Create(sec2), Create(sec3), run_time=2)
        lab = Tex("Across: circle \\quad Down the middle: rectangle \\quad Slant: oval").scale(0.6).shift(band_shift(7) + LEFT * 2.9 + DOWN * 0.7)
        self.play(Write(lab))
        v1 = Tex("Ball: always a circle").scale(0.8).shift(band_shift(7) + RIGHT * 4.0 + UP * 1.2)
        v2 = Tex("Pipe: a ring").scale(0.8).shift(band_shift(7) + RIGHT * 4.0 + UP * 0.4)
        for m in (v1, v2):
            self.play(Write(m))
            self.wait(2.2)
        v3 = Tex("Name it, list all four parts, slice to check.").scale(0.85).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(v3))
        self.play(Create(SurroundingRectangle(v3, color=YELLOW)))
        self.wait(4)
