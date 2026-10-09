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

# Band-layout whiteboard scene for gear-system-concepts-and-unequal-spur-gears (Part 1 Expert
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


class GearConceptsSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Gear System Concepts: Counter-Rotation, Idler, Ratios
        self.write_rows(0, "Gear System Concepts: Counter-Rotation, Idler, Ratios", [
            "Driver turns; driven is turned",
            "Meshed pairs counter-rotate",
            "Idler: direction back, ratio unchanged",
            "Trade speed for force",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): Spur Gears of Unequal Size: Velocity Ratio
        self.next_band(1)
        self.write_rows(1, "Spur Gears of Unequal Size: Velocity Ratio", [
            "Teeth pass one for one",
            "VR = driven teeth / driver teeth",
            "10 drives 40: 4 to 1, quarter speed",
            "1 200 rpm x 12/60 = 240 rpm",
        ], scale=0.82, box=1)

        # --- Band 2 (subtopic_3): Force Ratio and Mechanical Advantage Above and Below One
        self.next_band(2)
        self.write_rows(2, "Force Ratio and Mechanical Advantage Above and Below One", [
            "MA for gears = VR",
            "Above one: slow and strong",
            "Below one: fast and weak",
            "Winder needs MA well above one",
        ], scale=0.82, box=3)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``Meshed gears turn the same way''",
            "``Ratio inverted''",
            "``Gears multiply speed and force''",
            "``Driver swap ignored''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Teeth That Push Teeth
        self.next_band(4)
        self.write_rows(4, "Teeth That Push Teeth", [
            "Wheels with teeth that lock",
            "Opposite ways, every time",
            "More teeth, slower",
            "Slower is stronger",
        ], scale=0.9, box=2)

        # --- Band 5 (subtopic_5): Big Gear Slow, Small Gear Fast
        self.next_band(5)
        self.write_rows(5, "Big Gear Slow, Small Gear Fast", [
            "40 over 10 is 4",
            "Swap the driver, flip the effect",
            "Driven speed = driver speed x driver/driven",
            "Count teeth, not diameters",
        ], scale=0.9, box=1)

        # --- Band 6 (subtopic_6): Trade Speed for Force
        self.next_band(6)
        self.write_rows(6, "Trade Speed for Force", [
            "Small to big: MA above one",
            "Big to small: bicycle on the flat",
            "Quarter distance for four times force",
            "Fast weak motor, slow strong drum",
        ], scale=0.9, box=0)

        last = Tex("Teeth pass one for one, so more teeth means slower and slower means stronger; the winder gears a fast weak motor into a slow strong drum.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
