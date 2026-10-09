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

# Band-layout whiteboard scene for force-transfer-between-equal-syringes (Part 1 Expert
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


class ForceTransferBetweenEqualSyringesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Two Syringes, a Tube and a Push
        self.write_rows(0, "Two Syringes, a Tube and a Push", [
            "Master in, slave out: sealed system",
            "Fluid carries the push round corners",
            "Equal syringes: same distance, same force",
            "Transfer, not multiplication",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Pneumatic Versus Hydraulic: Air or Water in the Tube
        self.next_band(1)
        self.write_rows(1, "Pneumatic Versus Hydraulic: Air or Water in the Tube", [
            "Air = pneumatic; liquid = hydraulic",
            "Gas compresses: spongy, springs back",
            "Liquid does not: solid, immediate",
            "Brakes and jacks vs air tools and doors",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Investigating Force Transfer Fairly
        self.next_band(2)
        self.write_rows(2, "Investigating Force Transfer Fairly", [
            "Change one thing: air then water",
            "Measure distance and force; same masses",
            "Fill under water, no bubbles",
            "Slave force slightly less: friction",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Bubbles left in the water''",
            "``Fluid and mass changed together''",
            "``Different master distances''",
            "``Expecting exactly equal force''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Push One End, the Other End Moves
        self.next_band(4)
        self.write_rows(4, "Push One End, the Other End Moves", [
            "Push one, the other comes out",
            "The push goes down the tube",
            "Same size: same distance, same force",
            "Round corners to brakes",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Spongy Air, Solid Water
        self.next_band(5)
        self.write_rows(5, "Spongy Air, Solid Water", [
            "Air: spongy, springs back",
            "Water: solid, instant",
            "Gas squashes, liquid does not",
            "Drips vs hisses",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Doing the Test Properly
        self.next_band(6)
        self.write_rows(6, "Doing the Test Properly", [
            "One change at a time",
            "20 mm; 100, 200, 500 g",
            "No bubbles",
            "Write the table",
        ], scale=0.9, box=2)

        last = Tex("Two equal syringes transfer a push unchanged through a tube; air makes it pneumatic and spongy, water makes it hydraulic and solid, and a fair test shows both.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
