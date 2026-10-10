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

# Band-layout whiteboard scene for division-techniques-and-checking (Part 1 Expert
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


class DivisionTechniquesAndCheckingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Estimating Before You Divide
        self.write_rows(0, "Estimating Before You Divide", [
            "Estimate first",
            "756 divided by 18: try 800 divided by 20",
            "About 40 groups",
            "936 divided by 12: about 80",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Breaking Down and Building Up
        self.next_band(1)
        self.write_rows(1, "Breaking Down and Building Up", [
            "600 divided by 12 is 50",
            "336 divided by 12 is 28",
            "50 + 28 = 78",
            "18 times 40 is 720, two more 18s: 42",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Halving, Doubling and the Inverse Check
        self.next_band(2)
        self.write_rows(2, "Halving, Doubling and the Inverse Check", [
            "Halve both: 468 divided by 6 is 78",
            "Double both: 1 890 divided by 30 is 63",
            "Check: 78 times 12 is 936",
            "Check: 42 times 18 is 756",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``936 divided by 6 gives the same answer''",
            "``480 divided by 12 is 48 + 240''",
            "``Built up to 720, so the answer is 40''",
            "``Check by dividing again''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Guess the Size First
        self.next_band(4)
        self.write_rows(4, "Guess the Size First", [
            "Round to friendly numbers",
            "800 divided by 20 is 40",
            "The answer is about 40",
            "42 makes sense, 420 does not",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Split It into Easy Parts
        self.next_band(5)
        self.write_rows(5, "Split It into Easy Parts", [
            "Split the number being divided",
            "600 and 336 both share by 12",
            "50 + 28 = 78",
            "Never split the divisor",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Change It, Then Check It
        self.next_band(6)
        self.write_rows(6, "Change It, Then Check It", [
            "Halve both numbers",
            "468 divided by 6 is 78",
            "Multiply back: 78 times 12",
            "That gives 936, so it is right",
        ], scale=0.9, box=1)

        last = Tex("Estimate first, split the number being divided, halve or double both numbers, and multiply back to check.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
