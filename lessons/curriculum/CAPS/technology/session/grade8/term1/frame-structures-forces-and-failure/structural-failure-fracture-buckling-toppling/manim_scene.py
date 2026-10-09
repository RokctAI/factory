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

# Band-layout whiteboard scene for structural-failure-fracture-buckling-toppling (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/150/120/110/90 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class StructuralFailureSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Fracture: a Lack of Strength
        self.write_rows(0, "Fracture: a Lack of Strength", [
            "Fracture: snapped, torn, crushed",
            "Brittle snaps; ductile stretches first",
            "Fatigue: many small loads",
            "Cure: more material, bigger joints",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Bending and Buckling: a Lack of Stiffness
        self.next_band(1)
        self.write_rows(1, "Bending and Buckling: a Lack of Stiffness", [
            "Stiffness: holds its shape",
            "Bending: cure with depth and triangles",
            "Buckling: long thin strut bows",
            "Cure: brace, tube, or put in tension",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Toppling: a Lack of Stability
        self.next_band(2)
        self.write_rows(2, "Toppling: a Lack of Stability", [
            "Stability: stays upright",
            "Wide base, low centre of gravity",
            "Sideways push tips it past the edge",
            "Three failures, three different cures",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Every collapse is a lack of strength''",
            "``Stiff means stable''",
            "``A bowed member was weak''",
            "``Weight on top holds it down''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): When It Snaps
        self.next_band(4)
        self.write_rows(4, "When It Snaps", [
            "It snapped: not strong enough",
            "Chalk sudden, steel with warning",
            "Paper clip fatigue",
            "Bigger glue area",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): When It Bends or Bows
        self.next_band(5)
        self.write_rows(5, "When It Bends or Bows", [
            "It sagged or bowed: not stiff enough",
            "Card on edge, box, tube",
            "Ruler from the top: buckling",
            "Brace it halfway",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): When It Falls Over
        self.next_band(6)
        self.write_rows(6, "When It Falls Over", [
            "It fell over: not stable enough",
            "Wide bottom, weight low, light top",
            "Anchor the base",
            "Diagnose first, then fix",
        ], scale=0.9, box=1)

        last = Tex("Snapped means strength, bent or bowed means stiffness, fell over means stability: diagnose the failure, then choose the cure.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
