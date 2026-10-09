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

# Band-layout whiteboard scene for investigating-the-need-for-an-electronic-device (Part 1 Expert
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


class InvestigatingTheNeedForAnElectronicDeviceSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): The PAT Scenario: A Need That an Electronic Device Can Meet
        self.write_rows(0, "The PAT Scenario: A Need That an Electronic Device Can Meet", [
            "Scenario: detect a condition, tell someone",
            "Users: grandmother, weak eyesight; children",
            "Setting: sun, outdoors, kitchen 10 m away, no mains",
            "Must not: open tank, mains near water, eat batteries",
        ], scale=0.82, box=0)

        # --- Band 1 (subtopic_2): Investigating Users, Settings and Existing Devices
        self.next_band(1)
        self.write_rows(1, "Investigating Users, Settings and Existing Devices", [
            "Now: bang on tank, climb ladder",
            "Shops: float switch, LED ladder, ultrasonic gauge",
            "Compare: senses, shows, cost, power",
            "Interview: bright light at window, no night buzzer",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): From Need to Circuit: What the Electronics Must Do
        self.next_band(2)
        self.write_rows(2, "From Need to Circuit: What the Electronics Must Do", [
            "Input: level sensor; process: switch or transistor; output: LED",
            "User terms -> electronic terms",
            "LED + resistor, 4.5-6 V, low drain, waterproof, long wire",
            "Record on PAT investigation pages",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Favourite circuit chosen before asking the user''",
            "``Setting ignored: LED invisible in sunlight''",
            "``Device described without its user''",
            "``Power source and battery life forgotten''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Who Needs What, and Why
        self.next_band(4)
        self.write_rows(4, "Who Needs What, and Why", [
            "Cannot see inside; tap runs dry",
            "Grandmother at the kitchen window",
            "Hard sun, no mains, rain",
            "Not complicated, not hungry for batteries",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Look at What Already Exists
        self.next_band(5)
        self.write_rows(5, "Look at What Already Exists", [
            "Banging and ladders",
            "Float switch is a switch, cell, lamp",
            "Gauge: too costly, needs mains",
            "Ask her, write it down",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Sense, Decide, Show
        self.next_band(6)
        self.write_rows(6, "Sense, Decide, Show", [
            "Sense the level",
            "Decide it is low",
            "Show a bright LED",
            "Pages: scenario, users, products, interview, I-P-O",
        ], scale=0.9, box=3)

        last = Tex("Investigate the need first: who must know what, where, within what limits; then state the device as input, process and output.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
