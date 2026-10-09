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

# Band-layout whiteboard scene for revision-of-term-3-topics (Part 1 Expert
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


class RevisionOfTerm3TopicsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Fractions
        self.write_rows(0, "Fractions", [
            "3/8 sold, 5/8 left",
            "3/4 = 6/8, more than 5/8",
            "2/8 + 3/8 = 5/8",
            "3/4 of 24 is 18",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Data and Probability
        self.next_band(1)
        self.write_rows(1, "Data and Probability", [
            "15 + 10 + 9 + 6 = 40",
            "Scale from 0, equal steps",
            "Half of 40 is 20, a quarter is 10",
            "Coin: about half heads, no memory",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Mass and Transformations
        self.next_band(2)
        self.write_rows(2, "Mass and Transformations", [
            "1 kg = 1 000 g",
            "2 kg 30 g = 2 030 g",
            "6 bags of 250 g: 1 500 g",
            "Squares tessellate, circles do not",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``2/8 + 3/8 = 5/16''",
            "``Scale starts at 6''",
            "``2 kg 30 g = 2 300 g''",
            "``Circles tessellate''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): At the Cake Stall: Fractions
        self.next_band(4)
        self.write_rows(4, "At the Cake Stall: Fractions", [
            "3/8 sold, 5/8 left",
            "3/4 = 6/8",
            "Add tops, keep bottom",
            "3/4 of 24 = 18",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): At the Survey Table: Data and Chance
        self.next_band(5)
        self.write_rows(5, "At the Survey Table: Data and Chance", [
            "Tally, total 40",
            "Scale from 0",
            "Pie: half is 20",
            "Coin has no memory",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): At the Scale and the Tiles: Mass and Shapes
        self.next_band(6)
        self.write_rows(6, "At the Scale and the Tiles: Mass and Shapes", [
            "Half kg: 500 g",
            "Quarter kg: 250 g",
            "No gaps, no overlaps",
            "House shape: 1 line",
        ], scale=0.9, box=2)

        last = Tex("Fractions, data, chance, mass and shapes: draw it, label it, total it, check it.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
