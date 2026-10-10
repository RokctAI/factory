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

# Band-layout whiteboard scene for money-and-measurement-problems (Part 1 Expert
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


class MoneyAndMeasurementProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Money Problems: Budgets and Change
        self.write_rows(0, "Money Problems: Budgets and Change", [
            "Spend on several things: add",
            "R22 505 spent",
            "What is left: subtract",
            "R25 000 minus R22 505 = R2 495",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Measurement Problems: Distance and Mass
        self.next_band(1)
        self.write_rows(1, "Measurement Problems: Distance and Mass", [
            "Same units first",
            "3 km = 3 000 m",
            "1 268 km minus 645 km = 623 km",
            "Write the unit",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Multi-Step Problems
        self.next_band(2)
        self.write_rows(2, "Multi-Step Problems", [
            "Step 1: R18 650 + R6 375 = R25 025",
            "Step 2: R25 025 minus R9 990 = R15 035",
            "Read, plan, calculate, check",
            "Answer in a sentence",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Adding when the problem asks what is left''",
            "``3 km + 500 m = 503 km''",
            "``Sipho has R25 025''",
            "``623 with no unit''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Count the Rands
        self.next_band(4)
        self.write_rows(4, "Count the Rands", [
            "Add to join",
            "Subtract for what is left",
            "R2 495 left",
            "Profit: income minus expenses",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Same Units First
        self.next_band(5)
        self.write_rows(5, "Same Units First", [
            "Same units first",
            "3 km and 500 m is 3 500 m",
            "623 km left to drive",
            "Write the unit",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): One Step at a Time
        self.next_band(6)
        self.write_rows(6, "One Step at a Time", [
            "One step at a time",
            "R25 025 after the job",
            "R15 035 after the laptop",
            "Say it in a sentence",
        ], scale=0.9, box=2)

        last = Tex("Find the question, join or take away, keep the units the same, finish every step and answer in a sentence.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
