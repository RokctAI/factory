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

# Band-layout whiteboard scene for calculating-direct-distances (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/180/220/200/90/90/90 of 1040 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CalculatingDirectDistancesSession(MovingCameraScene):
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
        # --- Band 0: Direct Distance: As the Crow Flies
        self.write_rows(0, "Direct Distance: As the Crow Flies", [
            "Direct distance: straight line, point to point",
            "As the crow flies",
            "Always shorter than, or equal to, the road",
            "Measure from the centres of the symbols",
        ], scale=0.8, box=1)
        # --- Band 1: Estimating With the Scale
        self.next_band(1)
        self.write_rows(1, "Estimating With the Scale", [
            "Estimate first, measure second",
            "How many scale bars fit the gap?",
            "A finger is about 1.5 to 2 cm",
            "South Africa: about 1600 km across",
        ], scale=0.86, box=0)
        # --- Band 2: Measuring and Calculating Accurately
        self.next_band(2)
        self.write_rows(2, "Measuring and Calculating Accurately", [
            "1. Measure in cm, from the centres",
            "2. Write the scale",
            "3. Multiply",
            "4. Answer with unit; compare with estimate",
        ], scale=0.86, box=2)
        # --- Band 3: Checking and the Error Museum
        self.next_band(3)
        self.write_rows(3, "Checking and the Error Museum", [
            "Check with the estimate and the units",
            "Measure again, from the other end",
            "1 mm can be 10 km on a small-scale map",
            "Show distance, scale, sum, answer",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: As the Crow Flies
        self.next_band(4)
        self.write_rows(4, "As the Crow Flies", [
            "Straight line, like a bird",
            "Roads bend, so roads are longer",
            "Measure from the centre of the dots",
        ], scale=0.86, box=0)
        # --- Band 5: Guess, Then Measure
        self.next_band(5)
        self.write_rows(5, "Guess, Then Measure", [
            "Guess with the scale bar",
            "Ruler zero on the first dot",
            "Centimetres times the scale",
        ], scale=0.86, box=0)
        # --- Band 6: Does It Make Sense?
        self.next_band(6)
        self.write_rows(6, "Does It Make Sense?", [
            "Close to your guess?",
            "Unit written?",
            "Distance, scale, sum, answer",
        ], scale=0.86, box=0)
        self.wait(4)
