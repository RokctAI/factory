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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects (text/line/rect/dot/circle); every line of working is a
# single-string MathTex revealed with Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (240/240/240/240/185/185/170 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GeometryProbabilityEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the family tree and the minimum test
        title = Tex("Geometry and Probability Essentials").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Parallelogram: opp.\ sides $\parallel$ and $=$,").scale(1.0).shift(UP * 1.0)
        b0_l2 = Tex(r"opp.\ angles $=$, diagonals bisect").scale(1.0).shift(UP * 0.3)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Rectangle adds right angles; rhombus adds").scale(1.0).shift(DOWN * 0.6)
        b0_l4 = Tex(r"equal sides; the square inherits BOTH").scale(1.0).shift(DOWN * 1.3)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex(r"Prove the cheapest property — the tree pays the rest").scale(0.95).shift(DOWN * 2.3)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the midpoint theorem
        self.next_band(1)
        b1_title = Tex("The midpoint theorem").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        ta = Line(LEFT * 2.6 + DOWN * 1.2, RIGHT * 2.2 + DOWN * 1.2).shift(band_shift(1))
        tb = Line(LEFT * 2.6 + DOWN * 1.2, UP * 0.9 + LEFT * 0.4).shift(band_shift(1))
        tc = Line(RIGHT * 2.2 + DOWN * 1.2, UP * 0.9 + LEFT * 0.4).shift(band_shift(1))
        self.play(Create(ta), Create(tb), Create(tc))
        m1 = Dot(LEFT * 1.5 + DOWN * 0.15).shift(band_shift(1))
        m2 = Dot(RIGHT * 0.9 + DOWN * 0.15).shift(band_shift(1))
        mid = Line(LEFT * 1.5 + DOWN * 0.15, RIGHT * 0.9 + DOWN * 0.15, color=YELLOW).shift(band_shift(1))
        self.play(FadeIn(m1), FadeIn(m2))
        self.play(Create(mid))
        self.wait(2)
        b1_l1 = Tex(r"Midpoint segment $\parallel$ third side,").scale(1.05).shift(band_shift(1) + DOWN * 1.9)
        b1_l2 = Tex(r"and exactly HALF of it: 12 becomes 6").scale(1.05).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three coordinate formulas
        self.next_band(2)
        b2_title = Tex(r"A$(1; 2)$ and B$(7; 10)$: three questions").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"AB = \sqrt{6^2 + 8^2} = \sqrt{100} = 10").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"M = \left(\tfrac{1+7}{2}; \tfrac{2+10}{2}\right) = (4; 6)").scale(1.05).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"m = \frac{10 - 2}{7 - 1} = \frac{8}{6} = \frac{4}{3}").scale(1.05).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex(r"Distance is Pythagoras in coordinate clothing").scale(0.95).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): parallel, perpendicular, and the proof
        self.next_band(3)
        b3_l1 = Tex(r"Parallel: equal gradients").scale(1.1).shift(band_shift(3) + UP * 2.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\text{Perpendicular: } m_1 \times m_2 = -1").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\tfrac{4}{3} \; \to \; -\tfrac{3}{4} \quad \text{(flip and negate)}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"Prove a parallelogram on the grid:").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l4))
        self.wait(1.5)
        b3_l5 = Tex(r"midpoint of each diagonal — if they coincide,").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        b3_l6 = Tex(r"the diagonals bisect: parallelogram certified").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): probability and the Venn count
        self.next_band(4)
        b4_title = Tex(r"Probability: favourable over total").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"P(\text{six}) = \tfrac{1}{6} \approx 0{,}17 \; \text{(theory)}").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex(r"Class of 40: 25 maths, 18 science, 10 both").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_wrong = MathTex(r"25 + 18 = 43 \text{ learners}").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l3 = MathTex(r"25 + 18 - 10 = 33, \; \text{so 7 take neither}").scale(1.05).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex(r"Venn rule: fill the overlap FIRST").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the addition rule and the special cases
        self.next_band(5)
        b5_l1 = MathTex(r"P(A \text{ or } B) = P(A) + P(B) - P(A \text{ and } B)").scale(1.0).shift(band_shift(5) + UP * 2.0)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(3)
        b5_l2 = Tex(r"Subtract the overlap once — addition counted it twice").scale(0.95).shift(band_shift(5) + UP * 0.9)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Mutually exclusive: overlap zero, plain addition").scale(1.0).shift(band_shift(5) + DOWN * 0.1)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"\text{Complementary: } P(\text{not } A) = 1 - P(A)").scale(1.05).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = MathTex(r"P(\text{rain}) = 0{,}3 \Rightarrow P(\text{no rain}) = 0{,}7").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): centre and spread
        self.next_band(6)
        b6_title = MathTex(r"5; 7; 8; 10; 12; 15; 20").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Mean} = \tfrac{77}{7} = 11 \qquad \text{Median} = 10").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex(r"No mode — a legitimate answer").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"Q_1 = 7 \; \text{(of } 5; 7; 8\text{)} \qquad Q_3 = 15").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"IQR = 15 - 7 = 8").scale(1.1).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex(r"The median shrugs at outliers; the mean is dragged").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the box plot
        self.next_band(7)
        b7_title = Tex(r"Five numbers: $5, \; 7, \; 10, \; 15, \; 20$").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        # box plot: values 5..20 mapped to x in [-3, 3]
        w1 = Line(LEFT * 3.0 + UP * 0.5, LEFT * 2.2 + UP * 0.5).shift(band_shift(7))
        box = Rectangle(width=3.2, height=1.0).shift(band_shift(7) + LEFT * 0.6 + UP * 0.5)
        med = Line(LEFT * 1.0 + UP * 1.0, LEFT * 1.0 + UP * 0.0).shift(band_shift(7))
        w2 = Line(RIGHT * 1.0 + UP * 0.5, RIGHT * 3.0 + UP * 0.5).shift(band_shift(7))
        self.play(Create(w1))
        self.play(Create(box))
        self.play(Create(med))
        self.play(Create(w2))
        lbl5 = MathTex(r"5").scale(0.8).shift(band_shift(7) + LEFT * 3.0 + DOWN * 0.4)
        lbl7 = MathTex(r"7").scale(0.8).shift(band_shift(7) + LEFT * 2.2 + DOWN * 0.4)
        lbl10 = MathTex(r"10").scale(0.8).shift(band_shift(7) + LEFT * 1.0 + DOWN * 0.4)
        lbl15 = MathTex(r"15").scale(0.8).shift(band_shift(7) + RIGHT * 1.0 + DOWN * 0.4)
        lbl20 = MathTex(r"20").scale(0.8).shift(band_shift(7) + RIGHT * 3.0 + DOWN * 0.4)
        self.play(Write(lbl5), Write(lbl7), Write(lbl10), Write(lbl15), Write(lbl20))
        self.wait(2.5)
        b7_l1 = Tex(r"Long right whisker, mean 11 above median 10:").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        b7_l2 = Tex(r"the data leans right").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Quartiles from an UNORDERED list are wrong").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the family tree as inheritance
        self.next_band(8)
        b8_title = Tex("The quadrilateral family tree").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Every child keeps the family traits, adds one").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"Downwards: recite inherited properties free").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Upwards: pay only the ticket price —").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex(r"diagonals bisect $\to$ parallelogram;").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex(r"one right angle $\to$ rectangle").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)
        b8_l6 = Tex(r"``Midpoint'' twice? The theorem is the door").scale(0.95).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l6))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): chance as counting made fair
        self.next_band(9)
        b9_title = Tex("Chance as counting made fair").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Ways it can happen, over everything possible").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"More trials: experiment leans towards theory").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"25 + 18 - 10 = 33 \; \text{(overlap once)}").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex(r"No overlap possible: add cleanly.").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = Tex(r"Opposites: outside $= 1 -$ inside").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): data stories and the final sweep
        self.next_band(10)
        b10_title = Tex("Data stories and the final sweep").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Mean listens to everyone — one millionaire lies;").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"the median is the honest centre for skewed data").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(3)
        b10_l3 = Tex(r"ORDER first, then median, quartiles, box").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Check totals: Venn regions sum to the class;").scale(0.95).shift(band_shift(10) + DOWN * 1.4)
        b10_l5 = Tex(r"five numbers increase; midpoints sit between").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex(r"Every picture checks itself — for free").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
