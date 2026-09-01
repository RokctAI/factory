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

# Band-layout whiteboard scene for the session duo "Internal Control Basics"
# (grade10 term1, internal-control-ethics-gaap). One band per teaching beat,
# camera moves down to fresh space, nothing is ever removed. Exporter-safe
# vocabulary only: Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup,
# single-string Tex lines revealed with Write — no sub-part transforms.
#
# Subtopic time shares (subtopics.json, total 1230 s):
# 170/180/190/180/170/170/170 -> bands 0-1 / 2-3 / 4-5 / 6-7 / 8 / 9 / 10.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class InternalControlBasicsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: player holds the topic full-screen while intro.md plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definition and the four objectives ---
        title = Tex("Internal Control").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Policies, procedures and checks that:").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(1.5)
        b0_l2 = Tex("1. Safeguard assets").scale(1.0).shift(UP * 0.3)
        b0_l3 = Tex("2. Keep records accurate and reliable").scale(1.0).shift(DOWN * 0.5)
        b0_l4 = Tex("3. Promote efficient operations").scale(1.0).shift(DOWN * 1.3)
        b0_l5 = Tex("4. Encourage adherence to policies").scale(1.0).shift(DOWN * 2.1)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(VGroup(b0_l2, b0_l3, b0_l4, b0_l5), color=GREEN)))
        self.wait(2.5)
        b0_l6 = Tex("Against: errors, fraud, waste").scale(1.0).shift(DOWN * 3.1)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): division of duties ---
        self.next_band(1)
        b1_title = Tex("Division of duties").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("No single person controls a transaction").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("from beginning to end").scale(1.0).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        box1 = SurroundingRectangle(VGroup(b1_l1, b1_l2), color=YELLOW)
        self.play(Create(box1))
        self.wait(2)
        b1_l3 = Tex("Receives cash $\\neq$ records cash").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex("Orders stock $\\neq$ receives and pays").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Fraud must pass a second pair of eyes:").scale(0.95).shift(band_shift(1) + DOWN * 2.4)
        b1_l6 = Tex("trust in people becomes trust in a SYSTEM").scale(0.95).shift(band_shift(1) + DOWN * 3.2)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): components one to three ---
        self.next_band(2)
        b2_title = Tex("Five components — first three").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("1. Control environment — tone at the top").scale(0.95).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex("the soil every control grows in").scale(0.9).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex("2. Risk assessment — ask what can go wrong,").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        b2_l4 = Tex("repeatedly, as the business changes").scale(0.9).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("3. Control activities — the rules and checks").scale(0.95).shift(band_shift(2) + DOWN * 2.3)
        b2_l6 = Tex("that answer the risks").scale(0.9).shift(band_shift(2) + DOWN * 3.1)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): components four, five, flowing sentence ---
        self.next_band(3)
        b3_title = Tex("Components four and five").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("4. Information and communication —").scale(0.95).shift(band_shift(3) + UP * 1.3)
        b3_l2 = Tex("a rule nobody was told about controls nothing").scale(0.9).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = Tex("5. Monitoring — surprise counts, spot checks:").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        b3_l4 = Tex("controls decay when nobody watches").scale(0.9).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Tone set, risks asked, rules answer,").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        b3_l6 = Tex("information flows, monitoring proves").scale(0.95).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(VGroup(b3_l5, b3_l6), color=GREEN)))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): the working toolkit ---
        self.next_band(4)
        b4_title = Tex("Control activities — the toolkit").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Division of duties — no single master").scale(0.9).shift(band_shift(4) + UP * 1.4)
        b4_l2 = Tex("Authorisation — approval before money moves").scale(0.9).shift(band_shift(4) + UP * 0.6)
        b4_l3 = Tex("Documentation — numbered source documents").scale(0.9).shift(band_shift(4) + DOWN * 0.2)
        b4_l4 = Tex("Physical safeguards — locks, safes, registers").scale(0.9).shift(band_shift(4) + DOWN * 1.0)
        b4_l5 = Tex("Independent checks — records that must agree").scale(0.9).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2)
        b4_l6 = Tex("A gap in the number sequence").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        b4_l7 = Tex("asks its own question").scale(0.9).shift(band_shift(4) + DOWN * 3.5)
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): toolkit applied to three assets ---
        self.next_band(5)
        b5_title = Tex("The toolkit on three assets").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Cash: two count the till, banked daily,").scale(0.9).shift(band_shift(5) + UP * 1.3)
        b5_l2 = Tex("banker $\\neq$ recorder, vouchers for petty cash").scale(0.9).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex("Stock: counted against the delivery note").scale(0.9).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("by a non-orderer; locked; counted regularly").scale(0.9).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex("Fixed assets: register of item, cost, location;").scale(0.9).shift(band_shift(5) + DOWN * 2.1)
        b5_l6 = Tex("items marked; register checked physically").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): three-move answer, scenario one ---
        self.next_band(6)
        b6_title = Tex("Scenario: Zwane Building Supplies").scale(1.15).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("One clerk orders, receives, and pays").scale(0.95).shift(band_shift(6) + UP * 1.4)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("1. Weakness: no division of duties").scale(0.95).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("2. Risk: private orders, payment for").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("loads that never arrived — unseen").scale(0.95).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("3. Control: split order / receive / authorise,").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        b6_l6 = Tex("pay only against matched documents").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6_l2))
        self.wait(1.5)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(1.5)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(VGroup(b6_l2, b6_l3, b6_l4, b6_l5, b6_l6), color=GREEN)))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): scenario two and the worthless answer ---
        self.next_band(7)
        b7_title = Tex("Cash in a tin, banked when full").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Weakness: cash unbanked, unguarded").scale(0.95).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("Risk: theft, loss, deposits unverifiable").scale(0.95).shift(band_shift(7) + UP * 0.3)
        b7_l3 = Tex("Control: bank daily and intact, reconcile").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("``The owner should supervise more closely''").scale(0.95).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l4))
        self.play(Create(strike(b7_l4)))
        self.wait(1.5)
        b7_l5 = Tex("Recommendations must be specific,").scale(0.95).shift(band_shift(7) + DOWN * 2.4)
        b7_l6 = Tex("actionable, aimed at the exact weakness").scale(0.95).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the tuck-shop disaster ---
        self.next_band(8)
        b8_title = Tex("The tuck-shop disaster").scale(1.2).shift(band_shift(8) + UP * 2.4)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("One learner: money, stock, float, memory").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("Friday: float short — nobody can KNOW").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=RED)))
        self.wait(2)
        b8_l3 = Tex("Replay: Zanele on cash, Bongani on stock,").scale(0.9).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("Karabo ticks sales, box counted by two").scale(0.9).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("Box matches sheet — honesty provable:").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        b8_l6 = Tex("not suspicion, PROTECTION").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): the five plain questions ---
        self.next_band(9)
        b9_title = Tex("Five plain questions").scale(1.2).shift(band_shift(9) + UP * 2.4)
        self.play(Write(b9_title))
        self.wait(1.5)
        b9_l1 = Tex("Who sets the example? — environment").scale(0.9).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex("What could go wrong? — risk assessment").scale(0.9).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex("What rules stop it? — control activities").scale(0.9).shift(band_shift(9) + DOWN * 0.3)
        b9_l4 = Tex("Does everyone know? — information").scale(0.9).shift(band_shift(9) + DOWN * 1.1)
        b9_l5 = Tex("Who checks the checkers? — monitoring").scale(0.9).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Example, dangers, rules, information, checking").scale(0.9).shift(band_shift(9) + DOWN * 2.8)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=YELLOW)))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): spot the weakness — three patrols ---
        self.next_band(10)
        b10_title = Tex("Spot the weakness — three patrols").scale(1.2).shift(band_shift(10) + UP * 2.4)
        self.play(Write(b10_title))
        self.wait(1.5)
        b10_l1 = Tex("Car wash Saturdays: one person, every role,").scale(0.9).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex("wages from uncounted cash — list, count, split").scale(0.9).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = Tex("Storeroom propped open: lock it; one person").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        b10_l4 = Tex("counts deliveries against the note").scale(0.9).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2)
        b10_l5 = Tex("Loose unnumbered receipts: numbered book —").scale(0.9).shift(band_shift(10) + DOWN * 2.1)
        b10_l6 = Tex("the sequence itself becomes the watchdog").scale(0.9).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(3.5)
