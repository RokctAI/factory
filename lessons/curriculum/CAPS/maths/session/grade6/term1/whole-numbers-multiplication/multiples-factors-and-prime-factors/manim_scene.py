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

# Band-layout whiteboard scene for multiples-factors-and-prime-factors (Part 1 Expert
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


class MultiplesFactorsAndPrimeFactorsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Multiples of Two-Digit and Three-Digit Numbers
        self.write_rows(0, "Multiples of Two-Digit and Three-Digit Numbers", [
            "Multiples: skip-count",
            "125, 250, 375, 500",
            "Taxis 15, buses 20: meet at 60",
            "Lowest common multiple of 6 and 8: 24",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Factors of Two-Digit and Three-Digit Numbers
        self.next_band(1)
        self.write_rows(1, "Factors of Two-Digit and Three-Digit Numbers", [
            "Factors come in pairs",
            "120: 8 and 15, 10 and 12",
            "Common factors of 84 and 120",
            "Highest common factor: 12",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Prime Factors
        self.next_band(2)
        self.write_rows(2, "Prime Factors", [
            "Split until every branch is prime",
            "60 = 6 times 10",
            "= 2 times 3 times 2 times 5",
            "Prime factors of 60: 2, 3, 5",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``4 is a multiple of 120''",
            "``Lowest common multiple of 6 and 8 is 48''",
            "``1 is a prime factor''",
            "``Stopping the tree at 6''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Skip-Count Up
        self.next_band(4)
        self.write_rows(4, "Skip-Count Up", [
            "Skip-count up",
            "15, 30, 45, 60",
            "20, 40, 60",
            "They meet at 60",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Factor Pairs
        self.next_band(5)
        self.write_rows(5, "Factor Pairs", [
            "Pairs from 1",
            "Stop when they meet",
            "Highest common factor: 12",
            "10 sopranos, 7 altos",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Break It into Primes
        self.next_band(6)
        self.write_rows(6, "Break It into Primes", [
            "Split into pairs",
            "Keep splitting",
            "2 times 2 times 3 times 5",
            "1 is not prime",
        ], scale=0.9, box=2)

        last = Tex("Multiples go up by skip-counting, factors come in pairs, and a factor tree splits a number until only primes are left.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
