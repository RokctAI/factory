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

# Band-layout whiteboard scene for isometric-projection-on-a-grid (Part 1 Expert
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


class IsometricProjectionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What Isometric Projection Is
        self.write_rows(0, "What Isometric Projection Is", [
            "Vertical, 30 right, 30 left: 120 apart",
            "Axis edges true to scale; diagonals are not",
            "Top, front and side at once",
            "Measurable, unlike oblique",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Drawing on the Isometric Grid
        self.next_band(1)
        self.write_rows(1, "Drawing on the Isometric Grid", [
            "Dots run along the three axes",
            "Bottom front corner: height, width, depth",
            "Close front, side, then top",
            "Members as thin boxes; braces last",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Scale, Dimensions and the PAT Design
        self.next_band(2)
        self.write_rows(2, "Scale, Dimensions and the PAT Design", [
            "400, 300, 200 at 1:2 = 20, 15, 10 units",
            "Base parallelogram, verticals, rails, braces",
            "Axle: count down the uprights",
            "Dimensions along the axes, real mm, scale stated",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Depth at 45 degrees from habit''",
            "``Draw the brace at its real length''",
            "``Lines can drift off the grid''",
            "``Paper sizes, no scale''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Three Axes, Two Slopes
        self.next_band(4)
        self.write_rows(4, "Three Axes, Two Slopes", [
            "Up, up-right, up-left",
            "Equal measure",
            "Edges along the directions are true",
            "Measurements allowed",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Following the Dots
        self.next_band(5)
        self.write_rows(5, "Following the Dots", [
            "Dot to dot, one unit each",
            "Start at the bottom corner",
            "Three lines, then close the faces",
            "Braces last, corner to corner",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Drawing Your Own Frame
        self.next_band(6)
        self.write_rows(6, "Drawing Your Own Frame", [
            "Pick the scale, write it",
            "Base, uprights, rails, braces, axle",
            "Sizes slope with their edge",
            "Real millimetres",
        ], scale=0.9, box=2)

        last = Tex("Isometric: vertical, 30 right, 30 left, true along the axes, built from the bottom corner, dimensioned in real millimetres.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
