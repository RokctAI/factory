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

# Band-layout whiteboard scene for drawing-the-stairs-and-ramp-plan-to-scale (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/190/160/120/110/90 of 860 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DrawingTheStairsAndRampPlanToScaleSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): From Brief to Drawing: Choosing Views and Scale
        self.write_rows(0, "From Brief to Drawing: Choosing Views and Scale", [
            "Three views; side shows most",
            "10 m long, 1.5 m high: 1:50 fits A4",
            "Riser 150 = 3; tread 250 = 5",
            "Convert once in a table",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Setting Out the Front View and Projecting the Plan
        self.next_band(1)
        self.write_rows(1, "Setting Out the Front View and Projecting the Plan", [
            "Front: stairs rectangle, lines at 3, 6, 9",
            "Ramp: plain face; rails 18 up",
            "Plan below: treads 5, ramp 144, landing 24",
            "Check 144 x 50 = 7 200 = 12 x 600",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): The Side View, Hidden Detail and Dimensions
        self.next_band(2)
        self.write_rows(2, "The Side View, Hidden Detail and Dimensions", [
            "Side view right: sawtooth of four steps",
            "Ramp behind: dashed slope",
            "Dimensions real, once: 4 at 150; 7 200; 900",
            "Title block: 1:50, symbol, mm",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``144 written instead of 7 200''",
            "``Landing forgotten at the door''",
            "``Hidden ramp drawn dark''",
            "``Ramp length does not match 1 in 12''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Which Views and What Scale
        self.next_band(4)
        self.write_rows(4, "Which Views and What Scale", [
            "Front, plan, side",
            "1:50 on A4",
            "Table: divide by 50",
            "Scale in the title block",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Steps Across, Then Down to the Plan
        self.next_band(5)
        self.write_rows(5, "Steps Across, Then Down to the Plan", [
            "Rectangle with three lines",
            "Feint lines straight down",
            "Four treads, long ramp, landing",
            "1 in 12 checks out",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): The Side View and the Sizes
        self.next_band(6)
        self.write_rows(6, "The Side View and the Sizes", [
            "Project across, side on the right",
            "Dashed ramp behind the stairs",
            "Real sizes once each",
            "Title block last",
        ], scale=0.9, box=2)

        last = Tex("Views and scale, front view, plan below, side view across, dashed hidden ramp, real-size dimensions once, title block: a drawing a builder can use.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
