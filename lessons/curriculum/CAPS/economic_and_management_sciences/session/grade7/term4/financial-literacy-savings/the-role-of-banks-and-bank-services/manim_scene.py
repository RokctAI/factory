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

# Band-layout whiteboard scene for the-role-of-banks-and-bank-services (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-5). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (190/190/200/120/140 of 840 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TheRoleOfBanksAndBankServicesSession(MovingCameraScene):
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
        self.write_rows(0, "Banks as go-betweens", [
            "Accept deposits from savers",
            "Lend to borrowers",
            "Pay interest low, charge interest high",
            "Difference covers costs and profit",
        ], box=2)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Bank accounts and services", [
            "Transactional account: everyday payments",
            "Savings, fixed and notice deposits",
            "Loans: home, vehicle, personal, business",
            "Cards, EFTs, app banking, forex",
        ], box=0)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Interest, charges and choosing", [
            "Interest earned on savings",
            "Interest paid on loans and credit",
            "Bank charges: monthly and per transaction",
            "Compare fees, interest and convenience",
        ], box=2)


        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Where does my R1 000 go?", [
            "Gogo deposits R1 000: earns 5\\%",
            "Bank lends it to a baker at 12\\%",
            "Baker buys an oven, hires a worker",
            "Bank keeps the difference for costs",
        ], box=2)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Choose the right account", [
            "Saving: savings account",
            "Everyday payments: transactional",
            "Big goal, can wait: fixed deposit",
            "Watch the fees, check the statement",
        ], box=3)

        self.wait(4)
