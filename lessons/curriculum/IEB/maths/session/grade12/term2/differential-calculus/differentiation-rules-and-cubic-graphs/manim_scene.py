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
        title = Tex("Differentiation Rules and the Cubic").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = MathTex(r"\frac{d}{dx}\left[x^n\right] = n \, x^{n-1}").scale(1.2).shift(UP * 0.8)
        self.play(Write(d1))
        self.play(Create(SurroundingRectangle(d1, color=GREEN)))
        self.wait(2.5)
        d2 = Tex("Exponent falls forward; power steps down").scale(1.0).shift(DOWN * 0.2)
        self.play(Write(d2))
        self.wait(2)
        d3 = MathTex(r"y = 2x^5 - 4x + 7 \;\Rightarrow\; \frac{dy}{dx} = 10x^4 - 4").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(d3))
        self.wait(2.5)
        d4 = Tex("Constants multiply through; lone constants die to zero").scale(0.9).shift(DOWN * 2.2)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): rewriting first
        self.next_band(1)
        b1_title = Tex("Dress everything as a power of $x$").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"4\sqrt{x} = 4x^{1/2} \;\Rightarrow\; 2x^{-1/2} = \frac{2}{\sqrt{x}}").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"\frac{5}{x^3} = 5x^{-3} \;\Rightarrow\; -15x^{-4}").scale(1.0).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"\frac{3x^4 + x}{x^2} = 3x^2 + x^{-1} \;\Rightarrow\; 6x - x^{-2}").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex(r"Down from $-3$ lands on $-4$: more negative").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the tangent routine
        self.next_band(2)
        b2_title = Tex(r"Tangent to $f(x) = x^3 - 4x^2 + 3$ at $x = 2$").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"1.\; f(2) = 8 - 16 + 3 = -5").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"2.\; f'(x) = 3x^2 - 8x").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"3.\; f'(2) = 12 - 16 = -4").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"4.\; y + 5 = -4(x - 2) \;\Rightarrow\; y = -4x + 3").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): reverse questions
        self.next_band(3)
        b3_title = Tex("Where is the tangent gradient 3?").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"3x^2 - 8x = 3 \;\Rightarrow\; 3x^2 - 8x - 3 = 0").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"(3x + 1)(x - 3) = 0 \;\Rightarrow\; x = 3 \;\text{or}\; x = -\tfrac{1}{3}").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"Parallel to the $x$ axis $\Rightarrow$ gradient $0$").scale(1.0).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Parallel to a line: borrow that line's gradient").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): stationary points
        self.next_band(4)
        b4_title = Tex(r"Sketch $f(x) = x^3 - 3x^2 - 9x + 27$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"f'(x) = 3x^2 - 6x - 9 = 3(x + 1)(x - 3)").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"f'(x) = 0: \; x = -1 \;\text{or}\; x = 3").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"f(-1) = 32 \qquad f(3) = 0").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\text{Max } (-1; 32), \quad \text{Min } (3; 0)").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): intercepts and shape
        self.next_band(5)
        b5_title = Tex("Intercepts and the double root").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"f(0) = 27").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"f(x) = (x - 3)^2(x + 3)").scale(1.05).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex(r"$x = -3$ single: crosses. $x = 3$ double: touches and turns").scale(0.9).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"Touch point $=$ the minimum $(3; 0)$ — facts agree").scale(0.9).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): increase, decrease, inflection
        self.next_band(6)
        b6_title = Tex("Reading $f$ through $f'$").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"f' > 0: \text{ increasing} \qquad f' < 0: \text{ decreasing}").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{Decreasing for } -1 < x < 3").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"f''(x) = 6x - 6 = 0 \;\Rightarrow\; x = 1").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex(r"Inflection $(1; 16)$ — midway between the turning points").scale(0.9).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): second-derivative classification
        self.next_band(7)
        b7_title = Tex("Classify with $f''$").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"f''(-1) = -12 < 0: \text{ concave down — maximum}").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"f''(3) = 12 > 0: \text{ concave up — minimum}").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"$f$: position \quad $f'$: direction \quad $f''$: curvature").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the exponent falls forward
        self.next_band(8)
        b8_title = Tex("The exponent falls forward").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"x^2 \to 2x \qquad x^5 \to 5x^4 \qquad x^{12} \to 12x^{11}").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Lone numbers differentiate to zero").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = MathTex(r"4\sqrt{x} = 4x^{1/2} \qquad \frac{1}{x^4} = x^{-4}").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"\frac{3x^4 + x}{x^2} = 3x^2 + x^{-1} \to 6x - x^{-2}").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the hiking trail
        self.next_band(9)
        b9_title = Tex("The hiking trail").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        # Trail sketch: cubic-like path with lookout and valley floor
        tc = band_shift(9) + DOWN * 0.2 + LEFT * 2.6
        seg1 = ArcBetweenPoints(tc + LEFT * 1.4 + DOWN * 1.6, tc + UP * 1.2, angle=-0.9,
                                color=WHITE, stroke_width=5)
        seg2 = ArcBetweenPoints(tc + UP * 1.2, tc + RIGHT * 1.8 + DOWN * 1.0, angle=-0.9,
                                color=WHITE, stroke_width=5)
        seg3 = ArcBetweenPoints(tc + RIGHT * 1.8 + DOWN * 1.0, tc + RIGHT * 3.2 + UP * 1.4,
                                angle=0.9, color=WHITE, stroke_width=5)
        peak = Dot(tc + UP * 1.2, color=YELLOW)
        floor = Dot(tc + RIGHT * 1.8 + DOWN * 1.0, color=RED)
        self.play(Create(seg1))
        self.play(FadeIn(peak), Create(seg2))
        self.play(FadeIn(floor), Create(seg3))
        self.wait(2)
        b9_l1 = Tex("Level ground: $f'(x) = 0$").scale(0.95).shift(band_shift(9) + UP * 1.0 + RIGHT * 3.1)
        b9_l2 = Tex(r"Lookout $(-1; 32)$, floor $(3; 0)$").scale(0.9).shift(band_shift(9) + UP * 0.2 + RIGHT * 3.1)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"Decreasing between them: $-1 < x < 3$; inflection at $x = 1$").scale(0.85).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l3))
        self.wait(3)

        # --- Band 10 (subtopic_7): laying a ruler on the curve
        self.next_band(10)
        b10_title = Tex("Laying a ruler on the curve").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Function feeds heights; derivative feeds slopes").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"f(2) = -5 \qquad f'(2) = -4").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"y = -4x + 3").scale(1.1).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("Two feeds, one line, every time").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4))
        self.wait(3)

        # --- Band 11 (subtopic_7): reverse rulers
        self.next_band(11)
        b11_title = Tex("Rulers in reverse").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = MathTex(r"\text{Slope } 3: \; 3x^2 - 8x = 3 \Rightarrow x = 3 \text{ or } -\tfrac{1}{3}").scale(0.95).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.play(Create(SurroundingRectangle(b11_l1, color=GREEN)))
        self.wait(2.5)
        b11_l2 = Tex("A level ruler marks a stationary point").scale(1.0).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = Tex("Tangent questions and turning points: one question, two jackets").scale(0.9).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l3))
        self.wait(4)
