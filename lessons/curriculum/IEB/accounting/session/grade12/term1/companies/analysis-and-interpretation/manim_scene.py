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

# Band-layout whiteboard scene for "Analysis and Interpretation" (grade 12,
# term 1, companies). One band per teaching beat; the camera moves down and
# nothing is removed. Part 1 (Expert) = subtopics 1-4, Part 2 (Simplifier)
# = subtopics 5-7. Exporter-safe primitives only; write-only reveals.
# Subtopic durations 235/245/240/230/200/210/210 of 1570 s guide the
# apportioning. Worked figures follow Bokamoso Limited.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AnalysisInterpretationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): liquidity on Bokamoso's figures ---
        title = Tex("Analysis and Interpretation").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Current assets R880 000 vs").scale(1.0).shift(UP * 1.3)
        b0_l2 = Tex("current liabilities R400 000").scale(1.0).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Current ratio: 2,2 to 1").scale(1.0).shift(DOWN * 0.3)
        b0_l4 = Tex("Acid-test (no stock): 500 000 vs 400 000").scale(0.95).shift(DOWN * 1.1)
        b0_l5 = Tex("$=$ 1,25 to 1").scale(1.0).shift(DOWN * 1.9)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.wait(2.5)
        b0_l6 = Tex("Solvency: assets R4 450 000 vs").scale(0.95).shift(DOWN * 2.7)
        b0_l7 = Tex("liabilities R1 450 000 $=$ 3,1 to 1").scale(0.95).shift(DOWN * 3.4)
        self.play(Write(b0_l6))
        self.play(Write(b0_l7))
        self.wait(3)

        # --- Band 1 (subtopic_1): the operating cycle, read together ---
        self.next_band(1)
        b1_t = Tex("The operating cycle, read together").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Stock turnover: 2 850 000 $\\div$ 380 000").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("$=$ 7,5 times ($\\approx$ 49 days on the shelf)").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Debtors: 360 000 $\\div$ 4 380 000 $\\times$ 365").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("$=$ 30 days, on terms to the day").scale(0.95).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("Creditors: 400 000 $\\div$ 2 800 000 $\\times$ 365").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex("$\\approx$ 52 days: suppliers finance").scale(0.95).shift(band_shift(1) + DOWN * 2.8)
        b1_l7 = Tex("the debtors' book — within terms only").scale(0.95).shift(band_shift(1) + DOWN * 3.5)
        self.play(Write(b1_l5))
        self.wait(2)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): ROSHE and ROTCE ---
        self.next_band(2)
        b2_t = Tex("ROSHE and ROTCE").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("ROSHE: what did MY money earn?").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("438 000 $\\div$ avg equity 2 920 000 $=$ 15\\%").scale(0.95).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("vs fixed deposit $\\approx$ 8\\%: risk rewarded").scale(0.95).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("ROTCE: what does the whole pot earn?").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex("(600 000 $+$ 120 000) $\\div$ 4 000 000 $=$ 18\\%").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        b2_l6 = Tex("before tax, before interest: the engine").scale(0.9).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): the per-share four ---
        self.next_band(3)
        b3_t = Tex("The per-share four").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex("EPS: 438 000 $\\div$ 600 000 $=$ 73c earned").scale(0.95).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("DPS: 348 000 $\\div$ 600 000 $=$ 58c paid").scale(0.95).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("(interim 25c $+$ final 33c)").scale(0.9).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("Pay-out: 58 $\\div$ 73 $\\approx$ 80\\% out, rest kept").scale(0.95).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("NAV: 3 000 000 $\\div$ 600 000 $=$ 500c —").scale(0.95).shift(band_shift(3) + DOWN * 2.1)
        b3_l6 = Tex("what the books say a share is worth").scale(0.95).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): should Bokamoso borrow more? ---
        self.next_band(4)
        b4_t = Tex("Should Bokamoso borrow more?").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("Debt-equity: 1 050 000 : 3 000 000 $=$ 0,35 : 1").scale(0.9).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("ROTCE 18\\% vs loan cost $\\approx$ 11\\%").scale(1.0).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("each borrowed rand earns 18c, costs 11c").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("POSITIVE gearing — room to expand").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = Tex("State the risk too: interest is fixed,").scale(0.95).shift(band_shift(4) + DOWN * 2.2)
        b4_l6 = Tex("owed in the bad years as well").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): the share price and the scorecard ---
        self.next_band(5)
        b5_t = Tex("The price and the scorecard").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("JSE price 620c vs NAV 500c:").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("120c premium $=$ the market pricing").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("the future the books cannot show").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("ROSHE 15\\% vs 8\\%; EPS 73c covers DPS 58c").scale(0.9).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_trap = Tex("Rising EPS after a buy-back $=$ improvement?").scale(0.9).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_trap))
        self.play(Create(strike(b5_trap)))
        b5_l5 = Tex("fewer shares flatter the ratio — check").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the published annual report ---
        self.next_band(6)
        b6_t = Tex("Reading a published annual report").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Directors' report: the players'").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("own match report — read critically").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Auditor's report: find the opinion FIRST").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("Summarised statements: same skills apply").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Governance: pay disclosed, committees,").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex("King Code: responsibility, accountability,").scale(0.9).shift(band_shift(6) + DOWN * 2.8)
        b6_l7 = Tex("fairness, transparency").scale(0.9).shift(band_shift(6) + DOWN * 3.5)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # --- Band 7 (subtopic_4): the discipline ---
        self.next_band(7)
        b7_t = Tex("The interpretation discipline").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Audit opinion first: a qualification on stock").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("contaminates every stock-based ratio").scale(0.9).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Pay up while EPS falls: a governance").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("question for the AGM; insider trading").scale(0.9).shift(band_shift(7) + DOWN * 1.1)
        b7_l5 = Tex("and price manipulation: illegal").scale(0.9).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2.5)
        b7_l6 = Tex("FIGURE $\\to$ COMPARISON $\\to$ JUDGEMENT").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        b7_l7 = Tex("three sentences, full marks").scale(0.9).shift(band_shift(7) + DOWN * 3.5)
        self.play(Write(b7_l7))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the company's report card ---
        self.next_band(8)
        b8_t = Tex("The butchery's report card").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Bills this month: R2,20 ready per rand owed").scale(0.9).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("(R1,25 even if no more chops sell)").scale(0.9).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Speeds: stock turns 7,5 times; customers").scale(0.9).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("pay in 30 days; suppliers wait 52 —").scale(0.9).shift(band_shift(8) + DOWN * 1.1)
        b8_l5 = Tex("their patience carries the book").scale(0.9).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex("Storms: owns three times what it owes").scale(0.9).shift(band_shift(8) + DOWN * 2.7)
        b8_l7 = Tex("Never asked: is the profit big? Compare first.").scale(0.85).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): whose money works harder? ---
        self.next_band(9)
        b9_t = Tex("Whose money works harder?").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("The engine: 18c per rand in the pot (ROTCE)").scale(0.9).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("The bank takes its 11\\% first, always").scale(0.9).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex("The family keeps 15c per rand (ROSHE)").scale(0.9).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Borrow at 11, earn at 18: every borrowed").scale(0.9).shift(band_shift(9) + DOWN * 1.2)
        b9_l5 = Tex("rand works for the family — gearing").scale(0.9).shift(band_shift(9) + DOWN * 1.9)
        b9_l6 = Tex("but debt amplifies bad years too").scale(0.9).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(2.5)
        b9_l7 = Tex("Fixed-deposit test: 15\\% vs 8\\% — risk paid for").scale(0.85).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_7): the price and the value ---
        self.next_band(10)
        b10_t = Tex("The price and the value").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Books: 500c a share (NAV, winding-up answer)").scale(0.85).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("Cousins pay: 620c — buying the FUTURE,").scale(0.9).shift(band_shift(10) + UP * 0.5)
        b10_l3 = Tex("which no balance sheet can show").scale(0.9).shift(band_shift(10) + DOWN * 0.2)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Each share: earned 73c, paid 58c —").scale(0.9).shift(band_shift(10) + DOWN * 1.1)
        b10_l5 = Tex("15c stayed and thickened every share").scale(0.9).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex("Pay-out $\\approx$ 80\\%: grandmother happy;").scale(0.9).shift(band_shift(10) + DOWN * 2.7)
        b10_l7 = Tex("figure, comparison, judgement — always").scale(0.9).shift(band_shift(10) + DOWN * 3.4)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(4)
