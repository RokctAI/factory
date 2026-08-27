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
# band time apportioned to subtopics.json (220/230/240/240/190/200/200 of 1520 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LimitsAndFirstPrinciplesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the idea of a limit
        title = Tex("Limits and First Principles").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"\frac{x^2 - 9}{x - 3} \text{ at } x = 3: \;\; \frac{0}{0}").scale(1.05).shift(UP * 0.8)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = MathTex(r"x = 2{,}9 \to 5{,}9 \qquad x = 2{,}99 \to 5{,}99").scale(1.0).shift(DOWN * 0.3)
        d3 = MathTex(r"x = 3{,}01 \to 6{,}01").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(d2))
        self.wait(2)
        self.play(Write(d3))
        self.wait(2)
        d4 = MathTex(r"\lim_{x \to 3} \frac{x^2 - 9}{x - 3} = 6").scale(1.15).shift(DOWN * 2.4)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): factorise and cancel
        self.next_band(1)
        b1_title = Tex("Why 6? Factorise and cancel").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\frac{(x - 3)(x + 3)}{x - 3} = x + 3 \;\; (x \neq 3)").scale(1.05).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex(r"The line $y = x + 3$ with one open dot at $(3; 6)$").scale(1.0).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"\lim_{x \to 2} \frac{x^2 - 4}{x - 2} = \lim_{x \to 2}(x + 2) = 4").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("The function never EQUALS 6 there — the limit is 6").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): average gradient and the shrinking interval
        self.next_band(2)
        b2_title = Tex(r"Average gradient on $f(x) = x^2$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"x = 1 \text{ to } 3: \quad \frac{9 - 1}{3 - 1} = 4").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex("Now shrink the interval, left end fixed at 1:").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"1 \to 2: \; 3 \qquad 1 \to 1{,}5: \; 2{,}5").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"1 \to 1{,}1: \; 2{,}1 \qquad 1 \to 1{,}01: \; 2{,}01").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("The averages crowd in on 2 — a limit of gradients").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): secant pivots to tangent
        self.next_band(3)
        b3_title = Tex("Secant pivots into tangent").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        # Parabola arc as polyline with secant and tangent
        c = band_shift(3) + DOWN * 0.6
        pts = [c + LEFT * 2.4 + UP * 1.8, c + LEFT * 1.6 + UP * 0.7, c + LEFT * 0.8 + UP * 0.1,
               c + UP * 0.0, c + RIGHT * 0.8 + UP * 0.3, c + RIGHT * 1.6 + UP * 1.0,
               c + RIGHT * 2.4 + UP * 2.0]
        curve = VGroup(*[Line(pts[i], pts[i + 1], color=BLUE, stroke_width=5)
                         for i in range(len(pts) - 1)])
        self.play(Create(curve), run_time=2)
        p1 = Dot(c + LEFT * 0.8 + UP * 0.1, color=RED)
        p2 = Dot(c + RIGHT * 1.6 + UP * 1.0, color=YELLOW)
        secant = Line(c + LEFT * 1.7 + DOWN * 0.24, c + RIGHT * 2.4 + UP * 1.3, color=YELLOW, stroke_width=4)
        self.play(FadeIn(p1), FadeIn(p2), Create(secant))
        self.wait(2)
        tangent = Line(c + LEFT * 2.2 + DOWN * 0.35, c + RIGHT * 1.2 + UP * 0.75, color=GREEN, stroke_width=4)
        self.play(Create(tangent))
        self.wait(2)
        b3_l1 = Tex("Slide the second point in: the secant becomes").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        b3_l2 = Tex(r"the tangent — $y = x^2$ has gradient 2 at $x = 1$").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(3)

        # --- Band 4 (subtopic_3): the definition
        self.next_band(4)
        b4_title = Tex("The definition of the year").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Average from } x \text{ to } x + h: \; \frac{f(x+h) - f(x)}{h}").scale(1.0).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}").scale(1.2).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(3)
        b4_l3 = Tex("Let $h$ approach zero: average becomes instantaneous").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l3))
        self.wait(3)

        # --- Band 5 (subtopic_3): first principles on x squared
        self.next_band(5)
        b5_title = Tex(r"First principles on $f(x) = x^2$").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"f(x+h) = x^2 + 2xh + h^2").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"f(x+h) - f(x) = 2xh + h^2").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"\frac{2xh + h^2}{h} = 2x + h").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"f'(x) = \lim_{h \to 0}(2x + h) = 2x").scale(1.1).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = MathTex(r"\text{At } x = 1: 2, \quad x = 5: 10, \quad x = -3: -6").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_3): constant and straight line
        self.next_band(6)
        b6_title = Tex("Two more machines").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"f(x) = c: \quad \frac{c - c}{h} = 0 \;\Rightarrow\; f'(x) = 0").scale(1.05).shift(band_shift(6) + UP * 1.0)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex("A flat graph has no gradient anywhere").scale(1.0).shift(band_shift(6) + UP * 0.0)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"f(x) = ax + b: \quad \frac{ah}{h} = a \;\Rightarrow\; f'(x) = a").scale(0.95).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("The $h$ ALWAYS cancels — if not, hunt the slip").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): a x squared plus b
        self.next_band(7)
        b7_title = Tex(r"First principles on $f(x) = ax^2 + b$").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"f(x+h) - f(x) = a(2xh + h^2)").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"\frac{a(2xh + h^2)}{h} = 2ax + ah").scale(1.05).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"f'(x) = 2ax").scale(1.1).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("Added constants die; multiplied constants survive").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = MathTex(r"f(x) = 3x^2 \;\Rightarrow\; f'(x) = 6x").scale(1.05).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_4): one over x, and the notations
        self.next_band(8)
        b8_title = Tex(r"First principles on $f(x) = \dfrac{1}{x}$").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"\frac{1}{x+h} - \frac{1}{x} = \frac{x - (x+h)}{x(x+h)} = \frac{-h}{x(x+h)}").scale(0.9).shift(band_shift(8) + UP * 1.0)
        self.play(Write(b8_l1))
        self.wait(3)
        b8_l2 = MathTex(r"\div h: \quad \frac{-1}{x(x+h)} \;\to\; \frac{-1}{x^2}").scale(1.05).shift(band_shift(8) + DOWN * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"f'(x) = -\frac{1}{x^2}").scale(1.1).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = MathTex(r"f'(x), \quad \frac{dy}{dx}, \quad \frac{d}{dx}[\ldots], \quad D_x y").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Four notations, one machine").scale(1.0).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the pothole in the graph
        self.next_band(9)
        b9_title = Tex("The pothole in the graph").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"At exactly $x = 3$ the function gives up: $\tfrac{0}{0}$").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("But every neighbour points at the same value: 6").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("The limit is what belongs in the hole").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Routine: substitute; on $\\tfrac{0}{0}$, factorise,").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = Tex("cancel the shared factor, substitute again").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): the speedometer question
        self.next_band(10)
        b10_title = Tex("The speedometer question").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("160 km in 2 hours: average 80 km/h —").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("but what did the speedometer read RIGHT NOW?").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Shrink the stopwatch window: minute, second, tenth").scale(0.95).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("The averages home in — that limit IS the reading").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = MathTex(r"\text{On } y = x^2 \text{ at } x = 1: \; 3;\, 2{,}5;\, 2{,}1;\, 2{,}01 \to 2").scale(0.95).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): the recipe called first principles
        self.next_band(11)
        b11_title = Tex("The recipe called first principles").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"1. Write $f(x+h)$ \quad 2. Subtract $f(x)$").scale(1.0).shift(band_shift(11) + UP * 1.1)
        b11_l2 = Tex(r"3. Divide by $h$, cancel it \quad 4. Let $h = 0$").scale(1.0).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11_l1))
        self.wait(2)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = MathTex(r"x^2: \; 2xh + h^2 \to 2x + h \to 2x").scale(1.05).shift(band_shift(11) + DOWN * 0.7)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2.5)
        b11_l4 = Tex("A formula, not a number — every point at once").scale(1.0).shift(band_shift(11) + DOWN * 1.7)
        self.play(Write(b11_l4))
        self.wait(2)
        b11_l5 = Tex("The $h$ must cancel; if it refuses, hunt the slip").scale(1.0).shift(band_shift(11) + DOWN * 2.6)
        self.play(Write(b11_l5))
        self.wait(4)
