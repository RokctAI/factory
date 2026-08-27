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

# Band-layout whiteboard scene for "Perpetual and Periodic Inventory
# Systems" (grade 11, term 3, inventory systems). One band per teaching
# beat; camera moves down, nothing removed. Part 1 (Expert) = subtopics
# 1-4, Part 2 (Simplifier) = subtopics 5-7. Exporter-safe primitives only;
# write-only reveals. Subtopic durations 210/240/220/230/190/200/200 of
# 1490 s guide the apportioning.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InventorySystemsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): two systems, two philosophies ---
        title = Tex("Perpetual and Periodic Inventory Systems").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Perpetual: cost recorded at EVERY").scale(1.0).shift(UP * 1.1)
        b0_l2 = Tex("movement — the account always knows").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Periodic: record PURCHASES, count at").scale(1.0).shift(DOWN * 0.5)
        b0_l4 = Tex("period end, reason cost of sales backwards").scale(1.0).shift(DOWN * 1.2)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("Trading Stock: live claim vs untouched all year").scale(0.95).shift(DOWN * 2.1)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the entries at a sale ---
        self.next_band(1)
        b1_t = Tex("What one credit sale triggers").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Perpetual: Debtors and Sales at selling").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("price AND Trading Stock to Cost of Sales").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Periodic: selling price only —").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("no cost entry accompanies the sale").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("Between counts, nobody knows the stock").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): mark-up in the perpetual system ---
        self.next_band(2)
        b2_t = Tex("Cost of sales from the mark-up").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex(r"Mark-up 60\% ON COST, sales R480 000").scale(1.0).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"Sales $=$ 160\% of cost, so cost of sales").scale(1.0).shift(band_shift(2) + UP * 0.3)
        b2_l3 = Tex(r"$=$ 480 000 $\times$ 100/160 $=$ R300 000").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l2))
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Gross profit R180 000").scale(1.0).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Read the BASE: on cost or on selling price").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): the periodic formula, line by line ---
        self.next_band(3)
        b3_t = Tex("The periodic formula").scale(1.15).shift(band_shift(3) + UP * 2.3)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Opening stock \\quad R70 000").scale(0.95).shift(band_shift(3) + UP * 1.4)
        b3_l2 = Tex("$+$ Purchases \\quad R480 000").scale(0.95).shift(band_shift(3) + UP * 0.7)
        b3_l3 = Tex("$+$ Carriage on purchases \\quad R15 000").scale(0.95).shift(band_shift(3) + UP * 0.0)
        b3_l4 = Tex("$-$ Returns R10 000; $-$ drawings R5 000").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        b3_l5 = Tex("$=$ Available for sale \\quad R550 000").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        b3_l6 = Tex("$-$ Closing stock (counted) \\quad R88 000").scale(0.95).shift(band_shift(3) + DOWN * 2.1)
        b3_l7 = Tex("Cost of sales: R462 000").scale(1.05).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2)
        self.play(Write(b3_l6))
        self.play(Write(b3_l7))
        self.play(Create(SurroundingRectangle(b3_l7, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_2): gross profit and the silent flaw ---
        self.next_band(4)
        b4_t = Tex("Gross profit, and the silent flaw").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Sales R660 000 $-$ R462 000").scale(1.0).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex(r"$=$ R198 000 — about 42,9\% on cost").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_wrong = Tex("Everything not counted was sold?").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l3 = Tex("Theft and breakage hide INSIDE cost").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        b4_l4 = Tex("of sales — no deficit is ever named").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): advantages, disadvantages, the choice ---
        self.next_band(5)
        b5_t = Tex("The choice between the systems").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("Perpetual: always knows, catches losses;").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("but a cost record for every movement").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Periodic: simple and cheap; but blind").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("between counts, and NO control").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("High-value goods: perpetual, always;").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        b5_l6 = Tex("barcode tills made it practical for all").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): controls, ethics, audit ---
        self.next_band(6)
        b6_t = Tex("Protecting the stock itself").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Locked store, checked deliveries,").scale(0.95).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("pre-numbered documents, separated duties").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Counts by people independent of the store").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Overstate closing stock: cost of sales").scale(0.95).shift(band_shift(6) + DOWN * 1.4)
        b6_l5 = Tex("falls, profit RISES — a pen-stroke lie").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(2.5)
        b6_l6 = Tex("Audit: re-count samples, trace documents,").scale(0.9).shift(band_shift(6) + DOWN * 3.0)
        b6_l7 = Tex("compare achieved mark-up with policy").scale(0.9).shift(band_shift(6) + DOWN * 3.7)
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the notebook or the count ---
        self.next_band(7)
        b7_t = Tex("The notebook or the count").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Owner one: every cooldrink out, she writes").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("the R25 taken AND the R18 that left the shelf").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Owner two: writes what he buys, counts").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("at year end, works it out backwards").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("His sum assumes: not on the shelf $=$ SOLD").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3.5)

        # --- Band 8 (subtopic_6): working it out backwards ---
        self.next_band(8)
        b8_t = Tex("The year-end sum, in order").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Started with 70 000 $+$ bought 480 000").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("$+$ transport in 15 000 $-$ returns 10 000").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex("$-$ taken home 5 000 $=$ pile of 550 000").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Count the shelves: 88 000 still standing").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex("So out the door: R462 000 cost of sales").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2.5)
        b8_l6 = Tex("Sales 660 000: gross profit R198 000 —").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        b8_l7 = Tex("with the stolen case hiding inside the cost").scale(0.95).shift(band_shift(8) + DOWN * 3.6)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3.5)

        # --- Band 9 (subtopic_7): which one should the shop use? ---
        self.next_band(9)
        b9_t = Tex("Which one should the shop use?").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Few, expensive things: notebook, always").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Thousands of cheap things: counting was").scale(0.95).shift(band_shift(9) + UP * 0.3)
        b9_l3 = Tex("good enough — until the barcode scanner").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("The till now writes the notebook itself").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Padded closing count: smaller cost of").scale(0.95).shift(band_shift(9) + DOWN * 2.2)
        b9_l6 = Tex("sales, fatter paper profit, same empty shelves").scale(0.9).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(2.5)
        b9_l7 = Tex("So counters are independent, and verified").scale(0.95).shift(band_shift(9) + DOWN * 3.7)
        self.play(Write(b9_l7))
        self.wait(4)
