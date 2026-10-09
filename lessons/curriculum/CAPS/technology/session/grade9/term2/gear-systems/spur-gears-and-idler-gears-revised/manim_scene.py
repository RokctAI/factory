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

# Band-layout whiteboard scene for spur-gears-and-idler-gears-revised (Part 1 Expert
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


class SpurGearsAndIdlerGearsRevisedSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Spur Gears Revisited: Teeth, Meshing and Direction
        self.write_rows(0, "Spur Gears Revisited: Teeth, Meshing and Direction", [
            "Straight teeth, parallel axles, interlocking",
            "Meshing gears turn opposite ways",
            "Driver and driven; same tooth size",
            "No slip; mills, drills, gearboxes",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Gear Ratio, Speed and Force in Equal and Unequal Gears
        self.next_band(1)
        self.write_rows(1, "Gear Ratio, Speed and Force in Equal and Unequal Gears", [
            "Ratio = driven teeth / driver teeth",
            "10 -> 30: 3:1, slower, 3x turning force",
            "30 -> 10: 1:3, faster, 1/3 force",
            "Speed and force trade",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Idler Gears and Compound Trains
        self.next_band(2)
        self.write_rows(2, "Idler Gears and Compound Trains", [
            "Idler: direction back, ratio unchanged",
            "Idler teeth cancel",
            "Reverse gear, mill, bridging a gap",
            "Compound: ratios multiply",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Ratio written driver over driven''",
            "``Idler thought to change the ratio''",
            "``Speed and force both expected to rise''",
            "``Meshing gears drawn turning the same way''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Toothed Wheels That Push Each Other
        self.next_band(4)
        self.write_rows(4, "Toothed Wheels That Push Each Other", [
            "Teeth push teeth",
            "Opposite ways, always",
            "Driver turns driven",
            "Never slips",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Count the Teeth
        self.next_band(5)
        self.write_rows(5, "Count the Teeth", [
            "Count and divide",
            "Big driven: slow and strong",
            "Small driven: fast and weak",
            "Never both",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): The Middle Gear Changes Nothing but Direction
        self.next_band(6)
        self.write_rows(6, "The Middle Gear Changes Nothing but Direction", [
            "Middle gear flips direction",
            "Changes nothing else",
            "Reverse gear",
            "Two on a shaft: multiply",
        ], scale=0.9, box=0)

        last = Tex("Meshing spur gears turn opposite ways with ratio driven over driver, trading speed for force; an idler restores direction and leaves the ratio alone.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
