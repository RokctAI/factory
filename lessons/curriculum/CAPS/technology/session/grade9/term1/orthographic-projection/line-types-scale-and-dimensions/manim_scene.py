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

# Band-layout whiteboard scene for line-types-scale-and-dimensions (Part 1 Expert
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


class LineTypesScaleAndDimensionsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Five Line Types and What Each One Says
        self.write_rows(0, "Five Line Types and What Each One Says", [
            "Dark continuous: visible edges",
            "Feint: construction and projection",
            "Dashed: hidden detail",
            "Wavy: break; chain: centre or cut",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Scale: Fitting a Building on a Page
        self.next_band(1)
        self.write_rows(1, "Scale: Fitting a Building on a Page", [
            "1:50 means 1 mm = 50 mm",
            "7 200 / 50 = 144; 150 / 50 = 3",
            "Standard scales only; largest that fits",
            "Write the scale in the title block",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Dimensioning Rules That Make a Drawing Buildable
        self.next_band(2)
        self.write_rows(2, "Dimensioning Rules That Make a Drawing Buildable", [
            "Extension, dimension line, arrows, number",
            "Outside the outline; once each",
            "Overall sizes furthest out",
            "Real sizes in mm, no unit written",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``mm after every number''",
            "``Dimension the scaled size''",
            "``Dimension in the hidden view''",
            "``Extension line touches the object''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Dark, Feint, Dashed, Wavy, Chain
        self.next_band(4)
        self.write_rows(4, "Dark, Feint, Dashed, Wavy, Chain", [
            "Dark: see it",
            "Feint: helpers",
            "Dashed: hidden",
            "Wavy: break; chain: centre",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Shrinking the Ramp onto Paper
        self.next_band(5)
        self.write_rows(5, "Shrinking the Ramp onto Paper", [
            "Divide by 50 to draw",
            "Multiply by 50 to read",
            "Pick the biggest that fits",
            "Title block states the scale",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Putting the Sizes On
        self.next_band(6)
        self.write_rows(6, "Putting the Sizes On", [
            "Real sizes, no unit",
            "Once, outside, clearest view",
            "Number above the line",
            "Builder needs no ruler",
        ], scale=0.9, box=0)

        last = Tex("Five line types, a standard scale written in the title block, and real-size dimensions given once: a drawing a builder can build from.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
