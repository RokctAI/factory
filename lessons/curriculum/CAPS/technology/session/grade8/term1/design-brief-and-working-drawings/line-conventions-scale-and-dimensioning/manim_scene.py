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

# Band-layout whiteboard scene for line-conventions-scale-and-dimensioning (Part 1 Expert
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


class LineConventionsScaleSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Line Types and What They Mean
        self.write_rows(0, "The Line Types and What They Mean", [
            "Outline: dark, continuous, visible edges",
            "Construction: feint, left on lightly",
            "Hidden detail: dashed",
            "Centre line: thin chain",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Scale: Drawing Bigger and Smaller
        self.next_band(1)
        self.write_rows(1, "Scale: Drawing Bigger and Smaller", [
            "Scale = drawing : real",
            "1:2 half, 1:10 tenth, 2:1 double",
            "Shrink: divide; grow: multiply",
            "Write the real size, always",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Dimensioning in Millimetres
        self.next_band(2)
        self.write_rows(2, "Dimensioning in Millimetres", [
            "Millimetres, no unit",
            "Projection lines, dimension line, figure above",
            "Outside, 10 mm away, never crossing",
            "Once each; overall sizes; holes from centres",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Dimensions can be in centimetres''",
            "``Dimension the paper size on a scaled drawing''",
            "``Arrowheads can miss the lines''",
            "``Overall sizes can be left out''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Four Kinds of Line
        self.next_band(4)
        self.write_rows(4, "Four Kinds of Line", [
            "Dark for seen",
            "Feint for guide",
            "Dashed for hidden",
            "Chain for centre",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Shrinking and Growing on Paper
        self.next_band(5)
        self.write_rows(5, "Shrinking and Growing on Paper", [
            "Paper to real",
            "1:2 means half size",
            "Divide to shrink, multiply to grow",
            "Label 300, not 150",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Writing the Sizes
        self.next_band(6)
        self.write_rows(6, "Writing the Sizes", [
            "300 means 300 mm",
            "Two lines out, one between, arrows, number",
            "Outside, once, no crossing",
            "Always the overall sizes",
        ], scale=0.9, box=1)

        last = Tex("Dark, feint, dashed and chain lines, a stated scale and real sizes in millimetres: the language any maker can build from.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
