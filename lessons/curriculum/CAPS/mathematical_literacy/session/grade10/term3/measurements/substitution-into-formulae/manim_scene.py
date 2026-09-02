# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for the Substitution into Formulae session duo.
# One band per teaching beat, camera-only transitions, add-only lifecycle,
# exporter-supported mobjects only. Band time apportioned to subtopics.json
# (200/230/230/270/180/185/185 of 1480 s).

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
        # --- Band 0 (subtopic_1): reading the formula like a sentence ---
        title = Tex("Substitution into Formulae").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        formula = MathTex(r"\text{Cost} = \text{R}450 + \text{R}12{,}50 \times \text{km}").scale(1.2).shift(UP * 1.0)
        self.play(Write(formula))
        self.play(Create(SurroundingRectangle(formula, color=BLUE)))
        self.wait(2.5)
        b0_l1 = Tex("R450 stands alone: the FIXED charge").scale(1.05).shift(DOWN * 0.2)
        b0_l2 = Tex("R12,50 is glued to km: the RATE").scale(1.05).shift(DOWN * 1.1)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Fixed + rate $\\times$ usage — one skeleton").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(b0_l3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the skeleton everywhere + variables ---
        self.next_band(1)
        b1_t = Tex("The same skeleton, everywhere").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Electricity tariffs, cellphone contracts,").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("plumber call-outs, delivery charges").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("km: INDEPENDENT variable — you choose it").scale(1.0).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex("Cost: DEPENDENT variable — it responds").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_rule = Tex("The cost depends on the distance").scale(1.05).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1_rule))
        self.play(Create(SurroundingRectangle(b1_rule, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): forward substitution, 340 km ---
        self.next_band(2)
        b2_t = Tex("Forwards: price the 340 km trip").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Cost} = 450 + 12{,}50 \times \text{km}").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Cost} = 450 + 12{,}50 \times 340").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_note = Tex("(both written lines usually earn marks)").scale(0.9).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_note))
        self.wait(2)
        b2_l3 = MathTex(r"12{,}50 \times 340 = 4\;080 + 170 = 4\;250").scale(1.05).shift(band_shift(2) + DOWN * 1.3)
        b2_l4 = MathTex(r"450 + 4\;250 = \text{R}4\;700").scale(1.1).shift(band_shift(2) + DOWN * 2.3)
        self.play(Write(b2_l3))
        self.wait(2.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the order-of-operations disaster ---
        self.next_band(3)
        b3_t = Tex("The great trap: adding first").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_wrong = MathTex(r"(450 + 12{,}50) \times 340 = \text{R}157\;250").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2.5)
        b3_l1 = Tex("A hire-car bill that buys the car!").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_rule = Tex("Multiplication BEFORE addition, always").scale(1.1).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_rule))
        self.play(Create(SurroundingRectangle(b3_rule, color=GREEN)))
        self.wait(2)
        b3_l2 = Tex("Sense-check: R4 250 driving + R450 admin — fine").scale(0.95).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l2))
        self.wait(3)

        # --- Band 4 (subtopic_3): reverse substitution ---
        self.next_band(4)
        b4_t = Tex("Backwards: how far does R1 200 go?").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = MathTex(r"1\;200 = 450 + 12{,}50 \times \text{km}").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"1\;200 - 450 = 750").scale(1.05).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"750 = 12{,}50 \times \text{km}").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"\text{km} = 750 \div 12{,}50 = 60").scale(1.1).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("Peel the fixed fee first, then divide by the rate").scale(0.95).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): verify, and the 96 km trap ---
        self.next_band(5)
        b5_t = Tex("Prove it, and know the trap").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_wrong = MathTex(r"1\;200 \div 12{,}50 = 96 \text{ km?}").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l1 = Tex("R450 of that budget never bought a kilometre").scale(1.0).shift(band_shift(5) + UP * 0.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{Check: } 450 + 12{,}50 \times 60 = 450 + 750 = 1\;200").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("Built by $\\times$ then $+$; unwound by $-$ then $\\div$").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l3))
        self.wait(3)

        # --- Band 6 (subtopic_4): the six-step method ---
        self.next_band(6)
        b6_t = Tex("The method, six steps").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("1. Write the formula unchanged").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("2. Known variable vs wanted variable").scale(0.95).shift(band_shift(6) + UP * 0.5)
        b6_l3 = Tex("3. Substitute — write the full line").scale(0.95).shift(band_shift(6) + DOWN * 0.2)
        b6_l4 = Tex("4. Forwards: order of operations;").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        b6_l5 = Tex("backwards: unwind, fixed part first").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        b6_l6 = Tex("5. Answer WITH its unit \\quad 6. Verify").scale(0.95).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l1))
        self.wait(1.5)
        self.play(Write(b6_l2))
        self.wait(1.5)
        self.play(Write(b6_l3))
        self.wait(1.5)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(1.5)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the traps, ranked ---
        self.next_band(7)
        b7_t = Tex("The traps, ranked by damage").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("1. Adding the fixed charge before multiplying").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("2. Dividing a budget before removing the fee").scale(0.95).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex("3. Mixed units — convert BEFORE substituting").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("4. Rounding midway — round only at the end").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("The formula is printed on the paper —").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        b7_l6 = Tex("feed it carefully and these marks are yours").scale(0.95).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the gate fee and the meter ---
        self.next_band(8)
        b8_t = Tex("The gate fee and the meter").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("R450 = the gate fee: paid once, at the door").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("R12,50 = the pie money: grows with usage").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Bill = gate fee + driving money").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("You choose the km (independent);").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        b8_l5 = Tex("the bill answers you (dependent)").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): forwards, and the disaster explained ---
        self.next_band(9)
        b9_t = Tex("Forwards, in the order the day happens").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = MathTex(r"\text{Driving: } 340 \times 12{,}50 = \text{R}4\;250").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{Gate fee once: } 4\;250 + 450 = \text{R}4\;700").scale(1.05).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("Adding first = paying the gate fee 340 times:").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        b9_l4 = MathTex(r"340 \times 450 = 153\;000, \; +4\;250 = 157\;250").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("The once-off part never gets multiplied").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): backwards with R1 200 ---
        self.next_band(10)
        b10_t = Tex("Backwards: R1 200 in your pocket").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = MathTex(r"\text{Pay the counter first: } 1\;200 - 450 = 750").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = MathTex(r"750 \div 12{,}50 = 60 \text{ km}").scale(1.1).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("Skipping the peel gives 96 km — the extra 36").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        b10_l4 = Tex("is exactly what R450 would have bought").scale(0.95).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = MathTex(r"\text{Prove it: } 60 \times 12{,}50 + 450 = 1\;200 \; \checkmark").scale(1.0).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.wait(4)
