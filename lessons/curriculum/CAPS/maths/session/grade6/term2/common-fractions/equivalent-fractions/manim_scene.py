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

# Band-layout whiteboard scene for equivalent-fractions (Part 1 Expert
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


class EquivalentFractionsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Making Equivalent Fractions by Multiplying
        self.write_rows(0, "Making Equivalent Fractions by Multiplying", [
            "Multiply top and bottom by the same number",
            "2/3 = 4/6 = 6/9 = 8/12",
            "3/4 = 6/8 = 9/12",
            "5/8 = box/40: box = 25",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Simplifying Fractions by Dividing
        self.next_band(1)
        self.write_rows(1, "Simplifying Fractions by Dividing", [
            "Divide top and bottom by the same number",
            "18/24 = 3/4",
            "12/20 = 3/5",
            "Simplest form: only 1 divides both",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Equivalent Fractions with Two-Digit Denominators
        self.next_band(2)
        self.write_rows(2, "Equivalent Fractions with Two-Digit Denominators", [
            "3/4 = 75/100",
            "2/5 = 40/100",
            "9/20 = 45/100",
            "8/12 and 30/45 both simplify to 2/3",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``2/3 = 4/5''",
            "``5/8 = 5/40''",
            "``18/24 = 9/12 and stop''",
            "``75/100 is bigger than 3/4''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Cut Smaller Pieces
        self.next_band(4)
        self.write_rows(4, "Cut Smaller Pieces", [
            "Cut smaller pieces",
            "Same number top and bottom",
            "2/3 is 8/12",
            "Box is 25",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Join Pieces Back
        self.next_band(5)
        self.write_rows(5, "Join Pieces Back", [
            "Join pieces back",
            "Divide top and bottom",
            "18/24 is 3/4",
            "12/20 is 3/5",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Hundredths and Friends
        self.next_band(6)
        self.write_rows(6, "Hundredths and Friends", [
            "Hundredths and friends",
            "1/2 is 50/100",
            "3/4 is 75/100",
            "2/5 is 40/100",
        ], scale=0.9, box=2)

        last = Tex("Multiply or divide the top and bottom by the same number: the pieces change, but the amount stays the same.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
