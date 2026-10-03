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


class HitlerTheNazisAndTheGreatDepressionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Hitler and the Birth of the Nazi Party
        title = Tex('Hitler and the Nazi Party').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Born 1889 in Austria; soldier in World War I').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('1919 joins; 1920 renamed the NSDAP; 1921 leader').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Programme: end Versailles; strip Jews of citizenship').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('The SA: brownshirts who attacked opponents').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Beer Hall Putsch, Mein Kampf and a New Strategy
        self.next_band(1)
        b1_title = Tex('Putsch, prison and a new plan').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Beer Hall Putsch, Munich, 8 to 9 November 1923').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('About nine months in prison: Mein Kampf').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('False race theory, lebensraum, one leader').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('New plan: win power through elections').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Great Depression of 1929
        self.next_band(2)
        b2_title = Tex('The Great Depression').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('October 1929: the Wall Street Crash').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Banks fail; spending and jobs collapse').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Tariffs; world trade falls by about two thirds').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('American loans abroad recalled').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): The Depression in Germany and the Error Museum
        self.next_band(3)
        b3_title = Tex('The Depression in Germany').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Unemployment about 6 million by early 1932').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Brüning rules by decree under Article 48').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Nazi vote: 2,6 percent (1928) to 18,3 percent (1930)').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Promises of work and order, and scapegoats').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): The Depression in Germany and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Hitler was born in Germany''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``The putsch brought Hitler to power''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The Nazis were popular all through the 1920s''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``The Depression began in Germany''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): An Angry Soldier Finds a Microphone
        self.next_band(5)
        b5_title = Tex('An angry soldier finds a microphone').scale(1.0).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Austrian-born, failed art student, war veteran').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('A gifted, furious speaker').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Nazi Party: swastika, brownshirts, Versailles').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Racism was in the plan from the first page').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Failed Attack That Taught a Lesson
        self.next_band(6)
        b6_title = Tex('The failed putsch teaches a lesson').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('1923: storm a beer hall; police fire; it collapses').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('A soft trial and a short prison stay').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Mein Kampf: lies about race and living space').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Win votes, then destroy democracy from inside').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): When America Sneezed, Germany Caught Pneumonia
        self.next_band(7)
        b7_title = Tex('America sneezes').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('1929: the crash; American loans recalled').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('About 6 million Germans without work').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Middle parties look useless').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('1930: the Nazi vote leaps to 18,3 percent').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
