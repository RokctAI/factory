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

# Band-layout whiteboard scene for light-years-light-hours-and-light-minutes (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (230/240/240/240/180/170/180 of 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class LightDistancesSession(MovingCameraScene):
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
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, 'The speed of light', [
            '300 000 km/s',
            'Nothing is faster',
            'Distance = speed $\\times$ time',
            'Moon: 1.3 light seconds',
        ], scale=0.8, box=2)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, 'Light minutes and hours', [
            'Light minute: 18 million km',
            'Sun: 8 light minutes',
            'Light hour: 1 080 million km',
            'Neptune: 4 light hours',
        ], scale=0.8, box=1)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, 'The light year', [
            'Light travels for one year',
            'About 9.5 trillion km',
            'A distance, not a time',
            'Proxima: 4.24 light years',
        ], scale=0.8, box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, 'Choosing and using', [
            'Convert time to seconds',
            'Then multiply by 300 000',
            'Jupiter: 774 million km',
            'Write the unit',
        ], scale=0.8, box=0)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = [
            "``A light year is a time''",
            "``Multiply minutes by 300 000''",
            "``We see stars as they are now''",
            "``Signals arrive instantly''",
            "``The Sun is 8 light years away''",
        ]
        for i, e in enumerate(errs):
            m = Tex(e).scale(0.8).shift(band_shift(4) + UP * (1.3 - 1.0 * i))
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============

        # --- Band 5 (subtopic_5)
        self.next_band(5)
        self.write_rows(5, 'A message to Mars', [
            '300 000 km every second',
            'Mars: over 20 minutes',
            'Rovers think for themselves',
        ], scale=0.85, box=1)

        # --- Band 6 (subtopic_6)
        self.next_band(6)
        self.write_rows(6, 'A year of travelling light', [
            '9.5 trillion km',
            'A distance, not a time',
            'Nearest star: 4.24',
        ], scale=0.85, box=1)

        # --- Band 7 (subtopic_7)
        self.next_band(7)
        self.write_rows(7, 'A time machine', [
            'Sun: 8 minutes ago',
            'Andromeda: 2.5 million years',
            'Pick the right unit',
        ], scale=0.85, box=1)


        last = Tex('Distance = speed $\\times$ time.').scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
