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

# Band-layout whiteboard scene for terms-3-and-4-revision (Part 1 Expert
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


class Terms3And4RevisionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Term 3 Recalled: Electrical Systems and the Device
        self.write_rows(0, "Term 3 Recalled: Electrical Systems and the Device", [
            "Series: same current, voltage divides, one break",
            "Parallel: full voltage, current divides; houses",
            "V = I x R; 9 V / 450 ohms = 20 mA",
            "Components, sensors, transistor; logic; safety",
        ], scale=0.82, box=2)

        # --- Band 1 (subtopic_2): Term 4 Recalled: Preserving, Plastics and Recycling
        self.next_band(1)
        self.write_rows(1, "Term 4 Recalled: Preserving, Plastics and Recycling", [
            "Rust: air + water; paint, zinc, electroplating",
            "Food: store dry, pickle, dry, salt",
            "Plastics: thermo vs set; codes 1 to 7; 3 Rs in order",
            "Plant + systems diagram; 4 mouldings; design rules",
        ], scale=0.82, box=2)

        # --- Band 2 (subtopic_3): Exam Technique: Reading, Drawing and Explaining
        self.next_band(2)
        self.write_rows(2, "Exam Technique: Reading, Drawing and Explaining", [
            "Name, describe, explain, compare, draw, calculate",
            "Diagrams marked by parts: symbols, boxes, views",
            "Scenario: clues -> facts -> technical words",
            "A mark a minute; time for the drawing",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Describing when asked to explain''",
            "``Calculation without units or working''",
            "``Diagram with no labels''",
            "``Drawing rushed after overlong first section''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The Circuit Half of the Year
        self.next_band(4)
        self.write_rows(4, "The Circuit Half of the Year", [
            "One path or branches",
            "V = I x R with units",
            "Sensor, switch, output",
            "AND, OR, NOT",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): The Processing Half of the Year
        self.next_band(5)
        self.write_rows(5, "The Processing Half of the Year", [
            "Air and water",
            "Soften or char",
            "Reduce, reuse, recycle",
            "Three boxes and feedback",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): How to Earn the Marks
        self.next_band(6)
        self.write_rows(6, "How to Earn the Marks", [
            "Read the command word",
            "Label everything",
            "Show working",
            "Watch the clock",
        ], scale=0.9, box=0)

        last = Tex("Term 3 is circuits, components, logic and the device; Term 4 is preserving, plastics, recycling, moulding and the design process; marks come from command words, correct terms, working and labelled diagrams.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
