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

# Band-layout whiteboard scene for the Finance and Data Essentials revision
# session. One band per teaching beat; the camera moves down and earlier work
# stays on the canvas. Exporter-supported mobjects only; every working line is
# its own single-string Tex/MathTex revealed with Write. No transforms, no
# FadeOut.
#
# Subtopic time shares (subtopics.json, total 1135 s):
# 235/175/170/155/130/130/140 -> bands 0-1 / 2-3 / 4-5 / 6 / 7 / 8 / 9-10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinanceAndDataEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(13)

        # --- Band 0 (subtopic_1): the block tariff staircase
        title = Tex("Finance and Data Essentials").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Water: first 10 kl at R9,00; above at R16,50").scale(1.0).shift(UP * 1.2)
        b0_l2 = MathTex(r"10 \times 9 = \text{R}90{,}00").scale(1.0).shift(UP * 0.3)
        b0_l3 = MathTex(r"8 \times 16{,}50 = \text{R}132{,}00").scale(1.0).shift(DOWN * 0.5)
        b0_l4 = MathTex(r"90 + 132 = \text{R}222{,}00; \;\times 1{,}15 = \text{R}255{,}30").scale(0.95).shift(DOWN * 1.4)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = MathTex(r"18 \times 16{,}50 \; \text{ — all at the top rate: never}").scale(0.9).shift(DOWN * 2.4)
        self.play(Write(b0_l5))
        self.play(Create(strike(b0_l5)))
        self.wait(3)

        # --- Band 1 (subtopic_1): simple vs compound, and inflation
        self.next_band(1)
        b1_t = Tex("Simple looks back; compound looks at NOW").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Simple: } 8\;000 \times 0{,}05 = \text{R}400 \text{ each year} \to \text{R}9\;200").scale(0.9).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"\text{Compound: } 8\;000 \times 1{,}05^3 = \text{R}9\;261{,}00").scale(0.95).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("The R61,00 gap is interest earned on interest").scale(0.95).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"\text{Inflation: } 450 \times 1{,}06^2 = \text{R}505{,}62 \;\; (\text{not R}504)").scale(0.9).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): VAT in both directions
        self.next_band(2)
        b2_t = Tex("VAT: multiply forward, divide backward").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Excl R}320 \to 320 \times 1{,}15 = \text{R}368{,}00").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Incl R}368 \to 368 \div 1{,}15 = \text{R}320{,}00").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = MathTex(r"368 - 15\% \text{ of } 368 = \text{R}312{,}80 \; \text{ — too low}").scale(0.95).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(strike(b2_l3)))
        self.wait(2)
        b2_l4 = Tex("The 15\\% was charged on the SMALLER price").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the tax route and exchange rates
        self.next_band(3)
        b3_t = Tex("Tax: bracket, excess, base + \\%, rebate, months").scale(0.95).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"285\;000 - 226\;000 = \text{R}59\;000").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"38\;916 + 0{,}26 \times 59\;000 = \text{R}54\;256{,}00").scale(0.95).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"54\;256 - 16\;425 = \text{R}37\;831{,}00").scale(0.95).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = MathTex(r"\div 12 = \text{R}3\;152{,}58 \text{ per month}").scale(0.95).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"\text{Euros: } 95 \times 19{,}20 = 1\;824; \;\times 1{,}025 = \text{R}1\;869{,}60").scale(0.85).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): mean, median, range
        self.next_band(4)
        b4_t = Tex("Nine arranged marks — the toolkit").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"36, 43, 48, 52, 57, 63, 69, 74, 82").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"\text{Mean: } 524 \div 9 = 58{,}2").scale(1.05).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"\text{Median: position } 5 \to 57").scale(1.05).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = MathTex(r"\text{Range: } 82 - 36 = 46").scale(1.05).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): quartiles and the honest average
        self.next_band(5)
        b5_t = Tex("Quartiles cut the arranged data in quarters").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"Q_1 = \tfrac{43 + 48}{2} = 45{,}5 \qquad Q_3 = \tfrac{69 + 74}{2} = 71{,}5").scale(0.9).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"IQR = 71{,}5 - 45{,}5 = 26").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("Outliers drag the MEAN; the median holds position").scale(0.95).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = Tex("A percentile is a position, not a score").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): graphs and the traps
        self.next_band(6)
        b6_t = Tex("Choose the graph; catch the lie").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Categories: bar. Shares: pie. Time: line.").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("Five-number summary: box-and-whisker").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("Same median 63, narrower box: more consistent").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("Traps: axis starting at 60, tilted 3-D pie,").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        b6_l5 = Tex("and the biased sample that asked the wrong people").scale(0.9).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_5): the vetkoek stall
        self.next_band(7)
        b7_t = Tex("The stall: mark-up sits on the COST price").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Cost R}4{,}00 \to \text{sell R}7{,}00: \text{ profit R}3{,}00").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Mark-up: } \tfrac{3}{4} \times 100 = 75\%").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = MathTex(r"\tfrac{3}{7} \times 100 = 42{,}9\% \; \text{ — wrong base}").scale(0.95).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l3))
        self.play(Create(strike(b7_l3)))
        self.wait(2)
        b7_l4 = MathTex(r"\text{Flour: excl } 180 \times 1{,}15 = 207; \;\; 207 \div 1{,}15 = 180").scale(0.85).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_6): stokvel and the bank
        self.next_band(8)
        b8_t = Tex("Saving keeps; compounding grows").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = MathTex(r"\text{Stokvel: } 150 \times 12 = \text{R}1\;800 \text{ — kept, not grown}").scale(0.9).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"\text{Simple: } 6\;000 + 2 \times 300 = \text{R}6\;600").scale(0.95).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"\text{Compound: } 6\;000 \to 6\;300 \to \text{R}6\;615{,}00").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("The R15 gap is year two's interest on year one's").scale(0.95).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): the homework book argument
        self.next_band(9)
        b9_t = Tex("Five marks, one blackout week").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(1.5)
        b9_l1 = MathTex(r"68, 64, 75, 71, 22 \;\; \to \;\; 22, 64, 68, 71, 75").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{Mean: } 300 \div 5 = 60{,}0 \qquad \text{Median: } 68").scale(0.95).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{Without the 22: } \tfrac{64+68+71+75}{4} = 69{,}5").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        b9_l4 = Tex("One outlier dragged the mean 9,5 points down").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): the thumb test
        self.next_band(10)
        b10_t = Tex("The thumb test").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(1.5)
        b10_l1 = Tex("The poster's axis starts at R300, not zero").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("A small rise poses as a boom").scale(1.05).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex("Cover the axis numbers with a thumb —").scale(1.0).shift(band_shift(10) + DOWN * 0.7)
        b10_l4 = Tex("if the story vanishes, the axis told it").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(4)
