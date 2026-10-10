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

# Band-layout whiteboard scene for revision-of-term-1-and-2-work (Part 1 Expert
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


class RevisionOfTerm1And2WorkSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Whole Numbers and Number Sentences
        self.write_rows(0, "Whole Numbers and Number Sentences", [
            "1 344 times 18 = R24 192",
            "Estimate: 1 300 times 20 = 26 000",
            "box times 24 = 1 344, so box = 56",
            "Check: 56 times 24 = 1 344",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Numeric and Geometric Patterns
        self.next_band(1)
        self.write_rows(1, "Numeric and Geometric Patterns", [
            "5; 9; 13; 17; 21",
            "Rule: position times 4 + 1",
            "20th term: 81",
            "Squares: times 3 + 1, so 10 squares need 31",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Fractions, Decimals and Percentages
        self.next_band(2)
        self.write_rows(2, "Fractions, Decimals and Percentages", [
            "3/8 of 1 344 = 504",
            "25 per cent of 1 344 = 336",
            "3/8 + 2/8 = 5/8",
            "0,35 + 0,60 = 0,95",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``3/8 + 1/4 = 4/12''",
            "``0,35 + 0,6 = 0,41''",
            "``20th term of 5; 9; 13 is 80''",
            "``245 368 rounds to 246 000''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Count and Calculate
        self.next_band(4)
        self.write_rows(4, "Count and Calculate", [
            "Count and calculate",
            "Estimate first",
            "Box times 24 = 1 344",
            "Box is 56",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Find the Rule
        self.next_band(5)
        self.write_rows(5, "Find the Rule", [
            "Find the rule",
            "Times 4, plus 1",
            "Times 3, plus 1",
            "Work backwards",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Parts of the Whole
        self.next_band(6)
        self.write_rows(6, "Parts of the Whole", [
            "Parts of the whole",
            "3/8 of 1 344 is 504",
            "0,35 + 0,6 is 0,95",
            "3/4 is 0,75",
        ], scale=0.9, box=1)

        last = Tex("Estimate before, check after: every tool from Terms 1 and 2 works best with a check.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
