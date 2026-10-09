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

# Band-layout whiteboard scene for distance-force-trade-off-in-different-cylinders (Part 1 Expert
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


class DistanceForceTradeOffInDifferentCylindersSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Equal Volumes Moved: The Rule That Fixes Distance
        self.write_rows(0, "Equal Volumes Moved: The Rule That Fixes Distance", [
            "Liquid does not compress: volume conserved",
            "Area x distance (master) = area x distance (slave)",
            "2 cm2 x 10 cm = 20 cm3; / 10 cm2 = 2 cm",
            "Distance ratio = inverse of area ratio",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Working Out Extension from Areas
        self.next_band(1)
        self.write_rows(1, "Working Out Extension from Areas", [
            "Method: volume moved, then divide by slave area",
            "4 x 15 = 60; / 12 = 5 cm; swap: 15 cm",
            "Diameters: area = pi r2; ratio squared",
            "Same units; sense check",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Mechanical Advantage Above and Below 1
        self.next_band(2)
        self.write_rows(2, "Mechanical Advantage Above and Below 1", [
            "Force ratio = area ratio (Pascal)",
            "Force x distance equal both ends",
            "MA = slave area / master area",
            "Above 1 strong-slow; below 1 fast-weak; 1 equal",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Large slave moves as far as master''",
            "``Diameter ratio used as area ratio''",
            "``Units mixed''",
            "``MA above 1 with no distance loss''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The Same Water Has to Fit Somewhere
        self.next_band(4)
        self.write_rows(4, "The Same Water Has to Fit Somewhere", [
            "Water has to fit somewhere",
            "Five times area, a fifth of the move",
            "Narrow: long column; wide: short slab",
            "Pump the jack again and again",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Divide by the Area
        self.next_band(5)
        self.write_rows(5, "Divide by the Area", [
            "Area times distance, divide",
            "60 / 12 = 5",
            "Double diameter = four times area",
            "Bigger slave, smaller move",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Strong and Slow, or Fast and Weak
        self.next_band(6)
        self.write_rows(6, "Strong and Slow, or Fast and Weak", [
            "Force up, distance down, same ratio",
            "No free gain",
            "MA = big over small",
            "Choose the ratio, pay in distance",
        ], scale=0.9, box=1)

        last = Tex("Equal volumes fix the distance, Pascal fixes the force, their product stays constant, and mechanical advantage above or below 1 is bought with distance.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
