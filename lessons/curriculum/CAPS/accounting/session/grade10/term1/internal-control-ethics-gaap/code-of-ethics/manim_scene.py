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

# Band-layout whiteboard scene for the session duo "Code of Ethics"
# (grade10 term1, internal-control-ethics-gaap). One band per teaching beat,
# camera moves down to fresh space, nothing is ever removed. Exporter-safe
# vocabulary only: Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup,
# single-string Tex lines revealed with Write — no sub-part transforms.
#
# Subtopic time shares (subtopics.json, total 1240 s):
# 170/190/190/170/170/180/170 -> bands 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CodeOfEthicsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): what a code of ethics is ---
        title = Tex("The Code of Ethics").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Money concentrates temptation").scale(1.1).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("A formal statement of the values and").scale(1.1).shift(UP * 0.3)
        b0_l3 = Tex("standards of behaviour a business").scale(1.1).shift(DOWN * 0.5)
        b0_l4 = Tex("commits itself to").scale(1.1).shift(DOWN * 1.3)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(VGroup(b0_l2, b0_l3, b0_l4), color=GREEN)))
        self.wait(2.5)
        b0_l5 = Tex("Binds ALL parties: owners, managers,").scale(1.05).shift(DOWN * 2.2)
        b0_l6 = Tex("bookkeepers, employees, suppliers, state").scale(1.05).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): trust is the precondition ---
        self.next_band(1)
        b1_title = Tex("Why Accounting demands it").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Financial information has value").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("only if it can be TRUSTED").scale(1.1).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Controls make dishonesty difficult;").scale(1.1).shift(band_shift(1) + DOWN * 0.9)
        b1_l4 = Tex("ethics makes it unwanted").scale(1.1).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Two hands of the same grip").scale(1.1).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.play(Create(SurroundingRectangle(b1_l5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): characteristics 1-4 ---
        self.next_band(2)
        b2_title = Tex("The seven characteristics (1--4)").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("1. Leadership -- the example from the top").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("2. Discipline -- the rules, every time").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = Tex("3. Transparency -- open, visible records").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        b2_l4 = Tex("4. Accountability -- answer for actions").scale(1.05).shift(band_shift(2) + DOWN * 1.6)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Definition + one-line example = the marks").scale(1.0).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): characteristics 5-7 + overlaps ---
        self.next_band(3)
        b3_title = Tex("The seven characteristics (5--7)").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("5. Fairness -- all parties treated justly").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("6. Sustainability -- profit today must").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex("not destroy profit tomorrow").scale(1.05).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex("7. Responsible management -- careful").scale(1.05).shift(band_shift(3) + DOWN * 1.5)
        b3_l5 = Tex("stewardship of the business's resources").scale(1.05).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex("Overlaps happen -- choose the BEST fit").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): scenario one, worked in full ---
        self.next_band(4)
        b4_title = Tex("Scenario 1: cash sales left out").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Leave some cash sales out of the").scale(1.05).shift(band_shift(4) + UP * 1.1)
        b4_l2 = Tex("records to reduce tax''").scale(1.05).shift(band_shift(4) + UP * 0.3)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2)
        b4_l3 = Tex("Owner: fails leadership and fairness").scale(1.05).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex("Bookkeeper: fails discipline and").scale(1.05).shift(band_shift(4) + DOWN * 1.4)
        b4_l5 = Tex("accountability").scale(1.05).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex("False in one place = untrusted everywhere").scale(1.0).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l6))
        self.play(Create(SurroundingRectangle(b4_l6, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): scenarios two and three ---
        self.next_band(5)
        b5_title = Tex("Scenarios 2 and 3").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Expired stock sold without disclosure:").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("transparency and fairness fail").scale(1.05).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Waste dumped in the river:").scale(1.05).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = Tex("sustainability fails, with responsible").scale(1.05).shift(band_shift(5) + DOWN * 1.4)
        b5_l5 = Tex("management and leadership implicated").scale(1.05).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("The trade: small gain now, big loss later").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the four-move method ---
        self.next_band(6)
        b6_title = Tex("The four-move exam method").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("1. Identify the issue in plain words").scale(1.1).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("2. NAME the characteristic at stake").scale(1.1).shift(band_shift(6) + UP * 0.2)
        b6_l3 = Tex("3. Argue the link: definition to facts").scale(1.1).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = Tex("4. Consequence and correction").scale(1.1).shift(band_shift(6) + DOWN * 1.6)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.wait(2)
        self.play(Write(b6_l3))
        self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(VGroup(b6_l1, b6_l2, b6_l3, b6_l4), color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the two mark-losing errors ---
        self.next_band(7)
        b7_title = Tex("Two errors that cost marks").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_w1 = Tex("``This is wrong and bad''").scale(1.1).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_w1))
        self.play(Create(strike(b7_w1)))
        b7_e1 = Tex("moralising without naming = nothing").scale(1.0).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7_e1))
        self.wait(2.5)
        b7_w2 = Tex("``transparency, accountability, fairness''").scale(1.05).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_w2))
        self.play(Create(strike(b7_w2)))
        b7_e2 = Tex("a shopping list of names earns little").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        self.play(Write(b7_e2))
        self.wait(2.5)
        b7_ok = Tex("Name it, define it, tie it to the facts").scale(1.05).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_ok))
        self.play(Create(SurroundingRectangle(b7_ok, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the captain picture ---
        self.next_band(8)
        b8_title = Tex("The Captain Picture").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Trains hardest -- leadership").scale(1.0).shift(band_shift(8) + UP * 1.2 + LEFT * 3.0)
        b8_l2 = Tex("On time, every time -- discipline").scale(1.0).shift(band_shift(8) + UP * 0.4 + LEFT * 3.0)
        b8_l3 = Tex("Open selections -- transparency").scale(1.0).shift(band_shift(8) + DOWN * 0.4 + LEFT * 3.0)
        b8_l4 = Tex("Takes the blame -- accountability").scale(0.95).shift(band_shift(8) + DOWN * 1.2 + LEFT * 3.0)
        b8_r1 = Tex("Equal chances -- fairness").scale(1.0).shift(band_shift(8) + UP * 1.2 + RIGHT * 3.3)
        b8_r2 = Tex("Never cheats -- sustainability").scale(1.0).shift(band_shift(8) + UP * 0.4 + RIGHT * 3.3)
        b8_r3 = Tex("Minds the kit -- responsible").scale(1.0).shift(band_shift(8) + DOWN * 0.4 + RIGHT * 3.3)
        b8_r4 = Tex("management").scale(1.0).shift(band_shift(8) + DOWN * 1.1 + RIGHT * 3.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(1.5)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(1.5)
        self.play(Write(b8_r1))
        self.play(Write(b8_r2))
        self.wait(1.5)
        self.play(Write(b8_r3))
        self.play(Write(b8_r4))
        self.wait(1.5)
        b8_box = Tex("One captain, seven characteristics").scale(1.05).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_box))
        self.play(Create(SurroundingRectangle(b8_box, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): ethics at the till ---
        self.next_band(9)
        b9_title = Tex("Ethics at the Till").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Wrong change returned, till checked:").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex("accountability, fairness, transparency").scale(1.05).shift(band_shift(9) + UP * 0.3)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("``Cash price, no paper'': transparency").scale(1.05).shift(band_shift(9) + DOWN * 0.6)
        b9_l4 = Tex("and accountability traded away").scale(1.05).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Stock off a truck: sustainability says NO").scale(1.0).shift(band_shift(9) + DOWN * 2.2)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("The shop's real asset is trust").scale(1.05).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): good ethics is good business ---
        self.next_band(10)
        b10_title = Tex("Good ethics is good business").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Fairness $\Rightarrow$ loyal customers").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex(r"Honest records $\Rightarrow$ bank loans").scale(1.05).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex(r"Paying on time $\Rightarrow$ credit in hard months").scale(1.0).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2)
        b10_l4 = Tex("One dishonesty makes every figure suspect").scale(1.0).shift(band_shift(10) + DOWN * 1.6)
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Ethics protects the business AND").scale(1.05).shift(band_shift(10) + DOWN * 2.3)
        b10_l6 = Tex("earns it the profits of being trusted").scale(1.05).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(VGroup(b10_l5, b10_l6), color=GREEN)))
        self.wait(4)
