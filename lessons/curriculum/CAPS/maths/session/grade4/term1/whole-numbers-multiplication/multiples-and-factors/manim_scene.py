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

# Band-layout whiteboard scene for multiples-and-factors (Part 1 Expert
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


class MultiplesAndFactorsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Multiples
        self.write_rows(0, "Multiples", [
            "Multiples: the times table, going on",
            "7, 14, 21, 28 and so on",
            "84 divided by 7 is 12: a multiple",
            "Common multiples of 6 and 8: 24, 48",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Factors
        self.next_band(1)
        self.write_rows(1, "Factors", [
            "Factors divide exactly",
            "24: 1 and 24, 2 and 12, 3 and 8, 4 and 6",
            "Stop when pairs repeat",
            "36 has nine factors",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Linking Multiples, Factors and Common Factors
        self.next_band(2)
        self.write_rows(2, "Linking Multiples, Factors and Common Factors", [
            "4 times 6 is 24: one fact, two views",
            "24 is a multiple of 6, 6 is a factor of 24",
            "Common factors of 24 and 36: 1, 2, 3, 4, 6, 12",
            "Equal rows need a factor",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Factors are bigger than the number''",
            "``List factors in any order''",
            "``5 is a factor of 24''",
            "``List all the multiples''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Counting in a Number
        self.next_band(4)
        self.write_rows(4, "Counting in a Number", [
            "Multiples: the table that keeps going",
            "84 is a multiple of 7",
            "6 and 8 share 24 and 48",
            "Lowest common multiple: 24",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Numbers That Fit Exactly
        self.next_band(5)
        self.write_rows(5, "Numbers That Fit Exactly", [
            "Factors divide in exactly",
            "1 and 24, 2 and 12, 3 and 8, 4 and 6",
            "Stop when pairs repeat",
            "Factors of 8: 1, 2, 4, 8",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Two Sides of One Fact
        self.next_band(6)
        self.write_rows(6, "Two Sides of One Fact", [
            "4 times 6 is 24",
            "24: multiple of 6, 6: factor of 24",
            "24 and 36 share 12",
            "12 bags: 2 biscuits, 3 sweets",
        ], scale=0.9, box=2)

        last = Tex("Multiples count up in the number, factors divide in exactly, and one fact gives both.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
