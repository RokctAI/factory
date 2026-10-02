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

# Band-layout whiteboard scene for mines-factories-and-child-labour (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (290/180/210/240/150/150/150 of 1370 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class MinesFactoriesAndChildLabourSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
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
            self.play(Create(SurroundingRectangle(made[box], color=box_color)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0: Work in the mills
        self.write_rows(0, "Work in the mills", [
            "12 to 14 hours, six days a week",
            "Heat, dust, noise, unguarded machines",
            "Fines for lateness; straps for sleepy children",
            "Piecers join threads; scavengers sweep under machines",
        ], scale=0.8, box=3)
        # --- Band 1: Work in the mines
        self.next_band(1)
        self.write_rows(1, "Work in the mines", [
            "Firedamp explosions, floods, roof falls",
            "Trappers: alone in the dark, opening doors",
            "Hurriers: dragging tubs; bearers: ladders",
            "Huskar Colliery 1838: 26 children drowned",
        ], scale=0.86, box=1)
        # --- Band 2: The campaign and the laws
        self.next_band(2)
        self.write_rows(2, "The campaign and the laws", [
            "Oastler 1830; Sadler 1832; Lord Ashley",
            "1833 Factory Act: no under-9s; inspectors",
            "1842 Mines Act: no women or boys under 10 underground",
            "1844 fenced machines; 1847 Ten Hours Act",
        ], scale=0.8, box=1)
        # --- Band 3: Evidence and legacy
        self.next_band(3)
        self.write_rows(3, "Evidence and legacy", [
            "Inquiry evidence: powerful but selected",
            "About 160 million children in child labour worldwide",
            "South Africa: Constitution protects children",
            "No employment under 15 in South Africa",
        ], scale=0.8, box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A day in the mill
        self.next_band(4)
        self.write_rows(4, "A day in the mill", [
            "Bell at six; fines for lateness",
            "Piecer: quick hands on snapping threads",
            "Scavenger: under the moving machine",
        ], scale=0.86)
        # --- Band 5: Down the pit
        self.next_band(5)
        self.write_rows(5, "Down the pit", [
            "Trapper: twelve hours in the dark",
            "Hurrier: crawling with a coal tub",
            "1842 drawings shocked Britain",
        ], scale=0.86, box=0)
        # --- Band 6: How the law changed
        self.next_band(6)
        self.write_rows(6, "How the law changed", [
            "1833: no children under nine in mills",
            "1842: no women or young boys underground",
            "1847: ten-hour day; 1880: school to age ten",
        ], scale=0.86, box=0)
        self.wait(4)
