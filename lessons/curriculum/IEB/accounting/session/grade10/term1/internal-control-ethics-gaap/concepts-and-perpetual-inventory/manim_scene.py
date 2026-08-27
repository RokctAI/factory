# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
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

# Band-layout whiteboard scene for the concepts / perpetual-inventory session
# duo. Exporter-safe primitives only (Tex/MathTex/Line/Arrow/Rectangle/
# VGroup); write-only reveals. Band time follows subtopics.json
# (180/190/170/200/180/160/180 of 1260 s).

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
        self.wait(13)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the sole trader and the entity rule ---
        title = Tex("Concepts and Perpetual Inventory").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("Sole trader: one owner, own right").scale(1.0).shift(UP * 1.1)
        self.play(Write(l01)); self.wait(2)
        l02 = Tex("In LAW: owner and business are one —").scale(0.95).shift(UP * 0.2)
        l03 = Tex("personally liable for its debts").scale(0.95).shift(DOWN * 0.6)
        self.play(Write(l02)); self.play(Write(l03)); self.wait(2.5)
        l04 = Tex("In the RECORDS: separate — the entity rule").scale(0.95).shift(DOWN * 1.6)
        self.play(Write(l04))
        self.play(Create(SurroundingRectangle(l04, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the elements on a T layout ---
        self.next_band(1)
        b1_t = Tex("The elements, and their sides").scale(1.15).shift(band_shift(1) + UP * 2.5)
        self.play(Write(b1_t)); self.wait(2)
        b1_l1 = Tex("Assets: possessions and rights of value").scale(0.9).shift(band_shift(1) + UP * 1.4)
        b1_l2 = Tex("Liabilities: owed to outsiders").scale(0.9).shift(band_shift(1) + UP * 0.6)
        b1_l3 = Tex("Equity: the owner's running stake").scale(0.9).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l1)); self.wait(1.8)
        self.play(Write(b1_l2)); self.wait(1.8)
        self.play(Write(b1_l3)); self.wait(2)
        b1_l4 = Tex("Debit: assets and expenses grow left").scale(0.9).shift(band_shift(1) + DOWN * 1.1)
        b1_l5 = Tex("Credit: liabilities, equity, income grow right").scale(0.85).shift(band_shift(1) + DOWN * 1.9)
        self.play(Write(b1_l4)); self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the recording pipeline ---
        self.next_band(2)
        b2_t = Tex("The pipeline").scale(1.2).shift(band_shift(2) + UP * 2.5)
        self.play(Write(b2_t)); self.wait(2)
        steps = ["Journal — first entry, daily",
                 "Ledger — one account per item",
                 "Trial balance — debits = credits",
                 "Final accounts — gross, then net profit"]
        ys = [1.5, 0.6, -0.3, -1.2]
        prev = None
        for s, y in zip(steps, ys):
            item = Tex(s).scale(0.85).move_to([0, y, 0]).shift(band_shift(2))
            if prev is not None:
                a = Arrow([0, y + 0.62, 0], [0, y + 0.28, 0], buff=0,
                          stroke_width=4).shift(band_shift(2))
                self.play(Create(a), run_time=0.4)
            self.play(Write(item))
            self.wait(1.5)
            prev = item
        b2_l1 = Tex("Profit: earned minus incurred").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l1))
        self.wait(3)

        # --- Band 3 (subtopic_2): trade vs cash discount ---
        self.next_band(3)
        b3_t = Tex("Two discounts, two treatments").scale(1.15).shift(band_shift(3) + UP * 2.5)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("Trade: price cut BEFORE recording —").scale(0.95).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("invisible; the reduced price IS the price").scale(0.9).shift(band_shift(3) + UP * 0.6)
        self.play(Write(b3_l1)); self.play(Write(b3_l2)); self.wait(2.5)
        b3_l3 = Tex("Cash: existing debt settled for less —").scale(0.95).shift(band_shift(3) + DOWN * 0.3)
        b3_l4 = Tex("recorded: allowed = expense; received = income").scale(0.85).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3)); self.play(Write(b3_l4)); self.wait(2.5)
        b3_l5 = Tex("The test: before, or after?").scale(1.0).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): financial vs managerial ---
        self.next_band(4)
        b4_t = Tex("Financial vs managerial").scale(1.15).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("Financial: outsiders, the past, GAAP,").scale(0.9).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("standardised statements").scale(0.9).shift(band_shift(4) + UP * 0.6)
        self.play(Write(b4_l1)); self.play(Write(b4_l2)); self.wait(2.5)
        b4_l3 = Tex("Managerial: insiders, the future,").scale(0.9).shift(band_shift(4) + DOWN * 0.3)
        b4_l4 = Tex("no rulebook — usefulness only").scale(0.9).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3)); self.play(Write(b4_l4)); self.wait(2.5)
        b4_l5 = Tex("Last year's profit? Financial.").scale(0.9).shift(band_shift(4) + DOWN * 2.0)
        b4_l6 = Tex("Second branch next year? Managerial.").scale(0.9).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l5)); self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): perpetual system, the double record ---
        self.next_band(5)
        b5_t = Tex("Perpetual: updated at EVERY transaction").scale(1.0).shift(band_shift(5) + UP * 2.5)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("Buy: Trading Stock up, at cost").scale(0.95).shift(band_shift(5) + UP * 1.4)
        self.play(Write(b5_l1)); self.wait(2)
        b5_l2 = Tex("Sell: TWO records at once —").scale(0.95).shift(band_shift(5) + UP * 0.5)
        b5_l3 = Tex("the sale at selling price,").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        b5_l4 = Tex("cost of sales out of Trading Stock").scale(0.95).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l2)); self.play(Write(b5_l3)); self.play(Write(b5_l4)); self.wait(2.5)
        b5_l5 = Tex("Gross profit visible per sale, immediately").scale(0.9).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): stocktake checks, not discovers ---
        self.next_band(6)
        b6_t = Tex("The stocktake: check, not discovery").scale(1.05).shift(band_shift(6) + UP * 2.5)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("Account says R52 000 should be on hand").scale(0.9).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("Count finds R50 200").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = Tex("R1 800 gap: theft, breakage or error —").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("a named question demanding an answer").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l3)); self.play(Write(b6_l4)); self.wait(2.5)
        b6_l5 = Tex("Periodic: the gap is assumed sold — invisible").scale(0.85).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): Sipho's shop, every word ---
        self.next_band(7)
        b7_t = Tex("One shop, every word").scale(1.2).shift(band_shift(7) + UP * 2.5)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("R70 000 in: capital; his stake: equity").scale(0.9).shift(band_shift(7) + UP * 1.4)
        b7_l2 = Tex("Shelves, card machine: assets").scale(0.9).shift(band_shift(7) + UP * 0.6)
        b7_l3 = Tex("R25 000 from his aunt: a liability").scale(0.9).shift(band_shift(7) + DOWN * 0.2)
        b7_l4 = Tex("Backpacks to resell: trading stock, at cost").scale(0.85).shift(band_shift(7) + DOWN * 1.0)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(1.7)
        b7_l5 = Tex("Notebook: journal; Sunday pages: ledger").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(b7_l5))
        self.wait(3)

        # --- Band 8 (subtopic_6): report card and game plan ---
        self.next_band(8)
        b8_t = Tex("Report card and game plan").scale(1.15).shift(band_shift(8) + UP * 2.5)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("Report card: last year, by the rules,").scale(0.9).shift(band_shift(8) + UP * 1.4)
        b8_l2 = Tex("for the bank — financial accounting").scale(0.9).shift(band_shift(8) + UP * 0.6)
        self.play(Write(b8_l1)); self.play(Write(b8_l2)); self.wait(2.5)
        b8_l3 = Tex("Game plan: next winter's stock, no rules,").scale(0.9).shift(band_shift(8) + DOWN * 0.3)
        b8_l4 = Tex("for the coach — managerial accounting").scale(0.9).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3)); self.play(Write(b8_l4)); self.wait(2.5)
        b8_l5 = Tex("Past-future; outsiders-insiders; rules-freedom").scale(0.85).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): the fridge that counts ---
        self.next_band(9)
        b9_t = Tex("The fridge that counts").scale(1.2).shift(band_shift(9) + UP * 2.5)
        self.play(Write(b9_t)); self.wait(2)
        b9_l1 = Tex("Every bag in, counted; every bag out, counted").scale(0.85).shift(band_shift(9) + UP * 1.4)
        self.play(Write(b9_l1)); self.wait(2)
        b9_l2 = Tex("Sale: R450 in; R270 off the counter").scale(0.9).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex("R180 gross profit — seen TODAY").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(b9_l2)); self.wait(2)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2)
        b9_l4 = Tex("December: counter 52 000, count 50 200 —").scale(0.85).shift(band_shift(9) + DOWN * 1.2)
        b9_l5 = Tex("R1 800 missing since June: find out why").scale(0.9).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4)); self.play(Write(b9_l5))
        self.wait(4)
