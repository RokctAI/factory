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


class WorldWarI19141918ReviewSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Causes of World War I
        title = Tex('Causes of World War I').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('MAIN: militarism, alliances, imperialism, nationalism').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Triple Alliance against Triple Entente').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('28 June 1914: Franz Ferdinand shot in Sarajevo').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('4 August 1914: Britain at war after Belgium invaded').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Trench Warfare and the Western Front
        self.next_band(1)
        b1_title = Tex('Trench warfare').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Western Front: about 700 km of trenches, 1914 to 1918').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Machine guns, wire and artillery: deadlock').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Somme, 1 July 1916: about 57 000 British casualties').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Gas (1915), tanks (1916), aircraft and U-boats').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): South Africa in World War I
        self.next_band(2)
        b2_title = Tex('South Africa in the war').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('A British dominion: at war from August 1914').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('1915: German South West Africa conquered').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Delville Wood 1916: about 3 000 in, under 800 at roll call').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('SS Mendi, 21 Feb 1917: over 600 men died').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): The End of the War, Its Cost and the Error Museum
        self.next_band(3)
        b3_title = Tex('The end and the cost').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('1917: USA joins; revolution in Russia').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Armistice: 11 a.m., 11 November 1918').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('About 9 million soldiers killed; four empires fell').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Primary source: from the time. Secondary: later.').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): The End of the War, Its Cost and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The assassination was the only cause''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``The war was fought only in Europe''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``South Africa stayed neutral''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``The war ended with a surrender in 1919''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Playground Fight That Pulled In Everyone
        self.next_band(5)
        b5_title = Tex('A playground fight').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Two groups who promised to back each other up').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Showing off muscles, grabbing land, fierce pride').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('The spark: one shot in Sarajevo').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Deep causes plus a trigger').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Mud, Wire and Machine Guns
        self.next_band(6)
        b6_title = Tex('Mud, wire and machine guns').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Ditches 700 km long that hardly moved').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Running across no man's land into machine guns").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Gas, tanks, aeroplanes, submarines').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Soldiers' letters: primary sources").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Two South African Stories
        self.next_band(7)
        b7_title = Tex('Two South African stories').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Delville Wood: hold the wood whatever happens').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('The Mendi: over 600 men lost in fog, 1917').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Black South Africans served without guns').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("11 o'clock, 11 November 1918: the guns stop").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=YELLOW)))
        self.wait(4)
