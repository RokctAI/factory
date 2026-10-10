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

# Band-layout whiteboard scene for solving-number-sentences-and-checking-by-substitution (Part 1 Expert
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


class SolvingNumberSentencesAndCheckingBySubstitutionSession(MovingCameraScene):
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
            "Look for a fact you know",
            "7 times box = 63: box = 9",
            "Undo: box minus 2 480 = 3 520",
            "3 520 + 2 480 = 6 000",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Trial and Improvement
        self.next_band(1)
        self.write_rows(1, "Trial and Improvement", [
            "Guess, test, improve",
            "40 times 24 = 960: too small",
            "50 times 24 = 1 200: too big",
            "47 times 24 = 1 128",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Checking by Substitution
        self.next_band(2)
        self.write_rows(2, "Checking by Substitution", [
            "Put the answer back in",
            "3 times 10 + 5 = 35: wrong",
            "3 times 9 + 5 = 32: right",
            "Both sides equal: correct",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``box minus 2 480 = 3 520 gives 1 040''",
            "``Guessing at random''",
            "``3 times (10 + 5) when checking''",
            "``Handing in 10 with no check''",
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
            "Just look",
            "7 times 9 = 63",
            "250 + 750 = 1 000",
            "Undo to find 6 000",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Try, Then Get Closer
        self.next_band(5)
        self.write_rows(5, "Try, Then Get Closer", [
            "Try, then get closer",
            "Too small: go up",
            "Too big: go down",
            "47 bags",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Put It Back In
        self.next_band(6)
        self.write_rows(6, "Put It Back In", [
            "Put it back in",
            "47 times 24 = 1 128",
            "Sides match: correct",
            "Sides differ: try again",
        ], scale=0.9, box=1)

        last = Tex("Look for a fact or undo it, guess and improve when you must, and always put the answer back in to prove it.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
