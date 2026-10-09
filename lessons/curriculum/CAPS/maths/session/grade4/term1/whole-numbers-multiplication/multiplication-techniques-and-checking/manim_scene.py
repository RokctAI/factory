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

# Band-layout whiteboard scene for multiplication-techniques-and-checking (Part 1 Expert
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


class MultiplicationTechniquesAndCheckingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Estimate and Break Down
        self.write_rows(0, "Estimate and Break Down", [
            "48 times 5: estimate 250",
            "40 times 5 plus 8 times 5 is 240",
            "25 times 16 is 250 plus 150",
            "Or 50 times 5 minus 10",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Doubling and Halving
        self.next_band(1)
        self.write_rows(1, "Doubling and Halving", [
            "Halve one, double the other",
            "16 times 25 is 8 times 50 is 400",
            "Three doublings is times 8",
            "Times 5 is half of times 10",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Checking with Division
        self.next_band(2)
        self.write_rows(2, "Checking with Division", [
            "Division undoes multiplication",
            "240 divided by 5 is 48",
            "180 divided by 12 is 15",
            "Two techniques every time",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Double both numbers''",
            "``Halve the odd number''",
            "``Check by repeating the same method''",
            "``2 400 for 48 times 5''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Guess, Then Split
        self.next_band(4)
        self.write_rows(4, "Guess, Then Split", [
            "Guess: about 250",
            "40 times 5 is 200",
            "8 times 5 is 40",
            "240 chairs",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Halve One, Double the Other
        self.next_band(5)
        self.write_rows(5, "Halve One, Double the Other", [
            "16 trays of 25",
            "8 trays of 50: same rolls",
            "8 times 50 is 400",
            "Double three times for times 8",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Divide to Check
        self.next_band(6)
        self.write_rows(6, "Divide to Check", [
            "Divide undoes times",
            "240 divided by 5 is 48",
            "180 divided by 12 is 15",
            "Find one way, check another",
        ], scale=0.9, box=0)

        last = Tex("Estimate, break down or double and halve, then divide to prove the product.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
