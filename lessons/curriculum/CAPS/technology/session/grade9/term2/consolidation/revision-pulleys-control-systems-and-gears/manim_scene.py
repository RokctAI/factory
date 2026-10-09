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

# Band-layout whiteboard scene for revision-pulleys-control-systems-and-gears (Part 1 Expert
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


class RevisionPulleysControlSystemsAndGearsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Revising Pulleys: Fixed, Movable and Block and Tackle
        self.write_rows(0, "Revising Pulleys: Fixed, Movable and Block and Tackle", [
            "Fixed: MA 1, direction; movable: MA 2",
            "Tackle: MA = load-bearing sections",
            "Rope pulled = lift x MA",
            "Efficiency = actual / ideal",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Revising Control Systems: Ratchet, Brakes and Cleat
        self.next_band(1)
        self.write_rows(1, "Revising Control Systems: Ratchet, Brakes and Cleat", [
            "Controls add no force; they govern motion",
            "Ratchet: one direction; pawl into teeth",
            "Brakes: friction -> heat; disc and rim",
            "Cleat: holds, load tightens, instant release",
        ], scale=0.82, box=0)

        # --- Band 2 (subtopic_3): Revising Gears: Spur, Idler, Bevel, Rack and Worm
        self.next_band(2)
        self.write_rows(2, "Revising Gears: Spur, Idler, Bevel, Rack and Worm", [
            "Spur: opposite ways; ratio = driven / driver",
            "Idler: direction only; compound: multiply",
            "Bevel 90 degrees; rack: teeth x spacing",
            "Worm: ratio = wheel teeth; self-locking",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Hand rope counted as load-bearing''",
            "``Control system said to add force''",
            "``Gear ratio written driver over driven''",
            "``Idler thought to change ratio; wheel thought to drive worm''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Count the Ropes
        self.next_band(4)
        self.write_rows(4, "Count the Ropes", [
            "Count the up-ropes",
            "Hand rope from the top block: no",
            "60 N on 3 ropes: 20 N, 1.5 m rope",
            "Measured a bit less",
        ], scale=0.9, box=0)

        # --- Band 5 (subtopic_5): Allow, Stop, Hold
        self.next_band(5)
        self.write_rows(5, "Allow, Stop, Hold", [
            "Allow: ratchet",
            "Stop: brake",
            "Hold: cleat",
            "None adds force",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Count the Teeth
        self.next_band(6)
        self.write_rows(6, "Count the Teeth", [
            "15 -> 45: 3:1, 300 in, 100 out",
            "Idler: same ratio, same way",
            "8 teeth x 12 mm = 96 mm",
            "50-tooth worm wheel: 50:1",
        ], scale=0.9, box=0)

        last = Tex("Count ropes for pulleys, count teeth for gears, and remember controls allow, stop or hold without adding force.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
