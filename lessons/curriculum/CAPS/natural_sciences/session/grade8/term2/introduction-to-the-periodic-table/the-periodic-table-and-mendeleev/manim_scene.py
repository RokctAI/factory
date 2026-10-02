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

# Band-layout whiteboard scene for the-periodic-table-and-mendeleev (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/250/230/220/180/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PeriodicTableMendeleevSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1)
        self.write_rows(0, 'Element: one kind of atom, no simpler substance', [
            '118 known; about 90 occur naturally',
            'Classify: position tells you properties',
            'D\\"obereiner triads 1829: Li, Na, K and Cl, Br, I',
            'Newlands 1865: properties repeat, octaves',
        ], scale=0.8, box=1)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, 'Mendeleev, 1869: 63 elements on cards', [
            'Order of atomic mass; similar properties in columns',
            'Gaps left for undiscovered elements',
            'Eka-silicon predicted 72 and 5.5; germanium 72.6 and 5.35',
            'Moseley 1913: order by atomic number',
        ], scale=0.76, box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, 'Groups and periods', [
            '18 groups down: similar chemical properties',
            '7 periods across: metal to non-metal',
            'Group 1 alkali metals, 17 halogens, 18 noble gases',
            'Cl: Group 17, Period 3. \\ Ca: Group 2, Period 4',
        ], scale=0.8, box=0)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, 'The staircase', [
            'Left and centre: metals, more than three quarters',
            'Top right: non-metals, plus hydrogen',
            'On the staircase: B, Si, Ge, As, Sb, Te',
            'Position predicts properties',
        ], scale=0.8, box=2)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = [
            "``The modern table is ordered by mass''",
            "``Groups are rows''",
            "``Hydrogen is a metal''",
            "``Mendeleev discovered germanium''",
        ]
        for i, e in enumerate(errs):
            m = Tex(e).scale(0.85).shift(band_shift(4) + UP * (1.3 - 1.0 * i))
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5)
        self.next_band(5)
        self.write_rows(5, 'Sorting the supermarket', [
            'Unsorted shop: nothing can be found',
            'Element: one kind of atom',
            'Properties repeat in order: periodic',
        ], scale=0.85, box=2)

        # --- Band 6 (subtopic_6)
        self.next_band(6)
        self.write_rows(6, 'The man who left gaps', [
            'Cards in order, families in columns',
            'Gap below silicon: predicted 72',
            'Germanium 1886: 72.6',
        ], scale=0.85, box=2)

        # --- Band 7 (subtopic_7)
        self.next_band(7)
        self.write_rows(7, 'Reading the map', [
            'Address: group down, period across',
            'Metals left, non-metals top right',
            'Semi-metals on the staircase',
        ], scale=0.85, box=0)

        last = Tex('A list that predicts is a law.').scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
