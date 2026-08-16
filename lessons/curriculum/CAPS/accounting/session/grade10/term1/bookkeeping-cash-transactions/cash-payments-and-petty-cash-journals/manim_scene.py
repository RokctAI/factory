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

# Band-layout whiteboard scene for the CPJ + Petty Cash Journal session duo.
# Exporter-safe vocabulary only (Tex/MathTex/Line/Rectangle/SurroundingRectangle/
# VGroup); write-only reveals — nothing is transformed or faded out, the camera
# moves down to fresh bands instead. Band time is apportioned to subtopics.json
# (190/210/170/200/150/180/180 of 1280 s); Level 6 rescales to real audio.

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
        # Intro beat: topic held full-screen while intro.md plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the CPJ's job ---
        title = Tex("The Cash Payments Journal").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Records ALL payments from the bank").scale(1.1).shift(UP * 1.0)
        l02 = Tex("Source document: numbered EFT proof").scale(1.1)
        l03 = Tex("Name column = the PAYEE (who was paid)").scale(1.1).shift(DOWN * 1.0)
        self.play(Write(l01)); self.wait(2)
        self.play(Write(l02)); self.wait(2)
        self.play(Write(l03)); self.wait(2)
        l04 = Tex("One direction per book: receipts never enter").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(l04))
        self.wait(3)

        # --- Band 1 (subtopic_1): column skeleton + perpetual point ---
        self.next_band(1)
        b1_t = Tex("CPJ columns: regulars get lanes").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_t)); self.wait(1.5)
        # Journal skeleton: rails first, headings into them.
        top_y = 1.5
        rail_top = Line(LEFT * 6.2 + UP * top_y, RIGHT * 6.2 + UP * top_y,
                        stroke_width=3).shift(band_shift(1))
        rail_bot = Line(LEFT * 6.2 + UP * (top_y - 1.0), RIGHT * 6.2 + UP * (top_y - 1.0),
                        stroke_width=3).shift(band_shift(1))
        self.play(Create(rail_top), Create(rail_bot))
        heads = VGroup(
            Tex("Doc").scale(0.9).move_to([-5.4, top_y - 0.5, 0]),
            Tex("Day").scale(0.9).move_to([-4.2, top_y - 0.5, 0]),
            Tex("Name of payee").scale(0.9).move_to([-2.2, top_y - 0.5, 0]),
            Tex("Bank").scale(0.9).move_to([0.4, top_y - 0.5, 0]),
            Tex("Trading Stock").scale(0.9).move_to([2.4, top_y - 0.5, 0]),
            Tex("Wages").scale(0.9).move_to([4.3, top_y - 0.5, 0]),
            Tex("Sundry").scale(0.9).move_to([5.6, top_y - 0.5, 0]),
        ).shift(band_shift(1))
        self.play(Write(heads)); self.wait(2.5)
        b1_l1 = Tex("Every payment strikes the Bank column").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l1)); self.wait(2)
        b1_wrong = Tex("Buying stock $\\rightarrow$ ``Purchases'' account").scale(1.05).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(1.5)
        b1_right = Tex("Perpetual system: Trading Stock column").scale(1.05).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_right))
        self.play(Create(SurroundingRectangle(b1_right, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the first three payments ---
        self.next_band(2)
        b2_t = Tex("Thabo's Trading — the month's payments").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_t)); self.wait(1.5)
        b2_l1 = Tex("2nd: stock, Metro Wholesalers, EFT 101").scale(1.0).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("Bank R8 000; Trading Stock R8 000").scale(1.05).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1)); self.wait(1.5)
        self.play(Write(b2_l2)); self.wait(2)
        b2_l3 = Tex("8th: wages paid, EFT 102").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex("Bank R1 500; Wages R1 500 (again 28th)").scale(1.05).shift(band_shift(2) + DOWN * 1.2)
        self.play(Write(b2_l3)); self.wait(1.5)
        self.play(Write(b2_l4)); self.wait(2)
        b2_l5 = Tex("15th: rent, EFT 103 — no lane:").scale(1.0).shift(band_shift(2) + DOWN * 2.1)
        b2_l6 = Tex("Sundries R3 500, detail: Rent expense").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l5)); self.wait(1.5)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): the fridge and the drawings trap ---
        self.next_band(3)
        b3_t = Tex("Asset, expense — or drawings?").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_t)); self.wait(1.5)
        b3_l1 = Tex("20th: display fridge R6 000, EFT 104").scale(1.05).shift(band_shift(3) + UP * 1.3)
        b3_l2 = Tex("Kept for years $\\Rightarrow$ ASSET: Sundries, Equipment").scale(0.95).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1)); self.wait(2)
        self.play(Write(b3_l2)); self.wait(2)
        b3_l3 = Tex("25th: owner takes R2 000, EFT 105").scale(1.05).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l3)); self.wait(1.5)
        b3_wrong = Tex("Record it as an expense").scale(1.05).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l4 = Tex("Business received nothing $\\Rightarrow$ DRAWINGS").scale(1.05).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("Test: did the BUSINESS receive value?").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): totals and the cross-cast ---
        self.next_band(4)
        b4_t = Tex("Month end: rule off, total, prove").scale(1.15).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t)); self.wait(1.5)
        b4_l1 = MathTex(r"\text{Bank: } 8\,000 + 1\,500 + 3\,500").scale(1.05).shift(band_shift(4) + UP * 1.3)
        b4_l2 = MathTex(r"+\, 6\,000 + 2\,000 + 1\,500 = \text{R22 500}").scale(1.05).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1)); self.wait(1.5)
        self.play(Write(b4_l2)); self.wait(2)
        b4_l3 = Tex("Stock R8 000; Wages R3 000; Sundries R11 500").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l3)); self.wait(2)
        b4_l4 = Tex("Cross-cast: analysis must explain Bank").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        b4_l5 = MathTex(r"8\,000 + 3\,000 + 11\,500 = 22\,500\ \checkmark").scale(1.1).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l4)); self.wait(1.5)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): what posts where + control ---
        self.next_band(5)
        b5_t = Tex("The posting picture").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t)); self.wait(1.5)
        b5_l1 = Tex("Bank total R22 500 $\\rightarrow$ CREDIT Bank").scale(1.05).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Trading Stock R8 000 $\\rightarrow$ DEBIT Trading Stock").scale(1.0).shift(band_shift(5) + UP * 0.5)
        b5_l3 = Tex("Wages R3 000 $\\rightarrow$ DEBIT Wages").scale(1.05).shift(band_shift(5) + DOWN * 0.3)
        b5_l4 = Tex("Sundries post one by one: Rent,").scale(1.05).shift(band_shift(5) + DOWN * 1.1)
        b5_l5 = Tex("Equipment, Drawings — each DEBITED").scale(1.05).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        self.play(Write(b5_l3)); self.wait(2)
        self.play(Write(b5_l4)); self.play(Write(b5_l5)); self.wait(2)
        b5_l6 = Tex("Control: approver $\\neq$ capturer; reconcile monthly").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the imprest system ---
        self.next_band(6)
        b6_t = Tex("Petty cash: the imprest system").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_t)); self.wait(1.5)
        b6_l1 = Tex("Float is FIXED: R500").scale(1.1).shift(band_shift(6) + UP * 1.3)
        self.play(Write(b6_l1)); self.wait(2)
        b6_l2 = Tex("Every payment $\\rightarrow$ numbered, signed voucher").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = MathTex(r"\text{cash in tin} + \text{vouchers} = \text{R500}").scale(1.15).shift(band_shift(6) + DOWN * 0.6)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("R95 cash + R360 vouchers: balances").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        b6_l5 = Tex("R95 cash + R340 vouchers: R65 short!").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(b6_l4)); self.wait(2)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_4): month-end restoration ---
        self.next_band(7)
        b7_t = Tex("Month end: total the vouchers").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_t)); self.wait(1.5)
        b7_l1 = Tex("Stamps R60; taxi fare R85").scale(1.05).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex("Tea and coffee R120; cleaning R95").scale(1.05).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1)); self.wait(1.5)
        self.play(Write(b7_l2)); self.wait(1.5)
        b7_l3 = MathTex(r"60 + 85 + 120 + 95 = \text{R360}").scale(1.1).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3)); self.wait(2)
        b7_l4 = Tex("Restore R360 from the bank (via CPJ)").scale(1.05).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4)); self.wait(2)
        b7_l5 = Tex("Tin back to R500 for the new month").scale(1.05).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the money-out diary ---
        self.next_band(8)
        b8_t = Tex("The money-out diary").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Money leaves $\\rightarrow$ one line: date,").scale(1.05).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("proof number, WHO was paid, how much").scale(1.05).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1)); self.play(Write(b8_l2)); self.wait(2.5)
        b8_l3 = Tex("Lanes: Stock, Wages — the regulars").scale(1.05).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("Visitors named in one open column").scale(1.05).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3)); self.wait(2)
        self.play(Write(b8_l4)); self.wait(2)
        b8_l5 = Tex("Handshake: lanes + visitors = Bank R22 500").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the day Thabo paid himself ---
        self.next_band(9)
        b9_t = Tex("The day Thabo paid himself").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("Sorting question: what did the SHOP get?").scale(1.05).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1)); self.wait(2)
        b9_l2 = Tex("R8 000 $\\rightarrow$ stock; wages $\\rightarrow$ work;").scale(1.05).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex("rent $\\rightarrow$ a roof; fridge $\\rightarrow$ a machine").scale(1.05).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l2)); self.play(Write(b9_l3)); self.wait(2.5)
        b9_wrong = Tex("R2 000 to Thabo: just another cost").scale(1.05).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_wrong))
        self.play(Create(strike(b9_wrong)))
        self.wait(2)
        b9_l4 = Tex("Shop got nothing $\\Rightarrow$ DRAWINGS, not expense").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        b9_l5 = Tex("Hide it in expenses: shop looks R2 000 weaker").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the tin that tells the truth ---
        self.next_band(10)
        b10_t = Tex("The tin that always tells the truth").scale(1.2).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_t)); self.wait(2)
        b10_l1 = MathTex(r"\text{cash} + \text{slips} = \text{R500, always}").scale(1.1).shift(band_shift(10) + UP * 1.3)
        self.play(Write(b10_l1)); self.wait(2)
        b10_l2 = Tex("R245 cash + R255 slips: perfect").scale(1.05).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex("R245 cash + R230 slips: R25 missing").scale(1.05).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l2)); self.wait(2)
        self.play(Write(b10_l3))
        self.play(Create(strike(b10_l3)))
        self.wait(2)
        b10_l4 = MathTex(r"\text{Slips: } 60 + 85 + 120 + 95 = \text{R360}").scale(1.05).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(b10_l4)); self.wait(2)
        b10_l5 = Tex("Refill = slip total: R360 $\\rightarrow$ tin at R500").scale(1.05).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(4)
