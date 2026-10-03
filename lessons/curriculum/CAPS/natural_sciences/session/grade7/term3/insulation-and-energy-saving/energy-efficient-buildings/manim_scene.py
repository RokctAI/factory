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

# Band-layout whiteboard scene for energy-efficient-buildings (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (130/140/170/120/120/120 of 800 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EnergyEfficientBuildingsSession(MovingCameraScene):
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Buildings gain and lose heat
        self.write_rows(0, "Buildings gain and lose heat", [
            "Roof: sun radiates in, metal conducts through",
            "Walls and windows conduct heat",
            "Gaps: draughts by convection",
            "Saving energy saves money and coal",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Conserving heat in buildings
        self.next_band(1)
        self.write_rows(1, "Conserving heat in buildings", [
            "Ceiling insulation and foil",
            "Thick walls, cavity walls, thermal mass",
            "North windows plus overhang (Southern Hemisphere)",
            "Light colours, sealed gaps, ventilation, trees",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Indigenous homes
        self.next_band(2)
        self.write_rows(2, "Indigenous homes", [
            "Rondavel: mud walls, thick thatch, round shape",
            "Beehive hut: dome of thatch",
            "Karoo corbelled houses: thick stone",
            "Nama matjieshuis: reed mats; Ndebele lime-wash",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Modern always means efficient''",
            "``Thatch is too thin to insulate''",
            "``Thermal mass makes heat''",
            "``Big windows facing south''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Where houses leak heat
        self.next_band(4)
        self.write_rows(4, "Where houses leak heat", [
            "Roof, walls, windows, floor, gaps",
            "Thin metal roof: hot summer, cold winter",
            "Gaps: draughts",
            "Saving energy saves coal and money",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Making houses comfy
        self.next_band(5)
        self.write_rows(5, "Making houses comfy", [
            "Ceiling plus insulation, seal the gaps",
            "Thick walls store heat",
            "North windows with an overhang",
            "Light roofs and shady trees",
        ], scale=0.88, box=2)

        # --- Band 6 (subtopic_6): Traditional homes
        self.next_band(6)
        self.write_rows(6, "Traditional homes", [
            "Thatch traps air; mud walls store heat",
            "Round shape: less wall, wind slides by",
            "Karoo stone domes",
            "Nama reed mats swell shut in rain",
        ], scale=0.88, box=1)

        last = Tex("Smart design and local materials keep homes comfortable with less energy.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
