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

# Band-layout whiteboard scene for oblique-and-vertical-aerial-photographs (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/300/280/240/130/130/130 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ObliqueAndVerticalPhotosSession(MovingCameraScene):
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
        # --- Band 0: Aerial photographs
        self.write_rows(0, "Aerial photographs", [
            "Taken from aircraft or drones",
            "Lower than satellites",
            "Vertical: straight down",
            "Oblique: tilted",
        ], scale=0.86, box=2)
        # --- Band 1: Oblique and vertical
        self.next_band(1)
        self.write_rows(1, "Oblique and vertical", [
            "Oblique: sides, horizon",
            "Scale changes",
            "Vertical: map-like",
            "Measure on vertical",
        ], scale=0.86, box=3)
        # --- Band 2: Reading features
        self.next_band(2)
        self.write_rows(2, "Reading features", [
            "Natural and constructed",
            "Tone, texture, shape",
            "Size, shadow, pattern",
            "Association",
        ], scale=0.86, box=1)
        # --- Band 3: Scale of a vertical photo
        self.next_band(3)
        self.write_rows(3, "Scale of a vertical photo", [
            "Focal length $\\div$ flying height",
            "0.152 $\\div$ 1 520 = 1/10 000",
            "1 cm = 100 m",
            "Higher means smaller scale",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Pictures from the sky
        self.next_band(4)
        self.write_rows(4, "Pictures from the sky", [
            "Flat phone, tilted phone",
        ], scale=0.86, box=0)
        # --- Band 5: Tilted or straight down
        self.next_band(5)
        self.write_rows(5, "Tilted or straight down", [
            "Recognise or measure",
        ], scale=0.86, box=0)
        # --- Band 6: Nature or people?
        self.next_band(6)
        self.write_rows(6, "Nature or people?", [
            "Curves or straight lines",
        ], scale=0.86, box=0)
        self.wait(4)
