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

# Band-layout whiteboard scene for the CAPS Grade 10 Accounting session duo
# "Manufacturing Concepts and Basic Cost Calculations". Add-only lifecycle,
# one band per teaching beat, camera moves down between bands. Covers all
# seven subtopics: Part 1 Expert (subtopics 1-4), Part 2 Simplifier
# (subtopics 5-7) in fresh bands. subtopics.json durations
# 220/220/220/220/180/190/190 of 1440 s.

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
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the sorting test — direct costs
        title = Tex("Manufacturing Costs").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("A workshop sews 400 school shirts a month").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex("The test: trace this cost to ONE shirt?").scale(1.05).shift(UP * 0.3)
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = Tex("Direct materials: fabric, R40 per shirt").scale(1.0).shift(DOWN * 0.7)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Direct labour: machinist, R25 per shirt sewn").scale(1.0).shift(DOWN * 1.5)
        self.play(Write(b0_l4))
        self.wait(2)
        b0_l5 = Tex("Her work IS the shirt — traceable to each unit").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the indirect family and the factory fence
        self.next_band(1)
        b1_title = Tex("The indirect family: factory overheads").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("Indirect materials: thread, needles, machine oil").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Indirect labour: the supervisor of the floor").scale(1.0).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Plus workshop rent, electricity, depreciation").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("Real costs of making — spread over ALL shirts").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex("The fence: shop costs are NOT production costs").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): prime cost, computed
        self.next_band(2)
        b2_title = Tex("Layer one: prime cost").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Fabric: } 400 \times 40 = 16\,000").scale(1.1).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Machinist: } 400 \times 25 = 10\,000").scale(1.1).shift(band_shift(2) + UP * 0.0)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Prime cost: } 16\,000 + 10\,000 = 26\,000").scale(1.1).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Prime — first: the costs that touch the product").scale(1.0).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): total production cost and the unit cost
        self.next_band(3)
        b3_title = Tex("Layers two and three: total and unit").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = MathTex(r"\text{Overheads: } 3\,000 + 2\,000 + 600 + 400 = 6\,000").scale(0.95).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = MathTex(r"\text{Total production: } 26\,000 + 6\,000 = 32\,000").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Unit cost: } \frac{32\,000}{400} = \text{R}80").scale(1.1).shift(band_shift(3) + DOWN * 1.0)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("Sell at R100: clears R20. Below R80: a loss").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Half-sewn shirts: work-in-progress, the halfway house").scale(0.9).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): fixed and variable behaviour
        self.next_band(4)
        b4_title = Tex("The second sorting: behaviour").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex("Variable costs move WITH output:").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = MathTex(r"\text{per unit constant: } 40 + 25 = \text{R}65").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Fixed costs ignore output: rent R3 000,").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("supervisor R2 000 — R6 000 stands still").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("Per unit, fixed cost FALLS as output rises").scale(1.0).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the scale effect at three volumes
        self.next_band(5)
        b5_title = Tex("What volume does to the unit cost").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"400: \; 65 + \tfrac{6\,000}{400} = 65 + 15 = \text{R}80").scale(1.0).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"500: \; 65 + \tfrac{6\,000}{500} = 65 + 12 = \text{R}77").scale(1.0).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Cheaper per shirt — the fixed costs spread wider").scale(1.0).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.wait(2.5)
        b5_l4 = MathTex(r"200: \; 65 + \tfrac{6\,000}{200} = 65 + 30 = \text{R}95").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Quiet months hurt more than they seem").scale(1.0).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): classification and the cost statement
        self.next_band(6)
        b6_title = Tex("Exam shapes I: classify, then state").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Every cost carries BOTH labels:").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("fabric — direct AND variable;").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("rent — overhead AND fixed").scale(1.0).shift(band_shift(6) + DOWN * 0.3)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = MathTex(r"16\,000 + 10\,000 = 26\,000; \;\; + 6\,000 = 32\,000").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = MathTex(r"\frac{32\,000}{400} = \text{R}80 \text{ — labelled lines, in order}").scale(0.95).shift(band_shift(6) + DOWN * 2.4)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the what-if and the decision comment
        self.next_band(7)
        b7_title = Tex("Exam shapes II: what-if, then advise").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_wrong = MathTex(r"\text{At } 500: \text{ rent} \times \tfrac{5}{4} \text{ (scaling the fixed!)}").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2.5)
        b7_l1 = MathTex(r"500: \; 20\,000 + 12\,500 = 32\,500 \text{ prime}").scale(0.95).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"+ 6\,000 = 38\,500; \quad \frac{38\,500}{500} = \text{R}77").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Variables scale; fixeds stand").scale(1.05).shift(band_shift(7) + DOWN * 1.9)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("Advise in four moves: state, judge, explain, recommend").scale(0.9).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): cooking for the wedding
        self.next_band(8)
        b8_title = Tex("Cooking for the wedding").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("400 vetkoek: flour and oil in each one — direct").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex("The cousin paid to fry — direct labour").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Gas, soap, pot-wear, the pot-watcher —").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex("costs of keeping the kitchen cooking: overheads").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Taxi fare to deliver: outside the kitchen fence").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("One question: can I point at ONE unit?").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_6): what one vetkoek costs
        self.next_band(9)
        b9_title = Tex("What one vetkoek costs").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\text{Direct: } 2 + 1 = \text{R}3; \;\; 400 \times 3 = 1\,200").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{Overheads: } 300 + 60 + 240 = 600").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"\text{Total } 1\,800; \quad \frac{1\,800}{400} = \text{R}4{,}50").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Sell at R6: clears R1,50. At R4: a 50c loss").scale(1.0).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("The unit cost is the floor under the price").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the rent doesn't care how busy you are
        self.next_band(10)
        b10_title = Tex("The rent doesn't care how busy you are").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"400 \text{ units: } \tfrac{600}{400} = 1{,}50 \;\Rightarrow\; \text{R}4{,}50").scale(0.88).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"600 \text{ units: } \tfrac{600}{600} = 1{,}00 \;\Rightarrow\; \text{R}4{,}00").scale(0.88).shift(band_shift(10) + UP * 0.1)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"200 \text{ units: } \tfrac{600}{200} = 3{,}00 \;\Rightarrow\; \text{R}6{,}00").scale(0.88).shift(band_shift(10) + DOWN * 0.9)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("Busyness itself makes every unit cheaper").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2)
        b10_l5 = Tex("Standing costs are a drumbeat — match your volume").scale(0.95).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10_l5))
        self.wait(4)
