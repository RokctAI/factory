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

# Band-layout whiteboard scene for unequal-syringes-force-multiplication-and-division (Part 1 Expert
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


class UnequalSyringesForceMultiplicationAndDivisionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Small Master, Large Slave: Multiplying Force
        self.write_rows(0, "Small Master, Large Slave: Multiplying Force", [
            "Small master, large slave: force UP",
            "Pressure x larger area = larger force",
            "Ratio of areas, about 2.5 for 5 and 20",
            "Distance DOWN: 20 in, 8 out",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Large Master, Small Slave: Multiplying Distance
        self.next_band(1)
        self.write_rows(1, "Large Master, Small Slave: Multiplying Distance", [
            "Large master, small slave: distance UP",
            "Low pressure x small area = small force",
            "MA below 1",
            "Same system, opposite ends; like a pivot",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Measuring the Trade-Off Between Force and Distance
        self.next_band(2)
        self.write_rows(2, "Measuring the Trade-Off Between Force and Distance", [
            "Measure: 20 mm push; 200, 500, 1 000 g",
            "Swap and repeat",
            "Force x distance same both ends",
            "Friction trims the ideal ratio",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The big syringe is simply stronger''",
            "``More force AND more distance''",
            "``Volume ratio used as area ratio''",
            "``Friction ignored''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Push Small, Lift Big
        self.next_band(4)
        self.write_rows(4, "Push Small, Lift Big", [
            "Finger lifts half a kilo",
            "Big face, big force",
            "Short move",
            "Pump the jack many times",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Push Big, Move Far
        self.next_band(5)
        self.write_rows(5, "Push Big, Move Far", [
            "Small plunger flies out",
            "Little force",
            "Big face wins force, loses distance",
            "Choose the master, choose the gain",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): You Cannot Have Both
        self.next_band(6)
        self.write_rows(6, "You Cannot Have Both", [
            "No bubbles, same pushes",
            "About 2.5 and about 0.4",
            "Multiply one, divide the other",
            "Measure diameters, not millilitres",
        ], scale=0.9, box=2)

        last = Tex("Unequal syringes trade force for distance by the ratio of their areas: small master multiplies force, large master multiplies distance, and force times distance stays the same.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
