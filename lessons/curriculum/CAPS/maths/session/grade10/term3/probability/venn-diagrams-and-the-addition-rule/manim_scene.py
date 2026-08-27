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
# and nothing is ever removed. Venn diagrams are drawn from Rectangle +
# Circle + Tex only (exporter-safe primitives). Covers all seven subtopics
# of the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell times
# roughly proportional to subtopics.json (170/180/160/180/170/160/160 of 1180 s).

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def strike(m):
    """Diagonal cancellation stroke through a term, teacher-style."""
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VennAdditionRuleSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the survey and the four regions
        title = Tex("Venn Diagrams and the Addition Rule").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"40 learners: 22 play soccer, 15 play chess, 9 play BOTH").scale(1.0).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"Rectangle $= S$, all 40; two overlapping circles").scale(1.0).shift(UP * 0.2)
        b0_l3 = Tex(r"Four regions: both, soccer-only, chess-only, neither").scale(1.0).shift(DOWN * 0.7)
        self.play(Write(b0_l2))
        self.wait(2.5)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex(r"The filling rule: START WITH THE OVERLAP").scale(1.1).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): filling the diagram
        self.next_band(1)
        b1_title = Tex("Overlap first, subtract outward, total to check").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        vcen = band_shift(1) + LEFT * 3.4 + DOWN * 0.4
        box = Rectangle(width=6.4, height=4.2).move_to(vcen)
        cA = Circle(radius=1.5).move_to(vcen + LEFT * 0.9)
        cB = Circle(radius=1.5).move_to(vcen + RIGHT * 0.9)
        labS = Tex("S").scale(0.8).move_to(vcen + LEFT * 2.9 + UP * 1.8)
        labA = Tex("soccer").scale(0.7).move_to(vcen + LEFT * 2.0 + UP * 1.3)
        labB = Tex("chess").scale(0.7).move_to(vcen + RIGHT * 2.0 + UP * 1.3)
        self.play(Create(box), Create(cA), Create(cB), Write(labS), Write(labA), Write(labB))
        self.wait(2)
        n_both = MathTex("9").scale(0.9).move_to(vcen)
        self.play(Write(n_both))
        self.wait(2)
        n_soc = MathTex("13").scale(0.9).move_to(vcen + LEFT * 1.7)
        n_che = MathTex("6").scale(0.9).move_to(vcen + RIGHT * 1.7)
        n_nei = MathTex("12").scale(0.9).move_to(vcen + RIGHT * 2.6 + DOWN * 1.6)
        self.play(Write(n_soc))
        self.wait(1.5)
        self.play(Write(n_che))
        self.wait(1.5)
        self.play(Write(n_nei))
        self.wait(2)
        w1 = MathTex(r"22 - 9 = 13, \quad 15 - 9 = 6").scale(1.0).shift(band_shift(1) + RIGHT * 3.6 + UP * 0.5)
        w2 = MathTex(r"40 - 28 = 12 \;\text{ neither}").scale(1.0).shift(band_shift(1) + RIGHT * 3.6 + DOWN * 0.4)
        w3 = MathTex(r"13 + 9 + 6 + 12 = 40").scale(1.0).shift(band_shift(1) + RIGHT * 3.6 + DOWN * 1.3)
        self.play(Write(w1))
        self.wait(2)
        self.play(Write(w2))
        self.wait(2)
        self.play(Write(w3))
        self.play(Create(SurroundingRectangle(w3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the addition rule
        self.next_band(2)
        b2_title = Tex(r"$P(\text{soccer OR chess})$ — OR is inclusive").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_wrong = MathTex(r"\frac{22}{40} + \frac{15}{40} = \frac{37}{40} \;\text{— the 9 twice!}").scale(0.9).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2.5)
        b2_rule = MathTex(r"P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)").scale(1.05).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_rule))
        self.play(Create(SurroundingRectangle(b2_rule, color=GREEN)))
        self.wait(2.5)
        b2_l1 = MathTex(r"\frac{22}{40} + \frac{15}{40} - \frac{9}{40} = \frac{28}{40} = \frac{7}{10}").scale(0.9).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex(r"Verify by regions: $13 + 9 + 6 = 28$ — rule and map agree").scale(0.95).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l2))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the rule in reverse
        self.next_band(3)
        b3_title = Tex("The rule runs backwards too").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"P(A) = 0{,}45, \;\; P(B) = 0{,}3, \;\; P(A \text{ or } B) = 0{,}6").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"0{,}6 = 0{,}45 + 0{,}3 - P(A \text{ and } B)").scale(1.1).shift(band_shift(3) + UP * 0.1)
        b3_l3 = MathTex(r"P(A \text{ and } B) = 0{,}75 - 0{,}6 = 0{,}15").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"Any missing piece follows from the other three").scale(0.9).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): mutually exclusive events
        self.next_band(4)
        b4_title = Tex("Mutually exclusive — no shared outcome").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{less than } 3: \{1, 2\} \quad \text{at least } 5: \{5, 6\}").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        cL = Circle(radius=0.9).move_to(band_shift(4) + LEFT * 1.6 + UP * 0.0)
        cR = Circle(radius=0.9).move_to(band_shift(4) + RIGHT * 1.6 + UP * 0.0)
        self.play(Create(cL), Create(cR))
        self.wait(1.5)
        b4_l2 = Tex(r"Circles drawn apart — no lens, nothing to double-count").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"P(A \text{ and } B) = 0: \;\; P(A \text{ or } B) = P(A) + P(B)").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        b4_l4 = MathTex(r"\tfrac{2}{6} + \tfrac{2}{6} = \tfrac{2}{3} \;\text{— declare why!}").scale(0.9).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): complementary vs exclusive
        self.next_band(5)
        b5_title = Tex("Complementary: exclusive AND exhaustive").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"Mutually exclusive says only: no overlap").scale(1.05).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Complementary: no overlap AND nothing left outside").scale(1.05).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"P(A) + P(\text{not } A) = 1").scale(1.15).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex(r"$\{1,2\}$ and $\{5,6\}$: exclusive, NOT complementary").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        b5_l5 = Tex(r"— the 3s and 4s belong to neither").scale(1.0).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): full machinery on the survey
        self.next_band(6)
        b6_title = Tex("Full machinery on the survey").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"P(\text{neither}) = \frac{12}{40} = \frac{3}{10}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"1 - \tfrac{7}{10} = \tfrac{3}{10} \;\text{— two roads agree}").scale(0.9).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"P(\text{exactly one}) = \frac{13 + 6}{40} = \frac{19}{40}").scale(1.05).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex(r"``exactly one'' excludes the lens; ``at least one'' includes it").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        b6_l5 = MathTex(r"\text{Excl: } 0{,}4 + 0{,}35 = 0{,}75; \;\; P(\text{neither}) = 0{,}25").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l4))
        self.wait(2.5)
        self.play(Write(b6_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): two hoops on the playground
        self.next_band(7)
        b7_title = Tex("Two hoops chalked on the playground").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        vcen7 = band_shift(7) + LEFT * 3.4 + DOWN * 0.4
        box7 = Rectangle(width=6.4, height=4.2).move_to(vcen7)
        h1 = Circle(radius=1.5).move_to(vcen7 + LEFT * 0.9)
        h2 = Circle(radius=1.5).move_to(vcen7 + RIGHT * 0.9)
        self.play(Create(box7), Create(h1), Create(h2))
        self.wait(2)
        p_both = MathTex("9").scale(0.9).move_to(vcen7)
        p_soc = MathTex("13").scale(0.9).move_to(vcen7 + LEFT * 1.7)
        p_che = MathTex("6").scale(0.9).move_to(vcen7 + RIGHT * 1.7)
        p_nei = MathTex("12").scale(0.9).move_to(vcen7 + RIGHT * 2.6 + DOWN * 1.6)
        self.play(Write(p_both))
        self.wait(1.5)
        self.play(Write(p_soc), Write(p_che))
        self.wait(1.5)
        self.play(Write(p_nei))
        self.wait(2)
        b7_l1 = Tex(r"Both-players walk to the lens FIRST").scale(0.95).shift(band_shift(7) + RIGHT * 3.6 + UP * 0.7)
        b7_l2 = Tex(r"They hide inside both team counts").scale(0.95).shift(band_shift(7) + RIGHT * 3.6 + DOWN * 0.2)
        b7_l3 = MathTex(r"13 + 9 + 6 + 12 = 40").scale(1.0).shift(band_shift(7) + RIGHT * 3.6 + DOWN * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): why we subtract the overlap
        self.next_band(8)
        b8_title = Tex("Why we subtract: the two clipboards").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"22 + 15 = 37 \;\;\text{names — but only 28 stand in hoops}").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"The 9 in the lens are on BOTH clipboards").scale(1.05).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex(r"Adding registers counts memberships, not people").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"37 - 9 = 28 \;\Rightarrow\; \frac{28}{40} = \frac{7}{10}").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex(r"An answer past 1 means an overlap was double-counted").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): never together, and covering everything
        self.next_band(9)
        b9_title = Tex("Hoops apart, and hoops that cover everything").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Hoops pulled apart: mutually exclusive — no ``both''").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"\tfrac{2}{6} + \tfrac{2}{6} = \tfrac{2}{3} \;\text{— overlap is nought}").scale(0.85).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"Complementary: empty grass — a perfect two-way split").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = MathTex(r"P(\text{not } A) = 1 - P(A)").scale(1.1).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex(r"Outside-grass test: leftovers mean NOT complementary").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(4)
