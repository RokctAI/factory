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

# Band-layout whiteboard scene for design-brief-and-initial-sketches-for-the-headgear (Part 1 Expert
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


class HeadgearBriefAndSketchesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Writing the Headgear Design Brief
        self.write_rows(0, "Writing the Headgear Design Brief", [
            "Need, users, setting, purpose; no shape",
            "Every phrase from the notice or investigation",
            "'What we know': forms, gears, 40 m",
            "Checked line by line against the notice",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Specifications and Constraints From the Tender
        self.next_band(1)
        self.write_rows(1, "Specifications and Constraints From the Tender", [
            "300 g in 10-20 s; MA and speed",
            "Sway under 10 mm; triangulation, back-leg",
            "No topple at 100 mm swing; base",
            "Constraints: materials, cost, size, time",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Initial Idea Sketches of the Headgear
        self.next_band(2)
        self.write_rows(2, "Initial Idea Sketches of the Headgear", [
            "A-frame; four-legged; box tower",
            "Rope path, gears, materials, forces, safety",
            "Base plan and winder detail",
            "Compare, do not choose until Week 6",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Brief names the A-frame''",
            "``Specifications without numbers''",
            "``Sketches without the rope path''",
            "``One tower in three colours''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): What the Mine Asked For
        self.next_band(4)
        self.write_rows(4, "What the Mine Asked For", [
            "The mine's problem, not your answer",
            "40 m fixes the rope angle",
            "Sign, date, check",
            "Board reads this first",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Must Lift, Must Stand, Must Fit
        self.next_band(5)
        self.write_rows(5, "Must Lift, Must Stand, Must Fit", [
            "Must lift: 300 g, 10-20 s",
            "Must stand: 10 mm sway, no topple",
            "Must fit: 300 by 300, through a door",
            "Rule, reason, force",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Three Towers on Paper
        self.next_band(6)
        self.write_rows(6, "Three Towers on Paper", [
            "Three truly different towers",
            "Draw the rope, drum to cage",
            "Write materials and forces on",
            "Strangers must be able to judge",
        ], scale=0.9, box=1)

        last = Tex("State the mine's problem, set numbered rules with their forces, and sketch three different towers with the rope drawn, ready for other companies to judge.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
