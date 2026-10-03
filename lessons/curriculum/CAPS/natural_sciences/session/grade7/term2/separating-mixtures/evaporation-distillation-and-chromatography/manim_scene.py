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

# Band-layout whiteboard scene for evaporation-distillation-and-chromatography (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (140/150/180/120/120/120 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EvaporationDistillationAndChromatographySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Evaporation and crystallisation
        self.write_rows(0, "Evaporation and crystallisation", [
            "Evaporation: liquid to gas below boiling point",
            "Salt water in a dish: water goes, salt stays",
            "The liquid is lost to the air",
            "Salt pans; sugar mills; slow cooling = bigger crystals",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Distillation
        self.next_band(1)
        self.write_rows(1, "Distillation", [
            "Boil, then condense the vapour in a condenser",
            "Distillate collected; salt left in the flask",
            "Evaporation loses the liquid; distillation keeps it",
            "Uses: pure water, desalination, crude oil, buchu oil",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Chromatography and choosing
        self.next_band(2)
        self.write_rows(2, "Chromatography and choosing", [
            "Ink spot on a pencil line, above the solvent",
            "Dyes travel different distances: chromatogram",
            "Uses: food colours, drug tests, forensics",
            "Size: sieve; magnet; filter; evaporate; distil; chromatograph",
        ], scale=0.76, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Evaporation collects the water''",
            "``Distillation is just evaporation''",
            "``Draw the start line in pen''",
            "``Black ink is a pure substance''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Let the Sun do it
        self.next_band(4)
        self.write_rows(4, "Let the Sun do it", [
            "Seawater in shallow pans",
            "Sun and wind dry the water away",
            "Salt stays; water is lost to the air",
            "Slow drying: bigger crystals (sugar)",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Catch the steam
        self.next_band(5)
        self.write_rows(5, "Catch the steam", [
            "Boil: steam rises, salt stays",
            "Steam hits the cool lid: pure water drops",
            "Condenser: the cold tube",
            "Refineries and buchu oil use distillation",
        ], scale=0.88, box=1)

        # --- Band 6 (subtopic_6): The hidden colours
        self.next_band(6)
        self.write_rows(6, "The hidden colours", [
            "Ink dot on a pencil line, water below it",
            "Colours travel at different speeds",
            "Black ink was a mixture",
            "Food tests, drug tests, crime labs",
        ], scale=0.88, box=1)

        last = Tex("Evaporate to keep the solid, distil to keep the liquid, chromatograph to see the colours.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
