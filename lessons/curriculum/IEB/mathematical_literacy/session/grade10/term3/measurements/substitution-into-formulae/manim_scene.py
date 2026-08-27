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

# Band-layout whiteboard scene for the Substitution into Formulae session duo.
# One band per teaching beat, camera moves down between bands, add-only
# lifecycle. Exporter-supported mobjects only; every working line is a
# single-string Tex/MathTex revealed with Write. Band time apportioned to
# subtopics.json (200/230/230/270/180/185/185 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SubstitutionIntoFormulaeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): reading the formula ---
        title = Tex("Substitution into Formulae").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_f = MathTex(r"\text{Cost} = \text{R}380 + \text{R}9{,}50 \times \text{km}").scale(1.15).shift(UP * 1.2)
        self.play(Write(b0_f))
        self.play(Create(SurroundingRectangle(b0_f, color=BLUE)))
        self.wait(2)
        b0_l1 = Tex("R380: the fixed charge — owed before the wheels turn").scale(0.95).shift(UP * 0.1)
        b0_l2 = Tex("R9,50: the rate — every kilometre adds it").scale(0.95).shift(DOWN * 0.8)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("km: independent \\quad cost: dependent").scale(0.95).shift(DOWN * 1.8)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): forward substitution ---
        self.next_band(1)
        b1_t = Tex("Forwards: price the 260 km trip").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Cost} = 380 + 9{,}50 \times 260").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = MathTex(r"9{,}50 \times 260 = 2\;340 + 130 = 2\;470").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = MathTex(r"380 + 2\;470 = \text{R}2\;850").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("Multiplication BEFORE addition, always").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the disaster ---
        self.next_band(2)
        b2_t = Tex("The order-of-operations disaster").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_wrong = MathTex(r"(380 + 9{,}50) \times 260 = \text{R}101\;270").scale(1.05).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2.5)
        b2_l1 = MathTex(r"260 \times 380 = \text{R}98\;800 \text{ of phantom gate fees}").scale(0.95).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex("Sense check: R101 270 buys the bakkie").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): reverse substitution ---
        self.next_band(3)
        b3_t = Tex("Backwards: how far does R1 900 go?").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"1\;900 = 380 + 9{,}50 \times \text{km}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"1\;900 - 380 = 1\;520 \text{ for driving}").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{km} = 1\;520 \div 9{,}50 = 160").scale(1.05).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Check: } 380 + 9{,}50 \times 160 = 1\;900").scale(0.95).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): the 200 km trap ---
        self.next_band(4)
        b4_t = Tex("The reverse trap").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_wrong = MathTex(r"1\;900 \div 9{,}50 = 200 \text{ km}").scale(1.05).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2.5)
        b4_l1 = MathTex(r"\text{Extra } 40 \text{ km} = 380 \div 9{,}50").scale(1.0).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("The fixed fee never buys kilometres — peel it first").scale(0.95).shift(band_shift(4) + DOWN * 1.0)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the six-step method ---
        self.next_band(5)
        b5_t = Tex("The six-step method").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("1. Write the formula unchanged").scale(0.95).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("2. Known variable vs wanted variable").scale(0.95).shift(band_shift(5) + UP * 0.6)
        b5_l3 = Tex("3. Substitute, writing the full line").scale(0.95).shift(band_shift(5) + DOWN * 0.2)
        b5_l4 = Tex("4. Forwards: order of operations; backwards: unwind").scale(0.95).shift(band_shift(5) + DOWN * 1.0)
        b5_l5 = Tex("5. Answer WITH its unit").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        b5_l6 = Tex("6. Verify — sense-check, substitute back").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l1))
        self.wait(1.8)
        self.play(Write(b5_l2))
        self.wait(1.8)
        self.play(Write(b5_l3))
        self.wait(1.8)
        self.play(Write(b5_l4))
        self.wait(1.8)
        self.play(Write(b5_l5))
        self.wait(1.8)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the gate fee and the meter ---
        self.next_band(6)
        b6_t = Tex("The gate fee and the meter").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("R380 = the gate fee — paid once, at the counter").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("R9,50 = the meter — runs with every kilometre").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Same skeleton: plumber call-out, electricity, data").scale(0.95).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("You choose km (independent); cost answers (dependent)").scale(0.9).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): forwards in plain language ---
        self.next_band(7)
        b7_t = Tex("Forwards, the friendly way").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Driving: } 260 \times 9{,}50 = \text{R}2\;470").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"\text{Then the gate fee: } 2\;470 + 380 = \text{R}2\;850").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Adding first = paying the gate fee 260 times").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Repeat part first, once-off part last").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_7): backwards in plain language ---
        self.next_band(8)
        b8_t = Tex("Backwards: R1 900 in your pocket").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = MathTex(r"1\;900 - 380 = 1\;520 \text{ can become kilometres}").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"1\;520 \div 9{,}50 = 160 \text{ km}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Shoes off before socks: undo in reverse order").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = MathTex(r"\text{Prove it: } 380 + 9{,}50 \times 160 = 1\;900").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.wait(4)
