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

# Band-layout whiteboard scene for characteristics-of-good-management (Part 1 Expert
# subtopics 1-6, Part 2 Simplifier subtopics 7-8). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (280/150/170/150/150/130/110/120 of 1260 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CharacteristicsOfGoodManagementSession(MovingCameraScene):
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
        self.write_rows(0, "Qualities of a good manager", [
            "Integrity and fairness",
            "Clear two-way communication",
            "Sound decisions",
            "Motivates and develops people",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Management skills", [
            "Technical: knowing the work",
            "Human: working with people",
            "Conceptual: the big picture",
            "Higher level: more conceptual",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Leadership styles", [
            "Autocratic: tells",
            "Democratic: asks, then decides",
            "Laissez-faire: lets go",
            "Fit the style to the situation",
        ], box=3)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Decision-making steps", [
            "Define the problem; gather facts",
            "List and weigh options",
            "Choose and implement",
            "Evaluate the result",
        ], box=0)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Ethics and responsibility", [
            "Right, not just legal",
            "Employment Equity Act",
            "Health and safety",
            "Trust pays off",
        ], box=0)

        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Results show management", [
            "Productivity and quality",
            "Turnover: 1 / 8 = 12.5\\%",
            "Turnover: 4 / 8 = 50\\%",
            "Read the measures together",
        ], box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Two supervisors", [
            "A: greets, explains, thanks",
            "B: shouts, favourites, blames",
            "Team A lost 1 of 8",
            "Team B lost 4 of 8",
        ], box=3)

        # --- Band 7 (subtopic_8)
        self.next_band(7)
        self.write_rows(7, "A checklist", [
            "Vision, honesty, fairness",
            "Listens and praises",
            "Right style for the moment",
            "Results prove it",
        ], box=3)

        self.wait(4)
