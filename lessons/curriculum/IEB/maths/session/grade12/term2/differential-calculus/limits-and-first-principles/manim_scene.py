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
        d1 = MathTex(r"\frac{x^2 - 16}{x - 4} \text{ at } x = 4: \; \tfrac{0}{0}").scale(1.1).shift(UP * 0.8)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = MathTex(r"3{,}9 \to 7{,}9 \quad 3{,}99 \to 7{,}99 \quad 4{,}01 \to 8{,}01").scale(0.95).shift(DOWN * 0.2)
        self.play(Write(d2))
        self.wait(2.5)
        d3 = MathTex(r"\lim_{x \to 4} \frac{x^2 - 16}{x - 4} = 8").scale(1.1).shift(DOWN * 1.3)
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2.5)
        d4 = Tex(r"Line $y = x + 4$ with a hole at $(4; 8)$").scale(1.0).shift(DOWN * 2.3)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the technique
        self.next_band(1)
        b1_title = Tex("Substitute; on $\\tfrac{0}{0}$, factorise and cancel").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"\frac{x^2 - 16}{x - 4} = \frac{(x-4)(x+4)}{x-4} = x + 4").scale(1.0).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"\lim_{x \to -3} \frac{x^2 - 9}{x + 3} = \lim_{x \to -3} (x - 3) = -6").scale(1.0).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Limit $=$ approach, never arrival").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_2): average gradient
        self.next_band(2)
        b2_title = Tex(r"Average gradient on $f(x) = x^2$").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"x = 2 \text{ to } x = 4: \; \frac{16 - 4}{4 - 2} = 6").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex("A trip average, not a single instant").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"2 \to 3: 5 \quad 2 \to 2{,}5: 4{,}5 \quad 2 \to 2{,}1: 4{,}1 \quad 2 \to 2{,}01: 4{,}01").scale(0.85).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("The averages converge on 4").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): secant into tangent
        self.next_band(3)
        b3_title = Tex("Secant swings into tangent").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        # Parabola sketch with secant and tangent
        pc = band_shift(3) + DOWN * 0.4 + LEFT * 2.5
        axes_x = Line(pc + LEFT * 1.5, pc + RIGHT * 2.2, color=GREY, stroke_width=3)
        curve = ArcBetweenPoints(pc + LEFT * 1.2 + UP * 1.8, pc + RIGHT * 2.0 + UP * 2.6,
                                 angle=-1.6, color=WHITE, stroke_width=5)
        p1 = Dot(pc + LEFT * 0.4 + UP * 0.9, color=YELLOW)
        secant = Line(pc + LEFT * 1.4 + UP * 0.1, pc + RIGHT * 1.6 + UP * 2.4,
                      color=BLUE, stroke_width=4)
        tangent = Line(pc + LEFT * 1.3 + UP * 0.2, pc + RIGHT * 0.7 + UP * 1.8,
                       color=RED, stroke_width=4)
        self.play(Create(axes_x))
        self.play(Create(curve), FadeIn(p1))
        self.play(Create(secant))
        self.wait(2)
        self.play(Create(tangent))
        self.wait(2)
        b3_l1 = Tex("Second point slides home;").scale(0.95).shift(band_shift(3) + UP * 1.0 + RIGHT * 3.1)
        b3_l2 = Tex("the limiting line is the tangent").scale(0.95).shift(band_shift(3) + UP * 0.2 + RIGHT * 3.1)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"Gradient of curve at a point $=$ gradient of its tangent").scale(0.9).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l3))
        self.wait(3)

        # --- Band 4 (subtopic_3): the definition
        self.next_band(4)
        b4_title = Tex("The definition of the derivative").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"f'(x) = \lim_{h \to 0} \frac{f(x + h) - f(x)}{h}").scale(1.15).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(3)
        b4_l2 = MathTex(r"f(x) = x^2: \; (x+h)^2 - x^2 = 2xh + h^2").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"\frac{2xh + h^2}{h} = 2x + h \;\xrightarrow{h \to 0}\; 2x").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = MathTex(r"x = 2: 4 \quad x = 6: 12 \quad x = -4: -8").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): constant and straight line
        self.next_band(5)
        b5_title = Tex("Two quick machines").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"f(x) = c: \; \frac{c - c}{h} = 0 \;\Rightarrow\; f'(x) = 0").scale(1.0).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"f(x) = ax + b: \; \frac{ah}{h} = a \;\Rightarrow\; f'(x) = a").scale(1.0).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("If the $h$ refuses to cancel, the error is upstream").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3))
        self.wait(3)

        # --- Band 6 (subtopic_4): ax^2 + b and 1/x
        self.next_band(6)
        b6_title = Tex(r"$ax^2 + b$ and $\tfrac{1}{x}$ from first principles").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"a(2xh + h^2)/h = 2ax + ah \to 2ax").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"f(x) = 4x^2 \Rightarrow f'(x) = 8x").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"\frac{1}{x+h} - \frac{1}{x} = \frac{x - (x + h)}{x(x+h)} = \frac{-h}{x(x+h)}").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"\frac{-1}{x(x+h)} \;\xrightarrow{h \to 0}\; -\frac{1}{x^2}").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the notation
        self.next_band(7)
        b7_title = Tex("Four names, one machine").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"f'(x) \qquad \frac{dy}{dx} \qquad \frac{d}{dx}[\ldots] \qquad D_x[y]").scale(1.05).shift(band_shift(7) + UP * 1.0)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2.5)
        b7_l2 = Tex(r"$\tfrac{dy}{dx}$ is not a fraction — it remembers being one").scale(0.95).shift(band_shift(7) + DOWN * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Added constants vanish; multiplied constants survive").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the pothole in the graph
        self.next_band(8)
        b8_title = Tex("The pothole in the graph").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\frac{x^2 - 16}{x - 4}: \text{ silent at } x = 4").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"3{,}9 \to 7{,}9 \quad 3{,}99 \to 7{,}99 \quad 4{,}01 \to 8{,}01").scale(0.95).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Every neighbour points at 8 — that is the limit").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Substitute; on $\\tfrac{0}{0}$, factorise, cancel, substitute again").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the speedometer question
        self.next_band(9)
        b9_title = Tex("The speedometer question").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("210 km in 3 hours: average 70 km/h").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("One minute: 72. One second: closer. Shrink the window...").scale(0.95).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Instantaneous speed $=$ limit of shrinking averages").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = MathTex(r"y = x^2 \text{ at } x = 2: \; 5, \; 4{,}5, \; 4{,}1, \; 4{,}01 \to 4").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): the recipe
        self.next_band(10)
        b10_title = Tex("The recipe called first principles").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"1. write $f(x+h)$ \quad 2. subtract $f(x)$").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex(r"3. divide by $h$ and cancel \quad 4. let $h$ be zero").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"x^2: \; \frac{2xh + h^2}{h} = 2x + h \to 2x").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("A speedometer for every point at once").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(3)

        # --- Band 11 (subtopic_7): the small machines and the labels
        self.next_band(11)
        b11_title = Tex("Flat roads, straight roads, name tags").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = MathTex(r"f(x) = 12 \Rightarrow f'(x) = 0").scale(1.05).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"f(x) = ax + b \Rightarrow f'(x) = a").scale(1.05).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = MathTex(r"f'(x), \; \frac{dy}{dx}, \; D_x[y]: \text{ all read \emph{the derivative}}").scale(0.95).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2.5)
        b11_l4 = Tex("The $h$ must cancel — or hunt the slip upstream").scale(1.0).shift(band_shift(11) + DOWN * 2.0)
        self.play(Write(b11_l4))
        self.wait(4)
