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

# Band-layout whiteboard scene for the Measurement, Maps and Probability
# Essentials revision session. One band per teaching beat; the camera moves
# down and earlier work stays on the canvas. Exporter-supported mobjects only;
# every working line is its own single-string Tex/MathTex revealed with Write.
# No transforms, no FadeOut.
#
# Subtopic time shares (subtopics.json, total 1145 s):
# 210/165/170/170/135/145/150 -> bands 0-1 / 2 / 3-4 / 5-6 / 7 / 8 / 9-10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MeasurementMapsProbabilityEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(13)

        # --- Band 0 (subtopic_1): ladders, perimeter and area
        title = Tex("Measurement, Maps and Probability").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"3{,}2 \text{ kg} = 3\;200 \text{ g}; \quad 500 \text{ ml} = 0{,}5 \text{ litres}").scale(0.95).shift(UP * 1.2)
        b0_l2 = MathTex(r"1 \text{ m}^3 = 1\;000 \text{ litres}").scale(1.05).shift(UP * 0.3)
        b0_l3 = MathTex(r"\text{Chicken run 7} \times 4: \; P = 2(7+4) = 22 \text{ m}").scale(0.95).shift(DOWN * 0.6)
        b0_l4 = MathTex(r"A = 7 \times 4 = 28 \text{ m}^2").scale(1.0).shift(DOWN * 1.5)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("Edging and covering are different jobs").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the drum walked to litres
        self.next_band(1)
        b1_t = Tex("The drum: formula to litres in four lines").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"V = 3{,}142 \times 0{,}6^2 \times 1{,}2").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"0{,}36 \to 1{,}131\;12 \to 1{,}357 \text{ m}^3").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"\times 1\;000 \approx 1\;357 \text{ litres}").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("Given the diameter 1,2? Halve it FIRST").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): scale ladders and the sixties
        self.next_band(2)
        b2_t = Tex("Scale chains and the clock of sixties").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"9 \times 25\;000 = 225\;000 \text{ cm} = 2\;250 \text{ m} = 2{,}25 \text{ km}").scale(0.85).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Time: } 264 \div 80 = 3{,}3 \text{ hours}").scale(1.0).shift(band_shift(2) + UP * 0.1)
        b2_l3 = MathTex(r"0{,}3 \times 60 = 18 \;\Rightarrow\; 3 \text{ h } 18 \text{ min}").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"3 \text{ h } 30 \text{ min — the decimal read as minutes}").scale(0.9).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4))
        self.play(Create(strike(b2_l4)))
        self.wait(2)
        b2_l5 = Tex("Distance charts: row meets column; charts of climbs:").scale(0.85).shift(band_shift(2) + DOWN * 2.5)
        b2_l6 = Tex("steepest where the line rises fastest, not highest").scale(0.85).shift(band_shift(2) + DOWN * 3.2)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_3): plans and their symbols
        self.next_band(3)
        b3_t = Tex("The plan: a roofless view from above").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"88 \text{ mm} \times 50 = 4\;400 \text{ mm} = 4{,}4 \text{ m}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_l2 = Tex("Sanity: rooms live between 2 and 8 metres").scale(1.0).shift(band_shift(3) + UP * 0.1)
        b3_l3 = Tex("Arc = door swing; thin double lines = window").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        b3_l4 = Tex("Heights live on the ELEVATIONS, not the plan").scale(0.95).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): elevations and models
        self.next_band(4)
        b4_t = Tex("Match by counting; shrink by the scale").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Count the openings on each compass face —").scale(0.95).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("left and right flip when you step outside").scale(0.95).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"\text{Model 1:40 — } 8 \text{ m} \to 20 \text{ cm}; \; 5 \text{ m} \to 12{,}5 \text{ cm}").scale(0.9).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = MathTex(r"\text{Areas shrink by } 40^2 = 1\;600").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): dialects and listed outcomes
        self.next_band(5)
        b5_t = Tex("Probability speaks three dialects").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"P(\text{red}) = \tfrac{1}{8} = 0{,}125 = 12{,}5\%").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"\text{Coin and die: } 2 \times 6 = 12 \text{ outcomes}").scale(1.0).shift(band_shift(5) + UP * 0.1)
        b5_l3 = MathTex(r"P(\text{head and six}) = \tfrac{1}{12}").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex("Listing ALL outcomes is the method mark").scale(0.95).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the table and the denominator
        self.next_band(6)
        b6_t = Tex("Denominator discipline on tables").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("60 learners: 36 girls, 24 boys; 21 + 18 walk").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"P(\text{walks}) = \tfrac{39}{60} = 0{,}65").scale(1.0).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"P(\text{boy who walks}) = \tfrac{18}{60} = 0{,}3").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = MathTex(r"P(\text{walks, among boys}) = \tfrac{18}{24} = 0{,}75").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("The whole 60 — unless the question narrows the group").scale(0.9).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_5): setting up the shed
        self.next_band(7)
        b7_t = Tex("The shed: floor, edge, cooler").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"18 \times 8 = 144 \text{ m}^2; \; \div 12 = 12 \text{ tables}; \; \times 8 = 96").scale(0.85).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Bunting: } 2(18 + 8) = 52 \text{ m}").scale(1.0).shift(band_shift(7) + UP * 0.1)
        b7_l3 = MathTex(r"\text{Cooler: } 25\;000 \div 200 = 125 \text{ cups}").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        b7_l4 = Tex("125 cups against 96 guests: enough, 29 spare").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        b7_l5 = Tex("Calculate, then DECIDE — number plus verdict").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the trip for umkhulu
        self.next_band(8)
        b8_t = Tex("The reverse timeline earns per subtraction").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = MathTex(r"\text{Drive: } 240 \div 80 = 3 \text{ hours}").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"11{:}30 - 3{:}00 = 08{:}30; \quad -0{:}45 = 07{:}45").scale(0.95).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{Gravel: } 7 \times 100\;000 = 700\;000 \text{ cm} = 7 \text{ km}").scale(0.9).shift(band_shift(8) + DOWN * 0.9)
        b8_l4 = MathTex(r"\text{Fuel: } 2{,}4 \times 9 = 21{,}6 \text{ litres}; \; \times 22{,}40 = \text{R}483{,}84").scale(0.85).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): the forecast and its complement
        self.next_band(9)
        b9_t = Tex("One forecast, three dialects, one complement").scale(1.0).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(1.5)
        b9_l1 = MathTex(r"40\% = \tfrac{2}{5} = 0{,}4").scale(1.1).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"P(\text{dry}) = 1 - 0{,}4 = 0{,}6 = 60\%").scale(1.05).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("NOT rain for 40\\% of the day —").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        b9_l4 = Tex("about 4 times in 10 on days like this").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): experiment and the decision
        self.next_band(10)
        b10_t = Tex("Lived data and the marquee decision").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(1.5)
        b10_l1 = MathTex(r"\text{Experimental: } \tfrac{6}{24} = 0{,}25 = 25\%").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("Modelled forecast against lived history —").scale(0.95).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex("more years would make the figure steadier").scale(0.95).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("R1 200 marquee against 96 soaked guests:").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        b10_l5 = Tex("either choice scores — if the reason has a number").scale(0.95).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
