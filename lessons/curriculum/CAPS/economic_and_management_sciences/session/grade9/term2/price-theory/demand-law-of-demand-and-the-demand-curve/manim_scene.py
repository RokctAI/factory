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
# dwell time proportional to subtopics.json (200/220/240/240/180/190/180 of
# 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DemandCurveSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): What Demand Means
        b0_title = Tex("Demand").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Willing and able to buy").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("At each price, over a period").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Market demand: add all buyers").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("2 + 1 + 0 = 3 at R12").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Law of Demand and Why It Holds
        self.next_band(1)
        b1_title = Tex("Law of demand").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Price up: quantity demanded down").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Ceteris paribus").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Substitution and income effects").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Diminishing marginal utility").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Demand Schedule and Drawing the Demand Curve
        self.next_band(2)
        b2_title = Tex("Schedule and curve").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("R20: 50; R16: 80; R12: 120").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("R8: 170; R4: 230").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Price on vertical axis").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Curve D slopes downward").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Movements Along and Shifts of the Demand Curve
        self.next_band(3)
        b3_title = Tex("Movement or shift?").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Own price: movement along D").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Other factors: shift of D").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Income, related goods, tastes").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Population, expectations, policy").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Movements Along and Shifts of the Demand Curve
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Lower price increases demand''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Demand slopes upward''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Quantity on the vertical axis''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Cars and petrol are substitutes''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Muffins at the Tuck Shop
        self.next_band(5)
        b5_title = Tex("Muffins at the tuck shop").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("R20: 50 a day").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("R12: 120 a day").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("R4: 230 a day").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Want plus money = demand").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Plotting the Points
        self.next_band(6)
        b6_title = Tex("Plotting the points").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Price up the side").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Quantity along the bottom").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Dots make a slide down").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("20 x 50 = 1 000 rand").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Sliding or Jumping?
        self.next_band(7)
        b7_title = Tex("Slide or jump?").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Own price changes: slide").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("New school opens: jump right").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Health warning: jump left").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Anything else: jump").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
