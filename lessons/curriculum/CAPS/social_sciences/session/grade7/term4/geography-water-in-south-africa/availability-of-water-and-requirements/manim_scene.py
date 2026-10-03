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

# Band-layout whiteboard scene for availability-of-water-and-requirements (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/160/180/180/90/90/90 of 960 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class AvailabilityOfWaterAndRequirementsSession(MovingCameraScene):
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
        # --- Band 0: A Water-Scarce Country
        self.write_rows(0, "A Water-Scarce Country", [
            "Rainfall about 450 to 500 mm, half the world average",
            "More rain in the east, little in the west",
            "Droughts linked to El Nino",
            "Only about 9 percent becomes runoff",
        ], scale=0.8, box=1)
        # --- Band 1: Sources of Water
        self.next_band(1)
        self.write_rows(1, "Sources of Water", [
            "Surface water: about 77 percent",
            "Over 5000 large dams; Gariep the largest",
            "Groundwater from aquifers via boreholes",
            "Reuse, desalination, rain tanks",
        ], scale=0.86, box=2)
        # --- Band 2: Moving Water: Inter-Basin Transfers
        self.next_band(2)
        self.write_rows(2, "Moving Water: Inter-Basin Transfers", [
            "Catchment: area drained by a river",
            "Gauteng: high demand, no big river",
            "Lesotho Highlands: Katse Dam to the Vaal",
            "Tugela-Vaal and Orange-Fish transfers",
        ], scale=0.86, box=3)
        # --- Band 3: Requirements and Closing the Gap
        self.next_band(3)
        self.write_rows(3, "Requirements and Closing the Gap", [
            "Demand grows: people, cities, economy",
            "Climate change adds pressure",
            "Cape Town Day Zero, 2015 to 2018",
            "Increase supply and reduce demand",
        ], scale=0.86, box=4)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A Dry Country
        self.next_band(4)
        self.write_rows(4, "A Dry Country", [
            "Half the world's average rain",
            "Wet east, dry west",
            "Much rain evaporates",
        ], scale=0.86, box=0)
        # --- Band 5: Where Water Comes From
        self.next_band(5)
        self.write_rows(5, "Where Water Comes From", [
            "Rivers and dams",
            "Groundwater from boreholes",
            "Water from Lesotho for Gauteng",
        ], scale=0.86, box=0)
        # --- Band 6: Will There Be Enough?
        self.next_band(6)
        self.write_rows(6, "Will There Be Enough?", [
            "Demand is growing",
            "Day Zero in Cape Town",
            "Find more, use less",
        ], scale=0.86, box=0)
        self.wait(4)
