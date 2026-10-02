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

# Band-layout whiteboard scene for desert-polar-mediterranean-and-other-climates (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (250/280/260/200/150/150/150 of 1440 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class DesertPolarMediterraneanAndOtherClimatesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0: Desert and semi-desert
        self.write_rows(0, "Desert and semi-desert", [
            "Desert under about 250 mm",
            "Semi-desert about 250 to 500 mm",
            "Subtropical highs and cold currents",
            "Upington about 190 mm",
        ], scale=0.86, box=0)
        # --- Band 1: Mediterranean and continental
        self.next_band(1)
        self.write_rows(1, "Mediterranean and continental", [
            "Cape Town: dry summers, wet winters",
            "Fynbos: about 9 000 species",
            "Moscow: about --6 \\textdegree{}C and 19 \\textdegree{}C",
            "Large ranges far from the sea",
        ], scale=0.86, box=0)
        # --- Band 2: Polar, tundra, high mountain
        self.next_band(2)
        self.write_rows(2, "Polar, tundra, high mountain", [
            "Antarctica: about --89 \\textdegree{}C record",
            "Tundra: 0 to 10 \\textdegree{}C summer, permafrost",
            "Mountains: zones stacked by height",
            "Lesotho highlands: winter snow",
        ], scale=0.86, box=1)
        # --- Band 3: Recognising climates
        self.next_band(3)
        self.write_rows(3, "Recognising climates", [
            "Coolest above 18 \\textdegree{}C: tropical",
            "Winter rain, dry summer: Mediterranean",
            "360 $\\div$ 500 = 0.72",
            "Range 25 \\textdegree{}C with snow: continental",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Dry places
        self.next_band(4)
        self.write_rows(4, "Dry places", [
            "Under 250 mm: desert",
            "Succulents store water",
        ], scale=0.86, box=0)
        # --- Band 5: Winter rain and frozen winters
        self.next_band(5)
        self.write_rows(5, "Winter rain and frozen winters", [
            "Cape Town: rain in winter",
            "Moscow: snowy winters",
        ], scale=0.86, box=0)
        # --- Band 6: Ice, tundra and mountain tops
        self.next_band(6)
        self.write_rows(6, "Ice, tundra and mountain tops", [
            "Freezing all year at the poles",
            "Colder with height",
        ], scale=0.86, box=1)
        self.wait(4)
