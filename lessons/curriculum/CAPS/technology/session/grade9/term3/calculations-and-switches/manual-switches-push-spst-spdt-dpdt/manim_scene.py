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

# Band-layout whiteboard scene for manual-switches-push-spst-spdt-dpdt (Part 1 Expert
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


class ManualSwitchesPushSpstSpdtDpdtSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): What a Switch Is: Poles, Throws and Contacts
        self.write_rows(0, "What a Switch Is: Poles, Throws and Contacts", [
            "Switch: contacts touch or separate",
            "Poles: circuits at once; throws: positions",
            "Latching vs momentary; make vs break",
            "Ratings; symbol drawn open",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Push Switches and the SPST Toggle
        self.next_band(1)
        self.write_rows(1, "Push Switches and the SPST Toggle", [
            "Push-to-make: on while pressed",
            "PAT test button: parallel with sensor",
            "SPST: on-off, 2 terminals, latching",
            "PAT silence switch: series with buzzer",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): SPDT and DPDT Switches: Changeover and Reversing
        self.next_band(2)
        self.write_rows(2, "SPDT and DPDT Switches: Changeover and Reversing", [
            "SPDT: 3 terminals, changeover",
            "DPDT: 6 terminals, two SPDT on one lever",
            "Crossed wiring reverses a motor",
            "Choose: poles, throws, action, rating",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``SPDT used where SPST suffices''",
            "``Motor reversal attempted with an SPST''",
            "``Switch drawn closed on the diagram''",
            "``Tiny slide switch used for a motor current''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Metal That Touches or Does Not
        self.next_band(4)
        self.write_rows(4, "Metal That Touches or Does Not", [
            "Metal that touches or does not",
            "Count circuits, count positions",
            "Stay or spring back",
            "Draw it open",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): One Way to Break a Loop
        self.next_band(5)
        self.write_rows(5, "One Way to Break a Loop", [
            "Doorbell, horn, test button",
            "Light switch, torch slide",
            "Plus, two switches side by side, two branches",
            "On-off needs only SPST",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Choose Between Two, or Flip Everything
        self.next_band(6)
        self.write_rows(6, "Choose Between Two, or Flip Everything", [
            "This lamp or that lamp",
            "Toy car goes backwards",
            "How many, how many, stay, amps",
            "Six terminals in two rows",
        ], scale=0.9, box=2)

        last = Tex("Switches are named by poles and throws: push-to-make for a moment, SPST for on-off, SPDT to choose between two, DPDT to reverse a motor.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
