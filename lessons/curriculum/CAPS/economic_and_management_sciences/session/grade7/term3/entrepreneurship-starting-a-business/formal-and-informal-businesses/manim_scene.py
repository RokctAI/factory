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

# Band-layout whiteboard scene for formal-and-informal-businesses (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-5). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to
# subtopics.json (160/210/180/130/120 of 800 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class FormalAndInformalBusinessesSession(MovingCameraScene):
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
        self.write_rows(0, "Formal businesses", [
            "Registered with CIPC and SARS",
            "Pay tax, follow labour laws",
            "Fixed premises, records, bank accounts",
            "Easier to get loans and contracts",
        ], box=0)

        # --- Band 1 (subtopic_2)
        self.next_band(1)
        self.write_rows(1, "Informal businesses", [
            "Not registered, few records",
            "Street traders, spaza, home salons",
            "Easy to start, little capital",
            "Insecure, no loans, little protection",
        ], box=1)

        # --- Band 2 (subtopic_3)
        self.next_band(2)
        self.write_rows(2, "Ideas from needs and wants", [
            "Every business meets a need or want",
            "Spot problems people face",
            "Ask: will people pay for this?",
            "Needs: steady demand; wants: choice",
        ], box=0)


        # ============ Part 2 — Simplifier ============
        # --- Band 3 (subtopic_4)
        self.next_band(3)
        self.write_rows(3, "Supermarket and fruit stand", [
            "Supermarket: registered, pays tax, many staff",
            "Fruit stand: not registered, cash only",
            "Supermarket: loans, contracts, UIF",
            "Fruit stand: easy start, flexible, insecure",
        ], box=1)

        # --- Band 4 (subtopic_5)
        self.next_band(4)
        self.write_rows(4, "Start from a need", [
            "See a problem",
            "Ask: will people pay?",
            "Check: who else sells it?",
            "Start small and listen",
        ], box=1)

        self.wait(4)
