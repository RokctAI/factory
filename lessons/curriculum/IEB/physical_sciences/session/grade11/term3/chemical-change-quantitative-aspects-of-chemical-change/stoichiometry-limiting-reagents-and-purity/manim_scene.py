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

# Band-layout whiteboard scene for the stoichiometry / limiting reagent /
# purity session duo. Covers all seven subtopics (Part 1 Expert: 1-4,
# Part 2 Simplifier: 5-7), band time proportional to subtopics.json
# (225/245/245/235/195/200/200 of 1545 s). Add-only lifecycle; worked
# calculations appear line by line with the script's exact numbers and SA
# decimal commas.

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
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the three-leg journey ---
        title = Tex("Stoichiometry With Real-World Teeth").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Leg 1: grams to moles").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("Leg 2: ratio across the equation").scale(1.05).shift(UP * 0.4)
        b0_l3 = Tex("Leg 3: moles to the asked-for quantity").scale(1.05).shift(DOWN * 0.4)
        self.play(Write(b0_l1))
        self.wait(1.5)
        self.play(Write(b0_l2))
        self.wait(1.5)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_rule = Tex("Grams never cross — only MOLES cross").scale(1.1).shift(DOWN * 1.5)
        self.play(Write(b0_rule))
        self.play(Create(SurroundingRectangle(b0_rule, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the journey worked to 20,4 g ---
        self.next_band(1)
        b1_t = MathTex(r"4Al + 3O_2 \rightarrow 2Al_2O_3").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_q = Tex(r"Max mass of oxide from 10{,}8 g Al?").scale(1.0).shift(band_shift(1) + UP * 1.3)
        self.play(Write(b1_q))
        self.wait(2)
        b1_l1 = MathTex(r"n(Al) = \frac{10{,}8}{27} = 0{,}4 \text{ mol}").scale(1.05).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"n(Al_2O_3) = 0{,}4 \times \frac{2}{4} = 0{,}2 \text{ mol}").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = MathTex(r"m = 0{,}2 \times 102 = 20{,}4 \text{ g}").scale(1.1).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("Wanted over given: write the fraction out").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): who runs out first ---
        self.next_band(2)
        b2_t = MathTex(r"N_2 + 3H_2 \rightarrow 2NH_3").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = MathTex(r"n(N_2) = \frac{14}{28} = 0{,}5 \qquad n(H_2) = \frac{2{,}4}{2} = 1{,}2").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = Tex(r"Test: 0{,}5 mol $N_2$ demands 1{,}5 mol $H_2$").scale(1.0).shift(band_shift(2) + UP * 0.1)
        b2_l3 = Tex(r"Available: only 1{,}2 mol").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_verdict = Tex(r"$H_2$ limiting; $N_2$ in excess").scale(1.1).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_verdict))
        self.play(Create(SurroundingRectangle(b2_verdict, color=GREEN)))
        self.wait(2)
        b2_trap = Tex(r"Smaller mole count (0{,}5) limiting?").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_trap))
        self.play(Create(strike(b2_trap)))
        self.wait(3)

        # --- Band 3 (subtopic_2): build on the limiting reagent ---
        self.next_band(3)
        b3_t = Tex("Build everything on the limiting reagent").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = MathTex(r"n(NH_3) = 1{,}2 \times \frac{2}{3} = 0{,}8 \text{ mol}").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = MathTex(r"m(NH_3) = 0{,}8 \times 17 = 13{,}6 \text{ g}").scale(1.05).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = MathTex(r"N_2 \text{ left: } 0{,}5 - 0{,}4 = 0{,}1 \text{ mol} = 2{,}8 \text{ g}").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Audit: } 14 + 2{,}4 = 13{,}6 + 2{,}8 = 16{,}4 \text{ g}").scale(1.0).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("Conservation of mass: the free self-check").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): percentage yield ---
        self.next_band(4)
        b4_t = Tex("Percentage yield: the honest scoreboard").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_f = MathTex(r"\% \text{ yield} = \frac{\text{actual}}{\text{theoretical}} \times 100").scale(1.1).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_f))
        self.wait(2.5)
        b4_l1 = MathTex(r"\frac{17{,}34}{20{,}4} \times 100 = 85\%").scale(1.1).shift(band_shift(4) + DOWN * 0.1)
        self.play(Write(b4_l1))
        self.play(Create(SurroundingRectangle(b4_l1, color=GREEN)))
        self.wait(2.5)
        b4_l2 = Tex("Losses: incomplete reaction, transfers,").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        b4_l3 = Tex("side reactions, reverse reactions").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l2))
        self.wait(1.5)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex(r"Over 100\%: wet or contaminated product").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): percentage purity, backwards ---
        self.next_band(5)
        b5_t = MathTex(r"MgCO_3 + H_2SO_4 \rightarrow MgSO_4 + H_2O + CO_2").scale(0.95).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex(r"20 g rock sample, excess acid, gas caught").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = MathTex(r"n(CO_2) = \frac{4{,}48}{22{,}4} = 0{,}2 \text{ mol}").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"1:1 \Rightarrow n(MgCO_3) = 0{,}2 \text{ mol} = 16{,}8 \text{ g}").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = MathTex(r"\% \text{ purity} = \frac{16{,}8}{20} \times 100 = 84\%").scale(1.05).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("Impurities never react — never counted").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the airbag ---
        self.next_band(6)
        b6_t = MathTex(r"2NaN_3 \rightarrow 2Na + 3N_2").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = MathTex(r"M(NaN_3) = 23 + 42 = 65 \text{ g/mol}").scale(1.0).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"n = \frac{97{,}5}{65} = 1{,}5 \text{ mol}").scale(1.05).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"n(N_2) = 1{,}5 \times \frac{3}{2} = 2{,}25 \text{ mol}").scale(1.05).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"V = 2{,}25 \times 22{,}4 = 50{,}4 \text{ dm}^3").scale(1.1).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("Explosion = violent gas production, caught in a bag").scale(0.9).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the ingredient that runs out first ---
        self.next_band(7)
        b7_t = Tex("The ingredient that runs out first").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Recipe: 4 lemons + 1 cup sugar = 1 jug").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("Stock: 20 lemons, 6 cups sugar").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Test: 20 lemons demand 5 cups — have 6").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("LEMONS limit: 5 jugs, 1 cup left over").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("Sugar was the smaller number — irrelevant!").scale(0.95).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): promised versus delivered ---
        self.next_band(8)
        b8_t = Tex("Promised vs delivered").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Promised 5 jugs; 4 reached customers").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = MathTex(r"\frac{4}{5} \times 100 = 80\%").scale(1.1).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = Tex("Spills, leftovers on the glass, wasps:").scale(0.95).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex("real yields sit below 100").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        self.play(Write(b8_l3))
        self.wait(1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Over 100 = something extra weighed in").scale(0.95).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_7): the pillow that inflates ---
        self.next_band(9)
        b9_t = Tex("The pillow that inflates before you blink").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"97{,}5 g pellet $= 1{,}5$ crates of azide").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex(r"Recipe pays 3 gas crates per 2: $2{,}25$ crates").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"2{,}25 \times 22{,}4 = 50{,}4 \text{ dm}^3").scale(1.1).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("Inert nitrogen — never a flammable gas").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Engineers run the sum backwards: bag to pellet").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(4)
