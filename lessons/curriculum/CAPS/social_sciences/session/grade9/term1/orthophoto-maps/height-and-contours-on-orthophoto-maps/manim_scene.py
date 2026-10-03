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


class HeightAndContoursOnOrthophotoMapsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Height Information on the Orthophoto Map
        title = Tex('Height on the orthophoto').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Contours every 5 m, printed over the photograph').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Every fourth contour matches a 20 m topographic contour').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Spot heights and trig stations, metres above sea level').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Contours run smoothly; fences turn sharp corners').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Reading Height and Slope on the Orthophoto
        self.next_band(1)
        b1_title = Tex('Reading height and slope').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Count from a labelled contour in steps of 5 m').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Close contours steep; wide contours gentle').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('1 cm = 100 m at 1:10 000').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('35 m / 250 m = 1 : 7,1').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Landforms from Contours over the Image
        self.next_band(2)
        b2_title = Tex('Landforms over the image').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Valley V's upstream; river lined by dark bush").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Spur V's downhill; paths along the crest").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Cutting: contours bunch in beside the road').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Donga: sharp V, pale bare scar, no river').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Combining Photograph and Contours, and the Error Museum
        self.next_band(3)
        b3_title = Tex('Combining photo and contours').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Dam: smooth dark water; edge follows a contour').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Dam wall where the valley contours narrow').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('1 520 and 1 540 m on both maps; 1 525 to 1 535 only here').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Detail: orthophoto. Overall relief: topographic map.').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Combining Photograph and Contours, and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Orthophoto contours are 20 m apart''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``A dam's edge can cross contours''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``A fence will do as a contour''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``On the orthophoto 1 cm is 500 m''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Photo That Flattens the Hill
        self.next_band(5)
        b5_title = Tex('The photo that flattens the hill').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Straight down, hills look flat').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Contours every 5 m show the height').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Count in fives from a labelled line').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Contours never stop; fences turn at gates').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Dam That Fills Like a Bath
        self.next_band(6)
        b6_title = Tex('The dam that fills like a bath').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Still water is flat: the dam edge follows a contour').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Wall at the narrow end of the valley').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Fields stop where contours bunch up').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Up 35, along 250: about 1:7').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Road Cut Through the Hill
        self.next_band(7)
        b7_title = Tex('The road cut through the hill').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Cutting: contours bunch in beside the road').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Embankment: contours push outward').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Sharp V's on bare slopes with no river: dongas").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Close-up: orthophoto. Big picture: topographic map.').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
