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
# dwell time proportional to subtopics.json (220/230/230/230/180/180/190 of
# 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SectorLinksSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Value Chain: How Sectors Feed Each Other
        b0_title = Tex("The value chain").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Cotton: R10 (primary)").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Factory: 60 - 10 = 50 added").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Shop: 120 - 60 = 60 added").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("10 + 50 + 60 = 120").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)

        # --- Band 1 (subtopic_2): How Each Sector Depends on the Others
        self.next_band(1)
        b1_title = Tex("Each sector depends on the others").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Primary needs machines, transport, banks").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Secondary needs raw materials, shops").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Tertiary needs goods to sell").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Government: roads, ports, skills").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Role of Each Sector in the South African Economy
        self.next_band(2)
        b2_title = Tex("Roles in South Africa").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Primary: raw materials, food, exports").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Secondary: value added, infrastructure").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Tertiary: largest employer and GDP").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Together: output, jobs, exports").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): When One Sector Struggles: Ripple Effects
        self.next_band(3)
        b3_title = Tex("Ripple effects").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Drought: farms, mills, shops").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Mine closure: suppliers, town").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Load-shedding: every sector").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("New plant: income spreads out").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): When One Sector Struggles: Ripple Effects
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Services don't need the others''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Mining problems hit only miners''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Add full prices along the chain''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``The sectors compete''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Journey of a T-shirt
        self.next_band(5)
        b5_title = Tex("Journey of a T-shirt").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Farm R10").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Factory R60").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Shop R120").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Every link is someone's job").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Everyone Needs Everyone
        self.next_band(6)
        b6_title = Tex("Everyone needs everyone").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Farm needs tractor and truck").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Factory needs cotton and shops").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Shop needs goods and power").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Let go and the circle breaks").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): When the Mine Closes
        self.next_band(7)
        b7_title = Tex("When the mine closes").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Miners lose jobs: primary").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Boot factory loses work: secondary").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Shops and taxis suffer: tertiary").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Ripples spread both ways").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(4)
