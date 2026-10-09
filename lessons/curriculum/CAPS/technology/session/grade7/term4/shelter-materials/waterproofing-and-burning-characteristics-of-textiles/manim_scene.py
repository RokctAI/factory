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

# Band-layout whiteboard scene for waterproofing-and-burning-characteristics-of-textiles (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/190/300/100/100/110 of 1010 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class WaterproofingAndBurningCharacteristicsSession(MovingCameraScene):
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
        self.wait(60)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): How a textile is waterproofed
        self.write_rows(0, "How a textile is waterproofed", [
            "Plain canvas soaks through",
            "Repel: wax, oil, silicone; breathes",
            "Coat: acrylic, PU, PVC; no breathing",
            "Seams leak: tape, weld, seal",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Testing waterproofing
        self.next_band(1)
        self.write_rows(1, "Testing waterproofing", [
            "Drip: funnel at 100 mm, time to first drop",
            "Spray at 45 degrees; score beading",
            "Press: thumb on a towel",
            "Coated dry; repellent damp under pressure",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Burning and the choice
        self.next_band(2)
        self.write_rows(2, "Burning and the choice", [
            "Cotton: ash; synthetics: melt and drip",
            "PVC: chars, toxic smoke",
            "Wool and treated canvas: char, go out",
            "Table: safety, then weight and cost",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Waxed canvas called waterproof''",
            "``Plain seams on a waterproof shelter''",
            "``Tarpaulin for everything''",
            "``Learners holding samples in flame''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Keeping water out
        self.next_band(4)
        self.write_rows(4, "Keeping water out", [
            "Fibres wet and swell",
            "Beads roll off",
            "Film blocks all, needs vents",
            "Every needle hole leaks",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Test it
        self.next_band(5)
        self.write_rows(5, "Test it", [
            "Three tests, same for every square",
            "Plain fails fast",
            "Weigh each square",
            "Tape the seam, test again",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Fire, and the choice
        self.next_band(6)
        self.write_rows(6, "Fire, and the choice", [
            "Teacher only: tongs, sand, water",
            "Melting roof: worst burns",
            "Smoke kills first",
            "Treated cover, tarpaulin floor",
        ], scale=0.9, box=3)

        last = Tex("Repellents bead and breathe but leak under pressure; coatings block water but need vents; seams must be sealed; cotton burns, synthetics drip, treated fabrics char and go out; choose with safety first.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
