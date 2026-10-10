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

# Band-layout whiteboard scene for melting-freezing-evaporating-and-condensing (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (140/160/170/110/110/110 of 800 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MeltingFreezingEvaporatingAndCondensingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Melting and Freezing
        self.write_rows(0, "Melting and Freezing", [
            "Heat a solid: melting",
            "Ice lolly melts in the sun",
            "Cool a liquid: freezing",
            "Water freezes at 0 degrees",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Evaporating and Condensing
        self.next_band(1)
        self.write_rows(1, "Evaporating and Condensing", [
            "Heat a liquid: evaporating",
            "Washing dries, water boils",
            "Cool a gas: condensing",
            "Drops on a lid and cold glass",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Heating and Cooling Change the State
        self.next_band(2)
        self.write_rows(2, "Heating and Cooling Change the State", [
            "Heating: melt, evaporate",
            "Cooling: condense, freeze",
            "Same material, new state",
            "Wax melts and solidifies",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The cold glass is leaking''",
            "``The white cloud is vapour''",
            "``Melted ice is a new material''",
            "``Freezing needs heating''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Ice to Water and Back
        self.next_band(4)
        self.write_rows(4, "Ice to Water and Back", [
            "Ice to water and back",
            "Heat: melts",
            "Cool: freezes",
            "Also called solidifying",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Water to Vapour and Back
        self.next_band(5)
        self.write_rows(5, "Water to Vapour and Back", [
            "Water to vapour and back",
            "Heat: evaporates",
            "Cool: condenses",
            "Vapour is invisible",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Hot and Cold
        self.next_band(6)
        self.write_rows(6, "Hot and Cold", [
            "Hot and cold",
            "Heat: melt, evaporate",
            "Cool: condense, freeze",
            "Still the same material",
        ], scale=0.9, box=3)

        last = Tex("Heating melts and evaporates; cooling condenses and freezes; the material stays the same.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
