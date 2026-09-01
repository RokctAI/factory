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

# Band-layout whiteboard scene (reference: quadratics-by-factorisation).
# One band per teaching beat, add-only lifecycle, camera moves down between
# bands. Covers all seven subtopics: Part 1 Expert (the cosine rule and its
# proof, finding a side, finding an angle, 2D problems) then Part 2
# Simplifier (Pythagoras with an attitude adjustment, the toolbox question,
# one story two triangles). Band dwell proportional to subtopics.json
# (230/225/215/240/190/190/190 of 1480 s). Triangles drawn from Line/Dot/Tex
# primitives only.

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
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the rule and its anatomy ---
        title = Tex("The Cosine Rule and 2D Problems").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"a^2 = b^2 + c^2 - 2bc\cos A").scale(1.3).shift(UP * 0.8)
        self.play(Write(b0_l1))
        self.play(Create(SurroundingRectangle(b0_l1, color=GREEN)))
        self.wait(2.5)
        b0_l2 = Tex("The squared side and the cosine angle FACE each other").scale(1.0).shift(DOWN * 0.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Built for SAS and SSS — the sine rule's blind spots").scale(1.0).shift(DOWN * 1.5)
        self.play(Write(b0_l3))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the proof — drop a perpendicular ---
        self.next_band(1)
        b1_title = Tex("Proof: drop a perpendicular from $C$").scale(1.15).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        tc = band_shift(1) + UP * 0.3
        A = tc + LEFT * 2.8 + DOWN * 1.2
        B = tc + RIGHT * 2.8 + DOWN * 1.2
        C = tc + RIGHT * 0.7 + UP * 1.4
        D = tc + RIGHT * 0.7 + DOWN * 1.2
        sAB = Line(A, B)
        sAC = Line(A, C)
        sBC = Line(B, C)
        sCD = DashedLine(C, D, color=YELLOW)
        self.play(Create(sAB), Create(sAC), Create(sBC))
        self.play(Create(sCD))
        lA = MathTex("A").scale(0.9).move_to(A + LEFT * 0.35 + DOWN * 0.1)
        lB = MathTex("B").scale(0.9).move_to(B + RIGHT * 0.35 + DOWN * 0.1)
        lC = MathTex("C").scale(0.9).move_to(C + UP * 0.35)
        lD = MathTex("D").scale(0.9).move_to(D + DOWN * 0.35)
        self.play(Write(lA), Write(lB), Write(lC), Write(lD))
        self.wait(2)
        b1_l1 = MathTex(r"CD = b\sin A, \quad AD = b\cos A").scale(1.05).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"DB = c - b\cos A").scale(1.05).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l2))
        self.wait(2.5)

        # --- Band 2 (subtopic_1): Pythagoras in CDB, identity merges ---
        self.next_band(2)
        b2_title = Tex("Pythagoras in triangle $CDB$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"a^2 = CD^2 + DB^2").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"a^2 = b^2\sin^2 A + c^2 - 2bc\cos A + b^2\cos^2 A").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"b^2(\sin^2 A + \cos^2 A) = b^2 \times 1").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"a^2 = b^2 + c^2 - 2bc\cos A").scale(1.1).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = MathTex(r"A = 90^\circ: \cos A = 0 \Rightarrow a^2 = b^2 + c^2").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): finding a side, acute case ---
        self.next_band(3)
        b3_title = Tex(r"Find $a$: $b = 8$, $c = 5$, $A = 60^\circ$").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"a^2 = 64 + 25 - 2(8)(5)\cos 60^\circ").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\cos 60^\circ = \tfrac{1}{2}: \quad a^2 = 89 - 40").scale(1.1).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"a^2 = 49").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(1.5)
        b3_l4 = MathTex(r"a = 7 \text{ cm}").scale(1.15).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex(r"Square root at the end — 49 is unfinished").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_2): the obtuse case and the sign ---
        self.next_band(4)
        b4_title = Tex(r"Find $q$: $p = 6$, $r = 9$, $Q = 110^\circ$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"q^2 = 36 + 81 - 2(6)(9)\cos 110^\circ").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\cos 110^\circ = -0{,}3420 \;\; (\text{2nd quadrant})").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"q^2 = 117 + 36{,}94 = 153{,}94").scale(1.1).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"q = 12{,}41 \text{ cm}").scale(1.15).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex(r"Beyond $90^\circ$ the correction ADDS — longer side").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): finding an angle from three sides ---
        self.next_band(5)
        b5_title = Tex("Three sides, no angle: rearrange").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\cos A = \frac{b^2 + c^2 - a^2}{2bc}").scale(1.15).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = Tex("Sides 5, 7, 10: largest angle faces the 10").scale(1.0).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"\cos\theta = \tfrac{25+49-100}{2(5)(7)} = -0{,}3714").scale(1.0).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"\theta = 111{,}8^\circ").scale(1.15).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("Negative cosine announced obtuse — no ambiguity").scale(1.0).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the harbour — how far apart? ---
        self.next_band(6)
        b6_title = Tex(r"Two boats: $HP = 4$, $HQ = 6$, $\hat{H} = 70^\circ$").scale(1.1).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_title))
        self.wait(1.5)
        hc = band_shift(6) + UP * 0.6
        H = hc + LEFT * 2.6 + DOWN * 0.4
        P = hc + RIGHT * 0.6 + UP * 1.2
        Q = hc + RIGHT * 2.6 + DOWN * 1.0
        eHP = Line(H, P)
        eHQ = Line(H, Q)
        ePQ = Line(P, Q, color=YELLOW)
        lH = MathTex("H").scale(0.9).move_to(H + LEFT * 0.35)
        lP = MathTex("P").scale(0.9).move_to(P + UP * 0.35)
        lQ = MathTex("Q").scale(0.9).move_to(Q + RIGHT * 0.35)
        l4 = MathTex("4").scale(0.8).move_to((H + P) / 2 + UP * 0.35 + LEFT * 0.2)
        l6 = MathTex("6").scale(0.8).move_to((H + Q) / 2 + DOWN * 0.4)
        l70 = MathTex(r"70^\circ").scale(0.7).move_to(H + RIGHT * 0.85 + UP * 0.05)
        self.play(Create(eHP), Create(eHQ))
        self.play(Write(lH), Write(lP), Write(lQ), Write(l4), Write(l6), Write(l70))
        self.play(Create(ePQ))
        self.wait(2)
        b6_l1 = MathTex(r"PQ^2 = 16 + 36 - 2(4)(6)\cos 70^\circ").scale(1.05).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"= 52 - 16{,}42 = 35{,}58").scale(1.05).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"PQ = 5{,}97 \text{ km}").scale(1.1).shift(band_shift(6) + DOWN * 3.3)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the angle at P, and the habits ---
        self.next_band(7)
        b7_title = Tex(r"Now the angle $H\hat{P}Q$ — three sides known").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\cos P = \frac{16 + 35{,}58 - 36}{2(4)(5{,}97)} = \frac{15{,}58}{47{,}76}").scale(1.0).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"\cos P = 0{,}3262 \;\Rightarrow\; P = 70{,}96^\circ").scale(1.05).shift(band_shift(7) + DOWN * 0.1)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = MathTex(r"\hat{Q} = 180^\circ - 70^\circ - 71^\circ = 39^\circ").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Sketch, name the triangle, count what you hold").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Carry unrounded values; round only the report").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): Pythagoras with an attitude adjustment ---
        self.next_band(8)
        b8_title = Tex("Pythagoras with an attitude adjustment").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Two paths from one corner: 8 m and 5 m").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex(r"Square corner: $64 + 25$, root — Pythagoras").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex(r"Tighter than $90^\circ$: correction subtracts — closer").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex(r"Wider than $90^\circ$: two minuses add — further").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Wide corner, shorter answer? A minus got lost").scale(1.0).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the toolbox question ---
        self.next_band(9)
        b9_title = Tex("The toolbox question: what do you HOLD?").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Two sides + included angle (SAS): cosine rule").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Three sides (SSS): cosine rule, angle form").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("A complete opposite pair: sine rule — lighter").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Possibly obtuse angle? Cosine rule — no twins").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Say the inventory in words — it earns the mark").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): one story, two triangles ---
        self.next_band(10)
        b10_title = Tex("One story, two triangles, one bridge").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Two triangles always share one side — the bridge").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Solve triangle one FOR the bridge").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex(r"Carry it across: $PQ = 5{,}97$ km becomes known").scale(1.0).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Cross with the FULL calculator value, not 5,97").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("Circle the shared side before you compute").scale(1.0).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l5))
        self.wait(4)
