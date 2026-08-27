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

# Band-layout whiteboard scene for the accounting-cycle session duo.
# Exporter-safe primitives only (Tex/MathTex/Line/Arrow/Rectangle/VGroup);
# write-only reveals. Band time follows subtopics.json
# (180/180/180/240/170/180/160 of 1290 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AccountingCycleSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(13)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): why the cycle exists ---
        title = Tex("The Accounting Cycle").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l01 = Tex("A shoebox of slips cannot answer:").scale(1.05).shift(UP * 1.0)
        l02 = Tex("Did I make a profit?").scale(1.1).shift(UP * 0.1)
        l03 = Tex("What is my business worth?").scale(1.1).shift(DOWN * 0.8)
        self.play(Write(l01)); self.wait(2)
        self.play(Write(l02)); self.wait(1.5)
        self.play(Write(l03)); self.wait(2)
        l04 = Tex("The cycle: the fixed route every transaction").scale(0.95).shift(DOWN * 1.9)
        l05 = Tex("travels — repeated every period").scale(1.0).shift(DOWN * 2.7)
        self.play(Write(l04)); self.play(Write(l05))
        self.wait(3)

        # --- Band 1 (subtopic_1): the six stages, in order ---
        self.next_band(1)
        b1_t = Tex("Six stages, fixed order").scale(1.2).shift(band_shift(1) + UP * 2.7)
        self.play(Write(b1_t)); self.wait(1.5)
        stages = [
            "1. Source documents",
            "2. Journals",
            "3. Posting to the ledger",
            "4. Trial balance",
            "5. Final accounts",
            "6. Financial statements",
        ]
        ys = [1.8, 0.9, 0.0, -0.9, -1.8, -2.7]
        prev = None
        for s, y in zip(stages, ys):
            item = Tex(s).scale(0.95).move_to([0, y, 0]).shift(band_shift(1))
            if prev is not None:
                a = Arrow([0, y + 0.62, 0], [0, y + 0.28, 0], buff=0,
                          stroke_width=4).shift(band_shift(1))
                self.play(Create(a), run_time=0.4)
            self.play(Write(item))
            self.wait(1.2)
            prev = item
        b1_l1 = Tex("Each stage needs the one before it").scale(0.95).move_to([4.2, -0.4, 0]).shift(band_shift(1))
        self.play(Write(b1_l1))
        self.wait(3)

        # --- Band 2 (subtopic_2): stages one and two ---
        self.next_band(2)
        b2_t = Tex("Stage 1: evidence; Stage 2: sorting").scale(1.15).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_t)); self.wait(2)
        b2_l1 = Tex("Cash sale $\\rightarrow$ till slip; EFT $\\rightarrow$ proof;").scale(1.0).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("credit purchase $\\rightarrow$ invoice").scale(1.0).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1)); self.play(Write(b2_l2)); self.wait(2.5)
        b2_l3 = Tex("No source document, no entry").scale(1.05).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex("Journals sort by type: CRJ in, CPJ out,").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        b2_l5 = Tex("petty cash small — 80 sales, ONE total").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l4)); self.wait(2)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_3): stages three and four ---
        self.next_band(3)
        b3_t = Tex("Stage 3: the ledger; Stage 4: the check").scale(1.1).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_t)); self.wait(2)
        b3_l1 = Tex("Journals by DATE; ledger by ACCOUNT").scale(1.05).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_l1)); self.wait(2)
        b3_l2 = Tex("CRJ bank total $\\rightarrow$ debit Bank;").scale(1.0).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("sales total $\\rightarrow$ credit Sales; then balance").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l2)); self.play(Write(b3_l3)); self.wait(2.5)
        b3_l4 = Tex("Trial balance: debits column = credits column").scale(1.0).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l4)); self.wait(2)
        b3_wrong = Tex("It balances, so the books are perfect").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        b3_l5 = Tex("It checks arithmetic equality only").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_4): stage five — final accounts ---
        self.next_band(4)
        b4_t = Tex("Stage 5: profit worked out in the ledger").scale(1.1).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_t)); self.wait(2)
        b4_l1 = Tex("Trading account: Sales $-$ Cost of Sales").scale(1.05).shift(band_shift(4) + UP * 1.3)
        b4_l2 = Tex("= GROSS PROFIT").scale(1.1).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1)); self.wait(2)
        self.play(Write(b4_l2)); self.wait(2)
        b4_l3 = Tex("Profit and Loss account: gross profit").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("+ other incomes $-$ expenses = NET PROFIT").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l3)); self.play(Write(b4_l4)); self.wait(2.5)
        b4_l5 = Tex("Net profit $\\rightarrow$ Capital: it belongs to the owner").scale(1.0).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): stage six + the whole route in one breath ---
        self.next_band(5)
        b5_t = Tex("Stage 6: the financial statements").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_t)); self.wait(2)
        b5_l1 = Tex("Comprehensive Income: profit for the period").scale(1.0).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Financial Position: assets, equity, liabilities").scale(1.0).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1)); self.wait(2)
        self.play(Write(b5_l2)); self.wait(2)
        b5_l3 = Tex("One breath: slip $\\rightarrow$ CRJ $\\rightarrow$ ledger $\\rightarrow$").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("trial balance $\\rightarrow$ final accounts $\\rightarrow$ statements").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3)); self.play(Write(b5_l4)); self.wait(2.5)
        b5_l5 = Tex("Test: what does each stage receive and pass on?").scale(0.95).shift(band_shift(5) + DOWN * 2.3)
        self.play(Write(b5_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 6 (subtopic_5): the taxi route ---
        self.next_band(6)
        b6_t = Tex("The taxi route through the books").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_t)); self.wait(2)
        b6_l1 = Tex("1. Ticket — the source document").scale(1.0).shift(band_shift(6) + UP * 1.4)
        b6_l2 = Tex("2. Rank — the journals, queuing by type").scale(1.0).shift(band_shift(6) + UP * 0.6)
        b6_l3 = Tex("3. Home — each amount to its account").scale(1.0).shift(band_shift(6) + DOWN * 0.2)
        b6_l4 = Tex("4. Roll call — the trial balance counts all").scale(1.0).shift(band_shift(6) + DOWN * 1.0)
        b6_l5 = Tex("5. Weigh-up — the profit steps out").scale(1.0).shift(band_shift(6) + DOWN * 1.8)
        b6_l6 = Tex("6. Front page — the statements").scale(1.0).shift(band_shift(6) + DOWN * 2.6)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4, b6_l5, b6_l6):
            self.play(Write(m))
            self.wait(1.6)
        self.wait(2)

        # --- Band 7 (subtopic_6): one slip rides the whole route ---
        self.next_band(7)
        b7_t = Tex("One slip rides the whole route").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_t)); self.wait(2)
        b7_l1 = Tex("Monday: school shoes, R150 cash — slip printed").scale(0.95).shift(band_shift(7) + UP * 1.3)
        self.play(Write(b7_l1)); self.wait(2)
        b7_l2 = Tex("Evening: one line in the CRJ queue").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l2)); self.wait(2)
        b7_l3 = Tex("Month end: travels as one total —").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("into Bank AND into Sales: double entry").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l3)); self.play(Write(b7_l4)); self.wait(2.5)
        b7_l5 = Tex("Roll call balances; year end: Trading account;").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        b7_l6 = Tex("front page: part of the profit story").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5)); self.wait(2)
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_7): the three clocks ---
        self.next_band(8)
        b8_t = Tex("The three clocks on the wall").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_t)); self.wait(2)
        b8_l1 = Tex("FAST, daily: tickets written, queues entered").scale(1.0).shift(band_shift(8) + UP * 1.3)
        self.play(Write(b8_l1)); self.wait(2)
        b8_l2 = Tex("MIDDLE, monthly: post the totals, roll call").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2)); self.wait(2)
        b8_l3 = Tex("SLOW, yearly: weigh-up and front page").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l3)); self.wait(2)
        b8_l4 = Tex("Daily record, monthly check, yearly answer").scale(1.05).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(2.5)
        b8_l5 = Tex("Then July's first slip starts the cycle again").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.wait(4)
