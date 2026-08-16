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

# Band layout: one frame-height band per teaching beat; the camera moves down
# to fresh space and earlier work stays on the canvas. Only exporter-supported
# mobjects; every line of working is a single-string MathTex revealed with
# Write — no sub-part transforms.
#
# Mirrors script.md across all seven subtopics (Part 1 — Expert: 1-4;
# Part 2 — Simplifier: 5-7), band time roughly proportional to subtopics.json
# (220/230/250/250/180/190/170 of 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ScaleFactorKSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display holds while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): stretch one dimension — volume follows
        title = Tex("The Effect of a Scale Factor $k$").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\text{Box } 4 \times 3 \times 2: \; V = 24, \; A = 52").scale(1.1).shift(UP * 1.0)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"Double the height only: $4 \times 3 \times 4$").scale(1.1).shift(UP * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"V = 48 = 2 \times 24").scale(1.15).shift(DOWN * 0.9)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex(r"One dimension $\times\, k$: volume $\times\, k$").scale(1.1).shift(DOWN * 2.0)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): surface area refuses to be tidy
        self.next_band(1)
        b1_title = Tex("Surface area breaks the pattern").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"A_{\text{new}} = 2(12 + 16 + 12) = 80").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_wrong = MathTex(r"80 = 2 \times 52").scale(1.1).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l2 = Tex(r"Top and bottom never felt the stretch;").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        b1_l3 = Tex(r"the four sides doubled — no clean factor").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_rule = Tex("One dimension moved? Recompute $A$ honestly").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_rule))
        self.wait(3)

        # --- Band 2 (subtopic_2): the radius counts twice
        self.next_band(2)
        b2_title = Tex(r"Cylinder $r=5$, $h=12$: $V = 300\pi$").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Double } h: \; \pi \times 25 \times 24 = 600\pi").scale(1.05).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Double } r: \; \pi \times 100 \times 12 = 1200\pi").scale(1.05).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"1200\pi = 4 \times 300\pi \;\; \text{(not 2!)}").scale(1.1).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex(r"$r$ is squared — it enters the product twice").scale(1.05).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the governing principle
        self.next_band(3)
        b3_title = Tex("One $k$ for every appearance").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex(r"$h$ in $\pi r^2 h$: once, so $k$").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex(r"$r$ in $\pi r^2 h$: twice, so $k^2$").scale(1.1).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Triple } r: \; \pi \times 225 \times 12 = 2700\pi = 9V").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"Radius $\times 3$ means volume $\times 9$ — say why").scale(1.05).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): scale everything — k squared and k cubed
        self.next_band(4)
        b4_title = Tex(r"All dimensions doubled: $8 \times 6 \times 4$").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"V = 192 = 8 \times 24, \quad 8 = 2^3").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"A = 2(48+32+24) = 208 = 4 \times 52").scale(1.05).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"4 = 2^2 \; \text{ — every face scaled the same}").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex(r"Works for ANY solid — box, cone, statue").scale(1.05).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the full pattern and the 10 percent trap
        self.next_band(5)
        b5_l1 = MathTex(r"\text{lengths} \times k, \;\; \text{areas} \times k^2, \;\; \text{volumes} \times k^3").scale(0.85).shift(band_shift(5) + UP * 2.0)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(3)
        b5_l2 = Tex(r"Ten percent bigger: $k = 1{,}1$").scale(1.1).shift(band_shift(5) + UP * 0.8)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"V: \; 1{,}1^3 = 1{,}331 \; \to \; +33{,}1\%").scale(1.1).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"A: \; 1{,}1^2 = 1{,}21 \; \to \; +21\%").scale(1.1).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex(r"Not $+30\%$ — scale factors multiply, never add").scale(1.0).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): reverse gear — extract k first
        self.next_band(6)
        b6_title = Tex("Reverse gear: the change gives you $k$").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = MathTex(r"V \times 27: \; k^3 = 27 \Rightarrow k = 3").scale(1.1).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{then } A \times k^2 = 9").scale(1.1).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"\text{Balloon: } A \times 4: \; k^2 = 4 \Rightarrow k = 2").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"V \times k^3 = 8").scale(1.1).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_rule = Tex("Never jump area $\\to$ volume without passing $k$").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_rule))
        self.wait(3)

        # --- Band 7 (subtopic_4): the error museum
        self.next_band(7)
        b7_title = Tex("The error museum").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_w1 = Tex(r"Double all dimensions: volume doubles").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_w1))
        self.play(Create(strike(b7_w1)))
        self.wait(2)
        b7_l1 = Tex(r"It multiplies by $2^3 = 8$").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex(r"One dimension moved? One $k$ only, not $k^3$").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Percentages: $10\%$ each is $+33{,}1\%$ on $V$,").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        b7_l4 = Tex(r"never $+30\%$ — factors multiply").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): one brick, then a wall of doubles
        self.next_band(8)
        b8_title = Tex("One brick, then a wall of doubles").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Brick $4 \times 3 \times 2$: 24 unit cubes inside").scale(1.05).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex(r"Twice as tall = a second brick on top: 48").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Twice as big EVERYWHERE: $2 \times 2 \times 2$ bricks").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"Eight bricks — not two, not four").scale(1.1).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex(r"Tripled everywhere? $3 \times 3 \times 3 = 27$ bricks").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): paint grows slower than water
        self.next_band(9)
        b9_title = Tex("Paint grows slower than water").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Water inside = volume; paint outside = area").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{Double: water} \times 8, \;\; \text{paint} \times 4").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{Triple: water} \times 27, \;\; \text{paint} \times 9").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex(r"Paint scales by $k^2$, water by $k^3$").scale(1.1).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex(r"$10\%$: paint $+21\%$, water $+33{,}1\%$").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): working backwards without panic
        self.next_band(10)
        b10_title = Tex("Working backwards: cross the bridge at $k$").scale(1.05).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"1. Name the change: $V \to k^3$, $A \to k^2$").scale(1.05).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex(r"2. Undo the power with the matching root").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{Tank: } k^3 = 27 \Rightarrow k = 3").scale(1.1).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = MathTex(r"\text{Paint: } k^2 = 9 \text{ times more}").scale(1.1).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex(r"Check: enlargement means $k > 1$, and $k^3$ beats $k^2$").scale(0.95).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(4)
