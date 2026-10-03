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
# removed. Write-only reveals on single-string Tex keep the export to the
# allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MeaningOfDevelopmentSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Defining Development
        title = Tex('Defining development').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('A process: quality of life improves').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Standard of living: income and goods').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Quality of life: health, safety, freedom').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Development can go backwards').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Economic, Social and Environmental Aspects of Development
        self.next_band(1)
        b1_title = Tex('Three aspects of development').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Economic: GDP, jobs, infrastructure').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Social: health, education, rights').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Environmental: resources for the future').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Each aspect affects the others').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Classifying Countries: Developed, Developing, North and South
        self.next_band(2)
        b2_title = Tex('Classifying countries').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Developed and developing; MEDC and LEDC').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Brandt Line: Global North and South').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('NICs and emerging economies, BRICS').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('South Africa: upper-middle-income').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Development Within South Africa and the Error Museum
        self.next_band(3)
        b3_title = Tex('Development within South Africa').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Gini coefficient about 0,63').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Roots in land laws and apartheid').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Housing, water and grants since 1994').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('High unemployment, especially youth').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Development Within South Africa and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Development means economic growth''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Developed countries have no poverty''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``North and South follow the equator''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``An average shows how most people live''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Family's Life Getting Better
        self.next_band(5)
        b5_title = Tex("A family's life getting better").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('A tap, a clinic, a school').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Quality of life is more than money').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('War, drought or disease can reverse it').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('HIV: life expectancy fell, then rose').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Three-Legged Pot
        self.next_band(6)
        b6_title = Tex('A three-legged pot').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Economic leg: jobs, roads, power').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Social leg: health, school, rights').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Environmental leg: water, soil, air').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Break one leg and the pot falls').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Map With a Wavy Line
        self.next_band(7)
        b7_title = Tex('A map with a wavy line').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Developed and developing countries').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('The North-South line is about wealth').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('South Korea and China have changed').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('South Africa: a country with two faces').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
