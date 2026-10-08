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

# Band-layout whiteboard scene for evaluating-and-improving-design-ideas (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (220/160/160/110/110/110 of 870 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EvaluatingAndImprovingDesignIdeasSession(MovingCameraScene):
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
        self.wait(43)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Evaluating against the brief
        self.write_rows(0, "Evaluating against the brief", [
            "Specifications down, ideas across",
            "Tick, cross or question mark with a reason",
            "Two advantages, two disadvantages each",
            "Advise; the owner decides",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Giving and receiving criticism
        self.next_band(1)
        self.write_rows(1, "Giving and receiving criticism", [
            "The design, not the designer",
            "What works first; specific; suggest",
            "Listen, write it down, ask, thank, decide later",
            "Accepted or rejected, always with a reason",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Adapting and improving
        self.next_band(2)
        self.write_rows(2, "Adapting and improving", [
            "One change per comment, with a reason",
            "Third sketch or marked revisions",
            "Keep the original visible",
            "Re-check every specification",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Evaluate by taste''",
            "``Criticise the person''",
            "``Start a new design''",
            "``Erase the original''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Judging against the brief
        self.next_band(4)
        self.write_rows(4, "Judging against the brief", [
            "Tick, cross, question mark",
            "Reasons in the words of the term",
            "Good and weak, at least two each",
            "You choose your own idea",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): How to say it and hear it
        self.next_band(5)
        self.write_rows(5, "How to say it and hear it", [
            "Design, not person",
            "Point to the brief",
            "Hear it all, write it down",
            "Decide later, give reasons",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Better, not starting over
        self.next_band(6)
        self.write_rows(6, "Better, not starting over", [
            "Change by change, reason by reason",
            "Before and after, both on the page",
            "Say what you took and what you rejected",
            "Check the brief again",
        ], scale=0.9, box=1)

        last = Tex("Judge against the brief, speak to the design, listen fully, and improve by recorded changes.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
