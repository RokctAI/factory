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

# Band-layout whiteboard scene for first-class-levers (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (200/150/150/110/110/110 of 830 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FirstClassLeversSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Pivot in the middle
        self.write_rows(0, "Pivot in the middle", [
            "Effort on one side, load on the other",
            "Always reverses the direction of the force",
            "Seesaw, crowbar, claw hammer",
            "Scissors: two levers, one pivot",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Three possible advantages
        self.next_band(1)
        self.write_rows(1, "Three possible advantages", [
            "Pivot near the load: MA above 1",
            "Pivot in the centre: MA equal to 1",
            "Pivot near the effort: MA below 1, fast",
            "The longer arm carries the smaller force",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): First-class levers in design
        self.next_band(2)
        self.write_rows(2, "First-class levers in design", [
            "Pivot near the tips for a strong grip",
            "Tin snips: short blades, long handles",
            "Pedal bin: foot down, lid up",
            "Direction change is often the real reason",
        ], scale=0.82, box=0)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``All first-class levers make you stronger''",
            "``Judge the class by the shape''",
            "``Scissors are one lever''",
            "``The pivot position is fixed by nature''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): The pivot sits in the middle
        self.next_band(4)
        self.write_rows(4, "The pivot sits in the middle", [
            "Look at what is in the middle",
            "Push down, other end goes up",
            "Brick under the crowbar",
            "Scissors joined at the screw",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Stronger, same or weaker
        self.next_band(5)
        self.write_rows(5, "Stronger, same or weaker", [
            "Pivot near the load: stronger",
            "Pivot in the middle: same, opposite way",
            "Pivot near you: harder but fast",
            "Longer side, smaller force",
        ], scale=0.9, box=3)

        # --- Band 6 (subtopic_6): Choosing where the pivot goes
        self.next_band(6)
        self.write_rows(6, "Choosing where the pivot goes", [
            "Rescue jaws: pivot near the tips",
            "Kitchen scissors and tin snips",
            "Cut thick cloth near the pivot",
            "Pedal bin changes direction",
        ], scale=0.9, box=0)

        last = Tex("First class: pivot in the middle, direction reversed, and the pivot position sets the advantage.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
