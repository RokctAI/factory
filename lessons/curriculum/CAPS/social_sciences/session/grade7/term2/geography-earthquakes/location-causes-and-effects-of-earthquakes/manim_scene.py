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

# Band-layout whiteboard scene for location-causes-and-effects-of-earthquakes (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/200/190/220/90/90/100 of 1080 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LocationCausesAndEffectsOfEarthquakesSession(MovingCameraScene):
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
        # --- Band 0: What Causes an Earthquake
        self.write_rows(0, "What Causes an Earthquake", [
            "Plates lock, stress builds, rocks snap",
            "Energy spreads as seismic waves",
            "Focus underground; epicentre above it",
            "Aftershocks can last for months",
        ], scale=0.86, box=2)
        # --- Band 1: Where Earthquakes Happen and How They Are Measured
        self.next_band(1)
        self.write_rows(1, "Where Earthquakes Happen and How They Are Measured", [
            "Earthquakes follow plate boundaries",
            "Ring of Fire: about 80 percent of the largest",
            "Magnitude: energy; each step about 32 times",
            "Intensity: effects at a place, I to XII",
        ], scale=0.8, box=2)
        # --- Band 2: Effects on People
        self.next_band(2)
        self.write_rows(2, "Effects on People", [
            "Most deaths: collapsing buildings",
            "Broken roads, pipes and power lines",
            "Fires, disease and landslides",
            "Displacement and economic loss",
        ], scale=0.86, box=1)
        # --- Band 3: Tsunamis and Why Effects Differ
        self.next_band(3)
        self.write_rows(3, "Tsunamis and Why Effects Differ", [
            "Undersea earthquake lifts the sea floor",
            "Up to 800 km/h; giant at the coast",
            "Warning sign: the sea draws back",
            "Effects depend on buildings and wealth",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Snap!
        self.next_band(4)
        self.write_rows(4, "Snap!", [
            "Bend, bend, snap",
            "Focus below, epicentre above",
            "Aftershocks follow",
        ], scale=0.86, box=0)
        # --- Band 5: Where and How Big
        self.next_band(5)
        self.write_rows(5, "Where and How Big", [
            "Ring of Fire and the Himalayan belt",
            "Seismographs record shaking",
            "Each step: about 32 times stronger",
        ], scale=0.86, box=0)
        # --- Band 6: What Earthquakes Do
        self.next_band(6)
        self.write_rows(6, "What Earthquakes Do", [
            "Falling buildings, fires, disease",
            "Homes lost, tents for months",
            "Sea pulls back: run uphill",
        ], scale=0.86, box=0)
        self.wait(4)
