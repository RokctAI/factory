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

# Band-layout whiteboard scene for realistic-costs-of-materials-labour-and-transport (Part 1 Expert
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


class RealisticCostsOfMaterialsLabourAndTransportSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Three Parts of Every Building Cost
        self.write_rows(0, "Three Parts of Every Building Cost", [
            "Materials: fixed by the design",
            "Labour: skill x days",
            "Transport: distance x trips",
            "Plus 10\\% waste, 10\\% contingency",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Finding Real Prices and Measuring Real Quantities
        self.next_band(1)
        self.write_rows(1, "Finding Real Prices and Measuring Real Quantities", [
            "Prices: supplier, today, source and date",
            "Quantities: from the drawing",
            "7.2 x 1.2 x 0.3 = 2.6 m3",
            "1 m3 = 7 bags, 0.5 sand, 0.5 stone",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): A Worked Estimate for a Concrete Ramp
        self.next_band(2)
        self.write_rows(2, "A Worked Estimate for a Concrete Ramp", [
            "Table: item, qty, unit, price, total",
            "Materials + labour + transport",
            "Every figure traceable",
            "Compare designs and methods",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Prices from memory''",
            "``Quantities guessed''",
            "``Labour forgotten''",
            "``No waste or contingency''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Materials, People and Getting It There
        self.next_band(4)
        self.write_rows(4, "Materials, People and Getting It There", [
            "Materials, labour, transport",
            "Design, days, distance",
            "Extra for waste",
            "Extra for surprises",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Prices from the Shop, Quantities from the Drawing
        self.next_band(5)
        self.write_rows(5, "Prices from the Shop, Quantities from the Drawing", [
            "Ask the shop, write the date",
            "Measure the drawing",
            "Length x width x thickness",
            "23 bags for 3.3 m3",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Adding It Up for One Ramp
        self.next_band(6)
        self.write_rows(6, "Adding It Up for One Ramp", [
            "Item, how many, price, total",
            "Workers x days; deliveries",
            "Add 10\\% at the end",
            "Any line can be checked",
        ], scale=0.9, box=3)

        last = Tex("Materials, labour and transport, priced from suppliers and measured from the drawing, with waste and contingency: an estimate anyone can check.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
