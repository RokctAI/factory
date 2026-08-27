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

# Band-layout whiteboard scene (see the quadratics-by-factorisation worked
# example). One band per teaching beat; the camera moves down to clean space
# and nothing is ever removed. Covers all seven subtopics of the session duo
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
        b0_l1 = Tex(r"In $\triangle ABC$: $D$ midpoint of $AB$, $E$ midpoint of $AC$").scale(1.05).shift(UP * 1.2)
        b0_l2 = MathTex(r"DE \parallel BC, \;\; DE = \tfrac{1}{2}BC").scale(1.1).shift(UP * 0.2)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = Tex(r"One hypothesis, TWO conclusions:").scale(1.1).shift(DOWN * 0.9)
        b0_l4 = Tex(r"direction ($\parallel$) and length (half)").scale(1.1).shift(DOWN * 1.8)
        self.play(Write(b0_l3))
        self.wait(1.5)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex(r"Two midpoints, two DIFFERENT sides, third side").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(b0_l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): numbers on it, and the medial triangle
        self.next_band(1)
        b1_title = Tex(r"$\triangle PQR$: $PQ = 16$, $QR = 24$, $PR = 20$").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"$S$ midpoint of $PQ$, $T$ midpoint of $PR$").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"ST \parallel QR, \quad ST = \tfrac{1}{2}(24) = 12").scale(1.1).shift(band_shift(1) + UP * 0.3)
        b1_l3 = MathTex(r"PS = 8, \quad PT = 10").scale(1.1).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = MathTex(r"\text{Perimeter } \triangle PST = 8 + 12 + 10 = 30").scale(1.05).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_l5 = Tex(r"Half of $60$ — every inner side is half an outer one").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        b1_l6 = Tex(r"Join all three midpoints: 4 congruent triangles").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l5))
        self.wait(2)
        self.play(Write(b1_l6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the proof — construction and congruence
        self.next_band(2)
        b2_title = Tex(r"Proof — produce $DE$ to $F$ with $DE = EF$, join $FC$").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        # triangle ABC with D, E midpoints and F beyond E
        pA = band_shift(2) + LEFT * 4.6 + UP * 1.5
        pB = band_shift(2) + LEFT * 6.2 + DOWN * 1.3
        pC = band_shift(2) + LEFT * 2.4 + DOWN * 1.3
        pD = (pA + pB) / 2
        pE = (pA + pC) / 2
        pF = 2 * pE - pD
        tri = VGroup(Line(pA, pB), Line(pB, pC), Line(pC, pA))
        seg = Line(pD, pF, color=YELLOW)
        segFC = Line(pF, pC, color=YELLOW)
        labA = Tex("A").scale(0.8).next_to(pA, UP, buff=0.12)
        labB = Tex("B").scale(0.8).next_to(pB, DL, buff=0.12)
        labC = Tex("C").scale(0.8).next_to(pC, DR, buff=0.12)
        labD = Tex("D").scale(0.8).next_to(pD, LEFT, buff=0.12)
        labE = Tex("E").scale(0.8).next_to(pE, UP, buff=0.12)
        labF = Tex("F").scale(0.8).next_to(pF, RIGHT, buff=0.12)
        self.play(Create(tri), Write(labA), Write(labB), Write(labC))
        self.wait(1.5)
        self.play(Create(seg), Create(segFC), Write(labD), Write(labE), Write(labF))
        self.wait(2)
        c1 = Tex(r"$AE = EC$ ($E$ midpoint)").scale(1.0).shift(band_shift(2) + RIGHT * 3.0 + UP * 1.0)
        c2 = Tex(r"$DE = EF$ (construction)").scale(1.0).shift(band_shift(2) + RIGHT * 3.0 + UP * 0.1)
        c3 = Tex(r"$\hat{E}_1 = \hat{E}_2$ (vert opp)").scale(1.0).shift(band_shift(2) + RIGHT * 3.0 + DOWN * 0.8)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        c4 = MathTex(r"\triangle ADE \equiv \triangle CFE \;\;\text{(SAS)}").scale(1.1).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(c4))
        self.play(Create(SurroundingRectangle(c4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): harvest — the parallelogram pays out
        self.next_band(3)
        b3_title = Tex("Harvest the congruence").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"$AD = CF$ and $\hat{D}_1 = \hat{F}_1$ (corresp parts)").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"Alt $\angle$s equal: $AD$ and $CF$ are parallel").scale(0.95).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex(r"$AD = DB$ ($D$ midpoint) $\Rightarrow DB = FC$").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex(r"$DBCF$: one pair equal AND parallel $\Rightarrow$ parm").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.wait(2.5)
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = MathTex(r"DF \parallel BC,\; DF = BC,\; DE = \tfrac{1}{2}DF").scale(1.0).shift(band_shift(3) + DOWN * 2.4)
        b3_l6 = MathTex(r"\therefore\; DE \parallel BC, \; DE = \tfrac{1}{2}BC").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
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
        b4_l1 = Tex(r"$D$ midpoint of $AB$, $DE \parallel BC$, $E$ on $AC$").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"\Rightarrow\; AE = EC").scale(1.15).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex(r"Theorem: two midpoints $\Rightarrow$ parallel and half").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex(r"Converse: one midpoint $+$ parallel $\Rightarrow$ midpoint").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        b4_l5 = Tex(r"Reason: ``line through midpoint parallel to 2nd side''").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.wait(2.5)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): worked example — chaining both versions
        self.next_band(5)
        b5_title = Tex(r"$AB = 14$, $BC = 18$, $AD = 7$, $DE \parallel BC$").scale(0.9).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"AD = 7 = \tfrac{1}{2}(14): \; D \text{ a midpoint}").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"$DE \parallel BC \Rightarrow E$ midpoint (converse)").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex(r"Now the theorem applies as well:").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = MathTex(r"DE = \tfrac{1}{2} BC = \tfrac{1}{2}(18) = 9").scale(1.1).shift(band_shift(5) + DOWN * 1.6)
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
        b6_title = Tex(r"Rider: $D, E, F$ midpoints — prove $DEFB$ is a parm").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Target: one pair of sides equal AND parallel").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"DE \parallel BC, \; DE = \tfrac{1}{2}BC \;\text{(midpt thm)}").scale(0.9).shift(band_shift(6) + UP * 0.3)
        b6_l3 = MathTex(r"BF = \tfrac{1}{2}BC \;\;\text{($F$ midpoint of $BC$)}").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex(r"$\therefore DE = BF$, and $DE \parallel BF$ ($BF$ along $BC$)").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        b6_l5 = Tex(r"$DEFB$ is a parallelogram (pair equal and $\parallel$)").scale(1.0).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the error museum
        self.next_band(7)
        b7_title = Tex("The error museum — five exhibits").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"1. One midpoint, nothing parallel — theorem fails").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"2. Doubling instead of halving").scale(1.0).shift(band_shift(7) + UP * 0.3)
        b7_l2b = MathTex(r"DE = 12 \to BC = 24; \; BC = 12 \to DE = 6").scale(0.9).shift(band_shift(7) + DOWN * 0.5)
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
        beam_lab = Tex("beam 6 m").scale(0.85).next_to(Line(rL, rR).get_center(), DOWN, buff=0.15)
        brace_lab = Tex("brace 3 m").scale(0.85).next_to(brace.get_center(), UP, buff=0.15)
        self.play(Create(roof), Write(beam_lab))
        self.wait(2)
        self.play(Create(brace), Write(brace_lab))
        self.wait(2)
        b8_l1 = Tex(r"Level — exactly parallel to the beam").scale(1.0).shift(band_shift(8) + RIGHT * 3.4 + UP * 0.9)
        b8_l2 = Tex(r"Exactly half: cut it on the ground").scale(1.0).shift(band_shift(8) + RIGHT * 3.4 + UP * 0.0)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"10 \to 5, \quad 7 \to 3{,}5, \quad 24 \to 12").scale(1.05).shift(band_shift(8) + DOWN * 1.6)
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
        b9_l2 = Tex(r"It slots in: the pieces make a parallelogram").scale(1.05).shift(band_shift(9) + UP * 0.2)
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
        b9_l5 = Tex(r"Join all three marks: four identical wedges").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): spotting it under exam pressure
        self.next_band(10)
        b10_title = Tex("Spotting it under exam pressure").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Calling card: midpoints on TWO sides of a triangle").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"Write BOTH gifts: the parallel and the half").scale(1.0).shift(band_shift(10) + UP * 0.3)
        b10_l3 = Tex(r"One midpoint $+$ a parallel: second midpoint free").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"DE = \tfrac{1}{2}BC = BF \;\text{ and }\; DE \parallel BF").scale(1.05).shift(band_shift(10) + DOWN * 1.5)
        b10_l5 = Tex(r"$\Rightarrow DEFB$ is a parallelogram").scale(1.1).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l4))
        self.wait(2.5)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(2)
        b10_l6 = Tex(r"A reason beside every claim — two phrases, a mark each").scale(0.9).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l6))
        self.wait(4)
