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

# Band-layout whiteboard scene for Conversions, Volume and Surface Area.
# One band per teaching beat; the camera moves down and earlier work stays on
# the canvas. Exporter-supported mobjects only; every working line is its own
# single-string Tex/MathTex revealed with Write. No transforms, no FadeOut.
#
# Subtopic time shares (subtopics.json, total 1470 s):
# 215/215/225/230/195/195/195 -> bands 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConversionsVolumeSurfaceAreaSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): metric family and the imperial dictionary
        title = Tex("Conversions, Volume and Surface Area").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Metric moves in tens: shift the comma").scale(1.05).shift(UP * 1.2)
        b0_l2 = MathTex(r"3\;200 \text{ g} = 3{,}2 \text{ kg}").scale(1.1).shift(UP * 0.3)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Imperial needs the supplied factor table").scale(1.05).shift(DOWN * 0.6)
        b0_l4 = MathTex(r"5 \text{ pounds}: \; 5 \div 2{,}205 = 2{,}268 \text{ kg}").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the oven dial
        self.next_band(1)
        b1_t = Tex("Temperature: a formula, not a factor").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"^\circ F = 1{,}8 \times {}^\circ C + 32").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"400 - 32 = 368").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"368 \div 1{,}8 = 204{,}4\;^\circ C \to \text{dial } 200").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2.5)
        b1_l4 = MathTex(r"\text{Check forwards: } 1{,}8 \times 30 + 32 = 86\;^\circ F").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the tank's volume, worked
        self.next_band(2)
        b2_t = Tex("Cylinder: volume = pi $\\times$ r$^2$ $\\times$ height").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("Tank: 2,2 m across, so radius 1,1 m; height 1,5 m").scale(0.95).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"1{,}1 \times 1{,}1 = 1{,}21").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"1{,}21 \times 1{,}5 = 1{,}815").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"3{,}142 \times 1{,}815 = 5{,}703 \text{ m}^3").scale(1.1).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)
        b2_l5 = MathTex(r"5{,}703 \times 1\;000 = 5\;703 \text{ litres (brochure: 5 500)}").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the prism and the two disciplines
        self.next_band(3)
        b3_t = Tex("Prism: length $\\times$ width $\\times$ height").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"1{,}5 \times 0{,}6 \times 0{,}8 = 0{,}72 \text{ m}^3 = 720 \text{ litres}").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_l2 = Tex("Radius is HALF the diameter").scale(1.05).shift(band_shift(3) + UP * 0.1)
        b3_l3 = MathTex(r"\text{Radius } 2{,}2 \text{ instead of } 1{,}1: \text{ four times too big}").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(strike(b3_l3)))
        self.wait(2)
        b3_l4 = Tex("Same units BEFORE substituting — never mixed").scale(1.05).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the peeled wall and the lid
        self.next_band(4)
        b4_t = Tex("Surface area: what the tank WEARS").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Curved wall peels into a rectangle").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"2 \times 3{,}142 \times 1{,}1 = 6{,}912 \text{ m around}").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"6{,}912 \times 1{,}5 = 10{,}369 \text{ m}^2").scale(1.05).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\text{Lid circle: } 3{,}142 \times 1{,}21 = 3{,}802 \text{ m}^2").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        b4_l5 = MathTex(r"10{,}369 + 3{,}802 = 14{,}171 \approx 14{,}17 \text{ m}^2").scale(1.05).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the buying decision
        self.next_band(5)
        b5_t = Tex("The shop: buying always rounds UP").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("One litre covers 8 square metres").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"14{,}17 \div 8 = 1{,}77 \text{ litres}").scale(1.1).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Buy 2 litres — the ceiling, not the nearest").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("Not painted: the base on its concrete plinth").scale(1.05).shift(band_shift(5) + DOWN * 1.8)
        b5_l5 = Tex("List WHICH faces the job touches, first").scale(1.05).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): speed and filling time
        self.next_band(6)
        b6_t = Tex("Rates: the unit says what to divide").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Speed: } 360 \text{ km} \div 4 \text{ h} = 90 \text{ km/h}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{Filling: } 5\;703 \div 18 = 316{,}83 \text{ min}").scale(1.05).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"316{,}83 \text{ min} = 5 \text{ h } 17 \text{ min}").scale(1.05).shift(band_shift(6) + DOWN * 0.9)
        b6_l4 = Tex("Tap open 07:30: full a little before 12:50").scale(1.05).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): cost rates and value for money
        self.next_band(7)
        b7_t = Tex("Cost rates: rands per kilogram").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"1 \text{ kg at R}220: \; 220 \div 1 = \text{R}220 \text{ per kg}").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"2{,}5 \text{ kg at R}500: \; 500 \div 2{,}5 = \text{R}200 \text{ per kg}").scale(1.0).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Bigger bag saves R20 on every kilogram").scale(1.05).shift(band_shift(7) + DOWN * 0.9)
        b7_l4 = Tex("Judgement too: only if 2,5 kg stays fresh").scale(1.05).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): changing units without fear
        self.next_band(8)
        b8_t = Tex("Changing units without fear").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = Tex("Ask first: should the number grow or shrink?").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"\text{Sugar: } 5 \div 2{,}205 = 2{,}268 \text{ kg — under } 2{,}5").scale(0.95).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"11{,}03 \text{ kg? Moved the wrong way}").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.play(Create(strike(b8_l3)))
        self.wait(2)
        b8_l4 = Tex("Oven: off with the 32, then divide by 1,8").scale(1.05).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = MathTex(r"400 \to 368 \to 204 \to \text{dial } 200").scale(1.05).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): filling the tank
        self.next_band(9)
        b9_t = Tex("Filling the tank").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(1.5)
        b9_l1 = Tex("A cubic metre swallows 1 000 litres").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Across is 2,2 — the radius is HALF: 1,1").scale(1.05).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"\text{Floor: } 3{,}142 \times 1{,}21 = 3{,}802 \text{ m}^2").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = MathTex(r"3{,}802 \times 1{,}5 = 5{,}703 \text{ m}^3 = 5\;703 \text{ litres}").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2.5)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Brochure said 5 500 — the supplier told the truth").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): covering the outside
        self.next_band(10)
        b10_t = Tex("Covering the outside").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(1.5)
        b10_l1 = Tex("Peel the wall like a label off a tin").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"6{,}91 \times 1{,}5 \approx 10{,}37 \text{ m}^2 \text{, lid } 3{,}80 \text{ m}^2").scale(0.95).shift(band_shift(10) + UP * 0.2)
        b10_l3 = MathTex(r"\text{Total} \approx 14{,}17 \text{ m}^2; \; 14{,}17 \div 8 = 1{,}77 \text{ litres}").scale(0.95).shift(band_shift(10) + DOWN * 0.8)
        b10_l4 = Tex("Shopping ALWAYS rounds up: buy 2 litres").scale(1.05).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = Tex("List the faces the job touches, then add").scale(1.05).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.wait(2.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b10_l5))
        self.wait(4)
