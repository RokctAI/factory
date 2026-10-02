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


class DivisionOfGermanyAndTheBerlinWallSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Germany and Berlin Divided into Zones
        title = Tex('Germany in four zones').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('American, British, French, Soviet').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Berlin: four sectors in the Soviet zone').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('USSR: keep Germany weak').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('1947: Bizonia, then Trizonia').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Berlin Blockade and Airlift, and Two German States
        self.next_band(1)
        b1_title = Tex('Blockade and airlift').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('24 June 1948: roads and railways cut').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Over 270 000 flights in eleven months').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('About 2,3 million tonnes, mostly coal').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('1949: West Germany and East Germany').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Why and How the Berlin Wall Was Built
        self.next_band(2)
        b2_title = Tex('Building the Wall').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('2,7 million left the East, 1949-1961').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Doctors, teachers, engineers lost').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('13 August 1961: barbed wire overnight').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Checkpoint Charlie standoff, October 1961').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Life With the Wall, Its Meaning and the Error Museum
        self.next_band(3)
        b3_title = Tex('Life with the Wall').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Death strip, watchtowers, dogs').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('At least 140 killed at the Wall').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Tunnels, car boots, a balloon').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('Kennedy 1963; Reagan 1987').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Life With the Wall, Its Meaning and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``It divided the two German states''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``It kept Westerners out''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The Airlift was an attack''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Germany had two zones in 1945''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Cake Cut Into Four
        self.next_band(5)
        b5_title = Tex('A cake cut into four').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Four winners, four pieces').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Berlin cut into four as well').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Arguments about Germany's future").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('West and east drift apart').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Planes Every Few Minutes
        self.next_band(6)
        b6_title = Tex('Planes every few minutes').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('A new currency, a furious Stalin').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Two million people cut off').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Food and coal by air').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('1949: two German countries').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Wall Overnight
        self.next_band(7)
        b7_title = Tex('A wall overnight').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Millions leave the East').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('13 August 1961: barbed wire').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Families cut off overnight').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Tunnels, balloons and brave escapes').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
