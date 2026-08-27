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

# Band-layout whiteboard scene for the Measurement and Maps practice-run
# session (an original 150-mark practice paper walked question by question).
# One band per teaching beat; the camera moves down and earlier work stays on
# the canvas. Exporter-supported mobjects only; every working line is its own
# single-string Tex/MathTex revealed with Write. No transforms, no FadeOut.
#
# Subtopic time shares (subtopics.json, total 935 s):
# 150/110/140/140/120/130/145 -> bands 0-1 / 2 / 3-4 / 5 / 6 / 7-8 / 9-10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MeasurementPracticeRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(13)

        # --- Band 0 (subtopic_1): how the practice paper is built
        title = Tex("Measurement Practice Run: 150 Marks").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Q1: 30 marks of single-step warm-ups").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("Q2 Maps and Plans; Q3 Measurement").scale(1.05).shift(UP * 0.4)
        b0_l3 = Tex("Q4--5 mix them — Finance may visit").scale(1.05).shift(DOWN * 0.4)
        b0_l4 = Tex("Probability's few marks hide anywhere").scale(1.05).shift(DOWN * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("Special demand: UNITS on every line").scale(1.05).shift(DOWN * 2.2)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): conversions carry marks
        self.next_band(1)
        b1_t = Tex("The marking plan pays the crossing").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("mm to m, m$^3$ to litres, decimal hours to minutes").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("2 marks: one operation plus answer").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex("4 marks: a conversion lives inside").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("6 and up: a staged build — each stage pays").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): Question One warm-ups
        self.next_band(2)
        b2_t = Tex("Question One: warm-up marks").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"4\;800 \text{ m} \div 1\;000 = 4{,}8 \text{ km}").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"0{,}25 \text{ m}^3 \times 1\;000 = 250 \text{ litres}").scale(1.0).shift(band_shift(2) + UP * 0.2)
        b2_l3 = Tex("1 : 50 — one unit is 50 of the SAME units").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = MathTex(r"2\;700 \text{ mm} = 2{,}7 \text{ m}").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("One visible line each, units on every answer").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): the trip — time and the sixties trap
        self.next_band(3)
        b3_t = Tex("Q2 The N2 trip: 310 km at 100 km/h").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Time: } 310 \div 100 = 3{,}1 \text{ hours}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"0{,}1 \times 60 = 6 \; \Rightarrow \; 3 \text{ h } 6 \text{ min}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"3 \text{ h } 10 \text{ min — the decimal read as minutes}").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(strike(b3_l3)))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Fuel: } 3{,}1 \times 6{,}9 = 21{,}39 \text{ litres}").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        b3_l5 = MathTex(r"21{,}39 \times 22{,}80 = \text{R}487{,}69").scale(1.05).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the map and the reverse timeline
        self.next_band(4)
        b4_t = Tex("The strip map and the departure line").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"4 \times 200\;000 = 800\;000 \text{ cm} = 8 \text{ km}").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("Arrive 13:00; lunch stop 50 min; drive 3 h 6 min").scale(0.95).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"13{:}00 - 0{:}50 = 12{:}10").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"12{:}10 - 3{:}06 = 09{:}04").scale(1.05).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("Reverse timelines pay a mark per subtraction").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): painting the youth centre
        self.next_band(5)
        b5_t = Tex("Q3.1 Painting: six stages, six harvests").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Walls: } 2(10 + 7) \times 3 = 102 \text{ m}^2").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = MathTex(r"\text{Openings: } 3{,}6 + 9 \; \Rightarrow \; 102 - 12{,}6 = 89{,}4").scale(0.95).shift(band_shift(5) + UP * 0.3)
        b5_l3 = MathTex(r"\text{Two coats: } 178{,}8 \text{ m}^2; \; \div 8 = 22{,}35 \text{ litres}").scale(0.95).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = MathTex(r"\text{Tins: } 22{,}35 \div 10 = 2{,}235 \; \Rightarrow \; 3 \text{ tins}").scale(0.95).shift(band_shift(5) + DOWN * 1.5)
        b5_l5 = MathTex(r"3 \times 899 = \text{R}2\;697 \; > \; \text{budget R}2\;500").scale(0.95).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_l6 = Tex("Short by R197 — say both numbers in the verdict").scale(0.95).shift(band_shift(5) + DOWN * 3.2)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_5): the drum and the boxes
        self.next_band(6)
        b6_t = Tex("Q3.2 The drum and the flour boxes").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"V = 3{,}142 \times 0{,}4^2 \times 0{,}9").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"0{,}16 \to 0{,}502\;72 \to 0{,}452 \text{ m}^3").scale(1.0).shift(band_shift(6) + UP * 0.3)
        b6_l3 = MathTex(r"\times 1\;000 \approx 452 \text{ litres}").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("Diameter 0,8? Halve it FIRST — or quadruple the tank").scale(0.9).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = MathTex(r"\text{Boxes: } 4 \times 3 \times 5 = 60; \;\; 300\;000 \div 5\;000 = 60 \checkmark").scale(0.9).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_6): the plan and the ladder
        self.next_band(7)
        b7_t = Tex("Q4 The reading room plan at 1 : 50").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"96 \times 50 = 4\;800 \text{ mm} = 4{,}8 \text{ m}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2.5)
        b7_l2 = Tex("Sanity: rooms live between 2 and 8 metres").scale(1.0).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = MathTex(r"\text{Floor: } 4{,}8 \times 3{,}5 = 16{,}8 \text{ m}^2").scale(1.0).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = MathTex(r"16{,}8 \div 2{,}2 = 7{,}64 \; \Rightarrow \; 8 \text{ boxes}").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = MathTex(r"8 \times 215 = \text{R}1\;720{,}00").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the elevation match
        self.next_band(8)
        b8_t = Tex("Match elevations by counting, not vibes").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = Tex("Plan: door and two windows on the EAST wall").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("The drawing with three openings is the east elevation").scale(0.95).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("Anchor to compass directions —").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("left and right flip when you step outside").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.wait(1.5)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): probability moments
        self.next_band(9)
        b9_t = Tex("Probability hides inside the contexts").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(1.5)
        b9_l1 = MathTex(r"P(\text{win}) = \tfrac{6}{240} = \tfrac{1}{40} = 0{,}025 = 2{,}5\%").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"P(\text{not win}) = \tfrac{39}{40} = 0{,}975").scale(1.05).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("Six tickets multiply THIS raffle's chance by six —").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        b9_l4 = Tex("but every new raffle starts fresh").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(3)

        # --- Band 10 (subtopic_7): the five habits, measurement edition
        self.next_band(10)
        b10_t = Tex("Five memo habits, measurement edition").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(1.5)
        b10_l1 = Tex("1. Units on every line").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("2. Conversions are mark-bearing — write them").scale(1.0).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex("3. Round UP at the shop door, never mid-chain").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex("4. Substitution before evaluation").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        b10_l5 = Tex("5. Verdicts end with a number inside them").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.wait(2.5)
        self.play(Write(b10_l4))
        self.wait(2.5)
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex("Ten quiet marks recovered — every practice run").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
