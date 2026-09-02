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
# "Manufacturing Concepts and Basic Cost Calculations". Add-only lifecycle,
# one band per teaching beat, camera moves down between bands. Covers all
# seven subtopics: Part 1 Expert (subtopics 1-4), Part 2 Simplifier
# (subtopics 5-7). subtopics.json durations 220/220/220/220/180/190/190 of
# 1440 s. The stool workshop's layered cost statement and the samoosa order
# are built line by line, volumes rerun with fixeds standing.

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
        title = Tex("Manufacturing Costs — the Two Sortings").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Sorting one: traceable to ONE unit?").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2.5)
        b0_l2 = Tex("Direct materials: timber, R60 per stool").scale(1.0).shift(UP * 0.3)
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Direct labour: the carpenter, R30 per stool").scale(1.0).shift(DOWN * 0.6)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Traceable — the work IS the stool").scale(1.0).shift(DOWN * 1.6)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the indirect family and the factory fence
        self.next_band(1)
        b1_title = Tex("The indirect family — FACTORY OVERHEADS").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(2)
        b1_l1 = Tex("Indirect materials: glue, sandpaper, blades").scale(1.0).shift(band_shift(1) + UP * 1.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Indirect labour: the foreman, serving every stool").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l2))
        self.wait(2)
        b1_l3 = Tex("Rent, electricity, machine depreciation").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_wrong = Tex("The sales assistant as a production cost").scale(1.0).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l4 = Tex("The factory fence: count only inside it").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        self.play(Write(b1_l4))
        self.wait(3)

        # --- Band 2 (subtopic_2): prime cost, computed
        self.next_band(2)
        b2_title = Tex("Layer one — PRIME COST").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = MathTex(r"\text{Materials: } 300 \times 60 = 18\,000").scale(1.0).shift(band_shift(2) + UP * 1.0)
        self.play(Write(b2_l1))
        self.wait(2.5)
        b2_l2 = MathTex(r"\text{Labour: } 300 \times 30 = 9\,000").scale(1.0).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = MathTex(r"\text{Prime cost: } 18\,000 + 9\,000 = 27\,000").scale(1.05).shift(band_shift(2) + DOWN * 0.9)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex("Prime — first: the costs that touch the product").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): total production cost and the unit cost
        self.next_band(3)
        b3_title = Tex("Layers two and three").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(2)
        b3_l1 = Tex("Overheads: rent 4 200, foreman 2 400,").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("electricity 900, glue and blades 900 — R8 400").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"\text{Total production: } 27\,000 + 8\,400 = 35\,400").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = MathTex(r"\text{Unit cost: } 35\,400 \div 300 = \text{R}118").scale(1.05).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2.5)
        b3_l5 = Tex("Half-assembled at month-end: work-in-progress").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_3): fixed and variable behaviour
        self.next_band(4)
        b4_title = Tex("Sorting two — how costs BEHAVE").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2)
        b4_l1 = Tex("Variable: total moves with output,").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("per unit stands still — R90 per stool").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Fixed: total stands still — R8 400 —").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        b4_l4 = Tex("per unit falls as output rises").scale(1.0).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("The rent is the same in a busy or idle month").scale(0.95).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the scale effect at three volumes
        self.next_band(5)
        b5_title = Tex("The unit cost at three volumes").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(2)
        b5_l1 = MathTex(r"300: \; 90 + \tfrac{8\,400}{300} = 90 + 28 = 118").scale(1.0).shift(band_shift(5) + UP * 1.0)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = MathTex(r"400: \; 90 + \tfrac{8\,400}{400} = 90 + 21 = 111").scale(1.0).shift(band_shift(5) + UP * 0.0)
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = MathTex(r"150: \; 90 + \tfrac{8\,400}{150} = 90 + 56 = 146").scale(1.0).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=RED)))
        self.wait(2.5)
        b5_l4 = Tex("Busy months spread the rent thinner").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): classification and the cost statement
        self.next_band(6)
        b6_title = Tex("The assessment shapes").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Classify: every cost wears BOTH labels —").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("timber: direct AND variable; rent: overhead AND fixed").scale(0.9).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Statement: prime; plus overheads — total;").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("over units — unit cost, labelled lines in order").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = MathTex(r"18\,000 + 9\,000 \to 27\,000;\; +8\,400 \to 35\,400;\; \div 300 \to 118").scale(0.85).shift(band_shift(6) + DOWN * 2.3)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the what-if and the decision comment
        self.next_band(7)
        b7_title = Tex("The what-if — variables scale, fixeds stand").scale(1.05).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_wrong = Tex("Stretching the rent because output rose").scale(1.0).shift(band_shift(7) + UP * 1.2)
        self.play(Write(b7_wrong))
        self.play(Create(strike(b7_wrong)))
        self.wait(2)
        b7_l1 = MathTex(r"400: \; 24\,000 + 12\,000 = 36\,000;\; +8\,400 = 44\,400").scale(0.9).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.wait(2.5)
        b7_l2 = MathTex(r"44\,400 \div 400 = \text{R}111").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex("Comment in four moves: state, judge,").scale(1.0).shift(band_shift(7) + DOWN * 1.7)
        b7_l4 = Tex("explain, recommend").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): cooking for the function
        self.next_band(8)
        b8_title = Tex("Cooking for the function").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Pastry and filling — inside each samoosa: direct").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Gas, pot wear, the pot-watcher: overheads —").scale(0.95).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex("the cost of keeping the kitchen cooking").scale(0.95).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex("Taxi fare to deliver: outside the kitchen fence").scale(0.95).shift(band_shift(8) + DOWN * 1.5)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("One pointing question sorts everything").scale(1.0).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): what one samoosa costs
        self.next_band(9)
        b9_title = Tex("What one samoosa costs").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = MathTex(r"\text{Prime: } 500 \times 4 = 2\,000").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = MathTex(r"\text{Overheads: } 450 + 50 + 250 = 750").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = MathTex(r"2\,750 \div 500 = \text{R}5{,}50").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Sell at R8: clears R2,50 each — R1 250 the order;").scale(0.9).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = Tex("at R5: a 50c loss on every single one").scale(0.95).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_7): the rent doesn't care how busy you are
        self.next_band(10)
        b10_title = Tex("The rent doesn't care how busy you are").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = MathTex(r"500: \; \tfrac{750}{500} = 1{,}50 \;\to\; 5{,}50").scale(0.95).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = MathTex(r"750: \; \tfrac{750}{750} = 1{,}00 \;\to\; 5{,}00").scale(0.95).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = MathTex(r"150: \; \tfrac{750}{150} = 5{,}00 \;\to\; 9{,}00").scale(0.95).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=RED)))
        self.wait(2.5)
        b10_l4 = Tex("Standing costs are a drumbeat:").scale(1.0).shift(band_shift(10) + DOWN * 1.8)
        b10_l5 = Tex("match your volume to it").scale(1.0).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(4)
