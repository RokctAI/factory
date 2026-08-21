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

# Band-layout whiteboard scene for the IEB Grade 10 Accounting session duo
# "Budgeting Concepts and the Cash Budget". Add-only lifecycle, one band per
# teaching beat, camera moves down between bands. Covers all seven subtopics:
# Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7) in fresh
# bands. subtopics.json durations 220/220/220/220/180/190/190 of 1440 s.
# The quarter's cash budget for Lerato's Woodcraft is built as a month-column
# grid (Rectangle + Lines + Tex), figures posted in script order, balances
# rolled last.

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
        b0_l1 = Tex("A statement REPORTS — after the events, provable").scale(1.0).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex("A budget ESTIMATES — before the events, targets").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("They meet later: actual beside budgeted").scale(1.0).shift(DOWN * 0.6)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Every VARIANCE must be explained").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = Tex("The budget is the plan; comparing is the control").scale(0.95).shift(DOWN * 2.6)
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
        b1_l2 = Tex("Capital budget: long-life assets, planned apart").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Medium-term: 1 to 3 years; long-term: beyond").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_wrong = Tex("Copy last year's budget, add a percentage").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l4 = Tex("Zero-based: every line begins at NOTHING").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        b1_l5 = Tex("and argues for its whole amount afresh").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): receipts, with the collection lag
        self.next_band(2)
        b2_title = Tex("Receipts — money when it ARRIVES").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("Sales R30 000 a month: 70\\% cash,").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("30\\% on credit, collected the FOLLOWING month").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Cash sales: } 70\% \times 30\,000 = 21\,000").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = MathTex(r"\text{September's credit: } 30\% \times 30\,000 = 9\,000").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = MathTex(r"\text{Total in: R}30\,000").scale(1.05).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l5))
        self.play(Create(SurroundingRectangle(b2_l5, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): payments, with the capital landing
        self.next_band(3)
        b3_title = Tex("Payments — every rand that leaves").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex("Timber and materials R18 000, paid in the month").scale(1.0).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex("Wages R4 500; rent R2 500").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"18\,000 + 4\,500 + 2\,500 = 25\,000").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("November exception: wood lathe R9 000 —").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
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
        h1 = Tex("Oct").scale(1.0).shift(band_shift(4) + UP * 1.0 + LEFT * 3.8)
        h2 = Tex("Nov").scale(1.0).shift(band_shift(4) + UP * 1.0)
        h3 = Tex("Dec").scale(1.0).shift(band_shift(4) + UP * 1.0 + RIGHT * 3.8)
        self.play(Write(h1), Write(h2), Write(h3))
        self.wait(2)
        o1 = Tex("+5 000").scale(0.95).shift(band_shift(4) + UP * 0.1 + LEFT * 3.8)
        o2 = Tex("open 3 000").scale(0.9).shift(band_shift(4) + DOWN * 0.8 + LEFT * 3.8)
        o3 = Tex("close 8 000").scale(0.9).shift(band_shift(4) + DOWN * 1.7 + LEFT * 3.8)
        self.play(Write(o1))
        self.wait(1.5)
        self.play(Write(o2), Write(o3))
        self.wait(2)
        n1 = Tex("$-$4 000").scale(0.95).shift(band_shift(4) + UP * 0.1)
        n2 = Tex("open 8 000").scale(0.9).shift(band_shift(4) + DOWN * 0.8)
        n3 = Tex("close 4 000").scale(0.9).shift(band_shift(4) + DOWN * 1.7)
        self.play(Write(n1))
        self.wait(1.5)
        self.play(Write(n2), Write(n3))
        self.wait(2)
        d1 = Tex("+5 000").scale(0.95).shift(band_shift(4) + UP * 0.1 + RIGHT * 3.8)
        d2 = Tex("open 4 000").scale(0.9).shift(band_shift(4) + DOWN * 0.8 + RIGHT * 3.8)
        d3 = Tex("close 9 000").scale(0.9).shift(band_shift(4) + DOWN * 1.7 + RIGHT * 3.8)
        self.play(Write(d1))
        self.wait(1.5)
        self.play(Write(d2), Write(d3))
        self.play(Create(SurroundingRectangle(d3, color=GREEN)))
        self.wait(2)
        b4_l1 = Tex("Each closing rolls into the next opening").scale(0.95).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4_l1))
        self.wait(3)

        # --- Band 5 (subtopic_3): reading the quarter's decisions
        self.next_band(5)
        b5_title = Tex("The decisions inside the budget").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("November dips to R4 000 — BY DESIGN:").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("big purchases go where balances can hold them").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("If negative: shift a month later, or arrange the").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("overdraft IN ADVANCE — banks price desperation").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("The 30\\% lag: profit and cash run on").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
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
        b6_l3 = Tex("Medium-term: range, staffing, 1 to 3 years").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Long-term: own premises, a showroom").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Zero-based where habit renews expenses:").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        b6_l6 = Tex("justify from zero, or cut").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): technique and the cash-only traps
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
        b8_l2 = Tex("and the one subtraction that matters").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("A report is a rear-view mirror; a budget is the headlights").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("An unwritten plan cannot be checked — the page").scale(0.95).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = Tex("turns vanished money into findable answers").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the purse through three months
        self.next_band(9)
        b9_title = Tex("Watching the purse through three months").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Oct: in 30 000, out 25 000 — purse to R8 000").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Nov: the planned knock — lathe R9 000;").scale(1.0).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex("purse gives back 4 000, closes at R4 000").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Lerato KNEW it would be thin; the neighbour,").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        b9_l5 = Tex("buying on feeling, watches the rent bounce").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex("Dec: purse recovers to R9 000").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): zero-based — every rand re-applies
        self.next_band(10)
        b10_title = Tex("Every rand re-applies for its job").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Copied budgets carry their dead forever:").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("the unwatched service, the outgrown bundle").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Begin from nothing: why does this line exist?").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("What does it buy NOW? What breaks without it?").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)
        b10_l5 = Tex("Spring-cleaning for money — it pays in").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        b10_l6 = Tex("recovered rands every time it is honestly done").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.wait(4)
