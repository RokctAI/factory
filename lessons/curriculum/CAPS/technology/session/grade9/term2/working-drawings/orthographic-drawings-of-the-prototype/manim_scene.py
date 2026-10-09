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

# Band-layout whiteboard scene for orthographic-drawings-of-the-prototype (Part 1 Expert
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


class OrthographicDrawingsOfThePrototypeSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From Sketch to Working Drawing: Why Three Views Are Needed
        self.write_rows(0, "From Sketch to Working Drawing: Why Three Views Are Needed", [
            "Sketch: idea; working drawing: every size",
            "Orthographic: square-on, flat, measurable",
            "First angle: front, top below, left side right",
            "Symbol in the title block",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Drawing the Lifting Machine in First Angle Projection
        self.next_band(1)
        self.write_rows(1, "Drawing the Lifting Machine in First Angle Projection", [
            "Title block: title, scale, date, name, sheet, symbol",
            "1:10 -> 1200 becomes 120 on paper",
            "Faint lines, project down and across, 45 degree line",
            "Hidden dashed; centre long-short",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Dimensions, Scale, Hidden Detail and the Parts List
        self.next_band(2)
        self.write_rows(2, "Dimensions, Scale, Hidden Detail and the Parts List", [
            "Dimensions: true size, once, clearest view",
            "Overalls outside, details inside, diameter symbol",
            "Parts list: no., name, qty, material, size; balloons",
            "Check: aligned, scaled, sized, dashed, buildable",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Top view above the front with a first angle symbol''",
            "``Paper sizes written as dimensions''",
            "``Same length dimensioned in two views''",
            "``Hidden edges drawn solid''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Three Flat Pictures of One Machine
        self.next_band(4)
        self.write_rows(4, "Three Flat Pictures of One Machine", [
            "Three flat pictures",
            "Front: uprights, beam, winch, platform, rope",
            "Top: squares, beam, platform depth",
            "Side: depth, drum, thickness",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Front, Top, Side, in Their Places
        self.next_band(5)
        self.write_rows(5, "Front, Top, Side, in Their Places", [
            "Front, top below, side right",
            "Faint first, then dark outlines",
            "Dashed for hidden",
            "Centre lines on round parts",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Numbers on the Lines
        self.next_band(6)
        self.write_rows(6, "Numbers on the Lines", [
            "Write 1200, not 120",
            "Each size once",
            "Parts list is the shopping list",
            "Could a stranger build it?",
        ], scale=0.9, box=3)

        last = Tex("A first angle working drawing places front, top and side views square-on to scale, with hidden detail dashed, true dimensions once each, and a parts list.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
