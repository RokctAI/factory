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

# Band-layout whiteboard scene for identifying-urban-land-use-on-photographs-and-maps (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/260/300/220/130/130/130 of 1440 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class UrbanLandUseOnPhotosSession(MovingCameraScene):
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
        # --- Band 0: Large-scale maps
        self.write_rows(0, "Large-scale maps", [
            "Topographic: 1 to 50 000",
            "Orthophoto: 1 to 10 000",
            "Title, scale, key, north",
            "50 000 $\\div$ 10 000 = 5",
        ], scale=0.86, box=1)
        # --- Band 1: Evidence for each zone
        self.next_band(1)
        self.write_rows(1, "Evidence for each zone", [
            "CBD: tall, dense, shadows",
            "Industry: roofs, tanks, sidings",
            "High income: plots, pools",
            "Low income: tight rows",
        ], scale=0.86, box=0)
        # --- Band 2: Reading a town
        self.next_band(2)
        self.write_rows(2, "Reading a town", [
            "Orient yourself",
            "Find the CBD",
            "Industry, homes, recreation",
            "Explain each location",
        ], scale=0.86, box=3)
        # --- Band 3: Measuring and evidence
        self.next_band(3)
        self.write_rows(3, "Measuring and evidence", [
            "100 m x 70 m = 7 000 square m",
            "12 x 500 m = 6 km",
            "Claim, evidence, explanation",
            "Only visible evidence",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Two kinds of map
        self.next_band(4)
        self.write_rows(4, "Two kinds of map", [
            "A drawing and a photo",
        ], scale=0.86, box=0)
        # --- Band 5: Spot the zone
        self.next_band(5)
        self.write_rows(5, "Spot the zone", [
            "Clues for each zone",
        ], scale=0.86, box=0)
        # --- Band 6: Show your evidence
        self.next_band(6)
        self.write_rows(6, "Show your evidence", [
            "Claim, evidence, explanation",
        ], scale=0.86, box=0)
        self.wait(4)
