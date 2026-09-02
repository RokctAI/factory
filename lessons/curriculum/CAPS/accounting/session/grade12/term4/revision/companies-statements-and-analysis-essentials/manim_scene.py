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

# Band-layout whiteboard scene for the CAPS grade 12 accounting session duo
# "Companies Statements and Analysis Essentials" (term 4 revision). One band
# per teaching beat; camera moves down, earlier work stays. Exporter-safe
# mobjects only; write-only reveals — no Transform/FadeOut/sub-part indexing.
#
# Subtopic time shares (subtopics.json, total 1565 s):
# 240/240/230/240 expert, 205/205/205 simplifier.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CompaniesStatementsEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the income statement chain ---
        title = Tex("Companies: Statements and Analysis").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Sales 3\,600\,000 $-$ COS 2\,400\,000 $=$ GP 1\,200\,000").scale(0.9).shift(UP * 1.3)
        b0_l2 = Tex(r"Mark-up check: $\tfrac{1\,200\,000}{2\,400\,000} = 50\%$ on cost").scale(0.95).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"$+$ Other income 40\,000; $-$ expenses 600\,000").scale(0.9).shift(DOWN * 0.5)
        b0_l4 = Tex(r"Operating profit 640\,000; $+$10\,000; $-$50\,000").scale(0.9).shift(DOWN * 1.3)
        b0_l5 = Tex(r"Net profit before tax: R600\,000").scale(0.95).shift(DOWN * 2.1)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(2)
        b0_l6 = Tex(r"Tax $27\% = 162\,000$; NPAT R438\,000").scale(0.95).shift(DOWN * 2.9)
        self.play(Write(b0_l6))
        self.play(Create(SurroundingRectangle(b0_l6, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): share capital and the buy-back drill ---
        self.next_band(1)
        b1_title = Tex("Share capital and the buy-back drill").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"500\,000 shares, R1\,500\,000; issue 100\,000 @ R4,50").scale(0.85).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"600\,000 shares, R1\,950\,000 — average R3,25").scale(0.9).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex(r"Buy back 40\,000 @ R4,00 (average R3,25):").scale(0.9).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex(r"Capital $-$ 40\,000 $\times$ 3,25 $=$ R130\,000").scale(0.9).shift(band_shift(1) + DOWN * 1.3)
        b1_l5 = Tex(r"Retained income $-$ 40\,000 $\times$ 0,75 $=$ R30\,000").scale(0.9).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex(r"Bank $-$ R160\,000; check: $130 + 30 = 160$").scale(0.9).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.wait(2)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): retained income note ---
        self.next_band(2)
        b2_title = Tex("Retained income: the appropriation story").scale(1.05).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Opening R288\,000 $+$ NPAT R438\,000").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"$-$ Dividends R324\,000:").scale(0.95).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex(r"interim 24c $\times$ 600\,000 $=$ 144\,000 (paid)").scale(0.9).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex(r"final 30c $\times$ 600\,000 $=$ 180\,000 (declared, unpaid)").scale(0.85).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l2))
        self.wait(1.5)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = MathTex(r"288\,000 + 438\,000 - 324\,000 = 402\,000").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        b2_l6 = Tex(r"Equity: $1\,950\,000 + 402\,000 = $ R2\,352\,000").scale(0.9).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_3): cash flow signposts + three workings ---
        self.next_band(3)
        b3_title = Tex("Cash flow: the three workings").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_wrong = Tex(r"Tax paid $=$ the tax charge").scale(0.95).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Tax paid: } 162\,000 + 15\,000 - 21\,000 = 156\,000").scale(0.9).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_l2 = Tex(r"Dividends paid: last final 150\,000 $+$ interim 144\,000").scale(0.85).shift(band_shift(3) + DOWN * 0.6)
        b3_l3 = Tex(r"$=$ R294\,000; this final R180\,000 stays behind").scale(0.9).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"Financing: shares in R450\,000; loan unchanged —").scale(0.9).shift(band_shift(3) + DOWN * 2.2)
        b3_l5 = Tex("funding growth with equity, not debt").scale(0.9).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): the indicators ---
        self.next_band(4)
        b4_title = Tex("Quote, compare, judge").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Current 2,3:1; acid-test 1,3:1 — healthy").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"Stock turns 8$\times$; debtors 36,5 days — one caution").scale(0.9).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"ROSHE 21,2\% vs the bank's $\sim$8\% — richly paid").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"ROTCE 25,3\% vs loan at 10\% — positive gearing").scale(0.9).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = Tex(r"NAV 392c vs price 460c: 68c premium for the future").scale(0.85).shift(band_shift(4) + DOWN * 2.1)
        b4_l6 = Tex(r"EPS 73c; DPS 54c; pay-out $\sim$74\%").scale(0.9).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.wait(2)
        self.play(Write(b4_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): the bakery's year on one page ---
        self.next_band(5)
        b5_title = Tex("The bakery's year on one page").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex(r"Bread R3\,600\,000; flour and ovens R2\,400\,000").scale(0.9).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Baking made R1\,200\,000; running took R600\,000").scale(0.9).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Tax collector: 27c in the rand $=$ R162\,000").scale(0.9).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex(r"Kept profit: R438\,000 across 600\,000 slices").scale(0.9).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex(r"Each slice earned 73c; paid 54c; kept 19c").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_6): following the cash, not the profit ---
        self.next_band(6)
        b6_title = Tex("Following the cash, not the profit").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Tax clock: settled old R15\,000; R21\,000 waits —").scale(0.9).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"cash out R156\,000, not the R162\,000 charge").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Dividend clock: 150\,000 $+$ 144\,000 left the till;").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex(r"the R180\,000 promise has not").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex(r"Growth clock: cousins paid R450\,000 for new slices").scale(0.9).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex("The van dies in profit, never at the till — watch both").scale(0.85).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.wait(2)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_7): three questions before buying a slice ---
        self.next_band(7)
        b7_title = Tex("Three questions before you buy a slice").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex(r"1. Book worth: $\tfrac{2\,352\,000}{600\,000} = 392$c;").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"trades at 460c — 68c buys the future").scale(0.9).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"2. Money works harder here: 21,2c vs the bank's 8c").scale(0.9).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"3. The pot earns 25,3c; the loan eats 10c —").scale(0.9).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex("borrowed money works FOR the family").scale(0.9).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2.5)
        b7_l6 = Tex("Three comparisons, each ending in a judgement").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(4)
