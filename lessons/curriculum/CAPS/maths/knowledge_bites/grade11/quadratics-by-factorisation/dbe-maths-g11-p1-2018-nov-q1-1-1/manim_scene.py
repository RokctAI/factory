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

# Auto-generated past-paper worked example.
# Source: DBE Grade 11 Mathematics P1, November 2018, Q1.1.1
# (c) Department of Basic Education, 2018.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2018 P1 Q1.1.1").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        eq = MathTex(r"x(2x + 1) = 0")
        self.play(Write(eq)); self.wait(2)
        self.play(eq.animate.shift(UP * 2))
        note = Tex(r"Zero-product property: a product is 0 when a factor is 0").scale(0.7)
        self.play(Write(note)); self.wait(2)
        left = MathTex(r"x = 0").shift(LEFT * 2 + DOWN)
        right = MathTex(r"2x + 1 = 0 \Rightarrow x = -\tfrac{1}{2}").shift(RIGHT * 2 + DOWN)
        self.play(Write(left), Write(right)); self.wait(2)
        ans = MathTex(r"x = 0 \quad \text{or} \quad x = -\tfrac{1}{2}").shift(DOWN * 2.5)
        self.play(Write(ans)); self.wait(3)
