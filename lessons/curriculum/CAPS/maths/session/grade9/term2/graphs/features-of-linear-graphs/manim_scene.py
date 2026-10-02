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
    """Four-quadrant axes centred on origin, drawn from primitives."""
    g = VGroup()
    g.add(Line(origin + LEFT * half_w, origin + RIGHT * half_w, color=WHITE))
    g.add(Line(origin + DOWN * half_h, origin + UP * half_h, color=WHITE))
    return g


def seg(origin, p, q, s=0.6, color=BLUE):
    """Line through two scaled points (x; y)."""
    return Line(origin + RIGHT * p[0] * s + UP * p[1] * s,
                origin + RIGHT * q[0] * s + UP * q[1] * s, color=color, stroke_width=4)


def pt(origin, p, s=0.6, color=YELLOW):
    return Dot(origin + RIGHT * p[0] * s + UP * p[1] * s, radius=0.08, color=color)


def staircase(origin, p, run, rise, s=0.6, color=GREEN):
    """Rise-over-run triangle from point p: across first, then up."""
    a = origin + RIGHT * p[0] * s + UP * p[1] * s
    b = a + RIGHT * run * s
    c = b + UP * rise * s
    return VGroup(Line(a, b, color=color, stroke_width=3), Line(b, c, color=color, stroke_width=3))


class LinearFeaturesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): y-intercept
        title = Tex("Features of a linear graph: $y = 2x + 1$").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        o0 = np.array([-3.8, -0.4, 0])
        ax0 = cart_axes(o0, half_w=2.8, half_h=2.4)
        self.play(Create(ax0))
        line0 = seg(o0, (-2.5, -4), (1.5, 4), s=0.5)
        self.play(Create(line0))
        yint = pt(o0, (0, 1), s=0.5)
        self.play(Create(yint))
        l1 = MathTex(r"x = 0: \; y = 2(0) + 1 = 1 \;\Rightarrow\; (0;\,1)").scale(0.9).shift(RIGHT * 2.8 + UP * 1.2)
        l2 = MathTex(r"y = mx + c: \; c \text{ is the } y\text{-intercept}").scale(0.9).shift(RIGHT * 2.8 + UP * 0.3)
        l3 = MathTex(r"2y = 4x + 6 \;\Rightarrow\; y = 2x + 3 \;\Rightarrow\; c = 3").scale(0.85).shift(RIGHT * 2.8 + DOWN * 0.6)
        l4 = Tex("Taxi $12k + 20$: the flag fee R20 is the starting value.").scale(0.75).shift(RIGHT * 2.8 + DOWN * 1.5)
        for m in (l1, l2, l3, l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(l1, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_2): x-intercept
        self.next_band(1)
        b1_title = Tex("The $x$-intercept: set $y = 0$ and solve").scale(1.1).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_title))
        self.wait(1.5)
        o1 = band_shift(1) + np.array([-3.8, -0.6, 0])
        ax1 = cart_axes(o1, half_w=2.8, half_h=2.2)
        self.play(Create(ax1))
        line1 = seg(o1, (-1, -9), (4, 6), s=0.3, color=ORANGE)
        self.play(Create(line1))
        xint = pt(o1, (2, 0), s=0.3)
        self.play(Create(xint))
        b1_l1 = MathTex(r"y = 3x - 6: \; 0 = 3x - 6 \;\Rightarrow\; 3x = 6 \;\Rightarrow\; x = 2 \;\Rightarrow\; (2;\,0)").scale(0.8).shift(band_shift(1) + RIGHT * 2.6 + UP * 1.2)
        b1_l2 = MathTex(r"y = 2x + 1: \; 0 = 2x + 1 \;\Rightarrow\; x = -\tfrac{1}{2} \;\Rightarrow\; (-\tfrac{1}{2};\,0)").scale(0.8).shift(band_shift(1) + RIGHT * 2.6 + UP * 0.2)
        b1_l3 = Tex("$y$-intercept: $x = 0$, on the vertical axis.").scale(0.8).shift(band_shift(1) + RIGHT * 2.6 + DOWN * 0.7)
        b1_l4 = Tex("$x$-intercept: $y = 0$, on the horizontal axis.").scale(0.8).shift(band_shift(1) + RIGHT * 2.6 + DOWN * 1.5)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): gradient
        self.next_band(2)
        b2_title = Tex("Gradient: rise over run between any two points").scale(1.05).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_title))
        self.wait(1.5)
        o2 = band_shift(2) + np.array([-3.8, -1.0, 0])
        ax2 = cart_axes(o2, half_w=2.8, half_h=2.4)
        self.play(Create(ax2))
        line2 = seg(o2, (-1, -1), (2.5, 6), s=0.45)
        self.play(Create(line2))
        st = staircase(o2, (0, 1), 2, 4, s=0.45)
        self.play(Create(st))
        p_a = pt(o2, (0, 1), s=0.45)
        p_b = pt(o2, (2, 5), s=0.45)
        self.play(Create(p_a), Create(p_b))
        b2_l1 = MathTex(r"m = \frac{5 - 1}{2 - 0} = \frac{4}{2} = 2").scale(1.0).shift(band_shift(2) + RIGHT * 2.8 + UP * 1.3)
        b2_l2 = MathTex(r"m = \frac{y_2 - y_1}{x_2 - x_1} \quad\text{same order top and bottom}").scale(0.85).shift(band_shift(2) + RIGHT * 2.8 + UP * 0.3)
        b2_l3 = MathTex(r"y = -2x + 4: \; m = -2 \;\text{(falls)} \qquad y = 4: \; m = 0").scale(0.85).shift(band_shift(2) + RIGHT * 2.8 + DOWN * 0.6)
        b2_l4 = Tex("Taxi: gradient 12 is R12 per kilometre, the rate.").scale(0.8).shift(band_shift(2) + RIGHT * 2.8 + DOWN * 1.5)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): all three from a drawn line
        self.next_band(3)
        b3_title = Tex("All three features from two points").scale(1.1).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_title))
        self.wait(1.5)
        o3 = band_shift(3) + np.array([-3.8, -0.4, 0])
        ax3 = cart_axes(o3, half_w=2.8, half_h=2.4)
        self.play(Create(ax3))
        line3 = seg(o3, (-0.5, -4), (3.5, 4), s=0.5, color=GREEN)
        self.play(Create(line3))
        q1 = pt(o3, (0, -3), s=0.5)
        q2 = pt(o3, (3, 3), s=0.5)
        self.play(Create(q1), Create(q2))
        b3_l1 = MathTex(r"(0;\,-3),\;(3;\,3): \; c = -3,\quad m = \frac{3 - (-3)}{3 - 0} = \frac{6}{3} = 2").scale(0.8).shift(band_shift(3) + RIGHT * 2.8 + UP * 1.2)
        b3_l2 = MathTex(r"y = 2x - 3 \qquad 0 = 2x - 3 \;\Rightarrow\; x = 1{,}5").scale(0.9).shift(band_shift(3) + RIGHT * 2.8 + UP * 0.2)
        b3_l3 = Tex("Table: $(0;-3), (1;-1), (2;1), (3;3)$ --- difference 2 is the gradient.").scale(0.7).shift(band_shift(3) + RIGHT * 2.6 + DOWN * 0.7)
        b3_l4 = Tex("Pick grid-intersection points. Check the sign against the picture.").scale(0.75).shift(band_shift(3) + RIGHT * 2.6 + DOWN * 1.6)
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
        b4_l1 = MathTex(r"m = \frac{\text{run}}{\text{rise}} = \frac{2}{4} = \tfrac{1}{2}").scale(0.95).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("Positive gradient for a line that falls").scale(0.95).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"2y = 4x + 6 \;\Rightarrow\; c = 6").scale(0.95).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"m = \frac{y}{x} \;\text{from one point}").scale(0.95).shift(band_shift(4) + DOWN * 1.7)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the wall
        self.next_band(5)
        b5_title = Tex("Where the line crosses the wall").scale(1.15).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_title))
        self.wait(2)
        o5 = band_shift(5) + np.array([-4.2, -1.8, 0])
        wall = Line(o5, o5 + UP * 3.8, color=WHITE, stroke_width=6)
        floor = Line(o5, o5 + RIGHT * 5.0, color=WHITE, stroke_width=6)
        self.play(Create(wall), Create(floor))
        fare_line = Line(o5 + UP * 20 * 0.025, o5 + RIGHT * 4.6 + UP * 130 * 0.025, color=BLUE, stroke_width=4)
        self.play(Create(fare_line))
        wdot = Dot(o5 + UP * 20 * 0.025, radius=0.08, color=YELLOW)
        self.play(Create(wdot))
        b5_l1 = Tex("At the wall you have not moved: $x = 0$.").scale(0.8).shift(band_shift(5) + RIGHT * 2.8 + UP * 1.3)
        b5_l2 = Tex("Taxi: R20 on the meter before you move. Fare $= 12k + 20$.").scale(0.75).shift(band_shift(5) + RIGHT * 2.8 + UP * 0.4)
        b5_l3 = MathTex(r"y = 2x + 1 \;\Rightarrow\; (0;\,1) \qquad y = 3x - 6 \;\Rightarrow\; (0;\,-6)").scale(0.8).shift(band_shift(5) + RIGHT * 2.8 + DOWN * 0.5)
        b5_l4 = Tex("The number on its own, once $y$ is alone on the left.").scale(0.75).shift(band_shift(5) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): the staircase
        self.next_band(6)
        b6_title = Tex("Steps up for each step across").scale(1.15).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_title))
        self.wait(2)
        o6 = band_shift(6) + np.array([-3.8, -1.0, 0])
        ax6 = cart_axes(o6, half_w=2.8, half_h=2.4)
        self.play(Create(ax6))
        line6 = seg(o6, (-1, -1), (2.5, 6), s=0.45)
        self.play(Create(line6))
        st6a = staircase(o6, (0, 1), 1, 2, s=0.45)
        st6b = staircase(o6, (1, 3), 1, 2, s=0.45)
        self.play(Create(st6a), Create(st6b))
        b6_l1 = Tex("Up 4, across 2: gradient $4 \\div 2 = 2$. Up first, then across.").scale(0.75).shift(band_shift(6) + RIGHT * 2.8 + UP * 1.3)
        b6_l2 = Tex("Downhill is negative: $y = -2x + 4$ has gradient $-2$.").scale(0.75).shift(band_shift(6) + RIGHT * 2.8 + UP * 0.4)
        b6_l3 = Tex("Flat is 0. Same gradient means parallel.").scale(0.8).shift(band_shift(6) + RIGHT * 2.8 + DOWN * 0.5)
        b6_l4 = Tex("Gradient is the rate: R12 per km, $-25$ litres per minute.").scale(0.75).shift(band_shift(6) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): the floor
        self.next_band(7)
        b7_title = Tex("Where the line hits the floor").scale(1.15).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_title))
        self.wait(2)
        o7 = band_shift(7) + np.array([-3.8, -0.6, 0])
        ax7 = cart_axes(o7, half_w=2.8, half_h=2.2)
        self.play(Create(ax7))
        line7 = seg(o7, (-1, -9), (4, 6), s=0.3, color=ORANGE)
        self.play(Create(line7))
        fdot = pt(o7, (2, 0), s=0.3)
        self.play(Create(fdot))
        b7_l1 = Tex("On the floor the height is zero: $y = 0$.").scale(0.8).shift(band_shift(7) + RIGHT * 2.8 + UP * 1.3)
        b7_l2 = MathTex(r"0 = 3x - 6 \;\Rightarrow\; x = 2 \qquad 0 = 2x + 1 \;\Rightarrow\; x = -0{,}5").scale(0.8).shift(band_shift(7) + RIGHT * 2.8 + UP * 0.4)
        b7_l3 = Tex("Pairs with the zero showing: $(2;\\,0)$ floor, $(0;\\,-6)$ wall.").scale(0.75).shift(band_shift(7) + RIGHT * 2.8 + DOWN * 0.5)
        b7_l4 = Tex("Wall, staircase, floor: $y$-intercept, gradient, $x$-intercept.").scale(0.8).shift(band_shift(7) + RIGHT * 2.8 + DOWN * 1.4)
        for m in (b7_l1, b7_l2, b7_l3):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
