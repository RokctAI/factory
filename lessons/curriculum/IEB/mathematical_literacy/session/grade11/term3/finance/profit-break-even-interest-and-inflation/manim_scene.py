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

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Exporter-supported mobjects only (Tex/MathTex/Line/
# Rectangle/SurroundingRectangle); single-string Write reveals throughout.
#
# Covers all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# band time roughly proportional to subtopics.json
# (215/225/225/225/195/195/200 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ProfitBreakEvenInterestInflationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full screen while intro.md plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): cost price and selling price ---
        title = Tex("Profit, Break-even, Interest and Inflation").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l1 = MathTex(r"\text{Batch: } 150 + 250 + 50 + 30 = R480").scale(1.05).shift(UP * 1.1)
        l2 = MathTex(r"\text{Cost price: } 480 \div 80 = R6{,}00").scale(1.05).shift(UP * 0.2)
        self.play(Write(l1)); self.wait(2.5)
        self.play(Write(l2)); self.wait(2.5)
        l3 = MathTex(r"\text{Selling at } R10: \; \text{profit} = 10 - 6{,}00 = R4{,}00").scale(1.05).shift(DOWN * 0.8)
        self.play(Write(l3))
        self.play(Create(SurroundingRectangle(l3, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): percentage profit on the right base ---
        self.next_band(1)
        b1_title = Tex("Percentage profit: on COST, not selling price").scale(1.05).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_wrong = MathTex(r"4{,}00 \div 10 \times 100 = 40\% \quad \text{(wrong base!)}").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2.5)
        b1_l1 = MathTex(r"4{,}00 \div 6{,}00 \times 100 = 66{,}7\%").scale(1.15).shift(band_shift(1) + UP * 0.1)
        self.play(Write(b1_l1))
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2.5)
        b1_l2 = MathTex(r"\text{Season on season: } 680 \div 8\,500 \times 100 = 8\%").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        b1_l3 = Tex(r"Projected R550 vs actual R480: R70 under budget").scale(0.95).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l2)); self.wait(2.5)
        self.play(Write(b1_l3)); self.wait(2.5)

        # --- Band 2 (subtopic_2): break-even worked ---
        self.next_band(2)
        b2_title = Tex(r"Break-even: site fee R290, sell at R10").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Cost: } 290 + 6{,}00 \times n; \quad \text{income: } 10 \times n").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"10 \times n = 290 + 6{,}00 \times n").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\text{Each sale contributes } 10 - 6{,}00 = R4{,}00").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = MathTex(r"290 \div 4{,}00 = 72{,}5 \;\Rightarrow\; 73 \text{ rolls}").scale(1.1).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l1)); self.wait(2.5)
        self.play(Write(b2_l2)); self.wait(2)
        self.play(Write(b2_l3)); self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex(r"At 72: income 720 vs costs 722 — still short").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l5)); self.wait(2.5)

        # --- Band 3 (subtopic_2): the crossing moves ---
        self.next_band(3)
        b3_title = Tex("The graph, and how the crossing moves").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Income climbs from 0 at R10; costs start at R290, climb R6,00").scale(0.85).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("Left of the crossing: loss. Right: profit. Read the GAP.").scale(0.95).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1)); self.wait(2.5)
        self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = MathTex(r"\text{Cheaper site } R200: \; 200 \div 4{,}00 = 50").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = MathTex(r"\text{Price } R10{,}50: \; 290 \div 4{,}50 = 64{,}4 \Rightarrow 65").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l3)); self.wait(2.5)
        self.play(Write(b3_l4)); self.wait(2.5)
        b3_l5 = Tex("Say WHICH way each change moves the crossing").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5)); self.wait(2.5)

        # --- Band 4 (subtopic_3): compound interest year by year ---
        self.next_band(4)
        b4_title = Tex(r"R8\,000 at 6\%: build the table year by year").scale(1.05).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{Year 1: } 8\,000 \times 0{,}06 = 480 \;\to\; 8\,480").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = MathTex(r"\text{Year 2: } 8\,480 \times 0{,}06 = 508{,}80 \;\to\; 8\,988{,}80").scale(1.0).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"\text{Year 3: } 539{,}33 \;\to\; R9\,528{,}13").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l1)); self.wait(2.5)
        self.play(Write(b4_l2)); self.wait(2.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2.5)
        b4_l4 = MathTex(r"\text{Simple: } 3 \times 480 \to R9\,440; \;\; \text{compound wins by } R88{,}13").scale(0.83).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(b4_l4)); self.wait(2.5)
        b4_l5 = Tex("A loan walks the SAME staircase — against you").scale(0.95).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l5)); self.wait(2.5)

        # --- Band 5 (subtopic_3): banking vocabulary ---
        self.next_band(5)
        b5_title = Tex("Know your accounts").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Savings: modest interest, withdrawals allowed").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("Cheque/current: daily transactions, fees, little interest").scale(0.95).shift(band_shift(5) + UP * 0.2)
        b5_l3 = Tex("Fixed deposit: locked away, higher rate").scale(0.95).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = Tex("Debit spends your money; credit spends the bank's").scale(0.95).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        self.play(Write(b5_l3)); self.wait(2)
        self.play(Write(b5_l4)); self.wait(2)
        b5_l5 = Tex("Bank fees are expenses in every budget a question sets").scale(0.9).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5)); self.wait(2.5)

        # --- Band 6 (subtopic_4): inflation forwards and backwards ---
        self.next_band(6)
        b6_title = Tex(r"Inflation at 5\%: the basket next year").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"2\,400 \times 1{,}05 = R2\,520 \quad \text{(R120 short if unbudgeted)}").scale(0.92).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_wrong = MathTex(r"1{,}80 \div 24{,}30 = 7{,}4\% \quad \text{(divided by the NEW price!)}").scale(0.91).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_wrong))
        self.play(Create(strike(b6_wrong)))
        self.wait(2.5)
        b6_l2 = MathTex(r"\text{Milk: } 1{,}80 \div 22{,}50 \times 100 = 8\%").scale(1.05).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex("The base is always the OLD price").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l3)); self.wait(2.5)

        # --- Band 7 (subtopic_4): inflation compounds, and buying power ---
        self.next_band(7)
        b7_title = Tex("Inflation compounds, like the deposit").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Two years: } 1{,}05 \times 1{,}05 = 1{,}1025, \text{ not } 1{,}10").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"2\,400 \times 1{,}1025 = R2\,646").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1)); self.wait(2.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex(r"Deposit at 6\% vs inflation at 5\%: real growth is the sliver").scale(0.9).shift(band_shift(7) + DOWN * 0.8)
        b7_l4 = Tex(r"Cash in a drawer loses 5\% of its power each year").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l3)); self.wait(2.5)
        self.play(Write(b7_l4)); self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): pricing from behind the braai ---
        self.next_band(8)
        b8_title = Tex("The cost floor, then the price call").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2.5)
        b8_l1 = MathTex(r"480 \div 80 = R6{,}00 \text{ each — the floor}").scale(1.05).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1)); self.wait(3)
        b8_l2 = Tex(r"Sell at R10: each sale clears R4,00").scale(1.05).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2)); self.wait(3)
        b8_l3 = MathTex(r"4{,}00 \div 6{,}00 = 66{,}7\% \text{ profit on cost}").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)
        b8_l4 = Tex(r"This season R9\,180 vs last season R8\,500: up 8\%").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4)); self.wait(3.5)

        # --- Band 9 (subtopic_6): the crawl back to zero ---
        self.next_band(9)
        b9_title = Tex(r"R290 down before the first customer").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = Tex(r"Each roll pushes R4,00 against the hole").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = MathTex(r"290 \div 4{,}00 = 72{,}5 \;\Rightarrow\; \text{number } 73 \text{ breaks even}").scale(0.81).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(3)
        b9_l3 = Tex("Before 73 every sale shrinks a loss; after, it IS profit").scale(0.95).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3)); self.wait(3)
        b9_l4 = Tex(r"Cheaper site: 50. Price R10,50: 65. Decisions move the crossing.").scale(0.9).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4)); self.wait(3.5)

        # --- Band 10 (subtopic_7): two staircases ---
        self.next_band(10)
        b10_title = Tex("The bank's staircase and the trolley's").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = MathTex(r"8\,000 \to 8\,480 \to 8\,988{,}80 \to 9\,528{,}13").scale(1.0).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1)); self.wait(3)
        b10_l2 = Tex("Each step taller — interest earning its own interest").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2)); self.wait(3)
        b10_l3 = MathTex(r"\text{Trolley: } 2\,400 \times 1{,}05 = 2\,520; \;\; \times 1{,}1025 = 2\,646").scale(0.9).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(3)
        b10_l4 = Tex(r"Milk: 1,80 over the OLD 22,50 $=$ 8\%").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = Tex("Check which staircase climbs faster — that is the answer").scale(0.9).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l4)); self.wait(3)
        self.play(Write(b10_l5)); self.wait(4)
