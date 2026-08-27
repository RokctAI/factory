# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# Band-layout whiteboard scene: one band per teaching beat, camera moves down
# to clean space, nothing is ever removed. Covers all seven subtopics
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7),
# dwell times roughly proportional to subtopics.json
# (215/230/220/240/180/190/195 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a term, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MidpointTheoremSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the statement and its structure
        title = Tex("The Midpoint Theorem").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"In $\triangle PQR$: $M$ midpoint of $PQ$, $N$ midpoint of $PR$").scale(1.05).shift(UP * 1.2)
        b0_l2 = MathTex(r"MN \parallel QR, \;\; MN = \tfrac{1}{2}QR").scale(1.1).shift(UP * 0.2)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2)
        b0_l3 = Tex(r"One hypothesis, TWO conclusions:").scale(1.1).shift(DOWN * 0.9)
        b0_l4 = Tex(r"direction ($\parallel$) and length (half)").scale(1.1).shift(DOWN * 1.8)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex(r"Two midpoints, two DIFFERENT sides, third side").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(b0_l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): numbers on it, and the medial triangle
        self.next_band(1)
        b1_title = Tex(r"$\triangle XYZ$: $XY = 18$, $YZ = 30$, $XZ = 22$").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex(r"$M$ midpoint of $XY$, $N$ midpoint of $XZ$").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"MN \parallel YZ, \quad MN = \tfrac{1}{2}(30) = 15").scale(1.1).shift(band_shift(1) + UP * 0.3)
        b1_l3 = MathTex(r"XM = 9, \quad XN = 11").scale(1.1).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = MathTex(r"\text{Perimeter } \triangle XMN = 9 + 15 + 11 = 35").scale(1.05).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex(r"Half of $70$ — every inner side is half an outer one").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        b1_l6 = Tex(r"Join all three midpoints: 4 congruent triangles").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l5))
        self.wait(2)
        self.play(Write(b1_l6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the proof — construction and congruence
        self.next_band(2)
        b2_title = Tex(r"Proof — extend $MN$ to $K$ with $MN = NK$, join $KR$").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        # triangle PQR with M, N midpoints and K beyond N
        pP = band_shift(2) + LEFT * 4.6 + UP * 1.5
        pQ = band_shift(2) + LEFT * 6.2 + DOWN * 1.3
        pR = band_shift(2) + LEFT * 2.4 + DOWN * 1.3
        pM = (pP + pQ) / 2
        pN = (pP + pR) / 2
        pK = 2 * pN - pM
        tri = VGroup(Line(pP, pQ), Line(pQ, pR), Line(pR, pP))
        seg = Line(pM, pK, color=YELLOW)
        segKR = Line(pK, pR, color=YELLOW)
        labP = Tex("P").scale(0.8).next_to(pP, UP, buff=0.12)
        labQ = Tex("Q").scale(0.8).next_to(pQ, DL, buff=0.12)
        labR = Tex("R").scale(0.8).next_to(pR, DR, buff=0.12)
        labM = Tex("M").scale(0.8).next_to(pM, LEFT, buff=0.12)
        labN = Tex("N").scale(0.8).next_to(pN, UP, buff=0.12)
        labK = Tex("K").scale(0.8).next_to(pK, RIGHT, buff=0.12)
        self.play(Create(tri), Write(labP), Write(labQ), Write(labR))
        self.wait(1.5)
        self.play(Create(seg), Create(segKR), Write(labM), Write(labN), Write(labK))
        self.wait(2)
        c1 = Tex(r"$PN = NR$ ($N$ midpoint)").scale(1.0).shift(band_shift(2) + RIGHT * 3.0 + UP * 1.0)
        c2 = Tex(r"$MN = NK$ (construction)").scale(1.0).shift(band_shift(2) + RIGHT * 3.0 + UP * 0.1)
        c3 = Tex(r"$\hat{N}_1 = \hat{N}_2$ (vert opp)").scale(1.0).shift(band_shift(2) + RIGHT * 3.0 + DOWN * 0.8)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        c4 = MathTex(r"\triangle PMN \equiv \triangle RKN \;\;\text{(SAS)}").scale(1.1).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(c4))
        self.play(Create(SurroundingRectangle(c4, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): harvest — the parallelogram pays out
        self.next_band(3)
        b3_title = Tex("Harvest the congruence").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"$PM = RK$ and $\hat{M}_1 = \hat{K}_1$ (corresp parts)").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"Alt $\angle$s equal: $PM$ and $RK$ are parallel").scale(0.95).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex(r"$PM = MQ$ ($M$ midpoint) $\Rightarrow MQ = KR$").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex(r"$MQRK$: one pair equal AND parallel $\Rightarrow$ parm").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2.5)
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = MathTex(r"MK \parallel QR,\; MK = QR,\; MN = \tfrac{1}{2}MK").scale(1.0).shift(band_shift(3) + DOWN * 2.4)
        b3_l6 = MathTex(r"\therefore\; MN \parallel QR, \; MN = \tfrac{1}{2}QR").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.wait(2)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the converse
        self.next_band(4)
        b4_title = Tex("The converse — one midpoint and a parallel").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"$P$ midpoint of $AB$, $PQ \parallel BC$, $Q$ on $AC$").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"\Rightarrow\; AQ = QC").scale(1.15).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = Tex(r"Theorem: two midpoints $\Rightarrow$ parallel and half").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex(r"Converse: one midpoint $+$ parallel $\Rightarrow$ midpoint").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        b4_l5 = Tex(r"Reason: ``line through midpoint parallel to 2nd side''").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): worked example — chaining both versions
        self.next_band(5)
        b5_title = Tex(r"$AB = 16$, $BC = 26$, $AP = 8$, $PQ \parallel BC$").scale(0.9).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"AP = 8 = \tfrac{1}{2}(16): \; P \text{ a midpoint}").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"$PQ \parallel BC \Rightarrow Q$ midpoint (converse)").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex(r"Now the theorem applies as well:").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = MathTex(r"PQ = \tfrac{1}{2} BC = \tfrac{1}{2}(26) = 13").scale(1.1).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"Two theorems chained — the first delivers the midpoint").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the rider
        self.next_band(6)
        b6_title = Tex(r"Rider: $X, Y, Z$ midpoints — prove $XYZL$ is a parm").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Target: one pair of sides equal AND parallel").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"XY \parallel LM, \; XY = \tfrac{1}{2}LM \;\text{(midpt thm)}").scale(0.9).shift(band_shift(6) + UP * 0.3)
        b6_l3 = MathTex(r"LZ = \tfrac{1}{2}LM \;\;\text{($Z$ midpoint of $LM$)}").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex(r"$\therefore XY = LZ$, and $XY \parallel LZ$ ($LZ$ along $LM$)").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        b6_l5 = Tex(r"$XYZL$ is a parallelogram (pair equal and $\parallel$)").scale(1.0).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.wait(2.5)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the error museum
        self.next_band(7)
        b7_title = Tex("The error museum — five exhibits").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"1. One midpoint, nothing parallel — theorem fails").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"2. Doubling instead of halving").scale(1.0).shift(band_shift(7) + UP * 0.3)
        b7_l2b = MathTex(r"MN = 15 \to YZ = 30; \; YZ = 15 \to MN = 7{,}5").scale(0.9).shift(band_shift(7) + DOWN * 0.5)
        b7_l3 = Tex(r"3. Reading midpoints off the sketch").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        b7_l4 = Tex(r"4. Assuming the midpoint you must prove (circular)").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        b7_l5 = Tex(r"5. A statement with no reason earns nothing").scale(1.0).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(1.5)
        self.play(Write(b7_l2b))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): halfway up two rafters
        self.next_band(8)
        b8_title = Tex("Halfway up two rafters").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        # roof: two rafters and base beam, brace at midpoints
        rL = band_shift(8) + LEFT * 6.0 + DOWN * 0.4
        rR = band_shift(8) + LEFT * 2.0 + DOWN * 0.4
        rT = band_shift(8) + LEFT * 4.0 + UP * 1.4
        roof = VGroup(Line(rL, rT), Line(rR, rT), Line(rL, rR))
        brace = Line((rL + rT) / 2, (rR + rT) / 2, color=YELLOW)
        beam_lab = Tex("beam 8 m").scale(0.85).next_to(Line(rL, rR).get_center(), DOWN, buff=0.15)
        brace_lab = Tex("brace 4 m").scale(0.85).next_to(brace.get_center(), UP, buff=0.15)
        self.play(Create(roof), Write(beam_lab))
        self.wait(2)
        self.play(Create(brace), Write(brace_lab))
        self.wait(2)
        b8_l1 = Tex(r"Level — exactly parallel to the beam").scale(1.0).shift(band_shift(8) + RIGHT * 3.4 + UP * 0.9)
        b8_l2 = Tex(r"Exactly half: cut it at the saw bench").scale(1.0).shift(band_shift(8) + RIGHT * 3.4 + UP * 0.0)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"12 \to 6, \quad 9 \to 4{,}5, \quad 30 \to 15").scale(1.05).shift(band_shift(8) + DOWN * 1.6)
        b8_l4 = Tex(r"The join is always the SHORT one").scale(1.05).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l3))
        self.wait(2.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): why exactly half
        self.next_band(9)
        b9_title = Tex("Why exactly half — cut and spin").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Cut along the brace, spin the top triangle").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"It clicks in: the pieces make a parallelogram").scale(1.05).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex(r"Top edge: two braces. Bottom edge: one beam").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"2 \times \text{brace} = 1 \times \text{beam}").scale(1.05).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex(r"Join all three marks: four identical quarters").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): spotting it under exam pressure
        self.next_band(10)
        b10_title = Tex("Spotting it under exam pressure").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Signature: midpoints on TWO sides of a triangle").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"Write BOTH gifts: the parallel and the half").scale(1.0).shift(band_shift(10) + UP * 0.3)
        b10_l3 = Tex(r"One midpoint $+$ a parallel: second midpoint free").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"XY = \tfrac{1}{2}LM = LZ \;\text{ and }\; XY \parallel LZ").scale(1.05).shift(band_shift(10) + DOWN * 1.5)
        b10_l5 = Tex(r"$\Rightarrow XYZL$ is a parallelogram").scale(1.1).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l4))
        self.wait(2.5)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(2)
        b10_l6 = Tex(r"A reason beside every claim — two phrases, a mark each").scale(0.9).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l6))
        self.wait(4)
