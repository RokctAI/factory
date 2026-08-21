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

# Band-layout whiteboard scene for the IEB Grade 11 Term 1 duo
# "Disposal of Fixed Assets". One band per teaching beat; camera moves down,
# nothing is removed. Exporter-safe primitives only; the Asset Disposal
# T-account is drawn from Lines + Tex rows, entries posted in script order,
# balancing figure last. Subtopic shares: 220/250/230/220/190/200/200 of 1510 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DisposalOfFixedAssetsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): why the disposal account exists ---
        title = Tex("Disposal of Fixed Assets").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("An asset leaves with three pieces:").scale(1.1).shift(UP * 1.2)
        b0_l2 = Tex("cost, accumulated depreciation, proceeds").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_wrong = Tex("Credit selling price straight to the asset?").scale(1.0).shift(DOWN * 0.5)
        self.play(Write(b0_wrong))
        self.play(Create(strike(b0_wrong)))
        self.wait(2)
        b0_l3 = Tex("Asset Disposal: cost Dr; acc dep + proceeds Cr").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Balancing figure = profit or loss on disposal").scale(1.0).shift(DOWN * 2.2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = Tex("It is the day the estimate meets reality").scale(1.0).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_2): the four steps ---
        self.next_band(1)
        b1_title = Tex("The four steps that never vary").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("1. Bring depreciation up to date").scale(1.1).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l1b = Tex("(part-year first — most marks!)").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1b))
        self.wait(2)
        b1_l2 = Tex("2. Transfer COST: Dr Disposal, Cr Asset").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("3. Transfer ACC DEP: Dr Acc Dep, Cr Disposal").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("4. Record PROCEEDS: Bank / Debtor /").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        b1_l5 = Tex("new asset / Drawings, Cr Disposal").scale(1.05).shift(band_shift(1) + DOWN * 2.8)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the depreciation arithmetic ---
        self.next_band(2)
        b2_title = Tex(r"Vehicle R240 000, 20\% diminishing balance").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex(r"Year 1: 20\% $\times$ 240 000 = R48 000").scale(1.05).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("carrying value R192 000").scale(1.0).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Year 2: 20\% $\times$ 192 000 = R38 400").scale(1.05).shift(band_shift(2) + DOWN * 0.3)
        b2_l4 = Tex("carrying value R153 600").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = MathTex(r"\text{Sold 30 Nov: } 30\,720 \times \tfrac{9}{12} = R23\,040").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l5))
        self.wait(2.5)
        b2_l6 = Tex("Acc dep 109 440; carrying value R130 560").scale(1.05).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the Asset Disposal T-account ---
        self.next_band(3)
        b3_title = Tex("Asset Disposal").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1)
        t_top = Line(band_shift(3) + UP * 2.0 + LEFT * 3.4,
                     band_shift(3) + UP * 2.0 + RIGHT * 3.4, stroke_width=4)
        t_mid = Line(band_shift(3) + UP * 2.0,
                     band_shift(3) + DOWN * 1.6, stroke_width=4)
        self.play(Create(t_top))
        self.play(Create(t_mid))
        self.wait(1.5)
        b3_dr = Tex("Vehicles 240 000").scale(0.95).shift(band_shift(3) + UP * 1.4 + LEFT * 1.8)
        self.play(Write(b3_dr))
        self.wait(2)
        b3_cr1 = Tex("Acc dep 109 440").scale(0.95).shift(band_shift(3) + UP * 1.4 + RIGHT * 1.8)
        self.play(Write(b3_cr1))
        self.wait(2)
        b3_cr2 = Tex("Bank 122 000").scale(0.95).shift(band_shift(3) + UP * 0.7 + RIGHT * 1.8)
        self.play(Write(b3_cr2))
        self.wait(2)
        b3_bal = Tex("Credits 231 440 vs debits 240 000").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_bal))
        self.wait(2)
        b3_loss = Tex("Loss on disposal R8 560").scale(1.1).shift(band_shift(3) + DOWN * 1.5)
        self.play(Write(b3_loss))
        self.play(Create(SurroundingRectangle(b3_loss, color=GREEN)))
        self.wait(2)
        b3_chk = Tex(r"Check: 122 000 $-$ 130 560 = $-$8 560 — agrees").scale(0.95).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_chk))
        self.wait(3)

        # --- Band 4 (subtopic_3): timing decides step one ---
        self.next_band(4)
        b4_title = Tex("Timing decides step one").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("First day of year: no extra depreciation").scale(1.05).shift(band_shift(4) + UP * 1.0)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_l2 = Tex("During the year: part-year, months over 12").scale(1.05).shift(band_shift(4) + UP * 0.1)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Last day: a full year's charge first").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex("Count months from year start to sale date").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the four kinds of disposal ---
        self.next_band(5)
        b5_title = Tex("Four kinds — only step four changes").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Cash: Dr Bank").scale(1.05).shift(band_shift(5) + UP * 1.2)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Credit: Dr SUNDRY debtor, not trade debtor").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Trade-in: Dr new asset with allowance").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_wrong = Tex("New asset at cash paid only?").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l4 = Tex("Drawings: Dr Drawings at a FAIR value").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Scrapped: no proceeds, carrying value = loss").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): register, controls, ethics ---
        self.next_band(6)
        b6_title = Tex("The register and the controls").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Register page: cost, rate, yearly dep,").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("carrying value — closed off at disposal").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Register totals must agree with the ledger").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("Authorisation, pricing by valuation,").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("documents, segregation, physical counts").scale(1.0).shift(band_shift(6) + DOWN * 1.9)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex("Each control answers a named fraud").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): what the books still think it's worth ---
        self.next_band(7)
        b7_title = Tex("What the books still think it's worth").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Uncle's bakkie: paid R240 000").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("Books today: carrying value R130 560").scale(1.05).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("He sells it for R122 000").scale(1.05).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex(r"Gap: 130 560 $-$ 122 000 = R8 560 loss").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex("A correction of the guess — not a").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        b7_l6 = Tex("trading result. One desk, one deal").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(3.5)

        # --- Band 8 (subtopic_6): four moves, always the same order ---
        self.next_band(8)
        b8_title = Tex("Four moves, always the same order").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = MathTex(r"\text{1. Catch up wear: } 30\,720 \times \tfrac{9}{12} = R23\,040").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(3)
        b8_l2 = Tex("2. Price he paid on the desk: R240 000").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("3. All the wear: 48 000 + 38 400 + 23 040").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        b8_l3b = Tex("= R109 440").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l3))
        self.play(Write(b8_l3b))
        self.wait(2.5)
        b8_l4 = Tex("4. What he got: R122 000").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex(r"231 440 vs 240 000 $\Rightarrow$ loss R8 560").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3.5)

        # --- Band 9 (subtopic_7): four ways out ---
        self.next_band(9)
        b9_title = Tex("Cash, credit, trade-in, or home").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Cash to bank; credit = once-off debtor").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Trade-in: allowance 122 000, pays 208 000").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_wrong = Tex("New bakkie in the books at R208 000?").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2)
        b9_l3 = Tex("New bakkie recorded at R330 000").scale(1.05).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Home = drawings at the honest value").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Approval, valuation, receipt, split duties").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.wait(4)
