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

# Band-layout whiteboard scene for single-fixed-pulley (Part 1 Expert
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


class SingleFixedPulleySession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Fixed Pulley: A Wheel That Changes Direction
        self.write_rows(0, "The Fixed Pulley: A Wheel That Changes Direction", [
            "Grooved wheel, axle, block, rope",
            "Fixed to beam, pole or jib",
            "Changes the direction of the pull",
            "Wells, flagpoles, cranes, washing lines",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Why the Mechanical Advantage Is 1
        self.next_band(1)
        self.write_rows(1, "Why the Mechanical Advantage Is 1", [
            "10 N load, ~10 N effort: MA = 1",
            "Rope down 300, load up 300",
            "One rope, one tension: effort = load",
            "Work in = work out, minus friction",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Where Fixed Pulleys Earn Their Place
        self.next_band(2)
        self.write_rows(2, "Where Fixed Pulleys Earn Their Place", [
            "Pull down: body weight, strong muscles",
            "Stand safe; share the rope",
            "Feeds winches; tops a block and tackle",
            "Bracket carries twice the load",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Fixed pulley halves the effort''",
            "``Exactly equal readings expected''",
            "``Bracket rated for the load only''",
            "``Direction change is a small benefit''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Pull Down to Lift Up
        self.next_band(4)
        self.write_rows(4, "Pull Down to Lift Up", [
            "Wheel on a beam",
            "Pull down, load up",
            "Lean back, use your weight",
            "Still the same force",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): No Gain in Force, and Why That Is Fine
        self.next_band(5)
        self.write_rows(5, "No Gain in Force, and Why That Is Fine", [
            "Balance reads the load",
            "Same distance both ends",
            "One rope, one tension",
            "Cannot multiply",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Flagpoles, Wells and Washing Lines
        self.next_band(6)
        self.write_rows(6, "Flagpoles, Wells and Washing Lines", [
            "Direction and position",
            "Crane winch on the ground",
            "Top of the block and tackle",
            "Fixing takes double",
        ], scale=0.9, box=3)

        last = Tex("A single fixed pulley changes the direction of a pull with a mechanical advantage of 1, because one rope has one tension, and its bracket carries twice the load.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
