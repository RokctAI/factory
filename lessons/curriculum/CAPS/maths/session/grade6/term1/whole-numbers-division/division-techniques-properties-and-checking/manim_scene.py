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

# Band-layout whiteboard scene for division-techniques-properties-and-checking (Part 1 Expert
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


class DivisionTechniquesPropertiesAndCheckingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Breaking Down the Dividend
        self.write_rows(0, "Breaking Down the Dividend", [
            "Split into easy parts",
            "3 648 = 3 600 + 48",
            "300 + 4 = 304 bags",
            "Divide by 4: halve twice",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Building Up with Chunks
        self.next_band(1)
        self.write_rows(1, "Building Up with Chunks", [
            "Take away chunks of 15",
            "6 000, then 1 200, then 45",
            "400 + 80 + 3 = 483",
            "Bigger chunks, fewer steps",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Checking: Inverse, Estimation and Dividing by 1
        self.next_band(2)
        self.write_rows(2, "Checking: Inverse, Estimation and Dividing by 1", [
            "Multiply back: 483 times 15 = 7 245",
            "Estimate: about 500",
            "Divide by 1: no change",
            "You cannot divide by 0",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3 648 split as 3 000, 600, 40 and 8''",
            "``7 245 divided by 15 = 3''",
            "``4 875 divided by 1 = 1''",
            "``1 500 minus 2 880 first''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Split It Up
        self.next_band(4)
        self.write_rows(4, "Split It Up", [
            "Split it up",
            "3 600 and 48",
            "300 and 4",
            "304 bags",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Take Away Chunks
        self.next_band(5)
        self.write_rows(5, "Take Away Chunks", [
            "Take away chunks",
            "400 groups, 80 groups, 3 groups",
            "Add the chunks",
            "483 litres",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Multiply Back
        self.next_band(6)
        self.write_rows(6, "Multiply Back", [
            "Multiply back",
            "483 times 15 = 7 245",
            "Divide by 1: same number",
            "Divide by itself: 1",
        ], scale=0.9, box=1)

        last = Tex("Split into friendly parts or take away big chunks, add up the pieces, and multiply back to check.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
