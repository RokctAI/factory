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

# Band-layout whiteboard scene for energy-transfer-input-and-output (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/140/170/110/110/110 of 800 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class EnergyTransferInputAndOutputSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From a Source to Where It Is Needed
        self.write_rows(0, "From a Source to Where It Is Needed", [
            "Source: where energy comes from",
            "Sun to Earth",
            "Power station to home by wires",
            "Battery to bulb, food to muscles",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Input and Output Energy
        self.next_band(1)
        self.write_rows(1, "Input and Output Energy", [
            "Input energy goes in",
            "Kettle: electricity in, heat out",
            "Radio: sound out, torch: light out",
            "Windpump: wind in, pumping out",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Useful and Wasted Output
        self.next_band(2)
        self.write_rows(2, "Useful and Wasted Output", [
            "Useful output: what we want",
            "Wasted output: heat and sound",
            "Wasted energy spreads out",
            "Switch off to save energy",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A kettle's input is heat''",
            "``All input becomes useful''",
            "``Wasted energy disappears''",
            "``A bicycle needs no input''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Energy on the Move
        self.next_band(4)
        self.write_rows(4, "Energy on the Move", [
            "Energy on the move",
            "From a source",
            "Along wires",
            "To where it is needed",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): In and Out
        self.next_band(5)
        self.write_rows(5, "In and Out", [
            "In and out",
            "Kettle: heat out",
            "Radio: sound out",
            "Torch: light out",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Not All Useful
        self.next_band(6)
        self.write_rows(6, "Not All Useful", [
            "Not all useful",
            "Heat wasted",
            "Sound wasted",
            "Switch it off",
        ], scale=0.9, box=3)

        last = Tex("Energy travels from a source to a machine, which changes input energy into useful output energy, with some always wasted.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
