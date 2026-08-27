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

# Band-layout whiteboard scene for "The Mole Concept" (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe mobjects
# only; write-only reveals; camera moves down band by band. Band time
# apportioned to subtopics.json (230/220/240/270/170/170/170 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


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
        b0_l2 = MathTex(r"1\ \text{mole} = 6{,}02 \times 10^{23}\ \text{particles}").scale(1.05).shift(UP * 0.2)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = Tex("1 mol weighs its periodic-table number in grams").scale(0.9).shift(DOWN * 0.9)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"n = \frac{m}{M}").scale(1.2).shift(DOWN * 2.0)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        b0_l5 = Tex("moles = mass over mass-of-one-mole").scale(0.9).shift(DOWN * 3.1)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_2): molar mass of propane ---
        self.next_band(1)
        b1_t = Tex("Molar mass of propane, C$_3$H$_8$").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("three carbons, eight hydrogens — mind the subscripts").scale(0.85).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"M = 3 \times 12 + 8 \times 1").scale(1.05).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"M = 36 + 8 = 44\ \text{g\,mol}^{-1}").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("skimmed subscripts give 13 — everything downstream dies").scale(0.8).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the division and the sense-check ---
        self.next_band(2)
        b2_t = Tex("Moles in 8,8 g of propane").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = MathTex(r"n = \frac{m}{M} = \frac{8{,}8}{44}").scale(1.05).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = MathTex(r"n = 0{,}2\ \text{mol}").scale(1.1).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = Tex("sense-check: 8,8 is exactly one fifth of 44").scale(0.95).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("5 mol would weigh 220 g — inverted division caught").scale(0.85).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): moles to molecules ---
        self.next_band(3)
        b3_t = Tex("Moles to molecules").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"N = n \times N_A").scale(1.05).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"N = 0{,}2 \times 6{,}02 \times 10^{23}").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"N = 1{,}204 \times 10^{23}\ \text{molecules}").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("out of the centre: multiply — the count must be enormous").scale(0.8).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): volume at STP ---
        self.next_band(4)
        b4_t = Tex("Volume at STP").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Avogadro: same conditions, same volume, any gas").scale(0.85).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex(r"STP: 0\,$^\circ$C (273 K), 101,3 kPa; $V_m$ = 22,4 dm$^3$\,mol$^{-1}$").scale(0.8).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"V = n \times V_m = 0{,}2 \times 22{,}4").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"V = 4{,}48\ \text{dm}^3").scale(1.05).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        b4_l5 = Tex("22,4 only at STP — never for liquids or solids").scale(0.85).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): the mole map, drawn ---
        self.next_band(5)
        b5_t = Tex("The mole map").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_c = Circle(radius=0.7, color=YELLOW).shift(band_shift(5) + DOWN * 0.3)
        b5_n = MathTex(r"n").scale(1.2).shift(band_shift(5) + DOWN * 0.3)
        self.play(Create(b5_c))
        self.play(Write(b5_n))
        self.wait(1.5)
        b5_m = Tex("mass: $\\times M$ out, $\\div M$ in").scale(0.85).shift(band_shift(5) + UP * 1.0 + LEFT * 3.2)
        b5_p = Tex("particles: $\\times N_A$ out, $\\div N_A$ in").scale(0.85).shift(band_shift(5) + UP * 1.0 + RIGHT * 3.2)
        b5_v = Tex("gas at STP: $\\times 22{,}4$ out, $\\div 22{,}4$ in").scale(0.85).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_m))
        self.play(Write(b5_p))
        self.play(Write(b5_v))
        self.wait(2)
        b5_l1 = Line(band_shift(5) + UP * 0.7 + LEFT * 2.2, band_shift(5) + DOWN * 0.1 + LEFT * 0.7, color=BLUE)
        b5_l2 = Line(band_shift(5) + UP * 0.7 + RIGHT * 2.2, band_shift(5) + DOWN * 0.1 + RIGHT * 0.7, color=BLUE)
        b5_l3 = Line(band_shift(5) + DOWN * 1.7, band_shift(5) + DOWN * 1.0, color=BLUE)
        self.play(Create(b5_l1), Create(b5_l2), Create(b5_l3))
        b5_rule = Tex("in, divide; out, multiply").scale(1.0).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_rule))
        self.play(Create(SurroundingRectangle(b5_rule, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the error museum ---
        self.next_band(6)
        b6_t = Tex("The error museum").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("1. dividing by $N_A$ on the way OUT to particles").scale(0.9).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(1.5)
        b6_l2 = Tex("2. skimmed subscripts: 13 instead of 44").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2))
        self.wait(1.5)
        b6_l3 = Tex("3. 22,4 without STP, or for liquids and solids").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l3))
        self.wait(1.5)
        b6_l4 = Tex("4. unit chaos: kg into a grams formula;").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("1000 cm$^3$ = 1 dm$^3$ = 1 litre").scale(0.9).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2)
        b6_l6 = Tex("next stop: coefficients become mole ratios").scale(0.85).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): bags at the depot ---
        self.next_band(7)
        b7_t = Tex("Nobody counts rice grains").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("grains are too small, too many — count bags").scale(0.95).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("the mole is the bag: $6{,}02 \\times 10^{23}$ particles").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex("periodic table = price list, grams per bag").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("weighing stands in for counting: $n = m / M$").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_l4))
        self.wait(3)

        # --- Band 8 (subtopic_6): a fifth of a bag ---
        self.next_band(8)
        b8_t = Tex("A fifth of a bag").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("invoice for C$_3$H$_8$: C, C, C, then eight H's").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"36 + 8 = 44\ \text{g per bag}").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("8,8 g is one fifth of 44 — so 0,2 bags").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("a fifth of a bag of molecules: $1{,}204 \\times 10^{23}$").scale(0.9).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): same room for any gas + the taxi rank ---
        self.next_band(9)
        b9_t = Tex("Same room for any gas — and the rank").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("any gas, same conditions: same volume").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("at STP every mole takes 22,4 litres").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("$0{,}2 \\times 22{,}4 = 4{,}48$ litres — two big bottles").scale(0.9).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("moles are the taxi rank in the middle:").scale(0.95).shift(band_shift(9) + DOWN * 1.5)
        b9_l5 = Tex("ride in — divide; ride out — multiply").scale(0.95).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(4)
