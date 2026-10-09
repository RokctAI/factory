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

# Band-layout whiteboard scene for building-the-working-scale-model (Part 1 Expert
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


class BuildingTheHeadgearModelSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Safe Working Practices for the Headgear Build
        self.write_rows(0, "Safe Working Practices for the Headgear Build", [
            "Saw in a hook; drill clamped; knife along the rule",
            "Hot glue at its station; PVA for tower joints",
            "Floor not chair; one hand on the switch",
            "Record from the first cut",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Building the Structure True: Base, Faces, Tower, Back-Leg
        self.next_band(1)
        self.write_rows(1, "Building the Structure True: Base, Faces, Tower, Back-Leg", [
            "Base square with a try square",
            "Faces flat, every rectangle triangulated",
            "Stand, hold, glue, plumb before locking",
            "Back-leg cut to measured fit; sheave free",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Installing the Winder and Testing the Lift
        self.next_band(2)
        self.write_rows(2, "Installing the Winder and Testing the Lift", [
            "Gear plate square to the rope path",
            "Train free by hand; collars on shafts",
            "Free, direction, 100-400 g, brake, sway, topple",
            "Fix in order; before and after values",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Tower glued before checked square''",
            "``Drum skewed to the rope''",
            "``Shafts without collars''",
            "``Tests without numbers''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Knives, Saws and Hot Glue, Safely
        self.next_band(4)
        self.write_rows(4, "Knives, Saws and Hot Glue, Safely", [
            "Fingers behind the blade",
            "Cold water for hot glue",
            "Nobody under the cage",
            "Count the tools back",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Square, Plumb and Braced
        self.next_band(5)
        self.write_rows(5, "Square, Plumb and Braced", [
            "Crooked base, crooked tower",
            "A diagonal in every rectangle",
            "Check plumb from two sides",
            "Gussets at the back-leg ends",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Does It Lift? Measure It
        self.next_band(6)
        self.write_rows(6, "Does It Lift? Measure It", [
            "Wrong way? Swap the leads",
            "Seconds per metre at each load",
            "Millimetres of sway",
            "Stalled: batteries, friction, drum, path, ratio",
        ], scale=0.9, box=3)

        last = Tex("Build safely, make the base square, the faces braced and the tower plumb, align the winder to the rope, then test with numbers and record every fix.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
