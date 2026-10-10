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

# Band-layout whiteboard scene for special-processed-materials (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/130/140/110/110/110 of 790 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SpecialProcessedMaterialsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Concrete, Plaster and Ceramics
        self.write_rows(0, "Concrete, Plaster and Ceramics", [
            "Concrete: strong foundations",
            "Plaster of Paris: heated gypsum",
            "Ceramics: fired clay",
            "Tiles, basins, toilets",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Glass and Plastics
        self.next_band(1)
        self.write_rows(1, "Glass and Plastics", [
            "Glass: melted sand, soda, limestone",
            "See-through, hard, brittle",
            "Plastics: mostly from oil",
            "Light, waterproof, do not rot",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Fabrics and Paints
        self.next_band(2)
        self.write_rows(2, "Fabrics and Paints", [
            "Fabrics: spun, woven, knitted",
            "Cotton, wool, mohair",
            "Nylon, polyester from oil",
            "Paint: colour and protection",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Plastics grow naturally''",
            "``Glass is made from water''",
            "``All fabrics come from plants''",
            "``Paint is only for colour''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Strong, Smooth and Hard
        self.next_band(4)
        self.write_rows(4, "Strong, Smooth and Hard", [
            "Strong, smooth and hard",
            "Concrete",
            "Plaster",
            "Ceramics",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): See-Through and Mouldable
        self.next_band(5)
        self.write_rows(5, "See-Through and Mouldable", [
            "See-through and mouldable",
            "Glass from sand",
            "Plastic from oil",
            "Light and waterproof",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Soft and Colourful
        self.next_band(6)
        self.write_rows(6, "Soft and Colourful", [
            "Soft and colourful",
            "Woven fabrics",
            "Natural or synthetic",
            "Paint protects",
        ], scale=0.9, box=3)

        last = Tex("Concrete, plaster of Paris, ceramics, glass, plastics, fabrics and paints are processed materials, each with special properties for its job.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
