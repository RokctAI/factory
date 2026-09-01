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

# Band-layout whiteboard scene for "Partnerships and Statements Essentials"
# (grade 11, term 4, revision). One band per teaching beat; the camera moves
# down and nothing is removed. Part 1 (Expert) = subtopics 1-4, Part 2
# (Simplifier) = subtopics 5-7 in fresh bands. Exporter-safe primitives only;
# write-only reveals. Subtopic durations 220/220/230/230/190/200/200 of
# 1490 s guide the apportioning.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PartnershipsRevisionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): two accounts per partner ---
        title = Tex("Partnerships and Statements Essentials").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Two accounts PER partner:").scale(1.1).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("CAPITAL: the long-term stake —").scale(1.05).shift(UP * 0.5)
        b0_l3 = Tex("Lerato R240 000, Karabo R160 000; hardly moves").scale(0.95).shift(DOWN * 0.3)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex("CURRENT: the breathing account — profit share").scale(0.95).shift(DOWN * 1.2)
        b0_l5 = Tex("in, drawings out; credit $=$ business owes").scale(1.0).shift(DOWN * 2.0)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.wait(2.5)
        b0_l6 = Tex("The agreement is the constitution").scale(1.05).shift(DOWN * 2.9)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): appropriations are not expenses ---
        self.next_band(1)
        b1_t = Tex("The sharpest distinction in the topic").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_trap = Tex("Partners' salaries $=$ business expenses?").scale(1.05).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_trap))
        self.play(Create(strike(b1_trap)))
        self.wait(2)
        b1_l1 = Tex("They are APPROPRIATIONS —").scale(1.05).shift(band_shift(1) + UP * 0.2)
        b1_l2 = Tex("slices of a profit already earned").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2.5)
        b1_l3 = Tex("Income statement ends at net profit;").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        b1_l4 = Tex("only below that line does sharing begin").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): the appropriation account ---
        self.next_band(2)
        b2_t = Tex("Appropriating R300 000, in order").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Salaries: Lerato 108 000; Karabo 84 000").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("Interest at 10\\%: 24 000; 16 000").scale(1.0).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("Bonus to Karabo: 8 000").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        b2_l4 = Tex("Remainder 60 000, shared 3 : 2 —").scale(1.0).shift(band_shift(2) + DOWN * 1.3)
        b2_l5 = Tex("36 000 and 24 000").scale(1.0).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex("168 000 $+$ 132 000 $=$ 300 000: it EMPTIES").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the current accounts close ---
        self.next_band(3)
        b3_t = Tex("Closing the current accounts").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex("Lerato: 6 000 cr $+$ 168 000 $-$ 144 000").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("$=$ R30 000 credit").scale(1.05).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("Karabo: 9 000 DEBIT $+$ 132 000 $-$ 105 000").scale(1.0).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex("$=$ R18 000 credit").scale(1.05).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)
        b3_l5 = Tex("Business owes Lerato 30 000, Karabo 18 000 —").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        b3_l6 = Tex("both lived inside their earnings").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): statement of comprehensive income ---
        self.next_band(4)
        b4_t = Tex("Statement of comprehensive income").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("Sales 1 200 000 $-$ cost of sales 800 000").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("$=$ gross profit 400 000 (50\\% on cost)").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Other income: profit on disposal 6 000").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("Operating expenses 106 000").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Net profit 300 000 $\\rightarrow$ appropriation,").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        b4_l6 = Tex("never one partner's capital").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the asset disposal, four steps ---
        self.next_band(5)
        b5_t = Tex("The asset that left: four steps").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("1. Cost out: 90 000 to Disposal").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("2. Accumulated depreciation out: 60 000").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("$\\Rightarrow$ carrying value 30 000").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("3. Proceeds: 36 000").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex("4. Difference: PROFIT R6 000 — other income").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_l6 = Tex("Compare proceeds to CARRYING value, never cost").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_3): statement of financial position ---
        self.next_band(6)
        b6_t = Tex("Statement of financial position").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Non-current assets 420 000").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("Current: stock 120 000, debtors 80 000,").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("bank 40 000 — total assets 660 000").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Equity 448 000 (capitals 400 000").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex("$+$ current accounts 48 000)").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        b6_l6 = Tex("$+$ loan 112 000 $+$ current liabilities 100 000").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(2)
        b6_l7 = Tex("$=$ 660 000: it balances").scale(1.05).shift(band_shift(6) + DOWN * 3.5)
        self.play(Write(b6_l7))
        self.play(Create(SurroundingRectangle(b6_l7, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): profitability and the operating pulse ---
        self.next_band(7)
        b7_t = Tex("Profitability and the operating pulse").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Gross profit: 33,3\\% on sales; 50\\% on cost").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("Net profit: 300 000 / 1 200 000 $=$ 25\\%").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex("Stock turnover: 800 000 / 100 000 $=$ 8 times").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Debtors: 80 000 / 480 000 $\\times$ 12 $=$ 2 months").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        b7_l5 = Tex("vs 30-day terms: slack — tighten collections").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): liquidity, gearing, return ---
        self.next_band(8)
        b8_t = Tex("Liquidity, gearing, return").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Current ratio 240 000 / 100 000 $=$ 2,4 : 1").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Acid test 120 000 / 100 000 $=$ 1,2 : 1").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Debt-equity 112 000 / 448 000 $=$ 0,25 : 1 —").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("lightly geared; headroom to borrow").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Return: 300 000 / 422 500 $\\approx$ 71\\% —").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        b8_l6 = Tex("partners' salaries sit INSIDE it").scale(1.0).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): two friends, one till ---
        self.next_band(9)
        b9_t = Tex("Two friends, one till").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("``I invested more'' / ``I work harder''").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("— the agreement answers both first:").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        b9_l3 = Tex("salary for hours, interest for waiting,").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex("a ratio for the rest — written, signed").scale(1.0).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("Two piles per friend: the DEEP pile stays").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        b9_l6 = Tex("planted; the BREATHING pile moves yearly").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_6): slicing the profit pot ---
        self.next_band(10)
        b10_t = Tex("Slicing the R300 000 pot").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Scoop 1 — hours: 108 000 and 84 000").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("Scoop 2 — waiting money: 24 000 and 16 000").scale(1.0).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex("Scoop 3 — promised bonus: 8 000").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("Scoop 4 — the rest, 3 : 2: 36 000 and 24 000").scale(1.0).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Bowls: 168 000 $+$ 132 000 $=$ 300 000 —").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        b10_l6 = Tex("the pot empties to the rand").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): reading the scoreboard ---
        self.next_band(11)
        b11_t = Tex("Reading the scoreboard").scale(1.1).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("Shopper: a third of every sale is gross profit;").scale(0.95).shift(band_shift(11) + UP * 1.2)
        b11_l2 = Tex("stock turns 8 times — but debtors take 2 months").scale(0.95).shift(band_shift(11) + UP * 0.5)
        self.play(Write(b11_l1))
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = Tex("Creditor: 2,4 : 1 near money; 1,2 : 1").scale(0.95).shift(band_shift(11) + DOWN * 0.4)
        b11_l4 = Tex("without touching stock — sleep well").scale(0.95).shift(band_shift(11) + DOWN * 1.1)
        self.play(Write(b11_l3))
        self.play(Write(b11_l4))
        self.wait(2.5)
        b11_l5 = Tex("Bank: one rand borrowed per four owned").scale(0.95).shift(band_shift(11) + DOWN * 2.0)
        b11_l6 = Tex("Friends: about 71 rand back per hundred kept —").scale(0.95).shift(band_shift(11) + DOWN * 2.7)
        b11_l7 = Tex("part of it their own labour coming home").scale(0.95).shift(band_shift(11) + DOWN * 3.4)
        self.play(Write(b11_l5))
        self.wait(2)
        self.play(Write(b11_l6))
        self.play(Write(b11_l7))
        self.play(Create(SurroundingRectangle(b11_l7, color=GREEN)))
        self.wait(4)
