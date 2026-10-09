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

# Band-layout whiteboard scene for lines-of-symmetry (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/160/160/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LinesOfSymmetrySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Line of Symmetry Is
        self.write_rows(0, "What a Line of Symmetry Is", [
            "Fold: the halves fit exactly",
            "Mirror line, mirror image",
            "Rectangle diagonal: equal halves, not symmetric",
            "Check vertical, horizontal and slanted",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Lines of Symmetry of Common Shapes
        self.next_band(1)
        self.write_rows(1, "Lines of Symmetry of Common Shapes", [
            "Square: 4 lines",
            "Rectangle: 2 lines",
            "Equilateral triangle: 3, isosceles: 1, scalene: 0",
            "Regular polygon: as many lines as sides",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Symmetry in Letters, Flags and Everyday Life
        self.next_band(2)
        self.write_rows(2, "Symmetry in Letters, Flags and Everyday Life", [
            "A, M, T: vertical line",
            "B, C, D: horizontal line",
            "H, I, O, X: both",
            "Colours and patterns count too",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Equal halves means symmetric''",
            "``A square has 2 lines''",
            "``S has a line of symmetry''",
            "``Only the outline matters''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Fold It
        self.next_band(4)
        self.write_rows(4, "Fold It", [
            "A fold line",
            "Halves sit exactly on top",
            "Equal pieces are not enough",
            "Check every direction",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Count the Lines
        self.next_band(5)
        self.write_rows(5, "Count the Lines", [
            "Square: 4",
            "Rectangle: 2",
            "Equilateral triangle: 3",
            "Regular shape: lines equal sides",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Letters and Flags
        self.next_band(6)
        self.write_rows(6, "Letters and Flags", [
            "A, M, T: down the middle",
            "B, C, D: across",
            "H, I, O, X: both",
            "F, S, Z: none",
        ], scale=0.9, box=3)

        last = Tex("Fold it: if the halves fit exactly, it is a line of symmetry, so find them all and count them.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
