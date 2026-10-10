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

# Band-layout whiteboard scene for latitude-and-longitude-on-a-flat-map (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/130/160/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LatitudeAndLongitudeOnAFlatMapSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Grid on a Flat Map
        self.write_rows(0, "The Grid on a Flat Map", [
            "Latitude lines: across",
            "Longitude lines: up and down",
            "Degrees printed on the edges",
            "Estimate between lines",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Reading a Position
        self.next_band(1)
        self.write_rows(1, "Reading a Position", [
            "Find the place",
            "Latitude first, N or S",
            "Then longitude, E or W",
            "Johannesburg: 26 S, 28 E",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Finding a Place from Its Degrees
        self.next_band(2)
        self.write_rows(2, "Finding a Place from Its Degrees", [
            "Up or down from the equator",
            "Right or left from Greenwich",
            "30 N, 31 E: Cairo",
            "30 S, 31 E: Durban",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Longitude first''",
            "``No need for N, S, E or W''",
            "``Count latitude from the top''",
            "``Read the wrong edge''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Lines on Paper
        self.next_band(4)
        self.write_rows(4, "Lines on Paper", [
            "Across",
            "Up and down",
            "Edges",
            "Estimate",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Read the Address
        self.next_band(5)
        self.write_rows(5, "Read the Address", [
            "Find",
            "Latitude",
            "Longitude",
            "Write",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Follow the Clue
        self.next_band(6)
        self.write_rows(6, "Follow the Clue", [
            "Equator",
            "Greenwich",
            "Meet",
            "Place",
        ], scale=0.9, box=2)

        last = Tex("Latitude first, then longitude, always with the directions: that is how every place on a flat map gets its address.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
