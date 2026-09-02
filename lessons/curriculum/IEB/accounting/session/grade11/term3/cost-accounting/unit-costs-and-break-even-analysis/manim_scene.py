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

# Band-layout whiteboard scene for "Unit Costs and Break-Even Analysis"
# (grade 11, term 3, cost accounting). One band per teaching beat; camera
# moves down, nothing is removed. Part 1 (Expert) = subtopics 1-4,
# Part 2 (Simplifier) = subtopics 5-7 in fresh bands. Exporter-safe
# primitives only; write-only reveals. Subtopic durations
# 225/225/240/235/195/195/205 of 1520 s guide the apportioning.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BreakEvenAnalysisSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the budget, and cost behaviour ---
        title = Tex("Unit Costs and Break-Even Analysis").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Plan: 20 000 bags at R120 each").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("Variable R64 per bag: materials 34,").scale(1.0).shift(UP * 0.4)
        b0_l3 = Tex("labour 22, selling 8").scale(1.0).shift(DOWN * 0.3)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.wait(2.5)
        b0_l4 = Tex("Fixed R560 000: overheads 356 000").scale(1.0).shift(DOWN * 1.1)
        b0_l5 = Tex("$+$ administration 204 000").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): per unit vs in total ---
        self.next_band(1)
        b1_t = Tex("Watch each family from two angles").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Variable: R64 per unit always;").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("total grows — 512 000 at 8 000 bags").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Fixed: R560 000 total always;").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        b1_l4 = Tex("per unit shrinks — R70 at 8 000, R28 at 20 000").scale(0.95).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("A full unit cost is only true AT its output").scale(1.0).shift(band_shift(1) + DOWN * 2.1)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): contribution per unit ---
        self.next_band(2)
        b2_t = Tex("Contribution per unit").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex("R120 selling price $-$ R64 variable").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("$=$ R56 contribution").scale(1.1).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_wrong = Tex("Contribution $=$ profit?").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l3 = Tex("It first pays the R560 000 wall of").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        b2_l4 = Tex("fixed costs; only then falls through").scale(1.0).shift(band_shift(2) + DOWN * 2.1)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): the four-line statement ---
        self.next_band(3)
        b3_t = Tex("The four-line statement").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Sales: 20 000 $\\times$ R120 \\quad R2 400 000").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("$-$ Variable: 20 000 $\\times$ R64 \\quad R1 280 000").scale(1.0).shift(band_shift(3) + UP * 0.4)
        b3_l3 = Tex("Contribution \\quad R1 120 000").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex("$-$ Fixed costs \\quad R560 000").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        b3_l5 = Tex("Budgeted profit: R560 000").scale(1.05).shift(band_shift(3) + DOWN * 2.1)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the break-even point ---
        self.next_band(4)
        b4_t = Tex("The break-even point").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex("Fixed costs $\\div$ contribution per unit").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("R560 000 $\\div$ R56 $=$ 10 000 bags").scale(1.1).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2.5)
        b4_l3 = Tex("Value: 10 000 $\\times$ R120 $=$ R1 200 000").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("Check: contribution 560 000 $=$ fixed;").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        b4_l5 = Tex("profit zero — half the 20 000 plan").scale(1.0).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2.5)
        b4_l6 = Tex("10 001,8? Round UP: 10 002").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): margin of safety and what-ifs ---
        self.next_band(5)
        b5_t = Tex("Working with break-even").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex("Margin of safety: 20 000 $-$ 10 000").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("$=$ 10 000 bags — 50\\% of the plan").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Price R112: contribution 48;").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex("560 000 $\\div$ 48 $\\to$ 11 667 bags").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("Canvas $+$R4: 52 $\\to$ 10 770 bags;").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        b5_l6 = Tex("fixed $+$R56 000: 616 000 $\\div$ 56 $=$ 11 000").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the model's assumptions ---
        self.next_band(6)
        b6_t = Tex("The model's assumptions").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex("Price and unit variable cost constant;").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("fixed costs never step; all made is sold").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("True near the planned range,").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("fraying far outside it").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("Used in range: the cheapest consultant").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        b6_l6 = Tex("a small factory will ever appoint").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the pile of stones ---
        self.next_band(7)
        b7_t = Tex("The pile of stones").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Saturday costs R560 before plate one:").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("braai stand R340, gazebo and coolers R220").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Each plate: R64 travels with it;").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("sell at R120, keep R56").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("R56 $=$ one stone lifted off the pile").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l5))
        self.play(Create(SurroundingRectangle(b7_l5, color=GREEN)))
        self.wait(2.5)
        b7_l6 = Tex("Ingredients scale; the stand hire never does").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l6))
        self.wait(3.5)

        # --- Band 8 (subtopic_6): plate number ten ---
        self.next_band(8)
        b8_t = Tex("Plate number ten").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("R560 $\\div$ R56 $=$ TEN plates").scale(1.1).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.play(Create(SurroundingRectangle(b8_l1, color=GREEN)))
        self.wait(2.5)
        b8_l2 = Tex("Plates one to ten: working for the").scale(1.0).shift(band_shift(8) + UP * 0.2)
        b8_l3 = Tex("stand man. Plate eleven: for yourself").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Factory version: R560 000 $\\div$ R56").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex("$=$ bag number 10 000").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex("Ten comma four? Break even on ELEVEN —").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        b8_l7 = Tex("round the survival line UP, always").scale(0.95).shift(band_shift(8) + DOWN * 3.6)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3.5)

        # --- Band 9 (subtopic_7): when the price of meat goes up ---
        self.next_band(9)
        b9_t = Tex("When the price of meat goes up").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Steak $+$R4: contribution 52 $\\to$ 11 plates").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Team deal at R112: contribution 48").scale(0.95).shift(band_shift(9) + UP * 0.3)
        b9_l3 = Tex("$\\to$ 12 plates — one seventh of R56 gone").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Stand hire $+$R56: pile 616 $\\to$ 11 exactly").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Calculate BEFORE you commit").scale(1.05).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(2.5)
        b9_l6 = Tex("Break-even is not a report card;").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        b9_l7 = Tex("it is a headlight").scale(1.0).shift(band_shift(9) + DOWN * 3.7)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(4)
