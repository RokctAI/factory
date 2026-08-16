# Copyright (c) 2026 RokctAI
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# Band-layout whiteboard scene for "Internal Control Basics" (grade10 term1,
# internal-control-ethics-gaap). One band per teaching beat, add-only
# lifecycle, camera moves down between bands. Exporter-safe mobjects only
# (Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup).
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
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(13)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definition and the four objectives ---
        title = Tex("Internal Control Basics").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Policies, procedures and checks that:").scale(1.05).shift(UP * 1.2)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex("1. safeguard assets").scale(1.05).shift(UP * 0.4)
        b0_l3 = Tex("2. keep records accurate and reliable").scale(1.05).shift(DOWN * 0.4)
        b0_l4 = Tex("3. promote efficient operations").scale(1.05).shift(DOWN * 1.2)
        b0_l5 = Tex("4. encourage adherence to policies").scale(1.05).shift(DOWN * 2.0)
        self.play(Write(b0_l2))
        self.wait(1.5)
        self.play(Write(b0_l3))
        self.wait(1.5)
        self.play(Write(b0_l4))
        self.wait(1.5)
        self.play(Write(b0_l5))
        self.play(Create(SurroundingRectangle(VGroup(b0_l2, b0_l3, b0_l4, b0_l5), color=GREEN)))
        self.wait(2)
        b0_l6 = Tex("Against: errors, fraud, waste").scale(1.05).shift(DOWN * 3.0)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): division of duties ---
        self.next_band(1)
        b1_title = Tex("Division of duties").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("No single person controls a transaction").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex("from beginning to end").scale(1.05).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex("Receives cash $\\neq$ records cash").scale(1.05).shift(band_shift(1) + DOWN * 0.6)
        b1_l4 = Tex("Orders stock $\\neq$ receives and pays").scale(1.05).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_l3))
        self.wait(2)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex("Fraud must pass a second pair of eyes").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        b1_l6 = Tex("Trust in people becomes trust in a SYSTEM").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l5))
        self.wait(2)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): components 1-3 ---
        self.next_band(2)
        b2_title = Tex("The five components (1--3)").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("1. Control environment -- tone at the top;").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex("the soil every control grows in").scale(1.0).shift(band_shift(2) + UP * 0.3)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("2. Risk assessment -- ask deliberately:").scale(1.0).shift(band_shift(2) + DOWN * 0.6)
        b2_l4 = Tex("what can go wrong here?").scale(1.0).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex("3. Control activities -- the concrete").scale(1.0).shift(band_shift(2) + DOWN * 2.3)
        b2_l6 = Tex("rules and checks answering the risks").scale(1.0).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): components 4-5 + the flowing sentence ---
        self.next_band(3)
        b3_title = Tex("The five components (4--5)").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("4. Information and communication --").scale(1.0).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("a rule nobody was told controls nothing").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("5. Monitoring -- spot checks, surprise").scale(1.0).shift(band_shift(3) + DOWN * 0.6)
        b3_l4 = Tex("counts: controls decay unwatched").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex("Tone, risks, rules, information,").scale(1.05).shift(band_shift(3) + DOWN * 2.3)
        b3_l6 = Tex("and proof it all still works").scale(1.05).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(VGroup(b3_l5, b3_l6), color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the control activities toolkit ---
        self.next_band(4)
        b4_title = Tex("Control activities -- the toolkit").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Division of duties -- no single master").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("Authorisation -- approval before money moves").scale(1.0).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex("Documentation -- numbered source documents;").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex("a missing number asks its own question").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex("Physical safeguards -- safes, locks, registers").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        b4_l6 = Tex("Independent checks -- two records must agree").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l1))
        self.wait(1.5)
        self.play(Write(b4_l2))
        self.wait(1.5)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(1.5)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): the toolkit applied to the three assets ---
        self.next_band(5)
        b5_title = Tex("Applied: cash, stock, fixed assets").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Cash: two count the till together;").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("banked daily; banker $\\neq$ recorder").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Stock: deliveries checked by a non-orderer;").scale(1.0).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = Tex("stockroom locked; counts vs records").scale(1.0).shift(band_shift(5) + DOWN * 1.4)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("Fixed assets: an asset register, items").scale(1.0).shift(band_shift(5) + DOWN * 2.3)
        b5_l6 = Tex("marked, register checked physically").scale(1.0).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three-move answer, scenario one ---
        self.next_band(6)
        b6_title = Tex("Scenario: one employee orders,").scale(1.15).shift(band_shift(6) + UP * 2.3)
        b6_title2 = Tex("receives AND pays").scale(1.15).shift(band_shift(6) + UP * 1.6)
        self.play(Write(b6_title))
        self.play(Write(b6_title2))
        self.wait(2)
        b6_l1 = Tex("1. Weakness: no division of duties --").scale(1.0).shift(band_shift(6) + UP * 0.7)
        b6_l2 = Tex("one person owns the purchasing cycle").scale(1.0).shift(band_shift(6) + DOWN * 0.1)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("2. Risk: private orders, payments for").scale(1.0).shift(band_shift(6) + DOWN * 0.9)
        b6_l4 = Tex("goods never delivered -- unnoticed").scale(1.0).shift(band_shift(6) + DOWN * 1.7)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex("3. Control: split order / receive / pay;").scale(1.0).shift(band_shift(6) + DOWN * 2.5)
        b6_l6 = Tex("owner authorises against matched documents").scale(0.95).shift(band_shift(6) + DOWN * 3.2)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(VGroup(b6_l5, b6_l6), color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): scenario two + the worthless answer ---
        self.next_band(7)
        b7_title = Tex("Scenario: cash banked ``when").scale(1.15).shift(band_shift(7) + UP * 2.3)
        b7_title2 = Tex("there is time''").scale(1.15).shift(band_shift(7) + UP * 1.6)
        self.play(Write(b7_title))
        self.play(Write(b7_title2))
        self.wait(2)
        b7_l1 = Tex("Weakness: cash not banked promptly").scale(1.0).shift(band_shift(7) + UP * 0.7)
        b7_l2 = Tex("Risk: theft, loss, deposits uncheckable").scale(1.0).shift(band_shift(7) + DOWN * 0.1)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_w = Tex("``The owner must be more careful''").scale(1.0).shift(band_shift(7) + DOWN * 1.0)
        self.play(Write(b7_w))
        self.play(Create(strike(b7_w)))
        self.wait(2)
        b7_l3 = Tex("Control: bank daily and intact;").scale(1.0).shift(band_shift(7) + DOWN * 1.9)
        b7_l4 = Tex("reconcile deposits with the cash journal").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(VGroup(b7_l3, b7_l4), color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the tuck-shop disaster ---
        self.next_band(8)
        b8_title = Tex("The tuck-shop disaster").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Sipho does everything: money, chips,").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("float in his pocket, records ``later''").scale(1.05).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Friday: float short. Thief? NOBODY").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        b8_l4 = Tex("CAN KNOW -- not even Sipho").scale(1.05).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Replay: Ayanda takes cash, Sipho hands").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        b8_l6 = Tex("stock, Lerato ticks; two count the box").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(VGroup(b8_l5, b8_l6), color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): five plain questions ---
        self.next_band(9)
        b9_title = Tex("Five questions every business answers").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Who sets the example? $\Rightarrow$ environment").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex(r"What could go wrong? $\Rightarrow$ risk assessment").scale(1.0).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex(r"What rules stop it? $\Rightarrow$ control activities").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex(r"Does everyone know? $\Rightarrow$ information").scale(1.0).shift(band_shift(9) + DOWN * 1.2)
        b9_l5 = Tex(r"Who checks the rules? $\Rightarrow$ monitoring").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l1))
        self.wait(1.5)
        self.play(Write(b9_l2))
        self.wait(1.5)
        self.play(Write(b9_l3))
        self.wait(1.5)
        self.play(Write(b9_l4))
        self.wait(1.5)
        self.play(Write(b9_l5))
        self.wait(2)
        b9_l6 = Tex("Example, dangers, rules, info, checking").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): spot the weakness, three patrols ---
        self.next_band(10)
        b10_title = Tex("Spot the weakness -- on patrol").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Nephew alone, wages from the tin:").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("notebook, counted float, owner pays").scale(1.0).shift(band_shift(10) + UP * 0.3)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex("Storeroom open on delivery days:").scale(1.0).shift(band_shift(10) + DOWN * 0.6)
        b10_l4 = Tex("lock it; one named receiver counts").scale(1.0).shift(band_shift(10) + DOWN * 1.4)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex("Unnumbered receipts ``on request'':").scale(1.0).shift(band_shift(10) + DOWN * 2.2)
        b10_l6 = Tex("numbered receipts, every sale").scale(1.0).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l5))
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
