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

# Band-layout whiteboard scene for plotting-readings-and-finding-the-relationship (Part 1 Expert
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


class PlottingReadingsAndFindingTheRelationshipSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Setting Up the Graph: Axes, Scales and Plotting the Points
        self.write_rows(0, "Setting Up the Graph: Axes, Scales and Plotting the Points", [
            "V vertical, I horizontal: gradient = R",
            "Label axes with quantity and unit",
            "Even scales from zero, points fill the page",
            "Plot means as small crosses; check vs table",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): The Line of Best Fit and What a Straight Line Through the Origin Means
        self.next_band(1)
        self.write_rows(1, "The Line of Best Fit and What a Straight Line Through the Origin Means", [
            "Best fit: one ruler line, close to all, through origin",
            "Not dot-to-dot",
            "Straight through origin = direct proportionality",
            "Lamp curves; diode offset; resistor straight",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Finding Resistance From the Gradient and Writing the Conclusion
        self.next_band(2)
        self.write_rows(2, "Finding Resistance From the Gradient and Writing the Conclusion", [
            "Gradient = rise / run = 4.4 V / 0.044 A = 100 ohms",
            "Convert mA to A or get kilohms",
            "Compare: 100 ohms, 5\\%: 95 to 105 agrees",
            "Conclusion: relationship, resistance, limitations",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Dots joined in a zigzag''",
            "``Uneven scale or not from zero''",
            "``Gradient from two close data points''",
            "``Perfect line claimed despite scatter''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Dots on Squared Paper
        self.next_band(4)
        self.write_rows(4, "Dots on Squared Paper", [
            "Volts up, amps across",
            "Units on both",
            "Start at zero, even steps",
            "Neat crosses",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): A Straight Line Through Zero
        self.next_band(5)
        self.write_rows(5, "A Straight Line Through Zero", [
            "Ruler through zero",
            "Never join the dots",
            "Straight means proportional",
            "Honest about scatter",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Rise Over Run Is the Resistance
        self.next_band(6)
        self.write_rows(6, "Rise Over Run Is the Resistance", [
            "Two far points, divide",
            "100 volts per amp",
            "Matches the bands",
            "Three sentences",
        ], scale=0.9, box=1)

        last = Tex("Voltage against current for a resistor is a straight line through the origin; its gradient is the resistance, and the conclusion states both.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
