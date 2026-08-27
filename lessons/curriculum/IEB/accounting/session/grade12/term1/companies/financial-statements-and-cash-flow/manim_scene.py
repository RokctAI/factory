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
# Part 2 (Simplifier) = subtopics 5-7. Exporter-safe primitives only;
# write-only reveals. Subtopic durations 230/220/240/270/200/220/200 of
# 1580 s guide the apportioning. Worked figures follow Zamani Limited.

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
        title = Tex("Financial Statements and Cash Flow").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Adjustments enforce MATCHING: this year's").scale(0.95).shift(UP * 1.3)
        b0_l2 = Tex("income and expenses, no more, no less").scale(0.95).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Provision for bad debts: adjust the MOVEMENT").scale(0.9).shift(DOWN * 0.3)
        b0_l4 = Tex("R14 000 needed, R17 000 held").scale(0.95).shift(DOWN * 1.0)
        b0_l5 = Tex("$\\Rightarrow$ decrease of R3 000 (income)").scale(0.95).shift(DOWN * 1.7)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(2.5)
        b0_l6 = Tex("Reverse LAST year's accruals at the start,").scale(0.9).shift(DOWN * 2.6)
        b0_l7 = Tex("or the year counts them twice").scale(0.9).shift(DOWN * 3.3)
        self.play(Write(b0_l6))
        self.play(Write(b0_l7))
        self.wait(3)

        # --- Band 1 (subtopic_1): the appropriation traced ---
        self.next_band(1)
        b1_t = Tex("Trading $\\to$ Profit and Loss $\\to$ Appropriation").scale(1.0).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Net profit after tax in: R423 400").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Dividends out: R130 000 interim (paid Oct)").scale(0.95).shift(band_shift(1) + UP * 0.3)
        b1_l3 = Tex("$+$ R150 000 final (declared last day)").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("Retained this year: R143 400").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        b1_l5 = Tex("Opening R256 600 $+$ R143 400").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        b1_l6 = Tex("$=$ closing retained income R400 000").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): comprehensive income, top half ---
        self.next_band(2)
        b2_t = Tex("Statement of comprehensive income").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Sales R4 200 000 $-$ cost of sales R2 800 000").scale(0.9).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("$=$ GROSS PROFIT R1 400 000").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2)
        b2_l3 = Tex("Check: 1 400 000 $\\div$ 2 800 000 $=$ 50\\% on cost").scale(0.9).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("$+$ other operating income R100 000").scale(0.95).shift(band_shift(2) + DOWN * 1.4)
        b2_l5 = Tex("$-$ operating expenses R880 000").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        b2_l6 = Tex("$=$ OPERATING PROFIT R620 000").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(2)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): down to net profit after tax ---
        self.next_band(3)
        b3_t = Tex("Down to the bottom line").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex("$+$ interest income R20 000 $=$ R640 000").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("$-$ interest expense R60 000").scale(0.95).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("$=$ NET PROFIT BEFORE TAX R580 000").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("$-$ income tax 27\\% $=$ R156 600").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        b3_l5 = Tex("$=$ NET PROFIT AFTER TAX R423 400").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(2)
        b3_trap = Tex("Dividends among the expenses?").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_trap))
        self.play(Create(strike(b3_trap)))
        b3_l6 = Tex("distribution of profit — below the line").scale(0.9).shift(band_shift(3) + DOWN * 3.7)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): financial position — assets ---
        self.next_band(4)
        b4_t = Tex("Financial position: the assets").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("Fixed assets (carrying value) R3 050 000").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("$+$ fixed deposit R150 000 $=$ R3 200 000").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Current: inventories R420 000,").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("receivables R280 000, cash R200 000").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex("$=$ R900 000").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex("TOTAL ASSETS R4 100 000").scale(1.05).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): equity, liabilities, and the SARS slate ---
        self.next_band(5)
        b5_t = Tex("The claims on the assets").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("Equity: capital R2 900 000 $+$").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("retained income R400 000 $=$ R3 300 000").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Non-current: Dinaledi Bank loan R400 000").scale(0.9).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("Current: payables R211 400, shareholders").scale(0.9).shift(band_shift(5) + DOWN * 1.1)
        b5_l5 = Tex("for dividends R150 000, SARS R38 600").scale(0.9).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2.5)
        b5_l6 = Tex("3 300 000 $+$ 400 000 $+$ 400 000 $=$ R4 100 000").scale(0.9).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        b5_l7 = Tex("SARS: R156 600 charged $-$ R118 000 paid").scale(0.85).shift(band_shift(5) + DOWN * 3.5)
        self.play(Write(b5_l7))
        self.wait(3)

        # --- Band 6 (subtopic_4): cash flow — operating activities ---
        self.next_band(6)
        b6_t = Tex("Cash flow: operating activities").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("NPBT R580 000 $+$ depreciation R210 000").scale(0.9).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("$+$ interest expense R60 000 $=$ R850 000").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Stock $+$50 000 out; debtors $+$30 000 out;").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("creditors $+$42 000 in $\\Rightarrow$ R812 000").scale(0.9).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Interest paid 60 000; tax paid 143 000;").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        b6_l6 = Tex("dividends paid 250 000 (old final $+$ interim)").scale(0.85).shift(band_shift(6) + DOWN * 2.7)
        b6_l7 = Tex("Net operating: R359 000 in").scale(1.0).shift(band_shift(6) + DOWN * 3.5)
        self.play(Write(b6_l5))
        self.wait(2)
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.play(Create(SurroundingRectangle(b6_l7, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): investing, financing, the loop closes ---
        self.next_band(7)
        b7_t = Tex("Investing, financing, and the loop").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Investing: assets R520 000 out,").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("deposit R30 000 out $=$ R550 000 out").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Check: 2 740 000 $+$ 520 000 $-$ 210 000").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("$=$ 3 050 000 closing carrying value").scale(0.9).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Financing: shares R240 000 in, loan R80 000 out").scale(0.85).shift(band_shift(7) + DOWN * 1.9)
        b7_l6 = Tex("359 $-$ 550 $+$ 160 $=$ R31 000 decrease").scale(0.9).shift(band_shift(7) + DOWN * 2.7)
        b7_l7 = Tex("R231 000 $\\to$ R200 000 $=$ balance sheet cash").scale(0.9).shift(band_shift(7) + DOWN * 3.5)
        self.play(Write(b7_l5))
        self.wait(2)
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.play(Create(SurroundingRectangle(b7_l7, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): the audit report ---
        self.next_band(8)
        b8_t = Tex("The audit report").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("UNQUALIFIED: fairly presents — clean").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("QUALIFIED: fair EXCEPT FOR listed matters").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("DISCLAIMER / ADVERSE: the alarms").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Addressed to the SHAREHOLDERS:").scale(0.95).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex("directors prepare, auditors verify").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        b8_l6 = Tex("the fee buys an honest opinion, not a friendly one").scale(0.85).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_5): one year, three photographs ---
        self.next_band(9)
        b9_t = Tex("One year, three photographs").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("The playback: the whole year at speed,").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("ending on R423 400 after tax").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("The photograph: midnight, last day —").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex("both sides R4 100 000; all owned is claimed").scale(0.9).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("The puzzle: big profit, smaller cashbox —").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        b9_l6 = Tex("profit counts promises; the box counts money").scale(0.9).shift(band_shift(9) + DOWN * 2.7)
        b9_l7 = Tex("the cash flow statement is the bridge").scale(0.95).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(b9_l5))
        self.wait(2)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_6): where did the cash go? ---
        self.next_band(10)
        b10_t = Tex("Where did the cash go?").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Stride 1 — trading: add back depreciation,").scale(0.9).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("read shelves and notebooks: R359 000 in").scale(0.9).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Stride 2 — the future: R550 000 planted").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex("Stride 3 — the funders: R160 000 in").scale(0.9).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("The box: R231 000 $-$ R31 000 $=$ R200 000").scale(0.95).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(2)
        b10_l6 = Tex("Strong trading, heavy planting —").scale(0.9).shift(band_shift(10) + DOWN * 2.9)
        b10_l7 = Tex("read the story, not just the numbers").scale(0.9).shift(band_shift(10) + DOWN * 3.6)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(3)

        # --- Band 11 (subtopic_7): the auditor's three verdicts ---
        self.next_band(11)
        b11_t = Tex("The auditor's three verdicts").scale(1.1).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("House sound $=$ unqualified (clean)").scale(0.95).shift(band_shift(11) + UP * 1.2)
        b11_l2 = Tex("Sound except the roof $=$ qualified").scale(0.95).shift(band_shift(11) + UP * 0.4)
        b11_l3 = Tex("No access / unsafe $=$ disclaimer, adverse").scale(0.95).shift(band_shift(11) + DOWN * 0.4)
        self.play(Write(b11_l1))
        self.wait(2)
        self.play(Write(b11_l2))
        self.wait(2)
        self.play(Write(b11_l3))
        self.wait(2.5)
        b11_l4 = Tex("For the owners; reasonable assurance;").scale(0.95).shift(band_shift(11) + DOWN * 1.3)
        b11_l5 = Tex("fairly present, not to-the-cent correct").scale(0.95).shift(band_shift(11) + DOWN * 2.0)
        self.play(Write(b11_l4))
        self.play(Write(b11_l5))
        self.wait(2.5)
        b11_l6 = Tex("Independence, or the signature is worthless —").scale(0.9).shift(band_shift(11) + DOWN * 2.9)
        b11_l7 = Tex("IRBA can fine, suspend, deregister").scale(0.9).shift(band_shift(11) + DOWN * 3.6)
        self.play(Write(b11_l6))
        self.play(Write(b11_l7))
        self.wait(4)
