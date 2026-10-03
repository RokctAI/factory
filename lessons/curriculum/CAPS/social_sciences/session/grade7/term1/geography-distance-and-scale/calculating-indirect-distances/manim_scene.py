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

# Band-layout whiteboard scene for calculating-indirect-distances (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/190/230/180/90/90/90 of 1060 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CalculatingIndirectDistancesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0: Indirect Distance
        self.write_rows(0, "Indirect Distance", [
            "Indirect: along roads, rails, rivers",
            "Always longer than the direct distance",
            "Sani Pass: hairpin bends",
            "Big difference: barrier or poor link",
        ], scale=0.86, box=1)
        # --- Band 1: Adding Straight Sections
        self.next_band(1)
        self.write_rows(1, "Adding Straight Sections", [
            "Mark the start, end and every turn",
            "Measure each straight section",
            "3.2 + 4.5 + 1.3 = 9 cm",
            "9 cm times 100 m = 900 m",
        ], scale=0.86, box=2)
        # --- Band 2: The String Method With a Line Scale
        self.next_band(2)
        self.write_rows(2, "The String Method With a Line Scale", [
            "Thin, non-stretchy string",
            "Fix the start; follow every bend",
            "Pinch at the end; straighten it",
            "Lay it on the line scale from zero",
        ], scale=0.86, box=1)
        # --- Band 3: Comparing Distances and the Error Museum
        self.next_band(3)
        self.write_rows(3, "Comparing Distances and the Error Museum", [
            "Indirect minus direct: the extra distance",
            "Rivers, rails and fences force detours",
            "Huguenot Tunnel: about 11 km saved",
            "Slipping string cuts corners: too short",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: The Real Way Round
        self.next_band(4)
        self.write_rows(4, "The Real Way Round", [
            "Bird: straight line",
            "You: the real way round",
            "Mountains make it much longer",
        ], scale=0.86, box=0)
        # --- Band 5: Corners and String
        self.next_band(5)
        self.write_rows(5, "Corners and String", [
            "Straight bits: measure, add, multiply",
            "Curves: thin string along every bend",
            "Pinch, straighten, read from zero",
        ], scale=0.86, box=0)
        # --- Band 6: Why the Way Round Matters
        self.next_band(6)
        self.write_rows(6, "Why the Way Round Matters", [
            "Straight line versus the real path",
            "Barriers: rivers, rails, fences",
            "Slipping string: answer too short",
        ], scale=0.86, box=0)
        self.wait(4)
