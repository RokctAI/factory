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
# Source: DBE Grade 11 Maths P1, November 2017, Q1.1.1
# © Department of Basic Education, 2017. Reproduced for educational use with attribution.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2017 P1 Q1.1.1").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        eq = MathTex(r"(2x - 3)(x + 7) = 0")
        self.play(Write(eq)); self.wait(2)
        self.play(eq.animate.shift(UP * 2))
        note = Tex(r"Zero-product property: a product is 0 when a factor is 0").scale(0.7)
        self.play(Write(note)); self.wait(2)
        left = MathTex(r"2x - 3 = 0 \Rightarrow x = \tfrac{3}{2}").scale(0.9).shift(LEFT * 2.5 + DOWN)
        right = MathTex(r"x + 7 = 0 \Rightarrow x = -7").scale(0.9).shift(RIGHT * 2.5 + DOWN)
        self.play(Write(left), Write(right)); self.wait(2)
        ans = MathTex(r"x = \tfrac{3}{2} \quad \text{or} \quad x = -7").shift(DOWN * 2.5)
        self.play(Write(ans)); self.wait(3)
