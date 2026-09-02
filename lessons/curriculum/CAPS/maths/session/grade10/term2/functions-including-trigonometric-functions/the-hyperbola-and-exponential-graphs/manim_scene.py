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

# Band-layout whiteboard scene (see the quadratics-by-factorisation worked
# example). One band per teaching beat; the camera moves down to clean space
# and nothing is ever removed. Curves are drawn as short Line-segment chains
# and axes as Arrows (exporter-safe primitives only). Covers all seven
# subtopics of the duo (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# dwell times roughly proportional to subtopics.json
# (230/230/230/260/190/180/180 of 1500 s).

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


class HyperbolaExponentialSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): y = 6/x by table
        title = Tex(r"The Hyperbola: $y = \dfrac{6}{x}$").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"x: 1,\; 2,\; 3,\; 6,\; 12 \;\to\; y: 6,\; 3,\; 2,\; 1,\; \tfrac{1}{2}").scale(1.05).shift(UP * 1.1)
        b0_l2 = Tex(r"As $x$ grows, $y$ shrinks toward $0$ — never arrives").scale(1.0).shift(UP * 0.2)
        b0_l3 = MathTex(r"x = \tfrac{1}{2} \to y = 12, \quad x = \tfrac{1}{10} \to y = 60").scale(1.05).shift(DOWN * 0.7)
        b0_l4 = MathTex(r"x: -1,\; -2,\; -6 \;\to\; y: -6,\; -3,\; -1").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex(r"Two branches, mirrored through the origin").scale(1.05).shift(DOWN * 2.6)
        self.play(Write(b0_l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the picture, asymptotes and restrictions
        self.next_band(1)
        b1_title = Tex("Branches, asymptotes, restrictions").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        org = band_shift(1) + LEFT * 4.2 + DOWN * 0.5
        ax = VGroup(Arrow(org + LEFT * 2.2, org + RIGHT * 2.2, buff=0),
                    Arrow(org + DOWN * 2.2, org + UP * 2.4, buff=0))
        xlab = MathTex("x").scale(0.8).next_to(org + RIGHT * 2.2, DOWN, buff=0.1)
        ylab = MathTex("y").scale(0.8).next_to(org + UP * 2.4, RIGHT, buff=0.1)
        self.play(Create(ax), Write(xlab), Write(ylab))
        self.wait(1.5)
        u = 0.32
        br1 = polyline([(0.5, 6), (1, 3.2), (1.5, 2.1), (2.5, 1.3), (4, 0.8), (6, 0.5)], org, u)
        br2 = polyline([(-6, -0.5), (-4, -0.8), (-2.5, -1.3), (-1.5, -2.1), (-1, -3.2), (-0.5, -6)], org, u)
        self.play(Create(br1))
        self.wait(1.5)
        self.play(Create(br2))
        self.wait(2)
        f1 = Tex(r"Asymptotes: $x = 0$ and $y = 0$").scale(1.0).shift(band_shift(1) + RIGHT * 3.3 + UP * 1.2)
        f2 = Tex(r"Domain: $x \in \mathbb{R},\; x \neq 0$").scale(1.0).shift(band_shift(1) + RIGHT * 3.3 + UP * 0.3)
        f3 = Tex(r"Range: $y \in \mathbb{R},\; y \neq 0$").scale(1.0).shift(band_shift(1) + RIGHT * 3.3 + DOWN * 0.6)
        f4 = Tex(r"NO $y$-intercept — ever").scale(1.0).shift(band_shift(1) + RIGHT * 3.3 + DOWN * 1.5)
        self.play(Write(f1))
        self.wait(2)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(2)
        self.play(Write(f4))
        self.wait(2)
        f5 = Tex(r"$a > 0$: quadrants I, III; \quad $a < 0$: quadrants II, IV").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(f5))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): y = 6/x - 2 worked in full
        self.next_band(2)
        b2_title = Tex(r"Work $y = \dfrac{6}{x} - 2$ in full").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Asymptotes: $x = 0$ and $y = -2$ (it moved!)").scale(1.05).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex(r"Domain: $x \neq 0$; \; Range: $y \neq -2$").scale(1.05).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\frac{6}{x} = 2 \;\Rightarrow\; 6 = 2x \;\Rightarrow\; x = 3").scale(0.95).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex(r"$x$-intercept $(3; 0)$ — the shift created it").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = MathTex(r"x = 1 \to y = 4, \quad x = -1 \to y = -8").scale(1.05).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): the sketch, and reading the equation off it
        self.next_band(3)
        b3_title = Tex(r"Sketch of $y = \dfrac{6}{x} - 2$").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        org3 = band_shift(3) + LEFT * 4.2 + DOWN * 0.4
        ax3 = VGroup(Arrow(org3 + LEFT * 2.2, org3 + RIGHT * 2.4, buff=0),
                     Arrow(org3 + DOWN * 2.4, org3 + UP * 2.4, buff=0))
        u3 = 0.26
        asym3 = DashedLine(org3 + LEFT * 2.2 + UP * (-2) * u3, org3 + RIGHT * 2.4 + UP * (-2) * u3, color=BLUE)
        self.play(Create(ax3))
        self.play(Create(asym3), Write(MathTex(r"y = -2").scale(0.7).next_to(org3 + RIGHT * 2.4 + UP * (-2) * u3, DOWN, buff=0.1)))
        self.wait(2)
        br3a = polyline([(0.8, 5.5), (1, 4), (2, 1), (3, 0), (5, -0.8), (8, -1.25)], org3, u3)
        br3b = polyline([(-8, -2.75), (-5, -3.2), (-3, -4), (-1.5, -6), (-1, -8)], org3, u3)
        d1 = Dot(org3 + RIGHT * 3 * u3, radius=0.06)
        self.play(Create(br3a), Create(d1))
        self.wait(2)
        self.play(Create(br3b))
        self.wait(2)
        r1 = Tex(r"Read the equation off the graph:").scale(1.0).shift(band_shift(3) + RIGHT * 3.4 + UP * 1.0)
        r2 = Tex(r"asymptote $y = -2 \Rightarrow q = -2$").scale(1.0).shift(band_shift(3) + RIGHT * 3.4 + UP * 0.1)
        r3 = MathTex(r"(1; 4): \; 4 = \frac{a}{1} - 2 \Rightarrow a = 6").scale(1.0).shift(band_shift(3) + RIGHT * 3.4 + DOWN * 0.9)
        self.play(Write(r1))
        self.wait(2)
        self.play(Write(r2))
        self.wait(2)
        self.play(Write(r3))
        self.play(Create(SurroundingRectangle(r3, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): y = 2^x — the table and the features
        self.next_band(4)
        b4_title = Tex(r"The Exponential: $y = 2^x$").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"x: -3, -2, -1, 0, 1, 2, 3").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"y: \tfrac{1}{8}, \tfrac{1}{4}, \tfrac{1}{2}, 1, 2, 4, 8").scale(1.05).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Domain: $x \in \mathbb{R}$; \; Range: $y > 0$ STRICTLY").scale(1.05).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex(r"$y$-intercept: $b^0 = 1$, so $(0; 1)$ every time").scale(1.05).shift(band_shift(4) + DOWN * 1.5)
        b4_l5 = Tex(r"No $x$-intercept; asymptote $y = 0$ on the left").scale(1.05).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.wait(2.5)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): growth and decay side by side
        self.next_band(5)
        b5_title = Tex("Growth and decay").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        org5 = band_shift(5) + LEFT * 4.0 + DOWN * 0.9
        ax5 = VGroup(Arrow(org5 + LEFT * 2.4, org5 + RIGHT * 2.4, buff=0),
                     Arrow(org5 + DOWN * 0.4, org5 + UP * 3.0, buff=0))
        self.play(Create(ax5))
        u5 = 0.32
        growth = polyline([(-6, 0.02), (-3, 0.13), (-1, 0.5), (0, 1), (1, 2), (2, 4), (2.9, 7.5)], org5, u5)
        self.play(Create(growth), Create(Dot(org5 + UP * u5, radius=0.06)))
        self.wait(2)
        decay = polyline([(-2.9, 7.5), (-2, 4), (-1, 2), (0, 1), (1, 0.5), (3, 0.13), (6, 0.02)], org5, u5, color=ORANGE)
        self.play(Create(decay))
        self.wait(2)
        g5a = Tex(r"$y = 2^x$: rises — GROWTH ($b > 1$)").scale(1.0).shift(band_shift(5) + RIGHT * 3.4 + UP * 1.0)
        g5b = Tex(r"$y = \left(\tfrac{1}{2}\right)^x$: falls — DECAY ($0 < b < 1$)").scale(1.0).shift(band_shift(5) + RIGHT * 3.4 + UP * 0.0)
        g5c = Tex(r"Both pass through $(0; 1)$").scale(1.0).shift(band_shift(5) + RIGHT * 3.4 + DOWN * 1.0)
        self.play(Write(g5a))
        self.wait(2)
        self.play(Write(g5b))
        self.wait(2)
        self.play(Write(g5c))
        self.wait(2)
        g5d = Tex(r"$b \neq 1$ (a flat line) and $b > 0$ (no real value)").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(g5d))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): full sketch of y = 2^x - 4
        self.next_band(6)
        b6_title = Tex(r"Sketch $y = 2^x - 4$").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        s1 = Tex(r"Asymptote: $y = -4$").scale(1.0).shift(band_shift(6) + RIGHT * 3.4 + UP * 1.3)
        s2 = MathTex(r"x = 0: \; 2^0 - 4 = -3 \;\to\; (0; -3)").scale(0.95).shift(band_shift(6) + RIGHT * 3.4 + UP * 0.4)
        s3 = MathTex(r"y = 0: \; 2^x = 4 \Rightarrow x = 2 \;\to\; (2; 0)").scale(0.95).shift(band_shift(6) + RIGHT * 3.4 + DOWN * 0.5)
        s4 = Tex(r"Range: $y > -4$").scale(1.0).shift(band_shift(6) + RIGHT * 3.4 + DOWN * 1.4)
        org6 = band_shift(6) + LEFT * 4.0 + UP * 0.1
        u6 = 0.34
        ax6 = VGroup(Arrow(org6 + LEFT * 2.4, org6 + RIGHT * 2.4, buff=0),
                     Arrow(org6 + DOWN * 2.0, org6 + UP * 2.4, buff=0))
        asym6 = DashedLine(org6 + LEFT * 2.4 + DOWN * 4 * u6, org6 + RIGHT * 2.4 + DOWN * 4 * u6, color=BLUE)
        self.play(Create(ax6))
        self.play(Create(asym6))
        self.wait(1.5)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2.5)
        self.play(Write(s3))
        self.wait(2.5)
        curve6 = polyline([(-5, -3.97), (-3, -3.88), (-1, -3.5), (0, -3), (1, -2), (2, 0), (3, 4), (3.5, 7.3)], org6, u6)
        self.play(Create(curve6), Create(Dot(org6 + DOWN * 3 * u6, radius=0.06)), Create(Dot(org6 + RIGHT * 2 * u6, radius=0.06)))
        self.wait(2)
        self.play(Write(s4))
        self.play(Create(SurroundingRectangle(s4, color=GREEN)))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): negative a — y = -2^x + 8
        self.next_band(7)
        b7_title = Tex(r"Sketch $y = -2^x + 8$").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Asymptote: $y = 8$; $a < 0$ reflects the curve down").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = MathTex(r"x = 0: \; -1 + 8 = 7 \;\to\; (0; 7)").scale(1.05).shift(band_shift(7) + UP * 0.3)
        b7_l3 = MathTex(r"y = 0: \; 2^x = 8 \Rightarrow x = 3 \;\to\; (3; 0)").scale(1.05).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = Tex(r"Range: $y < 8$").scale(1.05).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.wait(2.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex(r"In from the left just under $y = 8$, through $(0; 7)$,").scale(0.95).shift(band_shift(7) + DOWN * 2.3)
        b7_l6 = Tex(r"crosses at $(3; 0)$, then plunges steeply").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2.5)

        # --- Band 8 (subtopic_4): the error museum
        self.next_band(8)
        b8_title = Tex("The error museum — five exhibits").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex(r"1. Asymptote $y = 0$ when $q \neq 0$ — it moved").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"2. A $y$-intercept for a hyperbola — it has none").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex(r"3. Range with $\geq$ instead of strictly $>$").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        b8_l4 = Tex(r"4. Confusing $2^x$ (never turns) with $x^2$ (turns)").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex(r"5. A curve touching its asymptote").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): sharing a fixed pot
        self.next_band(9)
        b9_title = Tex("Sharing a fixed pot: R120, split evenly").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"2 \to 60, \;\; 3 \to 40, \;\; 4 \to 30, \;\; 6 \to 20, \;\; 12 \to 10").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"More people, smaller share — fast, then gentle").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex(r"The share NEVER reaches zero").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = Tex(r"You cannot share among NOBODY").scale(1.05).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex(r"Two lines it never touches: the asymptotes").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): doubling every time
        self.next_band(10)
        b10_title = Tex("Doubling every time").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"1, 2, 4, 8, 16, 32 \dots \text{ (1000+ by round 10)}").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex(r"Backwards: $\tfrac{1}{2}, \tfrac{1}{4}, \tfrac{1}{8}$ — never zero").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Heights: strictly ABOVE zero, never ``zero or more''").scale(1.0).shift(band_shift(10) + DOWN * 0.7)
        b10_l4 = Tex(r"Zero rounds $\Rightarrow$ one teller: crosses at $1$").scale(1.05).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l3))
        self.wait(2.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex(r"Multiply by more than 1: climbs. By a fraction: falls").scale(0.95).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): asymptote first — the routine
        self.next_band(11)
        b11_title = Tex("Asymptote first — the sketching routine").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"1. Dashed line first: the number on its own is $q$").scale(1.0).shift(band_shift(11) + UP * 1.2)
        b11_l2 = Tex(r"2. $y$-intercept: put in $x = 0$ (hyperbola: skip!)").scale(1.0).shift(band_shift(11) + UP * 0.3)
        b11_l3 = Tex(r"3. $x$-intercept: set $y = 0$ and solve").scale(1.0).shift(band_shift(11) + DOWN * 0.6)
        b11_l4 = Tex(r"4. Extra points, then lean in — never land").scale(1.0).shift(band_shift(11) + DOWN * 1.5)
        self.play(Write(b11_l1))
        self.wait(2.5)
        self.play(Write(b11_l2))
        self.wait(2.5)
        self.play(Write(b11_l3))
        self.wait(2)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(2.5)
        b11_l5 = Tex(r"Ground floor or upstairs? $x^2$ turns; $2^x$ never does").scale(0.95).shift(band_shift(11) + DOWN * 2.6)
        self.play(Write(b11_l5))
        self.wait(4)
