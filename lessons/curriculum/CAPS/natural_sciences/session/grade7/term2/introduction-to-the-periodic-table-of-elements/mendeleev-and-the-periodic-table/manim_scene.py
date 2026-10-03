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

# Band-layout whiteboard scene for mendeleev-and-the-periodic-table (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (140/160/160/120/120/120 of 820 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MendeleevAndThePeriodicTableSession(MovingCameraScene):
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Elements
        self.write_rows(0, "Elements", [
            "Element: one kind of atom; cannot be broken down",
            "Compound: elements chemically joined (water)",
            "118 known; about 90 natural",
            "Similar families: lithium, sodium, potassium",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Mendeleev, 1869
        self.next_band(1)
        self.write_rows(1, "Mendeleev, 1869", [
            "63 elements on cards, in order of atomic mass",
            "New row when properties repeat; families in columns",
            "Left gaps and predicted missing elements",
            "Gallium 1875, scandium 1879, germanium 1886",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Left, right and the staircase
        self.next_band(2)
        self.write_rows(2, "Left, right and the staircase", [
            "Periods: rows (7); groups: columns (18)",
            "Metals left and centre (about 3/4)",
            "Non-metals far right (plus hydrogen)",
            "Semi-metals on the staircase: boron, silicon",
        ], scale=0.88, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Mendeleev used atomic number''",
            "``Non-metals are on the left''",
            "``Hydrogen is a metal''",
            "``Water is an element''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Building blocks
        self.next_band(4)
        self.write_rows(4, "Building blocks", [
            "Element: one kind of atom",
            "Compound: elements joined (water)",
            "118 elements",
            "Some elements are like families",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): The puzzle with missing pieces
        self.next_band(5)
        self.write_rows(5, "The puzzle with missing pieces", [
            "Cards in order; new row when behaviour repeats",
            "Empty spaces for undiscovered elements",
            "Gallium matched his prediction",
            "Prediction proved the pattern was real",
        ], scale=0.82, box=1)

        # --- Band 6 (subtopic_6): Reading the map
        self.next_band(6)
        self.write_rows(6, "Reading the map", [
            "Rows = periods; columns = groups (families)",
            "Left of the staircase: metals",
            "Right: non-metals; on it: semi-metals",
            "Hydrogen: top left, but a non-metal",
        ], scale=0.88, box=3)

        last = Tex("Metals left, non-metals right, semi-metals on the staircase between.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
