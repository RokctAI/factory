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

# Band-layout whiteboard scene for boreholes-and-wells (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/160/170/110/110/110 of 820 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BoreholesAndWellsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Water Under the Ground
        self.write_rows(0, "Water Under the Ground", [
            "Groundwater in cracks in rock",
            "Aquifer: like a sponge",
            "Water table: top of groundwater",
            "Dry areas depend on it",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Wells and Boreholes
        self.next_band(1)
        self.write_rows(1, "Wells and Boreholes", [
            "Well: wide, dug by hand",
            "Borehole: narrow, drilled, deep",
            "Hand pumps and windmills",
            "Solar pumps and tanks",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Benefits and Problems
        self.next_band(2)
        self.write_rows(2, "Benefits and Problems", [
            "Often clean, close to home",
            "Costly to drill and pump",
            "Too much pumping: runs dry",
            "Keep far from toilets",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Groundwater is an underground lake''",
            "``A borehole is the same as a well''",
            "``Groundwater never runs out''",
            "``Groundwater is always clean''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)


        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Hidden Water
        self.next_band(4)
        self.write_rows(4, "Hidden Water", [
            "Groundwater",
            "Aquifer",
            "Water table",
            "Dry areas",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Dig or Drill
        self.next_band(5)
        self.write_rows(5, "Dig or Drill", [
            "Well",
            "Borehole",
            "Hand pump",
            "Solar pump",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Good and Bad
        self.next_band(6)
        self.write_rows(6, "Good and Bad", [
            "Clean",
            "Close",
            "Costly",
            "Can run dry",
        ], scale=0.9, box=0)

        last = Tex("Wells and boreholes bring up water hidden in the rocks, and it must be protected and used carefully.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
