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

# Band-layout whiteboard scene for the session duo "The Cosine Rule and 2D
# Problems" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7). One band per teaching beat, add-only lifecycle, camera
# moves down between bands. Only exporter-supported mobjects; write-only
# reveals. Band dwell times follow subtopics.json
# (230/225/215/240/190/190/190 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CosineRule2DProblemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the rule and its anatomy ---
        title = Tex("The Cosine Rule and 2D Problems").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"a^2 = b^2 + c^2 - 2bc\cos A").scale(1.2).shift(UP * 0.8)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2.5)
        b0_l2 = Tex("The squared side and the cosine angle FACE each other").scale(0.95).shift(DOWN * 0.3)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Two sides squared and added, then the correction term").scale(0.95).shift(DOWN * 1.2)
        self.play(Write(b0_l3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the proof — drop a perpendicular ---
        self.next_band(1)
        b1_title = Tex("Proof: drop a perpendicular from C").scale(1.1).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        tc = band_shift(1) + DOWN * 0.6
        A = tc + LEFT * 3.2 + DOWN * 1.2
        B = tc + RIGHT * 3.2 + DOWN * 1.2
        C = tc + LEFT * 0.8 + UP * 1.6
        D = tc + LEFT * 0.8 + DOWN * 1.2
        sAB = Line(A, B); sAC = Line(A, C); sBC = Line(B, C); sCD = Line(C, D)
        lA = Tex("A").scale(0.9).move_to(A + LEFT * 0.35)
        lB = Tex("B").scale(0.9).move_to(B + RIGHT * 0.35)
        lC = Tex("C").scale(0.9).move_to(C + UP * 0.35)
        lD = Tex("D").scale(0.9).move_to(D + DOWN * 0.35)
        self.play(Create(sAB), Create(sAC), Create(sBC))
        self.play(Write(lA), Write(lB), Write(lC))
        self.wait(2)
        self.play(Create(sCD), Write(lD))
        self.wait(2)
        b1_l1 = MathTex(r"CD = b\sin A \qquad AD = b\cos A").scale(0.95).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"DB = c - b\cos A").scale(0.95).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(b1_l2))
        self.wait(3)

        # --- Band 2 (subtopic_1): Pythagoras in CDB, identity merges ---
        self.next_band(2)
        b2_title = Tex("Pythagoras in triangle CDB").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"a^2 = b^2\sin^2 A + (c - b\cos A)^2").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"= b^2(\sin^2 A + \cos^2 A) + c^2 - 2bc\cos A").scale(0.95).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\sin^2 A + \cos^2 A = 1 \;\Rightarrow\; a^2 = b^2 + c^2 - 2bc\cos A").scale(0.9).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = MathTex(r"A = 90^\circ: \cos 90^\circ = 0 \;\Rightarrow\; a^2 = b^2 + c^2").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): finding a side, acute case ---
        self.next_band(3)
        b3_title = Tex(r"Find $a$: $b = 8$, $c = 3$, $A = 60^\circ$").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"a^2 = 64 + 9 - 2(8)(3)\cos 60^\circ").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"= 73 - 48 \times 0{,}5 = 73 - 24 = 49").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"a = \sqrt{49} = 7 \text{ cm}").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Square root as the final move — always").scale(0.95).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_2): the obtuse case and the sign ---
        self.next_band(4)
        b4_title = Tex(r"Obtuse: $p = 7$, $r = 8$, $Q = 120^\circ$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"q^2 = 49 + 64 - 2(7)(8)\cos 120^\circ").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"\cos 120^\circ = -0{,}5: \;\; -112 \times (-0{,}5) = +56").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"q^2 = 113 + 56 = 169 \;\Rightarrow\; q = 13 \text{ cm}").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex(r"Beyond $90^\circ$ the far side grows past $\sqrt{113} \approx 10{,}6$").scale(0.9).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): finding an angle from three sides ---
        self.next_band(5)
        b5_title = Tex("Three sides 4, 7, 9: find the largest angle").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\cos\theta = \frac{b^2 + c^2 - a^2}{2bc}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = MathTex(r"\cos\theta = \frac{16 + 49 - 81}{2(4)(7)} = \frac{-16}{56} = -0{,}2857").scale(0.95).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\theta = 106{,}6^\circ \text{ — obtuse, as the sign warned}").scale(1.0).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("Inverse cosine has no second suspect").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the harbour — how far apart? ---
        self.next_band(6)
        b6_title = Tex(r"Bearings $040^\circ$ and $105^\circ$: angle $= 65^\circ$").scale(1.05).shift(band_shift(6) + UP * 2.6)
        self.play(Write(b6_title))
        self.wait(2)
        hc = band_shift(6) + DOWN * 0.5
        H = hc + DOWN * 1.4
        P = hc + LEFT * 2.2 + UP * 1.6
        Q = hc + RIGHT * 2.6 + UP * 1.0
        sHP = Line(H, P); sHQ = Line(H, Q); sPQ = Line(P, Q)
        lH = Tex("H").scale(0.9).move_to(H + DOWN * 0.35)
        lP = Tex("P").scale(0.9).move_to(P + UP * 0.35)
        lQ = Tex("Q").scale(0.9).move_to(Q + UP * 0.35)
        self.play(Create(sHP), Create(sHQ))
        self.play(Write(lH), Write(lP), Write(lQ))
        self.wait(2)
        self.play(Create(sPQ))
        self.wait(2)
        b6_l1 = MathTex(r"PQ^2 = 25 + 49 - 2(5)(7)\cos 65^\circ").scale(0.95).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"= 74 - 29{,}58 = 44{,}42 \;\Rightarrow\; PQ \approx 6{,}66 \text{ km}").scale(0.95).shift(band_shift(6) + DOWN * 3.4)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the angle at P, and the habits ---
        self.next_band(7)
        b7_title = Tex("The angle at P — choose the safe tool").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\cos P = \frac{25 + 44{,}42 - 49}{2(5)(6{,}66)} = \frac{20{,}42}{66{,}65} = 0{,}3064").scale(0.9).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"P \approx 72{,}2^\circ \quad\Rightarrow\quad Q \approx 42{,}8^\circ").scale(1.0).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Sketch, name the triangle, audit what you hold").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Carry unrounded values; round only what you report").scale(0.95).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): Pythagoras with an attitude adjustment ---
        self.next_band(8)
        b8_title = Tex("Pythagoras with an attitude adjustment").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Square corner: $\sqrt{49 + 64} = \sqrt{113} \approx 10{,}6$ m").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"Corner at $120^\circ$: $\sqrt{113 + 56} = 13$ m — further apart").scale(0.95).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Tighter than 90: closer. Wider: further. At 90: Pythagoras.").scale(0.9).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Wide corner, shorter answer? A minus went missing.").scale(0.9).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the toolbox question ---
        self.next_band(9)
        b9_title = Tex("The toolbox question: what do you HOLD?").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Side-Angle-Side $\\Rightarrow$ cosine rule").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Side-Side-Side $\\Rightarrow$ cosine rule, angle form").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Complete opposite pair $\\Rightarrow$ sine rule").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Angle might be obtuse? Prefer inverse cosine —").scale(0.95).shift(band_shift(9) + DOWN * 1.6)
        b9_l5 = Tex("it tells the twins apart; inverse sine cannot").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): one story, two triangles ---
        self.next_band(10)
        b10_title = Tex("One story, two triangles").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("The triangles share ONE side: the bridge").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Solve the complete triangle first; extract the bridge").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"PQ \approx 6{,}66 \text{ km — carried across UNROUNDED}").scale(0.95).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("Circle the shared side: who supplies it, who spends it").scale(0.95).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.wait(4)
