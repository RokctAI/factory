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

# Band-layout whiteboard scene for elements-symbols-and-atomic-numbers (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (140/150/170/120/120/120 of 820 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ElementsSymbolsAndAtomicNumbersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Names and symbols
        self.write_rows(0, "Names and symbols", [
            "One or two letters: first Capital, second small",
            "Co = cobalt; CO = carbon monoxide",
            "H, He, C, N, O, Mg, Al, Si, S, Cl, Ca, Zn",
            "Latin: Na, K, Fe, Cu, Ag, Au, Sn, Pb, Hg",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Atomic number
        self.next_band(1)
        self.write_rows(1, "Atomic number", [
            "Atom: nucleus (protons, neutrons) + electrons",
            "Atomic number = number of protons; the identity card",
            "Square: 6, C, carbon, 12",
            "H 1 ... O 8 ... Na 11 ... Ca 20",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Position on the table
        self.next_band(2)
        self.write_rows(2, "Position on the table", [
            "Period = row (1 to 7); group = column (1 to 18)",
            "Group 1: alkali metals; group 2: alkaline earth",
            "Group 17: halogens; group 18: noble gases",
            "Na: period 3 group 1; Cl: period 3 group 17",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``CA is the symbol for calcium''",
            "``S is the symbol for sodium''",
            "``Atomic number is the atomic mass''",
            "``Chemistry can turn lead into gold''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Short names
        self.next_band(4)
        self.write_rows(4, "Short names", [
            "First letter capital, second letter small",
            "H, O, C, He, Mg",
            "Sneaky Latin: Na, K, Fe, Cu",
            "Ag silver, Au gold, Pb lead (plumber)",
        ], scale=0.88, box=0)

        # --- Band 5 (subtopic_5): The ID number
        self.next_band(5)
        self.write_rows(5, "The ID number", [
            "Atomic number = number of protons",
            "H 1, C 6, O 8, Au 79",
            "Protons decide the element",
            "Squares in order from 1 to 118",
        ], scale=0.88, box=0)

        # --- Band 6 (subtopic_6): Where do you sit?
        self.next_band(6)
        self.write_rows(6, "Where do you sit?", [
            "Row = period; column = group",
            "Group 1 alkali metals; 17 halogens; 18 noble gases",
            "Sodium: period 3, group 1, a metal",
            "Chlorine: period 3, group 17, a non-metal",
        ], scale=0.82, box=1)

        last = Tex("Name, symbol, atomic number, position: four facts in every square.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
