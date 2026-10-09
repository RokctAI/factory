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

# Band-layout whiteboard scene for resistor-colour-codes (Part 1 Expert
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


class ResistorColourCodesSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Resistor Does and How Its Value Is Marked
        self.write_rows(0, "What a Resistor Does and How Its Value Is Marked", [
            "Resistor limits current; value in ohms, k, M",
            "Large: printed 10R, 4k7; small: colour bands",
            "Symbol: rectangle + value",
            "Value on the diagram, not colour",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Reading the Three Value Bands
        self.next_band(1)
        self.write_rows(1, "Reading the Three Value Bands", [
            "Black 0 ... white 9",
            "Band 1 digit, band 2 digit, band 3 zeros",
            "Yellow violet brown = 470; red red red = 2k2",
            "330 = orange orange brown; 47k = yellow violet orange",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): The Tolerance Band, Checking With a Meter and Choosing Values
        self.next_band(2)
        self.write_rows(2, "The Tolerance Band, Checking With a Meter and Choosing Values", [
            "Band 4 tolerance: gold 5\\%, silver 10\\%, none 20\\%",
            "470 at 5\\%: 447 to 494",
            "Meter on ohms, loose, not in fingers",
            "Standard values: 10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Bands read from the gold end''",
            "``Third band taken as a digit''",
            "``Resistor measured while held in fingers''",
            "``Colour written on the diagram instead of a value''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Component That Slows the Current
        self.next_band(4)
        self.write_rows(4, "A Component That Slows the Current", [
            "Slows the current",
            "Ohms, thousands, millions",
            "Bands read from any angle",
            "Write 470",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Two Digits and a Number of Zeros
        self.next_band(5)
        self.write_rows(5, "Two Digits and a Number of Zeros", [
            "Make up your sentence",
            "Lone band to the right",
            "4, 7, one zero",
            "Backwards works too",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): How Close Is Close Enough
        self.next_band(6)
        self.write_rows(6, "How Close Is Close Enough", [
            "Gold is good enough for an LED",
            "Measure if unsure",
            "Round up for safety",
            "That is why 470, not 270",
        ], scale=0.9, box=3)

        last = Tex("Resistor bands read as two digits and a count of zeros, with a tolerance band set apart: yellow, violet, brown, gold is 470 ohms within 5 percent.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
