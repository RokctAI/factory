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

# Band-layout whiteboard scene for describing-and-comparing-fractions-in-diagrams (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/160/160/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DescribingAndComparingFractionsInDiagramsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Fraction Is
        self.write_rows(0, "What a Fraction Is", [
            "A fraction is part of a whole",
            "Equal parts only",
            "Bottom number: how many equal parts",
            "Top number: how many we take",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Reading and Drawing Fractions in Diagrams
        self.next_band(1)
        self.write_rows(1, "Reading and Drawing Fractions in Diagrams", [
            "Count all parts: bottom number",
            "Count shaded parts: top number",
            "3/8 eaten, 5/8 left",
            "8/8 is one whole",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Comparing Fractions in Diagrams
        self.next_band(2)
        self.write_rows(2, "Comparing Fractions in Diagrams", [
            "More parts, smaller parts",
            "1/2 is bigger than 1/4",
            "3/4 reaches past 2/3",
            "Same size wholes only",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``4 unequal pieces are quarters''",
            "``1/8 is bigger than 1/2''",
            "``3 of 8 shaded is 3/5''",
            "``Different size wholes are fine''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Equal Parts
        self.next_band(4)
        self.write_rows(4, "Equal Parts", [
            "Cut into equal parts",
            "4 equal slices: quarters",
            "Bottom: parts in the whole",
            "Top: parts we take",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Shade and Name
        self.next_band(5)
        self.write_rows(5, "Shade and Name", [
            "All parts: bottom number",
            "Shaded parts: top number",
            "Shaded plus unshaded is one whole",
            "4/4 is one whole",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Look and Compare
        self.next_band(6)
        self.write_rows(6, "Look and Compare", [
            "More parts, smaller parts",
            "Halves bigger than quarters",
            "3/4 is bigger than 2/3",
            "Same size wholes",
        ], scale=0.9, box=2)

        last = Tex("Equal parts first: the bottom counts the parts, the top counts what we take, and more parts means smaller parts.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
