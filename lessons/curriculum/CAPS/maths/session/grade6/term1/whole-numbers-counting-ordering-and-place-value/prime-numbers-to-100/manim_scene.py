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

# Band-layout whiteboard scene for prime-numbers-to-100 (Part 1 Expert
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


class PrimeNumbersTo100Session(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What Is a Prime Number
        self.write_rows(0, "What Is a Prime Number", [
            "Prime: exactly two factors",
            "1 and itself",
            "13: only one long row",
            "12: 3 rows of 4, so composite",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Finding Primes to 100
        self.next_band(1)
        self.write_rows(1, "Finding Primes to 100", [
            "Cross out 1",
            "Keep 2, 3, 5, 7",
            "Cross out their multiples",
            "25 primes to 100",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Prime and Composite Numbers
        self.next_band(2)
        self.write_rows(2, "Prime and Composite Numbers", [
            "1 is neither prime nor composite",
            "2 is the only even prime",
            "Odd is not always prime",
            "12 = 2 times 2 times 3",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1 is prime''",
            "``All odd numbers are prime''",
            "``2 is not prime because it is even''",
            "``51 is prime because it ends in 1''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Only Two Factors
        self.next_band(4)
        self.write_rows(4, "Only Two Factors", [
            "Two factors only",
            "1 and itself",
            "13 is prime",
            "12 is composite",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Sieve the Hundred Square
        self.next_band(5)
        self.write_rows(5, "Sieve the Hundred Square", [
            "Cross out the multiples",
            "of 2, 3, 5 and 7",
            "What is left is prime",
            "91 is 7 times 13",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Prime or Not
        self.next_band(6)
        self.write_rows(6, "Prime or Not", [
            "1: not prime",
            "2: the only even prime",
            "9, 21 and 51: composite",
            "Test with 2, 3, 5 and 7",
        ], scale=0.9, box=1)

        last = Tex("A prime has exactly two factors, 1 and itself, so sieve out the multiples of 2, 3, 5 and 7 and what is left is prime.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
