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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GravityMassWeightSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Field Forces and Gravitational Attraction
        title = Tex("Gravitational force").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Field force: acts without touching").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Every mass attracts every other mass").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Bigger masses: stronger. Further apart: weaker").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Tides, orbits, falling objects").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Mass and Weight
        self.next_band(1)
        b1_title = Tex("Mass and weight").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Mass: matter, kg, balance, same everywhere").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Weight: force, N, spring balance").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = MathTex(r"W = m \times g").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = MathTex(r"60 \times 9{,}8 = 588 \ \mathrm{N}; \ 60 \times 1{,}6 = 96 \ \mathrm{N}").scale(0.75).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Falling, Free Fall and Weightlessness
        self.next_band(2)
        b2_title = Tex("Falling").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Without air, all objects fall at the same rate").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Hammer and feather on the Moon, 1971").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Air resistance slows light, wide objects").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Astronauts float: free fall").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Mass and Weight Problems and the Error Museum
        self.next_band(3)
        b3_title = Tex("Problems").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"900 \times 3{,}7 = 3330 \ \mathrm{N}").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = MathTex(r"16 \div 1{,}6 = 10 \ \mathrm{kg}").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Spring balance measures force").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("500 g is 0,5 kg").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Mass and Weight Problems and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Mass and weight are the same''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``No gravity in space''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Heavier objects fall faster''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Weight in kilograms''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Invisible Pull
        self.next_band(5)
        b5_title = Tex("The invisible pull").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Everything pulls everything").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Only huge masses pull strongly").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Moon goes round; tides rise").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Gravity only pulls").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Kilograms and Newtons
        self.next_band(6)
        b6_title = Tex("Kilograms and newtons").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Mass: stuff, kilograms, never changes").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Weight: pull, newtons, changes").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Times 9,8 on Earth").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Times 1,6 on the Moon").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Falling Together
        self.next_band(7)
        b7_title = Tex("Falling together").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Book and pencil land together").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Feather slowed by air").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Crumpled paper drops fast").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Astronauts fall around the Earth").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l1, color=YELLOW)))
        self.wait(4)
