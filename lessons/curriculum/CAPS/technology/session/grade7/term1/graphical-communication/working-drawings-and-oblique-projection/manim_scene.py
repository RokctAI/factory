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

# Band-layout whiteboard scene for working-drawings-and-oblique-projection (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (230/180/170/110/110/110 of 910 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class WorkingDrawingsAndObliqueProjectionSession(MovingCameraScene):
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
        self.wait(48)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): 2D working drawing of one face
        self.write_rows(0, "2D working drawing of one face", [
            "One face, flat, true lengths",
            "Scale chosen and written: 1:2",
            "Feint first, dark outlines after",
            "Real sizes in mm, each once, centre lines on holes",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): 3D oblique at 45 degrees
        self.next_band(1)
        self.write_rows(1, "3D oblique at 45 degrees", [
            "Front face true shape",
            "Depth lines back at 45 on the grid",
            "All parallel, all equal, usually half depth",
            "Circles on the front face stay round",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Which drawing for which job
        self.next_band(2)
        self.write_rows(2, "Which drawing for which job", [
            "Working drawing: for making",
            "Oblique drawing: for showing",
            "Same line conventions, scale stated",
            "PAT: one oblique, one dimensioned view",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Dimension along the 45 degree lines''",
            "``Write the paper size on a scaled drawing''",
            "``Depth lines at different angles''",
            "``Round holes on a receding face''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Flat and exact
        self.next_band(4)
        self.write_rows(4, "Flat and exact", [
            "Look straight at one face",
            "300 by 150 drawn 150 by 75",
            "Write 300 and 150, not 150 and 75",
            "Arm: 200 long, holes located",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Solid and real
        self.next_band(5)
        self.write_rows(5, "Solid and real", [
            "Same front face first",
            "One square across, one up",
            "Same length, join the ends",
            "Holes on the front face",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): One to make it, one to show it
        self.next_band(6)
        self.write_rows(6, "One to make it, one to show it", [
            "Exact sizes: working drawing",
            "Looks and fit: oblique drawing",
            "Both: dark, feint, dashed, scale",
            "Two drawings for the device",
        ], scale=0.9, box=0)

        last = Tex("Working drawing to make it, oblique drawing to see it; same face, same conventions, two jobs.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
