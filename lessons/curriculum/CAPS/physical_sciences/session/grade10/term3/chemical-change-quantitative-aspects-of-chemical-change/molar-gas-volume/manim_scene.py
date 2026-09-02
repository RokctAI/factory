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

# Band-layout whiteboard scene for molar-gas-volume (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). Exporter-safe mobjects
# only; add-only lifecycle; worked calculations line by line with the
# script's exact numbers and units.
# Time apportioned to subtopics.json (230/235/235/250/180/180/170 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MolarGasVolumeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Avogadro's law ---
        title = Tex("Molar Gas Volume").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        a1 = Tex(r"1 mol CO$_2$ (44 g) and 1 mol H$_2$ (2 g):").scale(1.0).shift(UP * 1.0)
        a2 = Tex("same $T$, same $p$ — SAME volume").scale(1.05).shift(UP * 0.2)
        self.play(Write(a1))
        self.wait(2)
        self.play(Write(a2))
        self.wait(2.5)
        a3 = Tex("Avogadro: equal volumes, equal counts").scale(1.05).shift(DOWN * 0.8)
        self.play(Write(a3))
        self.play(Create(SurroundingRectangle(a3, color=GREEN)))
        self.wait(2)
        a4 = Tex("A gas is mostly empty space:").scale(1.0).shift(DOWN * 1.8)
        a5 = Tex("spacing, not molecule size, sets volume").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(a4))
        self.play(Write(a5))
        self.wait(3)

        # --- Band 1 (subtopic_1): STP and the 22,4 ---
        self.next_band(1)
        b1_t = Tex("The 22,4 that fits every gas").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_1 = Tex(r"STP: 0 $^\circ$C (273 K), 101,3 kPa").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_1))
        self.wait(2)
        b1_2 = MathTex(r"V_m = 22{,}4\ \text{dm}^3\text{·mol}^{-1}").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_2))
        self.play(Create(SurroundingRectangle(b1_2, color=GREEN)))
        self.wait(2)
        b1_3 = MathTex(r"V = n \times V_m \qquad n = \frac{V}{22{,}4}").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_3))
        self.wait(2.5)
        b1_4 = Tex("Licence: GASES only, at STP only").scale(1.0).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_4))
        self.wait(2)
        b1_5 = Tex("(1 dm$^3$ = 1 litre)").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the reaction, balanced, and 'excess' ---
        self.next_band(2)
        b2_t = Tex("10 g CaCO$_3$ + excess HCl").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_1 = MathTex(r"\text{CaCO}_3 + 2\text{HCl} \rightarrow").scale(1.0).shift(band_shift(2) + UP * 1.3)
        b2_1b = MathTex(r"\text{CaCl}_2 + \text{H}_2\text{O} + \text{CO}_2").scale(1.0).shift(band_shift(2) + UP * 0.5 + RIGHT * 1.0)
        self.play(Write(b2_1))
        self.play(Write(b2_1b))
        self.wait(2.5)
        b2_2 = Tex("Balanced: Ca 1:1, C 1:1, O 3:3,").scale(1.0).shift(band_shift(2) + DOWN * 0.3)
        b2_3 = Tex("H 2:2, Cl 2:2 $\\checkmark$").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_2))
        self.play(Write(b2_3))
        self.wait(2.5)
        b2_4 = Tex("EXCESS acid: all the carbonate reacts,").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        b2_5 = Tex("so base everything on the carbonate").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_4))
        self.wait(1.5)
        self.play(Write(b2_5))
        self.play(Create(SurroundingRectangle(b2_5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the three-leg journey ---
        self.next_band(3)
        b3_t = Tex("Mass to moles to volume").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_1 = MathTex(r"M(\text{CaCO}_3) = 40 + 12 + 48 = 100").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_1))
        self.wait(2)
        b3_2 = MathTex(r"n = \frac{m}{M} = \frac{10}{100} = 0{,}1\ \text{mol}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_2))
        self.wait(2.5)
        b3_3 = MathTex(r"\text{Ratio } 1:1 \Rightarrow 0{,}1\ \text{mol CO}_2").scale(1.05).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_3))
        self.wait(2)
        b3_4 = MathTex(r"V = n V_m = 0{,}1 \times 22{,}4 = 2{,}24\ \text{dm}^3").scale(1.05).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_4))
        self.play(Create(SurroundingRectangle(b3_4, color=GREEN)))
        self.wait(2.5)
        b3_5 = MathTex(r"\text{By mass instead: } 0{,}1 \times 44 = 4{,}4\ \text{g}").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_5))
        self.wait(3)

        # --- Band 4 (subtopic_3): volume ratios read off coefficients ---
        self.next_band(4)
        b4_t = Tex("Volume ratios: no balance needed").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_1 = MathTex(r"\text{N}_2 + 3\text{H}_2 \rightarrow 2\text{NH}_3").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_1))
        self.wait(2)
        b4_2 = Tex("Coefficients wear litres: 1 : 3 : 2").scale(1.05).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_2))
        self.wait(2)
        b4_3 = MathTex(r"10\ \text{dm}^3\ \text{N}_2 + 30\ \text{dm}^3\ \text{H}_2").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_3))
        self.wait(2)
        b4_4 = MathTex(r"\rightarrow 20\ \text{dm}^3\ \text{NH}_3").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_4))
        self.play(Create(SurroundingRectangle(b4_4, color=GREEN)))
        self.wait(2)
        b4_5 = Tex("40 in, 20 out: volume is NOT conserved").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_5))
        self.wait(3)

        # --- Band 5 (subtopic_3): the shortcut's conditions ---
        self.next_band(5)
        b5_t = Tex("The shortcut's small print").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_1 = Tex("Mass conserved always; molecules counted:").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_2 = Tex("4 reactant molecules become 2").scale(0.95).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_1))
        self.wait(2)
        self.play(Write(b5_2))
        self.wait(2)
        b5_3 = Tex("Same $T$ and $p$ for all gases —").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        b5_4 = Tex("not necessarily STP; no 22,4 needed").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_3))
        self.wait(2)
        self.play(Write(b5_4))
        self.wait(2)
        b5_5 = Tex("Only species marked (g) join the ratio").scale(1.0).shift(band_shift(5) + DOWN * 2.4)
        self.play(Write(b5_5))
        self.play(Create(SurroundingRectangle(b5_5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the toolkit ---
        self.next_band(6)
        b6_t = Tex("The gas toolkit").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_1 = MathTex(r"\text{Tool 1: } V = n \times 22{,}4 \; \text{(STP)}").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_1))
        self.wait(2)
        b6_2 = Tex("Tool 2: mass $\\to$ moles $\\to$ ratio $\\to$ volume").scale(0.95).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_2))
        self.wait(2)
        b6_3 = Tex("Tool 3: coefficients as volume ratios").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_3))
        self.wait(2)
        b6_4 = Tex("Grams given: go through moles;").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        b6_5 = Tex("litres to litres: ride the ratio").scale(1.0).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_4))
        self.wait(1.5)
        self.play(Write(b6_5))
        self.wait(3)

        # --- Band 7 (subtopic_4): the five traps ---
        self.next_band(7)
        b7_t = Tex("The five traps").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_trap = Tex("Use 22,4 with no STP stated").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_trap))
        self.play(Create(strike(b7_trap)))
        self.wait(2)
        b7_1 = Tex(r"Liquid water: 1 mol $=$ 18 cm$^3$, not 22,4 dm$^3$").scale(0.9).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_1))
        self.wait(2)
        b7_2 = MathTex(r"250\ \text{cm}^3 = 0{,}25\ \text{dm}^3 \; \text{(before formulas)}").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_2))
        self.wait(2)
        b7_3 = Tex("Build on the reactant NOT in excess").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_3))
        self.wait(2)
        b7_4 = Tex("Volumes follow molecule counts, not mass").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_4))
        self.play(Create(SurroundingRectangle(b7_4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): same crate, whatever the cargo ---
        self.next_band(8)
        b8_t = Tex("Same crate, whatever the cargo").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        crate1 = Rectangle(width=2.4, height=1.6).move_to(band_shift(8) + UP * 0.6 + LEFT * 2.2)
        c1l = Tex(r"H$_2$: 2 g").scale(0.85).move_to(band_shift(8) + UP * 0.6 + LEFT * 2.2)
        crate2 = Rectangle(width=2.4, height=1.6).move_to(band_shift(8) + UP * 0.6 + RIGHT * 2.2)
        c2l = Tex(r"CO$_2$: 44 g").scale(0.85).move_to(band_shift(8) + UP * 0.6 + RIGHT * 2.2)
        clab = Tex(r"both 22,4 dm$^3$ at STP").scale(0.95).move_to(band_shift(8) + DOWN * 0.6)
        self.play(Create(crate1), Write(c1l))
        self.play(Create(crate2), Write(c2l))
        self.wait(2)
        self.play(Write(clab))
        self.play(Create(SurroundingRectangle(clab, color=GREEN)))
        self.wait(2)
        b8_1 = Tex("Packed by count, not by weight").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_1))
        self.wait(2)
        b8_2 = MathTex(r"11{,}2\ \text{dm}^3 = \text{half a crate} = 0{,}5\ \text{mol}").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_2))
        self.wait(3)

        # --- Band 9 (subtopic_6): a spoonful of chalk ---
        self.next_band(9)
        b9_t = Tex("A spoonful of chalk, a bottle of gas").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_1 = Tex("Plenty of acid: chalk decides the amounts").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_1))
        self.wait(2)
        b9_2 = MathTex(r"10\ \text{g} \div 100 = 0{,}1\ \text{mol chalk}").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_2))
        self.wait(2.5)
        b9_3 = MathTex(r"1:1 \Rightarrow 0{,}1\ \text{mol CO}_2").scale(1.0).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(b9_3))
        self.wait(2)
        b9_4 = MathTex(r"0{,}1 \times 22{,}4 = 2{,}24\ \text{dm}^3").scale(1.05).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_4))
        self.play(Create(SurroundingRectangle(b9_4, color=GREEN)))
        self.wait(2.5)
        b9_5 = Tex("Solids cramped, gases roomy — expect it").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_5))
        self.wait(3)

        # --- Band 10 (subtopic_7): recipes measured in litres ---
        self.next_band(10)
        b10_t = Tex("Recipes measured in litres").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_1 = MathTex(r"\text{N}_2 + 3\text{H}_2 \rightarrow 2\text{NH}_3: \; 1:3:2 \text{ cups}").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_1))
        self.wait(2.5)
        b10_2 = MathTex(r"10\ \text{L} + 30\ \text{L} \rightarrow 20\ \text{L}").scale(1.05).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_2))
        self.play(Create(SurroundingRectangle(b10_2, color=GREEN)))
        self.wait(2.5)
        b10_3 = Tex("40 L in, 20 L out: fewer, bigger molecules").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_3))
        self.wait(2)
        b10_4 = Tex("Same conditions needed; only (g) rides").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_4))
        self.wait(2)
        b10_5 = Tex("Else: the long road through moles, 22,4 last").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_5))
        self.wait(4)
