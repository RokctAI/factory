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

# Band-layout whiteboard scene for revision-of-term-2-topics (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (240/140/150/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RevisionOfTerm2TopicsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Trade and Why People Trade
        self.write_rows(0, "Trade and Why People Trade", [
            "Goods and services",
            "Barter, then money",
            "Exports out, imports in",
            "Raw and manufactured",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Value and Fair Trade
        self.next_band(1)
        self.write_rows(1, "Value and Fair Trade", [
            "Each stage adds value",
            "Cocoa to chocolate",
            "Gold to jewellery",
            "Fair price and premium",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Explorers from Europe
        self.next_band(2)
        self.write_rows(2, "Explorers from Europe", [
            "Renaissance in Italy",
            "Compass, gunpowder, caravel",
            "1488 Dias, 1498 da Gama",
            "1652 van Riebeeck",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Exports come in''",
            "``The cocoa farmer earns most''",
            "``Europeans first linked us to the world''",
            "``Da Gama was first around the Cape''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Buying and Selling
        self.next_band(4)
        self.write_rows(4, "Buying and Selling", [
            "Goods",
            "Services",
            "Exports",
            "Imports",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Adding Value
        self.next_band(5)
        self.write_rows(5, "Adding Value", [
            "Cocoa",
            "Gold",
            "Value",
            "Fair",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Around Africa
        self.next_band(6)
        self.write_rows(6, "Around Africa", [
            "Renaissance",
            "Dias",
            "Da Gama",
            "Cape",
        ], scale=0.9, box=3)

        last = Tex("Trade links people and places all over the world, and the search for new trade routes brought Europeans to southern Africa.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
