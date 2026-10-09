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

# Band-layout whiteboard scene for extending-and-describing-numeric-patterns (Part 1 Expert
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


class ExtendingAndDescribingNumericPatternsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Constant Difference Patterns
        self.write_rows(0, "Constant Difference Patterns", [
            "R15, R30, R45, R60, R75",
            "Add 15 each time",
            "1 000, 880, 760: take away 120",
            "14, 21, 28, 35, 42",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Constant Ratio Patterns
        self.next_band(1)
        self.write_rows(1, "Constant Ratio Patterns", [
            "1, 3, 9, 27, 81: times 3",
            "2, 4, 8, 16, 32: double",
            "64, 32, 16, 8, 4: halve",
            "Check at least three numbers",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Describing Rules and Making Your Own
        self.next_band(2)
        self.write_rows(2, "Describing Rules and Making Your Own", [
            "Start at 15 and add 15 each time",
            "Week 10: 10 times 15 is R150",
            "Start at 7, add 9: 7, 16, 25, 34, 43",
            "A tank cannot go below 0 litres",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1, 3, 9, 27, then 33''",
            "``2, 4, 8, then 10''",
            "``93, 86, 79, then 86''",
            "``Add 15, with no start''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Same Jump Each Time
        self.next_band(4)
        self.write_rows(4, "Same Jump Each Time", [
            "Same jump each time",
            "R15, R30, R45, R60",
            "1 000, 880, 760, 640",
            "Up or down by the same amount",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Times the Same Each Time
        self.next_band(5)
        self.write_rows(5, "Times the Same Each Time", [
            "Times the same each time",
            "1, 3, 9, 27, 81",
            "2, 4, 8, 16, 32",
            "64, 32, 16, 8",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Say It and Make One
        self.next_band(6)
        self.write_rows(6, "Say It and Make One", [
            "Say the start and the rule",
            "Start at 15, add 15 each time",
            "Week 10: R150",
            "Make your own and swap",
        ], scale=0.9, box=1)

        last = Tex("Compare neighbours, decide between the same jump and the same times, and describe the rule with its start.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
