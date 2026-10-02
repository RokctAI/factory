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

# Band-layout whiteboard scene for ocean-currents-durban-and-port-nolloth (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/290/230/240/150/150/150 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class OceanCurrentsDurbanAndPortNollothSession(MovingCameraScene):
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
        # --- Band 0: Ocean currents
        self.write_rows(0, "Ocean currents", [
            "Rivers in the sea, driven by winds",
            "Warm: from the tropics, east coasts",
            "Cold: towards the equator, west coasts",
            "Upwelling on the west coast",
        ], scale=0.86, box=2)
        # --- Band 1: Durban and Port Nolloth
        self.next_band(1)
        self.write_rows(1, "Durban and Port Nolloth", [
            "Same latitude, both at sea level",
            "January: about 24.5 \\textdegree{}C and 16.5 \\textdegree{}C",
            "Rain: about 1 000 mm and 60 mm",
            "Humid air against stable air and fog",
        ], scale=0.86, box=3)
        # --- Band 2: Deserts, fog and fish
        self.next_band(2)
        self.write_rows(2, "Deserts, fog and fish", [
            "Namib and Atacama beside cold currents",
            "North Atlantic Drift warms Europe",
            "Upwelling feeds plankton and fish",
            "The sardine run in winter",
        ], scale=0.86, box=2)
        # --- Band 3: Writing the comparison
        self.next_band(3)
        self.write_rows(3, "Writing the comparison", [
            "Name the current and its direction",
            "Air temperature, humidity, stability",
            "1 000 -- 60 = 940",
            "Same latitude isolates the currents",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Rivers in the sea
        self.next_band(4)
        self.write_rows(4, "Rivers in the sea", [
            "Warm Agulhas on the east",
            "Cold Benguela on the west",
        ], scale=0.86, box=0)
        # --- Band 5: Two towns, one latitude
        self.next_band(5)
        self.write_rows(5, "Two towns, one latitude", [
            "Warm and wet Durban",
            "Cool and foggy Port Nolloth",
        ], scale=0.86, box=1)
        # --- Band 6: Deserts, fog and fish
        self.next_band(6)
        self.write_rows(6, "Deserts, fog and fish", [
            "Cold coasts are dry",
            "Cold water feeds fish",
        ], scale=0.86, box=1)
        self.wait(4)
