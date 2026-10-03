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

# Band-layout whiteboard scene for management-tasks-polc (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (230/220/200/160/210/100/130 of 1250 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ManagementTasksPolcSession(MovingCameraScene):
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
        self.write_rows(0, "The four tasks", [
            "Planning: goals and how",
            "Organising: people and resources",
            "Leading: instruct and motivate",
            "Control: check and correct",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Planning", [
            "Analyse, set goals, choose, detail",
            "SMART goals",
            "Strategic, tactical, operational plans",
            "R12 600 / R35 = 360 deliveries",
        ], box=1)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Organising", [
            "Divide work into tasks",
            "Assign people and resources",
            "Delegation",
            "Authority, responsibility, accountability",
        ], box=3)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Leading", [
            "Clear instructions",
            "Two-way communication",
            "Motivation",
            "Resolve conflict, set an example",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Control", [
            "Set standards",
            "Measure: 320 deliveries",
            "Compare: 320 / 400 = 80\\%",
            "Correct: advertise, staff the phone",
        ], box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "A road trip called POLC", [
            "Plan the route",
            "Organise the car",
            "Lead the passengers",
            "Control: check the map",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "The delivery van, step by step", [
            "Month 1: 320 x R35 = R11 200",
            "R1 400 short of costs",
            "Month 3: 450 x R35 = R15 750",
            "R3 150 above costs",
        ], box=3)

        self.wait(4)
