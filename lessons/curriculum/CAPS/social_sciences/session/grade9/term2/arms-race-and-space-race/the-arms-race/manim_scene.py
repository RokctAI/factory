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


class TheArmsRaceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): What Was the Arms Race?
        title = Tex('What was the arms race?').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('A race to build more and better weapons').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('1949: Soviet atomic bomb').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('1952: US hydrogen bomb, about 700 times Hiroshima').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('1961: Tsar Bomba, about 50 megatons').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Stages of the Race: Bombers, Missiles and Submarines
        self.next_band(1)
        b1_title = Tex('Bombers, missiles, submarines').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('Long-range bombers in the 1950s').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('1957: first ICBM, the Soviet R-7').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('1960: submarine-launched Polaris').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('About 70 000 warheads by 1986').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Deterrence, Fear and Cost
        self.next_band(2)
        b2_title = Tex('Deterrence, fear and cost').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Deterrence and the security dilemma').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Duck and cover drills').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Fallout from atmospheric tests').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Trillions of dollars spent').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): The Cuban Missile Crisis, Arms Control and the Error Museum
        self.next_band(3)
        b3_title = Tex('Cuba and arms control').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('October 1962: thirteen days').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Blockade, then missiles removed').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('1963 test ban; 1968 NPT').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('1987 INF Treaty: Reagan and Gorbachev').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): The Cuban Missile Crisis, Arms Control and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``It was only about more bombs''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Cuba was a US-Cuba war''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Treaties ended nuclear weapons''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``The race made everyone safe''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Bigger and Bigger Dogs
        self.next_band(5)
        b5_title = Tex('Bigger and bigger dogs').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Fear leads to more weapons').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('1949, 1952, 1953, 1961').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Bombers, rockets, submarines').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('About 70 000 bombs by 1986').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Under the Desk
        self.next_band(6)
        b6_title = Tex('Under the desk').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Duck and cover drills').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Garden shelters with tinned food').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Deterrence: too scared to attack').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Radioactive dust and protest marches').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Thirteen Days in October
        self.next_band(7)
        b7_title = Tex('Thirteen days in October').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Missiles found in Cuba, 1962').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('A ring of ships around the island').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('28 October: the missiles go home').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Hotline, test ban, INF Treaty').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
