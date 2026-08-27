# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
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

# Band-layout whiteboard scene for the Grade 11 Term 2 duo
# "Financial Statements and Notes" (partnership statements).
# One band per teaching beat; camera moves down, nothing removed.
# Exporter-safe primitives only; statement faces and notes are built
# heading first, then posted line by line, totals last.
# Subtopic shares: 230/235/225/230/195/190/195 of 1500 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class FinancialStatementsNotesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): comprehensive income, top half ---
        title = Tex("Financial Statements and Notes").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("Statement of Comprehensive Income —").scale(1.0).shift(UP * 1.2)
        b0_l2 = Tex("FOR the year ended (a period, a film)").scale(1.0).shift(UP * 0.5)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"Sales 2 880 000 $-$ Cost of sales 1 800 000").scale(1.0).shift(DOWN * 0.4)
        self.play(Write(b0_l3))
        self.wait(2)
        b0_l4 = Tex("Gross profit R1 080 000").scale(1.05).shift(DOWN * 1.2)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = Tex("+ rent 45 600 + commission 26 400").scale(1.0).shift(DOWN * 2.1)
        b0_l6 = Tex("= gross operating income R1 152 000").scale(1.0).shift(DOWN * 2.9)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): expenses down to net profit ---
        self.next_band(1)
        b1_title = Tex("Down to the last line").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Less operating expenses R600 000:").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex("salaries 312 000, depreciation 66 000,").scale(0.95).shift(band_shift(1) + UP * 0.5)
        b1_l3 = Tex("deficit 3 400, provision adj 600, more").scale(0.95).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex("OPERATING PROFIT R552 000").scale(1.05).shift(band_shift(1) + DOWN * 1.0)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex(r"Less interest expense 24 000 $\Rightarrow$").scale(1.0).shift(band_shift(1) + DOWN * 1.8)
        b1_l6 = Tex("NET PROFIT FOR THE YEAR R528 000").scale(1.05).shift(band_shift(1) + DOWN * 2.6)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(2)
        b1_wrong = Tex("Partners' salaries in this statement?").scale(0.95).shift(band_shift(1) + DOWN * 3.3)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(3)

        # --- Band 2 (subtopic_2): financial position — the asset tower ---
        self.next_band(2)
        b2_title = Tex("Financial Position ON 28 Feb: assets").scale(1.1).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Fixed assets at carrying value 755 000").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex("Inventories 217 500; receivables:").scale(1.0).shift(band_shift(2) + UP * 0.4)
        b2_l3 = Tex(r"64 000 $-$ 3 200 = 60 800, + 3 100 + 1 900").scale(0.95).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(b2_l2))
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Cash: bank 134 600 + float 2 500").scale(1.0).shift(band_shift(2) + DOWN * 1.1)
        self.play(Write(b2_l4))
        self.wait(2)
        b2_l5 = Tex("Current assets 420 400").scale(1.0).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(b2_l5))
        self.wait(1.5)
        b2_l6 = Tex("TOTAL ASSETS R1 175 400").scale(1.05).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l6))
        self.play(Create(SurroundingRectangle(b2_l6, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the claims tower ---
        self.next_band(3)
        b3_title = Tex("Equity and liabilities").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Equity: capital 800 000 + current 89 800").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("= R889 800 (detail in the notes)").scale(1.0).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Non-current: loan 185 000, interest inside").scale(0.95).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Current: 94 200 + 2 300 + 4 100 = 100 600").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("TOTAL R1 175 400 — the towers match").scale(1.05).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l5))
        self.play(Create(SurroundingRectangle(b3_l5, color=GREEN)))
        self.wait(2)
        b3_l6 = Tex("Within 12 months = current; show NET values").scale(0.95).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): the fixed assets note ---
        self.next_band(4)
        b4_title = Tex("Note: fixed assets, class by class").scale(1.1).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Land and buildings 560 000 — no wear").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = Tex("Vehicles: 285 000; acc dep 114 000 + 57 000").scale(0.95).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex(r"= 171 000; carrying value R114 000").scale(0.95).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l2))
        self.play(Write(b4_l3))
        self.wait(2.5)
        b4_l4 = Tex(r"Equipment: 90 000 $-$ 9 000 wear = R81 000").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l4))
        self.wait(2.5)
        b4_l5 = Tex("560 000 + 114 000 + 81 000 = R755 000").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2)
        b4_l6 = Tex("Note reconciles; face concludes — to the rand").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_4): capital and current account notes ---
        self.next_band(5)
        b5_title = Tex("Notes: capital and current accounts").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Capital: 450 000 + 350 000 = 800 000 —").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("no movement; stillness is the message").scale(1.0).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex("Current accounts, per partner: opening,").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        b5_l4 = Tex("interest, salary, bonus, share, drawings").scale(0.95).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex("Closing: 48 100 + 41 700 = R89 800").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        self.play(Write(b5_l5))
        self.play(Create(SurroundingRectangle(b5_l5, color=GREEN)))
        self.wait(2)
        b5_l6 = Tex("The appropriation account, dressed for church").scale(0.95).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the principles behind the package ---
        self.next_band(6)
        b6_title = Tex("The principles, in words").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Historical cost — at what it cost").scale(1.0).shift(band_shift(6) + UP * 1.1)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex("Prudence — the provision, the counted stock").scale(1.0).shift(band_shift(6) + UP * 0.3)
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("Matching — each rand in its year").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        self.play(Write(b6_l3))
        self.wait(2)
        b6_l4 = Tex("Business entity; going concern;").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex("materiality — significant items stand alone").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.play(Create(SurroundingRectangle(b6_l5, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): highlights reel and team photo ---
        self.next_band(7)
        b7_title = Tex("The highlights reel and the team photo").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Reel = the whole season: FOR the year —").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"sales 2 880 000 down to profit 528 000").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(3)
        b7_l3 = Tex("Photo = one frozen day: ON 28 February —").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("owned R1 175 400, claimed R1 175 400").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(3)
        b7_l5 = Tex("Each is blind without the other").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        self.play(Write(b7_l5))
        self.wait(2)
        b7_l6 = Tex("Period gets FOR; moment gets ON — one mark").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3.5)

        # --- Band 8 (subtopic_6): the fine print ---
        self.next_band(8)
        b8_title = Tex("The fine print that shows the workings").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Scoreboard: fixed assets R755 000").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8_l1))
        self.wait(2.5)
        b8_l2 = Tex("Service logbook: 560 000 + 114 000 + 81 000").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("The note climbs exactly to the face figure").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex(r"Debtors: not 64 000 but 60 800 —").scale(1.0).shift(band_shift(8) + DOWN * 1.5)
        b8_l5 = Tex("dimmed by the R3 200 provision").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(3)
        b8_l6 = Tex("Face = conclusion; note = proof").scale(1.0).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(b8_l6))
        self.wait(3.5)

        # --- Band 9 (subtopic_7): the partners' pages ---
        self.next_band(9)
        b9_title = Tex("The partners' pages").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Planted: 450 000 and 350 000 — no movement").scale(0.95).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex(r"Venter's tab: $-$6 800 + 31 500 + 168 000").scale(0.95).shift(band_shift(9) + UP * 0.3)
        b9_l3 = Tex(r"+ 12 000 + 54 000 $-$ 217 000 = R41 700").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)
        b9_l4 = Tex("Ngcobo closes at 48 100; together 89 800").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        b9_l5 = Tex("— straight onto the photo, inside equity").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(3)
        b9_l6 = Tex("Cost, prudence, matching, entity — name them").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l6))
        self.wait(4)
