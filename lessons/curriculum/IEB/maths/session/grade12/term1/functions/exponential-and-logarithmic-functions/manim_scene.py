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

# Band-layout whiteboard scene. One band per teaching beat, camera moves down,
# nothing is ever removed. Covers all seven subtopics of the session duo:
# Part 1 — Expert (subtopics 1-4), Part 2 — Simplifier (subtopics 5-7),
# band time apportioned to subtopics.json (220/240/230/240/190/200/210 of 1530 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ExponentialLogFunctionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the exponential function
        title = Tex("Exponential and Log Functions").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"y = 3^x: \quad 3^0 = 1, \; 3^4 = 81, \; 3^{-2} = \tfrac{1}{9}").scale(1.0).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2)
        d2 = Tex("Through $(0; 1)$, outputs always positive").scale(1.05).shift(DOWN * 0.1)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"\text{Horizontal asymptote: } y = 0").scale(1.05).shift(DOWN * 1.1)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2)
        d4 = MathTex(r"b > 1 \text{ climbs}; \;\; 0 < b < 1 \text{ falls}: \; (\tfrac{1}{3})^x = 3^{-x}").scale(0.95).shift(DOWN * 2.1)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_2): the logarithm defined
        self.next_band(1)
        b1_title = Tex("The logarithm defined").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"y = \log_b x \;\iff\; x = b^y").scale(1.15).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2.5)
        b1_l2 = MathTex(r"\log_3 81 = 4, \quad \log_{10} 10\;000 = 4").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\log_3 1 = 0, \quad \log_3 \tfrac{1}{27} = -3").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"\log_3(-9) \;\text{does not exist}").scale(1.05).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.play(Create(strike(b1_l4)))
        self.wait(2)
        b1_l5 = Tex("Base positive, base $\\neq 1$, input strictly positive").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_3): the log graph
        self.next_band(2)
        b2_title = Tex(r"The graph of $y = \log_b x$").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Cuts the $x$ axis at $(1; 0)$ — every base").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"\text{Vertical asymptote: } x = 0").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = MathTex(r"\log_3: \; (3; 1), \; (9; 2), \; (81; 4)").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Domain $x > 0$, range all real $y$").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Never touch the $y$ axis — classic lost mark").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_4): solving for the exponent
        self.next_band(3)
        b3_title = Tex("Solving for the exponent").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"4 \times 3^x = 108 \;\Rightarrow\; 3^x = 27 = 3^3 \;\Rightarrow\; x = 3").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_l2 = MathTex(r"2^x = 11: \;\; x = \log_2 11 = \frac{\log 11}{\log 2} \approx 3{,}46").scale(1.0).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Estimate: } 2^3 = 8 < 11 < 16 = 2^4 \;\checkmark").scale(1.0).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Invert } y = 2^x: \; y = \log_2 x").scale(1.05).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"\text{Finance ahead: } 1{,}06^n = 3 \Rightarrow n \approx 18{,}85").scale(0.95).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): doubling on repeat
        self.next_band(4)
        b4_title = Tex("Doubling on repeat").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Views: } 1, \; 2, \; 4, \; 8, \ldots = 2^x").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("Day 0: one viewer — through $(0; 1)$").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Backwards: half, quarter, eighth — never zero").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex("Cooling tea: base one half, same shape falling").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_6): the question the log asks
        self.next_band(5)
        b5_title = Tex("The question the log asks").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("How many DAYS until 64 viewers?").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\log_2 64 = 6").scale(1.15).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = MathTex(r"\log_2 32 = 5, \quad \log_2 1 = 0, \quad \log_2 \tfrac{1}{8} = -3").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"\log_2(-9): \text{ no step count reaches it}").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(strike(b5_l4)))
        self.wait(3)

        # --- Band 6 (subtopic_7): mirror twins
        self.next_band(6)
        b6_title = Tex("Mirror twins across the diagonal").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"y = 2^x \;\leftrightarrow\; y = \log_2 x \;\text{across } y = x").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = MathTex(r"(0; 1) \mapsto (1; 0), \quad (6; 64) \mapsto (64; 6)").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Floor $y = 0$ tips up into wall $x = 0$").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"\text{Sketch anchors: } (1; 0), \; (2; 1), \; (16; 4)").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Stay strictly right of the wall").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.wait(4)
