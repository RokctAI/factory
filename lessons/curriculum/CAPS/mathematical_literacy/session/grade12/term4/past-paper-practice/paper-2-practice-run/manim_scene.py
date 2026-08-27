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

# Band-layout whiteboard scene for the Paper 2 Practice Run session
# (Measurement with Maps and Plans, 150 marks, walked question by question).
# One band per teaching beat; the camera moves down and earlier work stays on
# the canvas. Exporter-supported mobjects only; every working line is its own
# single-string Tex/MathTex revealed with Write. No transforms, no FadeOut.
#
# Subtopic time shares (subtopics.json, total 935 s):
# 150/110/140/140/120/130/145 -> bands 0 / 1 / 2-3 / 4-5 / 6-7 / 8-9 / 10-11.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Paper2PracticeRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): the architecture of Paper 2
        title = Tex("Paper 2 Practice Run: 150 Marks").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\text{Measurement } 55\%; \text{ Maps and Plans } 40\%; \text{ Prob } 5\%").scale(0.81).shift(UP * 1.2)
        b0_l2 = Tex("Q1: about 30 marks, Level 1 only").scale(1.05).shift(UP * 0.3)
        b0_l3 = Tex("Q2 Maps; Q3 Measurement; Q4--5 integrate").scale(1.05).shift(DOWN * 0.6)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("The special demand is UNITS:").scale(1.05).shift(DOWN * 1.6)
        b0_l5 = Tex("the memo puts a mark on every crossing").scale(1.05).shift(DOWN * 2.4)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): Question 1 warm-ups
        self.next_band(1)
        b1_t = Tex("Question 1: thirty marks of single steps").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"3\;500 \text{ m} \div 1\;000 = 3{,}5 \text{ km}").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1_l2 = MathTex(r"0{,}75 \text{ m}^3 \times 1\;000 = 750 \text{ litres}").scale(1.05).shift(band_shift(1) + UP * 0.3)
        b1_l3 = MathTex(r"4\;200 \text{ mm} = 4{,}2 \text{ m}").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("1 : 100 means 1 unit = 100 of the SAME units").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        b1_l5 = Tex("N3 off the label; the arc is the door's swing").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_3): trip time, and the decimal-hours trap
        self.next_band(2)
        b2_t = Tex("Q2 The N3 road trip: 568 km at 100 km/h").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Time} = 568 \div 100 = 5{,}68 \text{ hours}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"0{,}68 \times 60 = 40{,}8 \text{ min}").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = Tex("About 5 hours 41 minutes").scale(1.1).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("5 hours 68 minutes — the decimal is NOT minutes").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.play(Create(strike(b2_l4)))
        self.wait(3)

        # --- Band 3 (subtopic_3): fuel money, strip map, reverse timeline
        self.next_band(3)
        b3_t = Tex("Fuel, the strip map, and working backwards").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Fuel: } \tfrac{568}{100} \times 7{,}8 = 44{,}304 \text{ litres}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"44{,}304 \times 23{,}50 = \text{R}1\;041{,}14").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Strip map: } 9 \times 50\;000 = 450\;000 \text{ cm} = 4{,}5 \text{ km}").scale(0.91).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("Arrive 14:00, minus 45 min lunch,").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        b3_l5 = Tex("minus 5 h 41 min: depart by 07:34").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_4): painting the classroom, stages 1-3
        self.next_band(4)
        b4_t = Tex("Q3.1 Painting the classroom: the staged build").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Walls: } 2 \times (8 + 6) = 28 \text{ m}; \; 28 \times 3 = 84 \text{ m}^2").scale(0.95).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{Door: } 0{,}8 \times 2{,}1 = 1{,}68 \text{ m}^2").scale(1.0).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"\text{Windows: } 4 \times 1{,}2 \times 1{,}5 = 7{,}2 \text{ m}^2").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"84 - 1{,}68 - 7{,}2 = 75{,}12 \text{ m}^2").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        b4_l5 = MathTex(r"\text{Two coats: } 75{,}12 \times 2 = 150{,}24 \text{ m}^2").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): litres, tins, and the budget verdict
        self.next_band(5)
        b5_t = Tex("Litres, tins and the budget sentence").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = MathTex(r"150{,}24 \div 9 = 16{,}69 \text{ litres}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"16{,}69 \div 5 = 3{,}34 \;\Rightarrow\; 4 \text{ tins (UP)}").scale(1.05).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("3 tins leaves wall bare; 3,34 cannot be bought").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        b5_l4 = MathTex(r"\text{Cost: } 4 \times 649 = \text{R}2\;596{,}00").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        b5_l5 = Tex("Verdict: a sentence holding BOTH numbers").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_5): the cylindrical tank
        self.next_band(6)
        b6_t = Tex("Q3.2 The tank: substitution before evaluation").scale(1.0).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"V = 3{,}142 \times 0{,}55^2 \times 2").scale(1.1).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"0{,}55^2 = 0{,}3025; \;\; \times 3{,}142 = 0{,}950\;46").scale(1.0).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"\times \; 2 = 1{,}901 \text{ m}^3").scale(1.05).shift(band_shift(6) + DOWN * 0.9)
        b6_l4 = MathTex(r"1{,}901 \times 1\;000 \approx 1\;901 \text{ litres}").scale(1.05).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex("Given a diameter of 1,1 m? Halve it FIRST").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_5): packing the crate axis by axis
        self.next_band(7)
        b7_t = Tex("The boxes: count whole items per axis").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("Boxes 15 by 10 by 20 cm; crate 60 by 40 by 60 cm").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"60 \div 15 = 4; \quad 40 \div 10 = 4; \quad 60 \div 20 = 3").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"4 \times 4 \times 3 = 48 \text{ boxes}").scale(1.1).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = MathTex(r"\text{Check: } 144\;000 \div 3\;000 = 48 \;\checkmark").scale(1.0).shift(band_shift(7) + DOWN * 1.8)
        b7_l5 = Tex("Volume alone is a ceiling; only whole boxes ship").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): the plan and the tiles
        self.next_band(8)
        b8_t = Tex("Q4 The tuck shop plan at 1 : 100").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = MathTex(r"62 \text{ mm} \times 100 = 6\;200 \text{ mm} = 6{,}2 \text{ m}").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Sanity: rooms live between 2 m and 8 m").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = MathTex(r"\text{Floor: } 6{,}2 \times 4{,}5 = 27{,}9 \text{ m}^2").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = MathTex(r"27{,}9 \div 2{,}5 = 11{,}16 \;\Rightarrow\; 12 \text{ boxes}").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l3))
        self.wait(2.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the elevation match and the costing
        self.next_band(9)
        b9_t = Tex("Match the elevation; cost the tiles").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(1.5)
        b9_l1 = Tex("North wall holds the hatch and one window").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("The elevation with two openings is north —").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("reason by COUNTING, anchored to compass words").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Left and right flip when you step outside").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        b9_l5 = MathTex(r"\text{Tiles: } 12 \times 189 = \text{R}2\;268{,}00").scale(1.05).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the raffle
        self.next_band(10)
        b10_t = Tex("Probability hides inside the contexts").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(1.5)
        b10_l1 = MathTex(r"P(\text{win}) = \tfrac{5}{250} = \tfrac{1}{50} = 0{,}02").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"P(\text{not win}) = \tfrac{49}{50} = 0{,}98").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("Five tickets DO multiply this raffle's chance;").scale(1.0).shift(band_shift(10) + DOWN * 0.9)
        b10_l4 = Tex("last month's loss changes nothing — each").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        b10_l5 = Tex("draw starts fresh").scale(1.0).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): the five Paper 2 habits
        self.next_band(11)
        b11_t = Tex("Five habits, Paper 2 edition").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(1.5)
        b11_l1 = Tex("1. Units on every line").scale(1.0).shift(band_shift(11) + UP * 1.2)
        b11_l2 = Tex("2. Write conversions — they carry marks").scale(1.0).shift(band_shift(11) + UP * 0.4)
        b11_l3 = Tex("3. Tins, boxes, tiles round UP; never mid-chain").scale(1.0).shift(band_shift(11) + DOWN * 0.4)
        b11_l4 = Tex("4. Substitution before evaluation").scale(1.0).shift(band_shift(11) + DOWN * 1.2)
        b11_l5 = Tex("5. Verdicts end in a sentence with a number").scale(1.0).shift(band_shift(11) + DOWN * 2.0)
        self.play(Write(b11_l1))
        self.wait(2)
        self.play(Write(b11_l2))
        self.wait(2)
        self.play(Write(b11_l3))
        self.wait(2)
        self.play(Write(b11_l4))
        self.wait(2)
        self.play(Write(b11_l5))
        self.play(Create(SurroundingRectangle(b11_l5, color=GREEN)))
        self.wait(4)
