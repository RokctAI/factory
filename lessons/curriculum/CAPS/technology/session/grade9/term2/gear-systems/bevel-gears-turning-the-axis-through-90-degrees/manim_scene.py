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

# Band-layout whiteboard scene for bevel-gears-turning-the-axis-through-90-degrees (Part 1 Expert
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


class BevelGearsTurningTheAxisThrough90DegreesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Bevel Gears: Cone-Shaped Teeth That Meet at a Right Angle
        self.write_rows(0, "Bevel Gears: Cone-Shaped Teeth That Meet at a Right Angle", [
            "Teeth on cones; cones meet point to point",
            "Shafts at an angle, usually 90 degrees",
            "Mitre gears equal; pinion and crown unequal",
            "Turns motion to where it is needed",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Equal and Unequal Bevel Gears: Ratio, Speed and Force
        self.next_band(1)
        self.write_rows(1, "Equal and Unequal Bevel Gears: Ratio, Speed and Force", [
            "Ratio = driven / driver, unchanged",
            "20:20 -> 1:1, corner only",
            "10 -> 40: 4:1 slower, 4x force (axle)",
            "40 -> 10: 1:4 faster, 1/4 force (drill)",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Where Bevel Gears Are Used and How to Draw Them
        self.next_band(2)
        self.write_rows(2, "Where Bevel Gears Are Used and How to Draw Them", [
            "Drill, eggbeater, differential, grinder, windmill",
            "Sketch: cones, right-angle shafts, arrows, teeth",
            "Label counts, ratio, angle",
            "Guard the teeth; costlier than spur",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Bevel gears drawn with parallel shafts''",
            "``New ratio rule invented for the angle''",
            "``Teeth drawn equal width along the cone''",
            "``Bevel pair assumed always 1:1''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Gears on Cones
        self.next_band(4)
        self.write_rows(4, "Gears on Cones", [
            "Gears on cones",
            "Point to point, right angle",
            "Wide outside, narrow inside",
            "Handle one way, beaters another",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Turning the Corner
        self.next_band(5)
        self.write_rows(5, "Turning the Corner", [
            "Same arithmetic",
            "Equal: just turn the corner",
            "Small to big: strong and slow",
            "Big to small: fast and weak",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Same Rules, New Angle
        self.next_band(6)
        self.write_rows(6, "Same Rules, New Angle", [
            "Drill, beater, bakkie, windmill",
            "Two cones in a sketch",
            "Ratio written beside",
            "Fingers away from teeth",
        ], scale=0.9, box=0)

        last = Tex("Bevel gears put teeth on cones so meshing shafts meet at 90 degrees; ratio, speed and force follow the spur gear rules unchanged.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
