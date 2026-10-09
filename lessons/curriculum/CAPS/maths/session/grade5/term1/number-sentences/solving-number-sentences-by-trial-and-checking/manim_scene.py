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

# Band-layout whiteboard scene for solving-number-sentences-by-trial-and-checking (Part 1 Expert
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


class SolvingNumberSentencesByTrialAndCheckingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Solving by Inspection
        self.write_rows(0, "Solving by Inspection", [
            "Use facts you know",
            "Box plus 7 equals 15: the box is 8",
            "Equals means the same value on both sides",
            "25 plus 15 equals 10 plus 30",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Trial and Improvement
        self.next_band(1)
        self.write_rows(1, "Trial and Improvement", [
            "Try, then improve",
            "23 times 20 is 460: too small",
            "23 times 25 is 575: too big",
            "23 times 24 is 552: the box is 24",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Checking by Substitution and Inverses
        self.next_band(2)
        self.write_rows(2, "Checking by Substitution and Inverses", [
            "Undo with the inverse",
            "4 300 minus 1 875 is 2 425",
            "Put it back: 2 425 plus 1 875 is 4 300",
            "Box minus 368 equals 1 250: box is 1 618",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Box minus 368: subtract 368 again''",
            "``Random guesses with no plan''",
            "``Skip the check''",
            "``25 plus 15 equals 40 plus 30''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Just Look
        self.next_band(4)
        self.write_rows(4, "Just Look", [
            "Box plus 7 equals 15",
            "The box is 8",
            "60 times 6 is 360",
            "Both sides weigh the same",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Guess, Check, Improve
        self.next_band(5)
        self.write_rows(5, "Guess, Check, Improve", [
            "Box times 30 equals 840",
            "20 gives 600: go bigger",
            "30 gives 900: go smaller",
            "28 gives 840: got it",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Put It Back In
        self.next_band(6)
        self.write_rows(6, "Put It Back In", [
            "Undo the plus with a minus",
            "4 300 minus 1 875 is 2 425",
            "2 425 plus 1 875 is 4 300",
            "True, so the box is right",
        ], scale=0.9, box=2)

        last = Tex("Use what you know, let each try point the way, and put the answer back in the box to prove it.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
