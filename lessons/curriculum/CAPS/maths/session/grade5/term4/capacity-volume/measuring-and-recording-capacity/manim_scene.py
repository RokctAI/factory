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

# Band-layout whiteboard scene for measuring-and-recording-capacity (Part 1 Expert
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


class MeasuringAndRecordingCapacitySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Millilitres, Litres and Measuring Tools
        self.write_rows(0, "Millilitres, Litres and Measuring Tools", [
            "1 l is 1 000 ml",
            "Teaspoon 5 ml, cup 250 ml",
            "Can 330 ml, carton 1 l",
            "Spoons, cups and jugs",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Reading Measuring Jugs
        self.next_band(1)
        self.write_rows(1, "Reading Measuring Jugs", [
            "Flat table, eyes level",
            "Between 700 and 800: 750 ml",
            "Labels every 200: half is 100",
            "Fill spoons level",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Recording, Comparing and Ordering
        self.next_band(2)
        self.write_rows(2, "Recording, Comparing and Ordering", [
            "330 ml, 500 ml, 750 ml",
            "1 l is 1 000 ml, 2 l is 2 000 ml",
            "750 ml is 250 ml less than 1 l",
            "Always write the unit",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Reading from above: 800''",
            "``2 l less than 500 ml''",
            "``750 with no unit''",
            "``Tablespoon for teaspoon''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Spoons, Cups and Jugs
        self.next_band(4)
        self.write_rows(4, "Spoons, Cups and Jugs", [
            "Spoons, cups and jugs",
            "5 ml, 250 ml",
            "1 l is 1 000 ml",
            "Pick the right tool",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Eyes Level With the Line
        self.next_band(5)
        self.write_rows(5, "Eyes Level With the Line", [
            "Eyes level with the line",
            "Flat table",
            "750 ml",
            "Count the steps",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Same Unit, Then Compare
        self.next_band(6)
        self.write_rows(6, "Same Unit, Then Compare", [
            "Same unit, then compare",
            "330, 500, 750",
            "1 000, 2 000",
            "Smallest to largest",
        ], scale=0.9, box=1)

        last = Tex("Choose the right tool, read the jug at eye level, write the unit, and change to the same unit before you compare.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
