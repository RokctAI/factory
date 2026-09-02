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

# Band-layout whiteboard scene for the session duo "Manufacturing Costs and
# Ledger Accounts" (grade 11, term 3, cost accounting). One band per teaching
# beat; the camera moves down to fresh space and nothing is ever removed.
# Part 1 (Expert) covers subtopics 1-4, Part 2 (Simplifier) re-teaches as
# subtopics 5-7 in fresh bands. Exporter-safe primitives only; write-only
# reveals, no Transform/FadeOut. Subtopic durations
# 225/230/245/225/195/195/200 of 1515 s guide the time apportioning.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ManufacturingCostsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): sorting costs by traceability ---
        title = Tex("Manufacturing Costs and Ledger Accounts").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Sort every cost twice:").scale(1.1).shift(UP * 1.3)
        b0_l2 = Tex("by traceability and by behaviour").scale(1.1).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Direct materials $+$ direct labour").scale(1.0).shift(DOWN * 0.4)
        b0_l4 = Tex("$=$ PRIME COST — costs that touch the bag").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("$+$ factory overheads $=$ total production cost").scale(0.95).shift(DOWN * 2.0)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l5, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): period costs and cost behaviour ---
        self.next_band(1)
        b1_t = Tex("Period costs stay OUT of production").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Administration: office, bookkeeper").scale(1.05).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("Selling: advertising, delivery fuel").scale(1.05).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Behaviour: VARIABLE moves with output").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex("FIXED ignores output: rent, supervisor").scale(1.05).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_trap = Tex("Sales commission $=$ production cost?").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_trap))
        self.play(Create(strike(b1_trap)))
        b1_fix = Tex("Variable, but a SELLING cost").scale(1.05).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_fix))
        self.wait(3)

        # --- Band 2 (subtopic_2): three stock accounts, drawn as a table ---
        self.next_band(2)
        b2_t = Tex("Three stock accounts, not one").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        grid = Rectangle(width=11.0, height=3.0).shift(band_shift(2) + UP * 0.2)
        self.play(Create(grid))
        c1 = Tex("Raw materials").scale(0.95).shift(band_shift(2) + UP * 1.2 + LEFT * 3.7)
        c2 = Tex("Work-in-progress").scale(0.95).shift(band_shift(2) + UP * 1.2)
        c3 = Tex("Finished goods").scale(0.95).shift(band_shift(2) + UP * 1.2 + RIGHT * 3.7)
        self.play(Write(c1))
        self.play(Write(c2))
        self.play(Write(c3))
        d1 = Tex("canvas, zips,\\\\straps").scale(0.8).shift(band_shift(2) + UP * 0.0 + LEFT * 3.7)
        d2 = Tex("half-sewn bags,\\\\value mid-process").scale(0.8).shift(band_shift(2) + UP * 0.0)
        d3 = Tex("completed bags\\\\awaiting sale").scale(0.8).shift(band_shift(2) + UP * 0.0 + RIGHT * 3.7)
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Write(d3))
        self.wait(2.5)
        b2_l1 = Tex("Plus consumable stores: oil, needles").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        b2_l2 = Tex("used up, flow to overheads").scale(1.0).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(3)

        # --- Band 3 (subtopic_2): raw materials issued — the first key figure ---
        self.next_band(3)
        b3_t = Tex("Raw materials: what was ISSUED?").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Opening balance \\quad R72 000").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("$+$ Purchases \\quad R468 000").scale(1.05).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("$+$ Carriage on purchases \\quad R12 000").scale(1.05).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex("$=$ Available \\quad R552 000").scale(1.05).shift(band_shift(3) + DOWN * 1.2)
        b3_l5 = Tex("$-$ Closing stock \\quad R64 000").scale(1.05).shift(band_shift(3) + DOWN * 2.0)
        b3_l6 = Tex("Issued to production: R488 000").scale(1.1).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): cost accounts carry prime cost ---
        self.next_band(4)
        b4_t = Tex("The cost accounts fill up").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Direct materials cost \\quad R488 000").scale(1.05).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        b4_l2 = Tex("Direct labour: wages R342 000").scale(1.05).shift(band_shift(4) + UP * 0.3)
        b4_l3 = Tex("$+$ employer contributions R24 000").scale(1.05).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("Direct labour cost \\quad R366 000").scale(1.05).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Prime cost: R488 000 $+$ R366 000").scale(1.05).shift(band_shift(4) + DOWN * 2.2)
        b4_l6 = Tex("$=$ R854 000").scale(1.1).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): factory overheads, each named ---
        self.next_band(5)
        b5_t = Tex("Factory overhead cost account").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("Indirect materials \\quad R34 000").scale(1.0).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("Supervisor's salary \\quad R120 000").scale(1.0).shift(band_shift(5) + UP * 0.6)
        b5_l3 = Tex("Factory rent \\quad R84 000").scale(1.0).shift(band_shift(5) + DOWN * 0.1)
        b5_l4 = Tex("Electricity and water \\quad R48 000").scale(1.0).shift(band_shift(5) + DOWN * 0.8)
        b5_l5 = Tex("Depreciation R52 000; insurance R18 000").scale(1.0).shift(band_shift(5) + DOWN * 1.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2.5)
        b5_l6 = Tex("Total factory overheads: R356 000").scale(1.1).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_3): work-in-progress and the unit cost ---
        self.next_band(6)
        b6_t = Tex("Work-in-progress: the meeting pot").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Opening \\quad R38 000").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("$+$ prime cost R854 000 $+$ overheads R356 000").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("$=$ manufacturing costs R1 210 000").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("$-$ closing R48 000").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("Finished production: R1 200 000").scale(1.05).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(2)
        b6_l6 = Tex("20 000 bags: unit cost R60 per backpack").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_3): finished goods to gross profit ---
        self.next_band(7)
        b7_t = Tex("Finished goods closes the chain").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("Opening R76 000 $+$ production R1 200 000").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("$-$ closing R96 000 $=$ cost of sales R1 180 000").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Sales R1 770 000 $-$ R1 180 000").scale(1.0).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = Tex("Gross profit R590 000 — 50\\% on cost").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex("Materials $\\to$ prime cost $\\to$ WIP").scale(1.0).shift(band_shift(7) + DOWN * 2.3)
        b7_l6 = Tex("$\\to$ finished goods $\\to$ cost of sales").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_4): ethics and control on the floor ---
        self.next_band(8)
        b8_t = Tex("Control follows the flow").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = Tex("Materials: locked store, signed requisitions,").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("issued vs should-have-used compared").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Labour: clock cards, overtime pre-approved").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("Overheads: budgets, meters read, maintenance").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Waste in the drain $=$ cost saving?").scale(1.0).shift(band_shift(8) + DOWN * 2.0)
        self.play(Write(b8_l5))
        self.play(Create(strike(b8_l5)))
        b8_l6 = Tex("Costs shifted onto the community").scale(1.0).shift(band_shift(8) + DOWN * 2.8)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the samoosa stand ---
        self.next_band(9)
        b9_t = Tex("The samoosa stand").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Pastry, mince, spices: direct materials").scale(1.0).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("Aunt frying for a fee: direct labour").scale(1.0).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Gas, table hire, fryer wearing out:").scale(1.0).shift(band_shift(9) + DOWN * 0.5)
        b9_l4 = Tex("the overheads basket").scale(1.0).shift(band_shift(9) + DOWN * 1.2)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Posters and airtime: costs of the DAY,").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        b9_l6 = Tex("not of the samoosa — keep them out").scale(0.95).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_6): the three tables ---
        self.next_band(10)
        b10_t = Tex("Three tables, one grammar").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Ingredients / half-done / display box").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("= raw materials / WIP / finished goods").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Was there $+$ arrived $-$ still there").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        b10_l4 = Tex("$=$ moved on").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("72 000 $+$ 468 000 $+$ 12 000 $-$ 64 000").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l6 = Tex("USED in the making: R488 000").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(3.5)

        # --- Band 11 (subtopic_7): one backpack, followed all the way ---
        self.next_band(11)
        b11_t = Tex("One backpack, followed all the way").scale(1.1).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("Materials 488 000 $+$ wages 366 000").scale(0.95).shift(band_shift(11) + UP * 1.1)
        b11_l2 = Tex("$+$ overheads 356 000 $=$ 1 210 000 poured in").scale(0.95).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11_l1))
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = Tex("38 000 waited; 48 000 still half-sewn:").scale(0.95).shift(band_shift(11) + DOWN * 0.5)
        b11_l4 = Tex("finished bags cost R1 200 000").scale(1.0).shift(band_shift(11) + DOWN * 1.2)
        self.play(Write(b11_l3))
        self.play(Write(b11_l4))
        self.wait(2.5)
        b11_l5 = Tex("20 000 bags $\\to$ R60 a bag: the heartbeat").scale(1.0).shift(band_shift(11) + DOWN * 2.0)
        self.play(Write(b11_l5))
        self.play(Create(SurroundingRectangle(b11_l5, color=GREEN)))
        self.wait(2.5)
        b11_l6 = Tex("Store: 76 000 $+$ 1 200 000 $-$ 96 000").scale(0.95).shift(band_shift(11) + DOWN * 2.9)
        b11_l7 = Tex("$=$ cost of sales 1 180 000; profit R590 000").scale(0.95).shift(band_shift(11) + DOWN * 3.6)
        self.play(Write(b11_l6))
        self.play(Write(b11_l7))
        self.wait(4)
