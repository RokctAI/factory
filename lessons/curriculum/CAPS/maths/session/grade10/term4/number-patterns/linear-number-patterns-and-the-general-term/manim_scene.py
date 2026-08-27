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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; every line of working is a single-string MathTex revealed with
# Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (215/245/230/255/180/190/175 of 1490 s).

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
        # --- Band 0 (subtopic_1): spotting the constant difference
        title = Tex("Linear Number Patterns and the General Term").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"5; \; 8; \; 11; \; 14; \; \ldots").scale(1.2).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"8-5 = 3, \quad 11-8 = 3, \quad 14-11 = 3").scale(1.05).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"\text{Constant difference: } d = 3").scale(1.1).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex(r"$T_1 = 5$, $T_2 = 8$, $T_n$ = term in position $n$").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): falling patterns and the impostor
        self.next_band(1)
        b1_title = Tex("Test EVERY gap, in the right order").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"20; \; 17; \; 14: \quad 17 - 20 = -3").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Negative $d$ is legal — the pattern descends").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_wrong = MathTex(r"2; \; 4; \; 8: \quad \text{linear with } d = 2").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l3 = Tex(r"Second gap is 4 — it multiplies, not adds").scale(1.05).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_rule = Tex(r"Always term after minus term before").scale(1.05).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_rule))
        self.wait(3)

        # --- Band 2 (subtopic_2): building the general term
        self.next_band(2)
        b2_title = Tex("The three times table, shifted up by two").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"3; 6; 9; 12 \;\to\; 5; 8; 11; 14 \; (+2)").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Correction} = T_1 - d = 5 - 3 = 2").scale(1.1).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"T_n = 3n + 2").scale(1.25).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = MathTex(r"\text{Verify } T_3: \; 3(3) + 2 = 11 \; \checkmark").scale(1.05).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the falling pattern and the straight line
        self.next_band(3)
        b3_title = Tex(r"Falling pattern: $20; 17; 14$").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"d = -3, \quad T_1 - d = 20 - (-3) = 23").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"T_n = -3n + 23").scale(1.15).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"\text{Verify } T_2: \; -6 + 23 = 17 \; \checkmark").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"LINEAR: the points march in a straight line").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        b3_l5 = Tex(r"with gradient $d$ — same maths, new clothes").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): forwards and backwards
        self.next_band(4)
        b4_title = Tex("The two-way machine").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{Forwards: } T_{50} = 3(50) + 2 = 152").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = Tex(r"Backwards: which term equals 92?").scale(1.05).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"3n + 2 = 92").scale(1.1).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"3n = 90 \;\Rightarrow\; n = 30").scale(1.1).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_rule = Tex(r"A backwards answer is a POSITION — a natural number").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_rule))
        self.wait(3)

        # --- Band 5 (subtopic_3): membership — is 100 a term?
        self.next_band(5)
        b5_title = Tex("Is 100 a term of the sequence?").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"3n + 2 = 100").scale(1.1).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"3n = 98 \;\Rightarrow\; n = \tfrac{98}{3} = 32{,}67...").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Positions are whole — nothing between 32 and 33").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex(r"100 is NOT a term: $n$ is not a natural number").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_rule = Tex(r"The non-whole $n$ IS the proof").scale(1.05).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_rule))
        self.wait(3)

        # --- Band 6 (subtopic_4): matchstick figures
        self.next_band(6)
        b6_title = Tex("Patterns in disguise: matchsticks").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"4; \; 7; \; 10 \quad (d = 3)").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex(r"Each square borrows a wall: 3 new matches").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"T_n = 3n + 1 \quad (4 - 3 = 1)").scale(1.1).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"\text{Figure 20: } T_{20} = 61 \text{ matches}").scale(1.1).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): tables, tariffs and the museum
        self.next_band(7)
        b7_title = Tex("Tables, tariffs and the error museum").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Tables seat } 4; 6; 8: \; T_n = 2n + 2").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"2n + 2 = 40 \;\Rightarrow\; n = 19 \text{ tables}").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex(r"Taxi: R30 flat $+$ R12/km $\to T_n = 12n + 30$").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_w1 = MathTex(r"T_n = dn + T_1").scale(1.05).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_w1))
        self.play(Create(strike(b7_w1)))
        self.wait(1.5)
        b7_l4 = Tex(r"Correction is $T_1$ MINUS $d$ — verify to catch it").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the taxi fare's heartbeat
        self.next_band(8)
        b8_title = Tex("The taxi fare that climbs in equal steps").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{Zones: } 12; \; 19; \; 26 \text{ rand}").scale(1.1).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = MathTex(r"19 - 12 = 7, \quad 26 - 19 = 7").scale(1.1).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Every gap the same: the heartbeat is $d = 7$").scale(1.05).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex(r"Always later price minus earlier price").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the times table wearing a jacket
        self.next_band(9)
        b9_title = Tex("The times table wearing a jacket").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"7; 14; 21 \;\to\; 12; 19; 26 \; (+5)").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{Fare} = 7n + 5 \quad (12 - 7 = 5)").scale(1.1).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{15 zones: } 7(15) + 5 = \text{R}110").scale(1.05).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"\text{Paid R61: } 7n + 5 = 61 \Rightarrow n = 8").scale(1.05).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_rule = Tex(r"Forwards: substitute. Backwards: solve.").scale(1.0).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_rule))
        self.wait(3)

        # --- Band 10 (subtopic_7): is ninety on the price list?
        self.next_band(10)
        b10_title = Tex("Is ninety on the price list?").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"7n + 5 = 90").scale(1.1).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = MathTex(r"7n = 85 \;\Rightarrow\; n = \tfrac{85}{7} = 12{,}14...").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Zones are whole: no trip costs exactly R90").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex(r"Whole $n$: member. Broken $n$: outsider.").scale(1.05).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex(r"Check gaps; build $dn +$ jacket; test; verdict").scale(0.95).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(4)
