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

# Band-layout whiteboard scene for connections-short-circuits-and-symbols (Part 1 Expert
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


class CircuitSymbolsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Correct Connections: Complete Paths and Polarity
        self.write_rows(0, "Correct Connections: Complete Paths and Polarity", [
            "Complete loop or nothing",
            "Cell button is plus; LED long leg is anode",
            "Battery: plus to minus so volts add",
            "Resistor in series with the LED",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Short Circuits: What They Are and Why They Are Dangerous
        self.next_band(1)
        self.write_rows(1, "Short Circuits: What They Are and Why They Are Dangerous", [
            "Near-zero path bypasses parts",
            "Current as big as the supply allows",
            "Bypassed lamp goes out; lead warms",
            "Fuse melts; breaker trips; earth-leakage saves people",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Accepted Component Symbols and Reading a Circuit Diagram
        self.next_band(2)
        self.write_rows(2, "Accepted Component Symbols and Reading a Circuit Diagram", [
            "Long-short lines, circle-cross, box, gap",
            "Triangle with bar and arrows, pointing with current",
            "Dots at joins; ruler; plus left; switch open",
            "Trace the loop; hunt for shortcuts",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``LED backwards''",
            "``Lead across a component''",
            "``Free-hand diagram with odd symbols''",
            "``Switch in a branch, rest left live''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Making the Loop
        self.next_band(4)
        self.write_rows(4, "Making the Loop", [
            "Finger round the loop",
            "Clips on metal, screws tight",
            "Right way round: cell, LED, buzzer",
            "Switch anywhere in one loop",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): The Shortcut That Burns
        self.next_band(5)
        self.write_rows(5, "The Shortcut That Burns", [
            "Shortcut, not through the parts",
            "Hot wire, drained cell, fire",
            "Easiest path takes nearly all",
            "One lead at a time, switch open",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): A Language of Lines
        self.next_band(6)
        self.write_rows(6, "A Language of Lines", [
            "Symbols show connections, not looks",
            "Label 3 V, 330 ohms",
            "Second lamp in parallel: a branch",
            "Panic button handed in as a diagram",
        ], scale=0.9, box=0)

        last = Tex("Make the loop complete and the polarity right, never let a wire bypass a part, and draw it in standard symbols on a ruled rectangle so anyone can read and check it.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
