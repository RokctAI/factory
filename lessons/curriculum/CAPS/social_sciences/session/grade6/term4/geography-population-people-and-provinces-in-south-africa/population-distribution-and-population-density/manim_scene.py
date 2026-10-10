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

# Band-layout whiteboard scene for population-distribution-and-population-density (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (230/170/130/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PopulationDistributionAndPopulationDensitySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Population Distribution
        self.write_rows(0, "Population Distribution", [
            "Distribution: the pattern",
            "Dense and sparse",
            "Dot map: one dot, many people",
            "Clusters in Gauteng",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Population Density
        self.next_band(1)
        self.write_rows(1, "Population Density", [
            "Density: people per square km",
            "Population divided by area",
            "20000 / 10 = 2000",
            "South Africa: about 50",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Why South Africa's Population Is Spread Unevenly
        self.next_band(2)
        self.write_rows(2, "Why South Africa's Population Is Spread Unevenly", [
            "Rain in the east",
            "Jobs in Gauteng and ports",
            "Homelands and townships",
            "Dry west: few people",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Distribution equals density''",
            "``Density is the total''",
            "``Averages mean evenly spread''",
            "``One dot is one person''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The Pattern of People
        self.next_band(4)
        self.write_rows(4, "The Pattern of People", [
            "Pattern",
            "Dots",
            "Dense",
            "Sparse",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): People per Square Kilometre
        self.next_band(5)
        self.write_rows(5, "People per Square Kilometre", [
            "People",
            "Area",
            "Divide",
            "Average",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Rain, Jobs and History
        self.next_band(6)
        self.write_rows(6, "Rain, Jobs and History", [
            "Rain",
            "Jobs",
            "History",
            "West",
        ], scale=0.9, box=2)

        last = Tex("Distribution shows where people live, density shows how crowded it is, and in South Africa rain, jobs and history explain the pattern.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
