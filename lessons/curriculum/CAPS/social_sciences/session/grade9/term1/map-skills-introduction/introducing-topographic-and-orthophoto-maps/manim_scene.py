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


class IntroducingTopographicAndOrthophotoMapsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Grade 9 Geography and How It Is Assessed
        title = Tex('Grade 9 Geography').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Term 1 maps; Term 2 development; Term 3 rivers; Term 4 resources').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Tests: 50, 75, 50 and an exam of 75 marks').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Source-based questions and paragraph writing').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Answer the question; show the working; give the unit').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): What a Topographic Map Is
        self.next_band(1)
        b1_title = Tex('The 1:50 000 topographic map').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('A drawing from above, with symbols and a key').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('1 cm = 50 000 cm = 500 m, so 2 cm = 1 km').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Contours in brown at a 20 m interval').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Sheet 2628AB: 26 deg S, 28 deg E, then quarter A, part B').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): What an Orthophoto Map Is
        self.next_band(2)
        b2_title = Tex('The 1:10 000 orthophoto map').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Vertical aerial photograph, corrected to a uniform scale').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('1 cm = 10 000 cm = 100 m, so 10 cm = 1 km').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Contours at a 5 m interval, names and a grid printed on').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('25 orthophoto sheets fit in one topographic sheet').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Comparing the Two Maps and the Error Museum
        self.next_band(3)
        b3_title = Tex('Comparing the two maps').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Topographic: small scale, large area, less detail').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Orthophoto: large scale, small area, more detail').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Long distances and relief: topographic map').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Houses, fields and river bends: orthophoto').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Comparing the Two Maps and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``1:50 000 is the larger scale''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``An orthophoto is just a photograph''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Both maps have 20 m contours''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``A large-scale map covers a large area''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Standing on the Hill Above Town
        self.next_band(5)
        b5_title = Tex('Standing on the hill above town').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Geography studies the land and what people do with it').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('The topographic map is a careful drawing from above').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Symbols: blue river, black buildings, brown contours').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Two centimetres on the map is one kilometre').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Phone Camera Pointed Straight Down
        self.next_band(6)
        b6_title = Tex('The phone camera pointed straight down').scale(1.0).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Straight down: vertical. At an angle: oblique.').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Hilltops look bigger, edges lean: the photo must be corrected').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Corrected photo plus names and contours: the orthophoto').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('One centimetre is 100 metres: count the houses').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Drawing Pinned Next to the Photograph
        self.next_band(7)
        b7_title = Tex('The drawing next to the photograph').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Drawing: zoomed out, big area, less detail').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Photograph: zoomed in, small area, more detail').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Zoomed in means LARGER scale').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Big jobs: topographic map. Close-ups: orthophoto.').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
