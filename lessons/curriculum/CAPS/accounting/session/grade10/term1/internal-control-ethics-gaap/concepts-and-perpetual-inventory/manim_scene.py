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

# Band-layout whiteboard scene for "Concepts and Perpetual Inventory"
# (grade10 term1, internal-control-ethics-gaap). One band per teaching beat,
# add-only lifecycle, camera moves down between bands. Exporter-safe mobjects
# only (Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup).
#
# Subtopic time shares (subtopics.json, total 1260 s):
# 180/190/170/200/180/160/180 -> bands 0-1 / 2-3 / 4 / 5-6 / 7 / 8 / 9.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ConceptsAndPerpetualInventorySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the sole trader and the entity rule ---
        title = Tex("Concepts and Perpetual Inventory").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Sole trader: one owner, in their own right").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("In LAW: owner and business are one --").scale(1.05).shift(UP * 0.3)
        b0_l3 = Tex("owner personally liable for its debts").scale(1.05).shift(DOWN * 0.5)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex("In the RECORDS: kept separate --").scale(1.05).shift(DOWN * 1.5)
        b0_l5 = Tex("the business entity rule").scale(1.1).shift(DOWN * 2.4)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the elements on a T layout ---
        self.next_band(1)
        b1_title = Tex("The elements and their sides").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        t_top = Line(LEFT * 3.5, RIGHT * 3.5).shift(band_shift(1) + UP * 1.3)
        t_mid = Line(UP * 1.3, DOWN * 2.0).shift(band_shift(1))
        self.play(Create(t_top))
        self.play(Create(t_mid))
        b1_dr = Tex("Debit (left)").scale(1.05).shift(band_shift(1) + UP * 1.7 + LEFT * 1.9)
        b1_cr = Tex("Credit (right)").scale(1.05).shift(band_shift(1) + UP * 1.7 + RIGHT * 1.9)
        self.play(Write(b1_dr))
        self.play(Write(b1_cr))
        self.wait(2)
        b1_a1 = Tex("Assets grow here").scale(1.0).shift(band_shift(1) + UP * 0.5 + LEFT * 1.9)
        b1_a2 = Tex("Expenses grow here").scale(1.0).shift(band_shift(1) + DOWN * 0.4 + LEFT * 1.9)
        self.play(Write(b1_a1))
        self.play(Write(b1_a2))
        self.wait(2)
        b1_c1 = Tex("Liabilities").scale(1.0).shift(band_shift(1) + UP * 0.5 + RIGHT * 1.9)
        b1_c2 = Tex("Owner's equity").scale(1.0).shift(band_shift(1) + DOWN * 0.4 + RIGHT * 1.9)
        b1_c3 = Tex("Incomes").scale(1.0).shift(band_shift(1) + DOWN * 1.3 + RIGHT * 1.9)
        self.play(Write(b1_c1))
        self.play(Write(b1_c2))
        self.play(Write(b1_c3))
        self.wait(2)
        b1_rule = Tex("Debit what grows left; credit what grows right").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_rule))
        self.play(Create(SurroundingRectangle(b1_rule, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the recording pipeline ---
        self.next_band(2)
        b2_title = Tex("The recording pipeline").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Journal: book of first entry, daily").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("Ledger: one account per item").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = Tex("Trial balance: total Dr $=$ total Cr").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex(r"Trading account $\Rightarrow$ gross profit").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = Tex(r"Profit and Loss $\Rightarrow$ net profit $\Rightarrow$ Capital").scale(0.95).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(1.5)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): trade vs cash discount ---
        self.next_band(3)
        b3_title = Tex("Trade discount vs cash discount").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Trade: price reduced AT the sale --").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("never recorded; the low price IS the price").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Cash: prompt-payment reward, AFTER --").scale(1.05).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex("discount allowed: an expense").scale(1.05).shift(band_shift(3) + DOWN * 1.4)
        b3_l5 = Tex("discount received: an income").scale(1.05).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex("Test: reduced before, or settled after?").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): financial vs managerial ---
        self.next_band(4)
        b4_title = Tex("Financial vs managerial accounting").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_div = Line(UP * 1.6, DOWN * 2.0).shift(band_shift(4))
        self.play(Create(b4_div))
        b4_f0 = Tex("Financial").scale(1.1).shift(band_shift(4) + UP * 1.2 + LEFT * 2.6)
        b4_m0 = Tex("Managerial").scale(1.1).shift(band_shift(4) + UP * 1.2 + RIGHT * 2.6)
        self.play(Write(b4_f0))
        self.play(Write(b4_m0))
        self.wait(2)
        b4_f1 = Tex("for OUTSIDERS").scale(1.0).shift(band_shift(4) + UP * 0.4 + LEFT * 2.6)
        b4_m1 = Tex("for INSIDERS").scale(1.0).shift(band_shift(4) + UP * 0.4 + RIGHT * 2.6)
        self.play(Write(b4_f1))
        self.play(Write(b4_m1))
        self.wait(1.5)
        b4_f2 = Tex("reports the PAST").scale(1.0).shift(band_shift(4) + DOWN * 0.4 + LEFT * 2.6)
        b4_m2 = Tex("looks FORWARD").scale(1.0).shift(band_shift(4) + DOWN * 0.4 + RIGHT * 2.6)
        self.play(Write(b4_f2))
        self.play(Write(b4_m2))
        self.wait(1.5)
        b4_f3 = Tex("follows GAAP").scale(1.0).shift(band_shift(4) + DOWN * 1.2 + LEFT * 2.6)
        b4_m3 = Tex("no external rules").scale(1.0).shift(band_shift(4) + DOWN * 1.2 + RIGHT * 2.6)
        self.play(Write(b4_f3))
        self.play(Write(b4_m3))
        self.wait(2)
        b4_rule = Tex("Same figures -- different audience and rules").scale(1.0).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_rule))
        self.play(Create(SurroundingRectangle(b4_rule, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): perpetual system, the double record ---
        self.next_band(5)
        b5_title = Tex("The perpetual inventory system").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Trading Stock updated at EVERY transaction").scale(1.0).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_l1))
        self.wait(2)
        b5_l2 = Tex("Buy: Trading Stock increases, at COST").scale(1.05).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Sell: record TWO things at once --").scale(1.05).shift(band_shift(5) + DOWN * 0.7)
        b5_l4 = Tex("1) the sale, at selling price").scale(1.05).shift(band_shift(5) + DOWN * 1.5)
        b5_l5 = Tex("2) Cost of Sales out of Trading Stock").scale(1.05).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l3))
        self.wait(1.5)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("Every sale writes two truths").scale(1.05).shift(band_shift(5) + DOWN * 3.1)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): stocktake checks, not discovers ---
        self.next_band(6)
        b6_title = Tex("Stocktake: check, not discover").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Account says what SHOULD be on the shelf").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("Account: R48 000 \\quad Count: R46 500").scale(1.1).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = MathTex(r"\text{Gap} = \text{R48 000} - \text{R46 500} = \text{R1 500}").scale(1.0).shift(band_shift(6) + DOWN * 0.8)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2.5)
        b6_l4 = Tex("A question with a name: theft? error?").scale(1.05).shift(band_shift(6) + DOWN * 1.8)
        b6_l5 = Tex("Periodic system: the loss hides as sold").scale(1.0).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l4))
        self.wait(2)
        self.play(Write(b6_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): Zanele's shop, every word ---
        self.next_band(7)
        b7_title = Tex("One shop, every word").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Zanele, alone, her own savings: sole trader").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("R60 000 in: capital -- her owner's equity").scale(1.0).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex("Shelves and card machine: assets").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("Uncle's loan of R20 000: a liability").scale(1.05).shift(band_shift(7) + DOWN * 1.6)
        b7_l5 = Tex("Shoes to resell: trading stock, at cost").scale(1.05).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(1.5)
        self.play(Write(b7_l4))
        self.wait(1.5)
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex("Notebook daily = journal; pages = ledger").scale(1.0).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_6): report card and game plan ---
        self.next_band(8)
        b8_title = Tex("The report card and the game plan").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Bank asks about LAST year $\Rightarrow$ report card").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("financial: backward, by the rules, outside").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"Sneakers next winter? $\Rightarrow$ game plan").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        b8_l4 = Tex("managerial: forward, free form, inside").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Past-future, outsiders-insiders,").scale(1.05).shift(band_shift(8) + DOWN * 2.3)
        b8_l6 = Tex("rules-freedom: four pairs, one contrast").scale(1.05).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(VGroup(b8_l5, b8_l6), color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): the fridge that counts ---
        self.next_band(9)
        b9_title = Tex("The fridge that counts").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("A counter on the door: every bottle").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("in and out is counted").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Sale: customer pays R500 (the sale)").scale(1.05).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = Tex("R300 leaves the counter: cost of sales").scale(1.05).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = MathTex(r"\text{Gross profit} = \text{R500} - \text{R300} = \text{R200}").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(2.5)
        b9_l6 = Tex("Counter R48 000, count R46 500: R1 500").scale(1.0).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l6))
        self.wait(4)
