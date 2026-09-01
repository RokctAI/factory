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

# Band-layout whiteboard scene for the Profit, Loss and Financial Documents
# session duo. One band per teaching beat, camera moves down between bands,
# add-only lifecycle. Exporter-supported mobjects only; every working line is
# a single-string Tex/MathTex revealed with Write. Band time apportioned to
# subtopics.json (210/220/210/280/180/190/190 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ProfitLossFinancialDocumentsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): income side of the month ---
        title = Tex("Profit, Loss and Financial Documents").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_h = Tex("Karabo's month — money IN").scale(1.1).shift(UP * 1.4)
        self.play(Write(b0_h))
        self.wait(1.5)
        b0_l1 = MathTex(r"165 \text{ muffins} \times \text{R}8 = \text{R}1\;320").scale(1.05).shift(UP * 0.5)
        b0_l2 = MathTex(r"120 \text{ juices} \times \text{R}12 = \text{R}1\;440").scale(1.05).shift(DOWN * 0.4)
        b0_l3 = MathTex(r"\text{Total income: } 1\;320 + 1\;440 = \text{R}2\;760").scale(1.05).shift(DOWN * 1.3)
        self.play(Write(b0_l1))
        self.wait(2.5)
        self.play(Write(b0_l2))
        self.wait(2.5)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): expenditure and the profit line ---
        self.next_band(1)
        b1_t = Tex("Money OUT, and the profit line").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = MathTex(r"\text{Stock: } 540 + 840 = \text{R}1\;380").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("Rental R300, electricity R160, taxi R150").scale(1.0).shift(band_shift(1) + UP * 0.2)
        b1_l3 = MathTex(r"\text{Total out: } \text{R}1\;990").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_ans = MathTex(r"\text{Profit: } 2\;760 - 1\;990 = \text{R}770").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_ans))
        self.play(Create(SurroundingRectangle(b1_ans, color=GREEN)))
        b1_l4 = Tex("15 unsold muffins: R45 spent, nothing back").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the till slip's three lines ---
        self.next_band(2)
        b2_t = Tex("The till slip's three lines").scale(1.2).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_t))
        self.wait(1.5)
        slip = Rectangle(width=7.5, height=3.4).shift(band_shift(2) + UP * 0.3)
        self.play(Create(slip))
        self.wait(1)
        s1 = Tex("Subtotal \\quad R640,00").scale(1.0).shift(band_shift(2) + UP * 1.2)
        s2 = Tex("VAT at 15\\% \\quad R96,00").scale(1.0).shift(band_shift(2) + UP * 0.3)
        s3 = Tex("Total due \\quad R736,00").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(s1))
        self.wait(2)
        self.play(Write(s2))
        self.wait(2)
        self.play(Write(s3))
        self.wait(2)
        b2_l1 = MathTex(r"0{,}15 \times 640 = 96 \qquad 640 + 96 = 736").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l1))
        self.play(Create(SurroundingRectangle(b2_l1, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the invoice ---
        self.next_band(3)
        b3_t = Tex("Reading an invoice").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Quantity } 120 \times \text{unit price R}7 = \text{R}840").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex("Always check the multiplication").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Invoice: a promise to pay (30 days)").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex("Till slip: money already paid").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Balance: the amount currently owed").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): fixed, variable, occasional ---
        self.next_band(4)
        b4_t = Tex("Three kinds of expense").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Fixed: R300 rental — same every month").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("Variable: stock, electricity — follows trade").scale(1.0).shift(band_shift(4) + UP * 0.2)
        b4_l3 = Tex("Occasional: R280 gazebo repair — rare, random").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_l1))
        self.wait(2.5)
        self.play(Write(b4_l2))
        self.wait(2.5)
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_rule = Tex("Fixed costs set the floor — owed before any sale").scale(1.0).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_rule))
        self.play(Create(SurroundingRectangle(b4_rule, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): the statement, good month ---
        self.next_band(5)
        b5_t = Tex("Income-and-expenditure statement").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("Income: muffins R1 320 + juice R1 440 = R2 760").scale(0.95).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Expenditure: 1 380 + 300 + 160 + 150 = R1 990").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.wait(2.5)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"2\;760 - 1\;990 = \text{R}770").scale(1.1).shift(band_shift(5) + DOWN * 0.6)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_ans = Tex("Positive: a SURPLUS (a business says profit)").scale(1.0).shift(band_shift(5) + DOWN * 1.6)
        self.play(Write(b5_ans))
        self.play(Create(SurroundingRectangle(b5_ans, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the rainy month deficit ---
        self.next_band(6)
        b6_t = Tex("The rainy month").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Two trading Saturdays: income R1 700").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("Expenditure still R1 880 — the rental held firm").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = MathTex(r"1\;700 - 1\;880 = -\text{R}180").scale(1.1).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_ans = Tex("Negative: a DEFICIT — a loss of R180").scale(1.05).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_ans))
        self.play(Create(SurroundingRectangle(b6_ans, color=GREEN)))
        b6_l4 = Tex("Income fell; fixed costs stood still").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): the five-step method ---
        self.next_band(7)
        b7_t = Tex("Method for any statement question").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("1. Sort every amount: in or out").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("2. Total each side, showing the addition").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex("3. Income minus expenditure, in that order").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("4. Name the result: surplus/profit or deficit/loss").scale(1.0).shift(band_shift(7) + DOWN * 1.6)
        b7_l5 = Tex("5. Explain WHY with the expense categories").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the two shoeboxes ---
        self.next_band(8)
        b8_t = Tex("Two shoeboxes under the table").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("IN box: R1 320 + R1 440 = R2 760").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("OUT box: 540 + 840 + 300 + 160 + 150 = R1 990").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{Left over: } 2\;760 - 1\;990 = \text{R}770").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex("Selling earns; baking alone only spends").scale(1.0).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_6): the three piles ---
        self.next_band(9)
        b9_t = Tex("Sort the costs like washing").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Never budges: R300 rental — fixed").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Follows the crowd: stock, taxi — variable").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("Ambush: R280 gazebo repair — occasional").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_ans = Tex("Slow months lose to the pile that never shrinks").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_ans))
        self.play(Create(SurroundingRectangle(b9_ans, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the page that settles it ---
        self.next_band(10)
        b10_t = Tex("One page settles the argument").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Good month: in R2 760, out R1 990 — surplus R770").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("Rainy month: in R1 700, out R1 880 — deficit R180").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Every amount on the correct side").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        b10_l4 = Tex("Both totals shown before subtracting").scale(1.0).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_ans = Tex("Name the bottom line in words").scale(1.05).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_ans))
        self.play(Create(SurroundingRectangle(b10_ans, color=GREEN)))
        self.wait(4)
