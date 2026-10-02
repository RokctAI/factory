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


class FascismComparedWithDemocracySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): What Fascism Is
        title = Tex('What fascism is').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('Mussolini, Italy, 1922; fasces: rods bound to an axe').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Extreme nationalism; one leader; one party').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('Terror, propaganda, militarism and expansion').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('Nazism: fascism with racism at its centre').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): How the Nazi State Controlled Germany
        self.next_band(1)
        b1_title = Tex('How the Nazi state controlled Germany').scale(1.0).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('SS and Gestapo: arrest without trial').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Denunciations by ordinary citizens').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Goebbels: press, radio, film and the People's Receiver").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Autobahns and rearmament: unemployment under 1 million').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Life in the Nazi State
        self.next_band(2)
        b2_title = Tex('Life in the Nazi state').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Rewritten schools; Hitler Youth compulsory in 1939').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('Women: children, kitchen, church').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Churches controlled; the Confessing Church resisted').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Jobs and order for some; exclusion for others').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Fascism Compared with Democracy, and the Error Museum
        self.next_band(3)
        b3_title = Tex('Fascism and democracy').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('Democracy: free elections, many parties, rule of law').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('Separation of powers; independent courts').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('South Africa 1996: Bill of Rights, Constitutional Court').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('The state serves the people, not the reverse').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Fascism Compared with Democracy, and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Fascism began in Germany''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Small opposition parties are allowed''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The Gestapo held fair trials''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Democracy means the majority can do anything''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Captain Nobody May Question
        self.next_band(5)
        b5_title = Tex('A captain nobody may question').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Mussolini's Italy, 1922: the first fascist state").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('The bundle of sticks: tied together under one leader').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('One leader, one party, no opposition').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Nazi Germany: the same pattern plus racism').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Fear and the Loudspeaker
        self.next_band(6)
        b6_title = Tex('Fear and the loudspeaker').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Fear: the SS, the Gestapo, neighbours reporting').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Loudspeaker: Goebbels, radio, rallies, burned books').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Hitler Youth and the League of German Girls').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('Jobs for some made it easier to look away').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): The Rule Book That Protects Every Player
        self.next_band(7)
        b7_title = Tex('The rule book for every player').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('Vote the captain in, and vote him out').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('The Constitution of 1996 and the Bill of Rights').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('The Constitutional Court as referee').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Equal rights, free press, fair trials').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l2, color=YELLOW)))
        self.wait(4)
