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

# Band-layout whiteboard scene for term-3-revision-gears-mechanical-advantage-and-structures (Part 1 Expert
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


class Term3RevisionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Gear Systems Revisited: Direction, Ratio, Idlers and Bevels
        self.write_rows(0, "Gear Systems Revisited: Direction, Ratio, Idlers and Bevels", [
            "Counter-rotate; driven over driver teeth",
            "12 at 1 200 drives 36: ratio 3, 400 rpm",
            "Idler: direction only; stages multiply",
            "Bevels: cones, 90 degrees",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Mechanical Advantage Calculations for Levers and Gears
        self.next_band(1)
        self.write_rows(1, "Mechanical Advantage Calculations for Levers and Gears", [
            "Load / effort; effort arm / load arm",
            "Second class above one; third below",
            "Gear MA = ratio",
            "Crowbar 6: 900 N needs 150 N",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Structures With Mechanisms: Drawings, Systems and the Design Process
        self.next_band(2)
        self.write_rows(2, "Structures With Mechanisms: Drawings, Systems and the Design Process", [
            "Pitch circles, counts, arrows",
            "Input, process, output with numbers",
            "First angle; thick, dashed, chain",
            "Brief, specs, ideas, drawing, budget, make, evaluate",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Ratio inverted''",
            "``Stage ratios added''",
            "``Arrows not alternating or idler in ratio''",
            "``Brief names the solution''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Which Way, How Fast, How Hard
        self.next_band(4)
        self.write_rows(4, "Which Way, How Fast, How Hard", [
            "Which way: flip at each mesh",
            "How fast: divide by the ratio",
            "How hard: multiply by the ratio",
            "Check who drives first",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Two Divisions, Same Answer
        self.next_band(5)
        self.write_rows(5, "Two Divisions, Same Answer", [
            "Newtons over newtons",
            "Arms from the fulcrum, same unit",
            "Above one: force; below: speed",
            "Measured is less than ideal",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): The Headgear in Four Documents
        self.next_band(6)
        self.write_rows(6, "The Headgear in Four Documents", [
            "Back-leg compressed against the pull",
            "Triangles stop racking",
            "Fact, reason, example",
            "No blanks",
        ], scale=0.9, box=2)

        last = Tex("Count teeth and divide driven by driver, multiply the stages and flip at each mesh; MA from forces or arms; and carry the headgear as your example through every question.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
