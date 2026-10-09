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

# Band-layout whiteboard scene for switches-and-or-logic-and-conventional-current (Part 1 Expert
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


class SwitchesAndOrLogicAndConventionalCurrentSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Switches in Series: AND Logic
        self.write_rows(0, "Switches in Series: AND Logic", [
            "Series switches: one loop, two gaps",
            "Lamp on only when A and B closed: AND",
            "Table: off, off, off, on",
            "Mixer: lid down AND start pressed",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Switches in Parallel: OR Logic
        self.next_band(1)
        self.write_rows(1, "Switches in Parallel: OR Logic", [
            "Parallel switches: two routes",
            "Lamp on when A or B closed: OR",
            "Table: off, on, on, on",
            "Van light: any door; alarm: any sensor",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Conventional Current From Positive to Negative and Reading Logic in Devices
        self.next_band(2)
        self.write_rows(2, "Conventional Current From Positive to Negative and Reading Logic in Devices", [
            "Conventional current: + to -",
            "Electrons go the other way; convention kept",
            "Both/all/only when -> series; any/either/or -> parallel",
            "Combined: (low AND silence) OR test",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Parallel switches used for a safety interlock''",
            "``Current arrows drawn minus to plus''",
            "``Two-switch truth table with wrong row count''",
            "``Parallel switches confused with parallel lamps''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Both Must Be On
        self.next_band(4)
        self.write_rows(4, "Both Must Be On", [
            "Both must be on",
            "Only the last row lights",
            "Safety interlocks",
            "Buzzer: low and night switch on",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Either Will Do
        self.next_band(5)
        self.write_rows(5, "Either Will Do", [
            "Either will do",
            "Three rows light",
            "Alarms and convenience",
            "LED: low or test button",
        ], scale=0.9, box=0)

        # --- Band 6 (subtopic_6): Which Way the Arrows Point
        self.next_band(6)
        self.write_rows(6, "Which Way the Arrows Point", [
            "Arrows plus to minus",
            "Diodes drawn to match",
            "Read the words",
            "Build, test, tick the table",
        ], scale=0.9, box=2)

        last = Tex("Series switches mean all must be closed (AND); parallel switches mean any one will do (OR); conventional current is drawn from positive to negative.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
