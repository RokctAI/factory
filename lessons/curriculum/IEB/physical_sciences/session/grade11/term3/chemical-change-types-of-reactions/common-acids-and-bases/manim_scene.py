# Copyright (c) 2026 RokctAI
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

# Band-layout whiteboard scene for the common acids and bases session duo.
# Covers all seven subtopics (Part 1 Expert: 1-4, Part 2 Simplifier: 5-7),
# band time proportional to subtopics.json (225/230/235/240/200/195/200 of
# 1525 s). Add-only lifecycle; camera steps down one band per teaching beat.
# Only exporter-safe mobjects are used (Tex/MathTex/Line/Dot/Rectangle).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CommonAcidsAndBasesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the four acids, first two ---
        title = Tex("Nine Substances, One Chapter").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Hydrochloric acid: $HCl$").scale(1.1).shift(UP * 1.1)
        b0_l2 = Tex("stomach acid, pool acid").scale(0.95).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.wait(1.5)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex(r"Nitric acid: $HNO_3$").scale(1.1).shift(DOWN * 0.6)
        b0_l4 = Tex("the fertiliser acid").scale(0.95).shift(DOWN * 1.3)
        self.play(Write(b0_l3))
        self.wait(1.5)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("Both monoprotic: one $H^+$ per molecule").scale(1.0).shift(DOWN * 2.3)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): sulphuric and ethanoic ---
        self.next_band(1)
        b1_l1 = Tex(r"Sulphuric acid: $H_2SO_4$ — battery acid").scale(1.05).shift(band_shift(1) + UP * 2.0)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"TWO hydrogens: DIPROTIC").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = Tex(r"Ethanoic acid: $CH_3COOH$ — vinegar").scale(1.05).shift(band_shift(1) + DOWN * 0.1)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Four H printed, ONE acidic —").scale(1.0).shift(band_shift(1) + DOWN * 1.0)
        b1_l5 = Tex(r"only the H on oxygen leaves; monoprotic").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.wait(1.5)
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex("Also the standard WEAK acid").scale(1.0).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): bases one to three ---
        self.next_band(2)
        b2_t = Tex("The five bases, part one").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex(r"Sodium hydroxide: $NaOH$ — caustic soda").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"Potassium hydroxide: $KOH$ — its twin").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"Ammonia: $NH_3$ — the renegade base:").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        b2_l4 = Tex("no hydroxide, no metal, no oxygen —").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = Tex("a base because it ACCEPTS $H^+$").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l3))
        self.wait(1.5)
        self.play(Write(b2_l4))
        self.wait(1.5)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the carbonate pair ---
        self.next_band(3)
        b3_t = Tex("The carbonate pair — keep them apart").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex(r"Sodium carbonate: $Na_2CO_3$").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("washing soda — TWO Na, no H").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex(r"Sodium hydrogen carbonate: $NaHCO_3$").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("baking soda — ONE Na, one H").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("The name says it: 'hydrogen carbonate'").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the ions, and building the acids ---
        self.next_band(4)
        b4_t = Tex("Build from ions: charges total zero").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = MathTex(r"H^+ \; Na^+ \; K^+ \qquad Cl^- \; NO_3^- \; OH^- \; HCO_3^-").scale(0.9).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = MathTex(r"SO_4^{2-} \; CO_3^{2-} \text{ — the double-minus pair}").scale(0.95).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = MathTex(r"H^+ + Cl^- \rightarrow HCl \qquad H^+ + NO_3^- \rightarrow HNO_3").scale(0.9).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = MathTex(r"2H^+ + SO_4^{2-} \rightarrow H_2SO_4").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)
        b4_l5 = Tex("The subscript 2 IS the charge balance").scale(0.95).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): building the bases, spotting fakes ---
        self.next_band(5)
        b5_t = Tex("Build the bases; audit the fakes").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = MathTex(r"Na^+ + OH^- \rightarrow NaOH \qquad Na^+ + HCO_3^- \rightarrow NaHCO_3").scale(0.85).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"2Na^+ + CO_3^{2-} \rightarrow Na_2CO_3").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_w1 = MathTex(r"NaCO_3?").scale(1.05).shift(band_shift(5) + DOWN * 0.8 + LEFT * 2.5)
        b5_w2 = MathTex(r"H_2NO_3?").scale(1.05).shift(band_shift(5) + DOWN * 0.8 + RIGHT * 2.5)
        self.play(Write(b5_w1))
        self.play(Create(strike(b5_w1)))
        self.wait(1.5)
        self.play(Write(b5_w2))
        self.play(Create(strike(b5_w2)))
        self.wait(2)
        b5_l3 = Tex("One question kills them all:").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        b5_l4 = Tex("do the charges total zero?").scale(1.05).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l3))
        self.wait(1.5)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): salt takes the acid's surname ---
        self.next_band(6)
        b6_t = Tex("Acid + base = salt + water").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Metal from the BASE, surname from the ACID").scale(0.95).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = MathTex(r"KOH + HCl \rightarrow KCl + H_2O").scale(1.05).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"NaOH + HNO_3 \rightarrow NaNO_3 + H_2O").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = MathTex(r"2KOH + H_2SO_4 \rightarrow K_2SO_4 + 2H_2O").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("Diprotic acid: two hydroxides required").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): reading salts backwards ---
        self.next_band(7)
        b7_t = Tex("Read the salt backwards").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Chlorides — hydrochloric; nitrates — nitric;").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("sulphates — sulphuric; ethanoates — ethanoic").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Prepare sodium sulphate?").scale(1.05).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"sodium $\rightarrow$ NaOH; sulphate $\rightarrow$ $H_2SO_4$").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("The name holds the whole answer").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): tour of the house ---
        self.next_band(8)
        b8_t = Tex("A tour of the house in nine chemicals").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex(r"Kitchen: vinegar $CH_3COOH$, baking soda $NaHCO_3$").scale(0.85).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex(r"Laundry: washing soda $Na_2CO_3$").scale(0.9).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"Under the sink: caustic soda $NaOH$; spray $NH_3$").scale(0.85).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l2))
        self.wait(1.5)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex(r"Garage: pool acid $HCl$, battery $H_2SO_4$").scale(0.9).shift(band_shift(8) + DOWN * 1.3)
        b8_l5 = Tex(r"Farm co-op: fertiliser from $HNO_3$; plus $KOH$").scale(0.85).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): charges snap like magnets ---
        self.next_band(9)
        b9_t = Tex("Charges snap together like magnets").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Singles pair one-to-one:").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = MathTex(r"HCl, \; HNO_3, \; NaOH, \; KOH, \; NaHCO_3").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.wait(1.5)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Double-minus pieces demand two singles:").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        b9_l4 = MathTex(r"H_2SO_4, \; Na_2CO_3").scale(1.05).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l3))
        self.wait(1.5)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2)
        b9_l5 = Tex("Zero-check every formula — two seconds").scale(0.95).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): salts as compound words ---
        self.next_band(10)
        b10_t = Tex("Reading a salt like a compound word").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("First name from the base, surname from the acid").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        b10_l2 = Tex(r"Potassium chloride: KOH + HCl").scale(1.0).shift(band_shift(10) + UP * 0.3)
        b10_l3 = Tex(r"Sodium nitrate: NaOH + $HNO_3$").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex(r"Leftovers pair off: $H^+ + OH^- \rightarrow H_2O$").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Salt AND water — always both").scale(1.0).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l5))
        self.wait(4)
