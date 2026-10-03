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
# dwell time proportional to subtopics.json (230/240/240/240/180/180/180 of
# 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TradeUnionEffectsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Positive Effects of Trade Unions on Businesses
        b0_title = Tex("Good for business").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("One partner to negotiate with").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Grievances solved early").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Better morale, lower turnover").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Safety and training").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_1): Positive Effects of Trade Unions on Businesses
        self.next_band(1)
        b1_title = Tex("Turnover costs money").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("5 workers leave").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("R6 000 to replace each").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("5 x 6 000 = R30 000").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Stable staff saves this").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_2): Negative Effects of Trade Unions on Businesses
        self.next_band(2)
        b2_title = Tex("The cost side").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("6\% of R8 000 = R480").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("40 x 480 = R19 200 a month").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Strike: 60 000 x 10 = R600 000").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Worker loses R400 a day").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_3): Trade Unions and Sustainable Economic Growth
        self.next_band(3)
        b3_title = Tex("Sustainable growth").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Fair share of the benefits").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Skills and productivity").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Social dialogue at NEDLAC").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Decent work, just transition").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Weighing the Effects: Wages, Productivity and Jobs
        self.next_band(4)
        b4_title = Tex("Wages and productivity").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Wages up 6\%").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("Output 200 to 212 cases").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("(212 - 200) x 100 / 200 = 6\%").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("Cost per case stays the same").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)

        # --- Band 5 (subtopic_4): Weighing the Effects: Wages, Productivity and Jobs
        self.next_band(5)
        b5_title = Tex("Error museum").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("``Unions only cost money''").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("``Protected strikes allow violence''").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("``Higher wages always create jobs''").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("``Give only one side in an essay''").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): Good for Business Too
        self.next_band(6)
        b6_title = Tex("Good for business too").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("One deal, not 40 arguments").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Complaints solved early").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Workers stay longer").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Safer, better trained").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=GREEN)))
        self.wait(2)

        # --- Band 7 (subtopic_6): When Things Go Wrong
        self.next_band(7)
        b7_title = Tex("When things go wrong").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Higher wage bill").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Strike: R600 000 lost").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("No work, no pay").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Violence is never legal").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 8 (subtopic_7): Growing Together
        self.next_band(8)
        b8_title = Tex("Growing together").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Growth that lasts").scale(0.9).shift(band_shift(8) + UP * 1.30)
        b8_l2 = Tex("Wages and output rise together").scale(0.9).shift(band_shift(8) + UP * 0.35)
        b8_l3 = Tex("Talk at NEDLAC").scale(0.9).shift(band_shift(8) + DOWN * 0.60)
        b8_l4 = Tex("Strikes as the last step").scale(0.9).shift(band_shift(8) + DOWN * 1.55)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(4)
