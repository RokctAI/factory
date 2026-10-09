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

# Band-layout whiteboard scene for building-the-model-crane-with-crank-and-pulley (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/250/210/100/100/100 of 930 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BuildingTheModelCraneSession(MovingCameraScene):
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
        self.wait(60)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Base, mast and arm
        self.write_rows(0, "Base, mast and arm", [
            "Double card base, pressed flat",
            "Mast: tight tube or braced lattice",
            "Push the top: no sway",
            "Arm: stiff first, light second",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Winch, pulley, assembly
        self.next_band(1)
        self.write_rows(1, "Winch, pulley, assembly", [
            "Reel on skewer, handle at 75 mm",
            "Cheeks, bead, stop peg",
            "Bead pulley with cheeks at the tip",
            "Mast, arm, winch, string, cells at back",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): The whole-crane test
        self.next_band(2)
        self.write_rows(2, "The whole-crane test", [
            "Mixed pile; bin 200 mm away",
            "Lift 150; swing; release; stand",
            "Three runs recorded",
            "Fix one thing, retest",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Flat card mast or arm''",
            "``Drum off to one side''",
            "``Cells taped to the mast''",
            "``Never tested with mixed metals''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Build the frame
        self.next_band(4)
        self.write_rows(4, "Build the frame", [
            "Chart open, base first",
            "Roll 350 mm round a pencil",
            "Diagonal on every face",
            "Winch while glue dries",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Winch, pulley, put it together
        self.next_band(5)
        self.write_rows(5, "Winch, pulley, put it together", [
            "Reel, handle, cheeks, bead, peg",
            "Spin the bead: free",
            "String up, along, over, magnet on",
            "Press: light on",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Test the whole crane
        self.next_band(6)
        self.write_rows(6, "Test the whole crane", [
            "Steel only? Base down? Light out?",
            "Tie, cells back, peg, groove",
            "Trim, label, tick",
            "Note what ran late",
        ], scale=0.9, box=0)

        last = Tex("Built to the drawing in the chart's order, stiffened and triangulated, string straight from drum to grooved pulley, and tested three times against every specification.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
