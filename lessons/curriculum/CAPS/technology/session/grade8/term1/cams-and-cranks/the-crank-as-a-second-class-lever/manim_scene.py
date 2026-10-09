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

# Band-layout whiteboard scene for the-crank-as-a-second-class-lever (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/180/160/120/110/90 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CrankSecondClassLeverSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Crank Is
        self.write_rows(0, "What a Crank Is", [
            "Arm at right angles to an axle, handle at the end",
            "Pedals, reel, winder, mincer",
            "Hand keeps turning continuously",
            "PAT input: a comfortable crank",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): The Crank as a Second-Class Lever
        self.next_band(1)
        self.write_rows(1, "The Crank as a Second-Class Lever", [
            "Pivot: axle centre; effort: handle",
            "Load: axle surface, in between",
            "Second class: MA always above 1",
            "MA = arm length over axle radius",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Crank, Connecting Rod and Slider
        self.next_band(2)
        self.write_rows(2, "Crank, Connecting Rod and Slider", [
            "Crank, connecting rod, slider in a guide",
            "One turn: one stroke of twice the arm",
            "Works both ways: pump or engine",
            "Cam: one way, shape sets the motion",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A crank is first class because it turns''",
            "``A longer arm gives more speed''",
            "``The crank only converts hand to rotary''",
            "``The stroke equals the rod length''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Handle on an Axle
        self.next_band(4)
        self.write_rows(4, "A Handle on an Axle", [
            "Handle on an arm on an axle",
            "Turn the handle, the axle turns",
            "Pedal, reel, sharpener, winder",
            "Your PAT handle",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Why a Long Handle Helps
        self.next_band(5)
        self.write_rows(5, "Why a Long Handle Helps", [
            "Load in the middle, like a wheelbarrow",
            "Pivot centre, hand on handle, load at axle",
            "Always makes you stronger",
            "Longer arm, easier turn",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Making Round Into Back-and-Forth
        self.next_band(6)
        self.write_rows(6, "Making Round Into Back-and-Forth", [
            "Add a rod and a slider",
            "Round and round to back and forth",
            "Engine: back and forth to round",
            "Stroke is twice the arm",
        ], scale=0.9, box=1)

        last = Tex("A crank is a second-class lever bent into a circle; with a rod and slider it converts rotary and reciprocating motion either way.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
