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

# Band-layout whiteboard scene for crj-format-columns-and-source-documents (Part 1 Expert
# subtopics 1-5, Part 2 Simplifier subtopics 6-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (270/210/180/180/190/160/130 of 1320 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class CrjFormatColumnsAndSourceDocumentsSession(MovingCameraScene):
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
        self.write_rows(0, "The cash receipts journal", [
            "Book of first entry for all money received",
            "Date order, from source documents",
            "Analyses receipts; totals posted monthly",
            "Partner journal: the CPJ",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "The columns", [
            "Doc, Day, Details, Fol",
            "Analysis of receipts; Bank",
            "Current income",
            "Sundry: amount, fol, details",
        ], box=3)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Source documents", [
            "Duplicate receipts",
            "Cash register roll (CRR)",
            "Bank statement (B/S): EFTs, loans, interest",
            "Deposit slip checks the bank total",
        ], box=2)

        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Analysing receipts", [
            "Which document? Which account credited?",
            "Capital, loan, rent, interest: sundry",
            "CRR and receipts: current income",
            "Combined deposit: R3 600 + R900 = R4 500",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Conventions", [
            "Ink; corrections with one neat line",
            "No R sign; spaces for thousands",
            "Journal number CRJ 3 is the folio",
            "Single line above totals, double below",
        ], box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_6)
        self.next_band(5)
        self.write_rows(5, "A notebook with lanes", [
            "Bank lane: every receipt",
            "Current income lane: money earned",
            "Sundry lane: name tags",
            "Two lanes: the double entry",
        ], box=3)

        # --- Band 6 (subtopic_7)
        self.next_band(6)
        self.write_rows(6, "The end-of-day pile", [
            "Receipt copies: one line each",
            "Till roll: one line, CRR",
            "Deposit slip: the check",
            "Bank statement at month-end: B/S",
        ], box=2)

        self.wait(4)
