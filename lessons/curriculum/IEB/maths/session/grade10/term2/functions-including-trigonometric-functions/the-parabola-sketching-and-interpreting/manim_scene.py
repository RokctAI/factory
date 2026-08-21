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

# Band-layout whiteboard scene. One band per teaching beat; the camera moves
# down to clean space and nothing is ever removed. Curves are drawn as short
# Line-segment chains and axes as Arrows (exporter-safe primitives only).
# Covers all seven subtopics of the duo (Part 1 — Expert: 1-4; Part 2 —
# Simplifier: 5-7), dwell times roughly proportional to subtopics.json
# (220/220/230/270/180/190/190 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    """World-space shift that places content in band k."""
    return DOWN * BAND * k


def polyline(points, origin, u, color=YELLOW):
    """Chain of Lines through graph-space points, scaled by u about origin."""
    segs = VGroup()
    for (x1, y1), (x2, y2) in zip(points[:-1], points[1:]):
        segs.add(Line(origin + RIGHT * x1 * u + UP * y1 * u,
                      origin + RIGHT * x2 * u + UP * y2 * u, color=color))
    return segs


PARA = [(-3, 9), (-2.5, 6.25), (-2, 4), (-1.5, 2.25), (-1, 1), (-0.5, 0.25),
        (0, 0), (0.5, 0.25), (1, 1), (1.5, 2.25), (2, 4), (2.5, 6.25), (3, 9)]


class ParabolaSketchingSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the mother function by table
        title = Tex(r"The Parabola: $y = ax^2 + q$").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Mother function: $y = x^2$").scale(1.15).shift(UP * 1.2)
        b0_l2 = MathTex(r"x: -3, -2, -1, 0, 1, 2, 3").scale(1.05).shift(UP * 0.3)
        b0_l3 = MathTex(r"y: \;\; 9, \;\; 4, \;\; 1, \; 0, \; 1, \; 4, \; 9").scale(1.05).shift(DOWN * 0.6)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex(r"$-2$ and $2$ both give $4$: squaring wipes out the sign").scale(1.0).shift(DOWN * 1.6)
        b0_l5 = Tex(r"A smooth curve — it rounds and turns, never a sharp V").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(b0_l4))
        self.wait(2.5)
        self.play(Write(b0_l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the picture and its vocabulary
        self.next_band(1)
        b1_title = Tex("The features, in the official words").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        org1 = band_shift(1) + LEFT * 4.4 + DOWN * 1.6
        ax1 = VGroup(Arrow(org1 + LEFT * 2.2, org1 + RIGHT * 2.2, buff=0),
                     Arrow(org1 + DOWN * 0.4, org1 + UP * 3.4, buff=0))
        self.play(Create(ax1))
        u1 = 0.33
        curve1 = polyline(PARA, org1, u1)
        self.play(Create(curve1), Create(Dot(org1, radius=0.06)))
        self.wait(2)
        f1 = Tex(r"Turning point: $(0; 0)$ — a MINIMUM").scale(1.0).shift(band_shift(1) + RIGHT * 3.2 + UP * 1.1)
        f2 = Tex(r"Axis of symmetry: $x = 0$").scale(1.0).shift(band_shift(1) + RIGHT * 3.2 + UP * 0.2)
        f3 = Tex(r"Domain: $x \in \mathbb{R}$").scale(1.0).shift(band_shift(1) + RIGHT * 3.2 + DOWN * 0.7)
        f4 = Tex(r"Range: $y \geq 0$ — in $y$, NEVER in $x$").scale(1.0).shift(band_shift(1) + RIGHT * 3.2 + DOWN * 1.6)
        self.play(Write(f1))
        self.wait(2)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(2)
        self.play(Write(f4))
        self.play(Create(SurroundingRectangle(f4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the effect of a
        self.next_band(2)
        b2_title = Tex(r"The effect of $a$ — stretch, squash, flip").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"$a > 0$: opens UP (smile), minimum").scale(1.05).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex(r"$a < 0$: opens DOWN (frown), maximum").scale(1.05).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"$y = 3x^2$: at $x = 2$, $y = 12$ — NARROWER").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = Tex(r"$y = \tfrac{1}{4}x^2$: at $x = 2$, $y = 1$ — WIDER").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex(r"$a$ never moves the turning point: it stays at $(0; 0)$").scale(0.95).shift(band_shift(2) + DOWN * 2.4)
        b2_l6 = Tex(r"$y = -3x^2$: range becomes $y \leq 0$").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l5))
        self.wait(2)
        self.play(Write(b2_l6))
        self.wait(2.5)

        # --- Band 3 (subtopic_3): the effect of q
        self.next_band(3)
        b3_title = Tex(r"The effect of $q$ — a pure vertical shift").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Turning point moves to $(0; q)$").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"The $y$-intercept IS $q$ — read it off the graph").scale(1.05).shift(band_shift(3) + UP * 0.3)
        b3_l3 = Tex(r"Axis of symmetry stays $x = 0$").scale(1.05).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"Range: $y \geq q$ (for $a > 0$), $y \leq q$ (for $a < 0$)").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): x-intercepts and the sign test
        self.next_band(4)
        b4_title = Tex(r"$x$-intercepts: set $y = 0$").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"y = x^2 - 16: \;\; x^2 = 16 \;\Rightarrow\; x = \pm 4").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"The $\pm$ is compulsory — two intercepts").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"y = x^2 + 5: \;\; x^2 = -5 \;\;\text{— no real solution}").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex(r"NO $x$-intercepts: lowest point already at $(0; 5)$").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex(r"$a, q$ same sign: no cut; opposite: cuts twice; $q = 0$: touches").scale(0.9).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): sketching y = 2x^2 - 8, five steps
        self.next_band(5)
        b5_title = Tex(r"Sketch $y = 2x^2 - 8$").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        s1 = Tex(r"1. $a = 2 > 0$: opens up, minimum").scale(0.95).shift(band_shift(5) + RIGHT * 3.3 + UP * 1.4)
        s2 = Tex(r"2. Turning point $(0; -8)$, axis $x = 0$").scale(0.95).shift(band_shift(5) + RIGHT * 3.3 + UP * 0.6)
        s3 = Tex(r"3. $y$-intercept: $y = -8$").scale(0.95).shift(band_shift(5) + RIGHT * 3.3 + DOWN * 0.2)
        s4 = MathTex(r"4.\; 2x^2 = 8 \Rightarrow x^2 = 4 \Rightarrow x = \pm 2").scale(0.95).shift(band_shift(5) + RIGHT * 3.3 + DOWN * 1.0)
        s5 = Tex(r"5. Domain $x \in \mathbb{R}$; range $y \geq -8$").scale(0.95).shift(band_shift(5) + RIGHT * 3.3 + DOWN * 1.8)
        org5 = band_shift(5) + LEFT * 4.2 + DOWN * 0.3
        u5 = 0.27
        ax5 = VGroup(Arrow(org5 + LEFT * 2.4, org5 + RIGHT * 2.4, buff=0),
                     Arrow(org5 + DOWN * 2.5, org5 + UP * 3.0, buff=0))
        self.play(Create(ax5))
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        self.play(Write(s3))
        self.wait(2)
        self.play(Write(s4))
        self.wait(2.5)
        curve5 = polyline([(-3, 10), (-2.5, 4.5), (-2, 0), (-1.5, -3.5), (-1, -6), (0, -8),
                           (1, -6), (1.5, -3.5), (2, 0), (2.5, 4.5), (3, 10)], org5, u5)
        dots5 = VGroup(Dot(org5 + DOWN * 8 * u5, radius=0.06),
                       Dot(org5 + LEFT * 2 * u5, radius=0.06),
                       Dot(org5 + RIGHT * 2 * u5, radius=0.06))
        self.play(Create(curve5), Create(dots5))
        self.wait(2)
        self.play(Write(s5))
        self.play(Create(SurroundingRectangle(s5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): reading the equation off a graph
        self.next_band(6)
        b6_title = Tex(r"Reverse: TP $(0; -5)$, through $(2; 7)$ — find $a, q$").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Turning point gives $q$ at once: $q = -5$").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"y = ax^2 - 5").scale(1.1).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"(2; 7): \;\; 7 = a(2)^2 - 5 = 4a - 5").scale(1.1).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = MathTex(r"4a = 12 \;\Rightarrow\; a = 3").scale(1.1).shift(band_shift(6) + DOWN * 1.6)
        b6_l5 = MathTex(r"y = 3x^2 - 5").scale(1.15).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the error museum
        self.next_band(7)
        b7_title = Tex("The error museum — five exhibits").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"1. Range written in $x$ instead of $y$").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"2. The $\pm$ dropped from $x^2 = 4$").scale(1.0).shift(band_shift(7) + UP * 0.3)
        b7_l3 = Tex(r"3. $q$ mistaken for a sideways shift").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = Tex(r"4. $0 < a < 1$ called ``smaller'' — say WIDER").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        b7_l5 = Tex(r"5. Forcing intercepts when $x^2 = $ negative: NONE exist").scale(0.95).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the shape of a thrown ball
        self.next_band(8)
        b8_title = Tex("The shape of a thrown ball").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Up, a weightless beat at the top, down — a mirror").scale(1.05).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"One turning moment; folded down the middle").scale(1.05).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"0 \to 0, \;\; \pm 1 \to 1, \;\; \pm 2 \to 4, \;\; \pm 3 \to 9").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"Allowed IN: anything (domain)").scale(1.05).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex(r"Comes OUT: never negative (range, in $y$)").scale(1.05).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): turning the bowl over and lifting it
        self.next_band(9)
        b9_title = Tex("Mixing bowl or pot lid?").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Sign of $a$: positive holds batter; negative covers leftovers").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"Size of $a$: big $=$ narrow vase; fraction $=$ wide platter").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex(r"$q$ carries the whole bowl: windowsill up, hole down").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = Tex(r"Free gift: $q$ is the $y$-crossing AND the turn height").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex(r"Bowl on the windowsill: no crossings. Bowl in a hole: two").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): four moves to a sketch
        self.next_band(10)
        b10_title = Tex("Four moves to a sketch").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"1. Which way up? Sign in front of $x^2$").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"2. The turn: the end number, on the vertical axis").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"3.\; 2x^2 - 8 = 0: \; x^2 = 4, \; x = 2 \text{ or } {-2}").scale(0.95).shift(band_shift(10) + DOWN * 0.6)
        b10_l4 = MathTex(r"4.\; x = 3: \; 2(9) - 8 = 10 \;\to\; (3; 10) \text{ and } (-3; 10)").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l3))
        self.wait(2.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex(r"Range in $y$; $q$ never slides sideways; $x^2 = -5$: none").scale(0.95).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l5))
        self.wait(4)
