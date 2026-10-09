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

# Band-layout whiteboard scene for drawing-the-crane-in-oblique-projection (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (140/200/200/100/100/100 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DrawingTheCraneInObliqueSession(MovingCameraScene):
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
        self.wait(50)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Setting out the sheet
        self.write_rows(0, "Setting out the sheet", [
            "Landscape, border, title block",
            "SCALE 1:2, mm",
            "Conversion table on scrap paper",
            "Side view is the front face",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Building the crane in oblique
        self.next_band(1)
        self.write_rows(1, "Building the crane in oblique", [
            "Base: parallelogram at 45 degrees",
            "Mast, arm, pulley, string, magnet",
            "Winch: drum, dashed axle, handle",
            "Dark edges over faint construction",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Dimensions, detail, checking
        self.next_band(2)
        self.write_rows(2, "Dimensions, detail, checking", [
            "Height, arm, mast position, once each",
            "Depth along a 45 degree line",
            "DETAIL A with its own scale",
            "Check brief, sketch, conventions",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Flat base with no depth''",
            "``Mast not located by a dimension''",
            "``Detail with no scale under it''",
            "``Construction lines never darkened''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Get the sheet ready
        self.next_band(4)
        self.write_rows(4, "Get the sheet ready", [
            "Border 10 mm, title block 30 mm",
            "Every size halved in a table",
            "Mast up, arm across, winch at base",
            "Room for dimensions",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Grow the crane
        self.next_band(5)
        self.write_rows(5, "Grow the crane", [
            "Base, mast, arm, pulley, magnet",
            "Drum, axle, handle, cells",
            "Dashed hidden, chain centres",
            "Light first, dark last",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Sizes, detail, check
        self.next_band(6)
        self.write_rows(6, "Sizes, detail, check", [
            "Real numbers, no crossing",
            "Circle the winch: DETAIL A",
            "A team mate reads it as a maker",
            "Fix every question",
        ], scale=0.9, box=2)

        last = Tex("A scaled, dimensioned oblique drawing of base, mast, arm, pulley, magnet and winch, with a detail and a title block, from which the crane can be built.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
