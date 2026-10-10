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

# Band-layout whiteboard scene for revision-of-numbers-operations-and-patterns (Part 1 Expert
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


class RevisionOfNumbersOperationsAndPatternsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Whole Numbers, Adding and Subtracting
        self.write_rows(0, "Whole Numbers, Adding and Subtracting", [
            "136 480: the 3 is worth 30 000",
            "Nearest 1 000: 136 000",
            "1 245 + 1 878 = 3 123",
            "1 878 minus 1 245 is 633",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Multiplying, Dividing and Fractions
        self.next_band(1)
        self.write_rows(1, "Multiplying, Dividing and Fractions", [
            "48 times 26 is 960 + 288",
            "1 248 chairs, 52 stacks of 24",
            "750 programmes: 19 bundles",
            "3/8 of 48 is 18 rows",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Patterns and Number Sentences
        self.next_band(2)
        self.write_rows(2, "Patterns and Number Sentences", [
            "20, 24, 28, 32, 36: add 4",
            "Cups: 1, 3, 6, 10, 15",
            "Times 35, plus 5: 4 gives 145",
            "R180: 175 divided by 35 is 5",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``136 480 rounds to 137 000''",
            "``18 bundles for 750''",
            "``2/5 + 1/5 = 3/10''",
            "``4 plus 5 first: R315''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): At the Ticket Desk
        self.next_band(4)
        self.write_rows(4, "At the Ticket Desk", [
            "At the ticket desk",
            "The 3 is worth 30 000",
            "3 123 people",
            "633 more on Saturday",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): In the Hall
        self.next_band(5)
        self.write_rows(5, "In the Hall", [
            "In the hall",
            "1 248 chairs",
            "19 bundles",
            "3/8 of 48 is 18",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Price Patterns
        self.next_band(6)
        self.write_rows(6, "Price Patterns", [
            "Price patterns",
            "Times 35, plus 5",
            "4 tickets: R145",
            "R180: 5 tickets",
        ], scale=0.9, box=1)

        last = Tex("Place value, operations, fractions and patterns: every number tool from the year, estimated first and checked every time.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
