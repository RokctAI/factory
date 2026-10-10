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

# Band-layout whiteboard scene for writing-number-sentences-for-problems (Part 1 Expert
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


class WritingNumberSentencesForProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From Story to Number Sentence
        self.write_rows(0, "From Story to Number Sentence", [
            "Altogether: 1 245 plus 1 378 equals box",
            "How many more: 1 378 minus 1 245",
            "24 taxis of 15: 24 times 15 equals box",
            "Key words are clues, not rules",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Where the Box Goes
        self.next_band(1)
        self.write_rows(1, "Where the Box Goes", [
            "Put the box where the gap is",
            "Box plus 250 equals 1 750",
            "5 000 minus box equals 3 650",
            "Box times 24 equals 360",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Two-Step Sentences and Brackets
        self.next_band(2)
        self.write_rows(2, "Two-Step Sentences and Brackets", [
            "Two steps: bracket the first step",
            "(12 times 250) minus 1 200 equals box",
            "3 000 minus 1 200 is 1 800",
            "(3 times 18) plus (2 times 24) is 102",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1 245 minus 1 378 for how many more''",
            "``More than always means add''",
            "``Writing the answer, not the sentence''",
            "``Two steps with no brackets''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Story to Sentence
        self.next_band(4)
        self.write_rows(4, "Story to Sentence", [
            "Putting together: add",
            "How many more: subtract",
            "Equal groups: multiply",
            "Sharing or grouping: divide",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Box the Gap
        self.next_band(5)
        self.write_rows(5, "Box the Gap", [
            "Read the story in order",
            "Box plus 250 equals 1 750",
            "The box is where the gap is",
            "Read it back as a story",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): First Step in Brackets
        self.next_band(6)
        self.write_rows(6, "First Step in Brackets", [
            "Bracket the first step",
            "(12 times 250) minus 1 200",
            "3 000 minus 1 200 is 1 800",
            "R1 800 is left",
        ], scale=0.9, box=0)

        last = Tex("Read the story, put the box in the gap, bracket the first step, and read the sentence back.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
