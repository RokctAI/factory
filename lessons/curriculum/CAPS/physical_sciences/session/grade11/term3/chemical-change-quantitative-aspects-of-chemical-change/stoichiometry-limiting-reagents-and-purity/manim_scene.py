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

# Band-layout whiteboard scene for the stoichiometry / limiting reagents /
# purity session duo. Covers all seven subtopics (Part 1 Expert: 1-4,
# Part 2 Simplifier: 5-7), band time proportional to subtopics.json
# (225/245/245/235/195/200/200 of 1545 s). Add-only lifecycle; worked
# calculations line by line with the script's exact numbers and SA decimal
# commas.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class StoichiometryLimitingPuritySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the three-leg journey ---
        title = Tex("Stoichiometry: The Equation's Promise").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_eq = MathTex(r"N_2 + 3H_2 \rightarrow 2NH_3").scale(1.25).shift(UP * 1.0)
        self.play(Write(b0_eq))
        self.wait(2)
        b0_q = Tex(r"Max mass of $NH_3$ from 28 g of $N_2$?").scale(1.1).shift(UP * 0.0)
        self.play(Write(b0_q))
        self.wait(2)
        b0_l1 = Tex("Leg 1: mass to moles. Leg 2: ratio across.").scale(1.0).shift(DOWN * 1.0)
        b0_l2 = Tex("Leg 3: moles to mass.").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(b0_l1))
        self.wait(1.5)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Grams never cross the equation — moles do").scale(1.0).shift(DOWN * 2.8)
        self.play(Write(b0_l3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the journey worked to 34 g ---
        self.next_band(1)
        b1_t = Tex("The journey, at exam speed").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"M(N_2) = 2(14) = 28 \text{ g/mol}").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"n(N_2) = \frac{28}{28} = 1 \text{ mol}").scale(1.05).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"n(NH_3) = 1 \times \frac{2}{1} = 2 \text{ mol}").scale(1.05).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = MathTex(r"m = nM = 2 \times 17 = 34 \text{ g}").scale(1.1).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4))
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)
        b1_n = Tex("Write wanted-over-given — never invert it").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_n))
        self.wait(3)

        # --- Band 2 (subtopic_2): who runs out first ---
        self.next_band(2)
        b2_t = Tex(r"Limiting reagent: $2H_2 + O_2 \rightarrow 2H_2O$").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_q = Tex(r"Supplied: 4 g $H_2$ and 40 g $O_2$").scale(1.05).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_q))
        self.wait(2)
        b2_l1 = MathTex(r"n(H_2) = \frac{4}{2} = 2 \text{ mol}").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l2 = MathTex(r"n(O_2) = \frac{40}{32} = 1{,}25 \text{ mol}").scale(1.05).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"Test: 2 mol $H_2$ needs 1 mol $O_2$ —").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        b2_l4 = Tex(r"1{,}25 available: $O_2$ excess, $H_2$ LIMITING").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): build on the limiting reagent ---
        self.next_band(3)
        b3_wrong = Tex("Pick the smaller mole count as limiting?").scale(1.05).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_n = Tex("Only the ratio test decides").scale(1.05).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_n))
        self.wait(2)
        b3_l1 = MathTex(r"n(H_2O) = 2 \text{ mol} \Rightarrow 2 \times 18 = 36 \text{ g}").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"O_2 \text{ left: } 1{,}25 - 1 = 0{,}25 \text{ mol} = 8 \text{ g}").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\text{Audit: } 4 + 40 = 36 + 8 = 44 \text{ g} \; \checkmark").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("Conservation of mass is a free check").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): percentage yield ---
        self.next_band(4)
        b4_t = Tex("Percentage yield: the honest scoreboard").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_f = MathTex(r"\% \text{ yield} = \frac{\text{actual}}{\text{theory}} \times 100").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_f))
        self.wait(2.5)
        b4_l1 = MathTex(r"\frac{27{,}2}{34} \times 100 = 80\%").scale(1.1).shift(band_shift(4) + UP * 0.0)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = Tex("Losses: incomplete reaction, transfers,").scale(1.0).shift(band_shift(4) + DOWN * 1.0)
        b4_l3 = Tex("side reactions, reverse reactions").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l2))
        self.wait(1.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex(r"Over 100\%? Wet or contaminated product").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): percentage purity, backwards ---
        self.next_band(5)
        b5_t = Tex("Purity: 10 g seashell, excess HCl").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_eq = MathTex(r"CaCO_3 + 2HCl \rightarrow CaCl_2 + H_2O + CO_2").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_eq))
        self.wait(2)
        b5_l1 = MathTex(r"n(CO_2) = \frac{1{,}792}{22{,}4} = 0{,}08 \text{ mol}").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"1:1 \Rightarrow n(CaCO_3) = 0{,}08 \text{ mol}").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        b5_l3 = MathTex(r"m = 0{,}08 \times 100 = 8 \text{ g}").scale(1.05).shift(band_shift(5) + DOWN * 1.7)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"\% \text{ purity} = \frac{8}{10} \times 100 = 80\%").scale(1.1).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the airbag ---
        self.next_band(6)
        b6_t = Tex("Stoichiometry at speed: the airbag").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_eq = MathTex(r"2NaN_3 \rightarrow 2Na + 3N_2").scale(1.2).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_eq))
        self.wait(2)
        b6_l1 = MathTex(r"M(NaN_3) = 23 + 42 = 65 \text{ g/mol}").scale(1.0).shift(band_shift(6) + UP * 0.2)
        b6_l2 = MathTex(r"n = \frac{130}{65} = 2 \text{ mol}").scale(1.05).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"n(N_2) = 2 \times \frac{3}{2} = 3 \text{ mol}").scale(1.05).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"V = 3 \times 22{,}4 = 67{,}2 \text{ dm}^3").scale(1.1).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the ingredient that runs out first ---
        self.next_band(7)
        b7_t = Tex("The ingredient that runs out first").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Recipe: 2 bread + 1 cheese = 1 toastie").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("Stock: 10 bread, 7 cheese").scale(1.05).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_wrong = Tex("Blame the smaller number — cheese?").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_l3 = Tex("Ratio test: 10 bread needs 5 cheese — have 7").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        b7_l4 = Tex("BREAD limits: 5 toasties, 2 cheese left").scale(1.05).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): promised versus plated ---
        self.next_band(8)
        b8_t = Tex("Promised vs what reached the plate").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Promised 5, plated 4:").scale(1.05).shift(band_shift(8) + UP * 1.2)
        b8_l2 = MathTex(r"\frac{4}{5} \times 100 = 80\% \text{ yield}").scale(1.1).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.wait(1.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Over 100 = something extra weighed in,").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l4 = Tex("never a miracle kitchen").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l3))
        self.wait(1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Purity: real cheese over whole bag —").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        b8_l6 = Tex("the plastic never fizzes").scale(1.0).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l5))
        self.wait(1.5)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_7): the pillow that inflates ---
        self.next_band(9)
        b9_t = Tex("The pillow that inflates before you blink").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("A soap-bar pellet of sodium azide:").scale(1.05).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"130 \div 65 = 2 \text{ boxes of } NaN_3").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"2 \rightarrow 3 \text{ boxes of } N_2").scale(1.05).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = MathTex(r"3 \times 22{,}4 = 67{,}2 \text{ dm}^3 \text{ of gas}").scale(1.05).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("An explosion, caught in a nylon bag —").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        b9_l6 = Tex("inert nitrogen, sized by our arithmetic").scale(1.0).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l5))
        self.wait(1.5)
        self.play(Write(b9_l6))
        self.wait(4)
