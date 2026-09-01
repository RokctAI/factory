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

# Band-layout whiteboard scene for the IEB grade 12 accounting session duo
# "VAT Control and the Amount Owed to SARS". One band per teaching beat;
# camera moves down, earlier work stays. Exporter-safe mobjects only;
# write-only reveals — no Transform/FadeOut/sub-part indexing on MathTex.
#
# Subtopic time shares (subtopics.json, total 1555 s):
# 235/245/230/230 expert, 195/210/210 simplifier.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class VatControlAndSarsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the machinery, both calculations ---
        title = Tex("VAT Control and the Amount Owed to SARS").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Output tax: charged to customers — SARS's money").scale(1.0).shift(UP * 1.3)
        b0_l2 = Tex(r"Input tax: paid to suppliers — claimable back").scale(1.0).shift(UP * 0.5)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Exclusive R3\,000: VAT $= 15\% = $ R450").scale(1.05).shift(DOWN * 0.4)
        b0_l4 = MathTex(r"\text{Inclusive } 3\,450 \times \tfrac{15}{115} = R450").scale(1.05).shift(DOWN * 1.3)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_wrong = MathTex(r"15\% \times 3\,450 = R517{,}50").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_wrong))
        self.play(Create(strike(b0_wrong)))
        b0_l5 = Tex("Zero-rated: in the system at 0\\%; exempt: outside it").scale(0.9).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_2): the plain streams ---
        self.next_band(1)
        b1_title = Tex("Naledi Building Supplies: one VAT period").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Sales R380\,000 excl.\ $\Rightarrow$ output R57\,000").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"Purchases R260\,000 excl.\ $\Rightarrow$ input R39\,000").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"Plain difference: R18\,000 — but it never stops there").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Returns R16\,000: output $-$ R2\,400").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        b1_l5 = Tex(r"Drawings R4\,000: owed $+$ R600").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        b1_l6 = Tex(r"Bad debts R6\,900 incl.: $\tfrac{15}{115} =$ R900 relief").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.wait(2)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): assembling the amount owed ---
        self.next_band(2)
        b2_title = Tex("Assemble the period").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Output: } 57\,000 - 2\,400 + 600 = 55\,200").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Input: } 39\,000 + 900 = 39\,900").scale(1.05).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"55\,200 - 39\,900 = R15\,300 \text{ payable}").scale(1.1).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex(r"Input $>$ output flips it into a REFUND receivable").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_3): the VAT control account ---
        self.next_band(3)
        b3_title = Tex("VAT Control — the slate with SARS").scale(1.15).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        # T-account rails first (prescribed format), then post the figures
        t_top = Line(LEFT * 4.4, RIGHT * 4.4).shift(band_shift(3) + UP * 1.7)
        t_mid = Line(UP * 1.7, DOWN * 2.0).shift(band_shift(3))
        self.play(Create(t_top), Create(t_mid))
        b3_dh = Tex("Debit (owed back)").scale(0.85).shift(band_shift(3) + UP * 1.3 + LEFT * 2.3)
        b3_ch = Tex("Credit (owed to SARS)").scale(0.85).shift(band_shift(3) + UP * 1.3 + RIGHT * 2.3)
        self.play(Write(b3_dh), Write(b3_ch))
        self.wait(2)
        b3_c1 = Tex(r"Opening balance 9\,800").scale(0.8).shift(band_shift(3) + UP * 0.6 + RIGHT * 2.3)
        self.play(Write(b3_c1))
        self.wait(1.5)
        b3_d1 = Tex(r"Bank (payment) 9\,800").scale(0.8).shift(band_shift(3) + UP * 0.6 + LEFT * 2.3)
        self.play(Write(b3_d1))
        self.wait(1.5)
        b3_c2 = Tex(r"Output tax 57\,000").scale(0.8).shift(band_shift(3) + UP * 0.0 + RIGHT * 2.3)
        b3_c3 = Tex(r"Drawings 600").scale(0.8).shift(band_shift(3) + DOWN * 0.6 + RIGHT * 2.3)
        self.play(Write(b3_c2))
        self.play(Write(b3_c3))
        self.wait(2)
        b3_d2 = Tex(r"Input tax 39\,000").scale(0.8).shift(band_shift(3) + UP * 0.0 + LEFT * 2.3)
        b3_d3 = Tex(r"Returns 2\,400").scale(0.8).shift(band_shift(3) + DOWN * 0.6 + LEFT * 2.3)
        b3_d4 = Tex(r"Bad debts 900").scale(0.8).shift(band_shift(3) + DOWN * 1.2 + LEFT * 2.3)
        self.play(Write(b3_d2))
        self.play(Write(b3_d3))
        self.play(Write(b3_d4))
        self.wait(2)
        b3_bal = Tex(r"Balance: CREDIT R15\,300 — a current liability").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_bal))
        self.play(Create(SurroundingRectangle(b3_bal, color=GREEN)))
        b3_l5 = Tex("No valid tax invoice, no input claim").scale(0.9).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): ethics, fraud, duty ---
        self.next_band(4)
        b4_title = Tex("VAT collected is NEVER the vendor's money").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex("Under-declaring output — off-the-books cash sales").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("Inflating input — ghost suppliers, private costs").scale(0.95).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex("Failing to pay over — charging VAT and keeping it").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("False refund claims — engineering the period").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Controls: daily till reconciliation, sequential").scale(0.9).shift(band_shift(4) + DOWN * 2.0)
        b4_l6 = Tex("invoices, valid tax invoices, reviewed returns").scale(0.9).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(2)
        b4_l7 = Tex("A false return must be refused — no instruction changes that").scale(0.85).shift(band_shift(4) + DOWN * 3.2)
        self.play(Write(b4_l7))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the fifteen cents that was never yours ---
        self.next_band(5)
        b5_title = Tex("The R6 that was never Farida's").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"Sugar R46 $=$ R40 shop $+$ R6 SARS").scale(1.0).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex(r"Before-tax R300: $+15\% \Rightarrow$ R45 tax, R345 shelf").scale(0.95).shift(band_shift(5) + UP * 0.3)
        b5_l3 = MathTex(r"\text{Shelf } 46 \times \tfrac{15}{115} = R6").scale(1.05).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_wrong = Tex(r"15\% of the shelf price — taxing the tax").scale(0.95).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l4 = Tex("Brown bread, maize meal, eggs: zero-rated;").scale(0.95).shift(band_shift(5) + DOWN * 2.4)
        b5_l5 = Tex("the flat's rent: exempt — never in the building").scale(0.95).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_6): collected in, paid out, what remains ---
        self.next_band(6)
        b6_title = Tex("Collected in, paid out, what remains").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Collected: $15\% \times 38\,000 = $ R5\,700").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"Paid to vendors: $15\% \times 26\,000 = $ R3\,900").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"5\,700 - 3\,900 = R1\,800 \text{ owed}").scale(1.05).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex(r"Check: value added R12\,000; $15\% = $ R1\,800").scale(0.95).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex(r"Nudges: returns down, drawings up, bad debts down").scale(1.0).shift(band_shift(6) + DOWN * 2.3)
        b6_l6 = Tex("Big freezer month: the slate points back at SARS").scale(0.95).shift(band_shift(6) + DOWN * 3.1)
        self.play(Write(b6_l5))
        self.wait(2.5)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_7): why cheating VAT is stealing twice ---
        self.next_band(7)
        b7_title = Tex("Why cheating VAT is stealing twice").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_wrong = Tex("The brother-in-law's advice: keep two tills").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_l1 = Tex("Once from SARS; once from the community").scale(1.0).shift(band_shift(7) + UP * 0.3)
        b7_l2 = Tex("the clinic queue, the feeding scheme, the grants").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Caught boringly: the wholesaler's return shows her").scale(0.95).shift(band_shift(7) + DOWN * 1.3)
        b7_l4 = Tex("purchases; invoice gaps ask; bankings ask louder").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("VAT is held in trust; evasion is theft from the state").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(4)
