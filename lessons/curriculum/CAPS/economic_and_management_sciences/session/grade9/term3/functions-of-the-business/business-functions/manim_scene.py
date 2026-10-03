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
# dwell time proportional to subtopics.json (230/240/240/220/180/190/180 of
# 1480 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BusinessFunctionsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): General Management and Administration
        b0_title = Tex("General management").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Plan: set goals").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Organise: people, money, equipment").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Lead: guide and motivate").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Control: compare results to plan").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_1): General Management and Administration
        self.next_band(1)
        b1_title = Tex("Administration").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Collect and record information").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Store it securely").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Accounting records").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("POPIA protects personal data").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l4, color=GREEN)))
        self.wait(2)

        # --- Band 2 (subtopic_2): Purchasing, Production and Marketing
        self.next_band(2)
        b2_title = Tex("Purchasing and production").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Five rights: quality, quantity").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("price, time, supplier").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Production: inputs to outputs").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Job, batch, mass production").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_2): Purchasing, Production and Marketing
        self.next_band(3)
        b3_title = Tex("Marketing: the four Ps").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Product").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Price").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Place").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Promotion").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_3): Financing, Human Resources and Public Relations
        self.next_band(4)
        b4_title = Tex("Money, people, image").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Financing: obtain, manage funds").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("HR: recruit, train, pay").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("PR: goodwill with stakeholders").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("PR is not advertising").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b4_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 5 (subtopic_4): Risk Management
        self.next_band(5)
        b5_title = Tex("Risk management").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Avoid the risk").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Reduce it with controls").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Transfer it: insurance").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Accept small or uninsurable risks").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)

        # --- Band 6 (subtopic_4): Risk Management
        self.next_band(6)
        b6_title = Tex("Error museum").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("``Marketing is just advertising''").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("``PR means paid adverts''").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("``Insurance covers every risk''").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("``Small firms need no HR''").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): Nine Jobs Every Business Must Do
        self.next_band(7)
        b7_title = Tex("Nine jobs").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Manage, record, buy").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Make, sell, fund").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Staff, reputation, protect").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("One owner may do all nine").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 8 (subtopic_6): Following One Chair Through the Business
        self.next_band(8)
        b8_title = Tex("One chair").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("Marketing agrees the design").scale(0.9).shift(band_shift(8) + UP * 1.30)
        b8_l2 = Tex("Purchasing buys the pine").scale(0.9).shift(band_shift(8) + UP * 0.35)
        b8_l3 = Tex("Production makes and checks").scale(0.9).shift(band_shift(8) + DOWN * 0.60)
        b8_l4 = Tex("Finance pays until school pays").scale(0.9).shift(band_shift(8) + DOWN * 1.55)
        for m in (b8_l1, b8_l2, b8_l3, b8_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)

        # --- Band 9 (subtopic_7): Matching Problems to Functions
        self.next_band(9)
        b9_title = Tex("Match the problem").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = Tex("No timber: purchasing").scale(0.9).shift(band_shift(9) + UP * 1.30)
        b9_l2 = Tex("Wobbly legs: production").scale(0.9).shift(band_shift(9) + UP * 0.35)
        b9_l3 = Tex("No insurance: risk management").scale(0.9).shift(band_shift(9) + DOWN * 0.60)
        b9_l4 = Tex("Bad press: public relations").scale(0.9).shift(band_shift(9) + DOWN * 1.55)
        for m in (b9_l1, b9_l2, b9_l3, b9_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b9_l4, color=YELLOW)))
        self.wait(4)
