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

# Band-layout whiteboard scene for "Final Accounts and the Year-End Run"
# (grade10 term2, year-end-procedures-and-final-accounts). One band per
# teaching beat, add-only lifecycle, camera moves down between bands.
# Exporter-safe mobjects only (Tex/MathTex/Line/Rectangle/
# SurroundingRectangle/VGroup).
#
# Subtopic time shares (subtopics.json, total 1400 s):
# 210/220/220/200/180/190/180 -> bands 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinalAccountsYearEndRunSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the bridge and its sequence ---
        title = Tex("The Year-End Bridge").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Pre-adjustment trial balance").scale(1.0).shift(UP * 1.2)
        b0_l2 = Tex(r"$\Rightarrow$ adjustments").scale(1.0).shift(UP * 0.4)
        b0_l3 = Tex(r"$\Rightarrow$ post-adjustment trial balance").scale(1.0).shift(DOWN * 0.4)
        b0_l4 = Tex(r"$\Rightarrow$ final accounts $\Rightarrow$ statements").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(b0_l1))
        self.wait(1.5)
        self.play(Write(b0_l2))
        self.wait(1.5)
        self.play(Write(b0_l3))
        self.wait(1.5)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("The books must meet REALITY").scale(1.05).shift(DOWN * 2.2)
        b0_l6 = Tex("before they may report").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.play(Create(SurroundingRectangle(b0_l6, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the GAAP authority ---
        self.next_band(1)
        b1_title = Tex("The GAAP authority").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("MATCHING: this year's incomes and").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("expenses -- no more, no less").scale(1.0).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("PRUDENCE: losses the moment found").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("GOING CONCERN: the business continues").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        b1_l5 = Tex("HISTORICAL COST: values stay anchored").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex("Not tradition -- principles in order").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): consumable stores on hand ---
        self.next_band(2)
        b2_title = Tex("Consumable stores on hand").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Stationery account: R1 500 expensed").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("Cupboard at year end: R300 unused").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_w = Tex("Did the year USE R1 500?").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_w))
        self.play(Create(strike(b2_w)))
        self.wait(1.5)
        b2_l3 = Tex("Credit Stationery 300;").scale(1.0).shift(band_shift(2) + DOWN * 1.5)
        b2_l4 = Tex("debit Consumable Stores on Hand 300").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Expense 1 200 used; asset 300 waiting").scale(0.95).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the trading stock deficit ---
        self.next_band(3)
        b3_title = Tex("The trading stock deficit").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("The account claims R3 100;").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("the stocktake counts R2 880").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_m1 = MathTex(r"3\,100 - 2\,880 = 220 \text{ missing}").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_m1))
        self.wait(2)
        b3_l3 = Tex("Credit Trading Stock 220;").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        b3_l4 = Tex("debit Trading Stock Deficit 220").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("The count is the fact -- prudence acts now").scale(0.9).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the Trading account ---
        self.next_band(4)
        b4_title = Tex("The Trading account").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Sales R150 000 closes in $\Rightarrow$ credit").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"Cost of Sales R100 000 $\Rightarrow$ debit").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_m1 = MathTex(r"150\,000 - 100\,000 = \text{R50 000}").scale(1.05).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_m1))
        self.wait(2)
        b4_l3 = Tex("GROSS PROFIT -- the trading result").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = Tex("Check: 50\\% on 100 000 = 50 000 --").scale(0.95).shift(band_shift(4) + DOWN * 2.4)
        b4_l5 = Tex("the pricing kept its word").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(3)

        # --- Band 5 (subtopic_3): Profit and Loss, and Capital ---
        self.next_band(5)
        b5_title = Tex("Profit and Loss, then Capital").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("In: gross profit 50 000 + rent 9 000").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_m1 = MathTex(r"= 59\,000").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.play(Write(b5_m1))
        self.wait(2)
        b5_l2 = Tex("Out: salaries 18 000, phone 1 550,").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l3 = Tex("stationery 1 200, charges 430, deficit 220").scale(0.9).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.wait(2)
        b5_m2 = MathTex(r"59\,000 - 21\,400 = \text{R37 600}").scale(1.05).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_m2))
        self.play(Create(SurroundingRectangle(b5_m2, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex("NET PROFIT -- to Capital, the owner's").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the run, in order ---
        self.next_band(6)
        b6_title = Tex("The year-end run, in order").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("1. Pre-adjustment trial balance").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("2. Adjustments, with narrations").scale(0.95).shift(band_shift(6) + UP * 0.5)
        b6_l3 = Tex("3. Post-adjustment trial balance").scale(0.95).shift(band_shift(6) + DOWN * 0.2)
        b6_l4 = Tex("4. Final accounts: Trading, P\\&L").scale(0.95).shift(band_shift(6) + DOWN * 0.9)
        b6_l5 = Tex("5. Profit to Capital").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        b6_l6 = Tex("6. The financial statements").scale(0.95).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l1))
        self.wait(1.2)
        self.play(Write(b6_l2))
        self.wait(1.2)
        self.play(Write(b6_l3))
        self.wait(1.2)
        self.play(Write(b6_l4))
        self.wait(1.2)
        self.play(Write(b6_l5))
        self.wait(1.2)
        self.play(Write(b6_l6))
        self.wait(2)
        b6_l7 = Tex("Each step certifies the next -- the order").scale(0.9).shift(band_shift(6) + DOWN * 3.1)
        b6_l8 = Tex("IS the control").scale(0.95).shift(band_shift(6) + DOWN * 3.7)
        self.play(Write(b6_l7))
        self.play(Write(b6_l8))
        self.play(Create(SurroundingRectangle(b6_l8, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): three exam habits ---
        self.next_band(7)
        b7_title = Tex("Three habits").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("1. Every adjustment: BOTH accounts,").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("both directions -- no half-adjustments").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("2. Trace downstream: one fact,").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("two appearances").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex("3. Name the principle with the step:").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        b7_l6 = Tex("matching, prudence, going concern").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): report card day ---
        self.next_band(8)
        b8_title = Tex("The shop's report card day").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("A year of diary must become").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("one page of report card").scale(1.05).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("But lines have drifted: the cupboard").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        b8_l4 = Tex("holds 300; the shelf holds 2 880").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Two jobs, strict order:").scale(1.05).shift(band_shift(8) + DOWN * 2.2)
        b8_l6 = Tex("tidy first, squeeze second").scale(1.05).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the two tidyings ---
        self.next_band(9)
        b9_title = Tex("Tidying before the photo").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Cupboard: 1 200 used stays expense;").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("300 waiting becomes a parcel-asset").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Shelf: the count wins -- books down 220,").scale(0.95).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = Tex("the loss named and admitted NOW").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Bad news immediately; good news").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        b9_l6 = Tex("waits to be proven").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): two sieves and the owner's jar ---
        self.next_band(10)
        b10_title = Tex("Two sieves and the owner's jar").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Sieve one: sales 150 000 less cost").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex(r"100 000 $\Rightarrow$ gross 50 000").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Sieve two: 59 000 of earning, 21 400").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l4 = Tex(r"drains $\Rightarrow$ net 37 600").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("Into the owner's jar: Capital.").scale(1.05).shift(band_shift(10) + DOWN * 2.1)
        b10_l6 = Tex("Clean pages for the new year").scale(1.05).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(VGroup(b10_l5, b10_l6), color=GREEN)))
        self.wait(4)
