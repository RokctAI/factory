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

# Band-layout whiteboard scene for the cash-payments / petty-cash session duo.
# Exporter-safe primitives only (Tex/MathTex/Line/Arrow/Rectangle/VGroup);
# write-only reveals; the camera never returns to a written band — it
# moves down to fresh bands instead. Band time is apportioned to subtopics.json
# (190/210/170/200/150/180/180 of 1280 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CashPaymentsAndPettyCashSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the CPJ's job ---
        title = Tex("The Cash Payments Journal").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("ALL payments from the bank account,").scale(1.0).shift(UP * 1.1)
        l02 = Tex("in date order, for one month").scale(1.0).shift(UP * 0.3)
        self.play(Write(l01)); self.play(Write(l02)); self.wait(2.5)
        l03 = Tex("Proof: numbered EFT proof of payment").scale(0.95).shift(DOWN * 0.7)
        l04 = Tex("Name column: the PAYEE — who was paid").scale(0.95).shift(DOWN * 1.5)
        self.play(Write(l03)); self.wait(2)
        self.play(Write(l04))
        self.wait(3)

        # --- Band 1 (subtopic_1): column skeleton + perpetual point ---
        self.next_band(1)
        b1_t = Tex("Columns: Bank + the lanes").scale(1.15).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_t)); self.wait(2)
        b1_l1 = Tex("Bank — every payment strikes it").scale(1.0).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("Lanes: Trading Stock, Wages;").scale(1.0).shift(band_shift(1) + UP * 0.6)
        b1_l3 = Tex("Sundries for the named visitors").scale(1.0).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l1)); self.wait(2)
        self.play(Write(b1_l2)); self.play(Write(b1_l3)); self.wait(2.5)
        b1_wrong = Tex("Buying stock $\\rightarrow$ Purchases account").scale(0.95).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        b1_l4 = Tex("Perpetual system: Trading Stock, at cost").scale(0.95).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the first three payments ---
        self.next_band(2)
        b2_t = Tex("The month, line by line").scale(1.15).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("3rd: Coastal Wholesalers, EFT 201 —").scale(0.95).shift(band_shift(2) + UP * 1.4)
        b2_l2 = Tex("Bank R9 500; Trading Stock R9 500").scale(0.95).shift(band_shift(2) + UP * 0.6)
        self.play(Write(b2_l1)); self.play(Write(b2_l2)); self.wait(2.5)
        b2_l3 = Tex("9th: Wages, EFT 202 — Bank R1 800; Wages R1 800").scale(0.9).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l3)); self.wait(2)
        b2_l4 = Tex("16th: rent, EFT 203 —").scale(0.95).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex("Sundries R4 200: Rent expense").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4)); self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the shelving and the drawings trap ---
        self.next_band(3)
        b3_t = Tex("Two payments that fool people").scale(1.15).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("21st: shelving R5 500 — kept for years:").scale(0.95).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("an ASSET — Sundries: Equipment").scale(1.0).shift(band_shift(3) + UP * 0.6)
        self.play(Write(b3_l1)); self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = Tex("26th: owner takes R2 500 for herself").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l3)); self.wait(2)
        b3_wrong = Tex("Just another expense of the month").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        b3_l4 = Tex("DRAWINGS — the owner's own stake, out").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): totals and the cross-cast ---
        self.next_band(4)
        b4_t = Tex("Total, then prove").scale(1.2).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("Bank: R25 300").scale(1.05).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("Trading Stock 9 500; Wages 3 600;").scale(0.95).shift(band_shift(4) + UP * 0.6)
        b4_l3 = Tex("Sundries 12 200").scale(1.0).shift(band_shift(4) + DOWN * 0.2)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.play(Write(b4_l3)); self.wait(2.5)
        b4_l4 = MathTex(r"9\,500 + 3\,600 + 12\,200 = 25\,300\ \checkmark").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): what posts where + control ---
        self.next_band(5)
        b5_t = Tex("Where the totals go").scale(1.15).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("Bank total: CREDIT Bank").scale(1.0).shift(band_shift(5) + UP * 1.4)
        b5_l2 = Tex("Trading Stock: debit; Wages: debit").scale(1.0).shift(band_shift(5) + UP * 0.6)
        b5_l3 = Tex("Sundries: each item by name, debit").scale(1.0).shift(band_shift(5) + DOWN * 0.2)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        self.play(Write(b5_l3)); self.wait(2)
        b5_l4 = Tex("Control: approved documents, numbered EFTs,").scale(0.9).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex("approver $\\neq$ capturer, monthly reconciliation").scale(0.9).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4)); self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the imprest system ---
        self.next_band(6)
        b6_t = Tex("Petty cash: the imprest system").scale(1.15).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("Fixed float: R600").scale(1.05).shift(band_shift(6) + UP * 1.4)
        self.play(Write(b6_l1)); self.wait(2)
        b6_l2 = Tex("Every payment $\\rightarrow$ signed, numbered voucher").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = MathTex(r"\text{cash} + \text{vouchers} = R600").scale(1.1).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)
        b6_l4 = Tex("At any moment, in coin or in paper").scale(0.95).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l4))
        self.wait(3)

        # --- Band 7 (subtopic_4): month-end restoration ---
        self.next_band(7)
        b7_t = Tex("Month end: restore the float").scale(1.15).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Stamps 75 + taxi 90 + tea 140 + cleaning 115").scale(0.9).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("= vouchers R420").scale(1.05).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1)); self.wait(2)
        self.play(Write(b7_l2)); self.wait(2)
        b7_l3 = Tex("Restoration = voucher total: R420 from bank").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3)); self.wait(2)
        b7_l4 = Tex("Tin stands at R600 for the new month").scale(0.95).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the money-out diary ---
        self.next_band(8)
        b8_t = Tex("The money-out diary").scale(1.2).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("One line: date, proof, WHO, how much").scale(1.0).shift(band_shift(8) + UP * 1.4)
        self.play(Write(b8_l1)); self.wait(2)
        b8_l2 = Tex("Constant payments get lanes:").scale(1.0).shift(band_shift(8) + UP * 0.5)
        b8_l3 = Tex("stock, wages — the rest get named").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8_l2)); self.play(Write(b8_l3)); self.wait(2.5)
        b8_l4 = Tex("Handshake: lanes + visitors = Bank column").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the day Lindi paid herself ---
        self.next_band(9)
        b9_t = Tex("The day Lindi paid herself").scale(1.2).shift(band_shift(9) + UP * 2.5)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("The sorting question:").scale(1.0).shift(band_shift(9) + UP * 1.5)
        b9_l2 = Tex("what did the STORE get?").scale(1.1).shift(band_shift(9) + UP * 0.7)
        self.play(Write(b9_l1)); self.play(Write(b9_l2)); self.wait(2.5)
        b9_l3 = Tex("Stock: shelves fuller. Wages: work done.").scale(0.9).shift(band_shift(9) + DOWN * 0.2)
        b9_l4 = Tex("Rent: a roof. Shelving: kept for years.").scale(0.9).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l3)); self.wait(2)
        self.play(Write(b9_l4)); self.wait(2)
        b9_l5 = Tex("R2 500 to Lindi: the store got NOTHING").scale(0.95).shift(band_shift(9) + DOWN * 1.9)
        b9_l6 = Tex("Drawings — the owner's stake, not a cost").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5)); self.wait(2)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_7): the tin that tells the truth ---
        self.next_band(10)
        b10_t = Tex("The tin that always tells the truth").scale(1.15).shift(band_shift(10) + UP * 2.5)
        self.play(Write(b10_t)); self.wait(2)
        b10_l1 = Tex("Always worth R600: cash + slips").scale(1.0).shift(band_shift(10) + UP * 1.4)
        self.play(Write(b10_l1)); self.wait(2)
        b10_l2 = Tex("R260 cash + R340 slips: perfect").scale(0.95).shift(band_shift(10) + UP * 0.5)
        b10_l3 = Tex("R260 cash + R310 slips: R30 missing — today").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        self.play(Write(b10_l2)); self.wait(2)
        self.play(Write(b10_l3)); self.wait(2.5)
        b10_l4 = Tex("Refill = slips: R420, tin back to R600").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("One keeper, one set of keys").scale(0.95).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_l5))
        self.wait(4)
