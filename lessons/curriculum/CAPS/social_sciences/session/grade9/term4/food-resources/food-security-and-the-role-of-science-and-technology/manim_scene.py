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


class FoodSecurityAndTheRoleOfScienceAndTechnologySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): What Food Security Means
        title = Tex('Food security').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Enough safe, nutritious food').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('For all people, at all times').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Availability and access').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Utilisation and stability').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Food Security in the World and in South Africa
        self.next_band(1)
        b1_title = Tex('World and South Africa').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Enough food, yet millions hungry').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('SA: one in five households struggle').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('About 27\\% of young children stunted').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Grants and school meals help').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Science, Technology and the Green Revolution
        self.next_band(2)
        b2_title = Tex('Science and the Green Revolution').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Tractors, fertiliser, irrigation').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Borlaug's high-yield wheat").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('India avoids famine').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Precision farming today').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Benefits and Costs of Technology, and the Error Museum
        self.next_band(3)
        b3_title = Tex('Benefits and costs').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('More food per person').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Polluted rivers and dams').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Fewer farm jobs, more debt').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Sustainable intensification').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Benefits and Costs of Technology, and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Enough food means no hunger''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Calories are all that matter''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The Green Revolution was all good''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Hunger means a world shortage''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Full Shop and an Empty Pocket
        self.next_band(5)
        b5_title = Tex('A full shop and an empty pocket').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Our farms grow enough').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Many families can't afford it").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Children who don't grow tall").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Everyone must get healthy food').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Four-Legged Table
        self.next_band(6)
        b6_title = Tex('A four-legged table').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Enough food grown').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Able to get it').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Using it well').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Steady every day').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Magic Seed With a Price Tag
        self.next_band(7)
        b7_title = Tex('A magic seed with a price tag').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('New wheat feeds millions').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Tractors and fertiliser').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Pollution and lost jobs').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Poor farmers left behind').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
