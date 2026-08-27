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

# Band-layout whiteboard scene for the IEB grade 12 accounting session
# "Financial Reporting Practice Run" — a full financial-reporting practice
# set. This session's script runs seven task subtopics (no simplifier part),
# so each task gets its own band(s). Exporter-safe mobjects only;
# write-only reveals — no Transform/FadeOut/sub-part indexing on MathTex.
#
# Subtopic time shares (subtopics.json, total 1555 s):
# 215/230/225/220/225/230/210 — near-equal; bands are spread evenly.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinancialReportingPracticeRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): concepts + the asset disposal ---
        title = Tex("Practice Set: 150 marks").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Concept marks: going concern, prudence,").scale(1.0).shift(UP * 1.3)
        b0_l2 = Tex("materiality, IFRS — four marks, bank them fast").scale(1.0).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Disposal: vehicle cost R240\,000, acc.\ depr.\ R118\,000").scale(0.9).shift(DOWN * 0.3)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = MathTex(r"15\% \times 240\,000 \times \tfrac{8}{12} = R24\,000").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex(r"Acc.\ depr.: $118\,000 + 24\,000 = $ R142\,000").scale(0.95).shift(DOWN * 2.1)
        b0_l6 = Tex(r"Carrying value: $240\,000 - 142\,000 = $ R98\,000").scale(0.95).shift(DOWN * 2.9)
        self.play(Write(b0_l5))
        self.wait(2)
        self.play(Write(b0_l6))
        self.play(Create(SurroundingRectangle(b0_l6, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_2): income statement adjustments ---
        self.next_band(1)
        b1_title = Tex("Income statement: the adjustments").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Rent R91\,000 $=$ 14 months $\Rightarrow$ R13\,000 in advance").scale(0.9).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_wrong = Tex(r"Adding the prepaid insurance to the expense").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l2 = Tex(r"Insurance: prepaid R7\,200 OUT — expense R14\,400").scale(0.9).shift(band_shift(1) + DOWN * 0.4)
        b1_l3 = Tex(r"Audit fee R42\,000 accrued; depreciation R130\,000").scale(0.9).shift(band_shift(1) + DOWN * 1.2)
        b1_l4 = Tex(r"Loan interest: $9\% \times 800\,000 = 72\,000$; accrue R6\,000").scale(0.85).shift(band_shift(1) + DOWN * 2.0)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex(r"NPBT 840\,000; tax $27\% = 226\,800$; NPAT R613\,200").scale(0.9).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_3): share capital note ---
        self.next_band(2)
        b2_title = Tex("Ordinary share capital note").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Opening: 600\,000 shares, R2\,400\,000 (avg R4,00)").scale(0.9).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex(r"Issue: 150\,000 @ R5,50 $=$ R825\,000").scale(0.95).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex(r"Subtotal: 750\,000 shares, R3\,225\,000 — avg R4,30").scale(0.9).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex(r"Buy-back: 60\,000 $\times$ R4,30 $=$ R258\,000 out").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        b2_l5 = Tex(r"Closing: 690\,000 shares, R2\,967\,000").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l4))
        self.wait(2.5)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): retained income note ---
        self.next_band(3)
        b3_title = Tex("Retained income: five lines").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Opening R380\,000 $+$ NPAT R613\,200").scale(0.95).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex(r"$-$ Buy-back premium: 60\,000 $\times$ 60c $=$ R36\,000").scale(0.9).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("(the premium lives HERE, not in share capital)").scale(0.85).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"$-$ Dividends: interim 25c $\times$ 750\,000 $=$ 187\,500;").scale(0.85).shift(band_shift(3) + DOWN * 1.1)
        b3_l5 = Tex(r"final 40c $\times$ 690\,000 $=$ 276\,000 — counts differ!").scale(0.85).shift(band_shift(3) + DOWN * 1.8)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(2.5)
        b3_l6 = Tex(r"Closing: R493\,700; equity R3\,460\,700").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_4): the balance sheet ---
        self.next_band(4)
        b4_title = Tex("Balance sheet: filing under pressure").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Equity 3\,460\,700; loan 800\,000").scale(0.95).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex(r"Current: creditors 212\,300; accrued 48\,000;").scale(0.9).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex(r"in advance 13\,000; SARS 16\,800; dividends 276\,000").scale(0.9).shift(band_shift(4) + DOWN * 0.3)
        b4_l4 = Tex(r"Current liabilities total R566\,100").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.wait(2.5)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex(r"Both totals: R4\,826\,800 — balance").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2)
        b4_l6 = Tex("If it does not balance: rule off, move on —").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        b4_l7 = Tex("follow-on marks protect you; the hunt costs more").scale(0.9).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_5): cash flow workings ---
        self.next_band(5)
        b5_title = Tex("Cash flow: three workings and a map").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Tax paid: } 226\,800 + 11\,200 - 16\,800 = 221\,200").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex(r"Dividends paid: interim 187\,500 $+$ last final 230\,000").scale(0.85).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"$=$ R417\,500; this year's final stays a liability").scale(0.9).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"3\,560\,000 + P - 130\,000 - 98\,000 = 3\,905\,000").scale(0.9).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex(r"Purchases $P = $ R573\,000").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.wait(2.5)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_l6 = Tex(r"Buy-back in cash: FULL R294\,000 — cash left in full").scale(0.85).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_6): analysis and interpretation ---
        self.next_band(6)
        b6_title = Tex("Analysis: Baobab vs Karee, loans at 12\\%").scale(1.05).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex(r"Baobab: ROTCE 16,2\% $>$ 12\% — positive gearing").scale(0.9).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"so ROE 18,1\% beats ROTCE; 0,6:1 debt justified").scale(0.9).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex(r"Karee: 10,4\% $<$ 12\% — borrowing destroys value;").scale(0.9).shift(band_shift(6) + DOWN * 0.3)
        b6_l4 = Tex("its 0,2:1 gearing is wise, not weak").scale(0.9).shift(band_shift(6) + DOWN * 1.0)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex(r"Liquidity: 1,3 tight but workable; 4,1 is lazy money").scale(0.85).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l5))
        self.wait(2)
        b6_l6 = Tex(r"Market: 920c vs NAV 700c — confidence;").scale(0.9).shift(band_shift(6) + DOWN * 2.5)
        b6_l7 = Tex(r"480c below NAV 530c — doubt, or a bargain").scale(0.9).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # --- Band 7 (subtopic_7): audit report and governance ---
        self.next_band(7)
        b7_title = Tex("Audit report and governance").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Unqualified — fairly presents, all material respects").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("Qualified — fairly presents EXCEPT FOR ...").scale(0.9).shift(band_shift(7) + UP * 0.5)
        b7_l3 = Tex("Disclaimer/adverse — cannot or will not vouch").scale(0.9).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Addressed to the SHAREHOLDERS, not the directors").scale(0.9).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("King Code: responsibility, accountability,").scale(0.9).shift(band_shift(7) + DOWN * 1.8)
        b7_l6 = Tex("fairness, transparency — map any scenario").scale(0.9).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2)
        b7_l7 = Tex("Attempt every part; show every working").scale(0.95).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l7))
        self.wait(4)
