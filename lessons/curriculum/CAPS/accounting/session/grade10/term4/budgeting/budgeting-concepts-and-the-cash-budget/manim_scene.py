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

# Band-layout whiteboard scene for the CAPS Grade 10 Accounting session duo
# "Budgeting Concepts and the Cash Budget". Add-only lifecycle, one band per
# teaching beat, camera moves down between bands. Covers all seven subtopics:
# Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7) in fresh
# bands. subtopics.json durations 220/220/220/220/180/190/190 of 1440 s.
# The quarter's cash budget is built as a month-column grid (Rectangle +
# Lines + Tex), figures posted in script order, balances rolled last.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CashBudgetSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): report vs estimate; variance is the control
        title = Tex("Budgeting and the Cash Budget").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("A statement REPORTS — after the fact, verifiable").scale(1.0).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex("A budget ESTIMATES — before the fact, targets").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("They meet at year end: actual beside budgeted").scale(1.0).shift(DOWN * 0.6)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Every VARIANCE demands an explanation").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = Tex("The budget is the plan; comparison is the control").scale(0.95).shift(DOWN * 2.6)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the family of budgets; zero-based
        self.next_band(1)
        b1_title = Tex("The family of budgets").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("Cash budget: month by month — can we pay?").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Capital budget: long-term assets, planned apart").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Medium-term: 1 to 3 years; long-term: beyond").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_wrong = Tex("Copy last year's budget, add a percentage").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l4 = Tex("Zero-based: every line starts at NOTHING").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        b1_l5 = Tex("and must justify its whole amount afresh").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): receipts, with the collection lag
        self.next_band(2)
        b2_title = Tex("Receipts — money when it ARRIVES").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("Sales R20 000 a month: 60\\% cash,").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("40\\% on credit, collected the FOLLOWING month").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Cash sales: } 60\% \times 20\,000 = 12\,000").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"\text{December's credit: } 40\% \times 20\,000 = 8\,000").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = MathTex(r"\text{Total in: R}20\,000").scale(1.05).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): payments, with the capital landing
        self.next_band(3)
        b3_title = Tex("Payments — every rand that leaves").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex("Stock purchases R12 000, paid in the month").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Wages R3 000; rent R1 500").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"12\,000 + 3\,000 + 1\,500 = 16\,500").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("February exception: sewing machine R6 000 —").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex("a capital item, landing in its purchase month").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_2): the survival arithmetic, as a quarter grid
        self.next_band(4)
        b4_title = Tex("The survival arithmetic").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        grid = Rectangle(width=11.4, height=4.2).shift(band_shift(4) + DOWN * 0.6)
        v1 = Line(UP * 2.1, DOWN * 2.1).shift(band_shift(4) + DOWN * 0.6 + LEFT * 1.9)
        v2 = Line(UP * 2.1, DOWN * 2.1).shift(band_shift(4) + DOWN * 0.6 + RIGHT * 1.9)
        self.play(Create(grid), Create(v1), Create(v2))
        h1 = Tex("Jan").scale(1.0).shift(band_shift(4) + UP * 1.0 + LEFT * 3.8)
        h2 = Tex("Feb").scale(1.0).shift(band_shift(4) + UP * 1.0)
        h3 = Tex("Mar").scale(1.0).shift(band_shift(4) + UP * 1.0 + RIGHT * 3.8)
        self.play(Write(h1), Write(h2), Write(h3))
        self.wait(2)
        j1 = Tex("+3 500").scale(0.95).shift(band_shift(4) + UP * 0.1 + LEFT * 3.8)
        j2 = Tex("open 2 000").scale(0.9).shift(band_shift(4) + DOWN * 0.8 + LEFT * 3.8)
        j3 = Tex("close 5 500").scale(0.9).shift(band_shift(4) + DOWN * 1.7 + LEFT * 3.8)
        self.play(Write(j1))
        self.wait(1.5)
        self.play(Write(j2), Write(j3))
        self.wait(2)
        f1 = Tex("$-$2 500").scale(0.95).shift(band_shift(4) + UP * 0.1)
        f2 = Tex("open 5 500").scale(0.9).shift(band_shift(4) + DOWN * 0.8)
        f3 = Tex("close 3 000").scale(0.9).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(f1))
        self.wait(1.5)
        self.play(Write(f2), Write(f3))
        self.wait(2)
        m1 = Tex("+3 500").scale(0.95).shift(band_shift(4) + UP * 0.1 + RIGHT * 3.8)
        m2 = Tex("open 3 000").scale(0.9).shift(band_shift(4) + DOWN * 0.8 + RIGHT * 3.8)
        m3 = Tex("close 6 500").scale(0.9).shift(band_shift(4) + DOWN * 1.7 + RIGHT * 3.8)
        self.play(Write(m1))
        self.wait(1.5)
        self.play(Write(m2), Write(m3))
        self.play(Create(SurroundingRectangle(m3, color=GREEN)))
        self.wait(2)
        b4_l1 = Tex("Each closing rolls into the next opening").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l1))
        self.wait(3)

        # --- Band 5 (subtopic_3): reading the quarter's decisions
        self.next_band(5)
        b5_title = Tex("The decisions inside the budget").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("February dips to R3 000 — BY DESIGN:").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("big purchases go where balances can carry them").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("If negative: delay a month, or arrange the").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("overdraft IN ADVANCE — banks price desperation").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("The 40\\% lag: profit and cash keep").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        b5_l6 = Tex("different calendars; variances = early warnings").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the wider family, placed with meaning
        self.next_band(6)
        b6_title = Tex("The wider family, placed").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Capital budget: each asset with amount,").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("timing and funding — growth by plan").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Medium-term: expansion, staffing, 1 to 3 years").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Long-term: premises, a second branch").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Zero-based where habit renews expenses:").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        b6_l6 = Tex("justify from zero, or cut").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): exam technique and the cash-only traps
        self.next_band(7)
        b7_title = Tex("Technique — the cash-only rule").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_wrong = Tex("Depreciation as a line in the cash budget").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_l1 = Tex("No rand leaves — depreciation NEVER enters").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = Tex("Credit sales enter at COLLECTION, not sale").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Keep the order: receipts, payments, surplus,").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        b7_l4 = Tex("opening, closing — and label every estimate").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the month written before it happens
        self.next_band(8)
        b8_title = Tex("The month written before it happens").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Before the salary lands: money in, money out,").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("and the only subtraction that matters").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("A report is a mirror; a budget is a headlamp").scale(1.05).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("Unwritten plans cannot be checked — the page").scale(0.95).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = Tex("turns vanished money into findable answers").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the purse through three months
        self.next_band(9)
        b9_title = Tex("Watching the purse through three months").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Jan: in 20 000, out 16 500 — purse to R5 500").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Feb: the planned shock — machine R6 000;").scale(1.0).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex("purse gives back 2 500, closes at R3 000").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Thabo KNEW it would be thin; the cousin,").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        b9_l5 = Tex("buying on feeling, finds the rent bouncing").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex("Mar: purse recovers to R6 500").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): zero-based — every rand re-applies
        self.next_band(10)
        b10_title = Tex("Every rand re-applies for its job").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Copied budgets carry their dead forever:").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("the unused subscription, the outgrown bundle").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Start from nothing: why does this line exist?").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("What does it buy NOW? What breaks without it?").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("Spring-cleaning for money — it pays in").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        b10_l6 = Tex("found rands every time it is honestly done").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(4)
