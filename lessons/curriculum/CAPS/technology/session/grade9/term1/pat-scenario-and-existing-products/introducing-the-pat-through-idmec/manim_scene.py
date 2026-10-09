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

# Band-layout whiteboard scene for introducing-the-pat-through-idmec (Part 1 Expert
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


class IntroducingThePatThroughIdmecSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Problem Situation: An Entrance That Shuts People Out
        self.write_rows(0, "The Problem Situation: An Entrance That Shuts People Out", [
            "Raised floor, improvised step",
            "Wheelchair user shut out",
            "Team = building firm; tender = offer + price",
            "Access is a right",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): IDMEC as the Map for the Whole Term
        self.next_band(1)
        self.write_rows(1, "IDMEC as the Map for the Whole Term", [
            "Investigate wks 1-4: 15 marks",
            "Design wks 5-6: 20; Make wks 7-8: 35",
            "Evaluate inside and after",
            "Communicate wk 10: tender board",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Investigating the Site and Possible Structures
        self.next_band(2)
        self.write_rows(2, "Investigating the Site and Possible Structures", [
            "Measure rise at several points",
            "Measure the space; note door and ground",
            "Ask the users, especially the wheelchair user",
            "List options; do not choose yet",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Rise measured once''",
            "``Space never measured''",
            "``Users never asked''",
            "``Solution chosen before investigating''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Door Nobody Can Reach
        self.next_band(4)
        self.write_rows(4, "A Door Nobody Can Reach", [
            "Hall floor 600 up",
            "Pile of blocks for a step",
            "Your firm makes a tender",
            "Every learner through the door",
        ], scale=0.9, box=3)

        # --- Band 5 (subtopic_5): Five Steps and Ten Weeks
        self.next_band(5)
        self.write_rows(5, "Five Steps and Ten Weeks", [
            "Investigate 15, Design 20, Make 35",
            "Evaluate while you design",
            "Communicate in week 10",
            "The file is what is marked",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Looking Hard Before Drawing
        self.next_band(6)
        self.write_rows(6, "Looking Hard Before Drawing", [
            "Tape measure: biggest rise",
            "How far can the ramp go?",
            "Ask the people",
            "List, with good and bad",
        ], scale=0.9, box=0)

        last = Tex("A raised door, a tender to fix it, IDMEC across ten weeks, and an investigation that measures, asks and lists before anyone chooses.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
