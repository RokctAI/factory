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
# dwell time proportional to subtopics.json (210/240/220/240/180/190/180 of
# 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TradingBusinessCashSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): What Makes a Trading Business Different
        b0_title = Tex("A trading business").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Buys goods to sell: trading stock").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Stock is a current asset").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Sold: cost becomes cost of sales").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Sales - cost of sales = gross profit").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Cost Price, Mark-up, Selling Price and Gross Profit
        self.next_band(1)
        b1_title = Tex("Mark-up on cost").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("600 + 50 percent: 600 + 300 = 900").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("2 500 x 1,4 = 3 500").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Cost: 1 200 x 100 / 150 = 800").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("7 000 x 100 / 140 = 5 000").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Cash Transactions and Their Source Documents
        self.next_band(2)
        b2_title = Tex("Source documents").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Cash sales: cash register roll").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Other money in: duplicate receipt").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Money out: EFT proof, bank statement").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Deposit slip: money banked").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Trading Transactions in the Accounting Equation
        self.next_band(3)
        b3_title = Tex("Trading in the equation").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Buy stock: A +10 000, A -10 000").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Sale: A +900, OE +900 (sales)").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("A -600, OE -600 (cost of sales)").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Drawings of stock: at cost").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Trading Transactions in the Accounting Equation
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Buying stock is an expense''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``A sale has one effect''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Drawings of stock at selling price''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Cost = selling price less 50 percent''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Buy Low, Sell Higher
        self.next_band(5)
        b5_title = Tex("Buy low, sell higher").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Spaza buys chips: a swap").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Chips on the shelf: an asset").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Sold: sales and cost of sales").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("The gap: gross profit").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Working Out Mark-up Like a Shopkeeper
        self.next_band(6)
        b6_title = Tex("Mark-up like a shopkeeper").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Cost 100 parts, mark-up 50 parts").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Selling price 150 parts").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("1 200 / 150 = 8; 8 x 100 = 800").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Check: 800 + 400 = 1 200").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Two Sides of Every Sale
        self.next_band(7)
        b7_title = Tex("Two sides of every sale").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Heads: bank +900, sales").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Tails: stock -600, cost of sales").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Net: +300 gross profit").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("No paper, no entry").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
