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

# Band-layout whiteboard scene for results-for-the-ashanti-and-britain (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (260/290/250/240/130/130/130 of 1430 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ResultsForAshantiAndBritainSession(MovingCameraScene):
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
            "Indirect rule through chiefs",
            "Confederacy restored, 1935",
            "The stool stays safe",
        ], scale=0.86, box=0)
        # --- Band 1: Economic results
        self.next_band(1)
        self.write_rows(1, "Economic results", [
            "Cocoa: Tetteh Quarshie, 1879",
            "Largest producer by about 1911",
            "Gold at Obuasi",
            "Railways to the coast",
        ], scale=0.86, box=1)
        # --- Band 2: Social results, independence
        self.next_band(2)
        self.write_rows(2, "Social results, independence", [
            "Missions and Achimota",
            "Ex-servicemen, 1948",
            "Nkrumah and the CPP",
            "Ghana, 6 March 1957",
        ], scale=0.86, box=3)
        # --- Band 3: Weighing results
        self.next_band(3)
        self.write_rows(3, "Weighing results", [
            "40 000 $\\div$ 20 = 2 000 tonnes",
            "1957 - 1901 = 56 years",
            "Who gained, who lost?",
            "Model colony?",
        ], scale=0.86, box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Ruled from outside
        self.next_band(4)
        self.write_rows(4, "Ruled from outside", [
            "Chiefs under British officers",
        ], scale=0.86, box=0)
        # --- Band 5: Cocoa and gold
        self.next_band(5)
        self.write_rows(5, "Cocoa and gold", [
            "Farmers and companies",
        ], scale=0.86, box=0)
        # --- Band 6: Freedom in 1957
        self.next_band(6)
        self.write_rows(6, "Freedom in 1957", [
            "Ghana is born",
        ], scale=0.86, box=0)
        self.wait(4)
