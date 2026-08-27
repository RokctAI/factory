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

# Band-layout whiteboard scene for the IEB grade 12 accounting session duo
# "Companies Statements and Analysis Essentials" — revision of the whole
# company story on one set of figures (Kiepersol Limited), with the
# simplifier part retelling it as a family pizzeria. Exporter-safe mobjects
# only; write-only reveals — no Transform/FadeOut/sub-part indexing on
# MathTex.
#
# Subtopic time shares (subtopics.json, total 1565 s):
# 240/240/230/240/205/205/205 — subtopic_2 gets two bands (note + drill).

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

        # --- Band 0 (subtopic_1): the income statement chain ---
        title = Tex("The income statement chain").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Sales 4\,500\,000 $-$ COS 3\,000\,000 $=$ GP R1\,500\,000").scale(0.85).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex(r"(mark-up check: 50\% on cost — figures agree)").scale(0.85).shift(UP * 0.5)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex(r"$+$ other income 60\,000; $-$ expenses 760\,000").scale(0.85).shift(DOWN * 0.3)
        b0_l4 = Tex(r"Operating profit R800\,000; $+$ interest 20\,000").scale(0.85).shift(DOWN * 1.0)
        b0_l5 = Tex(r"$-$ interest expense 120\,000 $\Rightarrow$ NPBT R700\,000").scale(0.85).shift(DOWN * 1.7)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(2.5)
        b0_l6 = Tex(r"Tax $27\% = 189\,000$; NPAT R511\,000 — EPS 70c").scale(0.9).shift(DOWN * 2.6)
        self.play(Write(b0_l6))
        self.play(Create(SurroundingRectangle(b0_l6, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): share capital and the buy-back drill ---
        self.next_band(1)
        b1_title = Tex("Share capital and the buy-back drill").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"600\,000 shares, R2\,244\,000; issue 130\,000 @ R5,20").scale(0.85).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"730\,000 shares, R2\,920\,000 — average R4,00").scale(0.9).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.wait(2.5)
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"Buy back 30\,000 @ R4,60 (average R4,00):").scale(0.9).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex(r"Capital $-$ 30\,000 $\times$ 4,00 $=$ R120\,000").scale(0.9).shift(band_shift(1) + DOWN * 1.3)
        b1_l5 = Tex(r"Retained income $-$ 30\,000 $\times$ 0,60 $=$ R18\,000").scale(0.9).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex(r"Bank $-$ R138\,000; check: $120 + 18 = 138$").scale(0.9).shift(band_shift(1) + DOWN * 2.9)
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
        b2_l1 = Tex(r"Opening R350\,000 $+$ NPAT R511\,000").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"$-$ Dividends R328\,500:").scale(0.95).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex(r"interim 20c $\times$ 730\,000 $=$ 146\,000 (paid)").scale(0.9).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex(r"final 25c $\times$ 730\,000 $=$ 182\,500 (declared, unpaid)").scale(0.85).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = MathTex(r"350\,000 + 511\,000 - 328\,500 = 532\,500").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(2)
        b2_l6 = Tex(r"Equity: $2\,920\,000 + 532\,500 = $ R3\,452\,500").scale(0.9).shift(band_shift(2) + DOWN * 2.9)
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
        b3_l1 = MathTex(r"\text{Tax paid: } 189\,000 + 12\,000 - 18\,000 = 183\,000").scale(0.9).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex(r"Dividends paid: last final 130\,000 $+$ interim 146\,000").scale(0.85).shift(band_shift(3) + DOWN * 0.6)
        b3_l3 = Tex(r"$=$ R276\,000; this final R182\,500 stays behind").scale(0.9).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex(r"Financing: shares in R676\,000; loan unchanged —").scale(0.9).shift(band_shift(3) + DOWN * 2.2)
        b3_l5 = Tex("funding growth with equity, not debt").scale(0.9).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): the indicators ---
        self.next_band(4)
        b4_title = Tex("Quote, compare, judge").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Current 2,1:1; acid-test 1,2:1 — healthy").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"Stock turns 8$\times$; debtors 36,5 days — one caution").scale(0.9).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"ROSHE 16,9\% vs the bank's $\sim$8\% — well paid").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"ROTCE 20,4\% vs loan at 12\% — positive gearing").scale(0.9).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex(r"NAV 473c vs price 540c: 67c premium for the future").scale(0.85).shift(band_shift(4) + DOWN * 2.1)
        b4_l6 = Tex(r"EPS 70c; DPS 45c; pay-out $\sim$64\%").scale(0.9).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.wait(2)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_5): the pizzeria's year on one page ---
        self.next_band(5)
        b5_title = Tex("The pizzeria's year on one page").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Pizzas R4\,500\,000; flour and ovens R3\,000\,000").scale(0.9).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Cooking made R1\,500\,000; running took R760\,000").scale(0.9).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Tax collector: 27c in the rand $=$ R189\,000").scale(0.9).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex(r"Kept profit: R511\,000 across 730\,000 slices").scale(0.9).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex(r"Each slice earned 70c; paid 45c; kept 25c").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_6): following the cash, not the profit ---
        self.next_band(6)
        b6_title = Tex("Following the cash, not the profit").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Tax clock: settled old R12\,000; R18\,000 waits —").scale(0.9).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"cash out R183\,000, not the R189\,000 charge").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Dividend clock: 130\,000 $+$ 146\,000 left the till;").scale(0.9).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex(r"the R182\,500 promise has not").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex(r"Growth clock: cousins paid R676\,000 for new slices").scale(0.9).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex("The scooters die in profit, never at the till — watch both").scale(0.85).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.wait(2)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_7): three questions before buying a slice ---
        self.next_band(7)
        b7_title = Tex("Three questions before you buy a slice").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"1. Book worth: $\tfrac{3\,452\,500}{730\,000} \approx 473$c;").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"cousins pay 540c — 67c buys the future").scale(0.9).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2.5)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"2. Family money: 16,9c per rand vs the bank's 8c").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"3. The pot earns 20,4c; the loan costs 12c —").scale(0.9).shift(band_shift(7) + DOWN * 1.2)
        b7_l5 = Tex("borrowed rands work FOR the family, for now").scale(0.9).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(2.5)
        b7_l6 = Tex("Every indicator: quote, compare, judge").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(4)
