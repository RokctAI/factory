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

# Band-layout whiteboard scene for term-1-revision-orthographic-projection-forces-and-costing (Part 1 Expert
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


class Term1RevisionOrthographicProjectionForcesAndCostingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Revising Orthographic Projection and the Drawing Conventions
        self.write_rows(0, "Revising Orthographic Projection and the Drawing Conventions", [
            "Dark, feint, dashed, wavy, chain",
            "Standard scale; real sizes once",
            "Top below front; end view opposite",
            "Hole: circle then dashed; slope true in one view",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Revising Forces, Loads and Material Properties
        self.next_band(1)
        self.write_rows(1, "Revising Forces, Loads and Material Properties", [
            "Static vs dynamic; even vs uneven",
            "Tension: steel; compression: concrete",
            "Bend: steel on the stretched face",
            "Torsion: tubes, triangles; rust: zinc beats paint",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Revising the Design Process, Costing and the Tender
        self.next_band(2)
        self.write_rows(2, "Revising the Design Process, Costing and the Tender", [
            "Investigate, brief, specs, constraints",
            "Two ideas, scorecard, drawing, flow chart",
            "Model, check, photos; tender in order",
            "Cost: drawing x sources, round up, +10 +10",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Top view above the front''",
            "``Steel in the middle of the slab''",
            "``Specification without a number''",
            "``Budget rounded down, no contingency''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Three Views and Five Lines
        self.next_band(4)
        self.write_rows(4, "Three Views and Five Lines", [
            "Five lines",
            "Scale and sizes",
            "Three views, first angle",
            "Circle becomes dashes",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Push, Pull, Still, Moving, Rust
        self.next_band(5)
        self.write_rows(5, "Push, Pull, Still, Moving, Rust", [
            "Still, moving, spread, bunched",
            "Pull, push, bend, twist",
            "Heavy, hard, stiff, snap, dent",
            "Iron, air, water; cap the tubes",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): The Term in One Page
        self.next_band(6)
        self.write_rows(6, "The Term in One Page", [
            "Five stages, in order",
            "Numbers in the specs",
            "Round up, add ten twice",
            "Write, check, fix in colour",
        ], scale=0.9, box=3)

        last = Tex("Drawing conventions, forces and materials, and the design process with its costing and tender: Term 1 on one page, written from memory and corrected.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
