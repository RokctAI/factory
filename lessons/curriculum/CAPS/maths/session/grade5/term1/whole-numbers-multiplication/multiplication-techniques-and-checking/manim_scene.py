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
        # --- Band 0 (subtopic_1): Doubling and Halving
        self.write_rows(0, "Doubling and Halving", [
            "Double one number, halve the other",
            "16 times 25 is 8 times 50",
            "8 times 50 is 4 times 100: 400",
            "35 times 14 is 70 times 7: 490",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Breaking Down, Building Up and Compensating
        self.next_band(1)
        self.write_rows(1, "Breaking Down, Building Up and Compensating", [
            "48 times 15 is 480 + 240 = 720",
            "15 times 48 is 750 minus 30",
            "199 times 12 is 2 400 minus 12",
            "That is 2 388",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Estimating and Checking by Division
        self.next_band(2)
        self.write_rows(2, "Estimating and Checking by Division", [
            "Estimate: 400 times 20 is 8 000",
            "412 times 19 is 8 240 minus 412",
            "720 divided by 15 is 48",
            "Two techniques every time",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``16 times 25 is 32 times 50''",
            "``199 times 12 is 2 400 minus 1''",
            "``48 times 15 is 480 + 5''",
            "``Check by doing it again the same way''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Double One, Halve the Other
        self.next_band(4)
        self.write_rows(4, "Double One, Halve the Other", [
            "Double one, halve the other",
            "16 times 25 is 8 times 50",
            "4 times 100 is 400",
            "Never double both",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Split or Round
        self.next_band(5)
        self.write_rows(5, "Split or Round", [
            "48 times 10 is 480",
            "48 times 5 is half: 240",
            "200 times 12 is 2 400",
            "Take off one 12: 2 388",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Guess and Undo
        self.next_band(6)
        self.write_rows(6, "Guess and Undo", [
            "Guess first: about 8 000",
            "Times is undone by divide",
            "720 divided by 15 is 48",
            "The product checks out",
        ], scale=0.9, box=2)

        last = Tex("Double and halve, split, or round and fix, then estimate and divide to check.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
