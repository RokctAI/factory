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

# Band-layout whiteboard scene for the Municipal Tariffs and Rising Block
# Systems session duo. Part 1 — Expert: subtopics 1-4 (what a tariff is,
# rising block electricity, water and the free allowance, comparing two
# systems). Part 2 — Simplifier: subtopics 5-7 retell the staircase, the
# free kilolitres and the cheaper-deal decision. Durations
# 215/215/225/230/195/195/195 of 1470 s. Exporter-safe mobjects only;
# add-only lifecycle; camera moves down one band per teaching beat.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MunicipalTariffsRisingBlockSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic display while intro.md plays (~4-5% of scene).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): what a tariff is ---
        title = Tex("Municipal Tariffs and Rising Blocks").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Tariff: a price per unit used").scale(1.05).shift(UP * 1.1)
        b0_l2 = Tex("Flat: every unit the same price").scale(1.0).shift(UP * 0.2)
        b0_l3 = Tex("Rising block: each block costs more").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = Tex("Fixed charge: payable even at zero use").scale(1.0).shift(DOWN * 1.7)
        b0_l5 = Tex("Then VAT at 15\\% on the total").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(b0_l1)); self.wait(2)
        self.play(Write(b0_l2)); self.wait(2)
        self.play(Write(b0_l3)); self.wait(2)
        self.play(Write(b0_l4)); self.wait(2)
        self.play(Write(b0_l5)); self.wait(3)

        # --- Band 1 (subtopic_2): rising block electricity ---
        self.next_band(1)
        b1_title = Tex("420 kWh through the blocks").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Block 1: } 150 \times 1,95 = 292,50").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\text{Block 2: } 270 \times 2,45 = 661,50").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"\text{Total: } 292,50 + 661,50 = 954,00").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"\text{Wrong: } 420 \times 2,45 = 1\;029 \; (+75)").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        b1_l5 = Tex("Block 2 holds 300 units: 450 minus 150").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b1_l4)); self.wait(2)
        self.play(Write(b1_l5)); self.wait(3)

        # --- Band 2 (subtopic_3): water and the free allowance ---
        self.next_band(2)
        b2_title = Tex("26 kl through the water blocks").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{First 6 kl: free}").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"14 \times 16,80 = 235,20").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"6 \times 29,50 = 177,00").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"\text{Subtotal } 412,20; \; \text{VAT } 61,83").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = MathTex(r"\text{Payable: } 474,03").scale(1.1).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l1)); self.wait(2)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3)); self.wait(2)
        self.play(Write(b2_l4)); self.wait(2)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_4): comparing two systems ---
        self.next_band(3)
        b3_title = Tex("Prepaid vs conventional").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"420: \; 954 \text{ vs } 798 + 250 = 1\;048").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("Prepaid wins by R94").scale(1.0).shift(band_shift(3) + UP * 0.2)
        b3_l3 = MathTex(r"650: \; 1\;597,50 \text{ vs } 1\;235 + 250 = 1\;485").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("Conventional wins by R112,50").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        b3_l5 = Tex("Break-even: where the cost lines cross").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l1)); self.wait(2.5)
        self.play(Write(b3_l2)); self.wait(2)
        self.play(Write(b3_l3)); self.wait(2.5)
        self.play(Write(b3_l4)); self.wait(2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 4 (subtopic_5): the staircase of prices ---
        self.next_band(4)
        b4_title = Tex("The staircase of prices").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2.5)
        s1 = Rectangle(width=2.2, height=0.6).shift(band_shift(4) + LEFT * 3.0 + DOWN * 1.8)
        s2 = Rectangle(width=2.2, height=0.6).shift(band_shift(4) + LEFT * 0.8 + DOWN * 1.2)
        s3 = Rectangle(width=2.2, height=0.6).shift(band_shift(4) + RIGHT * 1.4 + DOWN * 0.6)
        l1 = MathTex(r"1,95").scale(0.8).shift(band_shift(4) + LEFT * 3.0 + DOWN * 1.8)
        l2 = MathTex(r"2,45").scale(0.8).shift(band_shift(4) + LEFT * 0.8 + DOWN * 1.2)
        l3 = MathTex(r"2,85").scale(0.8).shift(band_shift(4) + RIGHT * 1.4 + DOWN * 0.6)
        self.play(Create(s1), Write(l1)); self.wait(2)
        self.play(Create(s2), Write(l2)); self.wait(2)
        self.play(Create(s3), Write(l3)); self.wait(2)
        b4_l1 = Tex("Climbing never re-prices the steps below").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"292,50 + 661,50 = 954 \; (\text{not } 1\;029)").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(3)
        self.play(Write(b4_l2)); self.wait(3.5)

        # --- Band 5 (subtopic_6): the first six kilolitres ---
        self.next_band(5)
        b5_title = Tex("The first six kilolitres").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2.5)
        b5_l1 = Tex("Bottom step: free — six thousand litres").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"14 \text{ kl} \times 16,80 + 6 \text{ kl} \times 29,50").scale(1.0).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"412,20 + \text{VAT } 61,83 = 474,03").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex("A leak wastes TOP-step water: R200+ a month").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l1)); self.wait(3)
        self.play(Write(b5_l2)); self.wait(3)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(3)
        self.play(Write(b5_l4)); self.wait(3.5)

        # --- Band 6 (subtopic_7): which deal is cheaper for you ---
        self.next_band(6)
        b6_title = Tex("Which deal is cheaper for you").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2.5)
        b6_l1 = MathTex(r"420 \text{ units: prepaid } 954 < 1\;048").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"650 \text{ units: conventional } 1\;485 < 1\;597,50").scale(0.95).shift(band_shift(6) + UP * 0.2)
        b6_l3 = Tex("Fixed fee: bad for small users, good for big").scale(0.95).shift(band_shift(6) + DOWN * 0.8)
        # two crossing cost lines
        ax = Line(band_shift(6) + DOWN * 2.6 + LEFT * 4.0, band_shift(6) + DOWN * 2.6 + RIGHT * 4.0)
        lineA = Line(band_shift(6) + DOWN * 2.5 + LEFT * 3.6, band_shift(6) + DOWN * 1.3 + RIGHT * 3.6)
        lineB = Line(band_shift(6) + DOWN * 2.0 + LEFT * 3.6, band_shift(6) + DOWN * 1.6 + RIGHT * 3.6, color=YELLOW)
        self.play(Write(b6_l1)); self.wait(3)
        self.play(Write(b6_l2)); self.wait(3)
        self.play(Write(b6_l3)); self.wait(3)
        self.play(Create(ax))
        self.play(Create(lineA), Create(lineB))
        d = Dot(band_shift(6) + DOWN * 1.72 + RIGHT * 1.2, color=RED)
        self.play(Create(d))
        self.wait(4)
