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

# Band-layout whiteboard scene for circuit-diagram-3d-sketch-and-final-choice (Part 1 Expert
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


class CircuitDiagram3dSketchAndFinalChoiceSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Drawing the Circuit Diagram for Each Idea
        self.write_rows(0, "Drawing the Circuit Diagram for Each Idea", [
            "Standard symbols, straight wires, dots, + top left",
            "Every value and type; polarity correct",
            "A: float switch, 470, red LED, test button",
            "Trace: LED on when low? Else logic inverted",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): The 3D Sketch: What the Device Looks Like and Where the Circuit Lives
        self.next_band(1)
        self.write_rows(1, "The 3D Sketch: What the Device Looks Like and Where the Circuit Lives", [
            "Sketch: box on sill, LED and button on face",
            "Battery inside, wire out; sensor on tank",
            "Every diagram part has a place; sizes written",
            "Impression and materials note for presentation",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Comparing Ideas Against the Brief and Choosing as a Team
        self.next_band(2)
        self.write_rows(2, "Comparing Ideas Against the Brief and Choosing as a Team", [
            "Table: specs down, ideas across",
            "C sensor best; B output best; A simplest",
            "Combine: reed switch, flashing LED, series circuit",
            "Reasons by spec number; redraw clean; costs",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Circuit diagram without component values''",
            "``Sketch too small for the battery the diagram needs''",
            "``Idea chosen by argument, not the table''",
            "``LED drawn the wrong way round''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Symbols for the Insides
        self.next_band(4)
        self.write_rows(4, "Symbols for the Insides", [
            "Symbols for the insides",
            "Values on every part",
            "Right way round",
            "Lights when low",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): A Picture of the Outside
        self.next_band(5)
        self.write_rows(5, "A Picture of the Outside", [
            "A picture of the outside",
            "Where each part goes",
            "Fits the battery?",
            "A hand for scale",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Tick the List, Pick One
        self.next_band(6)
        self.write_rows(6, "Tick the List, Pick One", [
            "Tick, cross, note",
            "Best bits from each",
            "Write why",
            "Clean copy with parts and costs",
        ], scale=0.9, box=1)

        last = Tex("Each idea needs a valued, polarised circuit diagram and a matching 3D sketch; the team chooses by ticking every specification and combining the best parts.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
