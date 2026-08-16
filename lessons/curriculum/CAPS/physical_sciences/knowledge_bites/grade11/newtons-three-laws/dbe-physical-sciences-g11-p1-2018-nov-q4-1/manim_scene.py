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
# Source: DBE Grade 11 Physical Sciences P1, November 2018, Q4.1
# (c) Department of Basic Education, 2018.
class PastPaperWorkedExample(Scene):
    def construct(self):
        head = Tex(r"Past paper: DBE Nov 2018 P1 Q4.1").to_edge(UP)
        self.play(Write(head)); self.wait(1)
        ask = Tex(r"State Newton's Second Law of Motion in words. (2)").scale(0.8).shift(UP * 1.5)
        self.play(Write(ask)); self.wait(2)
        l1 = Tex(r"When a \textbf{net force} acts on an object, the object").scale(0.7)
        l2 = Tex(r"\textbf{accelerates} in the \textbf{direction of the force}.").scale(0.7).shift(DOWN * 0.5)
        l3 = Tex(r"The acceleration is \textbf{directly proportional to the net force}").scale(0.7).shift(DOWN * 1.2)
        l4 = Tex(r"and \textbf{inversely proportional to the mass}.").scale(0.7).shift(DOWN * 1.7)
        for l in (l1, l2, l3, l4):
            self.play(Write(l)); self.wait(1)
        warn = Tex(r"Memo: $-1$ mark if a key phrase is missing.").scale(0.6).shift(DOWN * 2.8)
        self.play(Write(warn)); self.wait(3)
