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

# Band-layout whiteboard scene for lever-mechanical-advantage-by-ratios (Part 1 Expert
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


class LeverMechanicalAdvantageSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Mechanical Advantage as a Ratio of Forces
        self.write_rows(0, "Mechanical Advantage as a Ratio of Forces", [
            "MA = load / effort, no unit",
            "Above one: force; below one: distance",
            "MA 6: effort moves six times further",
            "Measured below ideal: friction",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Mechanical Advantage from the Arms of a Lever
        self.next_band(1)
        self.write_rows(1, "Mechanical Advantage from the Arms of a Lever", [
            "Arms from the fulcrum",
            "MA = effort arm / load arm",
            "1.2 / 0.2 = 6, same as forces",
            "Second class above one; third below",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Worked Examples: Crowbar, Wheelbarrow, Brake Lever
        self.next_band(2)
        self.write_rows(2, "Worked Examples: Crowbar, Wheelbarrow, Brake Lever", [
            "Crowbar 6; actual 5.5",
            "Barrow 3; load over the wheel",
            "Brake lever 4; pliers 5",
            "Broom one third: speed",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Ratio inverted''",
            "``Arms not from the fulcrum''",
            "``Mixed units on the arms''",
            "``Friction never mentioned''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): How Many Times Easier
        self.next_band(4)
        self.write_rows(4, "How Many Times Easier", [
            "How many times easier",
            "Newtons over newtons",
            "Easier or faster, not both",
            "Hand swings far, slab rises little",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Long Arm, Small Effort
        self.next_band(5)
        self.write_rows(5, "Long Arm, Small Effort", [
            "Long effort arm, small effort",
            "Fulcrum middle, load middle, effort middle",
            "Barrow and nutcracker: always easier",
            "Broom and forearm: always faster",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Numbers From Real Levers
        self.next_band(6)
        self.write_rows(6, "Numbers From Real Levers", [
            "600 over 100; 1.2 over 0.2",
            "133 newtons for the barrow",
            "30 newtons becomes 120 on the cable",
            "Same units on both arms",
        ], scale=0.9, box=0)

        last = Tex("Load over effort or effort arm over load arm give the same number; above one is easier, below one is faster, and friction takes its share.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
