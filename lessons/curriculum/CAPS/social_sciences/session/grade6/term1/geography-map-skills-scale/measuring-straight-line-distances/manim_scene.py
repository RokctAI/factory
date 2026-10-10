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

# Band-layout whiteboard scene for measuring-straight-line-distances (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/140/150/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MeasuringStraightLineDistancesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=box_color)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(42)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Ruler Method
        self.write_rows(0, "The Ruler Method", [
            "Centre of dot to centre of dot",
            "Read centimetres",
            "Multiply by the word scale",
            "10 cm x 50 km = 500 km",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): The Paper Strip Method
        self.next_band(1)
        self.write_rows(1, "The Paper Strip Method", [
            "Mark both places on a strip",
            "First mark on the zero",
            "Read the second mark",
            "Slide along for long distances",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Straight Line or Road
        self.next_band(2)
        self.write_rows(2, "Straight Line or Road", [
            "As the crow flies",
            "Road distance is longer",
            "Durban: about 500 km straight",
            "About 570 km by road",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Measure from the edge of the dot''",
            "``Start at the end of the bar''",
            "``Forget to multiply''",
            "``Road and straight line are equal''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Measure and Multiply
        self.next_band(4)
        self.write_rows(4, "Measure and Multiply", [
            "Ruler",
            "Centimetres",
            "Multiply",
            "Kilometres",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Mark and Match
        self.next_band(5)
        self.write_rows(5, "Mark and Match", [
            "Strip",
            "Mark",
            "Zero",
            "Read",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): The Crow and the Car
        self.next_band(6)
        self.write_rows(6, "The Crow and the Car", [
            "Straight",
            "Shortest",
            "Road",
            "Longer",
        ], scale=0.9, box=1)

        last = Tex("The scale turns centimetres on a map into kilometres on the ground, and the straight line is always the shortest way.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
