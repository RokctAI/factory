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

# Band-layout whiteboard scene for "Free Fall — Equations and Graphs"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only: graphs are hand-built from Arrow axes and
# chained Line segments (no Axes/Polygon/Arc). Write-only reveals.
# Subtopic durations 230/235/240/230/185/190/190 of 1500 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FreeFallEquationsGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definition + the three equations ---
        title = Tex("Free Fall: Equations and Graphs").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_def = Tex("Projectile: gravity is the ONLY force").scale(1.05).shift(UP * 1.2)
        b0_g = MathTex(r"a = 9{,}8\ \text{m·s}^{-2}\ \text{down, always}").scale(1.05).shift(UP * 0.3)
        self.play(Write(b0_def))
        self.wait(2)
        self.play(Write(b0_g))
        self.wait(2)
        b0_e1 = MathTex(r"v_f = v_i + a\,\Delta t").scale(1.1).shift(DOWN * 0.7)
        b0_e2 = MathTex(r"\Delta y = v_i\,\Delta t + \tfrac{1}{2} a\,\Delta t^2").scale(1.1).shift(DOWN * 1.6)
        b0_e3 = MathTex(r"v_f^2 = v_i^2 + 2a\,\Delta y").scale(1.1).shift(DOWN * 2.5)
        self.play(Write(b0_e1))
        self.wait(2)
        self.play(Write(b0_e2))
        self.wait(2)
        self.play(Write(b0_e3))
        self.wait(2)
        b0_rule = Tex("Declare the sign convention first").scale(1.0).shift(DOWN * 3.3)
        self.play(Write(b0_rule))
        self.wait(3)

        # --- Band 1 (subtopic_1): hammer dropped from 44,1 m ---
        self.next_band(1)
        b1_title = Tex("Hammer dropped from 44,1 m (down $= +$)").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l0 = Tex(r"``Dropped'' means $v_i = 0$").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l0))
        self.wait(2)
        b1_l1 = MathTex(r"\Delta y = v_i\,\Delta t + \tfrac{1}{2} a\,\Delta t^2").scale(1.05).shift(band_shift(1) + UP * 0.3)
        b1_l2 = MathTex(r"44{,}1 = 0 + \tfrac{1}{2}(9{,}8)\,\Delta t^2").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        b1_l3 = MathTex(r"\Delta t^2 = \tfrac{44{,}1}{4{,}9} = 9").scale(1.05).shift(band_shift(1) + DOWN * 1.5)
        b1_l3b = MathTex(r"\Delta t = 3\ \text{s}").scale(1.05).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l3b))
        self.play(Create(SurroundingRectangle(b1_l3b, color=GREEN)))
        self.wait(2)
        b1_l4 = MathTex(r"v_f = 9{,}8 \times 3 = 29{,}4\ \text{m·s}^{-1}\ \text{down}").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): thrown up at 29,4 — top of flight ---
        self.next_band(2)
        b2_title = Tex("Thrown up at 29,4 (up $= +$, $a = -9{,}8$)").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_fact = Tex("At the top: $v = 0$ BUT $a = 9{,}8$ down").scale(1.05).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_fact))
        self.play(Create(SurroundingRectangle(b2_fact, color=GREEN)))
        self.wait(2.5)
        b2_l1 = MathTex(r"0 = 29{,}4 + (-9{,}8)\,\Delta t").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l2 = MathTex(r"\Delta t = 3\ \text{s to the top}").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"0 = 29{,}4^2 - 2(9{,}8)\,\Delta y").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        b2_l4 = MathTex(r"\Delta y = \frac{864{,}36}{19{,}6} = 44{,}1\ \text{m}").scale(1.05).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): symmetry + distance vs displacement ---
        self.next_band(3)
        b3_title = Tex("Symmetry: the free gift").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Time up $=$ time down: total 6 s").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"Returns at 29,4 m$\cdot$s$^{-1}$, now downward").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Only if it lands at the starting height!").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Up 44,1 and back: distance 88,2 m").scale(1.05).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex("but displacement $= 0$").scale(1.05).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): v-t and a-t graphs, hand-built axes ---
        self.next_band(4)
        b4_title = Tex("Velocity-time (up $= +$, thrown at 29,4)").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        o4 = band_shift(4) + LEFT * 4.5 + DOWN * 0.4
        ax4_t = Arrow(o4 + LEFT * 0.3, o4 + RIGHT * 6.5, buff=0, stroke_width=3)
        ax4_v = Arrow(o4 + DOWN * 2.2, o4 + UP * 2.2, buff=0, stroke_width=3)
        lab4_t = Tex("$t$ (s)").scale(0.9).shift(o4 + RIGHT * 6.8 + DOWN * 0.4)
        lab4_v = Tex("$v$").scale(0.9).shift(o4 + UP * 2.2 + LEFT * 0.5)
        self.play(Create(ax4_t), Create(ax4_v))
        self.play(Write(lab4_t), Write(lab4_v))
        self.wait(1.5)
        vline = Line(o4 + UP * 1.8, o4 + RIGHT * 5.6 + DOWN * 1.8, color=YELLOW)
        self.play(Create(vline))
        self.wait(1.5)
        top_dot = Dot(o4 + RIGHT * 2.8, color=RED)
        lab_top = Tex("top: $v = 0$ at 3 s").scale(0.85).shift(o4 + RIGHT * 3.3 + UP * 0.7)
        self.play(FadeIn(top_dot), Write(lab_top))
        self.wait(2)
        lab_start = MathTex(r"+29{,}4").scale(0.8).shift(o4 + UP * 1.8 + LEFT * 0.8)
        lab_end = MathTex(r"-29{,}4").scale(0.8).shift(o4 + RIGHT * 5.6 + DOWN * 2.2)
        self.play(Write(lab_start), Write(lab_end))
        self.wait(2)
        b4_note = Tex("$a$-$t$: flat line at 9,8 down, entire flight").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_note))
        self.wait(3)

        # --- Band 5 (subtopic_3): the bouncing ball sawtooth ---
        self.next_band(5)
        b5_title = Tex("Bouncing ball, down $= +$").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        o5 = band_shift(5) + LEFT * 4.5 + DOWN * 0.2
        ax5_t = Arrow(o5 + LEFT * 0.3, o5 + RIGHT * 6.8, buff=0, stroke_width=3)
        ax5_v = Arrow(o5 + DOWN * 1.9, o5 + UP * 2.1, buff=0, stroke_width=3)
        lab5_t = Tex("$t$").scale(0.9).shift(o5 + RIGHT * 7.0 + DOWN * 0.3)
        lab5_v = Tex("$v$").scale(0.9).shift(o5 + UP * 2.1 + LEFT * 0.5)
        self.play(Create(ax5_t), Create(ax5_v))
        self.play(Write(lab5_t), Write(lab5_v))
        self.wait(1.5)
        s1 = Line(o5, o5 + RIGHT * 1.8 + UP * 1.8, color=YELLOW)
        j1 = Line(o5 + RIGHT * 1.8 + UP * 1.8, o5 + RIGHT * 1.9 + DOWN * 1.3, color=RED)
        s2 = Line(o5 + RIGHT * 1.9 + DOWN * 1.3, o5 + RIGHT * 4.5 + UP * 1.3, color=YELLOW)
        j2 = Line(o5 + RIGHT * 4.5 + UP * 1.3, o5 + RIGHT * 4.6 + DOWN * 0.9, color=RED)
        s3 = Line(o5 + RIGHT * 4.6 + DOWN * 0.9, o5 + RIGHT * 6.4 + UP * 0.9, color=YELLOW)
        self.play(Create(s1))
        self.wait(1.5)
        self.play(Create(j1))
        self.wait(1.5)
        self.play(Create(s2))
        self.play(Create(j2))
        self.play(Create(s3))
        self.wait(2)
        b5_l1 = Tex("Plunge $=$ floor strike; smaller each time").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        b5_l2 = Tex("All teeth parallel: gradient 9,8 always").scale(1.0).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three read-out rules + area example ---
        self.next_band(6)
        b6_title = Tex("Reading numbers off the graphs").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_r1 = Tex("Gradient of $y$-$t$ graph $=$ velocity").scale(1.05).shift(band_shift(6) + UP * 1.2)
        b6_r2 = Tex("Gradient of $v$-$t$ graph $=$ acceleration").scale(1.05).shift(band_shift(6) + UP * 0.3)
        b6_r3 = Tex("Area under $v$-$t$ graph $=$ displacement").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_r1))
        self.wait(2)
        self.play(Write(b6_r2))
        self.wait(2)
        self.play(Write(b6_r3))
        self.wait(2)
        b6_l1 = MathTex(r"\text{0 to 3 s: } \tfrac{1}{2} \times 3 \times 29{,}4 = 44{,}1\ \text{m}").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = Tex("3 to 6 s: $-44{,}1$; total displacement $0$").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l2))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): gravity's tax ---
        self.next_band(7)
        b7_title = Tex("Gravity's tax: 9,8 every second").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"29{,}4 \rightarrow 19{,}6 \rightarrow 9{,}8 \rightarrow 0 \rightarrow 9{,}8\downarrow \rightarrow \dots").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("Three seconds up, three down: a mirror").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_wrong = Tex("At the top, $v = 0$ so $a = 0$").scale(1.05).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_rule = Tex("The tax office never closes: $a = 9{,}8$ down").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_rule))
        self.play(Create(SurroundingRectangle(b7_rule, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the ball's three diaries ---
        self.next_band(8)
        b8_title = Tex("The ball's diary: three graphs, one story").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        # Height diary: a small polyline arch (record of height, NOT a path).
        o8 = band_shift(8) + LEFT * 5.0 + DOWN * 0.1
        arch = VGroup(
            Line(o8, o8 + RIGHT * 0.7 + UP * 1.0, color=YELLOW),
            Line(o8 + RIGHT * 0.7 + UP * 1.0, o8 + RIGHT * 1.5 + UP * 1.5, color=YELLOW),
            Line(o8 + RIGHT * 1.5 + UP * 1.5, o8 + RIGHT * 2.3 + UP * 1.0, color=YELLOW),
            Line(o8 + RIGHT * 2.3 + UP * 1.0, o8 + RIGHT * 3.0, color=YELLOW),
        )
        self.play(Create(arch), run_time=2)
        lab8_h = Tex("height: an arch, not a path!").scale(0.9).shift(o8 + RIGHT * 1.5 + DOWN * 0.6)
        self.play(Write(lab8_h))
        self.wait(2)
        spd = Line(band_shift(8) + RIGHT * 1.5 + UP * 1.3, band_shift(8) + RIGHT * 5.0 + DOWN * 0.7, color=YELLOW)
        lab8_s = Tex("speed: ruler-straight").scale(0.9).shift(band_shift(8) + RIGHT * 3.2 + DOWN * 1.2)
        self.play(Create(spd))
        self.play(Write(lab8_s))
        self.wait(2)
        b8_l1 = Tex("Speed line hits zero exactly at the summit").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        b8_l2 = Tex("Gravity diary: flat at 9,8 down — that IS it").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(3)

        # --- Band 9 (subtopic_7): the bouncing ball without tears ---
        self.next_band(9)
        b9_title = Tex("The bouncing ball without tears").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Zero crossing $=$ a top of flight").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Vertical plunge $=$ a floor strike").scale(1.05).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("Each tooth shorter: bounces pay a toll").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_rule = Tex(r"Between bounces: $a = 9{,}8$ m$\cdot$s$^{-2}$ down").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_rule))
        self.play(Create(SurroundingRectangle(b9_rule, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("The parallel teeth are the proof").scale(1.05).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.wait(4)
