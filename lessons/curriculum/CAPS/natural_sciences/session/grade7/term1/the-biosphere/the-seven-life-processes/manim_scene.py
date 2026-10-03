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

# Band-layout whiteboard scene for the-seven-life-processes (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/200/180/120/120/120 of 930 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TheSevenLifeProcessesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Food, energy and waste
        self.write_rows(0, "Food, energy and waste", [
            "Nutrition: producers make food; consumers eat it",
            "Respiration: energy released from food in every cell",
            "Excretion: removing wastes the cells made (CO2, urea)",
            "Egestion (faeces) is NOT excretion",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Growth, offspring, senses, motion
        self.next_band(1)
        self.write_rows(1, "Growth, offspring, senses, motion", [
            "Growth: permanent increase in size, new cells",
            "Reproduction: sexual (two parents) or asexual (one)",
            "Sensitivity: detect a stimulus and respond",
            "Movement: animals by muscles; plants by slow turning",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): The test for life
        self.next_band(2)
        self.write_rows(2, "The test for life", [
            "M R S G R E N: all seven processes",
            "All seven, by itself, and made of cells",
            "Car and fire: imitations, not life",
            "Living / once living / never living",
        ], scale=0.88, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Respiration means breathing''",
            "``Faeces are excretion''",
            "``Plants do not move or respond''",
            "``A fire is alive because it uses oxygen''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A goat does all seven
        self.next_band(4)
        self.write_rows(4, "A goat does all seven", [
            "Eats grass: nutrition",
            "Burns food in its cells: respiration",
            "Urine and CO2: excretion",
            "Grows, has kids, hears, walks",
        ], scale=0.88, box=1)

        # --- Band 5 (subtopic_5): Plants do it slowly
        self.next_band(5)
        self.write_rows(5, "Plants do it slowly", [
            "Makes food from sunlight; respires day and night",
            "Grows and makes seeds",
            "Bends to light; roots go down",
            "Sunflowers turn, tendrils curl",
        ], scale=0.82, box=2)

        # --- Band 6 (subtopic_6): Is it alive?
        self.next_band(6)
        self.write_rows(6, "Is it alive?", [
            "Car: moves and uses fuel, but no growth, no cells",
            "All seven, by itself, made of cells",
            "Shirt and table: once living",
            "Seed: alive but sleeping",
        ], scale=0.82, box=1)

        last = Tex("Seven processes, all at once: that is what it means to be alive.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
