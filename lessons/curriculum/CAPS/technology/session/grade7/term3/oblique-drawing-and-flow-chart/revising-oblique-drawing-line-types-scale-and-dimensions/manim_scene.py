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

# Band-layout whiteboard scene for revising-oblique-drawing-line-types-scale-and-dimensions (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/180/200/100/100/100 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RevisingObliqueDrawingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Oblique projection
        self.write_rows(0, "Oblique projection", [
            "Front face true to shape",
            "Receding edges at 45 degrees",
            "Cabinet: half length",
            "Busy face at the front",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Line types and scale
        self.next_band(1)
        self.write_rows(1, "Line types and scale", [
            "Thick visible; thin construction",
            "Dashed hidden; chain centre",
            "1:2 is half size; write real sizes",
            "Conversion table first",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Dimensioning rules
        self.next_band(2)
        self.write_rows(2, "Dimensioning rules", [
            "Millimetres; each size once",
            "Thin line, arrowheads, extensions",
            "Number above the middle",
            "Title block: name, date, scale, units",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Receding edges at 30 or 60 degrees''",
            "``Paper size written instead of real''",
            "``Numbers sitting on the line''",
            "``No scale or units''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Drawing a box in 3D
        self.next_band(4)
        self.write_rows(4, "Drawing a box in 3D", [
            "Front flat and true",
            "45 degrees from each corner",
            "Half the depth",
            "Join the ends",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Lines and scale
        self.next_band(5)
        self.write_rows(5, "Lines and scale", [
            "Four line types",
            "Light first, dark last",
            "350 becomes 175",
            "Table, then draw once",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Putting on the sizes
        self.next_band(6)
        self.write_rows(6, "Putting on the sizes", [
            "Once each, never crossing",
            "Diameter symbol and centre lines",
            "True length on slanted edges",
            "Fill the title block",
        ], scale=0.9, box=0)

        last = Tex("Front face true, depth at 45 degrees and half length, four line types, a stated scale, real sizes once each, and a title block.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
