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

# Band-layout whiteboard scene for introduction-and-map-skills-review (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (270/240/240/270/150/150/160 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class IntroductionAndMapSkillsReviewSession(MovingCameraScene):
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
        # --- Band 0: Grade 8 Social Sciences: two disciplines
        self.write_rows(0, "Grade 8 Social Sciences: two disciplines", [
            "Geography: where things are, and why there",
            "History: change over time, from evidence",
            "Term 1 maps and globes; Term 2 climate; Term 3 settlement; Term 4 transport",
            "Formal tasks: map test, controlled test, project, examination",
        ], scale=0.72, box=0)
        # --- Band 1: Street maps: grid, index, key
        self.next_band(1)
        self.write_rows(1, "Street maps: grid, index, key", [
            "Columns A, B, C...; rows 1, 2, 3...",
            "Letter first: square C4",
            "Index: street name, then grid square",
            "Read the key before the map",
        ], scale=0.86, box=1)
        # --- Band 2: Word scale, line scale
        self.next_band(2)
        self.write_rows(2, "Word scale, line scale", [
            "Word scale: 1 cm represents 2 km",
            "Line scale: a ruler printed on the map",
            "Photocopy the map: only the line scale stays correct",
            "Large scale = small area, much detail",
        ], scale=0.8, box=3)
        # --- Band 3: Measure, multiply, state
        self.next_band(3)
        self.write_rows(3, "Measure, multiply, state", [
            "6,5 cm $\\times$ 2 = 13 km",
            "4,8 cm $\\times$ 250 m = 1 200 m = 1,2 km",
            "Winding road: string, 9,2 cm $\\times$ 5 = 46 km",
            "Line scale 2 cm = 1 km: 7 cm is 3,5 km",
        ], scale=0.86, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Two lenses on one world
        self.next_band(4)
        self.write_rows(4, "Two lenses on one world", [
            "Geography asks where; History asks when and why",
            "Four terms, four stops",
            "Sources are evidence from the past",
        ], scale=0.86)
        # --- Band 5: Your walk to school, from above
        self.next_band(5)
        self.write_rows(5, "Your walk to school, from above", [
            "Squares like a chessboard, letter first",
            "Index works like a contacts list",
            "Stand at the start, look at the target",
        ], scale=0.86, box=1)
        # --- Band 6: From ruler to real kilometres
        self.next_band(6)
        self.write_rows(6, "From ruler to real kilometres", [
            "Measure, multiply, say the unit",
            "Bendy road: follow it with string",
            "Suburb map: large scale. World map: small scale",
        ], scale=0.86, box=0)
        self.wait(4)
