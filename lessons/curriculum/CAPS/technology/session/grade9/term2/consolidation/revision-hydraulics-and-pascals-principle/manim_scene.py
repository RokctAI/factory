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

# Band-layout whiteboard scene for revision-hydraulics-and-pascals-principle (Part 1 Expert
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


class RevisionHydraulicsAndPascalsPrincipleSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Revising Pneumatics and Hydraulics: Syringes, Gases and Liquids
        self.write_rows(0, "Revising Pneumatics and Hydraulics: Syringes, Gases and Liquids", [
            "Air: spongy, compressible; water: immediate, incompressible",
            "Pneumatic = gas; hydraulic = liquid",
            "Small -> large: force up, distance down",
            "Air in brakes: spongy pedal",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Revising Pascal's Principle and the Distance-Force Trade-Off
        self.next_band(1)
        self.write_rows(1, "Revising Pascal's Principle and the Distance-Force Trade-Off", [
            "Pascal: pressure equal throughout",
            "F\\_in / A\\_in = F\\_out / A\\_out",
            "A x d equal both sides: trade-off",
            "MA = A\\_out / A\\_in; 2 and 10 -> 5",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Revising Press Calculations, the Jack and Systems Diagrams
        self.next_band(2)
        self.write_rows(2, "Revising Press Calculations, the Jack and Systems Diagrams", [
            "Step 1: p = F / A; step 2: F = p x A; step 3: check",
            "100 N on 5 -> 20; 20 on 50 -> 1000 N",
            "Jack: pump, one-way valve, release valve",
            "Systems diagram: input -> process -> output",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Input and output areas swapped''",
            "``Square centimetres mixed with square metres''",
            "``Jack said to create energy''",
            "``Systems diagram drawn as a picture''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Push Here, It Pushes There
        self.next_band(4)
        self.write_rows(4, "Push Here, It Pushes There", [
            "Gases squash, liquids do not",
            "Oil in jacks for full, instant force",
            "Small to big: strong and short",
            "Spongy means air",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Same Pressure, Different Areas
        self.next_band(5)
        self.write_rows(5, "Same Pressure, Different Areas", [
            "Same pressure everywhere",
            "Bigger area, bigger force",
            "Same volume, shorter move",
            "Work the same",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Three Steps, Then Check
        self.next_band(6)
        self.write_rows(6, "Three Steps, Then Check", [
            "Pressure, apply, check",
            "Big area gets big force",
            "Jack = press + pump + valves",
            "Boxes and arrows, not a picture",
        ], scale=0.9, box=0)

        last = Tex("Liquids do not compress, pressure is equal throughout, volume moved is equal: from these, every hydraulic force and distance follows.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
