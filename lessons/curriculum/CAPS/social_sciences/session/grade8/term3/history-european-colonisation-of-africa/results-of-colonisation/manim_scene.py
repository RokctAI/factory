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

# Band-layout whiteboard scene for results-of-colonisation (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (250/290/310/210/130/130/130 of 1450 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ResultsOfColonisationSession(MovingCameraScene):
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
        # --- Band 0: Political results
        self.write_rows(0, "Political results", [
            "Loss of independence",
            "Borders drawn in Europe",
            "Divided and combined peoples",
            "Nationalism and independence",
        ], scale=0.86, box=1)
        # --- Band 1: Economic results
        self.next_band(1)
        self.write_rows(1, "Economic results", [
            "Export economies",
            "Monoculture",
            "Land loss and forced labour",
            "Railways to the ports",
        ], scale=0.86, box=3)
        # --- Band 2: Social results
        self.next_band(2)
        self.write_rows(2, "Social results", [
            "Missions and Christianity",
            "Mission schools",
            "European languages",
            "Racial hierarchy",
        ], scale=0.86, box=3)
        # --- Band 3: Weighing results
        self.next_band(3)
        self.write_rows(3, "Weighing results", [
            "54 - 4 = 50 countries",
            "Who gained, who lost?",
            "Read sources for purpose",
            "Benefits and costs",
        ], scale=0.86, box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Rulers without power
        self.next_band(4)
        self.write_rows(4, "Rulers without power", [
            "Straight lines on the map",
        ], scale=0.86, box=0)
        # --- Band 5: Raw materials out, goods in
        self.next_band(5)
        self.write_rows(5, "Raw materials out, goods in", [
            "Railways to the ports",
        ], scale=0.86, box=0)
        # --- Band 6: Schools, churches, languages
        self.next_band(6)
        self.write_rows(6, "Schools, churches, languages", [
            "Gains and costs",
        ], scale=0.86, box=0)
        self.wait(4)
