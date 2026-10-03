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


class WarsawGhettoUprisingAndTheEndOfTheWarInEuropeSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Warsaw Ghetto and the Great Deportation
        title = Tex('The Warsaw Ghetto').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Sealed November 1940: 400 000 behind a wall').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Starvation rations; 80 000 dead by mid-1942').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Ringelblum's archive buried in milk cans").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('1942: about 265 000 deported to Treblinka').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Uprising of April and May 1943
        self.next_band(1)
        b1_title = Tex('The uprising, 1943').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('ŻOB led by Mordechaj Anielewicz, aged 23').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('19 April 1943: German troops driven back').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Stroop burns the ghetto block by block').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Almost four weeks of resistance').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Tide Turns: Stalingrad, North Africa, Italy and D-Day
        self.next_band(2)
        b2_title = Tex('The tide turns').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Stalingrad: 91 000 Germans surrender, Feb 1943').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('El Alamein 1942: South Africans fight').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('About 334 000 South African volunteers').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('6 June 1944: D-Day landings in Normandy').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): The Fall of Berlin, VE Day, the Cost of War and the Error Museum
        self.next_band(3)
        b3_title = Tex('The end in Europe').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("30 April 1945: Hitler's suicide").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('8 May 1945: VE Day, unconditional surrender').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('70 to 85 million dead worldwide').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Germany split into four zones').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): The Fall of Berlin, VE Day, the Cost of War and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The 1943 and 1944 uprisings were the same''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``The ghetto fighters expected to win''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``D-Day alone defeated Germany''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Black South Africans did not serve''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Choosing to Fight Behind the Wall
        self.next_band(5)
        b5_title = Tex('Choosing to fight').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('A wall with broken glass on top').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Children smuggle bread through holes').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('The trains to Treblinka').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Pistols and petrol bombs against tanks').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Tide Turns
        self.next_band(6)
        b6_title = Tex('The tide turns').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Trapped at Stalingrad in winter').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('South Africans in the desert and Italy').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Job Maseko sinks a ship').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('D-Day: 156 000 land on the first day').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Last Days and the Cost
        self.next_band(7)
        b7_title = Tex('The last days and the cost').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Auschwitz and Belsen reached by Allied troops').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('30 April: Hitler dies; 8 May: VE Day').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('About 11 000 South Africans died').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Nuremberg trials and four zones').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
