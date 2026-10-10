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

# Band-layout whiteboard scene for reading-pictographs-bar-graphs-and-pie-charts (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/160/160/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ReadingPictographsBarGraphsAndPieChartsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
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
        self.wait(42)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Reading Pictographs and Data in Words
        self.write_rows(0, "Reading Pictographs and Data in Words", [
            "Key: one basket is 4 kilograms",
            "Week 2: 5 baskets, 20 kilograms",
            "Week 3: 4 and a half, 18 kilograms",
            "Total: 58 kilograms",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Reading Bar Graphs
        self.next_band(1)
        self.write_rows(1, "Reading Bar Graphs", [
            "Scale in 3s: 0, 3, 6, up to 21",
            "Volunteers 12, 18, 9, 15, 21",
            "Most minus fewest: 12",
            "Total: 75 volunteers",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Reading Pie Charts and Reading Critically
        self.next_band(2)
        self.write_rows(2, "Reading Pie Charts and Reading Critically", [
            "Pie chart of 40 beds",
            "Half: 20 spinach beds",
            "Quarter: 10 tomato beds",
            "Eighth: 5 beds each",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``5 kilograms, not 20''",
            "``Half basket as a whole: 20''",
            "``Reading the 9 bar as 12''",
            "``An eighth of 40 is 8''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Baskets to Kilograms
        self.next_band(4)
        self.write_rows(4, "Baskets to Kilograms", [
            "Baskets to kilograms",
            "One basket: 4 kilograms",
            "5 baskets: 20 kilograms",
            "Half a basket: 2 kilograms",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Read the Bars
        self.next_band(5)
        self.write_rows(5, "Read the Bars", [
            "Read the bars",
            "Most: 21, fewest: 9",
            "Difference: 12",
            "Total: 75",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Slices of the Garden
        self.next_band(6)
        self.write_rows(6, "Slices of the Garden", [
            "Slices of the garden",
            "Half of 40 is 20",
            "A quarter of 40 is 10",
            "An eighth of 40 is 5",
        ], scale=0.9, box=1)

        last = Tex("Read the title, the key or the scale and the labels first, then turn every symbol, bar and slice into a number you can trust.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
