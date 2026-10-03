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

# Band-layout whiteboard scene for government-revenue-direct-and-indirect-tax (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (280/210/180/200/150/180/150 of 1350 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class GovernmentRevenueDirectAndIndirectTaxSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.78, box=None):
        t = Tex(title).scale(1.1).shift(band_shift(k) + UP * 2.4)
        self.play(Write(t))
        self.wait(1.5)
        made = []
        for i, r in enumerate(rows):
            m = Tex(r).scale(scale).shift(band_shift(k) + UP * (1.3 - 0.95 * i))
            self.play(Write(m))
            self.wait(2.3)
            made.append(m)
        if box is not None:
            self.play(Create(SurroundingRectangle(made[box], color=YELLOW)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1)
        self.write_rows(0, "The national budget", [
            "Plan of revenue and expenditure: 1 April to 31 March",
            "Presented in February; passed by Parliament",
            "Deficit: spending greater than revenue",
            "Revenue: tax, non-tax, borrowing, grants",
        ], box=2)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Direct taxes", [
            "Paid by the taxpayer on own income or wealth",
            "Personal income tax via PAYE: 18\\% to 45\\%",
            "18\\% x R200 000 = R36 000; - R17 235 = R18 765",
            "Company tax 27\\%; dividends tax 20\\%",
        ], box=2)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Indirect taxes", [
            "On goods and services; passed on in price",
            "VAT 15\\%: R400 + R60 = R460",
            "VAT inside R230: x 15/115 = R30",
            "Excise, fuel levy, customs duties",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Who carries the burden", [
            "Progressive: share rises with income",
            "Proportional: same share for all",
            "Regressive: poorer pay a larger share",
            "VAT: about 13\\% vs 6,5\\% of income",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Tax compliance", [
            "More spending: tax, borrow or cut",
            "Narrow tax base",
            "Avoidance: legal",
            "Evasion: illegal",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Payslip and till slip", [
            "Payslip: PAYE, a direct tax",
            "Till slip: VAT, an indirect tax",
            "Who hands the money to SARS?",
            "R200 + 15\\% = R230",
        ], box=2)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Who feels the tax more", [
            "Same 15\\% VAT, different bite",
            "Income tax: progressive",
            "Company tax: proportional",
            "No VAT on maize meal, bread, milk",
        ], box=0)

        self.wait(4)
