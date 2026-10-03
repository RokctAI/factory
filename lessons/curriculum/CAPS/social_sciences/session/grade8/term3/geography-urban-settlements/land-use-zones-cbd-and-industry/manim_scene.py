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

# Band-layout whiteboard scene for land-use-zones-cbd-and-industry (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (250/280/250/270/130/130/130 of 1440 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LandUseZonesSession(MovingCameraScene):
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
        # --- Band 0: Urban land use
        self.write_rows(0, "Urban land use", [
            "Secondary and tertiary jobs",
            "Land use zones",
            "Accessibility and land value",
            "Physical features and history",
        ], scale=0.86, box=2)
        # --- Band 1: The CBD
        self.next_band(1)
        self.write_rows(1, "The CBD", [
            "Tallest buildings",
            "Offices, banks, big shops",
            "Main transport terminals",
            "Decentralised: Sandton",
        ], scale=0.86, box=0)
        # --- Band 2: Light and heavy industry
        self.next_band(2)
        self.write_rows(2, "Light and heavy industry", [
            "Light: clothing, food, printing",
            "Near roads and workers",
            "Heavy: steel, oil, chemicals",
            "Space, transport, away from homes",
        ], scale=0.86, box=3)
        # --- Band 3: Zones on maps
        self.next_band(3)
        self.write_rows(3, "Zones on maps", [
            "Sidings, tanks, chimneys",
            "1 200 x 10 = 12 000 square m",
            "Explain the location",
            "Give map evidence",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Different jobs, different places
        self.next_band(4)
        self.write_rows(4, "Different jobs, different places", [
            "The city as a dartboard",
        ], scale=0.86, box=0)
        # --- Band 5: The CBD
        self.next_band(5)
        self.write_rows(5, "The CBD", [
            "Tall, busy, expensive",
        ], scale=0.86, box=0)
        # --- Band 6: Factories big and small
        self.next_band(6)
        self.write_rows(6, "Factories big and small", [
            "Light near homes, heavy far",
        ], scale=0.86, box=0)
        self.wait(4)
