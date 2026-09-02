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

# Band-layout whiteboard scene for "Acids, Bases, pH and Titrations"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; write-only reveals; camera moves between
# bands. Subtopic durations 240/245/245/250/195/200/200 of 1575 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AcidsBasesPhTitrationsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the two definitions + conjugate pairs ---
        title = Tex("Acids, Bases, pH and Titrations").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Arrhenius: acid gives $H_3O^+$ in water").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("Lowry-Br\\o nsted: acid $=$ PROTON DONOR").scale(1.05).shift(UP * 0.3)
        b0_l3 = Tex("base $=$ PROTON ACCEPTOR").scale(1.05).shift(DOWN * 0.5)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_eq = MathTex(r"HCl + H_2O \rightarrow H_3O^+ + Cl^-").scale(1.1).shift(DOWN * 1.5)
        self.play(Write(b0_eq))
        self.wait(2)
        b0_pair = Tex("Conjugate pair: differs by ONE proton").scale(1.05).shift(DOWN * 2.5)
        self.play(Write(b0_pair))
        self.play(Create(SurroundingRectangle(b0_pair, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): ampholytes and proton supply ---
        self.next_band(1)
        b1_title = Tex("Ampholytes and proton supply").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Ampholyte: acts as acid OR base").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"H_2O, \; HCO_3^-, \; HSO_4^-").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Monoprotic: $HCl$, $HNO_3$ — one proton").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
        b1_l4 = Tex("Diprotic: $H_2SO_4$ — TWO protons").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.wait(2.5)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): strength vs concentration, K_a ---
        self.next_band(2)
        b2_title = Tex("Strength is NOT concentration").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Strong: ionises completely ($HCl$, $HNO_3$)").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("Weak: partial only (ethanoic, $H_2CO_3$)").scale(1.0).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex(r"Concentrated/dilute: mol per dm$^3$").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Large $K_a$: strong. Small $K_a$: weak.").scale(1.05).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("Bench test: lower pH, conducts better,").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        b2_l6 = Tex("reacts faster with Mg — the strong one").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_3): pH calculations 1 and 2 ---
        self.next_band(3)
        b3_title = MathTex(r"pH = -\log[H_3O^+]").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex(r"$HCl$ at 0,01 mol$\cdot$dm$^{-3}$ (complete):").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"[H_3O^+] = 10^{-2} \;\Rightarrow\; pH = 2").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2.5)
        b3_l3 = Tex(r"$H_2SO_4$ at 0,05 mol$\cdot$dm$^{-3}$ — diprotic!").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_wrong = MathTex(r"pH = -\log 0{,}05 = 1{,}3").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l4 = MathTex(r"[H_3O^+] = 2 \times 0{,}05 = 0{,}1 \;\Rightarrow\; pH = 1").scale(1.0).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): base through K_w + the weak-acid caveat ---
        self.next_band(4)
        b4_title = MathTex(r"K_w = [H_3O^+][OH^-] = 10^{-14}").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex(r"$NaOH$ at 0,001 mol$\cdot$dm$^{-3}$:").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"[OH^-] = 10^{-3}").scale(1.05).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"[H_3O^+] = \frac{10^{-14}}{10^{-3}} = 10^{-11}").scale(1.05).shift(band_shift(4) + DOWN * 0.7)
        b4_l4 = MathTex(r"pH = 11").scale(1.1).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex(r"Weak: ethanoic 0,01 gives pH $\approx$ 3,4 not 2").scale(0.95).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_4): the four-line titration ---
        self.next_band(5)
        b5_title = Tex(r"Titration: 25 cm$^3$ $NaOH$ vs 20 cm$^3$ $HCl$").scale(1.05).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l0 = Tex(r"$HCl$: 0,1 mol$\cdot$dm$^{-3}$; ratio 1 : 1").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l0))
        self.wait(2)
        b5_l1 = MathTex(r"n(HCl) = 0{,}1 \times 0{,}020 = 0{,}002\ \text{mol}").scale(1.0).shift(band_shift(5) + UP * 0.3)
        b5_l2 = MathTex(r"n(NaOH) = 0{,}002\ \text{mol}").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        b5_l3 = MathTex(r"c = \frac{0{,}002}{0{,}025} = 0{,}08\ \text{mol·dm}^{-3}").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_rule = Tex(r"Volumes to dm$^3$ FIRST; $H_2SO_4$ carries a 2").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_rule))
        self.wait(3)

        # --- Band 6 (subtopic_4): salts and indicator choice ---
        self.next_band(6)
        b6_title = Tex("The salt sets the equivalence pH").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("strong $+$ strong: neutral — bromothymol").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("weak acid $+$ strong base: basic —").scale(1.0).shift(band_shift(6) + UP * 0.2)
        b6_l2b = Tex("phenolphthalein (flips above 7)").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6_l3 = Tex("strong acid $+$ weak base: acidic —").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        b6_l3b = Tex("methyl orange (flips below 7)").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.play(Write(b6_l2b))
        self.wait(2.5)
        self.play(Write(b6_l3))
        self.play(Write(b6_l3b))
        self.wait(2.5)
        b6_rule = Tex("The STRONG parent wins the salt's pH").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_rule))
        self.play(Create(SurroundingRectangle(b6_rule, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): givers and takers ---
        self.next_band(7)
        b7_title = Tex("Givers and takers").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("One tiny parcel: the proton").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("Acid gives it; base takes it. Done.").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Giver minus parcel $=$ its conjugate base").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = MathTex(r"NH_4^+ / NH_3, \quad H_3O^+ / H_2O").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l3))
        self.wait(2.5)
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("Water plays both positions: ampholyte").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the cordial picture ---
        self.next_band(8)
        b8_title = Tex("Strong is not concentrated").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Amount of syrup poured $=$ concentration").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Eagerness to split up $=$ strength").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Battery acid: concentrated strong").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("Pool drops: dilute strong. Vinegar: conc. weak").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Big $K_a$: eager splitter. Tiny $K_a$: reluctant.").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): ladder of tens + the exact balance ---
        self.next_band(9)
        b9_title = Tex("The ladder of tens").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Each pH rung $=$ a factor of TEN").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Two rungs down: a hundred times more acidic").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Titration: pour known acid into mystery base").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        b9_l4 = Tex("until givers and takers exactly match").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Endpoint is not always 7: the salt leans").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        b9_l6 = Tex("toward its STRONGER parent").scale(1.0).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(4)
