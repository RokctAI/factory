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

# Band-layout whiteboard scene for the-hydraulic-press-and-its-calculations (Part 1 Expert
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


class TheHydraulicPressAndItsCalculationsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Hydraulic Press Is and What It Does
        self.write_rows(0, "What a Hydraulic Press Is and What It Does", [
            "Small pump cylinder, large ram, oil between",
            "Same pressure: big area, big force",
            "2 cm2 in, 50 cm2 out: 200 N becomes 5 000 N",
            "Bearings, plate, bales, bricks, car panels",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): The Press Equation: Force Over Area Both Sides
        self.next_band(1)
        self.write_rows(1, "The Press Equation: Force Over Area Both Sides", [
            "F1 / A1 = F2 / A2",
            "F2 = F1 x A2 / A1; F1 = F2 x A1 / A2",
            "Newtons; same area units",
            "Mass x 10 = weight in newtons",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Worked Calculations and Checking the Answer
        self.next_band(2)
        self.write_rows(2, "Worked Calculations and Checking the Answer", [
            "150 N on 4; ram 100: 3 750 N",
            "12 000 N on 60; pump 3: 600 N",
            "Pressure 150/4 = 37.5 N/cm2 both sides",
            "Check: big area, big force",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Large area with the small force''",
            "``Kilograms used as newtons''",
            "``cm2 one side, m2 the other''",
            "``No sense check''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Machine That Squashes
        self.next_band(4)
        self.write_rows(4, "A Machine That Squashes", [
            "Squashes, bends, pushes",
            "Oil for seals, rust, frost",
            "Jack upside down",
            "Push small, press big",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Same Pressure, Two Areas
        self.next_band(5)
        self.write_rows(5, "Same Pressure, Two Areas", [
            "Same pressure, two areas",
            "Multiply by the ratio for the big force",
            "Divide for the small force",
            "Kilograms times ten",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Three Steps Every Time
        self.next_band(6)
        self.write_rows(6, "Three Steps Every Time", [
            "Write, substitute, rearrange",
            "3 750 and 600",
            "Big area, big force",
            "Catch the flipped ratio",
        ], scale=0.9, box=2)

        last = Tex("A press shares one pressure between a small effort cylinder and a large ram, so force over area is equal both sides and the load is the effort times the area ratio.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
