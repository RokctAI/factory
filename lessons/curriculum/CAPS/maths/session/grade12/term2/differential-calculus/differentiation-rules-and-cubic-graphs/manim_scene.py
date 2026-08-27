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

# Band-layout whiteboard scene (see AUTHORING-SPEC / quadratics-by-factorisation
# worked example). One band per teaching beat, camera moves down, nothing is
# ever removed. Covers all seven subtopics of the session duo:
# Part 1 — Expert (subtopics 1-4), Part 2 — Simplifier (subtopics 5-7),
# band time apportioned to subtopics.json (225/225/250/240/190/200/195 of 1525 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DifferentiationRulesAndCubicGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the power rule
        title = Tex("Differentiation Rules and Cubic Graphs").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"\frac{d}{dx}\, x^n = n\,x^{\,n-1}").scale(1.2).shift(UP * 0.8)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)
        d2 = Tex("Exponent falls forward, power steps down one").scale(1.0).shift(DOWN * 0.2)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"y = 3x^4 - 2x + 5").scale(1.1).shift(DOWN * 1.2)
        self.play(Write(d3))
        self.wait(2)
        d4 = MathTex(r"\frac{dy}{dx} = 12x^3 - 2 \quad \text{(the 5 dies to 0)}").scale(1.05).shift(DOWN * 2.4)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): rewrite before differentiating
        self.next_band(1)
        b1_title = Tex("Rewrite FIRST — three disguises").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\sqrt{x} = x^{\frac{1}{2}} \;\Rightarrow\; \tfrac{1}{2}x^{-\frac{1}{2}}").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"\frac{3}{x^2} = 3x^{-2} \;\Rightarrow\; -6x^{-3}").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"\frac{2x^3 - x}{x^2} = 2x - x^{-1}").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"\Rightarrow\; 2 + x^{-2}").scale(1.05).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Down from $-2$ lands on $-3$ — more negative").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the tangent routine
        self.next_band(2)
        b2_title = Tex(r"Tangent to $f(x) = x^3 - 3x^2 + 2$ at $x = 1$").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"1.\; f(1) = 1 - 3 + 2 = 0: \text{ point } (1; 0)").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"2.\; f'(x) = 3x^2 - 6x").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"3.\; f'(1) = 3 - 6 = -3").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"4.\; y - 0 = -3(x - 1)").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = MathTex(r"y = -3x + 3").scale(1.1).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the routine reordered
        self.next_band(3)
        b3_title = Tex("Where does the tangent have gradient 9?").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"3x^2 - 6x = 9").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"x^2 - 2x - 3 = 0 \;\Rightarrow\; (x - 3)(x + 1) = 0").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"x = 3 \quad \text{or} \quad x = -1").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"Parallel to the $x$-axis $=$ gradient zero;").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        b3_l5 = Tex("parallel to a line $=$ that line's gradient").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): stationary points
        self.next_band(4)
        b4_title = Tex(r"Sketch $f(x) = x^3 - 6x^2 + 9x$: stationary points").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"f'(x) = 3x^2 - 12x + 9 = 0").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"x^2 - 4x + 3 = (x - 1)(x - 3) = 0").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"x = 1 \quad \text{or} \quad x = 3").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"f(1) = 4, \qquad f(3) = 0").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = MathTex(r"\text{Max } (1; 4), \quad \text{min } (3; 0)").scale(1.05).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): intercepts and the double root
        self.next_band(5)
        b5_title = Tex("Intercepts: factorise $f$ itself").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"f(x) = x(x^2 - 6x + 9) = x(x - 3)^2").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{Roots: } x = 0 \text{ and } x = 3 \text{ (doubled)}").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("A double root TOUCHES the axis and turns away").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"Consistent: the minimum $(3; 0)$ sits on the axis").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Stubborn cubic? Factor theorem, then divide out").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_3): the sketch
        self.next_band(6)
        b6_title = Tex("The sketch").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        c = band_shift(6) + DOWN * 0.4
        xaxis = Arrow(c + LEFT * 3.1, c + RIGHT * 3.1, buff=0, stroke_width=4)
        yaxis = Arrow(c + LEFT * 2.0 + DOWN * 2.2, c + LEFT * 2.0 + UP * 2.4, buff=0, stroke_width=4)
        self.play(Create(xaxis), Create(yaxis))
        self.wait(1)
        pts = [c + LEFT * 2.6 + DOWN * 1.6, c + LEFT * 2.0, c + LEFT * 1.5 + UP * 1.1,
               c + LEFT * 1.0 + UP * 1.5, c + LEFT * 0.3 + UP * 0.8,
               c + RIGHT * 0.4 + UP * 0.2, c + RIGHT * 1.0,
               c + RIGHT * 1.6 + UP * 0.5, c + RIGHT * 2.2 + UP * 1.6]
        curve = VGroup(*[Line(pts[i], pts[i + 1], color=BLUE, stroke_width=5)
                         for i in range(len(pts) - 1)])
        self.play(Create(curve), run_time=2.5)
        self.wait(1.5)
        peak = Dot(c + LEFT * 1.0 + UP * 1.5, color=RED)
        peak_l = MathTex(r"(1; 4)").scale(0.85).move_to(c + LEFT * 1.0 + UP * 2.05)
        valley = Dot(c + RIGHT * 1.0, color=RED)
        valley_l = MathTex(r"(3; 0)").scale(0.85).move_to(c + RIGHT * 1.3 + DOWN * 0.5)
        self.play(FadeIn(peak), Write(peak_l))
        self.play(FadeIn(valley), Write(valley_l))
        self.wait(2)
        b6_l1 = Tex("Rise, peak, dip to touch, rise forever").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l1))
        self.wait(3)

        # --- Band 7 (subtopic_4): increase and decrease
        self.next_band(7)
        b7_title = Tex(r"$f'$ narrates the graph").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"f'(x) = 3(x - 1)(x - 3)").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"f' > 0: \text{ increasing outside the roots}").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"f' < 0: \text{ decreasing between them}").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"\text{Decreasing for } 1 < x < 3").scale(1.1).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): the second derivative
        self.next_band(8)
        b8_title = Tex(r"$f''$ — the gradient of the gradient").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"f''(x) = 6x - 12 = 0 \;\Rightarrow\; x = 2").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"\text{Inflection } (2; 2) \text{ — midway between 1 and 3}").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"f''(1) = -6 < 0: \text{ concave down — maximum}").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"f''(3) = 6 > 0: \text{ concave up — minimum}").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("$f$: position, $f'$: direction, $f''$: curvature").scale(1.05).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the exponent falls forward
        self.next_band(9)
        b9_title = Tex("The exponent falls forward").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"x^2 \to 2x, \quad x^3 \to 3x^2, \quad x^{10} \to 10x^9").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Lone numbers differentiate to zero").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("The wardrobe: dress everything as a power first").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"\sqrt{x} = x^{\frac{1}{2}}, \quad \frac{1}{x^3} = x^{-3}").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = MathTex(r"\frac{2x^3 - x}{x^2} = 2x - x^{-1} \;\Rightarrow\; 2 + x^{-2}").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): the hiking trail
        self.next_band(10)
        b10_title = Tex("The hiking trail").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("The derivative is the slope under your boots").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"\text{Level ground: } f' = 0 \text{ at } x = 1 \text{ and } x = 3").scale(1.0).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{Altitudes from } f: \text{ peak } 4, \text{ valley floor } 0").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"\text{Downhill stretch: } 1 < x < 3").scale(1.05).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Midway, $x = 2$: the curve rolls over — inflection").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): laying a ruler on the curve
        self.next_band(11)
        b11_title = Tex("Laying a ruler on the curve").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Two feeds: FUNCTION for heights, DERIVATIVE for slopes").scale(0.95).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"f(1) = 0, \qquad f'(1) = -3").scale(1.05).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = MathTex(r"y = -3x + 3").scale(1.1).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2.5)
        b11_l4 = Tex(r"Slope 9? Solve $f'(x) = 9$: $x = 3$ or $-1$").scale(1.0).shift(band_shift(11) + DOWN * 1.9)
        self.play(Write(b11_l4))
        self.wait(2)
        b11_l5 = Tex("A level ruler is a turning point in a new jacket").scale(1.0).shift(band_shift(11) + DOWN * 2.8)
        self.play(Write(b11_l5))
        self.wait(4)
