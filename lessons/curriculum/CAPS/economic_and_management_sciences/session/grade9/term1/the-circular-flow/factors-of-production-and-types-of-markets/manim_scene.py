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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex keep the export to the
# allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/210/230/210/190/180/190 of
# 1430 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FactorsAndMarketsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Four Factors of Production
        b0_title = Tex("Factors of production").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Natural resources: land, minerals, water").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Labour: human effort and skill").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Capital: machines, tools, buildings").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Entrepreneurship: organises, takes risk").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Rewards for the Factors of Production
        self.next_band(1)
        b1_title = Tex("Rewards").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Natural resources earn rent").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Labour earns wages and salaries").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Capital earns interest").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Entrepreneurship earns profit").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_2): Rewards for the Factors of Production
        self.next_band(2)
        b2_title = Tex("A bakery's profit").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Sales R50 000").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Less rent, wages, interest, ingredients").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("50 000 - 8 000 - 22 000 - 2 000 - 12 000").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Profit = R6 000").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2)

        # --- Band 3 (subtopic_3): What a Market Is and the Main Types of Markets
        self.next_band(3)
        b3_title = Tex("Types of markets").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Goods and services: households buy").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Factor market: households sell").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Financial: money and capital markets").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("JSE: shares; forex: currencies").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Markets by Place, Reach and Time
        self.next_band(4)
        b4_title = Tex("More ways to sort markets").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Physical or virtual").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("Local, national, international").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("Formal or informal").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("Many sellers or a monopoly").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b4_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 5 (subtopic_4): Markets by Place, Reach and Time
        self.next_band(5)
        b5_title = Tex("Error museum").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("``Capital means money''").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("``Profit is the reward for labour''").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("``A market must be a place''").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("``Households buy in the factor market''").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): Making a Batch of Vetkoek
        self.next_band(6)
        b6_title = Tex("A batch of vetkoek").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Flour, oil, water: natural resources").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("You and your cousin: labour").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Pot and burner: capital").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("The one who takes the risk").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_6): Who Gets Paid What
        self.next_band(7)
        b7_title = Tex("Who gets paid what").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Landowner: rent").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Worker: wages").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Lender: interest (R550 - R500 = R50)").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Entrepreneur: profit").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 8 (subtopic_7): Where Things Are Bought and Sold
        self.next_band(8)
        b8_title = Tex("Where things are sold").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Goods market: families buy").scale(0.9).shift(band_shift(8) + UP * 1.30)
        b8_l2 = Tex("Factor market: families sell").scale(0.9).shift(band_shift(8) + UP * 0.35)
        b8_l3 = Tex("Financial market: save and borrow").scale(0.9).shift(band_shift(8) + DOWN * 0.60)
        b8_l4 = Tex("Local, national, international").scale(0.9).shift(band_shift(8) + DOWN * 1.55)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b8_l2, color=YELLOW)))
        self.wait(4)
