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

# Band-layout whiteboard scene for grade-7-revision-and-baseline-assessment (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/170/140/120/120/100 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Grade7RevisionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What Grade 7 Technology Taught Us
        self.write_rows(0, "What Grade 7 Technology Taught Us", [
            "Four projects, one process: IDMEC",
            "Investigate, design, make, evaluate, communicate",
            "Dark, feint and dashed lines; mm; scale",
            "Impact on society and environment",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Levers, Mechanical Advantage and Structures
        self.next_band(1)
        self.write_rows(1, "Levers, Mechanical Advantage and Structures", [
            "Mechanical advantage: load bigger than effort",
            "Lever class: what sits in the middle",
            "Triangulation stops frames folding",
            "Circuit: complete loop; coil plus nail",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): The Baseline Assessment
        self.next_band(2)
        self.write_rows(2, "The Baseline Assessment", [
            "A check-up, not a verdict",
            "Label a lever, brace a frame, draw symbols",
            "Say it aloud, draw it once",
            "Short labelled sketches score",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Make comes before design''",
            "``A wheelbarrow is first class because of the wheel''",
            "``Triangles are strong just because of shape''",
            "``A lamp lights with a gap in the wire''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The Five Steps and Why They Matter
        self.next_band(4)
        self.write_rows(4, "The Five Steps and Why They Matter", [
            "Five steps, same every project",
            "I-D-M-E-C",
            "Dark edges, feint guides, dashed hidden",
            "1:2 means half size",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Stronger Hands and Stiffer Frames
        self.next_band(5)
        self.write_rows(5, "Stronger Hands and Stiffer Frames", [
            "Pivot in the middle: first class",
            "Load in the middle: second class",
            "Effort in the middle: third class",
            "One diagonal, two triangles",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Showing What You Already Know
        self.next_band(6)
        self.write_rows(6, "Showing What You Already Know", [
            "Baseline finds the gaps",
            "Short questions, quick sketches",
            "Honest effort gives a true reading",
            "You already know most of it",
        ], scale=0.9, box=2)

        last = Tex("Grade 7 gave you the process, the levers, the brace and the loop; Grade 8 builds on all four.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
