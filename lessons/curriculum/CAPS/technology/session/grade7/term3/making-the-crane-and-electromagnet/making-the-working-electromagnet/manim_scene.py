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

# Band-layout whiteboard scene for making-the-working-electromagnet (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/200/220/100/100/100 of 890 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MakingTheWorkingElectromagnetSession(MovingCameraScene):
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
        self.wait(50)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Core and coil
        self.write_rows(0, "Core and coil", [
            "Core must let go: test on a magnet",
            "Tape the head and point",
            "100 tight turns, one direction",
            "Strip ends bright; record variables",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Wiring from the diagram
        self.next_band(1)
        self.write_rows(1, "Wiring from the diagram", [
            "Cell, switch, coil, bulb: one loop",
            "Switch last; press; bulb lights",
            "One break stops the whole loop",
            "Never coil straight across a cell",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Testing to specification
        self.next_band(2)
        self.write_rows(2, "Testing to specification", [
            "Ten clips up, none left in one second",
            "Three trials, average",
            "Change one variable at a time",
            "Verdict, then the string loop",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Second layer wound backwards''",
            "``Clips gripping insulation''",
            "``One test written as proof''",
            "``Switch held for a minute''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Wind the coil
        self.next_band(4)
        self.write_rows(4, "Wind the coil", [
            "Nail that lets go",
            "Hand-length free, tight turns",
            "Fifty down, fifty back, same way",
            "Copper shining at both ends",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Wire it up
        self.next_band(5)
        self.write_rows(5, "Wire it up", [
            "Lay out like the diagram",
            "Light on means coil on",
            "No light? Walk the loop",
            "Ten seconds at a time",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Test it properly
        self.next_band(6)
        self.write_rows(6, "Test it properly", [
            "Dip, lift, count, release, count",
            "Three times",
            "Weak? One change, retest",
            "Write the verdict",
        ], scale=0.9, box=1)

        last = Tex("A coil of 100 turns on a soft core, wired as drawn with switch and indicator, tested three times against ten clips and one-second release, and recorded.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
