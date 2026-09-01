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
# Source: DBE Grade 11 Mathematics P1, November 2018, Q1.1.2
# (c) Department of Basic Education, 2018.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2018 P1 Q1.1.2").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        eq = MathTex(r"5x^2 + 2x - 6 = 0")
        self.play(Write(eq)); self.wait(2)
        self.play(eq.animate.shift(UP * 2))
        coeffs = MathTex(r"a = 5, \quad b = 2, \quad c = -6").scale(0.9).shift(UP * 0.5)
        self.play(Write(coeffs)); self.wait(2)
        formula = MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}").shift(DOWN * 0.5)
        self.play(Write(formula)); self.wait(2)
        sub = MathTex(r"x = \frac{-2 \pm \sqrt{2^2 - 4(5)(-6)}}{2(5)} = \frac{-2 \pm \sqrt{124}}{10}").scale(0.9).shift(DOWN * 1.5)
        self.play(Write(sub)); self.wait(2)
        ans = MathTex(r"x = 0{,}91 \quad \text{or} \quad x = -1{,}31").shift(DOWN * 2.6)
        self.play(Write(ans)); self.wait(3)
