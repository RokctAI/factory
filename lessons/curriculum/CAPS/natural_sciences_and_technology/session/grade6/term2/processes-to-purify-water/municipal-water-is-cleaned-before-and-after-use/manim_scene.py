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

# Band-layout whiteboard scene for municipal-water-is-cleaned-before-and-after-use (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (230/120/130/110/110/110 of 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MunicipalWaterIsCleanedBeforeAndAfterUseSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Cleaning Water Before We Use It
        self.write_rows(0, "Cleaning Water Before We Use It", [
            "Screens stop large objects",
            "Chemicals clump dirt into flocs",
            "Settling, then sand filters",
            "Chlorine kills germs",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Cleaning Water After We Use It
        self.next_band(1)
        self.write_rows(1, "Cleaning Water After We Use It", [
            "Wastewater flows through sewers",
            "Screens and grit channels",
            "Settling tanks: sludge",
            "Bacteria break down waste",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Why Both Matter
        self.next_band(2)
        self.write_rows(2, "Why Both Matter", [
            "Water is used again downstream",
            "Broken works: sewage in rivers",
            "Cleaning costs money",
            "Never flush wipes or fat",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Tap water comes straight from the river''",
            "``Chlorine is added for taste''",
            "``Sewage just disappears''",
            "``Wet wipes can be flushed''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Before the Tap
        self.next_band(4)
        self.write_rows(4, "Before the Tap", [
            "Before the tap",
            "Screen",
            "Settle and filter",
            "Chlorine",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): After the Drain
        self.next_band(5)
        self.write_rows(5, "After the Drain", [
            "After the drain",
            "Sewers",
            "Settling",
            "Bacteria",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Clean for the Next Town
        self.next_band(6)
        self.write_rows(6, "Clean for the Next Town", [
            "Clean for the next town",
            "Downstream",
            "Reused",
            "Protect the river",
        ], scale=0.9, box=1)

        last = Tex("Municipal water is cleaned before we use it and again after we use it, because the same water is used downstream.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
