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

# Band-layout whiteboard scene for cpj-format-columns-and-source-documents (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (280/190/170/200/150/110/140 of 1240 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CpjFormatColumnsAndSourceDocumentsSession(MovingCameraScene):
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
        self.write_rows(0, "Purpose of the CPJ", [
            "Book of first entry for money out",
            "Expenses, assets, loans, drawings",
            "Records, analyses, saves posting",
            "Partner of the CRJ",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Columns of the CPJ", [
            "Doc, Day, Payee, Fol",
            "Bank: credited to bank",
            "Analysis: wages, repair parts",
            "Sundry: amount, folio, details",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Source documents", [
            "EFT payment confirmation",
            "Supplier's invoice or till slip",
            "Bank statement: charges, debit orders",
            "Payslip; counterfoil is historical",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "April payments", [
            "Parts: R2 340 and R1 860",
            "Wages: R3 000 twice",
            "Drawings and equipment: sundry",
            "Bank charges and insurance: B/S",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Totalling and checking", [
            "Wages R6 000, parts R4 200",
            "Sundry R15 125",
            "Bank R25 325: cross-cast agrees",
            "Bank balance up R6 005",
        ], box=2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "Notebook for money out", [
            "One line per payment",
            "Write it twice",
            "Named lanes for frequent items",
            "Sundry with a name",
        ], box=1)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "The payment pile", [
            "EFT proofs and slips",
            "Bank statement surprises",
            "Drawings are not wages",
            "A tool is an asset",
        ], box=1)

        self.wait(4)
