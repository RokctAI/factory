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

# Band-layout whiteboard scene for fossil-fuels-are-non-renewable (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/120/140/110/110/110 of 800 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FossilFuelsAreNonRenewableSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): How Coal Formed
        self.write_rows(0, "How Coal Formed", [
            "Swamp plants died",
            "Peat formed under water",
            "Buried, squeezed, heated",
            "Coal: millions of years",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Oil and Natural Gas
        self.next_band(1)
        self.write_rows(1, "Oil and Natural Gas", [
            "Tiny sea living things",
            "Buried in sea-floor mud",
            "Crude oil and natural gas",
            "Petrol, diesel, paraffin",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Non-Renewable Fuels
        self.next_band(2)
        self.write_rows(2, "Non-Renewable Fuels", [
            "Renewable: replaced quickly",
            "Non-renewable: gone when used",
            "Coal, oil and gas",
            "Pollution and climate change",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Fossil fuels are dinosaur bones''",
            "``Coal forms in a few years''",
            "``Lots of coal means renewable''",
            "``Burning coal is harmless''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Coal from Old Plants
        self.next_band(4)
        self.write_rows(4, "Coal from Old Plants", [
            "Coal from old plants",
            "Swamps",
            "Buried",
            "Coal",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Oil and Gas from the Sea
        self.next_band(5)
        self.write_rows(5, "Oil and Gas from the Sea", [
            "Oil and gas from the sea",
            "Tiny sea life",
            "Oil",
            "Gas",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Gone When Used
        self.next_band(6)
        self.write_rows(6, "Gone When Used", [
            "Gone when used",
            "Non-renewable",
            "Cannot be replaced",
            "Use carefully",
        ], scale=0.9, box=1)

        last = Tex("Coal, oil and natural gas are fossil fuels formed over millions of years from dead plants and animals, so they are non-renewable.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
