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

# Band-layout whiteboard scene (see AUTHORING-SPEC / quadratics-by-factorisation
# worked example). One band per teaching beat, camera moves down, nothing is
# ever removed. Covers all seven subtopics of the session duo:
# Part 1 — Expert (subtopics 1-4), Part 2 — Simplifier (subtopics 5-7),
# band time apportioned to subtopics.json (235/235/240/240/195/200/195 of 1540 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class OptimisationAndRatesOfChangeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): motion — position, velocity, acceleration
        title = Tex("Optimisation and Rates of Change").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"s(t) \to v(t) \to a(t) \; \text{ (differentiate)}").scale(1.05).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = MathTex(r"s(t) = 2t^3 - 9t^2 + 12t").scale(1.1).shift(DOWN * 0.1)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"v(t) = 6t^2 - 18t + 12 = 6(t-1)(t-2)").scale(1.05).shift(DOWN * 1.1)
        self.play(Write(d3))
        self.wait(2.5)
        d4 = MathTex(r"\text{At rest at } t = 1 \text{ and } t = 2").scale(1.05).shift(DOWN * 2.1)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(2)
        d5 = MathTex(r"a(t) = 12t - 18 = 0 \text{ at } t = 1{,}5").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(d5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the language map
        self.next_band(1)
        b1_title = Tex("Words map to calculus, one to one").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{At rest / stationary: } v = 0").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"\text{Maximum height: } \frac{dh}{dt} = 0").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"\text{Initial velocity: } v(0) = 12").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"\text{Speed is the size: } v = -3 \Rightarrow \text{speed } 3").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the optimisation recipe — the camp
        self.next_band(2)
        b2_title = Tex("120 m of fence against a wall — biggest camp?").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Width } x: \text{ length} = 120 - 2x").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"A(x) = x(120 - 2x) = 120x - 2x^2").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"A'(x) = 120 - 4x = 0 \;\Rightarrow\; x = 30").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"30 \text{ m} \times 60 \text{ m}, \quad A = 1800 \text{ m}^2").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = MathTex(r"A''(x) = -4 < 0: \text{ concave down — maximum}").scale(0.95).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the recipe itself
        self.next_band(3)
        b3_title = Tex("The recipe, in four steps").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("1. Write the quantity as a formula").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("2. Use the constraint to reach ONE variable").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("3. Differentiate, set to zero, solve").scale(1.05).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex("4. Classify, then answer what is ASKED").scale(1.05).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("The constraint is where the second variable dies").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the open box — setup
        self.next_band(4)
        b4_title = Tex(r"Open box, square base, must hold 500 cm$^3$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"x^2 h = 500 \;\Rightarrow\; h = \frac{500}{x^2}").scale(1.05).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"S = x^2 + 4xh").scale(1.05).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"S(x) = x^2 + 4x \cdot \frac{500}{x^2}").scale(1.05).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"S(x) = x^2 + \frac{2000}{x} \quad \text{— one variable}").scale(1.05).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the open box — solved
        self.next_band(5)
        b5_title = Tex("Minimise the material").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"S'(x) = 2x - \frac{2000}{x^2} = 0").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"x^3 = 1000 \;\Rightarrow\; x = 10, \quad h = 5").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"S = 100 + 200 = 300 \text{ cm}^2").scale(1.05).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = MathTex(r"S''(x) = 2 + \frac{4000}{x^3} > 0: \text{ genuine minimum}").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = MathTex(r"\frac{2000}{x} = 2000x^{-1} \to -2000x^{-2} \; \text{(sign first!)}").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three interrogations
        self.next_band(6)
        b6_title = Tex("Calculus proposes; the context disposes").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"1. In the sensible domain? Here $0 < x < 60$").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = Tex("2. Right TYPE? Classify with $f''$ or a sign check").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("3. Asked for the $x$, the value, or a consequence?").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("On a closed domain, check the ENDPOINTS too").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the vetkoek profit model
        self.next_band(7)
        b7_title = Tex(r"$P(n) = -2n^3 + 30n^2 - 90n$, $0 \leq n \leq 12$").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"P'(n) = -6n^2 + 60n - 90 = 0").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = MathTex(r"n^2 - 10n + 15 = 0 \;\Rightarrow\; n = 5 \pm \sqrt{10}").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = MathTex(r"n \approx 1{,}84 \text{ (min)}, \; n \approx 8{,}16 \text{ (max)}").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = MathTex(r"P''(n) = -12n + 60 \text{ chooses which is which}").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex(r"Profit peaks near 816 vetkoek — report THAT root").scale(1.0).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the dashboard and the handbrake
        self.next_band(8)
        b8_title = Tex("The dashboard and the handbrake").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Odometer: position. Speedometer: its derivative.").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("The push in your back: acceleration").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{Handbrake moments: } v = 0 \text{ at } t = 1, \; t = 2").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Between them $v < 0$: the bakkie is reversing").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("The speedometer never shows a minus — velocity does").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the biggest kraal
        self.next_band(9)
        b9_title = Tex("The biggest kraal on a fixed roll of fence").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Skinny sliver: nothing. All-sides strip: nothing.").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("The best kraal hides between the extremes").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"A = x(120 - 2x), \quad A' = 120 - 4x = 0").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"x = 30: \;\; 30 \times 60 = 1800 \text{ m}^2").scale(1.05).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("Try 29 or 31 and watch the area dip").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the cheapest tin
        self.next_band(10)
        b10_title = Tex("The cheapest tin that holds enough").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Space fixed at 500; material is money").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Wide tin: huge base. Tall tin: endless walls.").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"S(x) = x^2 + \frac{2000}{x}, \quad 2x - \frac{2000}{x^2} = 0").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = MathTex(r"x = 10, \; h = 5: \; 300 \text{ cm}^2").scale(1.05).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Half as tall as it is wide — like real tins").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.wait(4)
