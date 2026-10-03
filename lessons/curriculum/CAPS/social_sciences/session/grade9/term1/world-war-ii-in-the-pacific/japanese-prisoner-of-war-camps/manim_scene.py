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


class JapanesePrisonerOfWarCampsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Who Were the Prisoners and Why Were They Treated So Harshly?
        title = Tex('Who were the prisoners?').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('About 140 000 Western Allied prisoners').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Singapore alone: about 80 000 captured').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Surrender taught as shameful').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Geneva Convention signed, not ratified').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Conditions in Captivity: Bataan, Changi and the Hell Ships
        self.next_band(1)
        b1_title = Tex('Bataan, Changi and the hell ships').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Bataan, April 1942: about 76 000 march').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Changi: gardens, lectures, starvation').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('Hell ships: unmarked, packed holds').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('About 1 in 4 died, versus 1 in 25').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Burma-Thailand Railway
        self.next_band(2)
        b2_title = Tex('The Burma-Thailand Railway').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('415 km built in about sixteen months').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('60 000 prisoners, 200 000+ romusha').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Hellfire Pass: the 1943 speedo').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('12 000 to 13 000 prisoners died').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Liberation, Justice, Memory and the Error Museum
        self.next_band(3)
        b3_title = Tex('Liberation and justice').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('August 1945: survivors freed').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Tokyo tribunal: seven executed').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Unit 731 leaders given immunity').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Van der Post: choosing not to hate').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Liberation, Justice, Memory and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Japanese people are naturally cruel''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Only Western soldiers died on the railway''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The River Kwai film is accurate''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Japan followed the Geneva Convention''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Rule About Surrender
        self.next_band(5)
        b5_title = Tex('A rule about surrender').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Never be taken prisoner').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('140 000 captured in 1942').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('A promise to follow the rules, broken').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Violence passed down the line').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): A Long Hungry March
        self.next_band(6)
        b6_title = Tex('A long hungry march').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Bataan: 100 km in burning heat').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Changi: concerts and gardens').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Hell ships with no markings').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('One in four prisoners died').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Railway Through the Jungle
        self.next_band(7)
        b7_title = Tex('A railway through the jungle').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Five years of work demanded in one').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('Picks, shovels and cholera').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('80 000 to 100 000 Asian workers died').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Truth, justice and remembering all').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
