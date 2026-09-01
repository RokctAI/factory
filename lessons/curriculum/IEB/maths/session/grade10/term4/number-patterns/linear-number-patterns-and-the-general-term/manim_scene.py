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
# (215/240/230/255/180/190/175 of 1485 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LinearNumberPatternsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): finding the steady step
        title = Tex("Linear Number Patterns and the General Term").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"4; \; 9; \; 14; \; 19; \; \ldots").scale(1.2).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"9-4 = 5, \quad 14-9 = 5, \quad 19-14 = 5").scale(1.05).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"\text{Constant difference: } d = 5").scale(1.1).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex(r"$T_1 = 4$, $T_2 = 9$, $T_n$ = term in position $n$").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): falling patterns and the impostor
        self.next_band(1)
        b1_title = Tex("Test EVERY gap, in the right order").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"50; \; 43; \; 36: \quad 43 - 50 = -7").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Negative $d$ is legal — the pattern descends").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_wrong = MathTex(r"1; \; 3; \; 9: \quad \text{linear with } d = 2").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l3 = Tex(r"Second gap is 6 — it multiplies, not adds").scale(1.05).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_rule = Tex(r"Always later term minus earlier term").scale(1.05).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_rule))
        self.wait(3)

        # --- Band 2 (subtopic_2): constructing the general term
        self.next_band(2)
        b2_title = Tex("The five times table, slid down by one").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"5; 10; 15; 20 \;\to\; 4; 9; 14; 19 \; (-1)").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Adjustment} = T_1 - d = 4 - 5 = -1").scale(1.1).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"T_n = 5n - 1").scale(1.25).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = MathTex(r"\text{Verify } T_3: \; 5(3) - 1 = 14 \; \checkmark").scale(1.05).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the falling pattern and the straight line
        self.next_band(3)
        b3_title = Tex(r"Falling pattern: $50; 43; 36$").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"d = -7, \quad T_1 - d = 50 - (-7) = 57").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"T_n = -7n + 57").scale(1.15).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"\text{Verify } T_2: \; -14 + 57 = 43 \; \checkmark").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"LINEAR: the plotted points form a straight line").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        b3_l5 = Tex(r"with gradient $d$ — one idea, two costumes").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): forwards and backwards
        self.next_band(4)
        b4_title = Tex("The two-direction machine").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Forward: } T_{60} = 5(60) - 1 = 299").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = Tex(r"Backward: which term equals 124?").scale(1.05).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"5n - 1 = 124").scale(1.1).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"5n = 125 \;\Rightarrow\; n = 25").scale(1.1).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_rule = Tex(r"A backward answer is a POSITION — a natural number").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_rule))
        self.wait(3)

        # --- Band 5 (subtopic_3): membership — is 163 a term?
        self.next_band(5)
        b5_title = Tex("Is 163 a term of the sequence?").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"5n - 1 = 163").scale(1.1).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"5n = 164 \;\Rightarrow\; n = \tfrac{164}{5} = 32{,}8").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Positions are whole — nothing between 32 and 33").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"163 is NOT a term: $n$ is not a natural number").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_rule = Tex(r"The broken $n$ IS the proof").scale(1.05).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_rule))
        self.wait(3)

        # --- Band 6 (subtopic_4): matchstick triangles
        self.next_band(6)
        b6_title = Tex("Hidden patterns: matchstick triangles").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"3; \; 5; \; 7 \quad (d = 2)").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex(r"Each triangle borrows a side: 2 new matches").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"T_n = 2n + 1 \quad (3 - 2 = 1)").scale(1.1).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"\text{Figure 30: } T_{30} = 61 \text{ matches}").scale(1.1).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): tables, fees and the classic failures
        self.next_band(7)
        b7_title = Tex("Tables, fees and the classic failures").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Tables seat } 6; 10; 14: \; T_n = 4n + 2").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"4n + 2 = 50 \;\Rightarrow\; n = 12 \text{ tables}").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex(r"Plumber: R60 call-out $+$ R40/h $\to T_n = 40n + 60$").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_w1 = MathTex(r"T_n = dn + T_1").scale(1.05).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_w1))
        self.play(Create(strike(b7_w1)))
        self.wait(1.5)
        b7_l4 = Tex(r"Adjustment is $T_1$ MINUS $d$ — verify to catch it").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the parcel price's heartbeat
        self.next_band(8)
        b8_title = Tex("The parcel price that climbs step by step").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Kilograms: } 14; \; 20; \; 26 \text{ rand}").scale(1.1).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"20 - 14 = 6, \quad 26 - 20 = 6").scale(1.1).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Every gap the same: the heartbeat is $d = 6$").scale(1.05).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex(r"Always later price minus earlier price").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): a times table with a top-up
        self.next_band(9)
        b9_title = Tex("A times table with a top-up").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"6; 12; 18 \;\to\; 14; 20; 26 \; (+8)").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{Price} = 6n + 8 \quad (14 - 6 = 8)").scale(1.1).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{20 kg: } 6(20) + 8 = \text{R}128").scale(1.05).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"\text{Paid R92: } 6n + 8 = 92 \Rightarrow n = 14").scale(1.05).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_rule = Tex(r"Forward: substitute. Backward: solve.").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_rule))
        self.wait(3)

        # --- Band 10 (subtopic_7): can a parcel cost exactly R75?
        self.next_band(10)
        b10_title = Tex("Can a parcel cost exactly R75?").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"6n + 8 = 75").scale(1.1).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = MathTex(r"6n = 67 \;\Rightarrow\; n = \tfrac{67}{6} = 11{,}17...").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Kilograms are whole: no parcel costs exactly R75").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex(r"Whole $n$: member. Broken $n$: outsider.").scale(1.05).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex(r"Check gaps; build $dn +$ top-up; test; verdict").scale(0.95).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(4)
