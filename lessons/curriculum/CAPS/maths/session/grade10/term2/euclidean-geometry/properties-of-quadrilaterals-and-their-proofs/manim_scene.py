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

# Band-layout whiteboard scene (see AUTHORING-SPEC / the quadratics-by-
# factorisation worked example). One band per teaching beat, camera moves
# down to clean space, nothing is ever removed. Covers all seven subtopics
# of the session duo (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7), dwell times roughly proportional to subtopics.json
# (225/240/225/240/185/195/190 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a term, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class QuadrilateralPropertiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the family of quadrilaterals
        title = Tex("The Special Quadrilaterals").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Quadrilateral: four sides, angles sum $360^\circ$").scale(1.1).shift(UP * 1.3)
        b0_l2 = Tex(r"Trapezium: ONE pair of opposite sides parallel").scale(1.1).shift(UP * 0.4)
        b0_l3 = Tex(r"Parallelogram: BOTH pairs parallel").scale(1.1).shift(DOWN * 0.5)
        b0_l4 = Tex(r"Rectangle: parallelogram $+$ a $90^\circ$ angle").scale(1.1).shift(DOWN * 1.4)
        b0_l5 = Tex(r"Rhombus: parallelogram $+$ adjacent sides equal").scale(1.1).shift(DOWN * 2.3)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): square, kite, and the hierarchy
        self.next_band(1)
        b1_title = Tex("The hierarchy runs one way only").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Square: rectangle AND rhombus at once").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex(r"Kite: two pairs of ADJACENT sides equal").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex(r"square $\Rightarrow$ rectangle $\Rightarrow$ parm").scale(1.1).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = Tex(r"square $\Rightarrow$ rhombus $\Rightarrow$ parm").scale(1.1).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex(r"A rectangle need not be a rhombus").scale(1.05).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the four properties
        self.next_band(2)
        b2_title = Tex("A parallelogram owns four properties").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"1. Both pairs of opposite sides equal").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"2. Both pairs of opposite angles equal").scale(1.1).shift(band_shift(2) + UP * 0.2)
        b2_l3 = Tex(r"3. Diagonals bisect each other").scale(1.1).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex(r"4. Consecutive angles add to $180^\circ$").scale(1.1).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex(r"(co-interior angles between parallel lines)").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): proof — opposite sides are equal
        self.next_band(3)
        b3_title = Tex(r"Prove: opposite sides of parm $ABCD$ are equal").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        # parallelogram ABCD with diagonal AC, drawn from Lines only
        pA = band_shift(3) + LEFT * 5.2 + UP * 1.4
        pB = band_shift(3) + LEFT * 1.8 + UP * 1.4
        pC = band_shift(3) + LEFT * 2.6 + DOWN * 0.2
        pD = band_shift(3) + LEFT * 6.0 + DOWN * 0.2
        quad = VGroup(Line(pA, pB), Line(pB, pC), Line(pC, pD), Line(pD, pA))
        diag = Line(pA, pC, color=YELLOW)
        labA = Tex("A").scale(0.9).next_to(pA, UP, buff=0.15)
        labB = Tex("B").scale(0.9).next_to(pB, UP, buff=0.15)
        labC = Tex("C").scale(0.9).next_to(pC, DOWN, buff=0.15)
        labD = Tex("D").scale(0.9).next_to(pD, DOWN, buff=0.15)
        self.play(Create(quad), Write(labA), Write(labB), Write(labC), Write(labD))
        self.wait(1.5)
        self.play(Create(diag))
        self.wait(1.5)
        c1 = Tex(r"$\hat{A}_1 = \hat{C}_1$ (alt $\angle$s, $AB \parallel DC$)").scale(1.0).shift(band_shift(3) + RIGHT * 2.6 + UP * 1.3)
        c2 = Tex(r"$\hat{C}_2 = \hat{A}_2$ (alt $\angle$s, $AD \parallel BC$)").scale(1.0).shift(band_shift(3) + RIGHT * 2.6 + UP * 0.4)
        c3 = Tex(r"$AC = CA$ (common)").scale(1.0).shift(band_shift(3) + RIGHT * 2.6 + DOWN * 0.5)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        c4 = MathTex(r"\triangle ABC \equiv \triangle CDA \;\; \text{(AAS)}").scale(1.05).shift(band_shift(3) + DOWN * 1.6)
        c5 = MathTex(r"\therefore\; AB = CD \;\text{ and }\; BC = DA").scale(1.05).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(c4))
        self.wait(2)
        self.play(Write(c5))
        self.play(Create(SurroundingRectangle(c5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): numerical application in parm PQRS
        self.next_band(4)
        b4_title = Tex(r"Parm $PQRS$ — find all four angles").scale(1.1).shift(band_shift(4) + UP * 2.3)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_given = MathTex(r"\hat{P} = 3x + 10^\circ, \quad \hat{Q} = 2x + 20^\circ").scale(1.05).shift(band_shift(4) + UP * 1.55)
        self.play(Write(b4_given))
        self.wait(1.5)
        b4_l1 = MathTex(r"3x + 10 + 2x + 20 = 180").scale(1.05).shift(band_shift(4) + UP * 0.7)
        b4_r1 = Tex(r"(consecutive $\angle$s of parm)").scale(0.95).shift(band_shift(4) + UP * 0.0)
        b4_l2 = MathTex(r"5x + 30 = 180 \;\Rightarrow\; 5x = 150").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        b4_l3 = MathTex(r"x = 30").scale(1.1).shift(band_shift(4) + DOWN * 1.45)
        b4_l4 = MathTex(r"\hat{P} = \hat{R} = 100^\circ, \; \hat{Q} = \hat{S} = 80^\circ").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_r1))
        self.wait(1.5)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(1.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex(r"Check: $100 + 80 + 100 + 80 = 360$").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): five conditions for a parallelogram
        self.next_band(5)
        b5_title = Tex("Enough to PROVE a parallelogram (any one)").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"1. Both pairs of opposite sides parallel").scale(1.05).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"2. Both pairs of opposite sides equal").scale(1.05).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"3. Both pairs of opposite angles equal").scale(1.05).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex(r"4. Diagonals bisect each other").scale(1.05).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex(r"5. ONE pair of sides equal AND parallel").scale(1.05).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l1))
        self.wait(1.5)
        self.play(Write(b5_l2))
        self.wait(1.5)
        self.play(Write(b5_l3))
        self.wait(1.5)
        self.play(Write(b5_l4))
        self.wait(1.5)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_l6 = Tex(r"Equal alone is not enough; parallel alone is not enough").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.wait(2.5)

        # --- Band 6 (subtopic_3): conditions for the special shapes
        self.next_band(6)
        b6_title = Tex("Conditions for the special shapes").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Rectangle: parm $+$ one $90^\circ$ angle").scale(1.05).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"Rectangle: parm $+$ EQUAL diagonals").scale(1.05).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex(r"Rhombus: parm $+$ adjacent sides equal").scale(1.05).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex(r"Rhombus: parm $+$ PERPENDICULAR diagonals").scale(1.05).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex(r"Square: equal diagonals at right angles").scale(1.05).shift(band_shift(6) + DOWN * 2.0)
        b6_l6 = Tex(r"Kite: long diagonal bisects the short one $\perp$").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(2)
        self.play(Write(b6_l6))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the rider, statement by statement
        self.next_band(7)
        b7_title = Tex(r"Rider: parm $ABCD$, $E, F$ on $AC$, $AE = CF$").scale(1.1).shift(band_shift(7) + UP * 2.2)
        b7_goal = Tex(r"Prove $BEDF$ is a parallelogram").scale(1.1).shift(band_shift(7) + UP * 1.3)
        self.play(Write(b7_title))
        self.wait(2)
        self.play(Write(b7_goal))
        self.wait(2)
        b7_l1 = Tex(r"Target: diagonals $EF$ and $BD$ bisect each other").scale(1.0).shift(band_shift(7) + UP * 0.4)
        b7_l2 = Tex(r"$AO = OC$ and $BO = OD$ (diags of parm $ABCD$)").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l3 = Tex(r"$AE = CF$ (given)").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
        b7_l4 = MathTex(r"EO = AO - AE = OC - CF = OF").scale(1.05).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex(r"$\therefore BEDF$ is a parm (diags bisect each other)").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): setting out, and the error museum
        self.next_band(8)
        b8_title = Tex("Statement on the left, reason on the right").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"1. Never assume what must be proved").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"2. A sketch is a guide, never evidence").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex(r"3. A statement with no reason scores nothing").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex(r"4. angle-side-side as a congruence test").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.play(Create(strike(b8_l4)))
        self.wait(2)
        b8_l5 = Tex(r"Equal parts must CORRESPOND").scale(1.05).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the family where every child inherits
        self.next_band(9)
        b9_title = Tex("The family where every child inherits").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Parallelogram: rails and sleepers — sides parallel").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"Rectangle adds square corners").scale(1.05).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex(r"Rhombus adds four equal sides").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = Tex(r"Square inherits from BOTH").scale(1.05).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex(r"Blazer and badge: inheritance runs DOWNWARD only").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): cut it corner to corner
        self.next_band(10)
        b10_title = Tex("Cut it corner to corner").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"One cut $\Rightarrow$ two identical triangles").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex(r"Opposite sides equal, diagonals cut in half").scale(1.05).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex(r"Neighbouring corners add to $180^\circ$").scale(1.05).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"5x + 30 = 180 \;\Rightarrow\; x = 30").scale(1.05).shift(band_shift(10) + DOWN * 1.6)
        b10_l5 = MathTex(r"100^\circ,\; 80^\circ,\; 100^\circ,\; 80^\circ").scale(1.1).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): a proof is a chain of receipts
        self.next_band(11)
        b11_title = Tex("A proof is a chain of receipts").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"Every claim needs its receipt — the reason").scale(1.05).shift(band_shift(11) + UP * 1.1)
        b11_l2 = Tex(r"Properties come AFTER proving the shape").scale(1.05).shift(band_shift(11) + UP * 0.2)
        b11_l3 = Tex(r"Aim first: diagonals cut each other in half").scale(1.05).shift(band_shift(11) + DOWN * 0.7)
        self.play(Write(b11_l1))
        self.wait(2.5)
        self.play(Write(b11_l2))
        self.wait(2.5)
        self.play(Write(b11_l3))
        self.wait(2)
        b11_l4 = Tex(r"$EO = OF$ and $BO = OD$ $\Rightarrow$ $BEDF$ is a parm").scale(1.0).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(2.5)
        b11_l5 = Tex(r"Never trust the picture — prove it").scale(1.05).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11_l5))
        self.wait(4)
