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
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (330/240/240/230/270/240/230 of
# 1780 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TransformTrianglesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): One Vertex at a Time
        t0 = Tex(r"One Vertex at a Time").scale(1.3).to_edge(UP)
        self.play(Write(t0))
        self.wait(1.5)
        m1 = MathTex(r"A(1;\ 1),\ B(4;\ 1),\ C(1;\ 3) \quad (x;\ y) \to (x;\ -y)").scale(1.1).shift(UP * 1.2)
        self.play(Write(m1))
        self.wait(2)
        m2 = MathTex(r"A'(1;\ -1),\ B'(4;\ -1),\ C'(1;\ -3)").scale(1.1).shift(DOWN * 0.17)
        self.play(Write(m2))
        self.wait(2)
        m3 = MathTex(r"(x;\ y) \to (y;\ x): \quad A'(1;\ 1),\ B'(1;\ 4),\ C'(3;\ 1)").scale(1.1).shift(DOWN * 1.53)
        self.play(Write(m3))
        self.wait(2)
        m4 = Tex(r"Same rule for every vertex; primes keep the corners matched").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(m4))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m4, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 1 (subtopic_2): Translating a Triangle
        self.next_band(1)
        t1 = Tex(r"Translating a Triangle").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(t1))
        self.wait(1.5)
        m5 = MathTex(r"(x;\ y) \to (x - 5;\ y + 2)").scale(1.1).shift(band_shift(1) + UP * 1.2)
        self.play(Write(m5))
        self.wait(2)
        m6 = MathTex(r"A'(-4;\ 3),\ B'(-1;\ 3),\ C'(-4;\ 5)").scale(1.1).shift(band_shift(1) + DOWN * 0.17)
        self.play(Write(m6))
        self.wait(2)
        m7 = MathTex(r"-4 - 1 = -5, \quad 3 - 1 = 2 \quad \text{for every vertex}").scale(1.1).shift(band_shift(1) + DOWN * 1.53)
        self.play(Write(m7))
        self.wait(2)
        m8 = Tex(r"Same shift for all three corners; horizontal sides stay horizontal").scale(1.05).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(m8))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m8, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 2 (subtopic_3): Rotating About the Origin
        self.next_band(2)
        t2 = Tex(r"Rotating About the Origin").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(t2))
        self.wait(1.5)
        m9 = MathTex(r"90^\circ \text{ anticlockwise}: (x;\ y) \to (-y;\ x)").scale(1.1).shift(band_shift(2) + UP * 1.2)
        self.play(Write(m9))
        self.wait(2)
        m10 = MathTex(r"A'(-1;\ 1),\ B'(-1;\ 4),\ C'(-3;\ 1)").scale(1.1).shift(band_shift(2) + DOWN * 0.17)
        self.play(Write(m10))
        self.wait(2)
        m11 = MathTex(r"4^2 + 1^2 = 17 = (-1)^2 + 4^2").scale(1.1).shift(band_shift(2) + DOWN * 1.53)
        self.play(Write(m11))
        self.wait(2)
        m12 = Tex(r"Clockwise: (y; -x). Half-turn: (-x; -y). Distances from the origin unchanged.").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(m12))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m12, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 3 (subtopic_4): Congruence and Orientation
        self.next_band(3)
        t3 = Tex(r"Congruence and Orientation").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(t3))
        self.wait(1.5)
        m13 = MathTex(r"AB = 3, \quad AC = 2, \quad BC = \sqrt{3^2 + 2^2} = \sqrt{13}").scale(1.1).shift(band_shift(3) + UP * 1.2)
        self.play(Write(m13))
        self.wait(2)
        m14 = MathTex(r"\text{Area} = \tfrac{1}{2} \times 3 \times 2 = 3").scale(1.1).shift(band_shift(3) + DOWN * 0.17)
        self.play(Write(m14))
        self.wait(2)
        m15 = Tex(r"Reflection reverses the order of the corners; rotation and translation keep it").scale(1.05).shift(band_shift(3) + DOWN * 1.53)
        self.play(Write(m15))
        self.wait(2)
        m16 = Tex(r"Same sides, same angles, same area: a congruent image").scale(1.05).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(m16))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m16, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): The Mural Motif
        self.next_band(4)
        t4 = Tex(r"The Mural Motif").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(t4))
        self.wait(1.5)
        m17 = MathTex(r"P(2;\ 1),\ Q(6;\ 1),\ R(2;\ 4): \quad 4^2 + 3^2 = 25 = 5^2").scale(1.1).shift(band_shift(4) + UP * 1.2)
        self.play(Write(m17))
        self.wait(2)
        m18 = MathTex(r"\text{y-axis}: P'(-2;\ 1),\ Q'(-6;\ 1),\ R'(-2;\ 4)").scale(1.1).shift(band_shift(4) + DOWN * 0.17)
        self.play(Write(m18))
        self.wait(2)
        m19 = MathTex(r"180^\circ: (-2;\ -1),\ (-6;\ -1),\ (-2;\ -4)").scale(1.1).shift(band_shift(4) + DOWN * 1.53)
        self.play(Write(m19))
        self.wait(2)
        m20 = Tex(r"Two perpendicular reflections make a half-turn").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(m20))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m20, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 5 (subtopic_6): The Stencil
        self.next_band(5)
        t5 = Tex(r"The Stencil").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(t5))
        self.wait(1.5)
        m21 = MathTex(r"D(1;\ 2),\ E(5;\ 2),\ F(1;\ 5)").scale(1.1).shift(band_shift(5) + UP * 1.2)
        self.play(Write(m21))
        self.wait(2)
        m22 = MathTex(r"\text{slide}: (x;\ y) \to (x - 6;\ y): \ D'(-5;\ 2),\ E'(-1;\ 2),\ F'(-5;\ 5)").scale(1.1).shift(band_shift(5) + DOWN * 0.17)
        self.play(Write(m22))
        self.wait(2)
        m23 = MathTex(r"\text{flip}: (x;\ y) \to (-x;\ y): \ (-1;\ 2),\ (-5;\ 2),\ (-1;\ 5)").scale(1.1).shift(band_shift(5) + DOWN * 1.53)
        self.play(Write(m23))
        self.wait(2)
        m24 = Tex(r"Reversed orientation gives the reflection away").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(m24))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m24, color=GREEN)))
        self.wait(1.5)
        self.wait(3)

        # --- Band 6 (subtopic_7): Examination Technique
        self.next_band(6)
        t6 = Tex(r"Examination Technique").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(t6))
        self.wait(1.5)
        m25 = Tex(r"Rule, table, every vertex, primes, plot, check").scale(1.05).shift(band_shift(6) + UP * 1.2)
        self.play(Write(m25))
        self.wait(2)
        m26 = MathTex(r"A(1;\ 1) \to A'(1;\ -1) \to A''(4;\ -1)").scale(1.1).shift(band_shift(6) + DOWN * 0.17)
        self.play(Write(m26))
        self.wait(2)
        m27 = Tex(r"Sides, angles and area unchanged; orientation reversed only by a reflection").scale(1.05).shift(band_shift(6) + DOWN * 1.53)
        self.play(Write(m27))
        self.wait(2)
        m28 = Tex(r"Same pattern on all three vertices before naming the transformation").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(m28))
        self.wait(2)
        self.play(Create(SurroundingRectangle(m28, color=GREEN)))
        self.wait(1.5)
        self.wait(3)
