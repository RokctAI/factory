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

# Band-layout whiteboard scene for terms-1-and-2-revision (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (200/150/180/110/110/110 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class Terms1And2RevisionSession(MovingCameraScene):
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
        self.wait(44)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Design process and the two briefs
        self.write_rows(0, "Design process and the two briefs", [
            "IDMEC as a loop, in both projects",
            "Brief; specifications test, constraints limit",
            "Eight considerations; analyse existing designs",
            "Group evaluation; impact listed both ways",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Levers and fluids
        self.next_band(1)
        self.write_rows(1, "Levers and fluids", [
            "MA = load over effort; distance is the price",
            "Middle: pivot 1st, load 2nd, effort 3rd",
            "Liquid firm and instant; air springy and late",
            "Bigger piston: more force, less move",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Structures, drawing, confusions
        self.next_band(2)
        self.write_rows(2, "Structures, drawing, confusions", [
            "Contain, protect, support, span; shell, frame, solid",
            "Stable: base and centre; strong vs rigid",
            "Tubes, folds, triangles; gussets, webs, bracing",
            "Dark, feint, dashed; working to make, oblique to show",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Judge a lever by its shape''",
            "``Horizontals stiffen a frame''",
            "``A tube is stronger than a sheet''",
            "``Benefits only in an evaluation''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Two projects, one method
        self.next_band(4)
        self.write_rows(4, "Two projects, one method", [
            "Five steps, round and round",
            "Brief, specifications, constraints",
            "Eight checks for fitness",
            "Who is it for, who pays",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Pushes made bigger
        self.next_band(5)
        self.write_rows(5, "Pushes made bigger", [
            "Load over effort",
            "What is in the middle",
            "Water firm, air soft",
            "Rule first, then apply",
        ], scale=0.95, box=1)

        # --- Band 6 (subtopic_6): Things that stand up
        self.next_band(6)
        self.write_rows(6, "Things that stand up", [
            "Shell, frame, solid",
            "Does not topple, break, or bend",
            "Tube, fold, triangle",
            "Know the pairs",
        ], scale=0.95, box=1)

        last = Tex("Two projects, one method: needs, briefs, forces managed by levers, fluids and triangles, drawn in one language.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
