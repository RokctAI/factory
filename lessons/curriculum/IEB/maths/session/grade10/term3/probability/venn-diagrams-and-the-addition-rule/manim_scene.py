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

# Band-layout whiteboard scene. One band per teaching beat; the camera moves
# down to clean space and nothing is ever removed. Covers all seven subtopics
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
        title = Tex("Two Events in One Picture").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"50 learners: 24 netball, 18 tennis, 10 BOTH").scale(1.0).shift(UP * 1.4)
        self.play(Write(b0_l1))
        self.wait(2)
        rect0 = Rectangle(width=8.0, height=4.2).shift(DOWN * 1.0)
        cA0 = Circle(radius=1.5).shift(DOWN * 1.0 + LEFT * 1.0)
        cB0 = Circle(radius=1.5).shift(DOWN * 1.0 + RIGHT * 1.0)
        labA0 = Tex("netball").scale(0.7).next_to(cA0, UP, buff=0.05).shift(LEFT * 1.0)
        labB0 = Tex("tennis").scale(0.7).next_to(cB0, UP, buff=0.05).shift(RIGHT * 1.0)
        labS0 = MathTex("S").scale(0.8).move_to(rect0.get_corner(UR) + 0.4 * DL)
        self.play(Create(rect0), Write(labS0))
        self.wait(1.5)
        self.play(Create(cA0), Write(labA0))
        self.play(Create(cB0), Write(labB0))
        self.wait(2)
        b0_l2 = Tex(r"Four regions: overlap, A-only, B-only, neither").scale(0.9).next_to(rect0, DOWN, buff=0.25)
        self.play(Write(b0_l2))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): filling the diagram
        self.next_band(1)
        b1_title = Tex("Fill the OVERLAP first").scale(1.2).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        rect1 = Rectangle(width=8.0, height=4.2).shift(band_shift(1) + DOWN * 0.2)
        cA1 = Circle(radius=1.5).shift(band_shift(1) + DOWN * 0.2 + LEFT * 1.0)
        cB1 = Circle(radius=1.5).shift(band_shift(1) + DOWN * 0.2 + RIGHT * 1.0)
        self.play(Create(rect1), Create(cA1), Create(cB1))
        self.wait(1.5)
        n_both = MathTex("10").scale(0.9).move_to(band_shift(1) + DOWN * 0.2)
        self.play(Write(n_both))
        self.wait(2)
        n_a = MathTex(r"24 - 10 = 14").scale(0.7).move_to(band_shift(1) + DOWN * 0.2 + LEFT * 1.8)
        n_b = MathTex(r"18 - 10 = 8").scale(0.7).move_to(band_shift(1) + DOWN * 0.2 + RIGHT * 1.8)
        self.play(Write(n_a))
        self.wait(2)
        self.play(Write(n_b))
        self.wait(2)
        n_out = MathTex(r"50 - 32 = 18").scale(0.7).move_to(band_shift(1) + DOWN * 1.9 + RIGHT * 2.6)
        self.play(Write(n_out))
        self.wait(2)
        b1_check = MathTex(r"14 + 10 + 8 + 18 = 50 \;\checkmark").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_check))
        self.play(Create(SurroundingRectangle(b1_check, color=GREEN)))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the addition rule
        self.next_band(2)
        b2_title = Tex("The addition rule").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_wrong = MathTex(r"\tfrac{24}{50} + \tfrac{18}{50} = \tfrac{42}{50} \;\text{?}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l1 = Tex(r"The 10 in the lens were counted TWICE").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_rule = MathTex(r"P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_rule))
        self.play(Create(SurroundingRectangle(b2_rule, color=GREEN)))
        self.wait(2.5)
        b2_l2 = MathTex(r"\tfrac{24}{50} + \tfrac{18}{50} - \tfrac{10}{50} = \tfrac{32}{50} = 0{,}64").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Regions agree: $14 + 10 + 8 = 32$").scale(0.95).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l3))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the rule in reverse
        self.next_band(3)
        b3_title = Tex("The rule runs backwards too").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"P(A) = 0{,}5, \; P(B) = 0{,}35, \; P(A \text{ or } B) = 0{,}7").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"0{,}7 = 0{,}5 + 0{,}35 - P(A \text{ and } B)").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"P(A \text{ and } B) = 0{,}85 - 0{,}7 = 0{,}15").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"Four variables — any three recover the fourth").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): mutually exclusive events
        self.next_band(4)
        b4_title = Tex("Mutually exclusive: never together").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        cA4 = Circle(radius=1.1).shift(band_shift(4) + UP * 0.6 + LEFT * 2.4)
        cB4 = Circle(radius=1.1).shift(band_shift(4) + UP * 0.6 + RIGHT * 2.4)
        labA4 = Tex(r"below 3").scale(0.7).move_to(cA4)
        labB4 = Tex(r"above 8").scale(0.7).move_to(cB4)
        self.play(Create(cA4), Create(cB4), Write(labA4), Write(labB4))
        self.wait(2)
        b4_l1 = Tex(r"Separated circles — no lens, nothing shared").scale(0.95).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"P(A \text{ and } B) = 0 \;\Rightarrow\; P(A \text{ or } B) = P(A) + P(B)").scale(0.9).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"\tfrac{2}{10} + \tfrac{2}{10} = \tfrac{4}{10} = \tfrac{2}{5}").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l3))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): complementary vs exclusive
        self.next_band(5)
        b5_title = Tex("Complementary $=$ exclusive AND exhaustive").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"P(A) + P(\text{not } A) = 1").scale(1.15).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = Tex(r"Exclusive: no overlap. \; Complementary: no overlap AND no leftovers").scale(0.8).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"``below 3'' and ``above 8'': exclusive, NOT complementary").scale(0.85).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex(r"— cards 3 to 8 belong to neither").scale(0.85).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): full machinery on the survey
        self.next_band(6)
        b6_title = Tex("Full machinery on the survey").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"P(\text{neither}) = \tfrac{18}{50} = 0{,}36").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{Check: } 1 - 0{,}64 = 0{,}36 \;\checkmark").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"P(\text{exactly one}) = \tfrac{14 + 8}{50} = \tfrac{22}{50}").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex(r"``exactly one'' excludes the lens; ``at least one'' includes it").scale(0.85).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): two ropes in the school hall
        self.next_band(7)
        b7_title = Tex("Two ropes in the school hall").scale(1.2).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_title))
        self.wait(2)
        rect7 = Rectangle(width=8.0, height=4.0).shift(band_shift(7) + DOWN * 0.3)
        cA7 = Circle(radius=1.4).shift(band_shift(7) + DOWN * 0.3 + LEFT * 1.0)
        cB7 = Circle(radius=1.4).shift(band_shift(7) + DOWN * 0.3 + RIGHT * 1.0)
        self.play(Create(rect7))
        self.play(Create(cA7), Create(cB7))
        self.wait(2)
        m10 = MathTex("10").scale(0.8).move_to(band_shift(7) + DOWN * 0.3)
        m14 = MathTex("14").scale(0.8).move_to(band_shift(7) + DOWN * 0.3 + LEFT * 1.8)
        m8 = MathTex("8").scale(0.8).move_to(band_shift(7) + DOWN * 0.3 + RIGHT * 1.8)
        m18 = MathTex("18").scale(0.8).move_to(band_shift(7) + DOWN * 1.9 + RIGHT * 3.0)
        self.play(Write(m10))
        self.wait(1.5)
        self.play(Write(m14), Write(m8))
        self.wait(1.5)
        self.play(Write(m18))
        self.wait(2)
        b7_l1 = Tex(r"Both-players stand in the lens FIRST — one pair of shoes, one region").scale(0.75).next_to(rect7, DOWN, buff=0.3)
        self.play(Write(b7_l1))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): why we subtract the overlap
        self.next_band(8)
        b8_title = Tex("Why we subtract the overlap").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Registers: } 24 + 18 = 42 \quad \text{Floor: } 32").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"The 10 in the lens are on BOTH registers").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex(r"Registers count memberships, not people").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"42 - 10 = 32 \;\;\checkmark").scale(1.1).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex(r"Past 1? The rule is shouting: double-counted!").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): never together, and covering everything
        self.next_band(9)
        b9_title = Tex("Never together, and covering everything").scale(1.1).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(2)
        cA9 = Circle(radius=0.9).shift(band_shift(9) + UP * 0.8 + LEFT * 2.6)
        cB9 = Circle(radius=0.9).shift(band_shift(9) + UP * 0.8 + RIGHT * 2.6)
        self.play(Create(cA9), Create(cB9))
        self.wait(1.5)
        b9_l1 = Tex(r"Rings apart: exclusive — add and stop, once justified").scale(0.9).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"Complementary: no shared floor AND no open floor").scale(0.9).shift(band_shift(9) + DOWN * 1.3)
        b9_l3 = MathTex(r"P(\text{not } A) = 1 - P(A)").scale(1.05).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex(r"Exclusive bans sharing; complementary bans sharing AND leftovers").scale(0.8).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l4))
        self.wait(4)
