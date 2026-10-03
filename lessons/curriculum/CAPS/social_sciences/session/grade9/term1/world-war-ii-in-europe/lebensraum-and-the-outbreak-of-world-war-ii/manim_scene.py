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


class LebensraumAndTheOutbreakOfWorldWarIiSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Hitler's Aims and the First Steps, 1933 to 1936
        title = Tex('Aims and first steps').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Aims: destroy Versailles, unite Germans, lebensraum').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('1933: leave the League. 1935: conscription, Luftwaffe').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('7 March 1936: troops into the Rhineland').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('1936: the Rome-Berlin Axis takes shape').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Appeasement: Austria, the Sudetenland and Munich
        self.next_band(1)
        b1_title = Tex('Appeasement').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('March 1938: Anschluss with Austria').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Sudetenland: about 3 million German speakers').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Munich, 30 September 1938: Czechoslovakia absent').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Fear of war, unready armies, Versailles seen as unfair').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): From Prague to Poland, 1939
        self.next_band(2)
        b2_title = Tex('From Prague to Poland').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('15 March 1939: Germany occupies the Czech lands').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('23 August 1939: the Nazi-Soviet Pact').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('1 September 1939: blitzkrieg on Poland').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('3 September 1939: Britain and France declare war').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Axis versus Allies, South Africa's Decision, and the Error Museum
        self.next_band(3)
        b3_title = Tex('Axis against Allies').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Axis: Germany, Italy, Japan').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Allies: Britain, France, the Commonwealth').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Later: USSR (June 1941), USA (December 1941)').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("South Africa: Smuts's motion carried 80 to 67").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Axis versus Allies, South Africa's Decision, and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Britain and France stopped the Rhineland move''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Czechoslovakia agreed at Munich''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The Soviet Union was always an Ally''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``The war began with an attack on Britain''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Testing the Fence
        self.next_band(5)
        b5_title = Tex('Testing the fence').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Push: leave the League').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Push harder: a banned army and air force').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Climb over: the Rhineland, 1936').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Nobody stops him; he gets bolder').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Feeding the Crocodile
        self.next_band(6)
        b6_title = Tex('Feeding the crocodile').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Austria taken, March 1938').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Munich: the Sudetenland given away').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Peace for our time').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('March 1939: the rest of Czechoslovakia').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Two Teams Line Up
        self.next_band(7)
        b7_title = Tex('Two teams line up').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Hitler and Stalin's secret deal").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('1 September 1939: Poland invaded').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Axis: Germany, Italy, Japan. Allies: Britain, France...').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('South Africa: 80 to 67 for war').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=YELLOW)))
        self.wait(4)
