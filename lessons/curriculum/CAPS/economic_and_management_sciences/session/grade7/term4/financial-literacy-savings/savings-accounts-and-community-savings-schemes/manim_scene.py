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

# Band-layout whiteboard scene for savings-accounts-and-community-savings-schemes (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-5). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (210/200/220/110/150 of 890 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class SavingsAccountsAndCommunitySavingsSchemesSession(MovingCameraScene):
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
        self.write_rows(0, "Opening a savings account", [
            "ID or birth certificate",
            "Proof of address (FICA)",
            "Minor: parent or guardian helps",
            "Choose account, deposit, get card or app",
        ], box=1)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Community savings schemes", [
            "Stokvel: regular contributions, rotating payout",
            "Grocery stokvel: bulk buying in December",
            "Burial society: funeral costs",
            "Built on trust, rules and meetings",
        ], box=0)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Bank versus community scheme", [
            "Bank: safe, regulated, earns interest",
            "Stokvel: discipline, support, lump sums",
            "Risks: theft, broken trust, no insurance",
            "Best: stokvel money in a bank account",
        ], box=3)


        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Ayanda opens her first account", [
            "Bring: birth certificate, Mom's ID",
            "Proof of address: municipal account",
            "Choose a youth savings account",
            "Deposit R50, set a secret PIN",
        ], box=3)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Mama's stokvel", [
            "12 members, R500 each a month",
            "Each month one member gets R6 000",
            "Rules, records, two signatures",
            "Money kept in a stokvel bank account",
        ], box=1)

        self.wait(4)
