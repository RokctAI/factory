# Copyright (c) 2026 RokctAI
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

# Band-layout whiteboard scene for the session duo "Venn Diagrams and the
# Addition Rule" (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier:
# subtopics 5-7). One band per teaching beat, add-only lifecycle, camera
# moves down between bands. Only exporter-supported mobjects; write-only
# reveals. Band dwell times follow subtopics.json
# (225/235/220/235/190/190/195 of 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VennDiagramsAdditionRuleSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the theoretical model ---
        title = Tex("Venn Diagrams and the Addition Rule").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Theoretical model: reason from symmetry").scale(1.1).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"P(\text{event}) = \frac{\text{favourable outcomes}}{\text{total outcomes}}").scale(1.05).shift(UP * 0.0)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = MathTex(r"P(\text{greater than 4}) = \tfrac{2}{6} = \tfrac{1}{3}").scale(1.05).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Entry fee: outcomes must be EQUALLY LIKELY").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): relative frequency ---
        self.next_band(1)
        b1_title = Tex("Relative frequency: measure, don't argue").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"\text{RF} = \frac{\text{times the event occurred}}{\text{number of trials}}").scale(1.05).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"\text{Courier: } \tfrac{35}{250} = 0{,}14 \text{ late}").scale(1.05).shift(band_shift(1) + DOWN * 0.1)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Jumpy for few trials, settles as trials grow").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Symmetric objects: theory. Messy reality: tally.").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the grade's Venn, overlap first ---
        self.next_band(2)
        b2_title = Tex("150 learners: 75 cricket, 60 rugby, 25 both").scale(1.05).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        vc = band_shift(2) + DOWN * 0.5
        box = Rectangle(width=7.6, height=4.4).move_to(vc)
        cC = Circle(radius=1.6, color=BLUE).move_to(vc + LEFT * 1.0)
        cR = Circle(radius=1.6, color=YELLOW).move_to(vc + RIGHT * 1.0)
        lC = Tex("C").scale(1.0).move_to(vc + LEFT * 2.9 + UP * 1.6)
        lR = Tex("R").scale(1.0).move_to(vc + RIGHT * 2.9 + UP * 1.6)
        self.play(Create(box), Create(cC), Create(cR))
        self.play(Write(lC), Write(lR))
        self.wait(2)
        n_mid = MathTex("25").scale(0.95).move_to(vc)
        self.play(Write(n_mid))
        self.wait(2)
        n_c = MathTex("50").scale(0.95).move_to(vc + LEFT * 1.8)
        n_r = MathTex("35").scale(0.95).move_to(vc + RIGHT * 1.8)
        self.play(Write(n_c), Write(n_r))
        self.wait(2)
        n_out = MathTex("40").scale(0.95).move_to(vc + RIGHT * 3.2 + DOWN * 1.8)
        self.play(Write(n_out))
        self.wait(2)
        b2_sum = MathTex(r"150 - (50 + 25 + 35) = 40 \text{ outside}").scale(1.0).shift(band_shift(2) + DOWN * 3.4)
        self.play(Write(b2_sum))
        self.wait(3)

        # --- Band 3 (subtopic_2): the addition rule ---
        self.next_band(3)
        b3_title = Tex("Never count anyone twice").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"75 + 60 = 135 \;\text{(overlap counted twice!)}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.play(Create(strike(b3_l1)))
        self.wait(2.5)
        b3_l2 = MathTex(r"75 + 60 - 25 = 110").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = MathTex(r"\tfrac{75}{150} + \tfrac{60}{150} - \tfrac{25}{150} = \tfrac{110}{150} = \tfrac{11}{15}").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): mutually exclusive ---
        self.next_band(4)
        b4_title = Tex("Mutually exclusive: circles that never touch").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"P(A \text{ and } B) = 0").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"\text{so } P(A \text{ or } B) = P(A) + P(B)").scale(1.05).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"P(\text{six or less than three}) = \tfrac{1}{6} + \tfrac{2}{6} = \tfrac{1}{2}").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("The short rule is a privilege, never a default").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): complementary, and the distinction ---
        self.next_band(5)
        b5_title = Tex("Complementary: exclusive AND exhaustive").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"P(\text{not } A) = 1 - P(A)").scale(1.1).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = Tex("Six and less-than-three: exclusive, yes —").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("but 3, 4, 5 belong to neither: NOT complementary").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Two checks: no overlap, and nothing left outside").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): independence and the product rule ---
        self.next_band(6)
        b6_title = Tex("Independence: no influence at all").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"A, B \text{ independent} \iff P(A \text{ and } B) = P(A) \times P(B)").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{Two flips: } \tfrac{1}{2} \times \tfrac{1}{2} = \tfrac{1}{4}").scale(1.05).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("With replacement: reset. Without: dependent.").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): test independence in the data ---
        self.next_band(7)
        b7_title = Tex("Test it — never assume it").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"P(C) \times P(R) = 0{,}5 \times 0{,}4 = 0{,}2").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"P(C \text{ and } R) = \tfrac{25}{150} \approx 0{,}167").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"0{,}167 \neq 0{,}2 \;\Rightarrow\; \text{dependent}").scale(1.1).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Exclusive is about overlap; independent is about influence").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): symmetry or tally ---
        self.next_band(8)
        b8_title = Tex("Guessing from symmetry or counting the tally").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Drawing pin: two outcomes, but NOT equally likely").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{Tally: } \tfrac{122}{200} = 0{,}61 \text{ point-up}").scale(1.05).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Symmetric by manufacture: theory. Lopsided: tally.").scale(0.95).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Small tallies lie; long tallies settle").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the double-counted friends ---
        self.next_band(9)
        b9_title = Tex("Two WhatsApp groups, 25 friends in both").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"75 + 60 = 135 \;\text{people?}").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.play(Create(strike(b9_l1)))
        self.wait(2.5)
        b9_l2 = MathTex(r"75 + 60 - 25 = 110 \text{ distinct people}").scale(1.05).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("That subtraction IS the addition rule").scale(1.05).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Overlap first: 25, then 50, then 35, then 40 outside").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): the coin has no memory ---
        self.next_band(10)
        b10_title = Tex("The coin has no memory").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Four heads in a row: the fifth flip is still fifty-fifty").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{Independent: } \tfrac{1}{2} \times \tfrac{1}{2} = \tfrac{1}{4}").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{Data: } 0{,}2 \text{ predicted vs } 0{,}167 \text{ actual — dependent}").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("Exclusive kills; independent ignores — separate pockets").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(4)
