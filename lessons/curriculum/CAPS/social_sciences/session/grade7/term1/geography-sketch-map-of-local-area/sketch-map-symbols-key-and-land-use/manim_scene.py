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

# Band-layout whiteboard scene for sketch-map-symbols-key-and-land-use (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/180/190/210/90/90/90 of 1030 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SketchMapSymbolsKeyAndLandUseSession(MovingCameraScene):
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
        # --- Band 0: Symbols and the Key
        self.write_rows(0, "Symbols and the Key", [
            "Point symbols: school, tap, tree",
            "Line symbols: roads, rivers, fences",
            "Area symbols: fields, parks, bush",
            "Every symbol appears in the key",
        ], scale=0.86, box=3)
        # --- Band 1: Direction and Scale on a Sketch Map
        self.next_band(1)
        self.write_rows(1, "Direction and Scale on a Sketch Map", [
            "Compass rose: 8 points, 45 degrees apart",
            "North arrow matches real north",
            "Pace a street: 200 m drawn as 4 cm",
            "1 cm represents about 50 m",
        ], scale=0.86, box=3)
        # --- Band 2: Observing Land Use and Vegetation
        self.next_band(2)
        self.write_rows(2, "Observing Land Use and Vegetation", [
            "Residential, commercial, industrial",
            "Recreational, institutional, transport, farming",
            "Grass, shrubs, trees, crops, bare ground",
            "Fieldwork: record in a table, stay safe",
        ], scale=0.8, box=1)
        # --- Band 3: Putting the Project Together
        self.next_band(3)
        self.write_rows(3, "Putting the Project Together", [
            "Frame, title, compass rose",
            "Roads, buildings, land-use shading",
            "Key, scale, then check everything",
            "Describe: pattern first, then details",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Little Pictures for Big Things
        self.next_band(4)
        self.write_rows(4, "Little Pictures for Big Things", [
            "Points, lines and areas",
            "Blue water, green plants",
            "On the map means in the key",
        ], scale=0.86, box=0)
        # --- Band 5: Which Way and How Big
        self.next_band(5)
        self.write_rows(5, "Which Way and How Big", [
            "Eight-point compass rose",
            "Pace a street to make a scale",
            "Keep things in proportion",
        ], scale=0.86, box=0)
        # --- Band 6: Be a Geographer Outside
        self.next_band(6)
        self.write_rows(6, "Be a Geographer Outside", [
            "Houses, shops, factories, parks",
            "Grass, bushes, trees, crops",
            "Pattern first, then details",
        ], scale=0.86, box=0)
        self.wait(4)
