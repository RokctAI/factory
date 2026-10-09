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

# Band-layout whiteboard scene for drawing-gear-systems-with-templates (Part 1 Expert
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


class DrawingGearSystemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Conventions for Drawing Gears
        self.write_rows(0, "Conventions for Drawing Gears", [
            "Pitch circle, centre cross, 40T beside it",
            "Scale: 1 mm per tooth",
            "Arrows for direction; driver and driven labelled",
            "Concentric circles for one shaft",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Drawing Counter-Rotation and an Idler Train
        self.next_band(1)
        self.write_rows(1, "Drawing Counter-Rotation and an Idler Train", [
            "Centre distance = sum of radii",
            "20T + 40T: 30 mm apart, circles kiss",
            "20-12-20 idler: 16 and 16",
            "Arrows flip at every mesh",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Drawing Faster and Slower Driven Gears
        self.next_band(2)
        self.write_rows(2, "Drawing Faster and Slower Driven Gears", [
            "12T drives 48T: 4:1, MA 4",
            "48T drives 12T: 1:4, MA 0.25",
            "Second stage: 12T inside the 48T",
            "Scale and layout fit the frame",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Every tooth drawn''",
            "``Circles overlap or gap''",
            "``Arrows not alternating''",
            "``Ratio without naming the driver''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Circles That Stand for Gears
        self.next_band(4)
        self.write_rows(4, "Circles That Stand for Gears", [
            "Circles, not teeth",
            "Size from the tooth count",
            "Kiss at one point",
            "Write VR, MA, which drives",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Two Gears, Then Three
        self.next_band(5)
        self.write_rows(5, "Two Gears, Then Three", [
            "Two radii added",
            "Light lines first",
            "Add the arrows: flip, flip, flip",
            "Idler fills the gap",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Small to Big, Big to Small
        self.next_band(6)
        self.write_rows(6, "Small to Big, Big to Small", [
            "Small to big: slow and strong",
            "Big to small: fast and weak",
            "Same circles, swapped driver",
            "Fold the train to fit the frame",
        ], scale=0.9, box=1)

        last = Tex("A gear is a pitch circle with a tooth count; circles kiss at the sum of their radii, arrows flip at each mesh, and the ratio is written with its driver.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
