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

# Band-layout whiteboard scene for what-makes-an-entrepreneur (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-5). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (200/180/180/140/110 of 810 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WhatMakesAnEntrepreneurSession(MovingCameraScene):
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
        self.write_rows(0, "What is an entrepreneur?", [
            "Spots a need or opportunity",
            "Has an idea to meet it",
            "Takes a risk to start a business",
            "Combines land, labour and capital",
        ], box=2)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Characteristics", [
            "Creative and innovative",
            "Willing to take calculated risks",
            "Determined, hard-working, resilient",
            "Responsible, honest, self-confident",
        ], box=1)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Entrepreneurial skills", [
            "Financial: budgets, records, pricing",
            "Communication and negotiation",
            "Planning, organising, time management",
            "Problem-solving, marketing, people skills",
        ], box=0)


        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Kagiso spots a gap", [
            "Problem: no stationery shop near school",
            "Idea: sell pens and exercise books",
            "Risk: R300 of his savings",
            "Result: profit and a happy class",
        ], box=0)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Kagiso's toolkit", [
            "Characteristics: brave, honest, determined",
            "Skills: pricing, records, selling",
            "Characteristics = who you are",
            "Skills = what you can learn",
        ], box=3)

        self.wait(4)
