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

# Band-layout whiteboard scene for mixtures-and-mechanical-separation (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/150/170/120/120/120 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MixturesAndMechanicalSeparationSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a mixture is
        self.write_rows(0, "What a mixture is", [
            "Mixture: substances not chemically joined, keep properties",
            "Air, sea water, soil, muesli",
            "Compound: elements joined in a fixed ratio (salt)",
            "Solution: solute dissolved in solvent",
        ], scale=0.76, box=0)

        # --- Band 1 (subtopic_2): Sorting, sieving, magnets
        self.next_band(1)
        self.write_rows(1, "Sorting, sieving, magnets", [
            "Hand sorting: big, different-looking pieces",
            "Sieving: size; small through, big stays",
            "Magnets: iron, steel, nickel, cobalt only",
            "Panning and winnowing: density",
        ], scale=0.88, box=2)

        # --- Band 2 (subtopic_3): Filtration and planning
        self.next_band(2)
        self.write_rows(2, "Filtration and planning", [
            "Filter: liquid through, insoluble solid trapped",
            "Filtrate passes through; residue stays",
            "Filtration cannot remove dissolved salt or germs",
            "Beans, magnet, dissolve, filter, evaporate",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Filtering removes dissolved salt''",
            "``All metals stick to magnets''",
            "``Salt water is a compound''",
            "``Filtered water is always safe''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Mixed, not joined
        self.next_band(4)
        self.write_rows(4, "Mixed, not joined", [
            "Mixture: mixed, not joined",
            "Each part stays itself",
            "Solution: something dissolved (sugar in tea)",
            "Soluble dissolves; insoluble does not",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Big, small and magnetic
        self.next_band(5)
        self.write_rows(5, "Big, small and magnetic", [
            "Big and different: pick out by hand",
            "Different sizes: sieve",
            "Iron and steel: magnet",
            "Heavy gold stays in the pan",
        ], scale=0.88, box=2)

        # --- Band 6 (subtopic_6): Through the filter
        self.next_band(6)
        self.write_rows(6, "Through the filter", [
            "Water through; sand stays",
            "Filtrate comes through; residue stays",
            "Dissolved salt and germs pass through",
            "Beans, magnet, dissolve, filter, dry",
        ], scale=0.88, box=3)

        last = Tex("Use the difference: size, magnetism or solubility pulls a mixture apart.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
