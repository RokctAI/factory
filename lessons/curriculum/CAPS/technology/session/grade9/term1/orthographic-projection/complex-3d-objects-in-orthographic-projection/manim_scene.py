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

# Band-layout whiteboard scene for complex-3d-objects-in-orthographic-projection (Part 1 Expert
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


class Complex3dObjectsInOrthographicProjectionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Sloping Faces, Holes and Slots in Three Views
        self.write_rows(0, "Sloping Faces, Holes and Slots in Three Views", [
            "Chamfer: true angle in one view only",
            "Hole: circle + centre lines from above",
            "Hole from side: two dashed lines",
            "True shape square-on; lines elsewhere",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Using Instruments: Set Squares, Compass and the Mitre Line
        self.next_band(1)
        self.write_rows(1, "Using Instruments: Set Squares, Compass and the Mitre Line", [
            "T-square; 90, 45, 30/60 set squares",
            "2H feint; HB dark",
            "Compass set to the radius; centre lines first",
            "Mitre line at 45 carries depths",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Reading Three Views Back into a Solid
        self.next_band(2)
        self.write_rows(2, "Reading Three Views Back into a Solid", [
            "Start simple; trace each feature",
            "Circle elsewhere = parallel lines",
            "Isometric sketch checks the reading",
            "Every line must be explained",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Hole drawn round in every view''",
            "``Chamfer at 45 in the foreshortened view''",
            "``Compass set to the diameter''",
            "``Centre lines forgotten''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): When the Edges Are Not Square
        self.next_band(4)
        self.write_rows(4, "When the Edges Are Not Square", [
            "Some faces slope; some blocks have holes",
            "Slope true in one view",
            "Hole: circle, then dashed lines",
            "Draw true shape where square-on",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Tools That Keep the Lines Honest
        self.next_band(5)
        self.write_rows(5, "Tools That Keep the Lines Honest", [
            "T-square flat; set squares upright",
            "Hard feint, soft dark",
            "Radius, not diameter",
            "45 line turns the corner",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): From Flat Views to a Shape in Your Head
        self.next_band(6)
        self.write_rows(6, "From Flat Views to a Shape in Your Head", [
            "Pick a feature, find it in all three",
            "Circle = two lines elsewhere",
            "Sketch it to check",
            "Unexplained line = wrong object",
        ], scale=0.9, box=0)

        last = Tex("Every feature is true in one view and lines in the others; instruments keep the views aligned, and tracing features through all three reads the solid.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
