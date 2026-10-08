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

# Band-layout whiteboard scene for load-effort-and-mechanical-advantage (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (210/160/170/110/110/110 of 870 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LoadEffortAndMechanicalAdvantageSession(MovingCameraScene):
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
        self.wait(44)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Load, effort and pivot
        self.write_rows(0, "Load, effort and pivot", [
            "Pivot: the fixed turning point",
            "Load: the force you must overcome",
            "Effort: the force you apply",
            "Effort arm and load arm: distances from the pivot",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Mechanical advantage
        self.next_band(1)
        self.write_rows(1, "Mechanical advantage", [
            "MA = load divided by effort",
            "800 N lifted by 100 N: MA = 8",
            "Longer effort arm than load arm: more help",
            "MA above 1, equal to 1, or below 1",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Nothing for nothing
        self.next_band(2)
        self.write_rows(2, "Nothing for nothing", [
            "Less force, more distance",
            "No machine creates energy",
            "Broom and bat: MA below 1 for speed",
            "Move the pivot, change the deal",
        ], scale=0.82, box=1)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The load is the push you make''",
            "``A longer bar always helps''",
            "``A lever gives you extra energy''",
            "``MA below 1 is a mistake''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Three words for every lever
        self.next_band(4)
        self.write_rows(4, "Three words for every lever", [
            "Pivot: the stone under the bar",
            "Load: the boulder",
            "Effort: the worker's push",
            "Seesaw: pivot in the middle",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): How much stronger
        self.next_band(5)
        self.write_rows(5, "How much stronger", [
            "800 divided by 100 = 8 times stronger",
            "Push far from the pivot",
            "Long spanner beats short",
            "Above 1 helps, 1 only turns, below 1 for speed",
        ], scale=0.85, box=1)

        # --- Band 6 (subtopic_6): You pay with distance
        self.next_band(6)
        self.write_rows(6, "You pay with distance", [
            "Hands move 40 cm, rock rises 5 cm",
            "Force swapped for distance",
            "Stone nearer rock: easier push",
            "Pivot placed to suit the job",
        ], scale=0.9, box=1)

        last = Tex("A lever trades distance for force: far from the pivot, small effort, big load.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
