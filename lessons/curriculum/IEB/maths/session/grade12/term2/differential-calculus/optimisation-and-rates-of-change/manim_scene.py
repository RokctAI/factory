# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

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
        # --- Band 0 (subtopic_1): the motion chain
        title = Tex("Optimisation and Rates of Change").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"s(t) \;\xrightarrow{\;d/dt\;}\; v(t) \;\xrightarrow{\;d/dt\;}\; a(t)").scale(1.1).shift(UP * 0.8)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)
        d2 = MathTex(r"s(t) = 2t^3 - 15t^2 + 24t").scale(1.05).shift(DOWN * 0.2)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"v(t) = 6t^2 - 30t + 24 = 6(t - 1)(t - 4)").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(d3))
        self.wait(2.5)
        d4 = MathTex(r"\text{At rest: } v = 0 \Rightarrow t = 1 \text{ or } t = 4").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): acceleration and the word map
        self.next_band(1)
        b1_title = Tex("Acceleration and the phrase book").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"a(t) = 12t - 30 = 0 \;\Rightarrow\; t = 2{,}5").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"\text{Initial velocity: } v(0) = 24 \text{ m/s}").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex(r"Velocity $-5$ m/s $=$ speed $5$ m/s, reversed").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("At rest $\\Rightarrow v = 0$; max height $\\Rightarrow$ derivative $= 0$").scale(0.9).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the recipe on the camp
        self.next_band(2)
        b2_title = Tex("160 m of fence against a wall").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        # Camp diagram: wall plus three fenced sides
        cc = band_shift(2) + UP * 0.7 + LEFT * 2.6
        wall = Line(cc + LEFT * 1.7, cc + RIGHT * 1.7, color=GREY, stroke_width=8)
        left_f = Line(cc + LEFT * 1.7, cc + LEFT * 1.7 + DOWN * 1.4, color=YELLOW, stroke_width=5)
        right_f = Line(cc + RIGHT * 1.7, cc + RIGHT * 1.7 + DOWN * 1.4, color=YELLOW, stroke_width=5)
        front_f = Line(cc + LEFT * 1.7 + DOWN * 1.4, cc + RIGHT * 1.7 + DOWN * 1.4,
                       color=YELLOW, stroke_width=5)
        self.play(Create(wall))
        self.play(Create(left_f), Create(right_f))
        self.play(Create(front_f))
        self.wait(2)
        b2_l1 = MathTex(r"A(x) = x(160 - 2x) = 160x - 2x^2").scale(0.95).shift(band_shift(2) + UP * 0.6 + RIGHT * 3.0)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"A'(x) = 160 - 4x = 0 \;\Rightarrow\; x = 40").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"40 \text{ m} \times 80 \text{ m}, \; A = 3200 \text{ m}^2, \; A'' = -4 < 0").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the four steps
        self.next_band(3)
        b3_title = Tex("The optimisation recipe").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("1. Formula for the quantity to optimise").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("2. Constraint kills all variables but one").scale(1.0).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("3. Differentiate, set to zero, solve").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex("4. Verify the type; answer what was asked").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the open-topped box
        self.next_band(4)
        b4_title = Tex(r"Open box, square base, holds $108$ cm$^3$").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"x^2 h = 108 \;\Rightarrow\; h = \frac{108}{x^2}").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"S = x^2 + 4xh = x^2 + \frac{432}{x}").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"S'(x) = 2x - \frac{432}{x^2} = 0 \;\Rightarrow\; x^3 = 216").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = MathTex(r"x = 6, \; h = 3, \; S = 108 \text{ cm}^2").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): verifying and the sign trap
        self.next_band(5)
        b5_title = Tex("Verify, and mind the minus sign").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"S''(x) = 2 + \frac{864}{x^3} > 0: \text{ genuine minimum}").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\frac{432}{x} = 432x^{-1} \;\Rightarrow\; -432x^{-2}").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"Open square boxes minimise at $h = \tfrac{x}{2}$ — prove it, never assume it").scale(0.85).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.wait(3)

        # --- Band 6 (subtopic_4): domains and interpretation
        self.next_band(6)
        b6_title = Tex("Calculus proposes; context decides").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Domain first: $0 < x < 80$; reject $x = -40$ in writing").scale(0.9).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"P(n) = -n^3 + 12n^2 - 21n, \; 0 \le n \le 10").scale(0.95).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"P'(n) = 0: \; (n - 1)(n - 7) = 0 \Rightarrow n = 1 \text{ or } 7").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"P''(7) = -18 < 0: \text{ profit peaks at } n = 7").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): endpoints
        self.next_band(7)
        b7_title = Tex("Check the ends of the range").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("On a closed range, the best value can sit at a boundary").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("with no zero derivative there at all").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Domain, type, phrasing: three interrogations, every time").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the dashboard
        self.next_band(8)
        b8_title = Tex("The dashboard and the handbrake").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Odometer: position. Speedometer: its derivative.").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("The shove in your seat: acceleration").scale(0.95).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"v(t) = 6(t - 1)(t - 4): \text{ handbrake at } t = 1, 4").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Between the stops: velocity negative — reversing").scale(0.95).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the kraal
        self.next_band(9)
        b9_title = Tex("The biggest kraal on one roll of fence").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Wall free; roll covers two widths and one front").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"A(x) = x(160 - 2x)").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"A'(x) = 160 - 4x = 0 \Rightarrow x = 40").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex(r"Width 40, front 80, area 3200 m$^2$ — try 39 and 41: it sags").scale(0.85).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): the tin
        self.next_band(10)
        b10_title = Tex("The cheapest tin that holds enough").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"x^2 h = 108 \Rightarrow h = \frac{108}{x^2}").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"S(x) = x^2 + \frac{432}{x}").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Wide: big base, small walls. Tall: small base, endless walls").scale(0.85).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("The cheapest design is the truce between the two costs").scale(0.9).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4))
        self.wait(3)

        # --- Band 11 (subtopic_7): the squat winner
        self.next_band(11)
        b11_title = Tex("The winning tin").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = MathTex(r"2x - \frac{432}{x^2} = 0 \Rightarrow x^3 = 216 \Rightarrow x = 6").scale(1.0).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2.5)
        b11_l2 = MathTex(r"h = 3, \quad S = 36 + 72 = 108 \text{ cm}^2").scale(1.0).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11_l2))
        self.play(Create(SurroundingRectangle(b11_l2, color=GREEN)))
        self.wait(2.5)
        b11_l3 = Tex("Half as tall as it is wide — squat, like real tins").scale(0.95).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = Tex("The fraction's minus sign must survive the derivative").scale(0.9).shift(band_shift(11) + DOWN * 1.8)
        self.play(Write(b11_l4))
        self.wait(4)
