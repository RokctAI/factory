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

# Band-layout whiteboard scene for "Reconciling Control Accounts with Lists"
# (grade10 term2, debtors-and-creditors-reconciliation). One band per teaching
# beat, add-only lifecycle, camera moves down between bands. Exporter-safe
# mobjects only (Tex/MathTex/Line/Rectangle/SurroundingRectangle/VGroup).
#
# Subtopic time shares (subtopics.json, total 1380 s):
# 210/230/210/180/180/190/180 -> bands 0-1 / 2-3 / 4-5 / 6 / 7 / 8 / 9.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ReconcilingControlAccountsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): two records, two journeys ---
        title = Tex("Reconciling Control and List").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Control account: built from JOURNAL").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("TOTALS, posted monthly").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2)
        b0_l3 = Tex("List of debtors: built from the PAGES,").scale(1.05).shift(DOWN * 0.5)
        b0_l4 = Tex("posted line by line, daily").scale(1.05).shift(DOWN * 1.3)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("Two journeys from the same documents:").scale(1.0).shift(DOWN * 2.2)
        b0_l6 = Tex("agreement certifies both").scale(1.05).shift(DOWN * 3.0)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.play(Create(SurroundingRectangle(b0_l6, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the three error families ---
        self.next_band(1)
        b1_title = Tex("Where did the error happen?").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"In a journal TOTAL $\Rightarrow$ control is wrong").scale(1.0).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex(r"In posting TO A PAGE $\Rightarrow$ list is wrong").scale(1.0).shift(band_shift(1) + UP * 0.3)
        b1_l3 = Tex(r"In the ORIGINAL LINE $\Rightarrow$ both are wrong").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.wait(2)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_w = Tex("``The control account is always right''").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1_w))
        self.play(Create(strike(b1_w)))
        self.wait(1.5)
        b1_ok = Tex("Only the evidence decides -- the truth is").scale(1.0).shift(band_shift(1) + DOWN * 2.4)
        b1_ok2 = Tex("where both, corrected, MEET").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_ok))
        self.play(Write(b1_ok2))
        self.play(Create(SurroundingRectangle(b1_ok2, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the debtors case, control side ---
        self.next_band(2)
        b2_title = Tex("Control R9 860, list R9 350: R510 out").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(2)
        b2_l1 = Tex("Finding 1: DJ sales column undercast").scale(1.0).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex(r"R300 -- totals journey $\Rightarrow$ debit control").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2)
        b2_m1 = MathTex(r"9\,860 + 300 = 10\,160").scale(1.1).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_m1))
        self.wait(2)
        b2_l3 = Tex("Finding 2: R260 write-off never reached").scale(1.0).shift(band_shift(2) + DOWN * 1.2)
        b2_l4 = Tex(r"control $\Rightarrow$ credit control R260").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2)
        b2_m2 = MathTex(r"10\,160 - 260 = 9\,900").scale(1.1).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_m2))
        self.wait(3)

        # --- Band 3 (subtopic_2): the list side, and the meeting ---
        self.next_band(3)
        b3_title = Tex("Now correct the list").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Finding 3: Pillay's R640 invoice never").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"posted to his page $\Rightarrow$ list up R640").scale(1.0).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2)
        b3_m1 = MathTex(r"9\,350 + 640 = 9\,990").scale(1.1).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_m1))
        self.wait(2)
        b3_l3 = Tex("Finding 4: Daniels' page shows R540 for").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        b3_l4 = Tex(r"a R450 invoice $\Rightarrow$ list down R90").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2)
        b3_m2 = MathTex(r"9\,990 - 90 = 9\,900").scale(1.1).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(b3_m2))
        self.play(Create(SurroundingRectangle(b3_m2, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the creditors mirror, worked ---
        self.next_band(4)
        b4_title = Tex("The creditors mirror").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Control R6 180 Cr; list R5 890").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("CPJ creditors column overcast R120:").scale(1.0).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex(r"too much debited $\Rightarrow$ credit control R120").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.wait(2)
        b4_m1 = MathTex(r"6\,180 + 120 = 6\,300").scale(1.1).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(b4_m1))
        self.wait(2)
        b4_l4 = Tex(r"Naidu's R410 invoice unposted $\Rightarrow$ list up").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        b4_m2 = MathTex(r"5\,890 + 410 = 6\,300").scale(1.1).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l4))
        self.play(Write(b4_m2))
        self.play(Create(SurroundingRectangle(b4_m2, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the supplier's statement ---
        self.next_band(5)
        b5_title = Tex("The supplier's statement").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Their record of our account, monthly,").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex("reconciled against their page in our books").scale(1.0).shift(band_shift(5) + UP * 0.3)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Timing: our payment in transit,").scale(1.05).shift(band_shift(5) + DOWN * 0.6)
        b5_l4 = Tex("their invoice not yet received").scale(1.05).shift(band_shift(5) + DOWN * 1.4)
        b5_l5 = Tex("-- or genuine errors, either side").scale(1.05).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(2)
        b5_l6 = Tex("Independent records, compared on schedule").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the method, compressed ---
        self.next_band(6)
        b6_title = Tex("The method, compressed").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("1. State both figures and the difference").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("2. Classify: totals road or pages road?").scale(1.0).shift(band_shift(6) + UP * 0.4)
        b6_l3 = Tex("3. Correct each record on its own side").scale(1.0).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex("4. Both statements end on the SAME figure").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        b6_l5 = Tex("5. Only that figure flows onward").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l1))
        self.wait(1.5)
        self.play(Write(b6_l2))
        self.wait(1.5)
        self.play(Write(b6_l3))
        self.wait(1.5)
        self.play(Write(b6_l4))
        self.wait(1.5)
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(2)
        b6_l6 = Tex("Difference div. by 9: transposition;").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        b6_l7 = Tex("by 2: wrong side; exact match: unposted").scale(0.95).shift(band_shift(6) + DOWN * 3.5)
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): two witnesses ---
        self.next_band(7)
        b7_title = Tex("Two witnesses, different stories").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("The line says R9 860; the pages R9 350").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("Do not pick a favourite witness --").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l3 = Tex("either road can carry a pothole").scale(1.05).shift(band_shift(7) + DOWN * 0.6)
        self.play(Write(b7_l2))
        self.play(Write(b7_l3))
        self.wait(2.5)
        b7_l4 = Tex("R510 proves an error exists;").scale(1.05).shift(band_shift(7) + DOWN * 1.5)
        b7_l5 = Tex("it does not say where").scale(1.05).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l4))
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex("Both corrected until they agree").scale(1.05).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): four potholes ---
        self.next_band(8)
        b8_title = Tex("Four potholes, each on its own road").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Short total: line up 300 $\Rightarrow$ 10 160").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"Missed write-off: line down 260 $\Rightarrow$ 9 900").scale(1.0).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"Pillay unposted: pages up 640 $\Rightarrow$ 9 990").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex(r"Daniels' digits danced: down 90 $\Rightarrow$ 9 900").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex("They meet at R9 900 -- the truth neither").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        b8_l6 = Tex("original answer contained").scale(1.0).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(VGroup(b8_l5, b8_l6), color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): the meeting in the middle ---
        self.next_band(9)
        b9_title = Tex("The meeting in the middle").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Tomorrow the shop acts on ONE number").scale(1.05).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Errors caught by routine, in the month --").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = Tex("mistakes get a one-month lifespan").scale(1.05).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex("Creditors: the same case in a mirror --").scale(1.0).shift(band_shift(9) + DOWN * 1.5)
        b9_l5 = Tex("re-derive every direction fresh").scale(1.05).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex("Case closed is month closed").scale(1.1).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(4)
