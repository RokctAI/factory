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

# Band-layout whiteboard scene for "Perpetual and Periodic Inventory Systems"
# (grade 11, term 3, inventory systems). One band per teaching beat; the
# camera moves down and nothing is removed. Part 1 (Expert) = subtopics 1-4,
# Part 2 (Simplifier) = subtopics 5-7 in fresh bands. Exporter-safe
# primitives only; write-only reveals. Subtopic durations
# 210/240/220/230/190/200/200 of 1490 s guide the apportioning.

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
        # --- Band 0 (subtopic_1): the perpetual system ---
        title = Tex("Perpetual and Periodic Inventory Systems").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("PERPETUAL: Trading Stock always current").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Purchase: debit Trading Stock").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Sale: TWO entries —").scale(1.05).shift(DOWN * 0.4)
        b0_l4 = Tex("selling price to Sales, AND").scale(1.05).shift(DOWN * 1.2)
        b0_l5 = Tex("cost out of Trading Stock to Cost of Sales").scale(1.0).shift(DOWN * 2.0)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(2)
        b0_l6 = Tex("Count tests the account: deficit or surplus").scale(1.0).shift(DOWN * 2.9)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): the periodic system ---
        self.next_band(1)
        b1_t = Tex("PERIODIC: no running stock record").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Purchases account (expense), not stock").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("Sale: selling price only — no cost entry").scale(1.05).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex("Trading Stock sleeps at opening balance").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex("Year end: COUNT, then compute by formula").scale(1.05).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Perpetual: cost at every movement").scale(1.0).shift(band_shift(1) + DOWN * 2.2)
        b1_l6 = Tex("Periodic: purchases, then reckon backwards").scale(1.0).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): perpetual — cost of sales from mark-up ---
        self.next_band(2)
        b2_t = Tex("Perpetual: derive it from the mark-up").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Mark-up 50\\% on cost, sales R450 000").scale(1.05).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("Sales $=$ 150\\% of cost").scale(1.05).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = MathTex(r"\text{Cost of sales} = 450\,000 \times \tfrac{100}{150}").scale(1.05).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("$=$ R300 000; gross profit R150 000").scale(1.05).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)
        b2_l5 = Tex("Read the base: mark-up on COST or").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        b2_l6 = Tex("on SELLING price — the reading is the mark").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): the periodic formula, line by line ---
        self.next_band(3)
        b3_t = Tex("The periodic formula").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex("Opening stock \\quad R80 000").scale(1.0).shift(band_shift(3) + UP * 1.3)
        b3_l2 = Tex("$+$ Purchases \\quad R520 000").scale(1.0).shift(band_shift(3) + UP * 0.6)
        b3_l3 = Tex("$+$ Carriage on purchases \\quad R18 000").scale(1.0).shift(band_shift(3) + DOWN * 0.1)
        b3_l4 = Tex("$-$ Purchases returns \\quad R12 000").scale(1.0).shift(band_shift(3) + DOWN * 0.8)
        b3_l5 = Tex("$-$ Drawings of stock \\quad R6 000").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        b3_l6 = Tex("$=$ Available for sale \\quad R600 000").scale(1.05).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l1))
        self.wait(1.5)
        self.play(Write(b3_l2))
        self.wait(1.5)
        self.play(Write(b3_l3))
        self.wait(1.5)
        self.play(Write(b3_l4))
        self.wait(1.5)
        self.play(Write(b3_l5))
        self.wait(1.5)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(2)
        b3_trap = Tex("Carriage outward in the formula?").scale(1.0).shift(band_shift(3) + DOWN * 3.2)
        self.play(Write(b3_trap))
        self.play(Create(strike(b3_trap)))
        self.wait(2.5)

        # --- Band 4 (subtopic_2): cost of sales, gross profit, hidden flaw ---
        self.next_band(4)
        b4_t = Tex("Less the count, out comes cost of sales").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("R600 000 $-$ closing stock R95 000").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("$=$ Cost of sales R505 000").scale(1.1).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = Tex("Sales R700 000 $-$ R505 000").scale(1.05).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex("$=$ Gross profit R195 000 (38,6\\% on cost)").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("The silent flaw: stolen or broken stock").scale(1.0).shift(band_shift(4) + DOWN * 2.4)
        b4_l6 = Tex("hides INSIDE the R505 000 — no deficit").scale(1.0).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): advantages and disadvantages ---
        self.next_band(5)
        b5_t = Tex("What each buys, what each costs").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_t))
        rail = Line(UP * 1.9, DOWN * 2.6).shift(band_shift(5))
        head_l = Tex("Perpetual").scale(1.0).shift(band_shift(5) + UP * 1.5 + LEFT * 2.9)
        head_r = Tex("Periodic").scale(1.0).shift(band_shift(5) + UP * 1.5 + RIGHT * 2.9)
        self.play(Create(rail), Write(head_l), Write(head_r))
        self.wait(2)
        p1 = Tex("stock known\\\\at any moment").scale(0.85).shift(band_shift(5) + UP * 0.6 + LEFT * 2.9)
        p2 = Tex("losses named\\\\as a deficit").scale(0.85).shift(band_shift(5) + DOWN * 0.4 + LEFT * 2.9)
        p3 = Tex("but admin-heavy\\\\per movement").scale(0.85).shift(band_shift(5) + DOWN * 1.4 + LEFT * 2.9)
        q1 = Tex("simple and cheap\\\\to run").scale(0.85).shift(band_shift(5) + UP * 0.6 + RIGHT * 2.9)
        q2 = Tex("no figure\\\\between counts").scale(0.85).shift(band_shift(5) + DOWN * 0.4 + RIGHT * 2.9)
        q3 = Tex("NO CONTROL:\\\\losses invisible").scale(0.85).shift(band_shift(5) + DOWN * 1.4 + RIGHT * 2.9)
        self.play(Write(p1))
        self.play(Write(q1))
        self.wait(2)
        self.play(Write(p2))
        self.play(Write(q2))
        self.wait(2)
        self.play(Write(p3))
        self.play(Write(q3))
        self.wait(3)

        # --- Band 6 (subtopic_3): the choice, and the technology point ---
        self.next_band(6)
        b6_t = Tex("Which system? Follow the goods").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Vehicles, jewellery: perpetual —").scale(1.05).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("high value, high cost of losing").scale(1.05).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Many cheap lines: periodic — once").scale(1.05).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Point-of-sale scanners post the cost").scale(1.05).shift(band_shift(6) + DOWN * 1.4)
        b6_l5 = Tex("automatically: perpetual for supermarkets").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): stock controls by category ---
        self.next_band(7)
        b7_t = Tex("Controls, named by category").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Physical: locked store, named person,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("check deliveries, separate duties").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Documents: pre-numbered orders and").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("invoices — a missing number is a question").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Counting: independent stocktakes,").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        b7_l6 = Tex("every difference investigated").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_4): the manipulation, traced ---
        self.next_band(8)
        b8_t = Tex("The pen-stroke fraud").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_trap = Tex("Overstate closing stock: harmless?").scale(1.05).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_trap))
        self.play(Create(strike(b8_trap)))
        self.wait(2)
        b8_l1 = Tex("Closing stock UP $\\Rightarrow$ cost of sales DOWN").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l2 = Tex("$\\Rightarrow$ gross and net profit UP — a lie").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        b8_l3 = Tex("that shifts the loss into next year").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Audit: re-count a sample; trace documents;").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        b8_l5 = Tex("compare achieved GP\\% with policy mark-up").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the notebook or the count ---
        self.next_band(9)
        b9_t = Tex("Two spaza owners, one street").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Owner 1, the notebook: loaf sold for R18,").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("AND a R13 loaf left the shelf — written").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("She knows her shelf at any hour").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("Owner 2, the count: writes what he buys,").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        b9_l5 = Tex("counts at year end, works it backwards").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex("His sum ASSUMES the missing was sold").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_6): working it out backwards ---
        self.next_band(10)
        b10_t = Tex("The year-end sum, in order").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Started with R80 000 $+$ bought R520 000").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("$+$ delivery TO him R18 000").scale(1.0).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex("$-$ returns R12 000 $-$ taken home R6 000").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex("$=$ pile of R600 000 to sell").scale(1.05).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(1.5)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Counted R95 000 left: R505 000 went out").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(2)
        b10_l6 = Tex("The stolen cooldrink is in there too —").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        b10_l7 = Tex("the sum calls theft a sale").scale(1.0).shift(band_shift(10) + DOWN * 3.5)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(3)

        # --- Band 11 (subtopic_7): which one should the shop use? ---
        self.next_band(11)
        b11_t = Tex("Which one should the shop use?").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("Few, expensive things: notebook").scale(1.05).shift(band_shift(11) + UP * 1.2)
        b11_l2 = Tex("Thousands of cheap things: count — once").scale(1.0).shift(band_shift(11) + UP * 0.4)
        self.play(Write(b11_l1))
        self.wait(2)
        self.play(Write(b11_l2))
        self.wait(2)
        b11_l3 = Tex("The scanner writes the notebook itself:").scale(1.0).shift(band_shift(11) + DOWN * 0.5)
        b11_l4 = Tex("today the question is what the till can do").scale(1.0).shift(band_shift(11) + DOWN * 1.2)
        self.play(Write(b11_l3))
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(2.5)
        b11_trap = Tex("Pad the count, profit looks better?").scale(1.0).shift(band_shift(11) + DOWN * 2.1)
        self.play(Write(b11_trap))
        self.play(Create(strike(b11_trap)))
        b11_l5 = Tex("Shelves stay empty; the loss lands next year").scale(0.95).shift(band_shift(11) + DOWN * 2.9)
        b11_l6 = Tex("— so independent people do the counting").scale(0.95).shift(band_shift(11) + DOWN * 3.6)
        self.play(Write(b11_l5))
        self.play(Write(b11_l6))
        self.wait(4)
