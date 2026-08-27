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

# Band-layout whiteboard scene for the Measurement, Maps and Data Essentials
# revision session duo. One band per teaching beat, camera-only transitions,
# add-only lifecycle, exporter-supported mobjects only. Band time apportioned
# to subtopics.json (235/230/245/245/190/190/190 of 1525 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MeasurementMapsDataEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the garden — perimeter, area, money ---
        title = Tex("Measurement, Maps and Data Essentials").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        garden = Rectangle(width=4.5, height=3.75).shift(LEFT * 3.4 + DOWN * 0.9)
        self.play(Create(garden))
        g_l = Tex("9 m").scale(0.85).shift(LEFT * 3.4 + UP * 1.3)
        g_w = Tex("7,5 m").scale(0.85).shift(LEFT * 6.2 + DOWN * 0.9)
        self.play(Write(g_l), Write(g_w))
        self.wait(2)
        b0_l1 = MathTex(r"P = 2(9 + 7{,}5) = 33 \text{ m}").scale(1.0).shift(RIGHT * 3.4 + UP * 0.7)
        b0_l2 = MathTex(r"A = 9 \times 7{,}5 = 67{,}5 \text{ m}^2").scale(1.0).shift(RIGHT * 3.4 + DOWN * 0.3)
        b0_l3 = MathTex(r"\text{Fence: } 33 \times 90 = \text{R}2\;970").scale(1.0).shift(RIGHT * 3.4 + DOWN * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex("`Around' = perimeter; `cover' = area").scale(0.95).shift(DOWN * 2.9)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the tank — volume into litres ---
        self.next_band(1)
        b1_t = Tex("The rain tank: volume fills the space").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"V = l \times w \times h = 2{,}5 \times 1{,}2 \times 1{,}4").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"= 4{,}2 \text{ m}^3").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"1 \text{ m}^3 = 1\;000 \text{ litres} \Rightarrow 4\;200 \text{ litres}").scale(0.89).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = Tex("Formula, values in, answer with unit —").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        b1_l5 = Tex("the substitution line itself earns marks").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the metric ladder ---
        self.next_band(2)
        b2_t = Tex("The metric ladder").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("Up the ladder (small to big): DIVIDE").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("Down the ladder (big to small): MULTIPLY").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"6\;200 \text{ mm} = 6{,}2 \text{ m} \quad 2{,}8 \text{ km} = 2\;800 \text{ m}").scale(0.86).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"3\;400 \text{ ml} = 3{,}4 \text{ litres}").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Temperature swings subtract: 26 $-$ 8 = 18$^\\circ$C").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the mixed-units trap ---
        self.next_band(3)
        b3_t = Tex("Convert FIRST, calculate SECOND").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_wrong = MathTex(r"480 \text{ cm} \times 1{,}5 \text{ m} = 720\;?!").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l1 = MathTex(r"480 \text{ cm} = 4{,}8 \text{ m}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        b3_l2 = MathTex(r"4{,}8 \times 1{,}5 = 7{,}2 \text{ m}^2").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Mixed units multiply into confident nonsense").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        b3_l4 = Tex("Write both lines — the conversion is a mark").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the floor plan at 1:100 ---
        self.next_band(4)
        b4_t = Tex("Floor plan, scale 1 : 100").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"62 \text{ mm on paper} \times 100 = 6\;200 \text{ mm}").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"= 6{,}2 \text{ m of real wall}").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{Reverse: } 2\;400 \div 100 = 24 \text{ mm on paper}").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex("Measure, multiply by the scale, convert —").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        b4_l5 = Tex("and check WHICH wall the label belongs to").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the map, and the two views ---
        self.next_band(5)
        b5_t = Tex("The map, scale 1 : 25 000").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"8 \text{ cm} \times 25\;000 = 200\;000 \text{ cm}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"= 2 \text{ km}").scale(1.1).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex("Absurd middle numbers are normal —").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = Tex("the final conversion tames them; show both").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("Floor plan: looks DOWN (widths, layout)").scale(0.95).shift(band_shift(5) + DOWN * 2.3)
        b5_l6 = Tex("Elevation: looks ACROSS (heights, windows)").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.wait(2)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): summarising the survey ---
        self.next_band(6)
        b6_t = Tex("Five households: 11, 14, 14, 16, 20 buckets").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Mean: } 75 \div 5 = 15").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{Median (middle): } 14 \quad \text{Mode: } 14").scale(1.05).shift(band_shift(6) + UP * 0.2)
        b6_l3 = MathTex(r"\text{Range: } 20 - 11 = 9").scale(1.05).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Range measures spread, not centre").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the outlier, and probability ---
        self.next_band(7)
        b7_t = Tex("The outlier, and data about the future").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("Add a 55-bucket mansion: the mean leaps,").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("the median barely moves").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("With an outlier, the median is the typical home").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = MathTex(r"\text{Green taxis: } \frac{9}{30} = 0{,}3 = 30\%").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("0 impossible, 0,5 even, 1 certain — an estimate").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the tape measure pays the bills ---
        self.next_band(8)
        b8_t = Tex("The tape measure pays the bills").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Around: 33 m of edge = the fencing order, R2 970").scale(0.95).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Across: 67,5 m$^2$ of ground = the paving order").scale(0.95).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Inside: 4,2 m$^3$ of tank = 4 200 litres of rain").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_ans = Tex("The money tells you which number it wants").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_ans))
        self.play(Create(SurroundingRectangle(b8_ans, color=GREEN)))
        b8_l4 = Tex("And units must match BEFORE multiplying").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): paper worlds ---
        self.next_band(9)
        b9_t = Tex("Plans and maps: shrunken reality").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("1 : 100 means shrunk 100 times to fit the page").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Un-shrink to read: 62 mm grows to 6,2 m").scale(0.95).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("Shrink to draw: 2 400 mm becomes 24 mm").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Multiply to grow, divide to shrink").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("Couch fits? Bird's view. Window sun? Neighbour's").scale(0.9).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): reading the street's numbers honestly ---
        self.next_band(10)
        b10_t = Tex("Reading the street's numbers honestly").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Mean 15, median 14, mode 14, range 9 —").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("four sentences about the same street").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Who is IN that average? The mansion drags it;").scale(0.95).shift(band_shift(10) + DOWN * 0.6)
        b10_l4 = Tex("the middle of the queue stays ordinary").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = MathTex(r"\text{Next taxi green? } 9 \div 30 = 30\% \text{ — an estimate}").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_ans = Tex("Quote every summary with its working attached").scale(0.95).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_ans))
        self.play(Create(SurroundingRectangle(b10_ans, color=GREEN)))
        self.wait(4)
