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

# Band-layout whiteboard scene for road-versus-rail-and-future-transport-networks (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (290/260/250/250/130/130/130 of 1440 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class RoadVersusRailSession(MovingCameraScene):
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
        # --- Band 0: Road transport
        self.write_rows(0, "Road transport", [
            "Door-to-door delivery",
            "Flexible and quick for short trips",
            "Small loads, more fuel per tonne",
            "Road damage, congestion, accidents",
        ], scale=0.86, box=3)
        # --- Band 1: Rail transport
        self.next_band(1)
        self.write_rows(1, "Rail transport", [
            "Huge loads of bulk goods",
            "Cheaper and cleaner per tonne",
            "Only where there are tracks",
            "Cable theft and breakdowns",
        ], scale=0.86, box=2)
        # --- Band 2: Durban to Gauteng
        self.next_band(2)
        self.write_rows(2, "Durban to Gauteng", [
            "N3 and railway side by side",
            "Trucks at Van Reenen's Pass",
            "Intermodal: rail then road",
            "Road-to-rail goal",
        ], scale=0.86, box=2)
        # --- Band 3: Future networks
        self.next_band(3)
        self.write_rows(3, "Future networks", [
            "100 x 30 = 3 000 tonnes",
            "3 000 $\\div$ 34 = about 88.2",
            "So at least 89 trucks",
            "Reliable, linked, safe, clean, fair",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Trucks
        self.next_band(4)
        self.write_rows(4, "Trucks", [
            "Go anywhere, carry little",
        ], scale=0.86, box=0)
        # --- Band 5: Trains
        self.next_band(5)
        self.write_rows(5, "Trains", [
            "Big loads on fixed tracks",
        ], scale=0.86, box=0)
        # --- Band 6: Both together
        self.next_band(6)
        self.write_rows(6, "Both together", [
            "Train far, truck near",
        ], scale=0.86, box=0)
        self.wait(4)
