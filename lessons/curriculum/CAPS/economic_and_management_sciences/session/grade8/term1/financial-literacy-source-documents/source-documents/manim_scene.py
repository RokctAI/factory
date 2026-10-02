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

# Band-layout whiteboard scene for source-documents (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (290/180/200/200/180/180/150 of 1380 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SourceDocumentsSession(MovingCameraScene):
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
        self.write_rows(0, "Why source documents", [
            "First written evidence of a transaction",
            "Basis for recording; proof; control",
            "Keep for five years (SARS)",
            "Issuer keeps duplicate; receiver keeps original",
        ], box=3)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Receipts and till slips", [
            "Receipt: proof money was received",
            "Original to payer; duplicate kept: CRJ",
            "Till slip to customer",
            "Cash register roll total: CRJ",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Deposit slips, EFTs, statements", [
            "Deposit slip: checks daily bank total",
            "EFT confirmation: CPJ for the payer",
            "Bank statement: charges, debit orders, direct deposits",
            "Check your own account, not a screenshot",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Cash invoices and tax invoices", [
            "Cash invoice: paid immediately",
            "Tax invoice: VAT number, serial number",
            "R800 + R200 = R1 000; VAT R150",
            "Total R1 150",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Matching documents to journals", [
            "CRJ: duplicate receipt, CRR, duplicate cash invoice",
            "CRJ: bank statement for deposits received",
            "CPJ: EFT confirmation, supplier's cash invoice",
            "CPJ: bank statement for charges and debit orders",
        ], box=0)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "The plumber's shoebox", [
            "Cash invoice copy and receipts: in",
            "Till roll: in",
            "EFT proof and cash slip: out",
            "Bank statement: everything",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "Top copy, bottom copy", [
            "Give it away: keep the bottom copy",
            "Receive it: keep the top copy",
            "Same paper, opposite direction",
            "No paper, no entry",
        ], box=0)

        self.wait(4)
