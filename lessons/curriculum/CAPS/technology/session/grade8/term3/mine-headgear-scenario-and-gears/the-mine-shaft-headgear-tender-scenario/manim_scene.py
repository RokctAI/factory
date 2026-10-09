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

# Band-layout whiteboard scene for the-mine-shaft-headgear-tender-scenario (Part 1 Expert
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


class HeadgearScenarioSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The Scenario: A Tender for a Mine Shaft Headgear
        self.write_rows(0, "The Scenario: A Tender for a Mine Shaft Headgear", [
            "Platinum mine, shaft 800 m to the reef",
            "Tender: design, model, budget, presentation",
            "Team = company; teacher = board",
            "Portfolio = the bid",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): What a Headgear Is and What It Must Do
        self.next_band(1)
        self.write_rows(1, "What a Headgear Is and What It Must Do", [
            "Drum, sheave, shaft, cage or skip",
            "Two conveyances in balance",
            "Structure: loads, no topple or buckle",
            "Mechanism: motor, gearbox, drum, brakes",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): The PAT Ahead: Gears, Structure, Tender
        self.next_band(2)
        self.write_rows(2, "The PAT Ahead: Gears, Structure, Tender", [
            "Weeks 1-3: gears and MA",
            "Weeks 4-6: research, brief, sketches, drawing",
            "Weeks 7-8: budget and model",
            "Week 9: tender board",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Headgear as tower only''",
            "``Headgear as mechanism only''",
            "``Budget and impact left to last week''",
            "``Claiming instead of showing''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A Tower Over a Hole in the Ground
        self.next_band(4)
        self.write_rows(4, "A Tower Over a Hole in the Ground", [
            "A tower over a hole",
            "Lifts people and rock",
            "Companies bid; board picks one",
            "Your bid is your portfolio",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Lifting People and Rock Safely
        self.next_band(5)
        self.write_rows(5, "Lifting People and Rock Safely", [
            "Rope: drum up, over, down",
            "Back-leg leans at the winder house",
            "Slow and strong through gears",
            "Inspect daily; lives depend on it",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): The Term's Journey in One Picture
        self.next_band(6)
        self.write_rows(6, "The Term's Journey in One Picture", [
            "Gears first",
            "Then design and impact report",
            "Then cost and build",
            "Then present and revise",
        ], scale=0.9, box=3)

        last = Tex("A mine needs a headgear; your company bids; the tower is a structure and a mechanism, and the term builds the bid week by week.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
