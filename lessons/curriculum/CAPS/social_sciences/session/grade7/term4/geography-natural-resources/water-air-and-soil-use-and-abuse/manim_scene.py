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

# Band-layout whiteboard scene for water-air-and-soil-use-and-abuse (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/180/140/170/90/90/90 of 920 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WaterAirAndSoilUseAndAbuseSession(MovingCameraScene):
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
        # --- Band 0: What Are Natural Resources?
        self.write_rows(0, "What Are Natural Resources?", [
            "Natural resources: provided by nature",
            "Renewable: sun, wind, water, forests",
            "Non-renewable: coal, oil, gold",
            "Sustainable: meet needs, protect the future",
        ], scale=0.86, box=1)
        # --- Band 1: Water, Air and Soil
        self.next_band(1)
        self.write_rows(1, "Water, Air and Soil", [
            "About 97 percent of water is salty",
            "Less than 1 percent easily available fresh",
            "Air: nitrogen 78, oxygen 21 percent",
            "Soil: rock particles, humus, water, air",
        ], scale=0.86, box=2)
        # --- Band 2: Abuse of Water and Air
        self.next_band(2)
        self.write_rows(2, "Abuse of Water and Air", [
            "Sewage, fertilisers, factory waste in rivers",
            "Acid mine drainage from old mines",
            "Leaking pipes waste treated water",
            "Coal power, vehicles and fires pollute air",
        ], scale=0.86, box=2)
        # --- Band 3: Abuse of Soil
        self.next_band(3)
        self.write_rows(3, "Abuse of Soil", [
            "Erosion: topsoil removed by water, wind",
            "Overgrazing leaves soil bare; dongas form",
            "Salinisation and desertification",
            "Contour ploughing, terraces, crop rotation",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Nature's Supplies
        self.next_band(4)
        self.write_rows(4, "Nature's Supplies", [
            "Renewable: sun, wind, trees",
            "Non-renewable: coal, oil, gold",
            "Sustainable: save for the future",
        ], scale=0.86, box=0)
        # --- Band 5: Water, Air and Soil
        self.next_band(5)
        self.write_rows(5, "Water, Air and Soil", [
            "Most water is salty",
            "Air: nitrogen and oxygen",
            "Soil forms very slowly",
        ], scale=0.86, box=0)
        # --- Band 6: Damaging Our Resources
        self.next_band(6)
        self.write_rows(6, "Damaging Our Resources", [
            "Water: sewage, chemicals, leaks",
            "Air: coal, cars, fires",
            "Soil: overgrazing and erosion",
        ], scale=0.86, box=0)
        self.wait(4)
