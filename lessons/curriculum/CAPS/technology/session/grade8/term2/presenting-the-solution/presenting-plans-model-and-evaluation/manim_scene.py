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

# Band-layout whiteboard scene for presenting-plans-model-and-evaluation (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/160/120/110/90 of 850 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PresentingTheSolutionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Design Presentation Must Do
        self.write_rows(0, "What a Design Presentation Must Do", [
            "Understand, judge, decide",
            "Assessor, class, client",
            "Evidence, exact words, candour",
            "Name the weakness first",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Structuring the Presentation Around the Design Process
        self.next_band(1)
        self.write_rows(1, "Structuring the Presentation Around the Design Process", [
            "30 s problem story; 45 s brief",
            "60 s two ideas and the choice",
            "45 s drawings and make; 90 s evaluation",
            "30 s recommendations; everyone speaks",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Delivering It: Visuals, Voice and Questions
        self.next_band(2)
        self.write_rows(2, "Delivering It: Visuals, Voice and Questions", [
            "Model up at start and during evaluation",
            "Point to drawings; name them",
            "Big tables, fails highlighted; no text slides",
            "Hear, repeat, answer with evidence",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Portfolio read page by page''",
            "``Failed tests hidden''",
            "``Slides full of text''",
            "``One member speaks for all''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Tell the Story of the Problem
        self.next_band(4)
        self.write_rows(4, "Tell the Story of the Problem", [
            "Portfolio said aloud, in order",
            "Not a show of effort, not an advert",
            "63 boxes in one drain",
            "'Forty cents', not 'a bit more'",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Investigate, Design, Make, Evaluate, in Five Minutes
        self.next_band(5)
        self.write_rows(5, "Investigate, Design, Make, Evaluate, in Five Minutes", [
            "Story, brief, ideas, drawings, make, evaluate",
            "Evaluation longest",
            "Builder talks building; tester talks testing",
            "Cards, not pages",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Hold Up the Model and Answer Back
        self.next_band(6)
        self.write_rows(6, "Hold Up the Model and Answer Back", [
            "Finger on the rib: buckled at fourteen",
            "Rehearse twice with a timer",
            "Do not know? Say how you would find out",
            "Never argue, never guess",
        ], scale=0.9, box=2)

        last = Tex("Tell the problem as a story, walk the design steps with the model in hand, give the evaluation the most time, and answer questions with evidence and honesty.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
