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

# Band-layout whiteboard scene for monocots-and-dicots (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (120/140/140/120/120/120 of 760 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MonocotsAndDicotsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): One seed leaf or two
        self.write_rows(0, "One seed leaf or two", [
            "Cotyledon = seed leaf of the embryo",
            "Monocot: one (mealie); dicot: two (bean)",
            "Bean splits into two halves; mealie does not",
            "Mealie grain: mostly endosperm, ground into meal",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Leaves, roots, stems
        self.next_band(1)
        self.write_rows(1, "Leaves, roots, stems", [
            "Monocot leaf: narrow, parallel veins",
            "Dicot leaf: broad, net veins",
            "Roots: fibrous (monocot) or tap root (dicot)",
            "Stem bundles: scattered (monocot) or ring (dicot)",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Flowers and the full table
        self.next_band(2)
        self.write_rows(2, "Flowers and the full table", [
            "Monocot flowers: parts in 3s; dicot: 4s or 5s",
            "Monocots: mealie, grass, aloe, agapanthus, strelitzia",
            "Dicots: bean, pumpkin, protea, marula, baobab",
            "Always check several features",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``One feature is enough to decide''",
            "``Grass does not flower''",
            "``All trees are dicots''",
            "``Monocots are not flowering plants''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Team One and Team Two
        self.next_band(4)
        self.write_rows(4, "Team One and Team Two", [
            "Bean splits into two halves: dicot",
            "Mealie does not split: monocot",
            "Mealie grain: one seed leaf + starch store",
            "Both are flowering plants",
        ], scale=0.88, box=0)

        # --- Band 5 (subtopic_5): Read the leaf, pull the roots
        self.next_band(5)
        self.write_rows(5, "Read the leaf, pull the roots", [
            "Train-track veins: monocot",
            "Net veins: dicot",
            "Beard of roots: monocot; one main root: dicot",
            "Woody trees with rings: mostly dicots",
        ], scale=0.82, box=1)

        # --- Band 6 (subtopic_6): Count the petals
        self.next_band(6)
        self.write_rows(6, "Count the petals", [
            "Threes: monocot; fours or fives: dicot",
            "Aloe: thick leaves, but veins, roots and flowers say monocot",
            "Check more than one feature",
            "Mealies, aloes vs beans, proteas",
        ], scale=0.76, box=2)

        last = Tex("One seed leaf or two: check the leaf veins, the flower count and the roots.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
