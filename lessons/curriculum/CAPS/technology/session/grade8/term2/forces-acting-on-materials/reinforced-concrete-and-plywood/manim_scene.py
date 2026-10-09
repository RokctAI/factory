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

# Band-layout whiteboard scene for reinforced-concrete-and-plywood (Part 1 Expert
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


class AdaptedMaterialsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Why Materials Are Adapted: Composites
        self.write_rows(0, "Why Materials Are Adapted: Composites", [
            "Composite: each covers the other's weakness",
            "Place each material where its force acts",
            "Straw in mud, horn and sinew, wattle and daub",
            "Which force acts here?",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Reinforced Concrete: Steel Where the Tension Is
        self.next_band(1)
        self.write_rows(1, "Reinforced Concrete: Steel Where the Tension Is", [
            "Concrete: compression yes, tension one tenth",
            "Bars near the bottom; near the top over columns",
            "Stirrups take shear",
            "Ribs, equal expansion, rust protection",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Plywood: Grain Crossed Against Grain
        self.next_band(2)
        self.write_rows(2, "Plywood: Grain Crossed Against Grain", [
            "Veneers crossed at right angles",
            "Odd number: faces match",
            "Strong both ways, no splitting, stays flat",
            "Glue is the weak spot; marine outdoors",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Steel at the neutral axis''",
            "``Steel carries the compression''",
            "``All plywood grain the same way''",
            "``Interior plywood where it gets wet''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Two Weak Things Make One Strong Thing
        self.next_band(4)
        self.write_rows(4, "Two Weak Things Make One Strong Thing", [
            "Every material hates one force",
            "Two weak things, one strong thing",
            "Straw in the brick",
            "Which force, how does it break?",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Steel Bars in the Right Place
        self.next_band(5)
        self.write_rows(5, "Steel Bars in the Right Place", [
            "Concrete squashes, steel pulls",
            "Bottom of a beam, top over a column",
            "Ribs grip; heat together; no rust",
            "Cover keeps the steel safe",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Sheets Glued Crosswise
        self.next_band(6)
        self.write_rows(6, "Sheets Glued Crosswise", [
            "Peel, cross, glue, odd number",
            "Split stops at the next layer",
            "Stays flat",
            "Drill before screwing near edges",
        ], scale=0.9, box=1)

        last = Tex("Put each material where the force it resists best will act: steel where concrete would be pulled, crossed grain where wood would split.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
