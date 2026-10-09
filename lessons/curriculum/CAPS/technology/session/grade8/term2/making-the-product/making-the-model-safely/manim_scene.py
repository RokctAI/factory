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

# Band-layout whiteboard scene for making-the-model-safely (Part 1 Expert
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


class MakingTheModelSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Planning the Make: Sequence, Materials and Tools
        self.write_rows(0, "Planning the Make: Sequence, Materials and Tools", [
            "Steps in order, who, tool, time",
            "Parts first; dry fit before glue",
            "Tests tied to specifications",
            "Model answers questions; say which",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Safe Use of Tools and Materials
        self.next_band(1)
        self.write_rows(1, "Safe Use of Tools and Materials", [
            "Knife towards you, along the steel rule",
            "Fingers on top of the rule",
            "Hot tools at their station only",
            "Eyes covered; report everything",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Marking Out, Cutting, Forming and Joining
        self.next_band(2)
        self.write_rows(2, "Marking Out, Cutting, Forming and Joining", [
            "Full-size numbers, check twice",
            "Score folds, cut outlines",
            "Join for the force",
            "Photograph and record every change",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Cut before plan and dry fit''",
            "``Knife towards the rule hand''",
            "``Fold lines cut, not scored''",
            "``Design changed, not recorded''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Plan Before You Cut
        self.next_band(4)
        self.write_rows(4, "Plan Before You Cut", [
            "Write the plan, then cut",
            "Spare material for first mistakes",
            "Leave time for testing",
            "Say what the model tests",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Sharp Things, Hot Things, Fingers
        self.next_band(5)
        self.write_rows(5, "Sharp Things, Hot Things, Fingers", [
            "Pen grip, light passes, cap it",
            "Hot glue: cold water, no wiping",
            "Windows open for hot wire",
            "Ask before using a tool",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Measure, Cut, Fold, Glue
        self.next_band(6)
        self.write_rows(6, "Measure, Cut, Fold, Glue", [
            "Mark folds differently from cuts",
            "Slots from the corners in",
            "Long tabs, gussets, mechanical joints",
            "Changes normal; unwritten changes not",
        ], scale=0.9, box=3)

        last = Tex("Plan the steps, cut safely along the rule, score folds and join for the force, and record every step and change.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
