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
        # --- Band 0 (subtopic_1): Seeing What Changes
        self.write_rows(0, "Seeing What Changes", [
            "Squares in a row: 4, 7, 10 matchsticks",
            "Each new square adds 3",
            "Staircase: 1, 3, 6, 10 blocks",
            "Differences 2, 3, 4: not constant",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Describing the Rule in Words
        self.next_band(1)
        self.write_rows(1, "Describing the Rule in Words", [
            "Rule 1: add 3 each time",
            "Rule 2: 3 times position plus 1",
            "Picture 20: 3 times 20 plus 1 is 61",
            "Triangles of dots: 1, 3, 6, 10",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Patterns of Your Own
        self.next_band(2)
        self.write_rows(2, "Patterns of Your Own", [
            "Start picture plus a rule",
            "T shape: 5, 7, 9, 11",
            "Cross of dots: 5, 9, 13, 17",
            "A friend must be able to continue it",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Each new square adds 4 sticks''",
            "``All patterns add the same amount''",
            "``Rules are only about numbers''",
            "``Change it differently each time''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): What Changed
        self.next_band(4)
        self.write_rows(4, "What Changed", [
            "What was added?",
            "3 new matchsticks each time",
            "4, 7, 10, 13",
            "Staircase jumps: 2, 3, 4",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Say the Rule
        self.next_band(5)
        self.write_rows(5, "Say the Rule", [
            "Next picture: add 3",
            "Picture number: times 3 plus 1",
            "Picture 10: 31 matchsticks",
            "The plus 1 is the first left side",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Make Your Own
        self.next_band(6)
        self.write_rows(6, "Make Your Own", [
            "Start shape plus a rule",
            "5, 7, 9, 11",
            "Can a friend draw picture 5?",
            "Bricks, tiles and beads",
        ], scale=0.9, box=2)

        last = Tex("See what changes, count it, say the rule in words, and make sure a friend could draw the next picture.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
