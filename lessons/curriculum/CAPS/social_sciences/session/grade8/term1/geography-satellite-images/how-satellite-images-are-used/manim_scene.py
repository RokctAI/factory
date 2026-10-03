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

# Band-layout whiteboard scene for how-satellite-images-are-used (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/200/280/290/150/150/150 of 1410 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class HowSatelliteImagesAreUsedSession(MovingCameraScene):
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
        # --- Band 0: Satellites and remote sensing
        self.write_rows(0, "Satellites and remote sensing", [
            "Remote sensing: information without touching",
            "Sensors record reflected and emitted energy",
            "Landsat since 1972; Meteosat since 1977",
            "SANSA ground station at Hartebeesthoek",
        ], scale=0.86, box=1)
        # --- Band 1: Two kinds of orbit
        self.next_band(1)
        self.write_rows(1, "Two kinds of orbit", [
            "Geostationary: about 36 000 km above the equator",
            "Sees Africa every 15 minutes: weather",
            "Polar-orbiting: about 700 km, pole to pole",
            "Fine detail, revisits every few days",
        ], scale=0.86, box=1)
        # --- Band 2: Pixels, resolution and colour
        self.next_band(2)
        self.write_rows(2, "Pixels, resolution and colour", [
            "Landsat pixel 30 m: soccer field about 3 by 2 pixels",
            "Sentinel-2 pixel 10 m: about 10 by 7 pixels",
            "True colour: red, green, blue",
            "False colour: near-infrared shown red, so plants glow red",
        ], scale=0.8, box=3)
        # --- Band 3: Uses in South Africa
        self.next_band(3)
        self.write_rows(3, "Uses in South Africa", [
            "Cold fronts, storms and cyclones",
            "Fires, floods and the 2018 Cape Town drought",
            "Crops, settlements and invasive plants",
            "Not a map; not GPS; always check the date",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A camera very high up
        self.next_band(4)
        self.write_rows(4, "A camera very high up", [
            "High satellite: watches the weather",
            "Low satellite: sees the detail",
            "SANSA catches the pictures near Pretoria",
        ], scale=0.86)
        # --- Band 5: A picture made of dots
        self.next_band(5)
        self.write_rows(5, "A picture made of dots", [
            "Pixels: tiny squares of ground",
            "30 m squares: the field, not the goalposts",
            "Invisible near-infrared coloured red: healthy plants",
        ], scale=0.8, box=2)
        # --- Band 6: Satellites at work
        self.next_band(6)
        self.write_rows(6, "Satellites at work", [
            "Weather warnings and fire alerts",
            "Shrinking dams and flooded areas",
            "Healthy and struggling crops",
        ], scale=0.86, box=0)
        self.wait(4)
