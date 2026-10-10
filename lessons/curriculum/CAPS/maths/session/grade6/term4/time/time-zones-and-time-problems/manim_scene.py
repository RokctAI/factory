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

# Band-layout whiteboard scene for time-zones-and-time-problems (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (180/160/160/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TimeZonesAndTimeProblemsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Why We Have Time Zones
        self.write_rows(0, "Why We Have Time Zones", [
            "Earth spins: sun rises in the east",
            "East: ahead; west: behind",
            "South Africa: one time zone",
            "Accra 2 hours behind, Nairobi 1 ahead",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Calculating the Time Somewhere Else
        self.next_band(1)
        self.write_rows(1, "Calculating the Time Somewhere Else", [
            "14:00 here: Dubai 16:00",
            "Beijing 20:00; Accra 12:00",
            "Brazil 09:00",
            "20:00 here: 03:00 next day in Tokyo",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Solving Time Problems
        self.next_band(2)
        self.write_rows(2, "Solving Time Problems", [
            "Leave 10:30, fly 8 hours",
            "Lands 18:30 our time",
            "Add 2: 20:30 in Dubai",
            "Tokyo 19:00 = 12:00 here",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Beijing: 14:00 minus 6 = 08:00''",
            "``Tokyo: 03:00 the same day''",
            "``Lands 18:30 Dubai time''",
            "``The flight takes 10 hours''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 4 (subtopic_4): East Is Ahead
        self.next_band(4)
        self.write_rows(4, "East Is Ahead", [
            "East is ahead",
            "Sun rises east",
            "Add for east",
            "Subtract for west",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Add or Subtract
        self.next_band(5)
        self.write_rows(5, "Add or Subtract", [
            "Add or subtract",
            "Dubai: plus 2",
            "Beijing: plus 6",
            "Accra: minus 2",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Fly and Call
        self.next_band(6)
        self.write_rows(6, "Fly and Call", [
            "Fly and call",
            "Add flying time",
            "Then change zones",
            "20:30 in Dubai",
        ], scale=0.9, box=3)

        last = Tex("East of us is ahead, so add hours; west of us is behind, so subtract hours, and watch for midnight.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
