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

# Band-layout whiteboard scene for river-health-and-care-of-catchment-areas (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (200/180/160/180/90/90/90 of 990 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class RiverHealthAndCareOfCatchmentAreasSession(MovingCameraScene):
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
        # --- Band 0: Rivers and Catchments
        self.write_rows(0, "Rivers and Catchments", [
            "Catchment: land draining into a river",
            "Watershed: high ground between catchments",
            "Source, tributary, confluence, mouth",
            "Wetlands: sponges and filters",
        ], scale=0.86, box=1)
        # --- Band 1: What Makes a River Healthy?
        self.next_band(1)
        self.write_rows(1, "What Makes a River Healthy?", [
            "Healthy: clear, oxygen, many species",
            "Unhealthy: algae, smell, litter, dead fish",
            "miniSASS: score small invertebrates",
            "Stoneflies and mayflies need clean water",
        ], scale=0.86, box=3)
        # --- Band 2: Threats to Rivers
        self.next_band(2)
        self.write_rows(2, "Threats to Rivers", [
            "Failing sewage works pollute rivers",
            "Alien trees and water hyacinth",
            "Dams change river flow",
            "Half or more of wetlands lost or damaged",
        ], scale=0.86, box=2)
        # --- Band 3: Caring for Catchments
        self.next_band(3)
        self.write_rows(3, "Caring for Catchments", [
            "Ecological reserve and catchment agencies",
            "Green Drop: waste water; Blue Drop: drinking water",
            "Buffer strips and careful farming",
            "Clean-ups, reporting, miniSASS",
        ], scale=0.8, box=4)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Catchments
        self.next_band(4)
        self.write_rows(4, "Catchments", [
            "Catchment: land that drains into a river",
            "Watershed separates catchments",
            "Wetlands: sponges",
        ], scale=0.86, box=0)
        # --- Band 5: Healthy and Sick Rivers
        self.next_band(5)
        self.write_rows(5, "Healthy and Sick Rivers", [
            "Healthy: clear and full of life",
            "Sick: smell, slime, litter",
            "miniSASS: check tiny creatures",
        ], scale=0.86, box=0)
        # --- Band 6: Caring for Rivers
        self.next_band(6)
        self.write_rows(6, "Caring for Rivers", [
            "Threats: sewage, litter, alien plants",
            "Clean-ups and reporting",
            "Plant indigenous trees",
        ], scale=0.86, box=0)
        self.wait(4)
