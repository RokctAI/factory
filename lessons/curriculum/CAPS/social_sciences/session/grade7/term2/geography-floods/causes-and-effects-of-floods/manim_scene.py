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

# Band-layout whiteboard scene for causes-and-effects-of-floods (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/180/190/210/90/90/90 of 1020 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CausesAndEffectsOfFloodsSession(MovingCameraScene):
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
        # --- Band 0: What a Flood Is and How Rain Becomes a Flood
        self.write_rows(0, "What a Flood Is and How Rain Becomes a Flood", [
            "Flood: water over normally dry land",
            "Interception, infiltration, surface run-off",
            "Run-off is fast; infiltration is slow",
            "Flash floods: minutes, no warning",
        ], scale=0.86, box=2)
        # --- Band 1: Natural Causes: Heavy Rain and Tsunamis
        self.next_band(1)
        self.write_rows(1, "Natural Causes: Heavy Rain and Tsunamis", [
            "Unusually heavy rain on saturated ground",
            "Cut-off lows: KZN, April 2022",
            "Cyclones: Eline, 2000",
            "Tsunamis and storm surges flood coasts",
        ], scale=0.86, box=1)
        # --- Band 2: Human Causes: How Land Use Makes Floods Worse
        self.next_band(2)
        self.write_rows(2, "Human Causes: How Land Use Makes Floods Worse", [
            "Cleared vegetation: more run-off",
            "Overgrazing and ploughing downhill",
            "Fires leave hard, bare soil",
            "Cities: roofs and roads stop infiltration",
        ], scale=0.86, box=3)
        # --- Band 3: Effects of Floods
        self.next_band(3)
        self.write_rows(3, "Effects of Floods", [
            "Drowning, often while crossing water",
            "Cholera, typhoid and diarrhoea",
            "Homes lost; port and roads damaged",
            "Topsoil washed away; dams silted up",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Too Much Water, Too Fast
        self.next_band(4)
        self.write_rows(4, "Too Much Water, Too Fast", [
            "Water over dry land",
            "Soak in slowly or run off fast",
            "Flash floods: minutes",
        ], scale=0.86, box=0)
        # --- Band 5: Why Floods Happen
        self.next_band(5)
        self.write_rows(5, "Why Floods Happen", [
            "Heavy rain, full ground",
            "Bare land runs off fast",
            "Roofs, roads and blocked drains",
        ], scale=0.86, box=0)
        # --- Band 6: What Floods Do
        self.next_band(6)
        self.write_rows(6, "What Floods Do", [
            "Drowning and disease",
            "Homes, roads and bridges lost",
            "If it's flooded, forget it",
        ], scale=0.86, box=0)
        self.wait(4)
