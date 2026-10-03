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

# Band-layout whiteboard scene for plants-with-and-without-seeds (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/160/160/120/120/120 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PlantsWithAndWithoutSeedsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Plants without seeds
        self.write_rows(0, "Plants without seeds", [
            "Spores: tiny, light, no food store",
            "Mosses: no true roots, no transport tissue, small",
            "Ferns: roots, fronds, transport tissue; sori make spores",
            "Both need water: sex cells swim",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Gymnosperms: naked seeds
        self.next_band(1)
        self.write_rows(1, "Gymnosperms: naked seeds", [
            "Seed: embryo, food store, seed coat",
            "Seeds on cone scales, no flowers; pollen by wind",
            "Conifers: pines (alien), yellowwoods (native)",
            "Cycads: ancient, slow, badly threatened",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Angiosperms: seeds in fruit
        self.next_band(2)
        self.write_rows(2, "Angiosperms: seeds in fruit", [
            "Flowers; ovary becomes a fruit around the seeds",
            "Fruit = any seed container: pods, tomatoes, grains",
            "Pollen by wind or animals; seeds spread by fruit",
            "Mosses, ferns, gymnosperms, angiosperms",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Ferns make seeds''",
            "``A pine cone is a fruit''",
            "``A fruit must taste sweet''",
            "``All trees are flowering plants''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Dust instead of seeds
        self.next_band(4)
        self.write_rows(4, "Dust instead of seeds", [
            "Mosses and ferns make spores, not seeds",
            "Spore: a speck that grows into a plant",
            "Moss: no roots, no pipes, small and damp",
            "Fern: roots, stems, pipes; still needs water",
        ], scale=0.88, box=0)

        # --- Band 5 (subtopic_5): A seed is a packed lunchbox
        self.next_band(5)
        self.write_rows(5, "A seed is a packed lunchbox", [
            "Baby plant + food store + tough coat",
            "Can wait for rain; pollen carries male cells",
            "Gymnosperms: naked seeds on cones, no flowers",
            "Pines, yellowwoods, cycads",
        ], scale=0.82, box=0)

        # --- Band 6 (subtopic_6): Seeds in a wrapper
        self.next_band(6)
        self.write_rows(6, "Seeds in a wrapper", [
            "Angiosperms: flowers, then fruit around seeds",
            "Fruit: anything from a flower holding seeds",
            "Juicy, hooked or winged fruits spread seeds",
            "Biggest plant group: grass, beans, proteas",
        ], scale=0.82, box=1)

        last = Tex("Spores or seeds; naked seeds or seeds inside fruit.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
