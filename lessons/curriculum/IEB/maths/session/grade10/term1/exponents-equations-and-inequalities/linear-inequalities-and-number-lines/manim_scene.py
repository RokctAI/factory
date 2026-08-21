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

# Band-layout whiteboard scene: one band per teaching beat, camera moves down
# to fresh space, nothing removed. Write-only reveals on single-string
# Tex/MathTex keep the export clean. Bands cover all seven subtopics
# (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7), dwell time proportional
# to subtopics.json (235/220/210/250/195/185/200 of 1495 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


def numberline(center, lo=-6, hi=6):
    line = Line(center + LEFT * 4.5, center + RIGHT * 4.5, stroke_width=4)
    return line


class LinearInequalitiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): one exception
        title = Tex("Linear Inequalities and Number Lines").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l01 = MathTex(r"5x - 2 \leq 13 \;\Rightarrow\; 5x \leq 15 \;\Rightarrow\; x \leq 3").scale(1.0).shift(UP * 0.9)
        self.play(Write(l01))
        self.wait(2)
        l02 = Tex(r"Divide by a NEGATIVE: the sign flips").scale(1.05).shift(UP * 0.0)
        self.play(Write(l02))
        self.play(Create(SurroundingRectangle(l02, color=YELLOW)))
        self.wait(2)
        l03 = MathTex(r"-3x > 12 \;\Rightarrow\; x < -4").scale(1.05).shift(DOWN * 1.0)
        self.play(Write(l03))
        self.play(Create(SurroundingRectangle(l03, color=GREEN)))
        self.wait(2)
        l04 = Tex(r"Test $x=-5$: $-3(-5)=15 > 12$ \; ✓").scale(0.95).shift(DOWN * 2.0)
        self.play(Write(l04))
        self.wait(2.5)

        # --- Band 1 (subtopic_2): number line and intervals
        self.next_band(1)
        b1_title = Tex("Dots, shading, brackets").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_line = Line(band_shift(1) + UP * 1.0 + LEFT * 4, band_shift(1) + UP * 1.0 + RIGHT * 4, stroke_width=4)
        self.play(Create(b1_line))
        b1_dot = Dot(band_shift(1) + UP * 1.0 + RIGHT * 1.5, radius=0.1, color=GREEN)
        self.play(Create(b1_dot))
        b1_shade = Line(band_shift(1) + UP * 1.0 + RIGHT * 1.5, band_shift(1) + UP * 1.0 + LEFT * 4, stroke_width=8, color=GREEN)
        self.play(Create(b1_shade))
        b1_l1 = Tex(r"$x \leq 3$: solid dot at 3, shade left").scale(0.95).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"(-\infty \, ; \, 3] \quad\text{round at } \infty,\; \text{square at } 3").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = Tex(r"Smaller value on the left, always").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l3))
        self.wait(2.5)

        # --- Band 2 (subtopic_3): compound
        self.next_band(2)
        b2_title = Tex(r"Compound: $-5 \leq 3x + 1 < 10$").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"-6 \leq 3x < 9").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"-2 \leq x < 3").scale(1.1).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_line = Line(band_shift(2) + DOWN * 0.8 + LEFT * 4, band_shift(2) + DOWN * 0.8 + RIGHT * 4, stroke_width=4)
        self.play(Create(b2_line))
        b2_seg = Line(band_shift(2) + DOWN * 0.8 + LEFT * 1.5, band_shift(2) + DOWN * 0.8 + RIGHT * 2.0, stroke_width=8, color=GREEN)
        b2_d1 = Dot(band_shift(2) + DOWN * 0.8 + LEFT * 1.5, radius=0.1, color=GREEN)
        b2_d2 = Circle(radius=0.1, color=GREEN).move_to(band_shift(2) + DOWN * 0.8 + RIGHT * 2.0)
        self.play(Create(b2_seg), Create(b2_d1), Create(b2_d2))
        self.wait(2)
        b2_l3 = MathTex(r"[-2 \, ; \, 3) \quad \text{solid at } -2, \text{ hollow at } 3").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l3))
        self.wait(2.5)

        # --- Band 3 (subtopic_4): vetkoek word problem
        self.next_band(3)
        b3_title = Tex("Stand fee R150, vetkoek R15, profit at least R450").scale(0.95).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"15n - 150 \geq 450").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"15n \geq 600 \;\Rightarrow\; n \geq 40").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex(r"Answer in context: at least forty vetkoek").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"Boundary: $40 \times 15 - 150 = 450$ — exactly on target").scale(0.9).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex(r"at least / at most: bar; \; more than / fewer than: strict").scale(0.85).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5): debt flips
        self.next_band(4)
        b4_title = Tex("Debt turns everything upside down").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"400 > 250 \quad\text{but}\quad -400 < -250").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=YELLOW)))
        self.wait(2)
        b4_l2 = Tex(r"Owing R400 is WORSE than owing R250").scale(1.0).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"-3x > 12 \;\Rightarrow\; x < -4").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 5 (subtopic_6): the gate and the dots
        self.next_band(5)
        b5_title = Tex("Admitted or turned away").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"``Sixteen and older'': the 16-year-old walks in").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"``Older than sixteen'': same person stays outside").scale(0.95).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex(r"Solid dot / square bracket: admitted").scale(0.95).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex(r"Hollow dot / round bracket: turned away").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l3))
        self.wait(1.5)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2.5)

        # --- Band 6 (subtopic_7): two fences and the vetkoek test
        self.next_band(6)
        b6_title = Tex("Between two fences, and the vetkoek test").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"-5 \leq 3x + 1 < 10 \;\Rightarrow\; -2 \leq x < 3").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)
        b6_l2 = MathTex(r"15n - 150 \geq 450 \;\Rightarrow\; n \geq 40").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex(r"The fortieth vetkoek lands the target — dot filled").scale(0.9).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex(r"Translate, solve, answer in the story's language").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.wait(4)
