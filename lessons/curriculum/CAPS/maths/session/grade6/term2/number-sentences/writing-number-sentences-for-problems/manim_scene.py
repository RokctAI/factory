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
        # --- Band 0 (subtopic_1): Choosing the Operation
        self.write_rows(0, "Choosing the Operation", [
            "Joining: add. Comparing: subtract.",
            "Equal groups: multiply. Sharing: divide.",
            "1 480 + 2 365 = box",
            "2 365 minus 1 480 = box: 885",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Where the Box Goes
        self.next_band(1)
        self.write_rows(1, "Where the Box Goes", [
            "The box goes at the gap",
            "box minus 3 750 = 8 250",
            "The box is 12 000",
            "Equals means the same value",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Two-Step Number Sentences
        self.next_band(2)
        self.write_rows(2, "Two-Step Number Sentences", [
            "4 times 85 + 6 times 45 = box",
            "340 + 270 = 610",
            "(2 000 minus 560) divided by 6 = box",
            "Each team gets R240",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``1 480 minus 2 365 = box''",
            "``8 250 minus 3 750 = box for the start''",
            "``No brackets in the cake sale''",
            "``Equals means the answer comes next''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): What Is Happening
        self.next_band(4)
        self.write_rows(4, "What Is Happening", [
            "What is happening?",
            "Join, compare, group, share",
            "3 845 tickets",
            "885 more on Saturday",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Box at the Gap
        self.next_band(5)
        self.write_rows(5, "Box at the Gap", [
            "Box at the gap",
            "box minus 3 750 = 8 250",
            "12 000 to start with",
            "Both sides balance",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Two Steps in One Sentence
        self.next_band(6)
        self.write_rows(6, "Two Steps in One Sentence", [
            "Two steps, one sentence",
            "Multiply first: R610",
            "Brackets go first",
            "R240 for each team",
        ], scale=0.9, box=2)

        last = Tex("Picture the story, put the box at the gap, and use brackets for the step that must come first.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
