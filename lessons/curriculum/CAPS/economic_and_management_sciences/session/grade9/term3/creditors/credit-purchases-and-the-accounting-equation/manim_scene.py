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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex keep the export to the
# allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/250/250/180/180/180 of
# 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CreditPurchasesEquationSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Buying on Credit and Creditors
        b0_title = Tex("Buying on credit").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Goods now, pay later").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Supplier becomes a creditor").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Creditors: a liability").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Mirror image of debtors").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Accounting Cycle for Credit Purchases
        self.next_band(1)
        b1_title = Tex("The cycle for purchases").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Original invoice from supplier").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Creditors journal (CJ)").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Creditors ledger and control").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Payment later in the CPJ").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Credit Purchases in the Accounting Equation
        self.next_band(2)
        b2_title = Tex("Credit purchases: A = OE + L").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Stock 8 000: A +, L +").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Stationery 600: OE -, L +").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Equipment 3 500: A +, L +").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Liabilities always rise").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Paying Creditors and the Full Analysis
        self.next_band(3)
        b3_title = Tex("Paying a creditor").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Bank - 5 000").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Creditors - 5 000").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("No effect on OE").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Not an expense").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Paying Creditors and the Full Analysis
        self.next_band(4)
        b4_title = Tex("The full table").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Assets + 6 500").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("Owner's equity - 600").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("Liabilities + 7 100").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("- 600 + 7 100 = 6 500").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)

        # --- Band 5 (subtopic_4): Paying Creditors and the Full Analysis
        self.next_band(5)
        b5_title = Tex("Error museum").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("``Paying a creditor is an expense''").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("``Buying stock lowers OE''").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("``Stationery is an asset''").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("``Creditors are assets''").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)



        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): Take Now, Pay Later
        self.next_band(6)
        b6_title = Tex("Take now, pay later").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Supplier we owe: creditor").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Debtors owe us: asset").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("We owe creditors: liability").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Keep the original invoice").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_6): What Goes Up When We Buy on Credit
        self.next_band(7)
        b7_title = Tex("What goes up").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Liability always goes up").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Stock or equipment: asset up").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Stationery: OE down").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Still own it? Asset").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)

        # --- Band 8 (subtopic_7): Paying What We Owe
        self.next_band(8)
        b8_title = Tex("Paying what we owe").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Bank down, liability down").scale(0.9).shift(band_shift(8) + UP * 1.30)
        b8_l2 = Tex("OE unchanged").scale(0.9).shift(band_shift(8) + UP * 0.35)
        b8_l3 = Tex("Owe 3 000 + 600 + 3 500").scale(0.9).shift(band_shift(8) + DOWN * 0.60)
        b8_l4 = Tex("Total 7 100").scale(0.9).shift(band_shift(8) + DOWN * 1.55)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(4)
