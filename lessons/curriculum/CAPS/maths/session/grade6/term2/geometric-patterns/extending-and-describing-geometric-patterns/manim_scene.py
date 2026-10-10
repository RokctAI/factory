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

# Band-layout whiteboard scene for extending-and-describing-geometric-patterns (Part 1 Expert
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


class ExtendingAndDescribingGeometricPatternsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Matchstick Patterns
        self.write_rows(0, "Matchstick Patterns", [
            "1 square: 4 matches",
            "Each new square adds 3",
            "4, 7, 10, 13, 16",
            "3 times the squares, plus 1",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Growing Shapes and Square Numbers
        self.next_band(1)
        self.write_rows(1, "Growing Shapes and Square Numbers", [
            "Square panels: 1, 4, 9, 16, 25",
            "Gaps 3, 5, 7, 9",
            "Panel 10: 10 times 10 = 100",
            "Pool border: 2 times the length, plus 6",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Describing and Creating Geometric Patterns
        self.next_band(2)
        self.write_rows(2, "Describing and Creating Geometric Patterns", [
            "Paper folds: 2, 4, 8, 16, 32",
            "Each fold doubles",
            "Say the start and what is added",
            "Cross of dots: 5, 9, 13, 17",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Each new square needs 4 matches''",
            "``1, 4, 9, 16, then 23''",
            "``10 squares need 40 matches''",
            "``It just gets bigger''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Count What Is Added
        self.next_band(4)
        self.write_rows(4, "Count What Is Added", [
            "Count what is added",
            "Shared side",
            "3 more matches",
            "10 squares: 31",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Shapes That Grow Faster
        self.next_band(5)
        self.write_rows(5, "Shapes That Grow Faster", [
            "Squares of beads",
            "1, 4, 9, 16",
            "Add 3, 5, 7",
            "Panel 10: 100 beads",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Make Your Own
        self.next_band(6)
        self.write_rows(6, "Make Your Own", [
            "Make your own",
            "Fold: doubles",
            "Draw three pictures",
            "Make a table",
        ], scale=0.9, box=1)

        last = Tex("Count what each new picture adds, write the counts in a table, and use the rule to predict pictures you have not drawn.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
