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

# Band-layout whiteboard scene for lifestyles-in-modern-and-rural-societies (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-6). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (360/170/180/180/210/160 of 1260 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LifestylesInModernAndRuralSocietiesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.78, box=None):
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
            self.play(Create(SurroundingRectangle(made[box], color=YELLOW)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, "Standard of living", [
            "Material well-being: goods and services",
            "Depends on income and access to services",
            "Quality of life adds health, safety, community",
            "Indicators: income per person, services, HDI",
        ], box=2)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Modern urban lifestyles", [
            "Specialised wage jobs",
            "Almost everything bought with money",
            "Better services, more choice",
            "High rent, long commutes, crime",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Rural lifestyles", [
            "Subsistence farming, grants, remittances",
            "Longer distances to services",
            "Fewer jobs, higher poverty",
            "Own land, food, strong community",
        ], box=0)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Comparing and urbanisation", [
            "Compare under headings",
            "Push: no jobs, drought, poor services",
            "Pull: jobs, schools, amenities",
            "Influx control abolished in 1986",
        ], box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Two cousins", [
            "City: more income and services",
            "Village: own home, food, neighbours",
            "Standard of living counts what you buy",
            "Quality of life counts how life feels",
        ], box=3)

        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "The long taxi ride", [
            "Urbanisation: village to city",
            "Remittances sent home",
            "Informal settlements if houses lag",
            "Make both places better",
        ], box=1)

        self.wait(4)
