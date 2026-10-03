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


def cart_axes(origin, half_w=3.0, half_h=2.6):
    g = VGroup()
    g.add(Line(origin + LEFT * half_w, origin + RIGHT * half_w, color=WHITE))
    g.add(Line(origin + DOWN * half_h, origin + UP * half_h, color=WHITE))
    return g


def seg(origin, p, q, s=0.5, color=BLUE):
    return Line(origin + RIGHT * p[0] * s + UP * p[1] * s,
                origin + RIGHT * q[0] * s + UP * q[1] * s, color=color, stroke_width=4)


def pt(origin, p, s=0.5, color=YELLOW):
    return Dot(origin + RIGHT * p[0] * s + UP * p[1] * s, radius=0.08, color=color)


def staircase(origin, p, run, rise, s=0.5, color=GREEN):
    a = origin + RIGHT * p[0] * s + UP * p[1] * s
    b = a + RIGHT * run * s
    c = b + UP * rise * s
    return VGroup(Line(a, b, color=color, stroke_width=3), Line(b, c, color=color, stroke_width=3))


class LinearEquationsGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): table of values
        title = Tex("Drawing $y = 2x - 1$ from a table").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        o0 = np.array([-3.6, -0.4, 0])
        self.play(Create(cart_axes(o0, half_w=2.8, half_h=2.4)))
        for p in [(-1, -3), (0, -1), (1, 1)]:
            self.play(Create(pt(o0, p, s=0.5)), run_time=0.5)
        self.play(Create(seg(o0, (-1.8, -4.6), (2.2, 3.4), s=0.5)))
        l1 = MathTex(r"x = -1: \; 2(-1) - 1 = -3 \qquad x = 0: \; -1 \qquad x = 1: \; 1").scale(0.8).shift(RIGHT * 2.8 + UP * 1.2)
        l2 = MathTex(r"(-1;\,-3),\;(0;\,-1),\;(1;\,1) \;\text{line up: difference } 2").scale(0.8).shift(RIGHT * 2.8 + UP * 0.3)
        l3 = Tex("Third point is the check. Rule, arrowheads, label.").scale(0.78).shift(RIGHT * 2.8 + DOWN * 0.6)
        l4 = Tex("$y = \\tfrac{1}{2}x + 3$: use $x = -2, 0, 2$ to clear the fraction.").scale(0.75).shift(RIGHT * 2.8 + DOWN * 1.5)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): intercepts and gradient
        self.next_band(1)
        b1_title = Tex("Two intercepts, or $c$ then the staircase $m$").scale(1.05).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        o1 = band_shift(1) + np.array([-3.6, -0.8, 0])
        self.play(Create(cart_axes(o1, half_w=2.8, half_h=2.4)))
        self.play(Create(pt(o1, (0, 4), s=0.5)), Create(pt(o1, (2, 0), s=0.5)))
        self.play(Create(seg(o1, (-0.8, 5.6), (3.2, -2.4), s=0.5, color=ORANGE)))
        self.play(Create(staircase(o1, (0, 4), 1, -2, s=0.5)))
        b1_l1 = MathTex(r"y = -2x + 4: \; (0;\,4) \text{ and } 0 = -2x + 4 \Rightarrow (2;\,0)").scale(0.8).shift(band_shift(1) + RIGHT * 2.8 + UP * 1.3)
        b1_l2 = Tex("Or start at $c = 4$, step 1 across and 2 DOWN.").scale(0.8).shift(band_shift(1) + RIGHT * 2.8 + UP * 0.4)
        b1_l3 = Tex("Through the origin ($y = 3x$): plot $(0;0)$ and $(1;3)$.").scale(0.75).shift(band_shift(1) + RIGHT * 2.8 + DOWN * 0.5)
        b1_l4 = Tex("$y = 3$: horizontal. \\quad $x = -2$: vertical.").scale(0.8).shift(band_shift(1) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): equation from a drawn line
        self.next_band(2)
        b2_title = Tex("From the picture to $y = mx + c$").scale(1.15).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_title))
        self.wait(1.5)
        o2 = band_shift(2) + np.array([-3.6, -0.4, 0])
        self.play(Create(cart_axes(o2, half_w=2.8, half_h=2.4)))
        self.play(Create(seg(o2, (-0.6, -4.2), (3.6, 4.2), s=0.5, color=GREEN)))
        self.play(Create(pt(o2, (0, -3), s=0.5)), Create(pt(o2, (3, 3), s=0.5)))
        self.play(Create(staircase(o2, (0, -3), 3, 6, s=0.5, color=YELLOW)))
        b2_l1 = MathTex(r"c = -3 \qquad m = \frac{3 - (-3)}{3 - 0} = \frac{6}{3} = 2").scale(0.9).shift(band_shift(2) + RIGHT * 2.8 + UP * 1.3)
        b2_l2 = MathTex(r"y = 2x - 3 \qquad \text{check } (1;\,-1): \; 2(1) - 3 = -1 \;\checkmark").scale(0.8).shift(band_shift(2) + RIGHT * 2.8 + UP * 0.4)
        b2_l3 = MathTex(r"(-2;\,0),(0;\,4): \; y = 2x + 4 \;\text{(parallel)} \qquad (0;\,5),(5;\,0): \; y = -x + 5").scale(0.72).shift(band_shift(2) + RIGHT * 2.6 + DOWN * 0.5)
        b2_l4 = Tex("Falling line: $m$ negative. Verify with a third point.").scale(0.78).shift(band_shift(2) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_4): two points, c not visible
        self.next_band(3)
        b3_title = Tex("Two points, $y$-intercept not shown").scale(1.1).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"(1;\,5),\;(3;\,9): \; m = \frac{9 - 5}{3 - 1} = \frac{4}{2} = 2").scale(0.95).shift(band_shift(3) + UP * 1.3)
        b3_l2 = MathTex(r"5 = 2(1) + c \;\Rightarrow\; c = 3 \;\Rightarrow\; y = 2x + 3 \qquad \text{check: } 2(3) + 3 = 9 \;\checkmark").scale(0.85).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"(2;\,1),\;(4;\,-3): \; m = \frac{-3 - 1}{4 - 2} = -2, \quad 1 = -4 + c \Rightarrow c = 5 \Rightarrow y = -2x + 5").scale(0.8).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("Layout: $c$ and its point, $m$ with two points, the equation, a verification.").scale(0.78).shift(band_shift(3) + DOWN * 1.7)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(1.5)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Two table points only; the slip goes unseen").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("$y = -2x + 4$ stepped upward").scale(0.95).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"m = \frac{\text{run}}{\text{rise}}").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = Tex("$y = 3$ drawn through the origin with gradient 3").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): three dots and a ruler
        self.next_band(5)
        b5_title = Tex("Three dots and a ruler").scale(1.2).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_title))
        self.wait(2)
        o5 = band_shift(5) + np.array([-3.6, -0.4, 0])
        self.play(Create(cart_axes(o5, half_w=2.8, half_h=2.4)))
        for p in [(-1, -3), (0, -1), (1, 1)]:
            self.play(Create(pt(o5, p, s=0.5)), run_time=0.5)
        self.play(Create(seg(o5, (-1.8, -4.6), (2.2, 3.4), s=0.5)))
        b5_l1 = Tex("Pick $x = -1, 0, 1$. Feed each into the machine.").scale(0.8).shift(band_shift(5) + RIGHT * 2.8 + UP * 1.3)
        b5_l2 = Tex("Hall then lift for each dot. Do they line up?").scale(0.8).shift(band_shift(5) + RIGHT * 2.8 + UP * 0.4)
        b5_l3 = Tex("Third dot is free insurance.").scale(0.8).shift(band_shift(5) + RIGHT * 2.8 + DOWN * 0.5)
        b5_l4 = Tex("Ruler, arrows past the ends, formula written beside.").scale(0.78).shift(band_shift(5) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): wall then staircase
        self.next_band(6)
        b6_title = Tex("Start on the wall, step the staircase").scale(1.15).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_title))
        self.wait(2)
        o6 = band_shift(6) + np.array([-3.6, -0.6, 0])
        self.play(Create(cart_axes(o6, half_w=2.8, half_h=2.4)))
        self.play(Create(pt(o6, (0, -1), s=0.5)))
        self.play(Create(staircase(o6, (0, -1), 1, 2, s=0.5)))
        self.play(Create(staircase(o6, (1, 1), 1, 2, s=0.5)))
        self.play(Create(seg(o6, (-1.5, -4), (2.5, 4), s=0.5)))
        b6_l1 = Tex("$y = 2x - 1$: wall at $-1$, then 1 across, 2 up. Twice.").scale(0.78).shift(band_shift(6) + RIGHT * 2.8 + UP * 1.3)
        b6_l2 = Tex("$y = -2x + 4$: wall at 4, then 1 across, 2 DOWN.").scale(0.78).shift(band_shift(6) + RIGHT * 2.8 + UP * 0.4)
        b6_l3 = Tex("$m = \\tfrac{1}{2}$: 2 across, 1 up.").scale(0.8).shift(band_shift(6) + RIGHT * 2.8 + DOWN * 0.5)
        b6_l4 = Tex("Flat line for $y = 3$; upright line for $x = -2$.").scale(0.78).shift(band_shift(6) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): read the line backwards
        self.next_band(7)
        b7_title = Tex("Read the line backwards").scale(1.2).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_title))
        self.wait(2)
        o7 = band_shift(7) + np.array([-3.6, -0.4, 0])
        self.play(Create(cart_axes(o7, half_w=2.8, half_h=2.4)))
        self.play(Create(seg(o7, (-0.6, -4.2), (3.6, 4.2), s=0.5, color=GREEN)))
        self.play(Create(pt(o7, (0, -3), s=0.5)), Create(pt(o7, (3, 3), s=0.5)))
        self.play(Create(staircase(o7, (0, -3), 3, 6, s=0.5, color=YELLOW)))
        b7_l1 = Tex("Wall: $c = -3$. Staircase: up 6, across 3, $m = 2$.").scale(0.78).shift(band_shift(7) + RIGHT * 2.8 + UP * 1.3)
        b7_l2 = MathTex(r"y = 2x - 3 \qquad (1;\,-1): \; 2(1) - 3 = -1 \;\checkmark").scale(0.8).shift(band_shift(7) + RIGHT * 2.8 + UP * 0.4)
        b7_l3 = Tex("No wall crossing shown? Put one dot into $y = mx + c$ for $c$.").scale(0.72).shift(band_shift(7) + RIGHT * 2.8 + DOWN * 0.5)
        b7_l4 = Tex("Three dots and a ruler. Wall then staircase. One more dot.").scale(0.75).shift(band_shift(7) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
