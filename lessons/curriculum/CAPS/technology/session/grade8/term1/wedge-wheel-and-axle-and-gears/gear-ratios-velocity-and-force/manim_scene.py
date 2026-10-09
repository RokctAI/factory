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

# Band-layout whiteboard scene for gear-ratios-velocity-and-force (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (190/180/150/120/110/90 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GearRatiosVelocityForceSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Different Sizes, Different Speeds
        self.write_rows(0, "Different Sizes, Different Speeds", [
            "Teeth pass one at a time",
            "Small driver, large driven: slower",
            "Large driver, small driven: faster",
            "Bicycle: low gear hill, high gear flat",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): Velocity Ratio and Force Ratio
        self.next_band(1)
        self.write_rows(1, "Velocity Ratio and Force Ratio", [
            "Velocity ratio = driver teeth over driven teeth",
            "10 driving 30: 1:3, one third of a turn",
            "Force ratio is the inverse: 3:1",
            "Speed up, force down; never both",
        ], scale=0.82, box=3)

        # --- Band 2 (subtopic_3): Choosing a Gear Ratio
        self.next_band(2)
        self.write_rows(2, "Choosing a Gear Ratio", [
            "Drill: big driver, small driven",
            "Winch: small driver, big driven",
            "PAT: slow lift or fast fan, say why",
            "Compound train multiplies stages",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``A bigger driven gear turns faster''",
            "``Gears can raise speed and force together''",
            "``Ratios can be read either way round''",
            "``A big idler changes the ratio''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): Big Gear, Small Gear
        self.next_band(4)
        self.write_rows(4, "Big Gear, Small Gear", [
            "Teeth are steps",
            "Small turning big: big goes slow",
            "Big turning small: small goes fast",
            "Low gear easy hill, high gear fast flat",
        ], scale=0.9, box=1)

        # --- Band 5 (subtopic_5): Faster or Stronger, Never Both
        self.next_band(5)
        self.write_rows(5, "Faster or Stronger, Never Both", [
            "Driven turns per driver turn",
            "1:3 slower, 3:1 faster",
            "Slower means stronger",
            "Faster means weaker",
        ], scale=0.9, box=2)

        # --- Band 6 (subtopic_6): Picking the Right Pair
        self.next_band(6)
        self.write_rows(6, "Picking the Right Pair", [
            "Fast job: big driver",
            "Strong job: big driven",
            "Stack pairs for huge ratios",
            "Write the choice and the reason",
        ], scale=0.9, box=1)

        last = Tex("Tooth counts set the speed, the force ratio is the inverse, and a designer picks the pair the job needs.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
