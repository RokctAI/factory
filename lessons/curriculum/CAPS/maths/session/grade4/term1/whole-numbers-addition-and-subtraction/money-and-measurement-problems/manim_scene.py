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
        # --- Band 0 (subtopic_1): Money Problems
        self.write_rows(0, "Money Problems", [
            "Altogether: add the takings",
            "2 375 plus 1 860 is 4 235",
            "How much more: subtract",
            "Change: 50 minus the total spent",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Distance and Length Problems
        self.next_band(1)
        self.write_rows(1, "Distance and Length Problems", [
            "42 minus 27 is 15 kilometres",
            "1 250 minus 865 is 385 metres",
            "1 450 plus 600 plus 1 875 is 3 925",
            "Same units before you add",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Capacity, Mass and the Four-Step Routine
        self.next_band(2)
        self.write_rows(2, "Capacity, Mass and the Four-Step Routine", [
            "5 000 minus 3 245 is 1 755 litres",
            "1 275 plus 2 850 is 4 125 grams",
            "Read, write, calculate, check",
            "The story is the final check",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Total spent answers a change question''",
            "``2 km plus 350 m is 352''",
            "``Leave the unit off''",
            "``Any answer is fine if the sum is right''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Money Stories
        self.next_band(4)
        self.write_rows(4, "Money Stories", [
            "Altogether: add",
            "How much more: take away",
            "Change: paid minus spent",
            "Answer what was asked",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Distance Stories
        self.next_band(5)
        self.write_rows(5, "Distance Stories", [
            "42 minus 27 is 15 km",
            "1 250 minus 865 is 385 m",
            "Same units together",
            "Write the unit in the answer",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Tanks, Flour and the Final Check
        self.next_band(6)
        self.write_rows(6, "Tanks, Flour and the Final Check", [
            "5 000 minus 3 245 is 1 755 litres",
            "1 275 plus 2 850 is 4 125 grams",
            "Read, write, calculate, check",
            "Could it really happen?",
        ], scale=0.9, box=2)

        last = Tex("Read, write the sentence, calculate two ways, answer with the unit, and check it fits the story.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
