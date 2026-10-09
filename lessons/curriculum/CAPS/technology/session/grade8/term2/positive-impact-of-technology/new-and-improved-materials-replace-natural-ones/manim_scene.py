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

# Band-layout whiteboard scene for new-and-improved-materials-replace-natural-ones (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/160/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class NewMaterialsReplaceNaturalSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Natural Materials and Their Limits
        self.write_rows(0, "Natural Materials and Their Limits", [
            "From plants, animals and the earth",
            "Timber rots, clay shatters, leather cracks",
            "Cotton holds water, thatch burns",
            "Varies piece to piece; limited supply",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): New and Improved Materials
        self.next_band(1)
        self.write_rows(1, "New and Improved Materials", [
            "New: polythene, PVC, nylon, polystyrene",
            "Improved: steel, concrete, plywood, treated timber",
            "Galvanised sheet for thatch; polythene tank for iron",
            "Remove the limit, keep the good",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Why the Change Was Positive
        self.next_band(2)
        self.write_rows(2, "Why the Change Was Positive", [
            "Clean water, safe hospitals, quick housing",
            "Lighter, stronger, cheaper, safer",
            "Consistent and always available",
            "Costs come next: waste, oil, pollution",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Natural always means better''",
            "``New always means plastic''",
            "``The bucket is the material''",
            "``Benefits only, no costs''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): What People Used Before
        self.next_band(4)
        self.write_rows(4, "What People Used Before", [
            "Wood, clay, leather, cotton, sisal, rubber",
            "Each has a weak spot",
            "Never the same twice",
            "Only as much as grows",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): The Materials That Took Over
        self.next_band(5)
        self.write_rows(5, "The Materials That Took Over", [
            "Plastics from chemistry",
            "Steel, concrete, plywood: natural made better",
            "Fix the weak spot, keep the good",
            "Bucket, pipe, rope, pot",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Better Lives From Better Materials
        self.next_band(6)
        self.write_rows(6, "Better Lives From Better Materials", [
            "Lighter, stronger, cheaper, safer",
            "Same every time, always available",
            "Water, hospitals, houses, food",
            "A technologist weighs both sides",
        ], scale=0.9, box=3)

        last = Tex("Natural materials have limits; new and improved materials removed them and made products lighter, stronger, cheaper and safer, at costs we study next.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
