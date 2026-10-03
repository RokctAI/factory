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

# Band-layout whiteboard scene for labour-and-fair-employment (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (270/160/210/180/150/150/150 of 1270 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LabourAndFairEmploymentSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.78, box=None):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=YELLOW)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, "Labour and skill levels", [
            "Labour: effort for wages and salaries",
            "Unskilled: dishwasher, cleaner",
            "Semi-skilled: waiter, driver",
            "Skilled: chef, electrician, nurse",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "The role of workers", [
            "Produce, serve customers, care for equipment",
            "Duties: on time, honest, safe, respectful",
            "Productivity: output per worker per hour",
            "Trade unions: collective bargaining",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Fair employment laws", [
            "BCEA: 45 hours, overtime x 1,5, leave",
            "Minimum wage: R28,79 an hour (2025)",
            "LRA and CCMA; EEA: no unfair discrimination",
            "OHSA safety; UIF 1\\% + 1\\%",
        ], box=1)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Wages and payslips", [
            "45 x R28,79 = R1 295,55",
            "45 x R40 + 5 x R60 = R2 100",
            "Gross R5 000 - UIF R50 = R4 950",
            "Payslip: rate, hours, deductions, net pay",
        ], box=1)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Fair employment is good business", [
            "Fair recruitment, pay and treatment",
            "Training and safe conditions",
            "Motivated workers stay and produce more",
            "Unfair practices cost more later",
        ], box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Everyone in the restaurant", [
            "Dishwasher: unskilled",
            "Waiters: semi-skilled",
            "Chef and bookkeeper: skilled",
            "Training moves workers up",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "The rules on the wall", [
            "45 ordinary hours; overtime x 1,5",
            "Minimum wage R28,79 an hour",
            "Leave, payslip, UIF",
            "No discrimination; fair hearing; CCMA",
        ], box=1)

        self.wait(4)
