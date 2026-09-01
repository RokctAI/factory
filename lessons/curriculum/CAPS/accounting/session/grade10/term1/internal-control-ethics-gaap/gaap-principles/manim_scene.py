# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for "GAAP Principles" (grade10 term1,
# internal-control-ethics-gaap). One band per teaching beat, add-only
# lifecycle, camera moves down between bands. Exporter-safe mobjects only
# (Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup).
#
# Subtopic time shares (subtopics.json, total 1420 s):
# 170/230/210/270/190/180/170 -> bands 0-1 / 2-3 / 4-5 / 6-8 / 9 / 10 / 11.

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
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the land mystery ---
        title = Tex("GAAP Principles").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Land bought in 2019 for R500 000").scale(1.1).shift(UP * 1.1)
        b0_l2 = Tex("Agent today: ``worth R900 000''").scale(1.1).shift(UP * 0.2)
        b0_l3 = Tex("The books still say: R500 000").scale(1.1).shift(DOWN * 0.7)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Lazy bookkeeper? No -- a principle at work").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): why agreed rules exist, the six names ---
        self.next_band(1)
        b1_title = Tex("Why Accounting needs agreed rules").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Without rules: nobody can trust or").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("compare any set of statements").scale(1.05).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("The six for Grade 10:").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex("historical cost, prudence, materiality,").scale(1.05).shift(band_shift(1) + DOWN * 1.4)
        b1_l5 = Tex("business entity, going concern, matching").scale(1.05).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex("Exams ask: which principle, and why?").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): historical cost solves the mystery ---
        self.next_band(2)
        b2_title = Tex("Historical cost").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Assets recorded at original purchase").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("price -- not today's estimated value").scale(1.05).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("Purchase price: a FACT on a document").scale(1.05).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = Tex("Today's value: an OPINION that shifts").scale(1.05).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("The land stays at R500 000: historical cost").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): prudence, and the cost-vs-caution trap ---
        self.next_band(3)
        b3_title = Tex("Prudence (conservatism)").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Never overstate good news, never").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("understate bad news").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("In action: bad debts written off,").scale(1.05).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex("stock at lower of cost and selling price").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_w = Tex("Land kept at R500 000 = prudence?").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_w))
        self.play(Create(strike(b3_w)))
        self.wait(1.5)
        b3_ok = Tex("Cost = original price; prudence = caution").scale(1.0).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_ok))
        self.play(Create(SurroundingRectangle(b3_ok, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): materiality, stapler vs vehicle ---
        self.next_band(4)
        b4_title = Tex("Materiality").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Material = big enough to change").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("a reader's decision").scale(1.05).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"R45 stapler $\Rightarrow$ expense, move on").scale(1.05).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex(r"R450 000 vehicle $\Rightarrow$ fixed asset, tracked").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Same logic, different scale").scale(1.05).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): business entity rule ---
        self.next_band(5)
        b5_title = Tex("The business entity rule").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Business and owner: two separate").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("entities in the books").scale(1.05).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex(r"Owner takes cash $\Rightarrow$ Drawings,").scale(1.05).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = Tex("a reduction of owner's equity").scale(1.05).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_w = Tex("Home electricity = business expense?").scale(1.0).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_w))
        self.play(Create(strike(b5_w)))
        self.wait(1.5)
        b5_ok = Tex("That is Drawings too -- never an expense").scale(1.0).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_ok))
        self.play(Create(SurroundingRectangle(b5_ok, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): going concern ---
        self.next_band(6)
        b6_title = Tex("Going concern").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Books assume the business continues").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("into the foreseeable future").scale(1.05).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("It justifies the others: keep land at").scale(1.05).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex("cost, spread a vehicle over its years").scale(1.05).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Closing next month? Then value all at").scale(1.0).shift(band_shift(6) + DOWN * 2.3)
        b6_l6 = Tex("quick-sale prices instead").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): matching, with the insurance figures ---
        self.next_band(7)
        b7_title = Tex("Matching").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Each period's expenses matched against").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("that same period's incomes").scale(1.05).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Insurance R12 000 paid in March;").scale(1.05).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = Tex("year ends June: only 3 months is").scale(1.05).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex("this year's expense -- rest is prepaid").scale(1.05).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex("June wages paid in July: still June's").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_4): the matching game, five scenarios ---
        self.next_band(8)
        b8_title = Tex("The matching game").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex(r"Land stays at R500 000 $\Rightarrow$ historical cost").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"Doubtful debt written off $\Rightarrow$ prudence").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"R45 stapler expensed $\Rightarrow$ materiality").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex(r"Home power as Drawings $\Rightarrow$ entity rule").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex(r"Trading next year assumed $\Rightarrow$ going concern").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l1))
        self.wait(1.5)
        self.play(Write(b8_l2))
        self.wait(1.5)
        self.play(Write(b8_l3))
        self.wait(1.5)
        self.play(Write(b8_l4))
        self.wait(1.5)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("Ask: what is the accountant refusing to do?").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): six principles, six faces ---
        self.next_band(9)
        b9_title = Tex("Six principles, six familiar faces").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Grandfather: what he PAID -- cost").scale(0.95).shift(band_shift(9) + UP * 1.2 + LEFT * 3.0)
        b9_l2 = Tex("Grandmother: no early").scale(1.0).shift(band_shift(9) + UP * 0.5 + LEFT * 3.0)
        b9_l3 = Tex("chickens -- prudence").scale(1.0).shift(band_shift(9) + DOWN * 0.2 + LEFT * 3.0)
        b9_l4 = Tex("Uncle: size decides the").scale(1.0).shift(band_shift(9) + DOWN * 0.9 + LEFT * 3.0)
        b9_l5 = Tex("fuss -- materiality").scale(1.0).shift(band_shift(9) + DOWN * 1.6 + LEFT * 3.0)
        self.play(Write(b9_l1))
        self.wait(1.5)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(1.5)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(1.5)
        b9_r1 = Tex("Aunt: two purses -- entity").scale(1.0).shift(band_shift(9) + UP * 1.2 + RIGHT * 3.0)
        b9_r2 = Tex("Father: plants trees --").scale(1.0).shift(band_shift(9) + UP * 0.5 + RIGHT * 3.0)
        b9_r3 = Tex("going concern").scale(1.0).shift(band_shift(9) + DOWN * 0.2 + RIGHT * 3.0)
        b9_r4 = Tex("Cousin: the calendar --").scale(1.0).shift(band_shift(9) + DOWN * 0.9 + RIGHT * 3.0)
        b9_r5 = Tex("matching").scale(1.0).shift(band_shift(9) + DOWN * 1.6 + RIGHT * 3.0)
        self.play(Write(b9_r1))
        self.wait(1.5)
        self.play(Write(b9_r2))
        self.play(Write(b9_r3))
        self.wait(1.5)
        self.play(Write(b9_r4))
        self.play(Write(b9_r5))
        self.wait(1.5)
        b9_box = Tex("Which relative just spoke?").scale(1.05).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_box))
        self.play(Create(SurroundingRectangle(b9_box, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_6): the family argues one messy story ---
        self.next_band(10)
        b10_title = Tex("The family argues a scenario").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Van worth more than she paid --").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"stays at cost $\Rightarrow$ historical cost").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("R800 groceries off her own shelves --").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex(r"record it $\Rightarrow$ Drawings, entity rule").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("R1 200 debtor emigrated -- write it").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        b10_l6 = Tex(r"off $\Rightarrow$ prudence").scale(1.0).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): why the rules make books believable ---
        self.next_band(11)
        b11_title = Tex("Why the rules make books believable").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Stubborn invoices: no inflated assets").scale(1.05).shift(band_shift(11) + UP * 1.1)
        b11_l2 = Tex("Caution: no dressed-up profits").scale(1.05).shift(band_shift(11) + UP * 0.2)
        b11_l3 = Tex("Two purses: the shop's own truth").scale(1.05).shift(band_shift(11) + DOWN * 0.7)
        b11_l4 = Tex("The calendar: each year a fair fight").scale(1.05).shift(band_shift(11) + DOWN * 1.6)
        self.play(Write(b11_l1))
        self.wait(2)
        self.play(Write(b11_l2))
        self.wait(2)
        self.play(Write(b11_l3))
        self.wait(2)
        self.play(Write(b11_l4))
        self.wait(2)
        b11_l5 = Tex("Generally accepted = accepted by all,").scale(1.05).shift(band_shift(11) + DOWN * 2.4)
        b11_l6 = Tex("so believed by all").scale(1.05).shift(band_shift(11) + DOWN * 3.1)
        self.play(Write(b11_l5))
        self.play(Write(b11_l6))
        self.play(Create(SurroundingRectangle(b11_l6, color=GREEN)))
        self.wait(4)
