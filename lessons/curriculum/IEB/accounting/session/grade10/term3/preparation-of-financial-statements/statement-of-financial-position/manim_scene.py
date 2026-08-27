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

# Band-layout whiteboard scene for the IEB Grade 10 Accounting session duo
# "Statement of Financial Position". Add-only lifecycle, one band per teaching
# beat, camera moves down between bands. Covers all seven subtopics: Part 1
# Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7) in fresh bands.
# subtopics.json durations 210/220/220/210/180/190/190 of 1420 s. The
# prescribed format skeleton is drawn first, figures posted in script order,
# totals last.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinancialPositionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): AT a moment; the equation dressed formally
        title = Tex("Statement of Financial Position").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("AT 30 June — a moment, not a period").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = MathTex(r"\text{Assets} = \text{Owner's equity} + \text{Liabilities}").scale(1.1).shift(UP * 0.3)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = Tex("Assets: non-current, then current").scale(1.0).shift(DOWN * 0.7)
        b0_l4 = Tex("Other side: equity, non-current, current liabilities").scale(0.95).shift(DOWN * 1.5)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("Current vs non-current: the ONE-YEAR time test").scale(1.0).shift(DOWN * 2.5)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_2): the asset side, family by family
        self.next_band(1)
        b1_title = Tex("The asset side").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = MathTex(r"\text{Fixed assets: } 14\,000 - 2\,800 = 11\,200").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex("(carrying value — detail lives in the note)").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Inventories: 10 700 + 400 = R11 100").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Receivables: 6 300 + 600 + 1 200 = R8 100").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Cash: 24 500 + 450 + 250 = R25 200").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): total assets
        self.next_band(2)
        b2_title = Tex("Total the asset side").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"11\,200 + 11\,100 + 8\,100 + 25\,200").scale(1.1).shift(band_shift(2) + UP * 0.9)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"= \text{R}55\,600").scale(1.2).shift(band_shift(2) + DOWN * 0.1)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("Hold that figure — the other side must meet it").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l3))
        self.wait(3)

        # --- Band 3 (subtopic_3): owner's equity and the pipe between pages
        self.next_band(3)
        b3_title = Tex("Owner's equity — the movement").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex("Capital at start: R22 000").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("+ net profit R10 500 — from the other statement").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("$-$ drawings (R4 500)").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"22\,000 + 10\,500 - 4\,500 = 28\,000").scale(1.1).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex("The most examined link: profit is a LINE here").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): liabilities and the meeting of totals
        self.next_band(4)
        b4_title = Tex("Liabilities, and the totals meet").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex("Non-current: loan at capitalised R16 500").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_wrong = Tex("Loan shown at the original R15 000").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l2 = Tex("Current: payables 10 200 + 300 + 600 = R11 100").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = MathTex(r"28\,000 + 16\,500 + 11\,100 = 55\,600").scale(1.05).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = Tex("Agreement — the equation exhibited").scale(1.0).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_4): where every adjustment landed
        self.next_band(5)
        b5_title = Tex("Every adjustment's address").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Accrued expenses — trade and other payables").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Prepaid expenses, accrued income — receivables").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Income in advance — payables; consumables —").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("inventories; accumulated depreciation — fixed assets").scale(0.9).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("Interest capitalised — the swollen loan").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("Seven adjustments, seven pairs, two pages").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): technique, four habits
        self.next_band(6)
        b6_title = Tex("Technique — four habits").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("1. Heading in full, with AT").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("2. Sub-headings in prescribed order, both sides").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("3. The one-year test decides borderline filings").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("4. Brackets and workings beside assembled lines").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Final act: total both sides, agree in writing").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the midnight photograph, two walls
        self.next_band(7)
        b7_title = Tex("The midnight photograph").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Last page was a movie; this one is a photo").scale(1.0).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("One wall: what the shop HOLDS — equipment,").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex("stock, IOUs in the drawer, the money itself").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Other wall: who FUNDED it — owner, loan, debts").scale(0.95).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("The two walls must weigh exactly the same").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): piles sorted by speed
        self.next_band(8)
        b8_title = Tex("Two piles that must weigh the same").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Sort by one question: how soon is it money?").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Long pile: the equipment. Fast pile: stock,").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("money on its way in, money already here").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = MathTex(r"\text{Fast assets } 44\,400 \text{ vs fast debts } 11\,100").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Payable four times over — analysis by layout").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): the owner's jar, opened and closed
        self.next_band(9)
        b9_title = Tex("The owner's jar, opened and closed").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Opened holding R22 000").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Profit poured in: R10 500 — the pipe from the movie").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Dipped into: drawings R4 500 — never an expense").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = MathTex(r"22\,000 + 10\,500 - 4\,500 = 28\,000").scale(1.1).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Both walls: R55 600 — level, unbroken").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.wait(4)
