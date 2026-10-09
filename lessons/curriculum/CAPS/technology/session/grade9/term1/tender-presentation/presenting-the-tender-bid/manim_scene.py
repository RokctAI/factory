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

# Band-layout whiteboard scene for presenting-the-tender-bid (Part 1 Expert
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


class PresentingTheTenderBidSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Tender Board Wants to Hear
        self.write_rows(0, "What a Tender Board Wants to Hear", [
            "Understanding; specs met; real price; trust",
            "Evidence, not claims",
            "Fixed time; running over costs marks",
            "Explain terms; numbers with reasons",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Structuring the Presentation: Sketches, Plans, Budget, Model
        self.next_band(1)
        self.write_rows(1, "Structuring the Presentation: Sketches, Plans, Budget, Model", [
            "Open; Investigate; Design; Make; Budget; Close",
            "Half, 1, 2, 1, 1, half minutes",
            "One stage per member; quick handovers",
            "Rehearse with a timer; predict questions",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Speaking, Answering and Judging Other Bids Fairly
        self.next_band(2)
        self.write_rows(2, "Speaking, Answering and Judging Other Bids Fairly", [
            "Answer briefly with evidence",
            "Do not know? Say so, say how to find out",
            "Score the bid on the sheet, with reasons",
            "Award with reasons; losing teaches",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Model shown, investigation skipped''",
            "``One member speaks for all''",
            "``Bluffed answer''",
            "``Scored by friendship''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Who You Are Talking To
        self.next_band(4)
        self.write_rows(4, "Who You Are Talking To", [
            "They spend the school's money",
            "Four things they listen for",
            "1 in 12 beats very safe",
            "Talk to people, point at the model",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): The Order of the Story
        self.next_band(5)
        self.write_rows(5, "The Order of the Story", [
            "Six parts in order",
            "Everyone speaks",
            "Timer and cuts",
            "Answers are in the file",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Say It, Show It, Answer It
        self.next_band(6)
        self.write_rows(6, "Say It, Show It, Answer It", [
            "Point to the number",
            "Honest beats bluff",
            "Reason for every score",
            "Bid, not friends",
        ], scale=0.9, box=1)

        last = Tex("Tell the term in IDMEC order with evidence, share the speaking, answer honestly, and judge other bids on the sheet: communicating and evaluating as a tender board does.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
