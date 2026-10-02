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
# dwell time proportional to subtopics.json (210/230/230/220/180/190/180 of
# 1440 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CircularFlowDiagramSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Real Flows and Money Flows
        b0_title = Tex("Real flows and money flows").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Real: factors, goods and services").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Money: income and spending").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Always opposite directions").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Money lets us add it all up").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Drawing the Two-Sector Circular Flow Diagram
        self.next_band(1)
        b1_title = Tex("Two-sector diagram").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Households left, businesses right").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Goods market top, factor market bottom").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Factors in, rent, wages, interest, profit out").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Goods out, spending in").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Adding the Government to the Diagram
        self.next_band(2)
        b2_title = Tex("Adding government").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Buys labour: salaries").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Buys goods and services").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Taxes: direct arrows in").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Grants: direct arrows out").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Leakages, Injections and Keeping the Flow Steady
        self.next_band(3)
        b3_title = Tex("Leakages and injections").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Leakages: savings, taxes").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Injections: investment, government").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("1 000 - 200 - 100 = 700").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("700 + 100 + 200 = 1 000").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Leakages, Injections and Keeping the Flow Steady
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Real and money flows run the same way''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Taxes pass through a market''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Saving is an injection''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("An arrow with no label").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Two Rivers Flowing in Opposite Directions
        self.next_band(5)
        b5_title = Tex("Two rivers").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Work out, wages in").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Shoes in, money out").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Taxes and grants: one way").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Count the money river").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Building the Diagram Step by Step
        self.next_band(6)
        b6_title = Tex("Draw it step by step").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("1. Households and businesses").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("2. Goods market and factor market").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("3. Things river; 4. money river").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("5. Government; label every arrow").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Leaks and Taps in the Pipe
        self.next_band(7)
        b7_title = Tex("Leaks and taps").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Leaks: saving, tax (300)").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Taps: investment, government (300)").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Equal: steady flow").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Leaks win: recession").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(4)
