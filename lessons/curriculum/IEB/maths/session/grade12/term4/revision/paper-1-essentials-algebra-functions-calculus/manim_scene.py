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
# mobjects only. Two-part revision sweep: subtopics 1-4 (Expert) work the
# core methods with fresh examples; subtopics 5-7 (Simplifier) map the
# material, the recurring shapes, and the donation list. Band dwell times
# proportional to subtopics.json (250/240/240/250/180/180/180 of 1520 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Paper1EssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(16)

        # --- Band 0 (subtopic_1): the opening solve — quadratic formula
        title = Tex("Paper One Essentials — the revision sweep").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_q = MathTex(r"5x^2 + 2x - 4 = 0 \;\; \text{(two decimal places)}").scale(1.0).shift(UP * 1.0)
        self.play(Write(b0_q))
        self.wait(2)
        b0_l1 = MathTex(r"x = \frac{-2 \pm \sqrt{4 + 80}}{10} = \frac{-2 \pm \sqrt{84}}{10}").scale(1.0).shift(UP * 0.0)
        b0_l2 = MathTex(r"x \approx 0{,}72 \;\text{ or }\; x \approx -1{,}12").scale(1.05).shift(DOWN * 1.1)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        b0_l3 = Tex("Round once — at the end").scale(0.9).shift(DOWN * 2.0)
        self.play(Write(b0_l3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the k-method
        self.next_band(1)
        b1_t = MathTex(r"2^{2x} - 12\cdot 2^x + 32 = 0").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = MathTex(r"\text{Let } k = 2^x: \;\; k^2 - 12k + 32 = 0").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"(k - 4)(k - 8) = 0").scale(1.05).shift(band_shift(1) + UP * 0.1)
        b1_l3 = MathTex(r"2^x = 4 \Rightarrow x = 2; \quad 2^x = 8 \Rightarrow x = 3").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        b1_l4 = Tex("k was never the answer — translate back").scale(0.9).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_1): surd equations demand a check
        self.next_band(2)
        b2_t = MathTex(r"\sqrt{3x + 1} = x - 3").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = MathTex(r"3x + 1 = x^2 - 6x + 9 \;\Rightarrow\; x^2 - 9x + 8 = 0").scale(0.95).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"(x - 8)(x - 1) = 0").scale(1.05).shift(band_shift(2) + UP * 0.1)
        b2_l3 = MathTex(r"x = 8: \; \sqrt{25} = 5 \; \checkmark \qquad x = 1: \; 2 \ne -2").scale(0.95).shift(band_shift(2) + DOWN * 0.9)
        b2_l4 = MathTex(r"x = 8 \text{ only}").scale(1.1).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_1): inequality picture + simultaneous pairs
        self.next_band(3)
        b3_t = MathTex(r"(x+1)(x-6) < 0").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        o3 = band_shift(3) + UP * 1.0
        ax3 = Line(o3 + LEFT * 3.0, o3 + RIGHT * 3.0, stroke_width=3)
        # upward parabola through roots -1 and 6 (mapped to -1.5 and 1.8)
        p1 = Line(o3 + LEFT * 2.4 + UP * 1.0, o3 + LEFT * 1.5, color=YELLOW)
        p2 = Line(o3 + LEFT * 1.5, o3 + RIGHT * 0.15 + DOWN * 0.8, color=YELLOW)
        p3 = Line(o3 + RIGHT * 0.15 + DOWN * 0.8, o3 + RIGHT * 1.8, color=YELLOW)
        p4 = Line(o3 + RIGHT * 1.8, o3 + RIGHT * 2.5 + UP * 1.0, color=YELLOW)
        self.play(Create(ax3))
        self.play(Create(p1), Create(p2), Create(p3), Create(p4))
        self.wait(2)
        b3_l1 = MathTex(r"-1 < x < 6 \;\; \text{(negative between the roots)}").scale(0.95).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_l2 = MathTex(r"y = 2x+1, \; xy = 10: \;\; 2x^2 + x - 10 = 0").scale(0.9).shift(band_shift(3) + DOWN * 1.4)
        b3_l3 = MathTex(r"(2x+5)(x-2)=0: \; (2;\,5) \text{ or } \left(-\tfrac{5}{2};\,-4\right)").scale(0.9).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): quadratic pattern by differences
        self.next_band(4)
        b4_t = MathTex(r"4; \; 11; \; 22; \; 37; \; \ldots").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = MathTex(r"\text{1st diff: } 7, 11, 15; \;\; \text{2nd diff: } 4 \Rightarrow a = 2").scale(0.95).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"3a + b = 7 \Rightarrow b = 1; \quad a + b + c = 4 \Rightarrow c = 1").scale(0.9).shift(band_shift(4) + UP * 0.1)
        b4_l3 = MathTex(r"T_n = 2n^2 + n + 1 \;\; \text{(check: } T_2 = 11 \checkmark)").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = MathTex(r"2n^2 + n - 171 = 0 \Rightarrow (n-9)(2n+19) = 0 \Rightarrow n = 9").scale(0.85).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_2): geometric series and the smallest n
        self.next_band(5)
        b5_t = MathTex(r"200 + 100 + 50 + \ldots: \; a = 200, \; r = \tfrac{1}{2}").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = MathTex(r"-1 < r < 1 \Rightarrow S_\infty = \frac{200}{1 - \tfrac{1}{2}} = 400").scale(1.0).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2.5)
        b5_l2 = MathTex(r"S_n > 399: \; (\tfrac{1}{2})^n < \tfrac{1}{400} \Rightarrow n = 9").scale(1.0).shift(band_shift(5) + DOWN * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\sum_{k=1}^{25}(2k+3) = \tfrac{25}{2}[10 + 48] = 725").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        b5_l4 = Tex("Count trap: $k = 4$ to $25$ is 22 terms").scale(0.9).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_3): the graph checklist on a hyperbola
        self.next_band(6)
        b6_t = MathTex(r"f(x) = \frac{4}{x+3} - 2").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Asymptotes: } x = -3, \; y = -2").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"y\text{-int: } \tfrac{4}{3} - 2 = -\tfrac{2}{3}; \quad x\text{-int: } x = -1").scale(0.95).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        b6_l3 = Tex("Shape, asymptotes, intercepts, special points — in order").scale(0.85).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.wait(3)

        # --- Band 7 (subtopic_3): inverses — reflect across y = x
        self.next_band(7)
        b7_t = MathTex(r"g(x) = 2^x \;\Rightarrow\; g^{-1}(x) = \log_2 x").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        o7 = band_shift(7) + DOWN * 0.3
        xax = Arrow(o7 + LEFT * 2.6, o7 + RIGHT * 2.6, buff=0, stroke_width=3)
        yax = Arrow(o7 + DOWN * 1.8, o7 + UP * 1.8, buff=0, stroke_width=3)
        mirror = Line(o7 + LEFT * 1.7 + DOWN * 1.7, o7 + RIGHT * 1.7 + UP * 1.7, color=BLUE, stroke_width=2)
        self.play(Create(xax), Create(yax))
        self.play(Create(mirror))
        # exponential rising curve (polyline) and its log reflection
        e1 = Line(o7 + LEFT * 2.2 + DOWN * 0.35, o7 + LEFT * 0.8 + DOWN * 0.1, color=YELLOW)
        e2 = Line(o7 + LEFT * 0.8 + DOWN * 0.1, o7 + RIGHT * 0.5 + UP * 0.7, color=YELLOW)
        e3 = Line(o7 + RIGHT * 0.5 + UP * 0.7, o7 + RIGHT * 1.2 + UP * 1.7, color=YELLOW)
        self.play(Create(e1), Create(e2), Create(e3))
        lg1 = Line(o7 + DOWN * 0.35 + LEFT * 0.1, o7 + DOWN * 0.1 + RIGHT * 0.0, color=GREEN)
        lg2 = Line(o7 + DOWN * 0.1 + RIGHT * 0.0, o7 + UP * 0.5 + RIGHT * 0.7, color=GREEN)
        lg3 = Line(o7 + UP * 0.5 + RIGHT * 0.7, o7 + UP * 1.2 + RIGHT * 1.7, color=GREEN)
        self.play(Create(lg1), Create(lg2), Create(lg3))
        d7a = Dot(o7 + LEFT * 0.0 + UP * 0.0 + RIGHT * 0.9 + UP * 1.3, radius=0.06, color=RED)
        d7b = Dot(o7 + RIGHT * 1.3 + UP * 0.9, radius=0.06, color=RED)
        self.play(Create(d7a), Create(d7b))
        self.wait(2)
        b7_l1 = MathTex(r"(3;\,8) \text{ on } g \;\Rightarrow\; (8;\,3) \text{ on } g^{-1}").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_3): finance — effective rate and the annuity
        self.next_band(8)
        b8_t = Tex(r"Finance: two skills").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = MathTex(r"7{,}2\% \text{ monthly: } 1{,}006^{12} - 1 = 7{,}44\%").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.play(Create(SurroundingRectangle(b8_l1, color=GREEN)))
        self.wait(2.5)
        b8_l2 = MathTex(r"\text{R}600\,000, \; i = 0{,}0095, \; n = 180").scale(1.0).shift(band_shift(8) + UP * 0.1)
        b8_l3 = MathTex(r"x = \frac{P\,i}{1 - (1+i)^{-n}} = \text{R}6\,971{,}10").scale(1.0).shift(band_shift(8) + DOWN * 1.0)
        b8_l4 = MathTex(r"\text{Interest} \approx \text{R}655\,000 > \text{the loan}").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_4): first principles, limit kept visible
        self.next_band(9)
        b9_t = MathTex(r"f(x) = 4x^2 + 1 \;\; \text{from first principles}").scale(1.0).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"f'(x) = \lim_{h \to 0}\frac{f(x+h) - f(x)}{h}").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"= \lim_{h \to 0}\frac{8xh + 4h^2}{h} = \lim_{h \to 0}(8x + 4h)").scale(0.95).shift(band_shift(9) + UP * 0.0)
        b9_l3 = MathTex(r"f'(x) = 8x").scale(1.1).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        b9_l4 = Tex("The limit symbol survives until it is used").scale(0.9).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_4): the rules, after rewriting
        self.next_band(10)
        b10_t = MathTex(r"y = 2x^5 - 3\sqrt{x} + \frac{4}{x^2}").scale(1.05).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = MathTex(r"y = 2x^5 - 3x^{\frac{1}{2}} + 4x^{-2}").scale(1.05).shift(band_shift(10) + UP * 1.0)
        b10_l2 = MathTex(r"\frac{dy}{dx} = 10x^4 - \tfrac{3}{2}x^{-\frac{1}{2}} - 8x^{-3}").scale(1.05).shift(band_shift(10) + DOWN * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        b10_l3 = Tex("Rewrite first — roots and fractions are powers in disguise").scale(0.85).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l3))
        self.wait(3)

        # --- Band 11 (subtopic_4): the cubic anatomised
        self.next_band(11)
        b11_t = MathTex(r"f(x) = x^3 + 3x^2 - 4 = (x-1)(x+2)^2").scale(1.0).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = MathTex(r"x\text{-ints: } 1 \text{ (cut)}, \; -2 \text{ (touch)}; \; y\text{-int } -4").scale(0.95).shift(band_shift(11) + UP * 1.1)
        b11_l2 = MathTex(r"f'(x) = 3x(x+2) = 0 \Rightarrow x = -2, \; 0").scale(0.95).shift(band_shift(11) + UP * 0.1)
        b11_l3 = MathTex(r"(-2;\,0) \text{ local max}, \; (0;\,-4) \text{ local min}, \; (-1;\,-2) \text{ inflection}").scale(0.85).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l1))
        self.wait(2.5)
        self.play(Write(b11_l2))
        self.wait(2.5)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(3)

        # --- Band 12 (subtopic_4): probability closes the part
        self.next_band(12)
        b12_t = MathTex(r"P(A) = 0{,}25, \; P(B) = 0{,}4, \; \text{independent}").scale(1.0).shift(band_shift(12) + UP * 2.2)
        self.play(Write(b12_t))
        self.wait(2)
        b12_l1 = MathTex(r"P(A \text{ and } B) = 0{,}1; \quad P(A \text{ or } B) = 0{,}55").scale(1.0).shift(band_shift(12) + UP * 1.1)
        self.play(Write(b12_l1))
        self.play(Create(SurroundingRectangle(b12_l1, color=GREEN)))
        self.wait(2.5)
        b12_l2 = MathTex(r"\text{BANANA: } \frac{6!}{3!\,2!} = 60").scale(1.05).shift(band_shift(12) + DOWN * 0.1)
        self.play(Write(b12_l2))
        self.play(Create(SurroundingRectangle(b12_l2, color=GREEN)))
        b12_l3 = Tex("Repeated letters divide — that is the whole trick").scale(0.9).shift(band_shift(12) + DOWN * 1.2)
        self.play(Write(b12_l3))
        self.wait(3)

        # --- Band 13 (subtopic_5): the map — six districts
        self.next_band(13)
        b13_t = Tex("The map: six districts, one city").scale(1.1).shift(band_shift(13) + UP * 2.2)
        self.play(Write(b13_t))
        self.wait(2)
        r1 = Rectangle(width=2.6, height=1.1, color=YELLOW).shift(band_shift(13) + LEFT * 1.6 + UP * 0.9)
        r2 = Rectangle(width=2.6, height=1.1, color=YELLOW).shift(band_shift(13) + RIGHT * 1.6 + UP * 0.9)
        r3 = Rectangle(width=1.6, height=0.8, color=BLUE).shift(band_shift(13) + LEFT * 2.2 + DOWN * 0.5)
        r4 = Rectangle(width=1.6, height=0.8, color=BLUE).shift(band_shift(13) + LEFT * 0.0 + DOWN * 0.5)
        r5 = Rectangle(width=1.6, height=0.8, color=BLUE).shift(band_shift(13) + RIGHT * 2.2 + DOWN * 0.5)
        r6 = Rectangle(width=1.6, height=0.8, color=BLUE).shift(band_shift(13) + LEFT * 0.0 + DOWN * 1.6)
        t1 = Tex("Functions").scale(0.7).move_to(r1)
        t2 = Tex("Calculus").scale(0.7).move_to(r2)
        t3 = Tex("Algebra").scale(0.55).move_to(r3)
        t4 = Tex("Patterns").scale(0.55).move_to(r4)
        t5 = Tex("Finance").scale(0.55).move_to(r5)
        t6 = Tex("Probability").scale(0.55).move_to(r6)
        self.play(Create(r1), Create(r2), Write(t1), Write(t2))
        self.wait(2)
        self.play(Create(r3), Create(r4), Create(r5), Create(r6), Write(t3), Write(t4), Write(t5), Write(t6))
        self.wait(2.5)
        b13_l1 = Tex("Lean the effort where the connections are — never camp").scale(0.85).shift(band_shift(13) + DOWN * 2.7)
        self.play(Write(b13_l1))
        self.wait(3)

        # --- Band 14 (subtopic_6): five shapes that repeat
        self.next_band(14)
        b14_t = Tex("Five shapes, five reflexes").scale(1.1).shift(band_shift(14) + UP * 2.2)
        self.play(Write(b14_t))
        self.wait(2)
        b14_l1 = Tex("1. Two decimal places $\\to$ formula").scale(0.85).shift(band_shift(14) + UP * 1.2)
        b14_l2 = Tex("2. Exponent twice $\\to$ $k$-substitution").scale(0.85).shift(band_shift(14) + UP * 0.5)
        b14_l3 = Tex("3. Pattern $\\to$ differences, then solve for $n$").scale(0.85).shift(band_shift(14) + DOWN * 0.2)
        b14_l4 = Tex("4. Graph $\\to$ the four-step checklist").scale(0.85).shift(band_shift(14) + DOWN * 0.9)
        b14_l5 = Tex("5. Cubic $\\to$ factorise, differentiate, classify").scale(0.85).shift(band_shift(14) + DOWN * 1.6)
        for m in (b14_l1, b14_l2, b14_l3, b14_l4, b14_l5):
            self.play(Write(m))
            self.wait(1.5)
        self.play(Create(SurroundingRectangle(b14_l5, color=GREEN)))
        self.wait(3)

        # --- Band 15 (subtopic_7): the donation list
        self.next_band(15)
        b15_t = Tex("The donation list — keep your marks").scale(1.1).shift(band_shift(15) + UP * 2.2)
        self.play(Write(b15_t))
        self.wait(2)
        b15_l1 = Tex("1. Early rounding").scale(0.85).shift(band_shift(15) + UP * 1.2)
        b15_l2 = Tex("2. The unchecked surd").scale(0.85).shift(band_shift(15) + UP * 0.5)
        b15_l3 = Tex("3. The missing second answer").scale(0.85).shift(band_shift(15) + DOWN * 0.2)
        b15_l4 = Tex("4. Finance without a timeline").scale(0.85).shift(band_shift(15) + DOWN * 0.9)
        b15_l5 = Tex("5. Abandoned calculus notation").scale(0.85).shift(band_shift(15) + DOWN * 1.6)
        for m in (b15_l1, b15_l2, b15_l3, b15_l4, b15_l5):
            self.play(Write(m))
            self.wait(1.5)
        b15_l6 = Tex("One check per answer — one line, every time").scale(0.9).shift(band_shift(15) + DOWN * 2.6)
        self.play(Write(b15_l6))
        self.play(Create(SurroundingRectangle(b15_l6, color=GREEN)))
        self.wait(4)
