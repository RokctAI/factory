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

# Band-layout whiteboard scene for the IEB Grade 10 Accounting session duo
# "Statement of Comprehensive Income". Add-only lifecycle, one band per
# teaching beat, camera moves down between bands. Covers all seven subtopics:
# Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7) in fresh
# bands. subtopics.json durations 210/220/220/200/180/200/190 of 1420 s.
# The prescribed statement skeleton is drawn first (Rectangle panel + ruled
# Lines), then each figure is posted into it in script order.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ComprehensiveIncomeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): nominal vs balance sheet, FOR vs AT
        title = Tex("Statement of Comprehensive Income").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("NOMINAL accounts measure the year's FLOWS").scale(1.0).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex("Balance sheet accounts: POSITION at a moment").scale(1.0).shift(UP * 0.4)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("This statement uses nominal accounts ONLY").scale(1.0).shift(DOWN * 0.5)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = Tex("Heading: FOR the year ended 30 June").scale(1.0).shift(DOWN * 1.5)
        b0_l5 = Tex("(a period — next lesson's photo is AT a date)").scale(0.95).shift(DOWN * 2.3)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_2): the trading layer, posted into the skeleton
        self.next_band(1)
        b1_title = Tex("The format — the trading layer").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        panel = Rectangle(width=10.5, height=4.4).shift(band_shift(1) + DOWN * 0.5)
        self.play(Create(panel))
        b1_r1 = Tex("Sales (61 500 $-$ 1 500 allowances)").scale(0.95).shift(band_shift(1) + UP * 0.9)
        b1_r1b = Tex("R60 000").scale(0.95).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_r1))
        self.wait(2)
        self.play(Write(b1_r1b))
        self.wait(2)
        b1_r2 = Tex("Cost of sales \\quad (40 000)").scale(0.95).shift(band_shift(1) + DOWN * 0.6)
        self.play(Write(b1_r2))
        self.wait(2)
        rule1 = Line(LEFT * 5.25, RIGHT * 5.25).shift(band_shift(1) + DOWN * 1.1)
        self.play(Create(rule1))
        b1_r3 = Tex("Gross profit \\quad R20 000").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_r3))
        self.play(Create(SurroundingRectangle(b1_r3, color=GREEN)))
        self.wait(2)
        b1_l1 = Tex("Confirms the 50\\% mark-up on cost").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l1))
        self.wait(3)

        # --- Band 2 (subtopic_2): operating and financing layers to net profit
        self.next_band(2)
        b2_title = Tex("Operating, then financing").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("+ Other operating income: rent R7 200").scale(0.95).shift(band_shift(2) + UP * 1.3)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Gross operating income: R27 200").scale(0.95).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("$-$ Operating expenses, by name: (15 200)").scale(0.95).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Operating profit: R12 000").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("$-$ Interest expense: (1 500)").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex("NET PROFIT FOR THE YEAR: R10 500").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_3): every adjustment with its working
        self.next_band(3)
        b3_title = Tex("Adjustments, with workings shown").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Water and electricity: } 2\,640 + 300 = 2\,940").scale(1.0).shift(band_shift(3) + UP * 1.2)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"\text{Insurance: } 1\,800 - 1\,200 = 600").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"\text{Rent income: } 6\,600 + 600 = 7\,200").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = MathTex(r"\text{Depreciation: } 14\,000 \times 20\% = 2\,800").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = MathTex(r"\text{Interest: } 15\,000 \times 10\% = 1\,500").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex("Workings in brackets — the route earns marks").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): the two placements the markers watch
        self.next_band(4)
        b4_title = Tex("Placements the markers watch").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex("Trading stock DEFICIT: an operating expense").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("A SURPLUS would join other operating income").scale(1.0).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_wrong = Tex("Interest listed among operating expenses").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l3 = Tex("Interest frames operating profit from below —").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        b4_l4 = Tex("operating profit measures operations alone").scale(1.0).shift(band_shift(4) + DOWN * 2.4)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): reading the statement as three audiences
        self.next_band(5)
        b5_title = Tex("Reading the statement").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = Tex("Owner: three layers, three diagnoses —").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("pricing, operations, financing").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"\text{Bank: } 12\,000 \div 1\,500 = 8 \text{ times covered}").scale(0.92).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = Tex("Accountant: every line traces to an adjusted").scale(1.0).shift(band_shift(5) + DOWN * 1.7)
        b5_l5 = Tex("ledger figure; every subtotal to its lines").scale(1.0).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): the year's story on one page
        self.next_band(6)
        b6_title = Tex("The year's story on one page").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("What the shop SOLD, minus what it COST —").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("first breath: trading profit").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Rent joins, running costs file through —").scale(1.0).shift(band_shift(6) + DOWN * 0.6)
        b6_l4 = Tex("second breath: operating profit").scale(1.0).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Interest steps up — the end: net profit").scale(1.0).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_6): the three floors of profit
        self.next_band(7)
        b7_title = Tex("Three floors of profit").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Trading floor: is buying-and-selling healthy?").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("R20 000").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Running floor: is the shop-machine healthy?").scale(0.95).shift(band_shift(7) + DOWN * 0.3)
        b7_l4 = Tex("R12 000").scale(1.0).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Borrowing floor: what did it truly keep?").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        b7_l6 = Tex("R10 500 — the floors tell you WHERE the leak is").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_7): where every adjustment lands
        self.next_band(8)
        b8_title = Tex("Where every adjustment lands").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Water and electricity: (2 640 + 300) = 2 940").scale(1.0).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("Insurance: (1 800 $-$ 1 200) = 600").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Rent income: (6 600 + 600) = 7 200").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l3))
        self.wait(2)
        b8_l4 = Tex("Depreciation R2 800; interest R1 500 —").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex("interest on the ground floor, never running costs").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex("Bracket the working — the road is worth marks").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(4)
