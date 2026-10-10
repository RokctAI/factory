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

# Band-layout whiteboard scene for multiplying-decimal-fractions-by-10-and-100 (Part 1 Expert
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


class MultiplyingDecimalFractionsBy10And100Session(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Multiplying Decimals by 10
        self.write_rows(0, "Multiplying Decimals by 10", [
            "Times 10: one place left",
            "4,75 times 10 = 47,5",
            "3,08 times 10 = 30,8",
            "0,35 m times 10 = 3,5 m",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Multiplying Decimals by 100
        self.next_band(1)
        self.write_rows(1, "Multiplying Decimals by 100", [
            "Times 100: two places left",
            "4,75 times 100 = 475",
            "2,4 times 100 = 240",
            "0,07 times 100 = 7",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Using ×10 and ×100 in Measurement and Money
        self.next_band(2)
        self.write_rows(2, "Using ×10 and ×100 in Measurement and Money", [
            "R1 = 100 cents",
            "R3,60 = 360 cents",
            "2,45 m = 245 cm",
            "12,5 cm = 125 mm",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``4,75 times 10 = 4,750''",
            "``2,4 times 100 = 2,400''",
            "``0,35 times 100 = 3,5''",
            "``R3,60 = 36 cents''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): Times 10
        self.next_band(4)
        self.write_rows(4, "Times 10", [
            "Times 10",
            "Each digit moves one place left",
            "Ten times bigger",
            "R4,75 to R47,50",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Times 100
        self.next_band(5)
        self.write_rows(5, "Times 100", [
            "Times 100",
            "Two places left",
            "Zeros fill gaps",
            "2,4 to 240",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Rand, Cents and Centimetres
        self.next_band(6)
        self.write_rows(6, "Rand, Cents and Centimetres", [
            "Rand to cents: times 100",
            "Metres to cm: times 100",
            "Cm to mm: times 10",
            "Small units, big number",
        ], scale=0.9, box=2)

        last = Tex("Times 10 moves every digit one place left; times 100 moves every digit two places left.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
