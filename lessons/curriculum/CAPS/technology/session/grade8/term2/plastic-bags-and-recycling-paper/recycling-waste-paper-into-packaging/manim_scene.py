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

# Band-layout whiteboard scene for recycling-waste-paper-into-packaging (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/170/170/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RecyclingPaperPackagingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From Waste Paper to New Board
        self.write_rows(0, "From Waste Paper to New Board", [
            "Fibres tangled, not melted: water frees them",
            "Collect, sort, bale, pulp, screen, de-ink",
            "Mesh, press, dry; flutes between liners",
            "Five to seven cycles, then fresh fibre",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Packaging Products Made From Recycled Paper
        self.next_band(1)
        self.write_rows(1, "Packaging Products Made From Recycled Paper", [
            "Corrugated boxes: the biggest product",
            "Moulded pulp: egg trays, cup carriers, inserts",
            "Cartons with a white skin; bags, cores",
            "Corrugated board is an I-beam in paper",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Benefits, Limits and the Recycling System
        self.next_band(2)
        self.write_rows(2, "Benefits, Limits and the Recycling System", [
            "17 trees, 26 000 litres, two thirds of the energy",
            "Three cubic metres out of landfill; jobs",
            "Limits: fibre wear, contamination, collection",
            "Sort cleanly, design for recycling, pay pickers",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Paper recycles for ever''",
            "``Greasy boxes belong in the paper bin''",
            "``Recycled always means weak''",
            "``The system runs itself''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Old Paper, New Paper
        self.next_band(4)
        self.write_rows(4, "Old Paper, New Paper", [
            "Trolley to buy-back centre to mill",
            "Fibre soup in the pulper",
            "Spread, squeeze, dry",
            "Fresh fibre after seven trips",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Boxes, Egg Trays and Cup Holders
        self.next_band(5)
        self.write_rows(5, "Boxes, Egg Trays and Cup Holders", [
            "Brown boxes, used once, round again",
            "Egg trays from the lowest grade",
            "Cereal cartons with a white face",
            "Two skins and a wavy web",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Why It Is Worth It and Where It Stops
        self.next_band(6)
        self.write_rows(6, "Why It Is Worth It and Where It Stops", [
            "Trees, water, energy, landfill, jobs",
            "Grease, wax and laminates spoil it",
            "Paper works; plastic struggles",
            "Sort at source, pay the pickers",
        ], scale=0.9, box=0)

        last = Tex("Waste paper is pulped, cleaned and reformed into board several times over, saving trees, water and energy, as long as it is sorted clean and collected.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
