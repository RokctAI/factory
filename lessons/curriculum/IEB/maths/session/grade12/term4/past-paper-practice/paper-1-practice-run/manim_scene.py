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

# Band-layout whiteboard scene: sequential vertical bands, one per teaching
# beat, camera moves down between bands, add-only lifecycle. Exporter-safe
# mobjects only. This practice-run session has seven question subtopics
# (Q1-Q7, no simplifier part in script.md); each question gets its own
# band(s), worked line by line with the mark-earning steps on the board.
# Band time apportioned to subtopics.json
# (280/200/220/220/220/260/220 of 1620 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Paper1PracticeRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(16)

        # --- Band 0 (Q1): 1.1 read the roots; 1.2 the formula
        title = Tex("Practice Paper Run — Question 1").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        q1a = MathTex(r"1.1: \; x(x + 3) = 0").scale(1.1).shift(UP * 1.0)
        q1a_ans = MathTex(r"x = 0 \;\text{ or }\; x = -3 \quad (2)").scale(1.1).shift(UP * 0.1)
        self.play(Write(q1a))
        self.wait(2)
        self.play(Write(q1a_ans))
        self.wait(2)
        q1b = MathTex(r"1.2: \; 2x^2 - 7x + 2 = 0").scale(1.1).shift(DOWN * 0.9)
        q1b_l1 = MathTex(r"x = \frac{7 \pm \sqrt{49 - 16}}{4} = \frac{7 \pm \sqrt{33}}{4}").scale(1.05).shift(DOWN * 1.9)
        q1b_l2 = MathTex(r"x = 3{,}19 \;\text{ or }\; x = 0{,}31 \quad (4)").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(q1b))
        self.wait(2)
        self.play(Write(q1b_l1))
        self.wait(2.5)
        self.play(Write(q1b_l2))
        self.play(Create(SurroundingRectangle(q1b_l2, color=GREEN)))
        self.wait(3)

        # --- Band 1 (Q1): 1.3 inequality; 1.4 the surd equation
        self.next_band(1)
        b1_t = MathTex(r"1.3: \; (x+5)(x-3) \le 0").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex(r"Roots $-5$ and $3$; parabola opens up; negative between").scale(0.9).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"-5 \le x \le 3 \quad (3)").scale(1.1).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = MathTex(r"1.4: \; \sqrt{2x+7} = x + 2").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = MathTex(r"2x + 7 = x^2 + 4x + 4 \;\Rightarrow\; x^2 + 2x - 3 = 0").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        b1_l5 = MathTex(r"(x+3)(x-1) = 0: \; x = 1 \; \checkmark, \; x = -3 \text{ out}").scale(0.9).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2.5)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (Q1): 1.5 simultaneous equations
        self.next_band(2)
        b2_t = MathTex(r"1.5: \; y = x - 3 \;\text{ and }\; x^2 + y^2 = 29").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = MathTex(r"x^2 + (x-3)^2 = 29").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"2x^2 - 6x - 20 = 0 \;\Rightarrow\; x^2 - 3x - 10 = 0").scale(1.05).shift(band_shift(2) + UP * 0.1)
        b2_l3 = MathTex(r"(x-5)(x+2) = 0").scale(1.1).shift(band_shift(2) + DOWN * 0.9)
        b2_l4 = MathTex(r"(5;\,2) \;\text{ or }\; (-2;\,-5) \quad (6)").scale(1.1).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        b2_l5 = Tex("Unpaired answers forfeit the marks").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (Q2): the quadratic pattern — build Tn
        self.next_band(3)
        b3_t = MathTex(r"\text{Q2: } 5; \; 12; \; 21; \; 32; \; \ldots").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = MathTex(r"\text{1st diff: } 7, 9, 11; \;\; \text{2nd diff: } 2").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"\text{Next term: } 32 + 13 = 45 \quad (1)").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"2a = 2 \Rightarrow a = 1; \; 3a + b = 7 \Rightarrow b = 4").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = MathTex(r"a + b + c = 5 \Rightarrow c = 0").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = MathTex(r"T_n = n^2 + 4n \quad (4)").scale(1.1).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l3))
        self.wait(2.5)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (Q2): which term equals 140
        self.next_band(4)
        b4_t = MathTex(r"\text{2.3: which term equals } 140?").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = MathTex(r"n^2 + 4n - 140 = 0").scale(1.1).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"(n + 14)(n - 10) = 0").scale(1.1).shift(band_shift(4) + UP * 0.1)
        b4_l3 = MathTex(r"n = 10; \;\; n = -14 \text{ rejected}").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        b4_l4 = Tex("Term numbers are natural numbers — say so").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (Q3): sum to infinity
        self.next_band(5)
        b5_t = MathTex(r"\text{Q3: } 81 + 27 + 9 + \ldots").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = MathTex(r"a = 81, \;\; r = \frac{1}{3}").scale(1.1).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"-1 < r < 1 \;\Rightarrow\; \text{the sum converges}").scale(1.0).shift(band_shift(5) + UP * 0.1)
        b5_l3 = MathTex(r"S_\infty = \frac{81}{1 - \tfrac{1}{3}} = 121{,}5 \quad (3)").scale(1.05).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(3)

        # --- Band 6 (Q3): the inequality and the sigma sum
        self.next_band(6)
        b6_t = MathTex(r"\text{3.2: smallest } n \text{ with } S_n > 121").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = MathTex(r"121{,}5\left(1 - (\tfrac{1}{3})^n\right) > 121").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"(\tfrac{1}{3})^n < (\tfrac{1}{3})^5 \Rightarrow n = 6").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"\text{3.3: } \sum_{k=1}^{30}(4k + 1): \; 5, 9, \ldots, 121").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        b6_l4 = MathTex(r"S_{30} = \tfrac{30}{2}\left[2(5) + 29(4)\right] = 15 \times 126 = 1890").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (Q4): hyperbola — asymptotes and intercepts
        self.next_band(7)
        b7_t = MathTex(r"\text{Q4: } f(x) = \frac{3}{x+2} - 1").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Asymptotes: } x = -2, \;\; y = -1 \quad (2)").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"y\text{-int: } \frac{3}{2} - 1 = \frac{1}{2}").scale(1.05).shift(band_shift(7) + UP * 0.1)
        b7_l3 = MathTex(r"x\text{-int: } \frac{3}{x+2} = 1 \Rightarrow x = 1").scale(1.05).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # --- Band 8 (Q4): sketch + the inverse of 5^x
        self.next_band(8)
        b8_t = Tex("4.3: the sketch inherits everything").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        o = band_shift(8) + DOWN * 0.2
        xax = Arrow(o + LEFT * 3.0, o + RIGHT * 3.0, buff=0, stroke_width=3)
        yax = Arrow(o + DOWN * 1.9, o + UP * 1.9, buff=0, stroke_width=3)
        va = Line(o + LEFT * 1.0 + DOWN * 1.8, o + LEFT * 1.0 + UP * 1.8, color=BLUE, stroke_width=2)
        ha = Line(o + LEFT * 2.8 + DOWN * 0.5, o + RIGHT * 2.8 + DOWN * 0.5, color=BLUE, stroke_width=2)
        self.play(Create(xax), Create(yax))
        self.play(Create(va), Create(ha))
        self.wait(1.5)
        # right branch: from just right of x=-2 (high) descending toward y=-1
        rb1 = Line(o + LEFT * 0.85 + UP * 1.7, o + LEFT * 0.5 + UP * 0.9, color=YELLOW)
        rb2 = Line(o + LEFT * 0.5 + UP * 0.9, o + RIGHT * 0.0 + UP * 0.25, color=YELLOW)
        rb3 = Line(o + RIGHT * 0.0 + UP * 0.25, o + RIGHT * 0.9 + DOWN * 0.0, color=YELLOW)
        rb4 = Line(o + RIGHT * 0.9 + DOWN * 0.0, o + RIGHT * 2.8 + DOWN * 0.35, color=YELLOW)
        # left branch: below the horizontal asymptote, diving at the vertical
        lb1 = Line(o + LEFT * 2.8 + DOWN * 0.7, o + LEFT * 1.7 + DOWN * 0.95, color=YELLOW)
        lb2 = Line(o + LEFT * 1.7 + DOWN * 0.95, o + LEFT * 1.15 + DOWN * 1.75, color=YELLOW)
        self.play(Create(rb1), Create(rb2), Create(rb3), Create(rb4))
        self.play(Create(lb1), Create(lb2))
        d1 = Dot(o + RIGHT * 0.0 + UP * 0.25, radius=0.06, color=RED)
        d2 = Dot(o + RIGHT * 0.5 + UP * 0.0, radius=0.06, color=RED)
        self.play(Create(d1), Create(d2))
        self.wait(2)
        b8_l1 = MathTex(r"4.4: \; g(x) = 5^x \Rightarrow g^{-1}: y = \log_5 x").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        b8_l2 = MathTex(r"(3;\,125) \text{ on } g \;\Rightarrow\; (125;\,3) \text{ on } g^{-1}").scale(1.0).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(3)

        # --- Band 9 (Q5): effective rate
        self.next_band(9)
        b9_t = Tex(r"Q5.1: nominal 9\% monthly $\to$ effective").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"1 + i_{\text{eff}} = \left(1 + \tfrac{0{,}09}{12}\right)^{12}").scale(1.1).shift(band_shift(9) + UP * 1.0)
        b9_l2 = MathTex(r"1{,}0075^{12} = 1{,}0938").scale(1.1).shift(band_shift(9) + UP * 0.0)
        b9_l3 = MathTex(r"i_{\text{eff}} = 9{,}38\% \quad (3)").scale(1.1).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)

        # --- Band 10 (Q5): the R750 000 loan
        self.next_band(10)
        b10_t = Tex(r"Q5.2: R750\,000, 300 months, 9,6\% monthly").scale(1.0).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = MathTex(r"i = \tfrac{0{,}096}{12} = 0{,}008, \quad n = 300").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"750\,000 = \frac{x\left[1 - (1{,}008)^{-300}\right]}{0{,}008}").scale(1.0).shift(band_shift(10) + UP * 0.0)
        b10_l3 = MathTex(r"x = \text{R}6\,604{,}94 \quad (4)").scale(1.1).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = MathTex(r"\text{Total: } 300x \approx \text{R}1\,981\,500").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        b10_l5 = MathTex(r"\text{Interest} \approx \text{R}1{,}23\text{m} > \text{the loan}").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (Q6): first principles
        self.next_band(11)
        b11_t = MathTex(r"\text{Q6.1: } f(x) = 2x^2 + 3 \text{ from first principles}").scale(1.0).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}").scale(1.05).shift(band_shift(11) + UP * 1.1)
        b11_l2 = MathTex(r"f(x+h) = 2x^2 + 4xh + 2h^2 + 3").scale(1.0).shift(band_shift(11) + UP * 0.1)
        b11_l3 = MathTex(r"\frac{4xh + 2h^2}{h} = 4x + 2h").scale(1.05).shift(band_shift(11) + DOWN * 0.9)
        b11_l4 = MathTex(r"f'(x) = \lim_{h \to 0}(4x + 2h) = 4x \quad (5)").scale(1.05).shift(band_shift(11) + DOWN * 2.0)
        self.play(Write(b11_l1))
        self.wait(2.5)
        self.play(Write(b11_l2))
        self.wait(2.5)
        self.play(Write(b11_l3))
        self.wait(2.5)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        b11_l5 = Tex("The limit symbol must survive to the last line").scale(0.95).shift(band_shift(11) + DOWN * 3.0)
        self.play(Write(b11_l5))
        self.wait(3)

        # --- Band 12 (Q6): the rules question is a rewriting question
        self.next_band(12)
        b12_t = MathTex(r"\text{Q6.2: } y = 5x^4 + \sqrt{x} - \frac{3}{x^2}").scale(1.05).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_t))
        self.wait(2)
        b12_l1 = MathTex(r"y = 5x^4 + x^{\frac{1}{2}} - 3x^{-2}").scale(1.1).shift(band_shift(12) + UP * 1.0)
        b12_l2 = MathTex(r"\frac{dy}{dx} = 20x^3 + \tfrac{1}{2}x^{-\frac{1}{2}} + 6x^{-3}").scale(1.05).shift(band_shift(12) + DOWN * 0.2)
        self.play(Write(b12_l1))
        self.wait(2.5)
        self.play(Write(b12_l2))
        self.play(Create(SurroundingRectangle(b12_l2, color=GREEN)))
        b12_l3 = Tex("Rewrite first — the marks follow the powers").scale(1.0).shift(band_shift(12) + DOWN * 1.4)
        self.play(Write(b12_l3))
        self.wait(3)

        # --- Band 13 (Q6): the cubic's full anatomy
        self.next_band(13)
        b13_t = MathTex(r"\text{Q6.3: } f(x) = x^3 - 12x + 16").scale(1.05).shift(band_shift(13) + UP * 2.2)
        self.play(Write(b13_t))
        self.wait(2)
        b13_l1 = MathTex(r"f(x) = (x - 2)^2(x + 4): \;\; x\text{-ints } 2 \text{ and } -4").scale(1.0).shift(band_shift(13) + UP * 1.1)
        b13_l2 = MathTex(r"f'(x) = 3x^2 - 12 = 0 \;\Rightarrow\; x = \pm 2").scale(1.0).shift(band_shift(13) + UP * 0.1)
        b13_l3 = MathTex(r"(-2;\,32) \text{ local max}, \quad (2;\,0) \text{ local min}").scale(1.05).shift(band_shift(13) + DOWN * 0.9)
        self.play(Write(b13_l1))
        self.wait(2.5)
        self.play(Write(b13_l2))
        self.wait(2.5)
        self.play(Write(b13_l3))
        self.play(Create(SurroundingRectangle(b13_l3, color=GREEN)))
        self.wait(2)
        b13_l4 = Tex("Shape: rise to the max, dip to touch at 2, rise").scale(0.95).shift(band_shift(13) + DOWN * 2.0)
        self.play(Write(b13_l4))
        self.wait(3)

        # --- Band 14 (Q7): independent events
        self.next_band(14)
        b14_t = MathTex(r"\text{Q7.1: } P(A) = 0{,}3, \; P(B) = 0{,}6, \text{ independent}").scale(1.0).shift(band_shift(14) + UP * 2.2)
        self.play(Write(b14_t))
        self.wait(2)
        b14_l1 = MathTex(r"P(A \text{ and } B) = 0{,}3 \times 0{,}6 = 0{,}18").scale(1.05).shift(band_shift(14) + UP * 1.1)
        b14_l2 = MathTex(r"P(A \text{ or } B) = 0{,}3 + 0{,}6 - 0{,}18").scale(1.05).shift(band_shift(14) + UP * 0.1)
        b14_l3 = MathTex(r"P(A \text{ or } B) = 0{,}72 \quad (4)").scale(1.1).shift(band_shift(14) + DOWN * 0.9)
        self.play(Write(b14_l1))
        self.wait(2.5)
        self.play(Write(b14_l2))
        self.wait(2.5)
        self.play(Write(b14_l3))
        self.play(Create(SurroundingRectangle(b14_l3, color=GREEN)))
        self.wait(3)

        # --- Band 15 (Q7): SUCCEED arrangements and the closing count
        self.next_band(15)
        b15_t = Tex(r"Q7.2: arrangements of SUCCEED (two C's, two E's)").scale(1.0).shift(band_shift(15) + UP * 2.2)
        self.play(Write(b15_t))
        self.wait(2)
        b15_l1 = MathTex(r"\frac{7!}{2!\,2!} = \frac{5\,040}{4} = 1\,260 \quad (3)").scale(1.05).shift(band_shift(15) + UP * 1.0)
        self.play(Write(b15_l1))
        self.play(Create(SurroundingRectangle(b15_l1, color=GREEN)))
        self.wait(2.5)
        b15_l2 = MathTex(r"\text{Begins with D: } \frac{6!}{2!\,2!} = 180").scale(1.05).shift(band_shift(15) + DOWN * 0.2)
        b15_l3 = MathTex(r"P = \frac{180}{1\,260} = \frac{1}{7} \quad (2)").scale(1.05).shift(band_shift(15) + DOWN * 1.3)
        self.play(Write(b15_l2))
        self.wait(2.5)
        self.play(Write(b15_l3))
        self.play(Create(SurroundingRectangle(b15_l3, color=GREEN)))
        self.wait(2)
        b15_l4 = Tex(r"84 marks walked — every technique scales to the real thing").scale(0.9).shift(band_shift(15) + DOWN * 2.5)
        self.play(Write(b15_l4))
        self.wait(4)
