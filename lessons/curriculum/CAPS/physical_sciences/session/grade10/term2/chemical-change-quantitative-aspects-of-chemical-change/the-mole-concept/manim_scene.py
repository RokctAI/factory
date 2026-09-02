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

# Band-layout whiteboard scene for "The Mole Concept" (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe mobjects
# only; write-only reveals; camera moves down band by band. Band time
# apportioned to subtopics.json (230/220/240/270/170/170/170 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MoleConceptSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why chemists count in moles ---
        title = Tex("The Mole Concept").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Count particles while weighing grams").scale(1.05).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = MathTex(r"N_A = 6{,}02 \times 10^{23} \text{ particles per mole}").scale(1.0).shift(UP * 0.2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("1 mol of carbon atoms weighs 12 g").scale(1.0).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"n = \frac{m}{M}").scale(1.3).shift(DOWN * 2.0)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = Tex("mass you have $\\div$ mass of one mole").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_2): molar mass of CO2 ---
        self.next_band(1)
        b1_t = Tex(r"How many moles in 8,8 g of CO$_2$?").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("read the formula atom by atom: C, O, O").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"M = 12 + 2 \times 16 = 44\;\text{g·mol}^{-1}").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = MathTex(r"M = 12 + 16 = 28 \quad \text{(one O counted!)}").scale(1.0).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l3))
        self.play(Create(strike(b1_l3)))
        self.wait(2.5)
        b1_l4 = Tex("subscripts command the arithmetic").scale(1.0).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the division and the sense-check ---
        self.next_band(2)
        b2_t = Tex("Divide, then sense-check").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"n = \frac{m}{M} = \frac{8{,}8}{44}").scale(1.1).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"n = 0{,}2\;\text{mol}").scale(1.15).shift(band_shift(2) + DOWN * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = Tex("8,8 is a fifth of 44: a fifth of a mole").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = MathTex(r"n = 5\;\text{mol would weigh } 220\;\text{g}").scale(1.0).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l4))
        self.play(Create(strike(b2_l4)))
        self.wait(2)
        b2_l5 = Tex("grams in, grams cancel, moles out").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): moles to molecules ---
        self.next_band(3)
        b3_t = Tex("How many molecules is 0,2 mol?").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"N = n \times N_A").scale(1.15).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"N = 0{,}2 \times 6{,}02 \times 10^{23}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"N = 1{,}204 \times 10^{23}\;\text{molecules}").scale(1.05).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("in under nine grams of gas —").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        b3_l5 = Tex("this is why nobody counts atoms").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): volume at STP ---
        self.next_band(4)
        b4_t = Tex("The volume at STP").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Avogadro's law: same conditions, same").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("volume, same count — ANY gas").scale(1.0).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"V_m = 22{,}4\;\text{dm}^3\text{ per mol at STP}").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"V = n \times V_m = 0{,}2 \times 22{,}4").scale(1.05).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = MathTex(r"V = 4{,}48\;\text{dm}^3").scale(1.1).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        b4_l6 = Tex("no STP in the question, no 22,4").scale(0.95).shift(band_shift(4) + DOWN * 3.2)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): the mole map, drawn ---
        self.next_band(5)
        b5_t = Tex("The mole map").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        centre = Circle(radius=0.75, color=WHITE).shift(band_shift(5) + DOWN * 0.3)
        centre_lab = MathTex(r"n").scale(1.1).shift(band_shift(5) + DOWN * 0.3)
        self.play(Create(centre), Write(centre_lab))
        self.wait(1.5)
        r1 = Arrow(band_shift(5) + DOWN * 0.3 + LEFT * 0.8, band_shift(5) + DOWN * 0.3 + LEFT * 3.2,
                   buff=0, color=YELLOW)
        r1_lab = Tex(r"mass: $\times M$").scale(0.9).shift(band_shift(5) + UP * 0.4 + LEFT * 2.4)
        self.play(Create(r1), Write(r1_lab))
        self.wait(1.5)
        r2 = Arrow(band_shift(5) + DOWN * 0.3 + RIGHT * 0.8, band_shift(5) + DOWN * 0.3 + RIGHT * 3.2,
                   buff=0, color=BLUE)
        r2_lab = Tex(r"particles: $\times N_A$").scale(0.9).shift(band_shift(5) + UP * 0.4 + RIGHT * 2.6)
        self.play(Create(r2), Write(r2_lab))
        self.wait(1.5)
        r3 = Arrow(band_shift(5) + DOWN * 1.05, band_shift(5) + DOWN * 2.3, buff=0, color=GREEN)
        r3_lab = Tex(r"gas at STP: $\times 22{,}4$").scale(0.9).shift(band_shift(5) + DOWN * 2.8)
        self.play(Create(r3), Write(r3_lab))
        self.wait(2)
        b5_l1 = Tex("in: divide — out: multiply").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the error museum ---
        self.next_band(6)
        b6_t = Tex("The error museum").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex(r"dividing by $N_A$ on the way OUT").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(strike(b6_l1)))
        self.wait(2)
        b6_l2 = Tex(r"CO$_2$ as 28 — the ignored subscript").scale(1.0).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l2))
        self.play(Create(strike(b6_l2)))
        self.wait(2)
        b6_l3 = Tex("22,4 without STP, or for liquids/solids").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l3))
        self.play(Create(strike(b6_l3)))
        self.wait(2)
        b6_l4 = MathTex(r"1\,000\;\text{cm}^3 = 1\;\text{dm}^3\text{; kg to g first}").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("next term: coefficients become mole ratios").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): bags at the wholesaler ---
        self.next_band(7)
        b7_t = Tex("Nobody counts rice grains — they count bags").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("the mole is chemistry's pack size:").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = MathTex(r"6{,}02 \times 10^{23}\text{ particles per pack}").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("the periodic table is the price list,").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = Tex("written in grams per pack: C costs 12 g").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = MathTex(r"n = \frac{m}{M}\;\; \text{— weighing counts for you}").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): a fifth of a bag ---
        self.next_band(8)
        b8_t = Tex("A fifth of a bag of sugar").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("read the invoice: C, O, O — mind the 2").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"12 + 16 + 16 = 44\;\text{g per pack}").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = MathTex(r"\frac{8{,}8}{44} = 0{,}2\;\text{mol}").scale(1.1).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = MathTex(r"0{,}2 \times 6{,}02 \times 10^{23} = 1{,}204 \times 10^{23}").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex("packs out to particles: always multiply").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): same room for any gas + the taxi rank ---
        self.next_band(9)
        b9_t = Tex("Same room for any gas").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("gas is mostly empty space: one mole of").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"ANY gas fills 22,4 dm$^3$ at STP").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"V = 0{,}2 \times 22{,}4 = 4{,}48\;\text{dm}^3").scale(1.05).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("about two big cooldrink bottles").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("moles are the taxi rank: ride in, divide;").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        b9_l6 = Tex("ride out, multiply — every question is a trip").scale(1.0).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(4)
