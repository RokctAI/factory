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

# Band-layout whiteboard scene for separating-mixtures (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/240/240/220/180/190/180 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SeparatingMixturesSession(MovingCameraScene):
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
        self.write_rows(0, 'Separate by physical means', [
            'Mixture: parts not joined, keep their properties',
            'Use: size, magnetism, density, solubility, boiling point',
            'Solution: solute dissolved in solvent',
            'Sand, salt, iron: magnet, dissolve, filter, evaporate',
        ], scale=0.78, box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, 'Solids and insoluble substances', [
            'Hand sorting, sieving, magnet, decanting',
            'Filtration: residue stays, filtrate passes',
            'Dissolved salt passes through the paper',
            'Evaporation; crystallisation for pure crystals',
        ], scale=0.8, box=1)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, 'Liquids and dissolved substances', [
            'Distillation: boil, condense, collect pure liquid',
            'Fractional: ethanol 78$^\\circ$C, water 100$^\\circ$C; crude oil; air',
            'Separating funnel: oil and water layers',
            'Chromatography: pencil line, spot above solvent',
        ], scale=0.76, box=0)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, 'Separation at scale', [
            'Water: screen, settle, sand filter, chlorine',
            'Gold panning; diamonds on grease tables',
            'Centrifuge: blood cells and plasma',
            'Method, property, where each part goes',
        ], scale=0.8, box=0)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = [
            "``Filtering removes salt''",
            "``Residue passes through the paper''",
            "``Chlorine filters the water''",
            "``Mixtures need a chemical reaction to separate''",
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
        self.write_rows(5, 'Use the difference', [
            'Not joined, so no chemistry needed',
            'Size, magnet, weight, dissolving, boiling',
            'Order: magnet, water, filter, boil',
        ], scale=0.85, box=2)

        # --- Band 6 (subtopic_6)
        self.next_band(6)
        self.write_rows(6, 'Sieve, filter, boil', [
            'Mud stays: residue. Clear water: filtrate',
            'Boil off water: salt stays',
            'Catch the steam: pure water',
        ], scale=0.85, box=2)

        # --- Band 7 (subtopic_7)
        self.next_band(7)
        self.write_rows(7, 'From muddy river to clean tap', [
            'Screen, settle, sand filter, chlorine',
            'Gold sinks; diamonds stick to grease',
            'Spin blood; magnets pick out steel',
        ], scale=0.85, box=0)

        last = Tex('Find the difference, and use it.').scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
