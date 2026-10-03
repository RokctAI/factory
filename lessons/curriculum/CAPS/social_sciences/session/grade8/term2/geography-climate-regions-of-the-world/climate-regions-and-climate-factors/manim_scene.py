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

# Band-layout whiteboard scene for climate-regions-and-climate-factors (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/220/280/230/150/150/150 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ClimateRegionsAndClimateFactorsSession(MovingCameraScene):
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
        # --- Band 0: The factor toolkit
        self.write_rows(0, "The factor toolkit", [
            "Latitude and pressure belts",
            "Distance from the sea",
            "Altitude: 6.5 \\textdegree{}C per 1 000 m",
            "Currents and mountains",
        ], scale=0.86, box=0)
        # --- Band 1: Hot regions
        self.next_band(1)
        self.write_rows(1, "Hot regions", [
            "Rainforest: rising air, rain all year",
            "Savanna: belts shift, summer rain",
            "Desert: sinking air, cold currents",
            "Karoo: rain shadow, far from moisture",
        ], scale=0.86, box=2)
        # --- Band 2: Middle latitudes, cold and high
        self.next_band(2)
        self.write_rows(2, "Middle latitudes, cold and high", [
            "Mediterranean: winter fronts",
            "Humid subtropical: warm Agulhas",
            "Continental: far from the sea",
            "Mountains: colder with height",
        ], scale=0.86, box=0)
        # --- Band 3: Linked explanations
        self.next_band(3)
        self.write_rows(3, "Linked explanations", [
            "Factor $\\rightarrow$ process $\\rightarrow$ effect",
            "1.75 $\\times$ 6.5 $\\approx$ 11.4 \\textdegree{}C",
            "1 010 $\\div$ 60 $\\approx$ 17",
            "Not ``closer to the sun''",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Six tools
        self.next_band(4)
        self.write_rows(4, "Six tools", [
            "Sun, air, sea, height, currents, mountains",
        ], scale=0.86, box=0)
        # --- Band 5: Hot, wet and dry
        self.next_band(5)
        self.write_rows(5, "Hot, wet and dry", [
            "Rising air wet, sinking air dry",
        ], scale=0.86, box=0)
        # --- Band 6: Cool, cold and high
        self.next_band(6)
        self.write_rows(6, "Cool, cold and high", [
            "Explain with a chain",
        ], scale=0.86, box=0)
        self.wait(4)
