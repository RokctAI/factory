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


class VerticalAerialPhotographsAndOrthophotoImagesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Aerial Photographs: Vertical and Oblique
        title = Tex('Aerial photographs').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Taken in overlapping strips: about 60 percent forward overlap').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Vertical: camera straight down, plan view, used for maps').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Low oblique: tilted, no horizon. High oblique: horizon.').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Obliques cannot be measured: scale changes').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): From Photograph to Orthophoto
        self.next_band(1)
        b1_title = Tex('From photograph to orthophoto').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Relief displacement, tilt and lens distortion').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Orthorectification: a uniform scale everywhere').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('1:10 000: 1 cm = 100 m; 5 m contours').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Names, spot heights and a co-ordinate frame printed on').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Reading the Image: Tone, Texture, Shape and More
        self.next_band(2)
        b2_title = Tex('Reading the image').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Tone, texture, shape, size, pattern, shadow, association').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Circles on farmland: centre-pivot irrigation').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Neat rows: formal suburb. Packed tiny roofs: informal.').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Midday shadows in South Africa fall south').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Land Use on the Orthophoto and the Error Museum
        self.next_band(3)
        b3_title = Tex('Land use on the orthophoto').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('CBD: large buildings packed close, dense streets').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Industry: long sheds beside the railway sidings').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Name the land use, its location and two clues').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Measure: a 4 cm circle is 400 m across').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Land Use on the Orthophoto and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Oblique photos are good for measuring''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``An orthophoto is a raw photograph''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Circles on farms are rings of trees''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Shadows in South Africa fall north at midday''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Drone Over Your Neighbourhood
        self.next_band(5)
        b5_title = Tex('The drone over your neighbourhood').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Straight down: vertical. Slanted: oblique.').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Oblique with sky: high. Without: low.').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Measure only on the straight-down photo').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('A photo shows land use but no names or heights').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Straightening the Wobbly Photo
        self.next_band(6)
        b6_title = Tex('Straightening the wobbly photo').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Hills look bigger; tall things lean').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('A computer straightens it: the orthophoto').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Names, 5 m contours and a grid printed on top').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('1 cm = 100 m; 25 sheets in one topographic sheet').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Spot the Difference
        self.next_band(7)
        b7_title = Tex('Spot the difference').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Dark or light? Smooth or rough? Shape? Size?').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Pattern? Shadow? What is next to it?').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Green circles: crops under centre-pivot irrigation').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Shadows point south in South Africa').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
