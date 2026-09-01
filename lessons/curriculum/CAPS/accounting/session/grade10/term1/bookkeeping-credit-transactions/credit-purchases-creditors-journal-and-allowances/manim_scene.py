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

# Band-layout whiteboard scene for the credit purchases (CJ + CAJ) duo.
# Exporter-safe primitives only; write-only reveals; camera moves down bands.
# Band time follows subtopics.json (180/200/190/200/170/180/180 of 1300 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CreditPurchasesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the mirror and the invoice received ---
        title = Tex("Credit Purchases: the Creditors Journal").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("In Metro's books: Thabo is a debtor").scale(1.05).shift(UP * 1.0)
        l02 = Tex("In OUR books: Metro is a CREDITOR — a liability").scale(1.0).shift(UP * 0.2)
        self.play(Write(l01)); self.wait(2)
        self.play(Write(l02)); self.wait(2)
        l03 = Tex("Source document: the invoice RECEIVED,").scale(1.0).shift(DOWN * 0.8)
        l04 = Tex("renumbered into our own sequence").scale(1.0).shift(DOWN * 1.6)
        self.play(Write(l03)); self.play(Write(l04)); self.wait(2)
        l05 = Tex("Same invoice, opposite sides — fix the mirror").scale(1.0).shift(DOWN * 2.6)
        self.play(Write(l05))
        self.play(Create(SurroundingRectangle(l05, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the CJ's columns ---
        self.next_band(1)
        b1_t = Tex("The CJ's columns").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_t)); self.wait(1.5)
        top_y = 1.5
        rail_top = Line(LEFT * 6.2 + UP * top_y, RIGHT * 6.2 + UP * top_y,
                        stroke_width=3).shift(band_shift(1))
        rail_bot = Line(LEFT * 6.2 + UP * (top_y - 1.0), RIGHT * 6.2 + UP * (top_y - 1.0),
                        stroke_width=3).shift(band_shift(1))
        self.play(Create(rail_top), Create(rail_bot))
        heads = VGroup(
            Tex("Inv").scale(0.85).move_to([-5.5, top_y - 0.5, 0]),
            Tex("Day").scale(0.85).move_to([-4.4, top_y - 0.5, 0]),
            Tex("Creditor").scale(0.85).move_to([-3.0, top_y - 0.5, 0]),
            Tex("Creditors Control").scale(0.85).move_to([-0.6, top_y - 0.5, 0]),
            Tex("Stock").scale(0.85).move_to([1.7, top_y - 0.5, 0]),
            Tex("Stationery").scale(0.85).move_to([3.3, top_y - 0.5, 0]),
            Tex("Equip/Sundry").scale(0.85).move_to([5.3, top_y - 0.5, 0]),
        ).shift(band_shift(1))
        self.play(Write(heads)); self.wait(2.5)
        b1_l1 = Tex("Every line strikes Creditors Control").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l1)); self.wait(2)
        b1_wrong = Tex("A cost of sales column in the CJ").scale(1.05).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(1.5)
        b1_l2 = Tex("Buying loads the shelf at cost — ONE truth;").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        b1_l3 = Tex("two truths belong to SELLING").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l2)); self.play(Write(b1_l3))
        self.wait(3)

        # --- Band 2 (subtopic_2): the month's purchases ---
        self.next_band(2)
        b2_t = Tex("The month's purchases").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_t)); self.wait(1.5)
        b2_l1 = Tex("3rd: stock, Metro, R9 000 — invoice 71").scale(1.0).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("9th: stationery, PNA, R400 — invoice 72").scale(1.0).shift(band_shift(2) + UP * 0.5)
        b2_l3 = Tex("15th: shelving, ShelfCo, R3 000 — invoice 73").scale(1.0).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l1)); self.wait(1.5)
        self.play(Write(b2_l2)); self.wait(1.5)
        self.play(Write(b2_l3)); self.wait(2)
        b2_l4 = Tex("Shelving is kept for use: EQUIPMENT (asset)").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l4)); self.wait(2)
        b2_l5 = Tex("Daily: Metro's personal account CREDITED R9 000").scale(0.95).shift(band_shift(2) + DOWN * 2.1)
        b2_l6 = Tex("— liabilities grow on the credit side").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5)); self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): totals, cross-cast, posting ---
        self.next_band(3)
        b3_t = Tex("Total, cross-cast, post").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_t)); self.wait(1.5)
        b3_l1 = MathTex(r"9\,000 + 400 + 3\,000 = 12\,400\ \checkmark").scale(1.05).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_l2 = Tex("CREDIT Creditors Control R12 400").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2)); self.wait(2)
        b3_l3 = Tex("DEBIT Trading Stock R9 000;").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex("DEBIT Stationery R400; Equipment R3 000").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l3)); self.play(Write(b3_l4)); self.wait(2.5)
        b3_l5 = MathTex(r"\text{Debits } 12\,400 = \text{credit } 12\,400").scale(1.0).shift(band_shift(3) + DOWN * 2.4)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): returns — debit note and CAJ ---
        self.next_band(4)
        b4_t = Tex("Returns to suppliers: the debit note").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t)); self.wait(1.5)
        b4_l1 = Tex("11th: Metro's box damaged — R800 back").scale(1.0).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("18th: PNA's wrong stationery — R100 back").scale(1.0).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1)); self.wait(1.5)
        self.play(Write(b4_l2)); self.wait(1.5)
        b4_l3 = Tex("WE issue the debit note — our record,").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        b4_l4 = Tex("our number, our timeline (CAJ)").scale(1.0).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3)); self.play(Write(b4_l4)); self.wait(2)
        b4_l5 = Tex("DEBIT Creditors Control R900;").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        b4_l6 = Tex("CREDIT Stock R800, Stationery R100").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5)); self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): what returns do NOT touch ---
        self.next_band(5)
        b5_t = Tex("What a return does not touch").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t)); self.wait(1.5)
        b5_wrong = Tex("Adjust cost of sales on the return").scale(1.05).shift(band_shift(5) + UP * 1.3)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l1 = Tex("Bought at cost, returned at cost —").scale(1.05).shift(band_shift(5) + UP * 0.4)
        b5_l2 = Tex("only selling creates the two-truths pair").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1)); self.play(Write(b5_l2)); self.wait(2.5)
        b5_l3 = Tex("And no money moved: returns adjust the DEBT;").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        b5_l4 = Tex("payment is a separate event, separate journal").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l3)); self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the pages, the list, the lock ---
        self.next_band(6)
        b6_t = Tex("Balance the pages, run the lock").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_t)); self.wait(1.5)
        b6_l1 = MathTex(r"\text{Metro: } 9\,000 - 800 = 8\,200\ \text{credit}").scale(1.0).shift(band_shift(6) + UP * 1.3)
        b6_l2 = MathTex(r"\text{PNA: } 400 - 100 = 300; \quad \text{ShelfCo: } 3\,000").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = MathTex(r"\text{List: } 8\,200 + 300 + 3\,000 = 11\,500").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l3)); self.wait(2)
        b6_l4 = MathTex(r"\text{Control: } 12\,400 - 900 = 11\,500\ \checkmark").scale(1.0).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex("Match order + delivery note + invoice;").scale(0.95).shift(band_shift(6) + DOWN * 2.5)
        b6_l6 = Tex("pay on terms; recorder $\\neq$ authoriser").scale(0.95).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l5)); self.play(Write(b6_l6))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the other side of the counter ---
        self.next_band(7)
        b7_t = Tex("The other side of the counter").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Thabo is a name in Metro's book now —").scale(1.0).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex("but he keeps his own book about THEM").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1)); self.play(Write(b7_l2)); self.wait(2.5)
        b7_l3 = Tex("Debtors: more coming in — grows debit side").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("Creditors: more going out — grows credit side").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3)); self.wait(2)
        self.play(Write(b7_l4)); self.wait(2)
        b7_l5 = Tex("Buying writes ONE truth: shelf loads at cost").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): the month of buying on trust ---
        self.next_band(8)
        b8_t = Tex("The month of buying on trust").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Stock R9 000; stationery R400 (used up);").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("shelving R3 000 — a possession: equipment").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1)); self.play(Write(b8_l2)); self.wait(2.5)
        b8_l3 = Tex("Damaged box back with a numbered letter:").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("debit note — Metro's page shrinks R800").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3)); self.play(Write(b8_l4)); self.wait(2.5)
        b8_l5 = MathTex(r"8\,200 + 300 + 3\,000 = 11\,500 = \text{control}\ \checkmark").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): paying like a pro ---
        self.next_band(9)
        b9_t = Tex("Paying like a pro").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("1. Three papers, one story: order,").scale(1.0).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex("delivery note, invoice — then pay").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1)); self.play(Write(b9_l2)); self.wait(2.5)
        b9_wrong = Tex("Invoiced 10 boxes, received 9 — pay anyway").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2)
        b9_l3 = Tex("2. On terms, on time — not late, not early:").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        b9_l4 = Tex("supplier credit is free financing").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l3)); self.play(Write(b9_l4)); self.wait(2)
        b9_l5 = Tex("3. Reconcile their statement to our page").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l5))
        self.wait(4)
