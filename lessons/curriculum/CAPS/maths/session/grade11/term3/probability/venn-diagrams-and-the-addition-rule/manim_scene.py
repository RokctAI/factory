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

# Band-layout whiteboard scene (reference: quadratics-by-factorisation).
# One band per teaching beat, add-only lifecycle, camera moves down between
# bands. Covers all seven subtopics: Part 1 Expert (two probability models,
# Venn diagrams and the addition rule, mutually exclusive and complementary,
# independence and the product rule) then Part 2 Simplifier (symmetry vs
# tally, WhatsApp groups, the coin has no memory). Band dwell proportional to
# subtopics.json (225/235/220/235/190/190/195 of 1490 s).

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
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the theoretical model ---
        title = Tex("Venn Diagrams and the Addition Rule").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Probability: a number from 0 to 1").scale(1.1).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Theoretical — needs EQUALLY LIKELY outcomes").scale(1.05).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"P(\text{even on a die}) = \tfrac{3}{6} = \tfrac{1}{2}").scale(1.15).shift(DOWN * 1.0)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = Tex("No experiment needed — but symmetry is the price").scale(1.05).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): relative frequency ---
        self.next_band(1)
        b1_title = Tex("Relative frequency — measure, don't reason").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("500 taxi trips logged, 60 late:").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"P(\text{late}) \approx \tfrac{60}{500} = 0{,}12").scale(1.15).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Wobbles when trials are few, settles as they grow").scale(1.05).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Coins and dice: theory. Messy real events: data").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the school Venn, overlap first ---
        self.next_band(2)
        b2_title = Tex("120 learners: 70 music, 50 gaming, 30 both").scale(1.1).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        vc = band_shift(2) + DOWN * 0.5
        box = Rectangle(width=7.4, height=4.4).move_to(vc)
        cM = Circle(radius=1.5, color=BLUE).move_to(vc + LEFT * 0.9)
        cG = Circle(radius=1.5, color=YELLOW).move_to(vc + RIGHT * 0.9)
        lM = Tex("M").scale(1.0).move_to(vc + LEFT * 2.7 + UP * 1.6)
        lG = Tex("G").scale(1.0).move_to(vc + RIGHT * 2.7 + UP * 1.6)
        self.play(Create(box), Create(cM), Create(cG))
        self.play(Write(lM), Write(lG))
        self.wait(2)
        rule = Tex("Start with the overlap").scale(1.0).shift(band_shift(2) + DOWN * 3.4)
        self.play(Write(rule))
        n_both = MathTex("30").scale(0.95).move_to(vc)
        self.play(Write(n_both))
        self.wait(2)
        n_m = MathTex(r"70 - 30 = 40").scale(0.8).move_to(vc + LEFT * 1.75)
        n_g = MathTex(r"50 - 30 = 20").scale(0.8).move_to(vc + RIGHT * 1.75)
        self.play(Write(n_m))
        self.wait(2)
        self.play(Write(n_g))
        self.wait(2)
        n_out = MathTex(r"120 - 90 = 30").scale(0.8).move_to(vc + RIGHT * 2.3 + DOWN * 1.85)
        self.play(Write(n_out))
        self.wait(3)

        # --- Band 3 (subtopic_2): the addition rule ---
        self.next_band(3)
        b3_title = Tex("Music OR gaming — never count twice").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_wrong = MathTex(r"70 + 50 = 120 \;\Rightarrow\; \text{a certainty?}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l1 = Tex("The 30 in the overlap were counted twice").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"70 + 50 - 30 = 90 \Rightarrow P = \tfrac{90}{120} = 0{,}75").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Given any three quantities, solve for the fourth").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): mutually exclusive ---
        self.next_band(4)
        b4_title = Tex("Mutually exclusive: cannot happen together").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"P(A \text{ and } B) = 0: \; P(A \text{ or } B) = P(A) + P(B)").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"Die: ``multiple of 4'' and ``odd'' share nothing").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\tfrac{1}{6} + \tfrac{3}{6} = \tfrac{4}{6} = \tfrac{2}{3}").scale(1.15).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("A privilege, not a default — check the overlap first").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): complementary, and the distinction ---
        self.next_band(5)
        b5_title = Tex("Complementary: exclusive AND exhaustive").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"P(\text{not } A) = 1 - P(A)").scale(1.2).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = Tex(r"$P(\text{at least one}) = 1 - P(\text{none})$ — the shortcut").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"``Multiple of 4'', ``odd'': exclusive, $\tfrac{2}{3} \neq 1$").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Two checks: no overlap, and nothing left outside").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): independence and the product rule ---
        self.next_band(6)
        b6_title = Tex("Independent: one leaves the other untouched").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"A, B \text{ independent} \iff P(A \text{ and } B) = P(A) \times P(B)").scale(0.95).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = MathTex(r"P(H \text{ then } H) = \tfrac{1}{2} \times \tfrac{1}{2} = \tfrac{1}{4}").scale(1.1).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("With replacement: independent — the pack resets").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Without replacement: dependent — chances change").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): test independence in the data ---
        self.next_band(7)
        b7_title = Tex("Is music independent of gaming? TEST it").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"P(M) \times P(G) = \tfrac{70}{120} \times \tfrac{50}{120} = 0{,}243").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"P(M \text{ and } G) = \tfrac{30}{120} = 0{,}25").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"0{,}25 \neq 0{,}243 \;\Rightarrow\; \text{not independent}").scale(1.05).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex("Exclusive is about overlap; independent, influence").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): symmetry or tally ---
        self.next_band(8)
        b8_title = Tex("Guess from symmetry, or count the tally").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_wrong = Tex(r"``Two sides, so fifty-fifty'' — no symmetry!").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_wrong))
        self.play(Create(strike(b8_wrong)))
        self.wait(2.5)
        b8_l1 = MathTex(r"\text{Tally: } \tfrac{63}{100} = 0{,}63 \text{ butter-down}").scale(1.1).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l1))
        self.play(Create(SurroundingRectangle(b8_l1, color=GREEN)))
        self.wait(2.5)
        b8_l2 = Tex("Jumpy at first, honest in the long run").scale(1.05).shift(band_shift(8) + DOWN * 1.0)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Name your model and your reason in a sentence").scale(1.05).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l3))
        self.wait(3)

        # --- Band 9 (subtopic_6): the double-counted friends ---
        self.next_band(9)
        b9_title = Tex("Two WhatsApp groups, double-counted friends").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_wrong = MathTex(r"70 + 50 = 120 \text{ people?}").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2)
        b9_l1 = Tex("30 sit in BOTH lists — counted twice").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = MathTex(r"70 + 50 - 30 = 90 \text{ distinct people}").scale(1.1).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("That minus IS the addition rule").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Overlap 30, music-only 40, gaming-only 20, out 30").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): the coin has no memory ---
        self.next_band(10)
        b10_title = Tex("The coin has no memory").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Five heads in a row — tails is NOT ``due''").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{Multiply: } \tfrac{1}{2} \times \tfrac{1}{2} = \tfrac{1}{4}").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Sweets without replacement: the packet remembers").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"0{,}243 \neq 0{,}25 \Rightarrow \text{dependent}").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("Exclusive and independent: separate pockets").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.wait(4)
