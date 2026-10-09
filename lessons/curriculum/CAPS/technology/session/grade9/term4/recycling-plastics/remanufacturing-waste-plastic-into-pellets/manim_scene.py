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

# Band-layout whiteboard scene for remanufacturing-waste-plastic-into-pellets (Part 1 Expert
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


class RemanufacturingWastePlasticIntoPelletsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Case Study: A Plastics Recycling Plant
        self.write_rows(0, "Case Study: A Plastics Recycling Plant", [
            "Input: dirty bales of PET from buy-back centres",
            "Output must be clean, uniform, tested pellet",
            "Price follows new plastic and oil",
            "Case study: in, change, out, measure",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): From Bale to Pellet: Sort, Wash, Shred, Melt
        self.next_band(1)
        self.write_rows(1, "From Bale to Pellet: Sort, Wash, Shred, Melt", [
            "1 sort, 2 strip labels, 3 shred to flake",
            "4 hot wash + float-sink: PET sinks, caps float",
            "5 rinse, dry, test flake",
            "6 extrude 270 deg, screen, die, chop pellets",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): The Systems Diagram: Input, Process, Output
        self.next_band(2)
        self.write_rows(2, "The Systems Diagram: Input, Process, Output", [
            "Input -> Process -> Output boxes",
            "Resources in above; waste out below",
            "Feedback: tests back to process",
            "Same diagram for your project",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Bottles melted unwashed and unsorted''",
            "``Drying step skipped before extrusion''",
            "``Systems diagram drawn without feedback''",
            "``Clear and coloured PET mixed in one batch''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Factory That Eats Bottles
        self.next_band(4)
        self.write_rows(4, "A Factory That Eats Bottles", [
            "Bales in",
            "Pellets out",
            "Tight money",
            "Ask at each machine",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Six Steps to a Pellet
        self.next_band(5)
        self.write_rows(5, "Six Steps to a Pellet", [
            "Sort, strip, chop",
            "Wash, float caps off",
            "Dry hard",
            "Melt, squeeze, chop",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Draw the System
        self.next_band(6)
        self.write_rows(6, "Draw the System", [
            "Three boxes",
            "Arrow back from tests",
            "Resources and waste",
            "Your project too",
        ], scale=0.9, box=1)

        last = Tex("A bale of dirty bottles becomes clean pellets through sorting, shredding, washing, float-sink separation, drying and extrusion, and a systems diagram shows that as input, process, output and feedback.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
