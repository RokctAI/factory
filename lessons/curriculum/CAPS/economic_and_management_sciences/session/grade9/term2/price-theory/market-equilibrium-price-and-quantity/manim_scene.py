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
# dwell time proportional to subtopics.json (210/230/230/250/180/180/180 of
# 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MarketEquilibriumSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Combining Demand and Supply in One Schedule
        b0_title = Tex("One combined schedule").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("R20: D 50, S 200 (surplus 150)").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("R16: D 80, S 160 (surplus 80)").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("R12: D 120, S 120").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("R8: shortage 90; R4: shortage 200").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Equilibrium Price and Equilibrium Quantity
        self.next_band(1)
        b1_title = Tex("Equilibrium").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Quantity demanded = quantity supplied").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Pe = R12, Qe = 120").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("D and S cross at E").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("12 x 120 = 1 440 rand").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Surpluses, Shortages and How the Market Clears
        self.next_band(2)
        b2_title = Tex("Surplus and shortage").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Above equilibrium: surplus").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Surplus pushes price down").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Below equilibrium: shortage").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Ceiling below Pe: lasting shortage").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Changes in Demand and Supply Move the Equilibrium
        self.next_band(3)
        b3_title = Tex("Shifts move the equilibrium").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Demand up: R16, 160").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Supply down: R16, 80").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Demand moves: P and Q together").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Supply moves: P opposite to Q").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Changes in Demand and Supply Move the Equilibrium
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Price change shifts the curve''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Equilibrium is a fair price''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Surplus below equilibrium''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Less supply lowers the price''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Where the Slide Meets the Ladder
        self.next_band(5)
        b5_title = Tex("Slide meets ladder").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Cross at R12 and 120").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Mark E, dotted lines").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Nobody decided R12").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Equilibrium is not affordability").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=GREEN)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Too Many Muffins or Too Few
        self.next_band(6)
        b6_title = Tex("Too many or too few").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("R16: 160 - 80 = 80 left over").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Leftovers: price falls").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("R8: 170 - 80 = 90 short").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Queues: price rises").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Four Moves to Remember
        self.next_band(7)
        b7_title = Tex("Four moves").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Demand up: P up, Q up").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Demand down: P down, Q down").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Supply down: P up, Q down").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Supply up: P down, Q up").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
