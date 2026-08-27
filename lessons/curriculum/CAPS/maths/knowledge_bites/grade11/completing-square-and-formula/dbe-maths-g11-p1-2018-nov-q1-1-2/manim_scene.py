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
