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

# Band-layout whiteboard scene for grade-8-revision-and-baseline-assessment (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/150/120/110/100 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Grade8RevisionAndBaselineAssessmentSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What Grade 8 Technology Left in Your Toolbox
        self.write_rows(0, "What Grade 8 Technology Left in Your Toolbox", [
            "IDMEC: five stages, every project",
            "Dark, feint, dashed; scale; millimetres",
            "Isometric then orthographic",
            "Fitness for purpose is the judge",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Structures, Mechanisms and Electricity in One Sweep
        self.next_band(1)
        self.write_rows(1, "Structures, Mechanisms and Electricity in One Sweep", [
            "Tension, compression, bending, torsion, shear",
            "Gear ratio: driven teeth over driver",
            "MA = load over effort",
            "Ohm's law in words; series and parallel",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): How the Baseline Assessment Works and What It Is For
        self.next_band(2)
        self.write_rows(2, "How the Baseline Assessment Works and What It Is For", [
            "Week one; does not count",
            "Four areas: process, drawing, forces, circuits",
            "Recall beats rereading",
            "Honest blanks help the teacher",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The baseline is a test to pass''",
            "``Grade 8 is finished with''",
            "``Gear ratio is lever MA''",
            "``Isometric when a working drawing was asked''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Five Big Ideas to Carry Forward
        self.next_band(4)
        self.write_rows(4, "Five Big Ideas to Carry Forward", [
            "IDMEC",
            "Line types and scale",
            "Forces and triangles",
            "Gears, MA, circuits",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): A Quick Run Through Last Year
        self.next_band(5)
        self.write_rows(5, "A Quick Run Through Last Year", [
            "Term 1 structure; Term 2 impact",
            "Term 3 headgear gears",
            "Term 4 electricity",
            "Same pattern this year",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Facing the Baseline Calmly
        self.next_band(6)
        self.write_rows(6, "Facing the Baseline Calmly", [
            "Short test, no mark",
            "Leave gaps honest",
            "Cover, say, check",
            "One drawing, one circuit, one ratio",
        ], scale=0.9, box=2)

        last = Tex("Grade 8 gave you IDMEC, line types, forces, gears and circuits; Grade 9 builds on all five, and the baseline shows where to start.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
