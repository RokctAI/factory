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

# Band-layout whiteboard scene for the Cash Receipts Journal session duo.
# Exporter-safe primitives only; write-only reveals, nothing morphed or removed.
# Band time follows subtopics.json (180/200/180/200/170/180/170 of 1280 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CashReceiptsJournalSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the job of the CRJ ---
        title = Tex("The Cash Receipts Journal").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Records ALL money received, in date order").scale(1.05).shift(UP * 1.0)
        l02 = Tex("Payments never enter — one direction per book").scale(1.0)
        self.play(Write(l01)); self.wait(2)
        self.play(Write(l02)); self.wait(2)
        l03 = Tex("No entry without evidence:").scale(1.05).shift(DOWN * 1.0)
        l04 = Tex("register roll, duplicate receipt, deposit slip").scale(1.0).shift(DOWN * 1.9)
        self.play(Write(l03)); self.wait(1.5)
        self.play(Write(l04))
        self.wait(3)

        # --- Band 1 (subtopic_1): columns + the analysis column ---
        self.next_band(1)
        b1_t = Tex("The CRJ's columns").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_t)); self.wait(1.5)
        top_y = 1.5
        rail_top = Line(LEFT * 6.4 + UP * top_y, RIGHT * 6.4 + UP * top_y,
                        stroke_width=3).shift(band_shift(1))
        rail_bot = Line(LEFT * 6.4 + UP * (top_y - 1.0), RIGHT * 6.4 + UP * (top_y - 1.0),
                        stroke_width=3).shift(band_shift(1))
        self.play(Create(rail_top), Create(rail_bot))
        heads = VGroup(
            Tex("Doc").scale(0.85).move_to([-5.7, top_y - 0.5, 0]),
            Tex("Day").scale(0.85).move_to([-4.6, top_y - 0.5, 0]),
            Tex("Details").scale(0.85).move_to([-3.3, top_y - 0.5, 0]),
            Tex("Analysis").scale(0.85).move_to([-1.6, top_y - 0.5, 0]),
            Tex("Bank").scale(0.85).move_to([0.2, top_y - 0.5, 0]),
            Tex("Sales").scale(0.85).move_to([1.6, top_y - 0.5, 0]),
            Tex("Cost of Sales").scale(0.85).move_to([3.4, top_y - 0.5, 0]),
            Tex("Sundry").scale(0.85).move_to([5.5, top_y - 0.5, 0]),
        ).shift(band_shift(1))
        self.play(Write(heads)); self.wait(2.5)
        b1_l1 = Tex("Analysis: each amount AS IT ARRIVES").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        b1_l2 = Tex("Bank: the day's total, when deposited").scale(1.05).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.wait(2)
        b1_l3 = Tex("Busy Saturday: five analysis amounts,").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        b1_l4 = Tex("one Bank figure").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(b1_l3)); self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the cash sale, two truths ---
        self.next_band(2)
        b2_t = Tex("3rd: register roll shows sales of R1 500").scale(1.1).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("Doc CRR 1; Details: Sales").scale(1.05).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("Analysis R1 500; Bank R1 500; Sales R1 500").scale(1.0).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1)); self.wait(1.5)
        self.play(Write(b2_l2)); self.wait(2)
        b2_l3 = Tex("Second truth — mark-up 25\\% on cost:").scale(1.05).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = MathTex(r"1\,500 \div 1{,}25 = \text{R1 200 (Cost of Sales)}").scale(1.05).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l3)); self.wait(1.5)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = MathTex(r"\text{Check: } 1\,200 \times 1{,}25 = 1\,500\ \checkmark").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        b2_l6 = Tex("Gross profit today: R300").scale(1.05).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l5)); self.wait(1.5)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): the two pitfalls ---
        self.next_band(3)
        b3_t = Tex("Two pitfalls to bury now").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_t)); self.wait(1.5)
        b3_wrong1 = MathTex(r"25\%\ \text{off selling price: R1 125}").scale(1.05).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_wrong1))
        self.play(Create(strike(b3_wrong1)))
        self.wait(2)
        b3_r1 = Tex("Mark-up was ON COST: divide by 1,25").scale(1.05).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_r1))
        self.play(Create(SurroundingRectangle(b3_r1, color=GREEN)))
        self.wait(2)
        b3_wrong2 = Tex("Cost of Sales left empty — ``no cash moved''").scale(1.0).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_wrong2))
        self.play(Create(strike(b3_wrong2)))
        self.wait(2)
        b3_r2 = Tex("The column records the non-cash truth").scale(1.05).shift(band_shift(3) + DOWN * 2.0)
        b3_r3 = Tex("One line feeds Bank, Sales, CoS, Stock").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_r2)); self.wait(1.5)
        self.play(Write(b3_r3))
        self.wait(3)

        # --- Band 4 (subtopic_3): receipts that are not sales ---
        self.next_band(4)
        b4_t = Tex("Receipts that are not sales: Sundries").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t)); self.wait(1.5)
        b4_l1 = Tex("5th: T. Mokoena deposits capital R50 000").scale(1.0).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("Receipt 41; Analysis, Bank, Sundries: Capital").scale(1.0).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2)
        b4_l3 = Tex("12th: tenant pays R2 400 — Receipt 42").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("Analysis, Bank, Sundries: Rent income").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l3)); self.wait(1.5)
        self.play(Write(b4_l4)); self.wait(2)
        b4_l5 = Tex("Columns are frequency decisions:").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        b4_l6 = Tex("regulars get lanes, visitors get named").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5)); self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): totals ---
        self.next_band(5)
        b5_t = Tex("Month end: rule off and total").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t)); self.wait(1.5)
        b5_l0 = Tex("(28th adds cash sales R3 000, cost R2 400)").scale(0.95).shift(band_shift(5) + UP * 1.4)
        self.play(Write(b5_l0)); self.wait(2)
        b5_l1 = MathTex(r"\text{Bank: } 1\,500 + 50\,000 + 2\,400 + 3\,000").scale(1.0).shift(band_shift(5) + UP * 0.5)
        b5_l2 = MathTex(r"= \text{R56 900}").scale(1.1).shift(band_shift(5) + DOWN * 0.3)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        b5_l3 = Tex("Sales R4 500; Cost of Sales R3 600").scale(1.05).shift(band_shift(5) + DOWN * 1.2)
        b5_l4 = Tex("Sundries R52 400").scale(1.05).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l3)); self.wait(1.5)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the cross-cast proof ---
        self.next_band(6)
        b6_t = Tex("The proof: cross-cast").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_t)); self.wait(1.5)
        b6_l1 = MathTex(r"4\,500 + 52\,400 = 56\,900 = \text{Bank}\ \checkmark").scale(1.1).shift(band_shift(6) + UP * 1.2)
        self.play(Write(b6_l1))
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2.5)
        b6_l2 = Tex("Cost of Sales stands OUTSIDE the cross-cast").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = Tex("Postings: Bank DR; Sales CR;").scale(1.05).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = Tex("CoS DR and Trading Stock CR;").scale(1.05).shift(band_shift(6) + DOWN * 1.5)
        b6_l5 = Tex("each sundry item by name").scale(1.05).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l3)); self.wait(1.5)
        self.play(Write(b6_l4)); self.wait(1.5)
        self.play(Write(b6_l5)); self.wait(1.5)
        b6_l6 = Tex("Control: bank daily and intact; number the docs").scale(0.95).shift(band_shift(6) + DOWN * 3.1)
        self.play(Write(b6_l6))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the money-in diary ---
        self.next_band(7)
        b7_t = Tex("The money-in diary").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Money arrives $\\rightarrow$ one line: date,").scale(1.05).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex("the proof, who it came from, how much").scale(1.05).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1)); self.play(Write(b7_l2)); self.wait(2.5)
        b7_l3 = Tex("Sales, Sales, Sales... give it a lane").scale(1.05).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3)); self.wait(2)
        b7_l4 = Tex("R50 000 savings, tenant's rent: visitors —").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex("one open column, each amount NAMED").scale(1.05).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l4)); self.wait(1.5)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the double line ---
        self.next_band(8)
        b8_t = Tex("The double line: till and shelf").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Saturday: R1 500 in the till").scale(1.05).shift(band_shift(8) + UP * 1.3)
        self.play(Write(b8_l1)); self.wait(2)
        b8_wrong = MathTex(r"\text{Shelf number: } 25\%\ \text{off R1 500}").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_wrong))
        self.play(Create(strike(b8_wrong)))
        self.wait(2)
        b8_l2 = MathTex(r"1\,500 \div 1{,}25 = \text{R1 200}").scale(1.1).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2)
        b8_l3 = MathTex(r"\text{Forwards: } 1\,200 + 300 = 1\,500\ \checkmark").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l3)); self.wait(2)
        b8_l4 = Tex("R300 gross profit — known TODAY").scale(1.05).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(b8_l4))
        self.wait(3)

        # --- Band 9 (subtopic_7): the month-end handshake ---
        self.next_band(9)
        b9_t = Tex("The month-end handshake").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = MathTex(r"\text{Sales } 4\,500 + \text{Sundries } 52\,400 = 56\,900").scale(1.0).shift(band_shift(9) + UP * 1.3)
        b9_l2 = MathTex(r"\text{Bank column: } 56\,900\ \checkmark").scale(1.1).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1)); self.wait(2)
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex("If Bank shows R57 200: hunt the R300").scale(1.05).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l3)); self.wait(2)
        b9_l4 = Tex("Cost of sales sits out — shelf, not money").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        self.play(Write(b9_l4)); self.wait(2)
        b9_l5 = Tex("The CRJ is the shop watching its own cash").scale(1.0).shift(band_shift(9) + DOWN * 2.4)
        self.play(Write(b9_l5))
        self.wait(4)
