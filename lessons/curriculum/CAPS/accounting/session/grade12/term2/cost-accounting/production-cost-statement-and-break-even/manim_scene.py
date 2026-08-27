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

# Band-layout whiteboard scene for "Production Cost Statement and Break-Even"
# (grade 12, term 2, cost accounting). One band per teaching beat; the camera
# moves down and nothing is removed. Part 1 (Expert) = subtopics 1-4, Part 2
# (Simplifier) = subtopics 5-7 in fresh bands. Exporter-safe primitives only;
# write-only reveals. Subtopic durations 230/250/230/250/190/205/215 of
# 1570 s guide the apportioning.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ProductionCostBreakEvenSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the three factory cost families ---
        title = Tex("Production Cost Statement and Break-Even").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Direct materials: timber, fabric, flour").scale(1.0).shift(UP * 1.2)
        b0_l2 = Tex("Direct labour: the hands that make it").scale(1.0).shift(UP * 0.5)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("Together: PRIME COST").scale(1.05).shift(DOWN * 0.3)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex("$+$ Factory overheads: rent, electricity,").scale(1.0).shift(DOWN * 1.1)
        b0_l5 = Tex("machine depreciation, indirect labour").scale(1.0).shift(DOWN * 1.8)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.wait(2)
        b0_trap = Tex("Sales office rent $=$ factory overhead?").scale(0.95).shift(DOWN * 2.6)
        self.play(Write(b0_trap))
        self.play(Create(strike(b0_trap)))
        b0_fix = Tex("Administration — the word FACTORY matters").scale(0.95).shift(DOWN * 3.3)
        self.play(Write(b0_fix))
        self.wait(3)

        # --- Band 1 (subtopic_1): three stocks, not one ---
        self.next_band(1)
        b1_t = Tex("Three stocks, not one").scale(1.15).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_t))
        self.wait(2)
        grid = Rectangle(width=11.0, height=2.6).shift(band_shift(1) + UP * 0.5)
        v1 = Line(grid.get_top() + LEFT * 1.85, grid.get_bottom() + LEFT * 1.85)
        v2 = Line(grid.get_top() + RIGHT * 1.85, grid.get_bottom() + RIGHT * 1.85)
        self.play(Create(grid), Create(v1), Create(v2))
        c1 = Tex("Raw\\\\materials").scale(0.9).shift(band_shift(1) + UP * 1.1 + LEFT * 3.7)
        c2 = Tex("Work-in-\\\\progress").scale(0.9).shift(band_shift(1) + UP * 1.1)
        c3 = Tex("Finished\\\\goods").scale(0.9).shift(band_shift(1) + UP * 1.1 + RIGHT * 3.7)
        self.play(Write(c1), Write(c2), Write(c3))
        self.wait(2)
        d1 = Tex("waiting to\\\\be used").scale(0.8).shift(band_shift(1) + DOWN * 0.2 + LEFT * 3.7)
        d2 = Tex("started, not\\\\finished").scale(0.8).shift(band_shift(1) + DOWN * 0.2)
        d3 = Tex("ready for\\\\sale").scale(0.8).shift(band_shift(1) + DOWN * 0.2 + RIGHT * 3.7)
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Write(d3))
        self.wait(2.5)
        b1_l1 = Tex("Beyond the factory: administration cost").scale(1.0).shift(band_shift(1) + DOWN * 1.6)
        b1_l2 = Tex("and selling and distribution cost").scale(1.0).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(3)

        # --- Band 2 (subtopic_2): the direct materials note ---
        self.next_band(2)
        b2_t = Tex("Mzansi Textiles: materials USED").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Opening raw materials \\quad R80 000").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("$+$ Purchases \\quad R640 000").scale(1.0).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex("$+$ Carriage on purchases \\quad R20 000").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex("$=$ Available \\quad R740 000").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        b2_l5 = Tex("$-$ Closing stock \\quad R120 000").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        b2_l6 = Tex("Direct material cost: R620 000").scale(1.05).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l1))
        self.wait(1.5)
        self.play(Write(b2_l2))
        self.wait(1.5)
        self.play(Write(b2_l3))
        self.wait(1.5)
        self.play(Write(b2_l4))
        self.wait(1.5)
        self.play(Write(b2_l5))
        self.wait(1.5)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        b2_l7 = Tex("buying is not using — the shelf stays out").scale(0.9).shift(band_shift(2) + DOWN * 3.6)
        self.play(Write(b2_l7))
        self.wait(3)

        # --- Band 3 (subtopic_2): down to cost of production ---
        self.next_band(3)
        b3_t = Tex("The production cost statement").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex("$+$ Direct labour R380 000:").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("PRIME COST R1 000 000").scale(1.05).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("$+$ Factory overheads R440 000:").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex("total manufacturing cost R1 440 000").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex("$+$ opening WIP R60 000 $-$ closing R100 000").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        b3_l6 = Tex("Cost of production: R1 400 000").scale(1.05).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l5))
        self.wait(2)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        b3_l7 = Tex("70 000 garments: unit cost R20").scale(1.0).shift(band_shift(3) + DOWN * 3.6)
        self.play(Write(b3_l7))
        self.wait(3)

        # --- Band 4 (subtopic_3): finished goods to gross profit ---
        self.next_band(4)
        b4_t = Tex("Factory floor to income statement").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("Finished goods: R90 000 $+$ R1 400 000").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("$=$ R1 490 000 $-$ closing R140 000").scale(1.0).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex("Cost of sales R1 350 000 (67 500 sold)").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex("Sales: 67 500 $\\times$ R32 $=$ R2 160 000").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        b4_l5 = Tex("Gross profit R810 000").scale(1.05).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        b4_l6 = Tex("check: 810/1 350 $=$ 60\\% on cost — policy").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): operating costs and the address game ---
        self.next_band(5)
        b5_t = Tex("Every expense has one address").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("Administration R290 000;").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("selling and distribution R256 000").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex("Net profit: 810 $-$ 290 $-$ 256 $=$ R264 000").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("Depreciation splits by USE: machinery to").scale(0.95).shift(band_shift(5) + DOWN * 1.4)
        b5_l5 = Tex("factory, office equipment to admin,").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        b5_l6 = Tex("delivery vehicles to selling").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): break-even, the drill case ---
        self.next_band(6)
        b6_t = Tex("Break-even: sort by BEHAVIOUR").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("Price R32; variable R21 a unit;").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("fixed costs R660 000 a year").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Contribution: R32 $-$ R21 $=$ R11").scale(1.05).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("R660 000 $\\div$ R11 $=$ 60 000 units").scale(1.1).shift(band_shift(6) + DOWN * 1.4)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2)
        b6_l5 = Tex("Sold 67 500: a 7 500-unit cushion —").scale(1.0).shift(band_shift(6) + DOWN * 2.3)
        b6_l6 = Tex("state it; the interpretation mark asks").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(3)

        # --- Band 7 (subtopic_4): the levers, and factory ethics ---
        self.next_band(7)
        b7_t = Tex("The levers, and the ethics").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("Price up: contribution widens, line falls").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("Materials dearer: line climbs;").scale(0.95).shift(band_shift(7) + UP * 0.5)
        b7_l3 = Tex("new machine: the fixed pile grows").scale(0.95).shift(band_shift(7) + DOWN * 0.2)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("Ethics: no expired or substandard goods;").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        b7_l5 = Tex("honest sourcing; price fixing is illegal").scale(0.95).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2.5)
        b7_l6 = Tex("Controls: requisitions, clock cards,").scale(0.95).shift(band_shift(7) + DOWN * 2.6)
        b7_l7 = Tex("independent production counts, waste watched").scale(0.9).shift(band_shift(7) + DOWN * 3.3)
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): Auntie Grace's koeksister kitchen ---
        self.next_band(8)
        b8_t = Tex("Auntie Grace's koeksister kitchen").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Flour, sugar, oil, syrup: direct materials").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Palesa braiding dough: direct labour").scale(0.95).shift(band_shift(8) + UP * 0.5)
        b8_l3 = Tex("Gas, stand rent, pan oil: overheads —").scale(0.95).shift(band_shift(8) + DOWN * 0.2)
        b8_l4 = Tex("real, spread over all, pinned to none").scale(0.95).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Cupboard $=$ raw materials; counter dough").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        b8_l6 = Tex("$=$ work-in-progress; display box $=$ finished").scale(0.95).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(2.5)
        b8_l7 = Tex("Kitchen makes; office runs; selling moves").scale(0.95).shift(band_shift(8) + DOWN * 3.3)
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): what one koeksister costs ---
        self.next_band(9)
        b9_t = Tex("What does ONE koeksister cost?").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Ingredients USED R6 000 (bought R7 000;").scale(0.95).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("R1 000 still in the cupboard stays out)").scale(0.95).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("$+$ wages R5 000 $+$ overheads R3 000").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        b9_l4 = Tex("$=$ kitchen total R14 000").scale(1.0).shift(band_shift(9) + DOWN * 1.0)
        self.play(Write(b9_l3))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("Dough trays: $+$R400 old $-$R600 new").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        b9_l6 = Tex("$=$ finished production R13 800").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l5))
        self.wait(2)
        self.play(Write(b9_l6))
        self.wait(2)
        b9_l7 = Tex("R13 800 $\\div$ 2 300 $=$ R6 a koeksister").scale(1.05).shift(band_shift(9) + DOWN * 3.3)
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): break-even at the stand ---
        self.next_band(10)
        b10_t = Tex("How many before she smiles?").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex("Each koeksister: sells R10, eats R5 —").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex("contributes R5; the rent pile is R4 000").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("R4 000 $\\div$ R5 $=$ 800 koeksisters").scale(1.1).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_l4 = Tex("Proof: 800 $\\times$ R10 $=$ R8 000 in;").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        b10_l5 = Tex("ingredients R4 000 $+$ rent R4 000 out").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        b10_l6 = Tex("$=$ zero — the smile starts at 801").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.wait(2)
        self.play(Write(b10_l6))
        self.wait(3)

        # --- Band 11 (subtopic_7): her levers, and her ethics ---
        self.next_band(11)
        b11_t = Tex("Move the levers, keep the ethics").scale(1.1).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex("Syrup up, eats R6: line jumps to 1 000").scale(1.0).shift(band_shift(11) + UP * 1.2)
        b11_l2 = Tex("Price R11: contribution R6, line near 667").scale(1.0).shift(band_shift(11) + UP * 0.4)
        b11_l3 = Tex("Second stand: R4 000 more rent —").scale(1.0).shift(band_shift(11) + DOWN * 0.4)
        b11_l4 = Tex("break-even doubles before growth pays").scale(1.0).shift(band_shift(11) + DOWN * 1.1)
        self.play(Write(b11_l1))
        self.wait(2)
        self.play(Write(b11_l2))
        self.wait(2)
        self.play(Write(b11_l3))
        self.play(Write(b11_l4))
        self.wait(2.5)
        b11_l5 = Tex("No day-old sold as fresh; no price deals").scale(0.95).shift(band_shift(11) + DOWN * 2.0)
        b11_l6 = Tex("with the vetkoek lady; bags counted").scale(0.95).shift(band_shift(11) + DOWN * 2.7)
        b11_l7 = Tex("against batches — kitchen-sized controls").scale(0.95).shift(band_shift(11) + DOWN * 3.4)
        self.play(Write(b11_l5))
        self.play(Write(b11_l6))
        self.play(Write(b11_l7))
        self.wait(4)
