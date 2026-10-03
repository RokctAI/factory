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
# dwell time proportional to subtopics.json (220/240/240/250/180/180/180 of
# 1490 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TradeUnionsConceptSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): What a Trade Union Is
        b0_title = Tex("What is a trade union?").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Workers organised together").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Protect wages and conditions").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Members pay subscriptions").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Unity is strength").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Functions of Trade Unions
        self.next_band(1)
        b1_title = Tex("Functions of unions").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Negotiate wages and benefits").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Safety and conditions").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Represent members in disputes").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Training and national voice").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l1, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_3): Trade Unions in South Africa: History and Federations
        self.next_band(2)
        b2_title = Tex("History in South Africa").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("1973 Durban strikes").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("1979 black unions recognised").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("1985 COSATU formed").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("1995 Labour Relations Act").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_3): Trade Unions in South Africa: History and Federations
        self.next_band(3)
        b3_title = Tex("Federations").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("COSATU 1985").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("NACTU 1986").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("FEDUSA 1997").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("SAFTU 2017").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Collective Bargaining, the Law and the Right to Strike
        self.next_band(4)
        b4_title = Tex("Collective bargaining").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Demand 9 percent: R720").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("Offer 5 percent: R400").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("Settle 7 percent: R560").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("New wage R8 560").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2)

        # --- Band 5 (subtopic_4): Collective Bargaining, the Law and the Right to Strike
        self.next_band(5)
        b5_title = Tex("Protected strike steps").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Refer to the CCMA").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Certificate or 30 days").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("48 hours' written notice").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("No work, no pay").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)



        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): Strength in Numbers
        self.next_band(6)
        b6_title = Tex("Strength in numbers").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("One voice is easy to ignore").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Many voices are not").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Shop stewards and federations").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Right to join a union").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_6): Sitting at the Table
        self.next_band(7)
        b7_title = Tex("Sitting at the table").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Talk, not fight").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Wages, hours, safety").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Meet in the middle").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("R8 000 becomes R8 560").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)

        # --- Band 8 (subtopic_7): When Talks Fail
        self.next_band(8)
        b8_title = Tex("When talks fail").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("CCMA first").scale(0.9).shift(band_shift(8) + UP * 1.30)
        b8_l2 = Tex("Then 48 hours' warning").scale(0.9).shift(band_shift(8) + UP * 0.35)
        b8_l3 = Tex("Protected, but unpaid").scale(0.9).shift(band_shift(8) + DOWN * 0.60)
        b8_l4 = Tex("Strike is the last step").scale(0.9).shift(band_shift(8) + DOWN * 1.55)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(4)
