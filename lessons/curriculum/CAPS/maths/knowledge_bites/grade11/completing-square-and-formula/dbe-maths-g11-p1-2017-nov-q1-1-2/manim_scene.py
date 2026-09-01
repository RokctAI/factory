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

# Auto-generated past-paper worked example.
# Source: DBE Grade 11 Maths P1, November 2017, Q1.1.2
# © Department of Basic Education, 2017. Reproduced for educational use with attribution.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2017 P1 Q1.1.2").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        eq = MathTex(r"7x^2 + 3x - 2 = 0")
        self.play(Write(eq)); self.wait(2)
        self.play(eq.animate.shift(UP * 2))
        coeffs = MathTex(r"a = 7, \quad b = 3, \quad c = -2").scale(0.9).shift(UP * 0.5)
        self.play(Write(coeffs)); self.wait(2)
        formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").shift(DOWN * 0.5)
        self.play(Write(formula)); self.wait(2)
        sub = MathTex(r"x = \frac{-3 \pm \sqrt{3^2 - 4(7)(-2)}}{2(7)} = \frac{-3 \pm \sqrt{65}}{14}").scale(0.9).shift(DOWN * 1.5)
        self.play(Write(sub)); self.wait(2)
        ans = MathTex(r"x = -0{,}79 \quad \text{or} \quad x = 0{,}36").shift(DOWN * 2.6)
        self.play(Write(ans)); self.wait(3)
