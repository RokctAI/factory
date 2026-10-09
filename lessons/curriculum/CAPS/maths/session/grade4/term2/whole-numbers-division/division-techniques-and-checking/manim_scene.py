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
        # --- Band 0 (subtopic_1): Estimating a Quotient
        self.write_rows(0, "Estimating a Quotient", [
            "144 divided by 8: between 10 and 20",
            "160 divided by 8 is 20: a little under",
            "700 divided by 5 is 140",
            "Estimate catches a missing digit",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Breaking Down and Building Up
        self.next_band(1)
        self.write_rows(1, "Breaking Down and Building Up", [
            "144 is 80 plus 64: 10 plus 8 is 18",
            "675 is 500, 150, 25: 135",
            "7 times 30 is 210, gap 42: 36",
            "Halve three times to divide by 8",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Checking with Multiplication
        self.next_band(2)
        self.write_rows(2, "Checking with Multiplication", [
            "Multiply back: 8 times 18 is 144",
            "5 times 135 is 675",
            "Divisor times quotient plus remainder",
            "7 times 36 plus 3 is 255",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``15 for 675 divided by 5''",
            "``Check without adding the remainder''",
            "``144 is 100 plus 44 for dividing by 8''",
            "``The check must be wrong''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Guess How Big
        self.next_band(4)
        self.write_rows(4, "Guess How Big", [
            "Between 10 and 20",
            "700 divided by 5 is 140",
            "A bit under 140",
            "Guess catches wild answers",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Friendly Pieces
        self.next_band(5)
        self.write_rows(5, "Friendly Pieces", [
            "80 and 64: 10 and 8",
            "500, 150, 25: 100, 30, 5",
            "7 times 30, then 7 times 6",
            "Answer 36",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Multiply Back to Check
        self.next_band(6)
        self.write_rows(6, "Multiply Back to Check", [
            "8 times 18 is 144",
            "7 times 36 plus 3 is 255",
            "Check fails? Answer is wrong",
            "Two techniques every time",
        ], scale=0.9, box=0)

        last = Tex("Estimate how big, divide in friendly pieces, then multiply back to prove it.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
