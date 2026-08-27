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


class OxidationNumbersRedoxSession(MovingCameraScene):
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
        b0_e1 = MathTex(r"KOH + HNO_3 \rightarrow KNO_3 + H_2O").scale(1.0).shift(UP * 0.3)
        b0_e2 = MathTex(r"CuO + H_2SO_4 \rightarrow CuSO_4 + H_2O").scale(1.0).shift(DOWN * 0.6)
        b0_e3 = MathTex(r"CaCO_3 + 2HCl \rightarrow CaCl_2 + H_2O + CO_2").scale(0.95).shift(DOWN * 1.5)
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
        b1_e1 = MathTex(r"2NaOH + H_2SO_4 \rightarrow Na_2SO_4 + 2H_2O").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_e1))
        self.wait(2)
        b1_l1 = Tex("Diprotic acid needs TWO hydroxides").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = MathTex(r"Ca^{2+} + 2Cl^- \Rightarrow CaCl_2").scale(1.05).shift(band_shift(1) + DOWN * 0.8)
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
        b3_l1 = MathTex(r"H_2O: \; 2(+1) + (-2) = 0").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"CH_4: \; C = -4 \qquad CO_2: \; C = +4").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Same element, $-4$ to $+4$ — that is why").scale(0.95).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex("carbon chemistry is so rich").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l3))
        self.wait(1.5)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"H_2O_2: \; O = -1 \text{ (peroxide!)}").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        b3_l6 = MathTex(r"HOCl: \; +1, \; -2, \; \text{so } Cl = +1").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.wait(2)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): OIL RIG and the zinc-copper audit ---
        self.next_band(4)
        b4_t = Tex("OIL RIG: Oxidation Is Loss, Reduction Is Gain").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.play(Create(SurroundingRectangle(b4_t, color=GREEN)))
        self.wait(2.5)
        b4_eq = MathTex(r"Zn + Cu^{2+} \rightarrow Zn^{2+} + Cu").scale(1.15).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_eq))
        self.wait(2)
        b4_l1 = MathTex(r"Zn: \; 0 \rightarrow +2 \; \text{(lost 2e}^-\text{): oxidised}").scale(1.0).shift(band_shift(4) + UP * 0.1)
        b4_l2 = MathTex(r"Cu: \; +2 \rightarrow 0 \; \text{(gained 2e}^-\text{): reduced}").scale(1.0).shift(band_shift(4) + DOWN * 0.8)
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
        b5_l3 = Tex(r"Here: $Cu^{2+}$ oxidising agent, $Zn$ reducing").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = MathTex(r"CH_4 + 2O_2 \rightarrow CO_2 + 2H_2O").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        b5_l5 = Tex(r"C: $-4$ to $+4$ oxidised; O: $0$ to $-2$ reduced").scale(0.95).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): half-reactions, electrons matched ---
        self.next_band(6)
        b6_t = Tex("Half-reactions: table, reverse, match").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = MathTex(r"\text{Reversed (donor): } Al \rightarrow Al^{3+} + 3e^-").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = MathTex(r"\text{Reduction: } Cu^{2+} + 2e^- \rightarrow Cu").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex(r"Electrons 3 vs 2 — LCM is 6:").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        self.play(Write(b6_l3))
        self.wait(1.5)
        b6_l4 = MathTex(r"2Al \rightarrow 2Al^{3+} + 6e^-").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        b6_l5 = MathTex(r"3Cu^{2+} + 6e^- \rightarrow 3Cu").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): add, cancel, audit ---
        self.next_band(7)
        b7_t = Tex("Add, cancel the electrons, audit").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_eq = MathTex(r"2Al + 3Cu^{2+} \rightarrow 2Al^{3+} + 3Cu").scale(1.15).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_eq))
        self.play(Create(SurroundingRectangle(b7_eq, color=GREEN)))
        self.wait(2.5)
        b7_l1 = Tex(r"Atoms: Al 2 = 2, Cu 3 = 3;").scale(1.0).shift(band_shift(7) + UP * 0.1)
        b7_l2 = MathTex(r"\text{charge: } +6 = +6 \; \checkmark").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l1))
        self.wait(1.5)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_wrong = MathTex(r"2Al + 3Cu^{2+} \rightarrow 2Al^{3+} + 3Cu + 6e^-").scale(0.9).shift(band_shift(7) + DOWN * 1.7)
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
        b8_l5 = MathTex(r"Ca^{2+} + 2Cl^- \Rightarrow CaCl_2, \; 2HCl").scale(1.0).shift(band_shift(8) + DOWN * 2.3)
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
        b9_l3 = MathTex(r"CH_4: \; C = -4 \;\rightarrow\; CO_2: \; C = +4").scale(1.0).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("An eight-unit swing: combustion moved").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
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
        b10_l1 = Tex(r"Zn paid 2e$^-$: oxidised (reducing agent)").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"$Cu^{2+}$ collected: reduced (oxidising agent)").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("The pickpocket is named by the victim's loss").scale(0.95).shift(band_shift(10) + DOWN * 0.6)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("Al pays in 3s, Cu collects in 2s: run 6 coins").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        b10_l5 = MathTex(r"2Al + 3Cu^{2+} \rightarrow 2Al^{3+} + 3Cu").scale(1.05).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(2)
        b10_l6 = Tex("Never leave a coin lying in the equation").scale(1.0).shift(band_shift(10) + DOWN * 3.3)
        self.play(Write(b10_l6))
        self.wait(4)
