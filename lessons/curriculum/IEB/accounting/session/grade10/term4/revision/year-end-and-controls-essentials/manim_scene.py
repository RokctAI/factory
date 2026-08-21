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

# Band-layout whiteboard scene for the IEB Grade 10 Term 4 revision duo
# "Year-End and Controls Essentials". Add-only lifecycle, one band per
# teaching beat, camera moves down between bands. Covers all seven subtopics:
# Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7).
# subtopics.json durations 220/220/220/220/180/190/190 of 1440 s. Lerato's
# Trading carries every figure: the four adjustments, the two statements,
# the gauges, the guards, and the candle and budget arithmetic.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class YearEndAndControlsEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): adjustments — the two depreciations ---
        title = Tex("Year-End and the Guards, Revised").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\text{Vehicle: } 60\,000 \times 15\% = 9\,000").scale(0.95).shift(UP * 1.1)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = MathTex(r"\text{Equipment: } 20\% \times (20\,000 - 4\,000) = 3\,200").scale(0.95).shift(UP * 0.2)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = MathTex(r"\text{Total depreciation: } 12\,200").scale(1.0).shift(DOWN * 0.8)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = Tex("An expense with no cash movement").scale(0.95).shift(DOWN * 1.8)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the three timing repairs ---
        self.next_band(1)
        b1_title = Tex("The timing repairs — matching").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("Accrued expense: telephone 3 300 + 300 —").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("expense 3 600; R300 a current liability").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Prepaid: insurance 2 400 $-$ 400 —").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("expense 2 000; R400 a current asset").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("Accrued income: rent 8 800 + 800 = 9 600;").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        b1_l6 = Tex("R800 a current asset").scale(0.95).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): trading account and profit and loss ---
        self.next_band(2)
        b2_title = Tex("Closing the year, in order").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Gross profit: } 150\,000 - 100\,000 = 50\,000").scale(0.95).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Policy check: } 100\,000 \times 1{,}5 = 150\,000").scale(0.95).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("Expenses: 22 000 + 3 600 + 2 000 + 12 200 = 39 800").scale(0.9).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"\text{Net profit: } 50\,000 + 9\,600 - 39\,800 = 19\,800").scale(0.95).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): statement of financial position balances ---
        self.next_band(3)
        b3_title = Tex("The midnight photograph").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex("Non-current at carrying value: 45 000 +").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("33 000 + 12 800 = 90 800").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Current: 9 500 + 5 200 + 3 300 + 400 + 800 = 19 200").scale(0.9).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("Equity: 88 000 + 19 800 $-$ 7 400 = 100 400;").scale(0.9).shift(band_shift(3) + DOWN * 1.4)
        b3_l5 = Tex("liabilities 9 600").scale(0.9).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2.5)
        b3_l6 = MathTex(r"110\,000 = 110\,000").scale(1.05).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): profitability gauges ---
        self.next_band(4)
        b4_title = Tex("Profitability — the earning gauges").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = MathTex(r"\text{GP on cost: } \tfrac{50\,000}{100\,000} = 50\%").scale(0.95).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("Equals the mark-up policy — no leakage").scale(0.95).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = MathTex(r"\text{GP on sales: } 33{,}3\% \quad \text{NP on sales: } 13{,}2\%").scale(0.95).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex("Of every R100 through the till, R13 stays").scale(0.95).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): liquidity, solvency, return ---
        self.next_band(5)
        b5_title = Tex("Liquidity, solvency, return").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"\text{Current: } \tfrac{19\,200}{9\,600} = 2:1").scale(0.95).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"\text{Acid test: } \tfrac{9\,700}{9\,600} \approx 1{,}01:1").scale(0.95).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Solvency: assets cover debts 11 times over").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"\text{ROE: } \tfrac{19\,800}{94\,200} = 21\%").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2.5)
        b5_l5 = Tex("Figure, comparison, judgement — every time").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): guards and rules ---
        self.next_band(6)
        b6_title = Tex("The guard-rails").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Control: split duties, numbered documents,").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("authorisation, safeguards, independent checks").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Ethics: integrity, objectivity,").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("confidentiality, competence").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("GAAP: cost, prudence, matching, going concern,").scale(0.9).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex("entity, materiality").scale(0.9).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): unit cost and the budget ---
        self.next_band(7)
        b7_title = Tex("The last arithmetic, in one breath").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = MathTex(r"\text{Prime: } 3\,500 + 2\,500 = 6\,000;\; +1\,500 = 7\,500").scale(0.9).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"\text{Unit: } 7\,500 \div 500 = \text{R}15").scale(0.95).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Budget: 11 000 in, 8 500 out, surplus 2 500,").scale(0.9).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("opening 1 500 — closing R4 000").scale(0.9).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_wrong = Tex("Depreciation inside the cash budget").scale(0.95).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): tidying the room before the photo ---
        self.next_band(8)
        b8_title = Tex("Tidying the room before the photo").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Admit the wearing: depreciation 12 200").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Pull in: the owed calls 300; the earned rent 800").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Push out: next year's cover 400").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("The photo shows what the year truly used").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        b8_l5 = Tex("and truly earned").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): report card and health check ---
        self.next_band(9)
        b9_title = Tex("The report card and the health check").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Top floor: the trading game earned 50 000").scale(0.95).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Middle: plus the tenant's 9 600").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Bottom: less 39 800 — the year's mark: 19 800").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Health: bills covered twice; debts covered").scale(0.95).shift(band_shift(9) + DOWN * 1.4)
        b9_l5 = Tex("11 times; R21 earned per R100 left in").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): locks and the candle ---
        self.next_band(10)
        b10_title = Tex("Locks on the doors, and one candle").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_wrong = Tex("One person takes, counts, records and banks").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_wrong))
        self.play(Create(strike(b10_wrong)))
        self.wait(2)
        b10_l1 = Tex("Split the jobs; numbered slips; a second nod;").scale(0.95).shift(band_shift(10) + UP * 0.3)
        b10_l2 = Tex("stock counted by someone who does not sell it").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"\text{One candle: } \tfrac{3\,500 + 2\,500 + 1\,500}{500} = \text{R}15").scale(0.9).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2.5)
        b10_l4 = Tex("Guard the money, cost the unit,").scale(0.95).shift(band_shift(10) + DOWN * 2.4)
        b10_l5 = Tex("write the month before living it").scale(0.95).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(4)
