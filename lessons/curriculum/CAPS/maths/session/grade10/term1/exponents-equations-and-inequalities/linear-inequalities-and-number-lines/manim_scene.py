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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing removed.
# Write-only reveals on single-string Tex/MathTex keep the export clean; the
# number lines are hand-built from Line/Arrow/Dot/Circle/Tex (the only
# exporter-supported shapes). Bands cover all seven subtopics (Part 1 —
# Expert: 1-4; Part 2 — Simplifier: 5-7), dwell time proportional to
# subtopics.json (235/220/210/250/195/185/200 of 1495 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LinearInequalitiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): solve like an equation
        title = Tex("Linear Inequalities and Number Lines").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        l1 = Tex(r"$<, \; >, \; \leq, \; \geq$: the bar includes the boundary").scale(1.0).shift(UP * 0.9)
        self.play(Write(l1))
        self.wait(2)
        l2 = MathTex(r"3x - 5 \leq 7").scale(1.15).shift(DOWN * 0.1)
        l3 = MathTex(r"3x \leq 12").scale(1.15).shift(DOWN * 1.0)
        l4 = MathTex(r"x \leq 4 \quad \text{(divided by } +3\text{: no flip)}").scale(1.1).shift(DOWN * 1.9)
        self.play(Write(l2))
        self.wait(2)
        self.play(Write(l3))
        self.wait(2)
        self.play(Write(l4))
        self.play(Create(SurroundingRectangle(l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the flip rule
        self.next_band(1)
        b1_title = Tex("The one exception: negatives flip the sign").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"5 > 3, \;\text{ but }\; -5 < -3").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"-2x > 6").scale(1.15).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"x < -3 \quad \text{(divided by } -2\text{: FLIP)}").scale(1.1).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = MathTex(r"\text{Test } x = -4: \; -2(-4) = 8 > 6 \;\checkmark").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex(r"No-flip road: $-6 > 2x \Rightarrow -3 > x$").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the number-line sketch
        self.next_band(2)
        b2_title = Tex("The sketch: solid dot in, open dot out").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        # number line for x <= 4: solid dot at 4, shade left
        nl1 = Line(LEFT * 4.5, RIGHT * 4.5).shift(band_shift(2) + UP * 0.8)
        self.play(Create(nl1))
        b2_lab1 = MathTex(r"4").scale(0.9).shift(band_shift(2) + UP * 0.3 + RIGHT * 2.0)
        tick1 = Line(UP * 0.15, DOWN * 0.15).shift(band_shift(2) + UP * 0.8 + RIGHT * 2.0)
        self.play(Create(tick1), Write(b2_lab1))
        dot1 = Dot(radius=0.12, color=YELLOW).shift(band_shift(2) + UP * 0.8 + RIGHT * 2.0)
        self.play(Create(dot1))
        shade1 = Arrow(RIGHT * 2.0, LEFT * 4.3, buff=0, color=YELLOW, stroke_width=8).shift(band_shift(2) + UP * 0.8)
        self.play(Create(shade1))
        b2_cap1 = MathTex(r"x \leq 4: \text{ solid dot, shade left}").scale(1.0).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(b2_cap1))
        self.wait(2.5)
        # number line for x < -3: open dot
        nl2 = Line(LEFT * 4.5, RIGHT * 4.5).shift(band_shift(2) + DOWN * 1.3)
        self.play(Create(nl2))
        b2_lab2 = MathTex(r"-3").scale(0.9).shift(band_shift(2) + DOWN * 1.8 + LEFT * 1.0)
        tick2 = Line(UP * 0.15, DOWN * 0.15).shift(band_shift(2) + DOWN * 1.3 + LEFT * 1.0)
        self.play(Create(tick2), Write(b2_lab2))
        circ2 = Circle(radius=0.12, color=YELLOW).shift(band_shift(2) + DOWN * 1.3 + LEFT * 1.0)
        self.play(Create(circ2))
        shade2 = Arrow(LEFT * 1.15, LEFT * 4.3, buff=0, color=YELLOW, stroke_width=8).shift(band_shift(2) + DOWN * 1.3)
        self.play(Create(shade2))
        b2_cap2 = MathTex(r"x < -3: \text{ open dot, shade left}").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_cap2))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): interval notation
        self.next_band(3)
        b3_title = Tex("Interval notation").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Round bracket excludes; square bracket includes").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"Infinity is never reached: always round").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"x \leq 4: \quad x \in (-\infty\,;\; 4\,]").scale(1.1).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = MathTex(r"x < -3: \quad x \in (-\infty\,;\; -3)").scale(1.1).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex(r"Smaller value on the left; state $x \in \mathbb{R}$").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): compound inequality
        self.next_band(4)
        b4_title = Tex(r"Solve: $-3 < 2x + 1 \leq 7$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex("Operate on all THREE parts at once").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"-4 < 2x \leq 6 \quad (\text{subtract } 1)").scale(1.1).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"-2 < x \leq 3 \quad (\text{divide by } +2)").scale(1.1).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        # segment number line
        nl4 = Line(LEFT * 4.5, RIGHT * 4.5).shift(band_shift(4) + DOWN * 1.8)
        self.play(Create(nl4))
        c4 = Circle(radius=0.12, color=YELLOW).shift(band_shift(4) + DOWN * 1.8 + LEFT * 1.5)
        d4 = Dot(radius=0.12, color=YELLOW).shift(band_shift(4) + DOWN * 1.8 + RIGHT * 1.5)
        seg4 = Line(LEFT * 1.38, RIGHT * 1.38, color=YELLOW, stroke_width=8).shift(band_shift(4) + DOWN * 1.8)
        lab4a = MathTex(r"-2").scale(0.9).shift(band_shift(4) + DOWN * 2.4 + LEFT * 1.5)
        lab4b = MathTex(r"3").scale(0.9).shift(band_shift(4) + DOWN * 2.4 + RIGHT * 1.5)
        self.play(Create(c4), Create(d4), Write(lab4a), Write(lab4b))
        self.play(Create(seg4))
        b4_l4 = MathTex(r"x \in (-2\,;\; 3\,]").scale(1.05).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l4))
        self.wait(2.5)

        # --- Band 5 (subtopic_4): the vetkoek word problem
        self.next_band(5)
        b5_title = Tex("Market stall: profit of at least R300").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"R120 table rental; vetkoek at R12 each").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = MathTex(r"12n - 120 \geq 300").scale(1.1).shift(band_shift(5) + UP * 0.3)
        b5_l3 = MathTex(r"12n \geq 420").scale(1.1).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = MathTex(r"n \geq 35").scale(1.15).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(1.5)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex(r"In context: at least 35 vetkoek (whole number)").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): translation table + trap museum
        self.next_band(6)
        b6_title = Tex("The translation table").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"``at least'' / ``no less than'': $\geq$").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"``at most'' / ``no more than'': $\leq$").scale(1.0).shift(band_shift(6) + UP * 0.5)
        b6_l3 = Tex(r"``more than'': $>$ \quad ``fewer than'': $<$").scale(1.0).shift(band_shift(6) + DOWN * 0.2)
        self.play(Write(b6_l1))
        self.wait(1.5)
        self.play(Write(b6_l2))
        self.wait(1.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_t1 = Tex(r"Traps: no flip on $\div$ negative; flipping on $-$;").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        b6_t2 = Tex(r"solid dot without the bar; algebra with no sentence").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_t1))
        self.play(Write(b6_t2))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): debt flips everything
        self.next_band(7)
        b7_title = Tex("Debt turns everything upside down").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"R500 in pocket beats R300 in pocket").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"Owing R500 is WORSE than owing R300").scale(1.0).shift(band_shift(7) + UP * 0.4)
        b7_l3 = MathTex(r"500 > 300 \;\text{ but }\; -500 < -300").scale(1.05).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = MathTex(r"-2x > 6 \;\Rightarrow\; x < -3").scale(1.1).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        b7_l5 = Tex(r"Then test one number: $x=-4$ works, $x=0$ fails").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # --- Band 8 (subtopic_6): dots and shading
        self.next_band(8)
        b8_title = Tex("Eighteen and over — or over eighteen?").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"``and over'' lets the 18-year-old in: solid dot").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"``over 18'' leaves her outside: open dot").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        nl8 = Line(LEFT * 4.5, RIGHT * 4.5).shift(band_shift(8) + DOWN * 0.7)
        self.play(Create(nl8))
        d8 = Dot(radius=0.12, color=YELLOW).shift(band_shift(8) + DOWN * 0.7 + RIGHT * 1.5)
        lab8 = MathTex(r"4").scale(0.9).shift(band_shift(8) + DOWN * 1.3 + RIGHT * 1.5)
        shade8 = Arrow(RIGHT * 1.5, LEFT * 4.3, buff=0, color=YELLOW, stroke_width=8).shift(band_shift(8) + DOWN * 0.7)
        self.play(Create(d8), Write(lab8))
        self.play(Create(shade8))
        b8_l3 = MathTex(r"x \leq 4: \;\; (-\infty\,;\; 4\,] \;\text{ — square = invited}").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l3))
        b8_l4 = Tex(r"Whole numbers only? Separate dots, no shading").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l4))
        self.wait(2.5)

        # --- Band 9 (subtopic_7): fences and the vetkoek test
        self.next_band(9)
        b9_title = Tex("Between two fences").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"-3 < 2x + 1 \leq 7").scale(1.05).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"-4 < 2x \leq 6 \;\Rightarrow\; -2 < x \leq 3").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2)
        b9_l3 = Tex(r"Hollow gate at $-2$, closed-in guest at $3$").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"12n - 120 \geq 300 \;\Rightarrow\; n \geq 35").scale(1.05).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex(r"35 vetkoek at R12 is R420; minus R120 = R300 exactly").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(4)
