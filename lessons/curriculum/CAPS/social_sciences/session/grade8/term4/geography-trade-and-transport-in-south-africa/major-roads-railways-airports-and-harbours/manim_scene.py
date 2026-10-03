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

# Band-layout whiteboard scene for major-roads-railways-airports-and-harbours (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/270/270/200/130/130/130 of 1400 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SouthAfricanTransportNetworkSession(MovingCameraScene):
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
        # --- Band 0: National roads
        self.write_rows(0, "National roads", [
            "N1: Cape Town to Beitbridge",
            "N2: the coastal route",
            "N3: Durban to Johannesburg",
            "Transport corridors",
        ], scale=0.86, box=2)
        # --- Band 1: Railways and airports
        self.next_band(1)
        self.write_rows(1, "Railways and airports", [
            "Built for diamonds and gold",
            "Coal and iron ore lines",
            "O. R. Tambo: busiest",
            "Cape Town, King Shaka",
        ], scale=0.86, box=2)
        # --- Band 2: Harbours and pattern
        self.next_band(2)
        self.write_rows(2, "Harbours and pattern", [
            "Eight commercial ports",
            "Durban: busiest",
            "Hub and spokes: Gauteng",
            "Serving neighbours",
        ], scale=0.86, box=2)
        # --- Band 3: Map skills
        self.next_band(3)
        self.write_rows(3, "Map skills", [
            "570 $\\div$ 75 = 7.6 hours",
            "1 cm = 100 km at 1 to 10 million",
            "12.8 cm = 1 280 km",
            "Describe, evidence, explain",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Roads across the country
        self.next_band(4)
        self.write_rows(4, "Roads across the country", [
            "N1, N2, N3",
        ], scale=0.86, box=0)
        # --- Band 5: Trains and planes
        self.next_band(5)
        self.write_rows(5, "Trains and planes", [
            "Mines to ports",
        ], scale=0.86, box=0)
        # --- Band 6: Ports and the wheel
        self.next_band(6)
        self.write_rows(6, "Ports and the wheel", [
            "Gauteng at the hub",
        ], scale=0.86, box=0)
        self.wait(4)
