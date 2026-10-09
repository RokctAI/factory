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
            "1 shared among 4: 1/4 each",
            "3 shared among 4: 3/4 each",
            "Top: amount shared",
            "Bottom: how many share",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Fractions of a Group
        self.next_band(1)
        self.write_rows(1, "Fractions of a Group", [
            "1/4 of 20: 20 divided by 4 is 5",
            "3/4 of 20: 3 times 5 is 15",
            "Divide by the bottom",
            "Multiply by the top",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Sharing and Grouping Problems
        self.next_band(2)
        self.write_rows(2, "Sharing and Grouping Problems", [
            "7 rotis between 2: 3 and a half each",
            "10 loaves among 4: 2 and a half each",
            "3 cups hold 6 half cups",
            "Only cut what can be cut",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3 among 4 is 4/3''",
            "``3/4 of 20: divide by 3''",
            "``7 rotis between 2: 3 remainder 1''",
            "``Half a learner''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Share One, Share Many
        self.next_band(4)
        self.write_rows(4, "Share One, Share Many", [
            "1 among 4: 1/4",
            "3 among 4: 3/4",
            "Top: what is shared",
            "Bottom: who shares",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): A Fraction of a Group
        self.next_band(5)
        self.write_rows(5, "A Fraction of a Group", [
            "Divide by the bottom",
            "Times by the top",
            "3/4 of 20 is 15",
            "2/3 of 18 is 12",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Leftovers Become Fractions
        self.next_band(6)
        self.write_rows(6, "Leftovers Become Fractions", [
            "7 between 2: 3 and a half",
            "10 among 4: 2 and a half",
            "3 cups: 6 half cups",
            "Cut bread, not children",
        ], scale=0.9, box=0)

        last = Tex("A fraction is a sharing: divide by the bottom, times by the top, and cut only what can be cut.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
