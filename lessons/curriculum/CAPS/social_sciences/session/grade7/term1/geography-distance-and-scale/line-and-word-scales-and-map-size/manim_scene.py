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

# Band-layout whiteboard scene for line-and-word-scales-and-map-size (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/160/170/180/90/90/90 of 930 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LineAndWordScalesAndMapSizeSession(MovingCameraScene):
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
        # --- Band 0: What Scale Means
        self.write_rows(0, "What Scale Means", [
            "Scale: map distance compared to ground distance",
            "1 cm to 1 km: 4 cm means 4 km",
            "100 cm in 1 m; 1000 m in 1 km",
            "Bigger reduction, less detail",
        ], scale=0.8, box=1)
        # --- Band 1: Word Scales
        self.next_band(1)
        self.write_rows(1, "Word Scales", [
            "Word scale: 1 cm represents 5 km",
            "7 cm times 5 km equals 35 km",
            "3.5 cm times 200 m equals 700 m",
            "Enlarge the map: the words go wrong",
        ], scale=0.86, box=1)
        # --- Band 2: Line Scales
        self.next_band(2)
        self.write_rows(2, "Line Scales", [
            "Line scale: a bar divided and labelled",
            "Grows and shrinks with the map",
            "Paper strip: mark, lay on, read",
            "0 to 20 km measures 4 cm: 1 cm is 5 km",
        ], scale=0.86, box=1)
        # --- Band 3: Large-Scale and Small-Scale Maps
        self.next_band(3)
        self.write_rows(3, "Large-Scale and Small-Scale Maps", [
            "Large scale: small area, lots of detail",
            "Small scale: large area, little detail",
            "On a large-scale map things look large",
            "Choose the scale for the purpose",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Shrinking the World
        self.next_band(4)
        self.write_rows(4, "Shrinking the World", [
            "Scale: how much the world was shrunk",
            "1 cm to 1 km: 6 cm is 6 km",
            "Shrink a lot, lose detail",
        ], scale=0.86, box=0)
        # --- Band 5: Scales in Words and Lines
        self.next_band(5)
        self.write_rows(5, "Scales in Words and Lines", [
            "Word scale: measure and multiply",
            "Line scale: paper strip from zero",
            "Copy it bigger: the line still works",
        ], scale=0.86, box=0)
        # --- Band 6: Big Scale, Small Scale
        self.next_band(6)
        self.write_rows(6, "Big Scale, Small Scale", [
            "Large scale: small area, things look large",
            "Small scale: big area, things look small",
            "Pick the map for the job",
        ], scale=0.86, box=0)
        self.wait(4)
