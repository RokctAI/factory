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

# Band-layout whiteboard scene for traditional-and-modern-societies (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-5). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (200/230/240/160/140 of 970 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TraditionalAndModernSocietiesSession(MovingCameraScene):
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
        self.write_rows(0, "Life without money", [
            "No money: swap or make everything yourself",
            "Hard to save, hard to compare value",
            "Trade only with people nearby",
            "Money solves problems of exchange",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Traditional societies", [
            "Hunting, gathering, herding, farming",
            "Households largely self-sufficient",
            "Sharing within family and village",
            "Cattle as a store of wealth",
        ], box=1)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Modern societies", [
            "People specialise in one kind of work",
            "Earn an income in money",
            "Buy goods and services from others",
            "Everyone depends on everyone",
        ], box=3)


        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Gogo's village and your street", [
            "Gogo's village: grow, herd, build, share",
            "Your street: buy almost everything",
            "Village: few swaps, little money",
            "Street: many swaps, needs money",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "One morning with no money", [
            "Bread: what can I swap?",
            "Taxi: driver wants fuel, not pencils",
            "Value: how many pencils per loaf?",
            "Money makes every swap easy",
        ], box=3)

        self.wait(4)
