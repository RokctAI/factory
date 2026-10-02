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
# dwell time proportional to subtopics.json (210/230/240/230/180/190/180 of
# 1460 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CreditSalesNCASession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Cash Sales and Credit Sales
        b0_title = Tex("Cash and credit sales").scale(1.2).to_edge(UP)
        self.play(Write(b0_title))
        self.wait(1.5)
        b0_l1 = Tex("Cash: pay now").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Credit: goods now, pay later").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Debtor: owes the business").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Sale recorded when goods delivered").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Debtors, Credit Policy and the Documents of a Credit Sale
        self.next_band(1)
        b1_title = Tex("Debtors and credit policy").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Debtors: a current asset").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Credit check, limit, terms").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Source document: duplicate invoice").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Monthly statement of account").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The National Credit Act and Consumer Rights
        self.next_band(2)
        b2_title = Tex("National Credit Act, 34 of 2005").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Right to clear cost information").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Reasons if refused; free credit report").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Affordability assessment required").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("No reckless lending; debt counselling").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): The Cost of Credit and Using Credit Wisely
        self.next_band(3)
        b3_title = Tex("The cost of credit").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("12 x 650 = 7 800").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("7 800 - 6 000 = 1 800").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("1 800 / 6 000 = 30 percent").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Credit for assets, not consumables").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): The Cost of Credit and Using Credit Wisely
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Record credit sales when paid''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Debtors are a liability''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The Act protects lying applicants''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``No deposit means free credit''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)


        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Buy Now, Pay Later
        self.next_band(5)
        b5_title = Tex("Buy now, pay later").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Builder takes goods now").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Builder becomes a debtor").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Debt is the shop's asset").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Check, limit, terms").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Rules That Protect Borrowers
        self.next_band(6)
        b6_title = Tex("Rules that protect borrowers").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Right to apply fairly").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Full cost before signing").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Lender checks affordability").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Debt counsellors help").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): What Credit Really Costs
        self.next_band(7)
        b7_title = Tex("What credit really costs").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("R6 000 cash").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("R650 x 12 = R7 800").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("R1 800 extra").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Pay on time: good record").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(4)
