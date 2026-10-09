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

# Band-layout whiteboard scene for gases-compress-liquids-do-not (Part 1 Expert
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


class GasesCompressLiquidsDoNotSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Particles Far Apart, Particles Touching
        self.write_rows(0, "Particles Far Apart, Particles Touching", [
            "Gas: particles far apart, empty space",
            "Liquid: particles touching, sliding",
            "Push a gas: space closes; push a liquid: nothing to close",
            "Blocked air syringe moves; blocked water does not",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): What Compressibility Does Inside a System
        self.next_band(1)
        self.write_rows(1, "What Compressibility Does Inside a System", [
            "Stores energy: a spring; burst hose whips",
            "Delays: squash first, then move; no exact position",
            "Cushions: gives under load; liquid holds rigid",
            "Air in brakes = spongy pedal; bleed them",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Choosing Air or Liquid for the Job
        self.next_band(2)
        self.write_rows(2, "Choosing Air or Liquid for the Job", [
            "Hydraulic: large, exact, rigid; brakes, jacks, arms",
            "Pneumatic: fast, light, soft; tools, doors, tyres",
            "Drawbacks: leaks vs imprecision and stored energy",
            "Trucks use both",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Liquids are stronger than gases''",
            "``Pneumatics always weaker''",
            "``Stored energy ignored''",
            "``Air used where exact position is needed''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Why Air Squashes and Water Does Not
        self.next_band(4)
        self.write_rows(4, "Why Air Squashes and Water Does Not", [
            "Far apart vs touching",
            "Space to use up vs none",
            "Squashes vs will not budge",
            "Pump and fizzy drink",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): The Spring Hidden in Every Bubble
        self.next_band(5)
        self.write_rows(5, "The Spring Hidden in Every Bubble", [
            "Spring in every bubble",
            "Lag before the move",
            "Pillow, not rod",
            "Bleed the brakes",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Which Fluid for Which Machine
        self.next_band(6)
        self.write_rows(6, "Which Fluid for Which Machine", [
            "Liquid for big exact force",
            "Air for fast soft action",
            "Both in one truck",
            "Respect compressed air",
        ], scale=0.9, box=0)

        last = Tex("Far-apart gas particles compress and store energy; touching liquid particles do not, so hydraulics give exact rigid force and pneumatics give fast soft action.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
