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

# Band-layout whiteboard scene for "Financial Statements and Cash Flow"
# (grade 12, term 1, companies). One band per teaching beat; the camera
# moves down and nothing is removed. Part 1 (Expert) = subtopics 1-4,
# Part 2 (Simplifier) = subtopics 5-7 in fresh bands. Exporter-safe
# primitives only; write-only reveals. Subtopic durations
# 230/220/240/270/200/220/200 of 1580 s guide the apportioning.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinancialStatementsCashFlowSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): adjustments and the provision movement ---
        title = Tex("Financial Statements and Cash Flow").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Adjustments enforce MATCHING:").scale(1.05).shift(UP * 1.3)
        b0_l2 = Tex("this year's income and expenses only").scale(1.05).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Provision for bad debts: adjusted,").scale(1.0).shift(DOWN * 0.4)
        b0_l4 = Tex("not recreated — needed R12 000,").scale(1.0).shift(DOWN * 1.1)
        b0_l5 = Tex("standing R14 000: DECREASE R2 000").scale(1.05).shift(DOWN * 1.9)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(2)
        b0_l6 = Tex("Reverse LAST year's accruals first,").scale(0.95).shift(DOWN * 2.8)
        b0_l7 = Tex("or income and expenses count twice").scale(0.95).shift(DOWN * 3.5)
        self.play(Write(b0_l6))
        self.play(Write(b0_l7))
        self.wait(3)

        # --- Band 1 (subtopic_1): the appropriation traced ---
        self.next_band(1)
        b1_t = Tex("Trading, profit and loss, appropriation").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Net profit after tax in: R394 200").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Dividends R270 000: interim R120 000").scale(1.0).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex("paid, final R150 000 declared").scale(1.0).shift(band_shift(1) + DOWN * 0.3)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("Retained for the year: R124 200").scale(1.05).shift(band_shift(1) + DOWN * 1.2)
        b1_l5 = Tex("$+$ opening R215 800 $=$ R340 000").scale(1.05).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        b1_l6 = Tex("every figure reappears in the statements").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): comprehensive income, top half ---
        self.next_band(2)
        b2_t = Tex("Statement of Comprehensive Income").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Sales R3 600 000 $-$ cost R2 250 000").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("$=$ Gross profit R1 350 000 (60\\% on cost)").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("$+$ other income R90 000 $=$ R1 440 000").scale(1.0).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("$-$ operating expenses R840 000").scale(1.0).shift(band_shift(2) + DOWN * 1.3)
        b2_l5 = Tex("(incl. depreciation R180 000)").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        b2_l6 = Tex("$=$ Operating profit R600 000").scale(1.05).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(2)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): down to net profit after tax ---
        self.next_band(3)
        b3_t = Tex("Three profit levels, by name").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex("$+$ interest income R15 000 $=$ R615 000").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("$-$ interest expense R75 000 $=$ R540 000").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("$-$ income tax R145 800 (27\\%)").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex("$=$ Net profit after tax R394 200").scale(1.05).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_trap = Tex("Dividends among the expenses?").scale(1.05).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_trap))
        self.play(Create(strike(b3_trap)))
        b3_fix = Tex("A distribution of profit — retained").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        b3_fix2 = Tex("income note, never above the profit line").scale(0.95).shift(band_shift(3) + DOWN * 3.7)
        self.play(Write(b3_fix))
        self.play(Write(b3_fix2))
        self.wait(3)

        # --- Band 4 (subtopic_3): financial position — assets ---
        self.next_band(4)
        b4_t = Tex("Financial Position: the assets").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("Fixed assets (carrying) R2 900 000").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("$+$ fixed deposit R100 000 $=$ R3 000 000").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Current: inventories R380 000,").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("receivables R240 000, cash R130 000").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex("$=$ R750 000").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex("TOTAL ASSETS: R3 750 000").scale(1.1).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): equity, liabilities, and the SARS slate ---
        self.next_band(5)
        b5_t = Tex("The claims on those assets").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("Equity: shares R2 500 000 $+$ retained").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("income R340 000 $=$ R2 840 000").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Loan R500 000; current liabilities R410 000:").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("payables R232 200, shareholders for").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        b5_l5 = Tex("dividends R150 000, SARS R27 800").scale(0.95).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("SARS: R145 800 $-$ R118 000 $=$ R27 800").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        b5_l7 = Tex("Balances at R3 750 000").scale(1.05).shift(band_shift(5) + DOWN * 3.4)
        self.play(Write(b5_l6))
        self.wait(2)
        self.play(Write(b5_l7))
        self.play(Create(SurroundingRectangle(b5_l7, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): cash flow — operating activities ---
        self.next_band(6)
        b6_t = Tex("Cash flow: operating activities").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Profit before tax R540 000 $+$ depreciation").scale(0.95).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("R180 000 $+$ interest R75 000 $=$ R795 000").scale(0.95).shift(band_shift(6) + UP * 0.7)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Stock $+$R40 000 out; debtors $+$R25 000 out;").scale(0.95).shift(band_shift(6) + DOWN * 0.1)
        b6_l4 = Tex("payables $+$R32 000 in $\\Rightarrow$ R762 000").scale(0.95).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Paid: interest R75 000, tax R140 000,").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        b6_l6 = Tex("dividends R250 000 (old final $+$ interim)").scale(0.95).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(2)
        b6_trap = Tex("This year's declared final in here?").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_trap))
        self.play(Create(strike(b6_trap)))
        b6_l7 = Tex("No cash moved — net operating R297 000").scale(0.95).shift(band_shift(6) + DOWN * 3.7)
        self.play(Write(b6_l7))
        self.wait(3)

        # --- Band 7 (subtopic_4): investing, financing, the loop closes ---
        self.next_band(7)
        b7_t = Tex("Investing, financing, and the loop").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Investing: assets R450 000 out,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("fixed deposit R20 000 out $=$ R470 000 out").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Financing: shares R200 000 in,").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("loan repaid R60 000 $=$ R140 000 in").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("297 in $-$ 470 out $+$ 140 in:").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        b7_l6 = Tex("cash DOWN R33 000: R163 000 $\\to$ R130 000").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.wait(2)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        b7_l7 = Tex("— exactly the balance sheet's cash figure").scale(0.95).shift(band_shift(7) + DOWN * 3.5)
        self.play(Write(b7_l7))
        self.wait(3)

        # --- Band 8 (subtopic_4): the audit report ---
        self.next_band(8)
        b8_t = Tex("The audit report: three opinions").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Unqualified: fairly presents — clean").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Qualified: fair EXCEPT FOR stated matters").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("Disclaimer / adverse: the alarm bells").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Addressed to the SHAREHOLDERS:").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        b8_l5 = Tex("directors prepare, auditors verify —").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        b8_l6 = Tex("an opinion, never a guarantee").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): one year, three photographs ---
        self.next_band(9)
        b9_t = Tex("One year, three answers").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("How did we DO? The video of the year:").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("ends at R394 200 after tax").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("What do we HAVE? The midnight photo:").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex("both sides come to R3 750 000").scale(1.0).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Where is the CASH? Profit near R400 000,").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        b9_l6 = Tex("yet the tin holds LESS — both true:").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        b9_l7 = Tex("profit is matching; cash is the bank").scale(1.0).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(b9_l5))
        self.wait(2)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_6): where did the cash go? ---
        self.next_band(10)
        b10_t = Tex("Walk the bridge in three strides").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Trading: R540 000 $+$ R180 000 depreciation").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("(no rand left the bank for it);").scale(0.95).shift(band_shift(10) + UP * 0.5)
        b10_l3 = Tex("shelves and notebooks read: R762 000").scale(0.95).shift(band_shift(10) + DOWN * 0.2)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("after interest, tax, dividends PAID:").scale(0.95).shift(band_shift(10) + DOWN * 0.9)
        b10_l5 = Tex("R297 000 into the tin").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2)
        b10_l6 = Tex("Future: R470 000 invested, not lost").scale(0.95).shift(band_shift(10) + DOWN * 2.3)
        b10_l7 = Tex("Funders: R140 000 net in").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l6))
        self.wait(2)
        self.play(Write(b10_l7))
        self.wait(2)
        b10_l8 = Tex("Tin: down R33 000 to R130 000 — it checks").scale(0.95).shift(band_shift(10) + DOWN * 3.7)
        self.play(Write(b10_l8))
        self.play(Create(SurroundingRectangle(b10_l8, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): the auditor's three verdicts ---
        self.next_band(11)
        b11_t = Tex("The roadworthy certificate").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("Unqualified: taxi roadworthy — clean").scale(1.0).shift(band_shift(11) + UP * 1.2)
        b11_l2 = Tex("Qualified: fine EXCEPT the brakes").scale(1.0).shift(band_shift(11) + UP * 0.4)
        b11_l3 = Tex("Disclaimer / adverse: do not board").scale(1.0).shift(band_shift(11) + DOWN * 0.4)
        self.play(Write(b11_l1))
        self.wait(2)
        self.play(Write(b11_l2))
        self.wait(2)
        self.play(Write(b11_l3))
        self.wait(2)
        b11_l4 = Tex("The auditor works for the owners,").scale(1.0).shift(band_shift(11) + DOWN * 1.3)
        b11_l5 = Tex("checking the managers — independence").scale(1.0).shift(band_shift(11) + DOWN * 2.0)
        b11_l6 = Tex("is everything; IRBA can deregister").scale(1.0).shift(band_shift(11) + DOWN * 2.7)
        b11_l7 = Tex("an auditor whose opinion is for sale").scale(1.0).shift(band_shift(11) + DOWN * 3.4)
        self.play(Write(b11_l4))
        self.play(Write(b11_l5))
        self.wait(2)
        self.play(Write(b11_l6))
        self.play(Write(b11_l7))
        self.wait(4)
