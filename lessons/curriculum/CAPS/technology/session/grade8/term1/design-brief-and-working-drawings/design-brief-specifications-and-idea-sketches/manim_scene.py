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

# Band-layout whiteboard scene for design-brief-specifications-and-idea-sketches (Part 1 Expert
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


class DesignBriefSketchesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From Scenario to Design Brief
        self.write_rows(0, "From Scenario to Design Brief", [
            "Scenario is the story; brief is the job",
            "Who, what need, what kind, where",
            "Say the problem, not the solution",
            "One or two sentences, starts with a verb",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Specifications and Constraints
        self.next_band(1)
        self.write_rows(1, "Specifications and Constraints", [
            "Specifications: testable musts",
            "Constraints: size, materials, time, cost, tools",
            "Musts are tested; limits are checked",
            "Measurable: 500 g, not 'strong'",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Initial Idea Sketches
        self.next_band(2)
        self.write_rows(2, "Initial Idea Sketches", [
            "Several quick, different, annotated ideas",
            "Pencil, 3D, no ruler, no erasing",
            "Table: ideas versus specs and constraints",
            "Keep rejected sketches",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``One neat drawing is the idea sketches''",
            "``Sketches need no labels''",
            "``The loudest member chooses''",
            "``Throw away rejected sketches''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Saying the Problem in One Sentence
        self.next_band(4)
        self.write_rows(4, "Saying the Problem in One Sentence", [
            "Story into a one-sentence job",
            "Who, need, thing, where",
            "No gears or pulleys yet",
            "Judged against it later",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Musts and Limits
        self.next_band(5)
        self.write_rows(5, "Musts and Limits", [
            "Musts: lift, hold, stand, enclose",
            "Limits: size, materials, lessons, budget",
            "Miss a must, it fails; break a limit, it is out",
            "Make musts testable",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Three Quick Ideas
        self.next_band(6)
        self.write_rows(6, "Three Quick Ideas", [
            "Three really different sketches",
            "Labels, arrows, best and worst line",
            "Tick table picks the winner",
            "Write why; keep the losers",
        ], scale=0.9, box=2)

        last = Tex("A brief states the problem, specifications and constraints set the musts and limits, and several annotated sketches find the best idea.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
