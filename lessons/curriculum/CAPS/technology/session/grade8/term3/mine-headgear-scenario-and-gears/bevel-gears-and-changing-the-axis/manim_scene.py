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

# Band-layout whiteboard scene for bevel-gears-and-changing-the-axis (Part 1 Expert
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


class BevelGearsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Bevel Gears: Teeth on a Cone
        self.write_rows(0, "Bevel Gears: Teeth on a Cone", [
            "Teeth on a cone, converging to the apex",
            "Apexes meet; shafts at 90 degrees",
            "Mitre gears: equal, direction only",
            "12 drives 36: VR 3, MA 3",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Turning the Axis Through 90 Degrees
        self.next_band(1)
        self.write_rows(1, "Turning the Axis Through 90 Degrees", [
            "Motor axis here, need there",
            "Hand drill: big wheel drives pinion, fast bit",
            "Car: pinion drives crown wheel, slow wheels",
            "Egg beater, grinder, wind pump",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Bevel Gears in Machines and in the Headgear
        self.next_band(2)
        self.write_rows(2, "Bevel Gears in Machines and in the Headgear", [
            "Winder main drive: parallel spur gears",
            "Bevels in right-angle drives and indicators",
            "Model: motor stands where there is room",
            "Apexes meet; collars against end thrust",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Spur gears forced at right angles''",
            "``Apexes not meeting''",
            "``End thrust ignored''",
            "``Bevels cannot change the ratio''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Gears Shaped Like Cones
        self.next_band(4)
        self.write_rows(4, "Gears Shaped Like Cones", [
            "Cones, not cylinders",
            "Tip to tip, round the corner",
            "Same tooth rule",
            "Arrows show direction on each shaft",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Round the Corner
        self.next_band(5)
        self.write_rows(5, "Round the Corner", [
            "Fast weak drill; slow strong axle",
            "Two pinions: beaters counter-rotate",
            "Vanes' shaft to pump rod",
            "Rotation here, needed there",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Hand Drill, Egg Beater, Winder
        self.next_band(6)
        self.write_rows(6, "Hand Drill, Egg Beater, Winder", [
            "Sheaves are pulleys, no gears",
            "Drum bevel bigger: free gear-down",
            "Shafts cross at exactly 90",
            "Bevels push apart; stop the shafts",
        ], scale=0.9, box=3)

        last = Tex("Teeth on cones, tips meeting, turn rotation through 90 degrees with the same ratio rules; fix the shafts so the pair stays in mesh.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
