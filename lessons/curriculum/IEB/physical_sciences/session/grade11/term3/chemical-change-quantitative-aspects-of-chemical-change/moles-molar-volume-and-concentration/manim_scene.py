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

# Band-layout whiteboard scene for the moles / molar volume / concentration
# session duo. Covers all seven subtopics (Part 1 Expert: 1-4, Part 2
# Simplifier: 5-7), band time proportional to subtopics.json
# (230/235/230/245/190/190/200 of 1520 s). Add-only lifecycle; every worked
# calculation appears line by line with the script's exact numbers and SA
# decimal commas.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MolesMolarVolumeConcentrationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the mole and its three symbols ---
        title = Tex("The Mole: One Unit Under Everything").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"1 mole $= 6{,}02 \times 10^{23}$ particles").scale(1.15).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"(as many particles as atoms in 12 g of C-12)").scale(0.95).shift(UP * 0.3)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_f1 = MathTex(r"n = \frac{N}{N_A}").scale(1.2).shift(DOWN * 0.9 + LEFT * 2.2)
        b0_f2 = MathTex(r"n = \frac{m}{M}").scale(1.2).shift(DOWN * 0.9 + RIGHT * 2.2)
        self.play(Write(b0_f1))
        self.wait(1.5)
        self.play(Write(b0_f2))
        self.wait(2)
        b0_l3 = Tex(r"$M$ = molar mass in g$\cdot$mol$^{-1}$,").scale(1.0).shift(DOWN * 2.1)
        b0_l4 = Tex("assembled from the periodic table").scale(1.0).shift(DOWN * 2.9)
        self.play(Write(b0_l3))
        self.wait(1.5)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): molar masses, subscripts intact ---
        self.next_band(1)
        b1_t = Tex("Molar mass, atom by atom").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = MathTex(r"NH_3: \; 14 + 3(1) = 17 \text{ g/mol}").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"SO_2: \; 32 + 2(16) = 64 \text{ g/mol}").scale(1.1).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"K_2CO_3: \; 78 + 12 + 48 = 138 \text{ g/mol}").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_trap = Tex(r"$K_2CO_3$ with ONE K $= 99$?").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_trap))
        self.play(Create(strike(b1_trap)))
        self.wait(1.5)
        b1_fix = Tex("Count the atoms aloud — every subscript").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_fix))
        self.wait(3)

        # --- Band 2 (subtopic_1): conversions both directions ---
        self.next_band(2)
        b2_t = Tex(r"How many moles is 16 g of $SO_2$?").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = MathTex(r"n = \frac{m}{M} = \frac{16}{64}").scale(1.15).shift(band_shift(2) + UP * 1.0)
        b2_l2 = MathTex(r"n = 0{,}25 \text{ mol}").scale(1.15).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = MathTex(r"N = n \times N_A = 0{,}25 \times 6{,}02 \times 10^{23}").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        b2_l4 = MathTex(r"N = 1{,}505 \times 10^{23} \text{ molecules}").scale(1.05).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = MathTex(r"\text{Backwards: } 0{,}3 \text{ mol } NH_3 = 0{,}3 \times 17 = 5{,}1 \text{ g}").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): molar gas volume at STP ---
        self.next_band(3)
        b3_t = Tex("Gases: measured by volume").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex(r"At STP (0$^\circ$C, 101{,}3 kPa):").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"1 mol of ANY gas fills 22{,}4 dm$^3$").scale(1.1).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_f = MathTex(r"n = \frac{V}{V_M} = \frac{11{,}2}{22{,}4} = 0{,}5 \text{ mol}").scale(1.1).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_f))
        self.play(Create(SurroundingRectangle(b3_f, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex("Avogadro: equal volumes, same T and p,").scale(1.0).shift(band_shift(3) + DOWN * 1.8)
        b3_l4 = Tex("contain equal numbers of molecules").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l3))
        self.wait(1.5)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_2): coefficients as volume ratios ---
        self.next_band(4)
        b4_t = Tex("The volume-ratio shortcut").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_eq = MathTex(r"2CO + O_2 \rightarrow 2CO_2").scale(1.2).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_eq))
        self.wait(2)
        b4_l1 = MathTex(r"12 \text{ dm}^3 + 6 \text{ dm}^3 \rightarrow 12 \text{ dm}^3").scale(1.1).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("Coefficients ARE volume ratios —").scale(1.05).shift(band_shift(4) + DOWN * 0.9)
        b4_l3 = Tex("no grams, no molar masses required").scale(1.05).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l2))
        self.wait(1.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_warn = Tex("GASES ONLY — a solid or solution").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        b4_warn2 = Tex("sends the problem back through moles").scale(1.0).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(b4_warn))
        self.play(Write(b4_warn2))
        self.wait(3)

        # --- Band 5 (subtopic_3): concentration and the cm3 trap ---
        self.next_band(5)
        b5_t = Tex("Concentration: amount per volume").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_f = MathTex(r"c = \frac{n}{V} \quad \text{in mol} \cdot \text{dm}^{-3}").scale(1.2).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_f))
        self.wait(2.5)
        b5_l1 = Tex(r"Glassware reads cm$^3$; the formula").scale(1.0).shift(band_shift(5) + DOWN * 0.1)
        b5_l2 = Tex(r"wants dm$^3$: divide by 1 000 first").scale(1.0).shift(band_shift(5) + DOWN * 0.9)
        self.play(Write(b5_l1))
        self.wait(1.5)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"750 \text{ cm}^3 = 0{,}75 \text{ dm}^3").scale(1.0).shift(band_shift(5) + DOWN * 1.9)
        b5_l4 = MathTex(r"200 \text{ cm}^3 = 0{,}2 \text{ dm}^3").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l3))
        self.wait(1.5)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_3): worked both directions ---
        self.next_band(6)
        b6_t = Tex(r"8{,}4 g KOH made up to 750 cm$^3$").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = MathTex(r"M(KOH) = 39 + 16 + 1 = 56 \text{ g/mol}").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"n = \frac{8{,}4}{56} = 0{,}15 \text{ mol}").scale(1.1).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"c = \frac{n}{V} = \frac{0{,}15}{0{,}75}").scale(1.1).shift(band_shift(6) + DOWN * 0.9)
        b6_l4 = MathTex(r"c = 0{,}2 \text{ mol} \cdot \text{dm}^{-3}").scale(1.1).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = MathTex(r"\text{Backwards: } n = cV = 0{,}6 \times 0{,}2 = 0{,}12 \text{ mol}").scale(0.95).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): percentage composition ---
        self.next_band(7)
        b7_t = Tex(r"Percentage composition: $SO_3$ (M = 80)").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = MathTex(r"S: \; \frac{32}{80} \times 100 = 40\%").scale(1.05).shift(band_shift(7) + UP * 1.0)
        b7_l2 = MathTex(r"O: \; \frac{48}{80} \times 100 = 60\%").scale(1.05).shift(band_shift(7) + UP * 0.0)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l4 = MathTex(r"40 + 60 = 100\% \; \checkmark").scale(1.05).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("The percentages must always close on 100").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_4): empirical to molecular formula ---
        self.next_band(8)
        b8_t = Tex(r"80\% C, 20\% H — find the formula").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = MathTex(r"C: \frac{80}{12} = 6{,}67 \qquad H: \frac{20}{1} = 20").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"\div 6{,}67: \quad 1 : 3 \;\Rightarrow\; CH_3").scale(1.1).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = MathTex(r"CH_3 \text{ (15 g/mol)}, \; M = 30 \text{ g/mol}").scale(1.0).shift(band_shift(8) + DOWN * 0.9)
        b8_l4 = MathTex(r"\frac{30}{15} = 2 \;\Rightarrow\; C_2H_6").scale(1.1).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2)
        b8_l5 = Tex("Empirical = ratio; molecular = the molecule").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): counting by the boxful ---
        self.next_band(9)
        b9_t = Tex("Counting by the boxful").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"A mole is a crate of $6{,}02 \times 10^{23}$ items").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Same count per crate, different weights:").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex(r"H 1 g, $NH_3$ 17 g, $SO_2$ 64 g per crate").scale(1.05).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l2))
        self.wait(1.5)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = MathTex(r"16 \text{ g} \div 64 \text{ g/crate} = 0{,}25 \text{ crates (mol)}").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("The periodic table = the warehouse ledger").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): balloons are honest ---
        self.next_band(10)
        b10_t = Tex("Balloons are honest about the count").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Identical balloons, same T and p:").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("identical counts inside — Avogadro").scale(1.05).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.wait(1.5)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"\frac{11{,}2}{22{,}4} = 0{,}5 \text{ mol}").scale(1.1).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = MathTex(r"2CO + O_2 \rightarrow 2CO_2: \; 12 : 6 : 12").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Balloon ratios — gases only!").scale(1.0).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l5))
        self.wait(3)

        # --- Band 11 (subtopic_7): how strong is the mix ---
        self.next_band(11)
        b11_t = Tex("How strong is the mix").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("Same shot of syrup, bigger jug = weaker").scale(1.05).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1))
        self.wait(2)
        b11_l2 = MathTex(r"c = \frac{0{,}15}{0{,}75} = 0{,}2 \text{ mol/dm}^3").scale(1.0).shift(band_shift(11) + UP * 0.1)
        self.play(Write(b11_l2))
        self.play(Create(SurroundingRectangle(b11_l2, color=GREEN)))
        self.wait(2.5)
        b11_l3 = Tex(r"cm$^3$ to dm$^3$: divide by 1 000 FIRST").scale(1.0).shift(band_shift(11) + DOWN * 0.9)
        self.play(Write(b11_l3))
        self.wait(2)
        b11_l4 = MathTex(r"n = cV = 0{,}6 \times 0{,}2 = 0{,}12 \text{ mol}").scale(1.0).shift(band_shift(11) + DOWN * 1.8)
        self.play(Write(b11_l4))
        self.wait(2)
        b11_l5 = Tex("Every quantity checks in at moles first").scale(1.05).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11_l5))
        self.wait(4)
