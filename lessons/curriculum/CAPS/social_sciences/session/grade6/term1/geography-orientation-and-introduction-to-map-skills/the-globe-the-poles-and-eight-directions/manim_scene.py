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

# Band-layout whiteboard scene for the-globe-the-poles-and-eight-directions (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (200/130/200/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheGlobeThePolesAndEightDirectionsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Grade 6 Geography
        self.write_rows(0, "Grade 6 Geography", [
            "Term 1: map skills",
            "Term 2: trade",
            "Term 3: climate and vegetation",
            "Term 4: population",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): The Globe, the Equator and the Poles
        self.next_band(1)
        self.write_rows(1, "The Globe, the Equator and the Poles", [
            "Globe: a round model",
            "Axis from pole to pole",
            "Equator: around the middle",
            "South Africa: Southern Hemisphere",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Eight Directions from a Fixed Point
        self.next_band(2)
        self.write_rows(2, "Eight Directions from a Fixed Point", [
            "North, east, south, west",
            "Four in-between points",
            "North or south comes first",
            "Always from a fixed point",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Say east-north''",
            "``The equator is painted on the ground''",
            "``A direction needs no fixed point''",
            "``North is where you face''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Four Topics
        self.next_band(4)
        self.write_rows(4, "Four Topics", [
            "Maps",
            "Trade",
            "Climate",
            "Population",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Ball and Line
        self.next_band(5)
        self.write_rows(5, "Ball and Line", [
            "Globe",
            "Poles",
            "Equator",
            "Hemispheres",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Eight Points
        self.next_band(6)
        self.write_rows(6, "Eight Points", [
            "North",
            "East",
            "South",
            "West",
        ], scale=0.9, box=0)

        last = Tex("A globe, the equator and eight compass points from a fixed point are the base of every map skill in Grade 6.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
