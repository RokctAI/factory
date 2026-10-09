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

# Band-layout whiteboard scene for fractions-and-division-in-sharing-problems (Part 1 Expert
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


class FractionsAndDivisionInSharingProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): A Fraction Is a Division
        self.write_rows(0, "A Fraction Is a Division", [
            "A fraction is a division",
            "3/4 means 3 divided by 4",
            "3 pizzas for 4 children: 3/4 each",
            "12/4 is 12 divided by 4, which is 3",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Sharing with Fraction Answers
        self.next_band(1)
        self.write_rows(1, "Sharing with Fraction Answers", [
            "7 oranges for 2: 3 and 1/2 each",
            "10 cakes for 4: 2 and 2/4 each",
            "23 divided by 4 is 5 and 3/4",
            "5 rotis for 3: 1 and 2/3 each",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Grouping Problems with Fractions
        self.next_band(2)
        self.write_rows(2, "Grouping Problems with Fractions", [
            "How many quarter cups in 3 cups?",
            "4 in each cup, 12 altogether",
            "5 litres fills 10 half-litre bottles",
            "3 m in 3/4 m pieces: 4 pieces",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3 pizzas for 4 children: 4/3 each''",
            "``7 oranges for 2: 3 remainder 1''",
            "``23 divided by 4 is 5 and 3/5''",
            "``Quarter cups in 3 cups: 3/4''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Top Shared by Bottom
        self.next_band(4)
        self.write_rows(4, "Top Shared by Bottom", [
            "Top shared by bottom",
            "3 shared by 4 is 3/4",
            "5/8 is 5 divided by 8",
            "6/3 is 6 divided by 3, which is 2",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Share the Leftovers
        self.next_band(5)
        self.write_rows(5, "Share the Leftovers", [
            "Share the leftovers too",
            "7 for 2: 3 and 1/2",
            "Leftover over the divisor",
            "23 divided by 4: 5 and 3/4",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): How Many Pieces Fit
        self.next_band(6)
        self.write_rows(6, "How Many Pieces Fit", [
            "How many pieces fit?",
            "4 quarter cups in each cup",
            "3 cups: 12 quarter cups",
            "5 litres: 10 half litres",
        ], scale=0.9, box=2)

        last = Tex("A fraction is a division: share the top by the bottom, share leftovers as fractions, and count how many pieces fit.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
