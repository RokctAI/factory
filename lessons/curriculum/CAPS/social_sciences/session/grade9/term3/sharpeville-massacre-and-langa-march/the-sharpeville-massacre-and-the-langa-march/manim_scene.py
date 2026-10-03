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


class TheSharpevilleMassacreAndTheLangaMarchSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Causes of the Protests
        title = Tex('Causes').scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex('The hated pass book').scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex('Hardship in Sharpeville and Langa').scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex('PAC: leave your pass at home').scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex('No bail, no defence, no fine').scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Sharpeville Massacre
        self.next_band(1)
        b1_title = Tex('Sharpeville, 21 March 1960').scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex('A crowd at the police station').scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex('Police fire without warning').scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex('69 killed, about 180 wounded').scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex('Many shot in the back').scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Langa and the March on Cape Town
        self.next_band(2)
        b2_title = Tex('Langa and Cape Town').scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex('Shootings and a strike in Langa').scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex('30 March: about 30 000 march').scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex('Kgosana sends the crowd home').scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex('Then he is arrested').scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Short- and Longer-Term Consequences, and the Error Museum
        self.next_band(3)
        b3_title = Tex('Consequences').scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex('State of emergency, 30 March').scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex('ANC and PAC banned, 8 April').scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex('Turn to armed struggle').scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex('21 March: Human Rights Day').scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Short- and Longer-Term Consequences, and the Error Museum
        self.next_band(4)
        b4_title = Tex('Error museum').scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The crowd attacked with weapons''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``The ANC organised the protest''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The pass laws were abolished''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``No effect outside South Africa''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): A Book Left at Home
        self.next_band(5)
        b5_title = Tex('A book left at home').scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex('Everyone hated the pass book').scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex('Hard times in the townships').scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex('Arrest us, said the PAC').scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex('Fill the jails').scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Forty Seconds of Gunfire
        self.next_band(6)
        b6_title = Tex('Forty seconds of gunfire').scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex('Thousands singing and waiting').scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex('Jets and armoured cars').scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex('Shooting without warning').scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex('69 people killed').scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Long Walk Into the City
        self.next_band(7)
        b7_title = Tex('A long walk into the city').scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex('30 000 march peacefully').scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex('A broken promise').scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex('Thousands locked up').scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex('Peaceful protest turns to armed struggle').scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
