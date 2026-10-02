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


class ScaleAndMeasuringDistanceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Three Ways to Write a Scale
        title = Tex('Three ways to write a scale').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Word: 1 cm represents 0,5 km').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Ratio: 1:50 000, one unit to 50 000 of the same unit').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Line: a ruled line, 2 cm for each kilometre').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('50 000 cm = 500 m = 0,5 km').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Large and Small Scale, and the Photocopier Problem
        self.next_band(1)
        b1_title = Tex('Large scale, small scale').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('1:10 000 is larger than 1:50 000').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Large scale: small area, more detail').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Reduced photocopy: the ratio becomes wrong').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('The line scale shrinks with the map: trust it').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Measuring Straight and Curved Distances
        self.next_band(2)
        b2_title = Tex('Measuring distance').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Actual distance = map distance x scale').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('6,3 cm x 50 000 = 315 000 cm = 3,15 km').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Curved: paper strip or string along the route').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Road 9,6 cm = 4,8 km, longer than the straight line').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Distance, Time and the Error Museum
        self.next_band(3)
        b3_title = Tex('Distance and time').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Time = distance / speed').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('4,8 km / 5 km/h = 0,96 h, about 58 minutes').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('3 km on the ground = 6 cm on the 1:50 000 map').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Measure centre to centre; always write the unit').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Distance, Time and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``1 cm is 50 km on a 1:50 000 map''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``The ratio scale survives a photocopier''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``A ruler end to end gives curved distance''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Time = speed / distance''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Toy Car and the Real Car
        self.next_band(5)
        b5_title = Tex('The toy car and the real car').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('A map is the land shrunk by a fixed amount').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('1 cm = 500 m; 2 cm = 1 km').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Orthophoto: 1 cm = 100 m').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Map made smaller? Trust the line.').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): String Along the Taxi Route
        self.next_band(6)
        b6_title = Tex('String along the taxi route').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Ruler: straight, as the crow flies, 3,15 km').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('String or paper: along every bend').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Road 9,6 cm x 0,5 = 4,8 km').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('The road is longer because it winds').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Timing the Walk
        self.next_band(7)
        b7_title = Tex('Timing the walk').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Time = distance / speed').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('4,8 / 5 = 0,96 h, about 58 minutes').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Centimetres to kilometres before the time sum').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Write the unit every time').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
