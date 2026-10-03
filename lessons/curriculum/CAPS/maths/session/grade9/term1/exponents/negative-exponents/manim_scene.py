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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class NegativeExponentsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): extending the division law
        title = Tex("Negative Exponents").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = MathTex(r"2^3 \div 2^5 = 2^{3-5} = 2^{-2}").scale(1.05).shift(UP * 1.3)
        l2 = MathTex(r"\frac{2 \cdot 2 \cdot 2}{2 \cdot 2 \cdot 2 \cdot 2 \cdot 2} = \frac{1}{2^2} = \frac{1}{4}").scale(1.0).shift(UP * 0.2)
        l3 = MathTex(r"a^{-m} = \frac{1}{a^m} \quad (a \neq 0)").scale(1.15).shift(DOWN * 0.8)
        l4 = MathTex(r"8,\; 4,\; 2,\; 1,\; \tfrac{1}{2},\; \tfrac{1}{4},\; \tfrac{1}{8} \;\text{(small, never negative)}").scale(0.95).shift(DOWN * 1.8)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): evaluating
        self.next_band(1)
        b1_title = Tex("Evaluate: reciprocal first, then the power").scale(1.1).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"3^{-2} = \frac{1}{9} \qquad 6^{-2} = \frac{1}{36} \qquad 10^{-3} = 0{,}001").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"(-2)^{-3} = \frac{1}{(-2)^3} = -\frac{1}{8} \qquad (-2)^{-2} = \frac{1}{4}").scale(0.95).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"\left(\tfrac{2}{3}\right)^{-2} = \left(\tfrac{3}{2}\right)^{2} = \tfrac{9}{4} \qquad \left(\tfrac{1}{2}\right)^{-3} = 8").scale(0.95).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"5 \times 2^{-3} = \tfrac{5}{8} \qquad (5 \times 2)^{-3} = \tfrac{1}{1\,000}").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): simplifying
        self.next_band(2)
        b2_title = Tex("Cross the bar, flip the sign").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"x^{-3} = \frac{1}{x^3} \qquad \frac{1}{x^{-2}} = x^2").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = MathTex(r"x^2 \div x^6 = x^{-4} = \frac{1}{x^4} \qquad (2x)^{-2} = \frac{1}{4x^2}").scale(0.95).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"3x^{-2} = \frac{3}{x^2} \;\text{(the 3 stays on top)}").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"\frac{4a^{-3}b^2}{2ab^{-1}} = 2a^{-4}b^3 = \frac{2b^3}{a^4}").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): scientific notation and units
        self.next_band(3)
        b3_title = Tex("Scientific notation through the law").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"7{,}5 \times 10^{-6} = \frac{7{,}5}{1\,000\,000} = 0{,}0000075").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"0{,}00052 = \frac{5{,}2}{10^4} = 5{,}2 \times 10^{-4}").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"2^{-10} = \frac{1}{1\,024} \approx 0{,}001 \qquad \text{m s}^{-1} = \text{metres per second}").scale(0.9).shift(band_shift(3) + DOWN * 0.8)
        for m in (b3_l1, b3_l2, b3_l3):
            self.play(Write(m))
            self.wait(2.4)
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"2^{-3} = -8 \qquad 2^{-3} = -\tfrac{1}{8}").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"3x^{-2} = \frac{1}{3x^2}").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"\frac{1}{2^{-3}} = \frac{1}{8}").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"2^{-1} + 2^{-2} = 2^{-3}").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the pattern keeps going
        self.next_band(5)
        b5_title = Tex("The pattern keeps going down").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(2)
        rows = [
            r"2^3 = 8 \quad 2^2 = 4 \quad 2^1 = 2 \quad 2^0 = 1",
            r"2^{-1} = \tfrac{1}{2} \quad 2^{-2} = \tfrac{1}{4} \quad 2^{-3} = \tfrac{1}{8}",
            r"10^3,\; 10^2,\; 10^1,\; 10^0,\; 10^{-1},\; 10^{-2},\; 10^{-3}",
            r"1\,000,\; 100,\; 10,\; 1,\; 0{,}1,\; 0{,}01,\; 0{,}001",
        ]
        for i, r in enumerate(rows):
            m = MathTex(r).scale(0.95).shift(band_shift(5) + UP * (1.3 - 0.85 * i))
            self.play(Write(m))
            self.wait(2.2)
        b5_l5 = Tex("Small, not negative.").scale(1.1).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): flip it over
        self.next_band(6)
        b6_title = Tex("Flip it over: hop the fence").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(2)
        fence = Line(LEFT * 2.5, RIGHT * 2.5, color=WHITE, stroke_width=4).shift(band_shift(6) + UP * 0.9)
        above = MathTex(r"2^{-3}").scale(1.1).shift(band_shift(6) + UP * 1.5 + LEFT * 1.5)
        below = MathTex(r"2^{3} = 8 \;\text{(below)}").scale(1.0).shift(band_shift(6) + UP * 0.3 + RIGHT * 1.0)
        self.play(Create(fence))
        self.play(Write(above))
        self.wait(1.5)
        self.play(Write(below))
        self.wait(2)
        b6_l3 = Tex(r"Only the one with the minus hops: $3x^{-2} = \dfrac{3}{x^2}$").scale(0.95).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = Tex(r"A fraction that hops turns over: $\left(\tfrac{2}{3}\right)^{-2} = \tfrac{9}{4}$").scale(0.95).shift(band_shift(6) + DOWN * 1.7)
        for m in (b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.wait(1.5)

        # --- Band 7 (subtopic_7): where they show up
        self.next_band(7)
        b7_title = Tex("Where negative exponents show up").scale(1.15).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"5{,}2 \times 10^{-4} = 5{,}2 \div 10\,000 = 0{,}00052").scale(1.0).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"m s$^{-1}$ means metres per second").scale(1.0).shift(band_shift(7) + UP * 0.4)
        b7_l3 = MathTex(r"2^{-10} = \tfrac{1}{1\,024} \approx 0{,}001").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex(r"Check with $x = 1$: $(2x)^{-2}$ is $\tfrac{1}{4}$, not $\tfrac{1}{2}$").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex("Small, not negative. Hop the fence. Only the minus hops.").scale(0.9).shift(band_shift(7) + DOWN * 2.3)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=YELLOW)))
        self.wait(4)
