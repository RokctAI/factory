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

# Band-layout whiteboard scene for identifying-a-need-for-a-plastic-item (Part 1 Expert
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


class IdentifyingANeedForAPlasticItemSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Finding a Real Need Around You
        self.write_rows(0, "Finding a Real Need Around You", [
            "Need = gap between is and wanted; observe people",
            "Tap, cables, phone, bottle, hooks, bin",
            "Good need: real, specific, small, suits plastic",
            "Problem statement: who, what, where, why",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Writing the Design Brief and Specifications
        self.next_band(1)
        self.write_rows(1, "Writing the Design Brief and Specifications", [
            "Brief: what, for whom, to do what; no solution named",
            "Specs: measurable; function, size, material",
            "Durability, safety, cost, environment, looks",
            "Write before sketching; tests check specs",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Choosing Recycled Plastic and a Making Method
        self.next_band(2)
        self.write_rows(2, "Choosing Recycled Plastic and a Making Method", [
            "Outdoors/knocked: PP or HDPE, UV stabilised",
            "Clear: PET sheet; flat: HIPS/PET; hinge: PP",
            "Design for injection; make with school method",
            "Ready: statement, brief, 6 specs, plastic, method",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Product chosen first, need invented after''",
            "``Brief that names the solution''",
            "``Untestable specification like good quality''",
            "``Plastic chosen for colour alone''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Problem Worth Solving
        self.next_band(4)
        self.write_rows(4, "A Problem Worth Solving", [
            "Watch where people struggle",
            "One small real problem",
            "Suits plastic",
            "Who, what, where, why",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Say Exactly What It Must Do
        self.next_band(5)
        self.write_rows(5, "Say Exactly What It Must Do", [
            "Say the need, not the answer",
            "Testable, not vague",
            "Size in mm, cost in rand",
            "Contract for the end",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Which Plastic, Made How
        self.next_band(6)
        self.write_rows(6, "Which Plastic, Made How", [
            "Plastic from the specs",
            "Mould rules, school tools",
            "Old bucket is fine",
            "Four things ready",
        ], scale=0.9, box=2)

        last = Tex("A design begins with an observed need written as a problem statement, a brief that leaves the solution open, measurable specifications, and a recycled plastic and method chosen to meet them.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
