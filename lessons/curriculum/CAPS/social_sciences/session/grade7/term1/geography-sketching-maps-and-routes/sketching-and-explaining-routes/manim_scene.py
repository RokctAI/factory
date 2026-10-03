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

# Band-layout whiteboard scene for sketching-and-explaining-routes (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/200/180/190/90/90/90 of 1030 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SketchingAndExplainingRoutesSession(MovingCameraScene):
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
        # --- Band 0: What a Route Map Needs
        self.write_rows(0, "What a Route Map Needs", [
            "Title, start, end, route line",
            "North arrow, key, distances",
            "Landmarks at the turning points",
            "Leave out what distracts",
        ], scale=0.86, box=2)
        # --- Band 1: Sketching a Route Step by Step
        self.next_band(1)
        self.write_rows(1, "Sketching a Route Step by Step", [
            "Plan: walk it, note turns and landmarks",
            "North arrow, then start and end",
            "Roads in rough proportion",
            "Landmarks, route line, key, title",
        ], scale=0.86, box=1)
        # --- Band 2: Explaining a Route in Words
        self.next_band(2)
        self.write_rows(2, "Explaining a Route in Words", [
            "Start and which way to face",
            "Compass directions with left and right",
            "Landmarks at every turn",
            "Distances or times, never just a bit",
        ], scale=0.86, box=3)
        # --- Band 3: Estimating Distances Along a Route
        self.next_band(3)
        self.write_rows(3, "Estimating Distances Along a Route", [
            "About 1500 steps make a kilometre",
            "Walking: about 1 km in 12 to 15 minutes",
            "Soccer field: about 100 metres",
            "Round sensibly and give units",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Drawing the Way
        self.next_band(4)
        self.write_rows(4, "Drawing the Way", [
            "North arrow, start and end",
            "Landmarks at every turn",
            "Bold route line with arrows",
        ], scale=0.86, box=0)
        # --- Band 5: Saying the Way
        self.next_band(5)
        self.write_rows(5, "Saying the Way", [
            "Step by step, in order",
            "Left or right, plus the compass point",
            "No fuzzy words",
        ], scale=0.86, box=0)
        # --- Band 6: How Far Is It?
        self.next_band(6)
        self.write_rows(6, "How Far Is It?", [
            "About 1500 steps: 1 km",
            "About 15 minutes walking: 1 km",
            "Round it and say the unit",
        ], scale=0.86, box=0)
        self.wait(4)
