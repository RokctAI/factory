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

# Band-layout whiteboard scene for plastics-around-the-home (Part 1 Expert
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


class PlasticsAroundTheHomeSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Case Study: A Room-by-Room Audit
        self.write_rows(0, "Case Study: A Room-by-Room Audit", [
            "Audit: item, plastic, property, lifespan",
            "Built-in: PVC pipes, conduit, uPVC frames",
            "Insulation, damp sheet, rotomoulded tank",
            "Cheaper, longer; fire trade-off with PVC, foam",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Kitchen, Bathroom and Services: Which Plastic and Why
        self.next_band(1)
        self.write_rows(1, "Kitchen, Bathroom and Services: Which Plastic and Why", [
            "Kitchen: PP kettle, ABS fridge liner, HDPE board",
            "PP microwave tubs; melamine not microwave",
            "Bath acrylic; PP seat; nylon bristles",
            "Chairs PP, TV ABS, foam mattress, PC lights",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Lifespan, Safety and What to Do With It After
        self.next_band(2)
        self.write_rows(2, "Lifespan, Safety and What to Do With It After", [
            "Built-in 40 yr; durable 2 to 20; packaging days",
            "Durable recyclable; packaging: reduce, reuse",
            "Safety: microwave PP only; sun; small parts",
            "Fire: toxic smoke; retardants; smoke alarm",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Food microwaved in polystyrene or melamine''",
            "``All household plastic treated as rubbish''",
            "``Plastic pipe assumed weaker and shorter-lived than steel''",
            "``Plastic item placed in sun or on a stove''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Count the Plastic in One Room
        self.next_band(4)
        self.write_rows(4, "Count the Plastic in One Room", [
            "Room by room",
            "Pipes and frames",
            "No rust, no paint",
            "Chlorine in fire",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): The Right Plastic in Each Room
        self.next_band(5)
        self.write_rows(5, "The Right Plastic in Each Room", [
            "Kettle, tubs, board",
            "Melamine takes heat not waves",
            "Bath, brush, bucket",
            "Chairs, TV, mattress",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Long Life, Short Life, Next Life
        self.next_band(6)
        self.write_rows(6, "Long Life, Short Life, Next Life", [
            "40 years, 10 years, 1 day",
            "Bucket worth recycling",
            "PP in the microwave",
            "Smoke alarm",
        ], scale=0.9, box=1)

        last = Tex("A home's plastics are chosen by property, from PVC pipes lasting forty years to PET bottles lasting a day, and each item raises the questions of right plastic, long enough life and a next life.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
