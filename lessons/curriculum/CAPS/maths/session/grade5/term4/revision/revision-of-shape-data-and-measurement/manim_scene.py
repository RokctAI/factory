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

# Band-layout whiteboard scene for revision-of-shape-data-and-measurement (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/160/160/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RevisionOfShapeDataAndMeasurementSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Shapes, Objects and Transformations
        self.write_rows(0, "Shapes, Objects and Transformations", [
            "Tent: triangular prism, 5 faces",
            "Tank: cylinder",
            "Cool box: 6 faces, 12 edges",
            "Hexagon tiles: no gaps",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Measurement: Time, Length, Mass and Capacity
        self.next_band(1)
        self.write_rows(1, "Measurement: Time, Length, Mass and Capacity", [
            "07:15 to 11:40: 4 h 25 min",
            "2:30 p.m. is 14:30",
            "3 and 1/2 km is 3 500 m",
            "24 times 1 500 ml is 36 l",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Data, Perimeter, Area and Volume
        self.next_band(2)
        self.write_rows(2, "Data, Perimeter, Area and Volume", [
            "Hiking 9, swimming 7",
            "Campfire 6, birdwatching 2",
            "Tent floor: 12 square units",
            "Cool box: 15 times 2 is 30",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3 hours 85 minutes''",
            "``3 and 1/2 km is 350 m''",
            "``Area of 14''",
            "``A tent is a triangle''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Around the Camp
        self.next_band(4)
        self.write_rows(4, "Around the Camp", [
            "Around the camp",
            "Tent: prism",
            "Tank: cylinder",
            "Tiles: tessellation",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): On the Move
        self.next_band(5)
        self.write_rows(5, "On the Move", [
            "On the move",
            "4 hours 25 minutes",
            "3 500 m hike",
            "1 500 ml each",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Around the Campfire
        self.next_band(6)
        self.write_rows(6, "Around the Campfire", [
            "Around the campfire",
            "Mode: hiking",
            "12 squares inside",
            "30 juice boxes",
        ], scale=0.9, box=1)

        last = Tex("Shapes, objects, time, length, mass, capacity, data, area and volume: look carefully, pick the right unit, and check that every answer makes sense.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
