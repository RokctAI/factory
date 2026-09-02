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

# Band-layout whiteboard scene for the oxidation numbers and redox session
# duo. Covers all seven subtopics (Part 1 Expert: 1-4, Part 2 Simplifier:
# 5-7), band time proportional to subtopics.json
# (230/245/240/250/195/200/210 of 1570 s). Add-only lifecycle; exporter-safe
# mobjects only.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RedoxAndOxidationNumbersSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): salts from their parents ---
        title = Tex("Designing a Salt from its Parents").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Anion picks the acid; cation picks the base").scale(1.0).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_e1 = MathTex(r"2KOH + H_2SO_4 \rightarrow K_2SO_4 + 2H_2O").scale(0.95).shift(UP * 0.3)
        b0_e2 = MathTex(r"MgO + 2HNO_3 \rightarrow Mg(NO_3)_2 + H_2O").scale(0.95).shift(DOWN * 0.6)
        b0_e3 = MathTex(r"Na_2CO_3 + 2HCl \rightarrow 2NaCl + H_2O + CO_2").scale(0.9).shift(DOWN * 1.5)
        self.play(Write(b0_e1))
        self.wait(2)
        self.play(Write(b0_e2))
        self.wait(2)
        self.play(Write(b0_e3))
        self.wait(2)
        b0_l2 = Tex("hydroxide, oxide, carbonate (+ fizz)").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(b0_l2))
        self.wait(3)

        # --- Band 1 (subtopic_1): charges drive the balancing ---
        self.next_band(1)
        b1_t = Tex("Charges drive the coefficients").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_e1 = MathTex(r"Mg^{2+} + 2NO_3^- \Rightarrow Mg(NO_3)_2").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_e1))
        self.wait(2)
        b1_l1 = Tex("Two nitrates demand two $HNO_3$").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Diprotic $H_2SO_4$ demands TWO hydroxides").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Write the salt's formula first, from").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        b1_l4 = Tex("its charges — the coefficients follow").scale(1.0).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l3))
        self.wait(1.5)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the oxidation number rules ---
        self.next_band(2)
        b2_t = Tex("Oxidation numbers: the rules").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("1. Free element: 0").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("2. Simple ion: its charge").scale(1.0).shift(band_shift(2) + UP * 0.5)
        b2_l3 = Tex(r"3. F: $-1$. \; 4. H: $+1$ ($-1$ in hydrides)").scale(1.0).shift(band_shift(2) + DOWN * 0.2)
        b2_l4 = Tex(r"5. O: $-2$ ($-1$ in peroxides)").scale(1.0).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l1))
        self.wait(1.5)
        self.play(Write(b2_l2))
        self.wait(1.5)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("6. Sum = 0 in a compound,").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        b2_l6 = Tex("= the charge in an ion — the solver").scale(1.05).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5))
        self.wait(1.5)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the practice set worked ---
        self.next_band(3)
        b3_t = Tex("The practice set, worked").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"NH_3: \; N = -3 \qquad H_2S: \; S = -2").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"SO_2: \; S = +4 \qquad SO_4^{2-}: \; S = +6").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Same element, $-2$ to $+6$ — that is why").scale(0.95).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex("sulphur chemistry fills factories").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l3))
        self.wait(1.5)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"Na_2O_2: \; O = -1 \text{ (peroxide!)}").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        b3_l6 = MathTex(r"KMnO_4: \; +1, \; -8, \; \text{so } Mn = +7").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.wait(2)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): OIL RIG and the copper-silver audit ---
        self.next_band(4)
        b4_t = Tex("OIL RIG: Oxidation Is Loss, Reduction Is Gain").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.play(Create(SurroundingRectangle(b4_t, color=GREEN)))
        self.wait(2.5)
        b4_eq = MathTex(r"Cu + 2Ag^{+} \rightarrow Cu^{2+} + 2Ag").scale(1.15).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_eq))
        self.wait(2)
        b4_l1 = MathTex(r"Cu: \; 0 \rightarrow +2 \; \text{(lost 2e}^-\text{): oxidised}").scale(1.0).shift(band_shift(4) + UP * 0.1)
        b4_l2 = MathTex(r"Ag: \; +1 \rightarrow 0 \; \text{(gained e}^-\text{): reduced}").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Simultaneous and inseparable:").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        b4_l4 = Tex("every electron lost is an electron gained").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l3))
        self.wait(1.5)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): the agents, named without inversion ---
        self.next_band(5)
        b5_t = Tex("Agents: named for what they do to the OTHER").scale(1.0).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("Oxidising agent takes electrons — is REDUCED").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("Reducing agent donates — is OXIDISED").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex(r"Here: $Ag^{+}$ oxidising agent, $Cu$ reducing").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = MathTex(r"2Mg + O_2 \rightarrow 2MgO").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        b5_l5 = Tex(r"Mg: $0$ to $+2$ oxidised; O: $0$ to $-2$ reduced").scale(0.95).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): half-reactions, electrons matched ---
        self.next_band(6)
        b6_t = Tex("Half-reactions: table, reverse, match").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Reversed (donor): } Mg \rightarrow Mg^{2+} + 2e^-").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"\text{Reduction: } Fe^{3+} + 3e^- \rightarrow Fe").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex(r"Electrons 2 vs 3 — LCM is 6:").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.wait(1.5)
        b6_l4 = MathTex(r"3Mg \rightarrow 3Mg^{2+} + 6e^-").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        b6_l5 = MathTex(r"2Fe^{3+} + 6e^- \rightarrow 2Fe").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): add, cancel, audit ---
        self.next_band(7)
        b7_t = Tex("Add, cancel the electrons, audit").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_eq = MathTex(r"3Mg + 2Fe^{3+} \rightarrow 3Mg^{2+} + 2Fe").scale(1.15).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_eq))
        self.play(Create(SurroundingRectangle(b7_eq, color=GREEN)))
        self.wait(2.5)
        b7_l1 = Tex(r"Atoms: Mg 3 = 3, Fe 2 = 2;").scale(1.0).shift(band_shift(7) + UP * 0.1)
        b7_l2 = MathTex(r"\text{charge: } +6 = +6 \; \checkmark").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l1))
        self.wait(1.5)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_wrong = MathTex(r"3Mg + 2Fe^{3+} \rightarrow 3Mg^{2+} + 2Fe + 6e^-").scale(0.9).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_l3 = Tex("Electrons never appear in the final answer").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l3))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): salt as a full name ---
        self.next_band(8)
        b8_t = Tex("Assembling a salt like a full name").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("First name from the base,").scale(1.05).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("surname from the acid").scale(1.05).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.wait(1.5)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Three costumes: hydroxide, oxide,").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("carbonate — only the carbonate fizzes").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3))
        self.wait(1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = MathTex(r"Mg^{2+} + 2NO_3^- \Rightarrow Mg(NO_3)_2, \; 2HNO_3").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): every atom gets an account ---
        self.next_band(9)
        b9_t = Tex("Every atom gets an account").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"Habits: H at $+1$, O at $-2$; element 0;").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("the books must sum to zero").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = MathTex(r"H_2S: \; S = -2 \;\rightarrow\; SO_4^{2-}: \; S = +6").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("An eight-unit swing: those reactions moved").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        b9_l5 = Tex("serious electrons").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l4))
        self.wait(1.5)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Balance up = paid; balance down = collected").scale(0.95).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): coins change pockets ---
        self.next_band(10)
        b10_t = Tex("Coins change pockets — trade must balance").scale(1.05).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex(r"Cu paid 2e$^-$: oxidised (reducing agent)").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"$Ag^{+}$ collected: reduced (oxidising agent)").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("The pickpocket is named by the victim's loss").scale(0.95).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("Mg pays in 2s, $Fe^{3+}$ collects in 3s: run 6 coins").scale(0.9).shift(band_shift(10) + DOWN * 1.5)
        b10_l5 = MathTex(r"3Mg + 2Fe^{3+} \rightarrow 3Mg^{2+} + 2Fe").scale(1.05).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(2)
        b10_l6 = Tex("Never leave a coin lying in the equation").scale(1.0).shift(band_shift(10) + DOWN * 3.3)
        self.play(Write(b10_l6))
        self.wait(4)
