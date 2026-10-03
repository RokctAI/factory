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

# Band-layout whiteboard scene for commuter-costs-congestion-and-pollution (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (290/280/230/270/130/130/130 of 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CommuterCostsCongestionPollutionSession(MovingCameraScene):
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
        # --- Band 0: Cost of commuting
        self.write_rows(0, "Cost of commuting", [
            "Fares, fuel, insurance, parking",
            "Poorest pay the biggest share",
            "Hours lost each day",
            "Late workers cost businesses",
        ], scale=0.86, box=1)
        # --- Band 1: Congestion
        self.next_band(1)
        self.write_rows(1, "Congestion", [
            "Morning and afternoon peaks",
            "Cars with one person",
            "Accidents and roadworks",
            "Lost time and wasted fuel",
        ], scale=0.86, box=1)
        # --- Band 2: Pollution
        self.next_band(2)
        self.write_rows(2, "Pollution", [
            "Carbon monoxide and particles",
            "Smog and winter inversions",
            "Asthma and bronchitis",
            "Noise and runoff",
        ], scale=0.86, box=1)
        # --- Band 3: The fuel bill
        self.next_band(3)
        self.write_rows(3, "The fuel bill", [
            "30 x 2 x 22 = 1 320 km",
            "1 320 $\\div$ 100 x 8 = 105.6 L",
            "105.6 x 22 = R2 323.20",
            "Lift club of four: R580.80",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Paying to get to work
        self.next_band(4)
        self.write_rows(4, "Paying to get to work", [
            "Money and time",
        ], scale=0.86, box=0)
        # --- Band 5: Stuck in traffic
        self.next_band(5)
        self.write_rows(5, "Stuck in traffic", [
            "Too many cars",
        ], scale=0.86, box=0)
        # --- Band 6: Dirty air and noise
        self.next_band(6)
        self.write_rows(6, "Dirty air and noise", [
            "Smog harms health",
        ], scale=0.86, box=0)
        self.wait(4)
