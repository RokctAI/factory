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

# Band-layout whiteboard scene for presenting-to-the-tender-board (Part 1 Expert
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


class TenderBoardPresentationSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Tender Board Looks For
        self.write_rows(0, "What a Tender Board Looks For", [
            "Board = client; hunts for risk",
            "Rubric first; minutes follow marks",
            "Specialists ask from knowledge",
            "Evidence, numbers, candour",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Structuring the Bid Presentation: Research to Budget
        self.next_band(1)
        self.write_rows(1, "Structuring the Bid Presentation: Research to Budget", [
            "Six documents, design-process order",
            "1-1-1-2-1-0.5 minutes",
            "Each presents their own part; budget by its maker",
            "Rehearse twice; protect the demo",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): The Demonstration, the Questions and the Board's Decision
        self.next_band(2)
        self.write_rows(2, "The Demonstration, the Questions and the Board's Decision", [
            "Test on the real table; checklist on the base",
            "Narrate the numbers as it lifts",
            "Sources and dates; admit omissions",
            "Board scores, confers, gives reasons",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Demo run first in front of the board''",
            "``Budget presented by someone who does not know the rates''",
            "``Model without its drawings''",
            "``Arguing with a board member''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Who Is in the Room and What They Want
        self.next_band(4)
        self.write_rows(4, "Who Is in the Room and What They Want", [
            "Who is in the room",
            "They have read your documents",
            "Four companies, one rubric",
            "Teamwork under pressure",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Seven Minutes, Six Documents, One Model
        self.next_band(5)
        self.write_rows(5, "Seven Minutes, Six Documents, One Model", [
            "Brief, drawing, gears, demo, money, close",
            "Hold up the model early",
            "Point at every document",
            "Cards, not pages",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Lift the Cage, Take the Questions
        self.next_band(6)
        self.write_rows(6, "Lift the Cage, Take the Questions", [
            "Switch, narrator, stopwatch, watcher",
            "Fail live? Say so, quote the table",
            "'We'd need to check' is allowed",
            "Flashiest rarely wins",
        ], scale=0.9, box=1)

        last = Tex("Know the rubric, walk the six documents, demonstrate with numbers you tested beforehand, answer with sources, and let the evidence win the tender.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
