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

# Band-layout whiteboard scene for shear-torsion-and-forces-on-members (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/150/120/110/90 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ShearTorsionForcesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Four Forces on a Member
        self.write_rows(0, "Four Forces on a Member", [
            "Tension along outward; compression along inward",
            "Shear across, opposite either side of a plane",
            "Torsion around the axis, opposite ends",
            "Snap, crush, slice, twist off",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Shear and Torsion in Real Structures
        self.next_band(1)
        self.write_rows(1, "Shear and Torsion in Real Structures", [
            "Shear in bolts, nails, pins, beam ends",
            "Torsion in shafts and off-centre loads",
            "Tubes resist twist; thick paired bolts resist shear",
            "Shear walls in earthquakes",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Identifying Forces on a Drawing
        self.next_band(2)
        self.write_rows(2, "Identifying Forces on a Drawing", [
            "Four arrow symbols",
            "Find the loads, follow them into the member",
            "Carport: posts C, cable T, bolts S, beam torsion",
            "Say how your member resists it",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Shear arrows run along the member''",
            "``Torsion only happens in machines''",
            "``A bending beam has one force only''",
            "``Name the member, not the force''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Pull, Push, Slice, Twist
        self.next_band(4)
        self.write_rows(4, "Pull, Push, Slice, Twist", [
            "Pull a rope: tension",
            "Push a brick: compression",
            "Scissors: shear",
            "Wring a cloth: torsion",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Where Slicing and Twisting Happen
        self.next_band(5)
        self.write_rows(5, "Where Slicing and Twisting Happen", [
            "Bolts and nails get sliced",
            "Anything that spins gets twisted",
            "Tubes beat rods for twisting",
            "Carport base bolts: shear",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Reading the Arrows
        self.next_band(6)
        self.write_rows(6, "Reading the Arrows", [
            "Out, in, sideways, curved",
            "Follow the load into the bar",
            "Posts, cable, bolts, beam",
            "String for pull, dowel for push",
        ], scale=0.9, box=0)

        last = Tex("Tension pulls, compression pushes, shear slices, torsion twists: four arrows name every force on a member.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
