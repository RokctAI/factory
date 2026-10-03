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

# Band-layout whiteboard scene for migrant-labour-and-closed-compounds (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/230/260/230/150/150/150 of 1430 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MigrantLabourAndClosedCompoundsSession(MovingCameraScene):
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
        # --- Band 0: Why workers came
        self.write_rows(0, "Why workers came", [
            "Migrant labour: work away, return home",
            "Pull: wages, guns, cattle, ploughs",
            "Push: hut tax, land loss, drought",
            "Early bargaining power",
        ], scale=0.86, box=0)
        # --- Band 1: Passes and contracts
        self.next_band(1)
        self.write_rows(1, "Passes and contracts", [
            "Pass laws from 1872",
            "Contract breaking a crime for workers",
            "Stop desertion, keep wages low",
            "Model for later pass laws",
        ], scale=0.86, box=0)
        # --- Band 2: Closed compounds
        self.next_band(2)
        self.write_rows(2, "Closed compounds", [
            "From 1885: fenced barracks",
            "Whole contract inside, searched daily",
            "Reasons given: theft, drink, desertion",
            "White workers exempted after 1884",
        ], scale=0.86, box=3)
        # --- Band 3: Legacy
        self.next_band(3)
        self.write_rows(3, "Legacy", [
            "20 $\\times$ 12 = 240 shillings",
            "8 $\\times$ 12 = 96 back to the store",
            "Copied on the gold mines",
            "Workers resisted",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Walking to the diamonds
        self.next_band(4)
        self.write_rows(4, "Walking to the diamonds", [
            "Work away, then go home",
        ], scale=0.86, box=0)
        # --- Band 5: Papers to work
        self.next_band(5)
        self.write_rows(5, "Papers to work", [
            "No pass, no freedom",
        ], scale=0.86, box=0)
        # --- Band 6: Behind the fence
        self.next_band(6)
        self.write_rows(6, "Behind the fence", [
            "Searched and confined",
        ], scale=0.86, box=0)
        self.wait(4)
