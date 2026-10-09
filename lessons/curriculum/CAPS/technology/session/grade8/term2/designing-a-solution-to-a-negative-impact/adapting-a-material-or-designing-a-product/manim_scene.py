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

# Band-layout whiteboard scene for adapting-a-material-or-designing-a-product (Part 1 Expert
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


class SolutionDesignBriefSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From Investigation to Design Brief
        self.write_rows(0, "From Investigation to Design Brief", [
            "Problem, users, setting, purpose",
            "Never name the solution",
            "Worst harm by evidence",
            "Real users, real place",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Two Routes: Adapt the Material or Design the Product
        self.next_band(1)
        self.write_rows(1, "Two Routes: Adapt the Material or Design the Product", [
            "Adapt the material: bagasse, thicker bag",
            "Design the product: returnable, drain guard",
            "New material must carry the old forces",
            "Harm in use? Change the system",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Specifications and Constraints for the Solution
        self.next_band(2)
        self.write_rows(2, "Specifications and Constraints for the Solution", [
            "Specification: must do and be",
            "Constraint: must stay inside",
            "Measurable, traceable, matters",
            "Each rule hides a force",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Brief names the solution''",
            "``Specifications that cannot be measured''",
            "``Constraints that forget the setting''",
            "``Material chosen on story, not tested on forces''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Turning a Problem into a Brief
        self.next_band(4)
        self.write_rows(4, "Turning a Problem into a Brief", [
            "Who is hurt, where, what for",
            "Not 'design a box'",
            "One purpose judges every idea",
            "No bins, no tap, thin margins",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Fix the Stuff or Fix the Thing
        self.next_band(5)
        self.write_rows(5, "Fix the Stuff or Fix the Thing", [
            "Fix the stuff or fix the thing",
            "Look where the harm sits",
            "Biodegradable still blocks a drain",
            "Often do both; sketch two",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Must Do, Must Not, Can Only
        self.next_band(6)
        self.write_rows(6, "Must Do, Must Not, Can Only", [
            "500 g for 30 minutes: testable",
            "Twenty high because the box is twenty deep",
            "Fifty cents, no electricity",
            "Compression, bending, shear",
        ], scale=0.9, box=3)

        last = Tex("State the problem, not the answer; choose adapt or design by where the harm sits; and write rules you can test, each with its reason and its force.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
