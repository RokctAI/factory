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

# Band-layout whiteboard scene for working-drawing-of-the-headgear (Part 1 Expert
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


class HeadgearWorkingDrawingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From Sketch to Working Drawing: Views and Scale
        self.write_rows(0, "From Sketch to Working Drawing: Views and Scale", [
            "Flat views, instruments, to scale",
            "First angle: front, plan below, side right",
            "Front: A and back-leg; plan: footprint",
            "Full-size dimensions; scale in title block",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Dimensioning and Line Conventions for the Headgear
        self.next_band(1)
        self.write_rows(1, "Dimensioning and Line Conventions for the Headgear", [
            "Thick visible, dashed hidden, chain centres",
            "Each dimension once, outermost overall",
            "Back-leg by foot and top, not slope",
            "Member sizes as notes or parts list",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Drawing the Mechanism and the Assembly
        self.next_band(2)
        self.write_rows(2, "Drawing the Mechanism and the Assembly", [
            "Drum, motor, gears, rope, brake in place",
            "Gears end-on with centre distances",
            "Detail A at 1:2; section through the tower",
            "Parts list: number, material, length, quantity",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Views not aligned''",
            "``Back-leg dimensioned by slope''",
            "``Mechanism on a separate sheet''",
            "``No parts list''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Front, Side and Top
        self.next_band(4)
        self.write_rows(4, "Front, Side and Top", [
            "One face is not enough",
            "Line the views up",
            "Plan: does it topple, does it fit",
            "600 means 600",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Numbers the Builder Can Trust
        self.next_band(5)
        self.write_rows(5, "Numbers the Builder Can Trust", [
            "Lines mean things",
            "Chain of numbers up the leg",
            "Two ends set the slope",
            "Small arrowheads, no units",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Where the Winder Sits
        self.next_band(6)
        self.write_rows(6, "Where the Winder Sits", [
            "Draw the winder where it lives",
            "Rope: drum, sheave, cage",
            "Balloon numbers to the list",
            "Revision letter when it changes",
        ], scale=0.9, box=2)

        last = Tex("Three aligned views to a stated scale, real dimensions given once, the winder drawn in its place, and a numbered parts list the budget and build will follow.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
