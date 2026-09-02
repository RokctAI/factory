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

# Band-layout whiteboard scene for "Corporate Governance and Ethics"
# (grade 12, term 1, companies). One band per teaching beat; the camera
# moves down and nothing is removed. Part 1 (Expert) = subtopics 1-4,
# Part 2 (Simplifier) = subtopics 5-7. Exporter-safe primitives only;
# write-only reveals. Subtopic durations 230/235/235/225/190/195/190 of
# 1500 s guide the apportioning. Scenarios follow Masakhane Limited and
# the Sondela Netball Club.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CorporateGovernanceAndEthicsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): owners vs runners ---
        title = Tex("Corporate Governance and Ethics").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Shareholders OWN: vote at the AGM,").scale(0.95).shift(UP * 1.3)
        b0_l2 = Tex("elect and remove, appoint the auditor").scale(0.95).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex("Directors RUN — on the owners' behalf:").scale(0.95).shift(DOWN * 0.3)
        b0_l4 = Tex("fiduciary duty: good faith, company first,").scale(0.9).shift(DOWN * 1.0)
        b0_l5 = Tex("no private gain, interests declared").scale(0.9).shift(DOWN * 1.7)
        self.play(Write(b0_l3))
        self.wait(2)
        self.play(Write(b0_l4))
        self.play(Write(b0_l5))
        self.wait(2.5)
        b0_l6 = Tex("Dividends: declared when affordable —").scale(0.9).shift(DOWN * 2.6)
        b0_l7 = Tex("never guaranteed").scale(0.9).shift(DOWN * 3.3)
        self.play(Write(b0_l6))
        self.play(Write(b0_l7))
        self.wait(3)

        # --- Band 1 (subtopic_1): the board's structure ---
        self.next_band(1)
        b1_t = Tex("The board's anatomy").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(2)
        b1_l1 = Tex("Executive: inside daily (CEO, FD)").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("Non-executive: outside oversight").scale(0.95).shift(band_shift(1) + UP * 0.4)
        b1_l3 = Tex("Independent NED: no other financial ties").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_trap = Tex("Chairperson $=$ chief executive?").scale(0.95).shift(band_shift(1) + DOWN * 1.4)
        self.play(Write(b1_trap))
        self.play(Create(strike(b1_trap)))
        self.wait(2)
        b1_l4 = Tex("Chair leads the BOARD; CEO leads the").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        b1_l5 = Tex("COMPANY — divide the power").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(3)

        # --- Band 2 (subtopic_2): the King Code's four demands ---
        self.next_band(2)
        b2_t = Tex("King IV: four demands").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(2)
        b2_l1 = Tex("Code of practice, not an Act —").scale(0.95).shift(band_shift(2) + UP * 1.2)
        b2_l2 = Tex("JSE-listed: apply and explain").scale(0.95).shift(band_shift(2) + UP * 0.5)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex("RESPONSIBILITY: take charge, repair, not hide").scale(0.85).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex("ACCOUNTABILITY: everyone answers to somebody").scale(0.85).shift(band_shift(2) + DOWN * 1.1)
        b2_l5 = Tex("FAIRNESS: all stakeholders weighed").scale(0.85).shift(band_shift(2) + DOWN * 1.8)
        b2_l6 = Tex("TRANSPARENCY: bad news reported with good").scale(0.85).shift(band_shift(2) + DOWN * 2.5)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(2)
        self.play(Write(b2_l5))
        self.play(Write(b2_l6))
        self.wait(2.5)
        b2_l7 = Tex("Diagnosis is the skill: name the demand broken").scale(0.85).shift(band_shift(2) + DOWN * 3.4)
        self.play(Write(b2_l7))
        self.wait(3)

        # --- Band 3 (subtopic_2): committees turn words into structures ---
        self.next_band(3)
        b3_t = Tex("Words become structures").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(2)
        b3_l1 = Tex("AUDIT COMMITTEE (independent NEDs):").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("oversees reporting, receives internal audit,").scale(0.9).shift(band_shift(3) + UP * 0.5)
        b3_l3 = Tex("guards the external auditor's independence").scale(0.9).shift(band_shift(3) + DOWN * 0.2)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("REMUNERATION COMMITTEE: sets directors' pay").scale(0.9).shift(band_shift(3) + DOWN * 1.1)
        b3_l5 = Tex("so directors never set their own —").scale(0.9).shift(band_shift(3) + DOWN * 1.8)
        b3_l6 = Tex("then disclosed, director by director").scale(0.9).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): the five ethics principles ---
        self.next_band(4)
        b4_t = Tex("Five principles of conduct").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(2)
        b4_l1 = Tex("INTEGRITY: no massaged figures").scale(0.9).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("OBJECTIVITY: no bias or pressure rules").scale(0.9).shift(band_shift(4) + UP * 0.5)
        b4_l3 = Tex("COMPETENCE and DUE CARE: skills current").scale(0.9).shift(band_shift(4) + DOWN * 0.2)
        b4_l4 = Tex("CONFIDENTIALITY: never a shield for crime").scale(0.9).shift(band_shift(4) + DOWN * 0.9)
        b4_l5 = Tex("PROFESSIONAL BEHAVIOUR: obey the law").scale(0.9).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4_l1))
        self.wait(2)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.wait(2)
        self.play(Write(b4_l4))
        self.play(Write(b4_l5))
        self.wait(2.5)
        b4_l6 = Tex("January sales moved into December?").scale(0.9).shift(band_shift(4) + DOWN * 2.5)
        self.play(Write(b4_l6))
        self.play(Create(strike(b4_l6)))
        b4_l7 = Tex("integrity refuses: no longer fairly presents").scale(0.85).shift(band_shift(4) + DOWN * 3.3)
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): conflicts and share dealing ---
        self.next_band(5)
        b5_t = Tex("Conflicts and share dealing").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(2)
        b5_l1 = Tex("Brother bids for the contract: DECLARE,").scale(0.9).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("WITHDRAW, let the rest decide on merit").scale(0.9).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Buying before the good news is public:").scale(0.9).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex("INSIDER TRADING — illegal, both directions").scale(0.9).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=RED)))
        self.wait(2)
        b5_l5 = Tex("False rumours / staged trades to move price:").scale(0.85).shift(band_shift(5) + DOWN * 2.0)
        b5_l6 = Tex("MANIPULATION — its twin offence").scale(0.9).shift(band_shift(5) + DOWN * 2.7)
        b5_l7 = Tex("Consequence: dismissal, prosecution, expulsion").scale(0.85).shift(band_shift(5) + DOWN * 3.4)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(2)
        self.play(Write(b5_l7))
        self.wait(3)

        # --- Band 6 (subtopic_4): three layers of checking ---
        self.next_band(6)
        b6_t = Tex("Three layers of checking").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(2)
        b6_l1 = Tex("1. INTERNAL CONTROL: divided duties,").scale(0.9).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("authorisation, documents, safeguards,").scale(0.9).shift(band_shift(6) + UP * 0.5)
        b6_l3 = Tex("reconciliation — directors responsible").scale(0.9).shift(band_shift(6) + DOWN * 0.2)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Write(b6_l3))
        self.wait(2.5)
        b6_l4 = Tex("2. INTERNAL AUDIT: tests controls all year,").scale(0.9).shift(band_shift(6) + DOWN * 1.1)
        b6_l5 = Tex("reports to the AUDIT COMMITTEE").scale(0.9).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex("3. INDEPENDENT AUDIT: appointed by and").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        b6_l7 = Tex("reporting to the SHAREHOLDERS").scale(0.9).shift(band_shift(6) + DOWN * 3.3)
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.play(Create(SurroundingRectangle(b6_l7, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_5): the club and its committee ---
        self.next_band(7)
        b7_t = Tex("Sondela Netball Club").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(2)
        b7_l1 = Tex("150 members OWN the club; once a year").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("they elect a committee of seven to RUN it").scale(0.9).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("Members keep: votes, the report-back,").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex("hard questions, the outside checker").scale(0.9).shift(band_shift(7) + DOWN * 1.1)
        b7_l5 = Tex("Committee gets: fixtures, kit, the bank card").scale(0.9).shift(band_shift(7) + DOWN * 1.8)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.wait(2.5)
        b7_l6 = Tex("The treasurer's rand is not the treasurer's —").scale(0.85).shift(band_shift(7) + DOWN * 2.7)
        b7_l7 = Tex("held on 150 people's behalf: fiduciary duty").scale(0.85).shift(band_shift(7) + DOWN * 3.4)
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.wait(3)

        # --- Band 8 (subtopic_6): house rules and the kit contract ---
        self.next_band(8)
        b8_t = Tex("House rules that keep money clean").scale(1.05).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex("Responsibility: kit counted, money banked").scale(0.85).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex("Accountability: every rand explained yearly").scale(0.85).shift(band_shift(8) + UP * 0.5)
        b8_l3 = Tex("Fairness: under-14s matter like the first team").scale(0.85).shift(band_shift(8) + DOWN * 0.2)
        b8_l4 = Tex("Transparency: bad months reported too").scale(0.85).shift(band_shift(8) + DOWN * 0.9)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_trap = Tex("Zanele orders kit from her sister — no quotes").scale(0.85).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_trap))
        self.play(Create(strike(b8_trap)))
        self.wait(2)
        b8_l5 = Tex("Repair: declare, step out, three quotes,").scale(0.85).shift(band_shift(8) + DOWN * 2.7)
        b8_l6 = Tex("minute the choice — clean, even if she wins").scale(0.85).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8_l5))
        self.play(Write(b8_l6))
        self.wait(3)

        # --- Band 9 (subtopic_7): who checks the checkers ---
        self.next_band(9)
        b9_t = Tex("Who checks the checkers?").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex("Habits: two signatures; counter, recorder,").scale(0.9).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("banker all different; receipts for everything").scale(0.85).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Karabo checks all year, reports to the").scale(0.9).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex("oversight group $=$ internal audit").scale(0.9).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.wait(2.5)
        b9_l5 = Tex("Outside accountant, chosen by the MEMBERS,").scale(0.85).shift(band_shift(9) + DOWN * 2.0)
        b9_l6 = Tex("answers to the members $=$ independent audit").scale(0.85).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5))
        self.play(Write(b9_l6))
        self.wait(2.5)
        b9_l7 = Tex("PROBLEM $\\to$ PRINCIPLE $\\to$ REMEDY").scale(1.0).shift(band_shift(9) + DOWN * 3.5)
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(4)
