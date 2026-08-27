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
# band time apportioned to subtopics.json (230/250/220/250/190/200/220 of 1560 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EquationOfACircleAndTangentSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the circle as a distance statement
        title = Tex("The Circle and Its Tangent").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"(x - a)^2 + (y - b)^2 = r^2").scale(1.2).shift(UP * 0.8)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)
        d2 = Tex("The distance formula, holding a promise").scale(1.0).shift(DOWN * 0.2)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"(x - 3)^2 + (y + 2)^2 = 25").scale(1.1).shift(DOWN * 1.2)
        self.play(Write(d3))
        self.wait(2)
        d4 = MathTex(r"\text{Centre } (3; -2), \quad r = \sqrt{25} = 5").scale(1.05).shift(DOWN * 2.2)
        self.play(Write(d4))
        self.wait(2)
        d5 = Tex("Flip the signs; root the right side").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(d5))
        self.wait(3)

        # --- Band 1 (subtopic_1): membership testing
        self.next_band(1)
        b1_title = Tex(r"Does $(6; 2)$ lie on the circle?").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"(6 - 3)^2 + (2 + 2)^2").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"= 9 + 16 = 25 \;\checkmark \text{ on the circle}").scale(1.1).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = MathTex(r"< 25: \text{ inside} \qquad > 25: \text{ outside}").scale(1.05).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"\text{Origin centre: } x^2 + y^2 = r^2").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): completing the square
        self.next_band(2)
        b2_title = Tex(r"Unmask: $x^2 + y^2 - 6x + 4y - 12 = 0$").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"(x^2 - 6x) + (y^2 + 4y) = 12").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"(x - 3)^2 - 9 + (y + 2)^2 - 4 = 12").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"(x - 3)^2 + (y + 2)^2 = 12 + 9 + 4 = 25").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"\text{Centre } (3; -2), \quad r = 5").scale(1.1).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("Whatever completes a square must balance across").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): structural warnings
        self.next_band(3)
        b3_title = Tex("When is it really a circle?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"$x^2$ and $y^2$ need EQUAL coefficients, no $xy$").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex("A coefficient on both squares? Divide it out first").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"r^2 = 0: \text{ a single point} \qquad r^2 < 0: \text{ nothing}").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("Check by expanding back, or test a known point").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): radius meets tangent at ninety degrees
        self.next_band(4)
        b4_title = Tex("Radius meets tangent at $90^\\circ$").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        # Wheel-and-road mini diagram: circle, road line, spoke to touch point
        wc = band_shift(4) + UP * 0.6 + LEFT * 2.3
        wheel = Circle(radius=1.0, color=WHITE, stroke_width=5).move_to(wc)
        road = Line(wc + DOWN * 1.0 + LEFT * 1.6, wc + DOWN * 1.0 + RIGHT * 1.6,
                    color=YELLOW, stroke_width=5)
        spoke = Line(wc, wc + DOWN * 1.0, color=RED, stroke_width=5)
        touch = Dot(wc + DOWN * 1.0, color=RED)
        self.play(Create(wheel))
        self.play(Create(road))
        self.play(Create(spoke), FadeIn(touch))
        self.wait(2)
        b4_l1 = Tex("One touching point;").scale(1.0).shift(band_shift(4) + UP * 1.0 + RIGHT * 3.0)
        b4_l2 = Tex("spoke square to road").scale(1.0).shift(band_shift(4) + UP * 0.2 + RIGHT * 3.0)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"m_{\text{radius}} \times m_{\text{tangent}} = -1").scale(1.1).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = MathTex(r"m_r = \tfrac{4}{3} \Rightarrow m_t = -\tfrac{3}{4}").scale(0.95).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): what the fact settles instantly
        self.next_band(5)
        b5_title = Tex("Three questions the spoke settles").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Tangent at a point? Check $m_r \times m_t = -1$").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Shortest distance centre to tangent $=$ the radius").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Tangents through an external point: exactly two,").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex("symmetric about the line to the centre").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the tangent equation routine
        self.next_band(6)
        b6_title = Tex(r"Tangent to $(x-3)^2 + (y+2)^2 = 25$ at $(6; 2)$").scale(1.0).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"1.\; \text{On circle: } 9 + 16 = 25 \;\checkmark").scale(1.0).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"2.\; m_r = \frac{2 - (-2)}{6 - 3} = \frac{4}{3}").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"3.\; m_t = -\tfrac{3}{4}").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"4.\; y - 2 = -\tfrac{3}{4}(x - 6)").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = MathTex(r"y = -\tfrac{3}{4}x + \tfrac{13}{2}").scale(1.1).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the origin-centred version
        self.next_band(7)
        b7_title = Tex(r"Tangent to $x^2 + y^2 = 25$ at $(3; 4)$").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"m_r = \tfrac{4}{3} \;\Rightarrow\; m_t = -\tfrac{3}{4}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"y = -\tfrac{3}{4}x + \tfrac{25}{4}").scale(1.1).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = MathTex(r"\text{Origin: at } (x_1; y_1), \; m = -\tfrac{x_1}{y_1}").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Certify: substitute the touching point back in").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): every point the rope can reach
        self.next_band(8)
        b8_title = Tex("Every point the rope can reach").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("A goat on a taut rope of 5 traces the circle").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"(x - 3)^2 + (y + 2)^2 = 25").scale(1.1).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex(r"Peg at $(3; -2)$ — the signs flip; rope $= \sqrt{25} = 5$").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"(6; 2): \; 9 + 16 = 25 \text{ — rope taut, ON the circle}").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex("Below 25: inside reach. Above: beyond the rope").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the circle in disguise
        self.next_band(9)
        b9_title = Tex("The circle in disguise").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"x^2 + y^2 - 6x + 4y - 12 = 0").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Sort the drawer: $x$ items, $y$ items, numbers across").scale(0.95).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"(x - 3)^2 + (y + 2)^2 = 12 + 9 + 4").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"\text{Peg } (3; -2), \text{ rope } 5").scale(1.1).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("Declare every sneaked-in number on both sides").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the wheel and the road
        self.next_band(10)
        b10_title = Tex("Where the wheel kisses the road").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Hub, spoke, road $=$ centre, radius, tangent").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("The spoke stands dead square to the road").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Four stops: on the wheel? spoke gradient;").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        b10_l4 = Tex("flip and negate; point-gradient form").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(3)

        # --- Band 11 (subtopic_7): the ride, worked
        self.next_band(11)
        b11_title = Tex(r"Hub $(3; -2)$, touch point $(6; 2)$").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Spoke climbs 4 for every 3 across").scale(1.05).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = Tex("Road drops 3 for every 4 across").scale(1.05).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = MathTex(r"y = -\tfrac{3}{4}x + \tfrac{13}{2}").scale(1.15).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2.5)
        b11_l4 = Tex("Substitute the kiss point back — it balances").scale(1.0).shift(band_shift(11) + DOWN * 2.0)
        self.play(Write(b11_l4))
        self.wait(4)
