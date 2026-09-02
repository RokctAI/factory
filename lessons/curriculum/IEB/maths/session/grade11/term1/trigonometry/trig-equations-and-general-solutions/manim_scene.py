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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; every line of working is a single-string MathTex revealed with
# Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (220/235/225/260/190/200/200 of 1530 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TrigEquationsGeneralSolutionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): one answer becomes infinitely many
        title = Tex("Trig Equations and General Solutions").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\sin x = 0{,}8: \quad \text{calculator says } 53{,}13^\circ").scale(0.95).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = MathTex(r"\text{Second quadrant: } 180^\circ - 53{,}13^\circ = 126{,}87^\circ").scale(0.95).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"413{,}13^\circ, \; -306{,}87^\circ, \ldots \text{ every turn repeats both}").scale(0.9).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex(r"Calculator once; quadrants double; period forever").scale(0.95).shift(DOWN * 2.1)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): sine and cosine general solutions
        self.next_band(1)
        b1_l1 = MathTex(r"\sin x = a: \;\; x = \alpha + k \cdot 360^\circ \text{ or } x = 180^\circ - \alpha + k \cdot 360^\circ").scale(0.8).shift(band_shift(1) + UP * 2.0)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"\cos x = a: \;\; x = \pm\alpha + k \cdot 360^\circ").scale(0.95).shift(band_shift(1) + UP * 1.0)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"2\cos x - \sqrt{3} = 0 \Rightarrow \cos x = \tfrac{\sqrt{3}}{2}").scale(0.95).shift(band_shift(1) + UP * 0.0)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"x = \pm 30^\circ + k \cdot 360^\circ").scale(1.0).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): negative value discipline
        self.next_band(2)
        b2_title = Tex(r"Solve $5\sin x + 2 = 0$").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\sin x = -0{,}4").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_wrong = MathTex(r"\sin^{-1}(-0{,}4) = -23{,}58^\circ \;\text{then quadrants too}").scale(0.9).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l2 = MathTex(r"\text{Reference from } +0{,}4: \; 23{,}58^\circ; \;\text{sine negative: Q3, Q4}").scale(0.85).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"x = 203{,}58^\circ + k \cdot 360^\circ \text{ or } x = 336{,}42^\circ + k \cdot 360^\circ").scale(0.85).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): tangent's short period
        self.next_band(3)
        b3_l1 = MathTex(r"\tan(180^\circ + \theta) = \tan\theta \;\Rightarrow\; \text{period } 180^\circ").scale(0.95).shift(band_shift(3) + UP * 2.0)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"\tan x = \sqrt{3}: \;\; x = 60^\circ + k \cdot 180^\circ").scale(1.0).shift(band_shift(3) + UP * 1.0)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"\tan x = -1{,}5: \; \text{ref } 56{,}31^\circ, \; \text{Q2: } 123{,}69^\circ").scale(0.9).shift(band_shift(3) + UP * 0.0)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"x = 123{,}69^\circ + k \cdot 180^\circ").scale(0.95).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): tidying with a defended division
        self.next_band(4)
        b4_title = Tex(r"Solve $\sqrt{3}\sin x = \cos x$").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\div \cos x: \quad \tan x = \tfrac{1}{\sqrt{3}}").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"x = 30^\circ + k \cdot 180^\circ").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = Tex(r"Defence: if $\cos x = 0$ then $\sin x = \pm 1$,").scale(0.9).shift(band_shift(4) + DOWN * 0.8)
        b4_l4 = Tex(r"giving $\pm\sqrt{3} = 0$ — impossible, so nothing lost").scale(0.9).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): harvesting an interval
        self.next_band(5)
        b5_title = Tex(r"$\cos x = 0{,}5$ on $[-360^\circ; 360^\circ]$").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"x = \pm 60^\circ + k \cdot 360^\circ").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"k = -1, 0, 1: \;\; -300^\circ, -60^\circ, 60^\circ, 300^\circ \;\; (420^\circ \text{ out})").scale(0.85).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Audit: 2 crossings per turn $\times$ 2 turns $= 4$ answers").scale(0.9).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the hidden quadratic
        self.next_band(6)
        b6_title = Tex(r"Solve $2\cos^2 x + \cos x - 1 = 0$, \; $x \in [0^\circ; 360^\circ]$").scale(0.9).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"c = \cos x: \;\; 2c^2 + c - 1 = (2c - 1)(c + 1) = 0").scale(0.9).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\cos x = \tfrac{1}{2}: \; 60^\circ, \; 300^\circ").scale(0.95).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"\cos x = -1: \; 180^\circ \;\text{(boundary — one door)}").scale(0.95).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"x = 60^\circ, \; 180^\circ, \; 300^\circ").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex(r"A value beyond $[-1; 1]$: reject in writing").scale(0.9).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the taxi on a loop
        self.next_band(7)
        b7_title = Tex("The taxi on a loop").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        loop = Circle(radius=1.3).shift(band_shift(7) + LEFT * 2.4 + DOWN * 0.3)
        gate = Dot(band_shift(7) + LEFT * 1.1 + DOWN * 0.3, color=YELLOW)
        self.play(Create(loop))
        self.play(Create(gate))
        self.wait(2)
        b7_l1 = Tex(r"Seen at 8:00, loop of 1 hour: passes at $8 + k$ hours").scale(0.85).shift(band_shift(7) + RIGHT * 1.9 + UP * 0.7)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"53{,}13^\circ + k \cdot 360^\circ: \; k \text{ is the lap counter}").scale(0.85).shift(band_shift(7) + RIGHT * 1.9 + DOWN * 0.4)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Tangent runs a half-length loop: $k \cdot 180^\circ$").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): two doors into the hall
        self.next_band(8)
        b8_title = Tex("Two doors into the hall").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Same height twice: once riding up, once riding down").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"\sin x = 0{,}8: \; 53{,}13^\circ \text{ and } 126{,}87^\circ").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\sin x = -0{,}4: \text{ size } 23{,}58^\circ, \text{ doors } 203{,}58^\circ, \; 336{,}42^\circ").scale(0.85).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"Extremes have ONE door: $\cos x = -1$ at $180^\circ$").scale(0.9).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): harvesting the stretch
        self.next_band(9)
        b9_title = Tex("Harvesting the stretch you were given").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\pm 60^\circ + k \cdot 360^\circ \text{ on } [-360^\circ; 360^\circ]").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{Keep: } -300^\circ, -60^\circ, 60^\circ, 300^\circ").scale(0.95).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = MathTex(r"c = \cos x: \; 2c^2 + c - 1 = 0 \;\text{— old homework}").scale(0.9).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex(r"Guard at the gate: $-1 \le \sin x, \cos x \le 1$, always").scale(0.9).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.wait(4)
