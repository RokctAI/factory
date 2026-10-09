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

# Band-layout whiteboard scene for evaluating-the-solution-objectively (Part 1 Expert
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


class EvaluatingTheSolutionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What Evaluation Is and Why It Must Be Objective
        self.write_rows(0, "What Evaluation Is and Why It Must Be Objective", [
            "Evidence, not hope",
            "Objective: repeatable, verdict last",
            "Fair: its own brief; accurate: numbers, units",
            "In depth: setting, users, footprint, next",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Testing Against the Specifications
        self.next_band(1)
        self.write_rows(1, "Testing Against the Specifications", [
            "Rule, test, result, verdict",
            "500 g, thermometer, towel, 10/20/30 min",
            "Stack twenty, measure crushing, repeat",
            "Fail written plainly with its cause",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Fair, Accurate and In Depth: Judging the Impact
        self.next_band(2)
        self.write_rows(2, "Fair, Accurate and In Depth: Judging the Impact", [
            "Less harm? Estimate with assumptions",
            "Same benefit? Who says so?",
            "Works here? What breaks it?",
            "Own footprint; numbered fixes",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Verdict written before testing''",
            "``Feelings instead of numbers''",
            "``Object evaluated, harm forgotten''",
            "``Failed test hidden''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Does It Work? Prove It
        self.next_band(4)
        self.write_rows(4, "Does It Work? Prove It", [
            "Stand back from the finished model",
            "Set tests first, decide last",
            "Numbers, not 'it worked fine'",
            "Admitted fails are believed",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Test Every Rule, Write Every Number
        self.next_band(5)
        self.write_rows(5, "Test Every Rule, Write Every Number", [
            "Scale, jug, stopwatch, books",
            "Cannot test a year; say so",
            "Neutral question to three people",
            "Buckled at 14: start of the fix",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Honest About the Harm
        self.next_band(6)
        self.write_rows(6, "Honest About the Harm", [
            "Boxes a day kept out of drains",
            "Paperboard breaks up in weeks",
            "Who empties the crate?",
            "Harm moved is not harm removed",
        ], scale=0.9, box=3)

        last = Tex("Test every rule with numbers, record the fails with their causes, return to the brief, and be honest about your own footprint.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
