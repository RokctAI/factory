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

# Band-layout whiteboard scene for what-affects-the-rate-of-dissolving (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (200/120/180/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class WhatAffectsTheRateOfDissolvingSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Hot and Cold
        self.write_rows(0, "Hot and Cold", [
            "Rate of dissolving: how fast",
            "Hot water: faster",
            "Particles move faster",
            "Adults pour hot water",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Stirring and Shaking
        self.next_band(1)
        self.write_rows(1, "Stirring and Shaking", [
            "Stirring or shaking: faster",
            "Sugary water moved away",
            "Fresh water reaches the grains",
            "Shake the bottle",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Big Lumps and Fine Grains
        self.next_band(2)
        self.write_rows(2, "Big Lumps and Fine Grains", [
            "Small pieces: faster",
            "More surface touches water",
            "Cube, sugar, icing sugar",
            "Fair test: change one thing",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Stirring makes more dissolve in total''",
            "``Lumps and powder dissolve equally fast''",
            "``Hot water makes sugar melt''",
            "``Change two things in a test''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Hotter Is Faster
        self.next_band(4)
        self.write_rows(4, "Hotter Is Faster", [
            "Hotter is faster",
            "Hot tea",
            "Fast particles",
            "Quick to dissolve",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Stir It Up
        self.next_band(5)
        self.write_rows(5, "Stir It Up", [
            "Stir it up",
            "Stir",
            "Shake",
            "Fresh water",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Small Is Quick
        self.next_band(6)
        self.write_rows(6, "Small Is Quick", [
            "Small is quick",
            "Big lump: slow",
            "Fine grains: fast",
            "More surface",
        ], scale=0.9, box=3)

        last = Tex("A solid dissolves faster in a hotter solvent, when it is stirred or shaken, and when it is in smaller pieces.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
