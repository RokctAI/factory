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

# Band-layout whiteboard scene for Body Measurements, BMI and Medicine Dosage.
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


class BodyMeasurementsBmiDosageSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the two instruments and the unit discipline
        title = Tex("Body Measurements, BMI and Dosage").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Mass: scale, in kilograms (zeroed, shoes off)").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("Height: stadiometer, in METRES").scale(1.05).shift(UP * 0.3)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = MathTex(r"175 \text{ cm} = 1{,}75 \text{ m (comma two places)}").scale(1.05).shift(DOWN * 0.6)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = Tex("First patient: 95 kg, standing 1,75 m").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): precision and reading between the marks
        self.next_band(1)
        b1_t = Tex("Precision fits the purpose").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Adult mass: nearest 0,5 kg is fine").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Baby mass: nearest 0,1 kg — the body is only 3 kg").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Needle halfway between 95 and 96:").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = MathTex(r"95{,}5 \text{ kg}").scale(1.15).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the BMI formula, worked
        self.next_band(2)
        b2_t = Tex("BMI = mass $\\div$ height$^2$ (kg and m)").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"1{,}75 \times 1{,}75 = 3{,}0625").scale(1.1).shift(band_shift(2) + UP * 1.0)
        b2_l2 = MathTex(r"95 \div 3{,}0625 = 31{,}0").scale(1.15).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("Categories: under 18,5 / 18,5-24,9 / 25-29,9 / 30 up").scale(0.95).shift(band_shift(2) + DOWN * 1.0)
        b2_l4 = Tex("31,0 falls in the obese range, just past its edge").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the unit crime and the blind spot
        self.next_band(3)
        b3_t = Tex("The calculator obeys the wrong units too").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"95 \div 175^2 = 0{,}003 \text{ — impossible}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.play(Create(strike(b3_l1)))
        self.wait(2)
        b3_l2 = Tex("Human BMIs live between about 15 and 45").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("BMI sees only mass and height").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        b3_l4 = Tex("Muscle reads as overweight: screening, not diagnosis").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the percentile idea, drawn
        self.next_band(4)
        b4_t = Tex("Percentiles: a line of 100 babies").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # fan of percentile curves suggested with rising lines
        base = band_shift(4) + LEFT * 4.5 + DOWN * 1.2
        for i, k in enumerate([0.25, 0.45, 0.7, 0.95, 1.15]):
            self.play(Create(Line(base, base + RIGHT * 7.5 + UP * (0.8 + k))), run_time=0.4)
        lab_3 = Tex("3rd").scale(0.8).shift(base + RIGHT * 7.9 + UP * 1.05)
        lab_50 = Tex("50th").scale(0.8).shift(base + RIGHT * 7.9 + UP * 1.5)
        lab_97 = Tex("97th").scale(0.8).shift(base + RIGHT * 7.9 + UP * 1.95)
        self.play(Write(lab_3), Write(lab_50), Write(lab_97))
        self.wait(2)
        pt = Dot(base + RIGHT * 5.0 + UP * 1.35, color=RED)
        self.play(FadeIn(pt))
        b4_l1 = Tex("Boy, 9 months, 8,9 kg: on the 50th curve").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        b4_l2 = Tex("Half of peers weigh less — dead centre").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(3)

        # --- Band 5 (subtopic_3): reading both ways, and the journey
        self.next_band(5)
        b5_t = Tex("Read the chart both ways").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("9-month boy on the 85th: about 10,0 kg").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("Midway between 50th and 85th: roughly the 70th").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Healthy: tracking along ONE curve").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        b5_l4 = Tex("Alarm: falling 85th to 50th across visits").scale(1.05).shift(band_shift(5) + DOWN * 1.7)
        b5_l5 = Tex("One dot is a photograph; the chart is a film").scale(1.05).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): dose from rate, syrup from label
        self.next_band(6)
        b6_t = Tex("Dosage: rate times mass, label to millilitres").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Boy of 16 kg; ibuprofen at 10 mg per kg").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"10 \times 16 = 160 \text{ mg per dose}").scale(1.1).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = MathTex(r"\text{Label: } 100 \text{ mg per } 5 \text{ ml} \Rightarrow 20 \text{ mg per ml}").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        b6_l4 = MathTex(r"160 \div 20 = 8 \text{ ml, in a marked syringe}").scale(1.05).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l3))
        self.wait(2.5)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the bottle's life and the safe rounding
        self.next_band(7)
        b7_t = Tex("The bottle's life: round the safe way").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Day: } 8 \times 3 = 24 \text{ ml} = 480 \text{ mg}").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Bottle: } 150 \div 8 = 18{,}75 \text{ doses}").scale(1.05).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Round DOWN: 18 full doses — dose 19 would be short").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        b7_l4 = Tex("18 doses at 3 a day: exactly 6 full days").scale(1.05).shift(band_shift(7) + DOWN * 1.8)
        b7_l5 = Tex("Never double after a missed dose").scale(1.05).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the number on the clinic wall
        self.next_band(8)
        b8_t = Tex("The number on the clinic wall").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = Tex("Wall says 175 — that is centimetres").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"\text{Comma across: } 1{,}75 \text{ m, then } 95 \div 3{,}06 = 31{,}0").scale(0.95).shift(band_shift(8) + UP * 0.2)
        b8_l3 = MathTex(r"\text{Centimetres left in: } 0{,}003 \text{ — a paperclip}").scale(1.0).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        self.play(Write(b8_l3))
        self.play(Create(strike(b8_l3)))
        self.wait(2)
        b8_l4 = Tex("Human BMIs: about 15 to 45 — check the units first").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): reading the curves
        self.next_band(9)
        b9_t = Tex("Reading the curves").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(1.5)
        b9_l1 = Tex("100 babies in a line: percentile = position").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Age along the bottom, weight up the side, dot").scale(1.05).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("9 months, 8,9 kg: the dot kisses the 50th").scale(1.05).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = Tex("Healthy walks along its own curve").scale(1.05).shift(band_shift(9) + DOWN * 1.6)
        b9_l5 = Tex("Alarm: crossing lanes downward, visit after visit").scale(1.05).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the medicine spoon
        self.next_band(10)
        b10_t = Tex("The medicine spoon").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(1.5)
        b10_l1 = MathTex(r"\text{Rate} \times \text{weight}: 10 \times 16 = 160 \text{ mg}").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"\text{Label: } 20 \text{ mg per ml} \Rightarrow 160 \div 20 = 8 \text{ ml}").scale(1.0).shift(band_shift(10) + UP * 0.1)
        b10_l3 = MathTex(r"\text{Bottle: } 150 \div 8 = 18{,}75 \to 18 \text{ doses}").scale(1.05).shift(band_shift(10) + DOWN * 0.9)
        b10_l4 = Tex("Paint rounds up; medicine rounds DOWN").scale(1.05).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = Tex("Six full days — plan the refill before the syrup dies").scale(1.0).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b10_l5))
        self.wait(4)
