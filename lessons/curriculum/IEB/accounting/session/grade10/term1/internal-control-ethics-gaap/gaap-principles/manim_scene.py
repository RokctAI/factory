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

# Band-layout whiteboard scene for the GAAP-principles session duo.
# Exporter-safe primitives only (Tex/MathTex/Line/Arrow/Rectangle/VGroup);
# write-only reveals. Band time follows subtopics.json
# (170/230/210/270/190/180/170 of 1420 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GaapPrinciplesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the land mystery ---
        title = Tex("GAAP Principles").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Land bought 2020: R650 000").scale(1.0).shift(UP * 1.1)
        l02 = Tex("Agent today: worth R1 100 000").scale(1.0).shift(UP * 0.3)
        self.play(Write(l01)); self.wait(2)
        self.play(Write(l02)); self.wait(2)
        l03 = Tex("The books still say: R650 000").scale(1.05).shift(DOWN * 0.7)
        self.play(Write(l03))
        self.play(Create(SurroundingRectangle(l03, color=GREEN)))
        self.wait(2)
        l04 = Tex("Lazy? No — obeying a principle").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(l04))
        self.wait(3)

        # --- Band 1 (subtopic_1): why agreed rules exist, the six names ---
        self.next_band(1)
        b1_t = Tex("Why agreed rules exist").scale(1.2).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_t)); self.wait(2)
        b1_l1 = Tex("Without them: hopeful values, early profits,").scale(0.9).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("mixed purses — nothing comparable").scale(0.9).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1_l1)); self.play(Write(b1_l2)); self.wait(2.5)
        b1_l3 = Tex("The six: historical cost, prudence,").scale(0.9).shift(band_shift(1) + DOWN * 0.3)
        b1_l4 = Tex("materiality, business entity,").scale(0.9).shift(band_shift(1) + DOWN * 1.1)
        b1_l5 = Tex("going concern, matching").scale(0.9).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l3)); self.play(Write(b1_l4)); self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): historical cost solves the mystery ---
        self.next_band(2)
        b2_t = Tex("Historical cost").scale(1.2).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("Assets at the original purchase price —").scale(0.95).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("verifiable fact, not shifting opinion").scale(0.95).shift(band_shift(2) + UP * 0.6)
        self.play(Write(b2_l1)); self.play(Write(b2_l2)); self.wait(2.5)
        b2_l3 = Tex("The invoice is fact; the estimate is opinion").scale(0.9).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l3)); self.wait(2)
        b2_l4 = Tex("Tell-tale: `now worth more' but").scale(0.9).shift(band_shift(2) + DOWN * 1.3)
        b2_l5 = Tex("`still shown at' the original price").scale(0.9).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l4)); self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): prudence, and the cost-vs-caution trap ---
        self.next_band(3)
        b3_t = Tex("Prudence").scale(1.2).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("Never overstate good news;").scale(0.95).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("never understate bad news").scale(0.95).shift(band_shift(3) + UP * 0.6)
        self.play(Write(b3_l1)); self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = Tex("Bad debts written off; stock at the").scale(0.9).shift(band_shift(3) + DOWN * 0.3)
        b3_l4 = Tex("lower value — caution under uncertainty").scale(0.9).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3)); self.play(Write(b3_l4)); self.wait(2.5)
        b3_wrong = Tex("Land at R650 000 is prudence").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        b3_l5 = Tex("Cost = original price; prudence = caution").scale(0.9).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): materiality, calculator vs vehicle ---
        self.next_band(4)
        b4_t = Tex("Materiality").scale(1.2).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("Material = would change a reader's decision").scale(0.9).shift(band_shift(4) + UP * 1.4)
        self.play(Write(b4_l1)); self.wait(2)
        b4_l2 = Tex("R60 calculator: expense it, move on").scale(0.9).shift(band_shift(4) + UP * 0.5)
        b4_l3 = Tex("R380 000 vehicle: fixed asset, tracked").scale(0.9).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l2)); self.wait(2)
        self.play(Write(b4_l3)); self.wait(2)
        b4_l4 = Tex("Same logic, different scale").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): business entity rule ---
        self.next_band(5)
        b5_t = Tex("The business entity rule").scale(1.15).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("Business and owner: separate in the books").scale(0.9).shift(band_shift(5) + UP * 1.4)
        self.play(Write(b5_l1)); self.wait(2)
        b5_l2 = Tex("Owner takes cash or pays home bills").scale(0.9).shift(band_shift(5) + UP * 0.5)
        b5_l3 = Tex("from the business: DRAWINGS, never expense").scale(0.9).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l2)); self.play(Write(b5_l3)); self.wait(2.5)
        b5_l4 = Tex("Tell-tale: `the owner took',").scale(0.9).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex("`for personal use'").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4)); self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): going concern ---
        self.next_band(6)
        b6_t = Tex("Going concern").scale(1.2).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("Books assume the business continues").scale(0.95).shift(band_shift(6) + UP * 1.4)
        self.play(Write(b6_l1)); self.wait(2)
        b6_l2 = Tex("Justifies: assets kept for use,").scale(0.9).shift(band_shift(6) + UP * 0.5)
        b6_l3 = Tex("costs spread over future years").scale(0.9).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l2)); self.play(Write(b6_l3)); self.wait(2.5)
        b6_l4 = Tex("Closing next month? Everything at").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("quick-sale value instead").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4)); self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): matching, with the insurance figures ---
        self.next_band(7)
        b7_t = Tex("Matching").scale(1.2).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Expenses matched to the period they serve").scale(0.9).shift(band_shift(7) + UP * 1.4)
        self.play(Write(b7_l1)); self.wait(2)
        b7_l2 = Tex("Insurance R24 000 paid 1 April;").scale(0.9).shift(band_shift(7) + UP * 0.5)
        b7_l3 = Tex("year ends 30 June:").scale(0.9).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(b7_l2)); self.play(Write(b7_l3)); self.wait(2)
        b7_l4 = MathTex(r"24\,000 \times \tfrac{3}{12} = 6\,000").scale(1.05).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("R18 000 prepaid — next year's story").scale(0.9).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_4): the matching game, five scenarios ---
        self.next_band(8)
        b8_t = Tex("The matching game").scale(1.2).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t)); self.wait(2)
        rows = [
            "Land still at R650 000: historical cost",
            "Doubtful debt written off: prudence",
            "R60 calculator expensed: materiality",
            "Home power as drawings: entity rule",
            "`Still trading next year': going concern",
        ]
        ys = [1.5, 0.7, -0.1, -0.9, -1.7]
        for s, y in zip(rows, ys):
            m = Tex(s).scale(0.8).move_to([0, y, 0]).shift(band_shift(8))
            self.play(Write(m))
            self.wait(1.5)
        b8_l1 = Tex("Ask: refusing what? Insisting on what?").scale(0.9).shift(band_shift(8) + DOWN * 2.6)
        self.play(Write(b8_l1))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): six principles, six faces ---
        self.next_band(9)
        b9_t = Tex("Six principles, six familiar faces").scale(1.1).shift(band_shift(9) + UP * 2.5)
        self.play(Write(b9_t)); self.wait(2)
        faces = [
            "Grandfather: what he PAID — cost",
            "Grandmother: no unhatched chickens — prudence",
            "Uncle: size decides the fuss — materiality",
            "Aunt: two purses, never mixed — entity",
            "Father: plants for future years — going concern",
            "Cousin: every cost pinned to its month — matching",
        ]
        ys9 = [1.5, 0.7, -0.1, -0.9, -1.7, -2.5]
        for s, y in zip(faces, ys9):
            m = Tex(s).scale(0.75).move_to([0, y, 0]).shift(band_shift(9))
            self.play(Write(m))
            self.wait(1.4)
        self.wait(2)

        # --- Band 10 (subtopic_6): the family argues one messy story ---
        self.next_band(10)
        b10_t = Tex("The family argues a scenario").scale(1.15).shift(band_shift(10) + UP * 2.5)
        self.play(Write(b10_t)); self.wait(2)
        b10_l1 = Tex("Van `worth more' for the loan:").scale(0.9).shift(band_shift(10) + UP * 1.4)
        b10_l2 = Tex("grandfather — the invoice is fact").scale(0.9).shift(band_shift(10) + UP * 0.6)
        self.play(Write(b10_l1)); self.play(Write(b10_l2)); self.wait(2.5)
        b10_l3 = Tex("R950 groceries, unwritten:").scale(0.9).shift(band_shift(10) + DOWN * 0.3)
        b10_l4 = Tex("the aunt — drawings, recorded, always").scale(0.9).shift(band_shift(10) + DOWN * 1.1)
        self.play(Write(b10_l3)); self.play(Write(b10_l4)); self.wait(2.5)
        b10_l5 = Tex("Emigrated R1 500 debt kept `in case':").scale(0.9).shift(band_shift(10) + DOWN * 2.0)
        b10_l6 = Tex("grandmother — write it off now").scale(0.9).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5)); self.play(Write(b10_l6))
        self.wait(3)

        # --- Band 11 (subtopic_7): why the rules make books believable ---
        self.next_band(11)
        b11_t = Tex("The treasure they all guard").scale(1.15).shift(band_shift(11) + UP * 2.5)
        self.play(Write(b11_t)); self.wait(2)
        b11_l1 = Tex("BELIEVABILITY").scale(1.3).shift(band_shift(11) + UP * 1.3)
        self.play(Write(b11_l1))
        self.play(Create(SurroundingRectangle(b11_l1, color=GREEN)))
        self.wait(2)
        b11_l2 = Tex("No inflated assets, no dressed-up profits,").scale(0.9).shift(band_shift(11) + UP * 0.2)
        b11_l3 = Tex("no mixed purses, fair years").scale(0.9).shift(band_shift(11) + DOWN * 0.6)
        self.play(Write(b11_l2)); self.play(Write(b11_l3)); self.wait(2.5)
        b11_l4 = Tex("Generally accepted: accepted by everyone,").scale(0.9).shift(band_shift(11) + DOWN * 1.5)
        b11_l5 = Tex("so believed by everyone").scale(0.95).shift(band_shift(11) + DOWN * 2.3)
        self.play(Write(b11_l4)); self.play(Write(b11_l5))
        self.wait(4)
