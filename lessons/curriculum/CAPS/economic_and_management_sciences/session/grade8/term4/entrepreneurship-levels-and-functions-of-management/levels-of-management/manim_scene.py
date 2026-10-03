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

# Band-layout whiteboard scene for levels-of-management (Part 1 Expert
# subtopics 1-6, Part 2 Simplifier subtopics 7-8). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (250/130/130/150/170/160/140/110 of 1240 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class LevelsOfManagementSession(MovingCameraScene):
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
        self.write_rows(0, "What management is", [
            "Getting work done through people",
            "Effective: reach the goal",
            "Efficient: no waste",
            "2 + 6 + 10 = 18 managers",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Top management", [
            "Owner, MD, general manager, board",
            "Vision, mission, long-term goals",
            "Strategic decisions",
            "Three to five years or more",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Middle management", [
            "Department heads",
            "Tactical decisions, about a year",
            "Departmental plans and budgets",
            "The link between levels",
        ], box=3)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Lower management", [
            "Supervisors and team leaders",
            "Operational decisions, day to day",
            "Technical and people skills",
            "Span of control",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Levels working together", [
            "Organisational chart",
            "Authority flows down",
            "Responsibility flows up",
            "Information flows both ways",
        ], box=3)

        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Other organisations", [
            "Company: board, CEO, regional, branch",
            "School: principal and SGB; HODs; grade heads",
            "Government: DG, directors, supervisors",
            "Same pattern everywhere",
        ], box=1)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "The supermarket's pyramid", [
            "Top: 2 people, five-year view",
            "Middle: 6 department managers",
            "Lower: 10 supervisors",
            "Plus 42 workers = 60 people",
        ], box=3)

        # --- Band 7 (subtopic_8)
        self.next_band(7)
        self.write_rows(7, "One idea, three levels", [
            "Top: yes, 400 deliveries a month",
            "Middle: plan orders and packing",
            "Lower: roster and checks",
            "How long, how wide?",
        ], box=3)

        self.wait(4)
