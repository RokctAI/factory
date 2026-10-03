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

# Band-layout whiteboard scene for modes-of-transport-and-their-uses (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/260/300/230/130/130/130 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ModesOfTransportSession(MovingCameraScene):
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
        # --- Band 0: Sea transport
        self.write_rows(0, "Sea transport", [
            "Container ships and bulk carriers",
            "Tankers, reefers, ro-ro",
            "Cheapest for heavy loads",
            "Slow, needs ports",
        ], scale=0.86, box=2)
        # --- Band 1: Air and road
        self.next_band(1)
        self.write_rows(1, "Air and road", [
            "Air: fast, perishable, valuable",
            "Air: costly, high emissions",
            "Road: door-to-door",
            "Road: congestion, damage",
        ], scale=0.86, box=2)
        # --- Band 2: Rail and pipelines
        self.next_band(2)
        self.write_rows(2, "Rail and pipelines", [
            "Sishen to Saldanha",
            "Rail: bulk over distance",
            "Pipelines: liquids, gases",
            "Durban to Gauteng fuel",
        ], scale=0.86, box=1)
        # --- Band 3: Choosing a mode
        self.next_band(3)
        self.write_rows(3, "Choosing a mode", [
            "100 x 60 = 6 000 tonnes",
            "6 000 $\\div$ 34 = about 177 trucks",
            "Intermodal journeys",
            "Emissions: air highest",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Ships
        self.next_band(4)
        self.write_rows(4, "Ships", [
            "Slow but cheap",
        ], scale=0.86, box=0)
        # --- Band 5: Planes and trucks
        self.next_band(5)
        self.write_rows(5, "Planes and trucks", [
            "Fast, or door-to-door",
        ], scale=0.86, box=0)
        # --- Band 6: Trains and pipes
        self.next_band(6)
        self.write_rows(6, "Trains and pipes", [
            "Heavy loads and liquids",
        ], scale=0.86, box=0)
        self.wait(4)
