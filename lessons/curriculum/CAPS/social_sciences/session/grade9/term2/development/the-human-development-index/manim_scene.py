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
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheHumanDevelopmentIndexSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Why the HDI Was Created and Its Three Dimensions
        title = Tex('Why the HDI?').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('UNDP, 1990: ul Haq and Sen').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Income is a means, not the goal').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Health, knowledge, living standard').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Four indicators, three dimensions').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Calculating the HDI Step by Step
        self.next_band(1)
        b1_title = Tex('Calculating the HDI').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('(actual - min) / (max - min)').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Health: (65 - 20) / (85 - 20) = 0,692').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Education 0,764; income 0,746').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Cube root of the product: about 0,734').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Reading HDI Categories, Rankings and Maps
        self.next_band(2)
        b2_title = Tex('Reading the HDI').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Very high 0,800+; high 0,700-0,799').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Medium 0,550-0,699; low below 0,550').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Switzerland above 0,95; Somalia below 0,40').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('South Africa about 0,72, near 110th').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Limitations of the HDI, Related Indices and the Error Museum
        self.next_band(3)
        b3_title = Tex('Limitations and the IHDI').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('An average hides inequality').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('South Africa: a large inequality loss').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Years in school, not quality').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Leaves out environment and freedom').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Limitations of the HDI, Related Indices and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The HDI measures income only''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``The three indices are added''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``0,72 means 72 per cent developed''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``High HDI means everyone lives well''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Three-Part Test
        self.next_band(5)
        b5_title = Tex('A three-part test').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Do people live long and healthy lives?').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Do they get knowledge?').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Do they have a decent living?').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Money alone is not enough').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Recipe for One Score
        self.next_band(6)
        b6_title = Tex('A recipe for one score').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Each answer becomes 0 to 1').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('65 years gives about 0,69').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Multiply, then cube root').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Example: about 0,73').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The League Table
        self.next_band(7)
        b7_title = Tex('The league table').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Four groups from very high to low').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Switzerland, Norway at the top').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('South Africa high, about 0,72').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Adjust for inequality: it drops').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
