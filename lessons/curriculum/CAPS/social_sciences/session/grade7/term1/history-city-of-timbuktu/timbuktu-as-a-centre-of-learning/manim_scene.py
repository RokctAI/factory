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

# Band-layout whiteboard scene for timbuktu-as-a-centre-of-learning (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (160/170/170/190/90/90/90 of 960 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class TimbuktuAsACentreOfLearningSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
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
            self.play(Create(SurroundingRectangle(made[box], color=box_color)))
            self.wait(2)
        return made

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0: How Trade Built Learning
        self.write_rows(0, "How Trade Built Learning", [
            "Trade wealth paid for books and teachers",
            "Islam brought Arabic literacy",
            "Rulers honoured scholars",
            "Links to Fez, Cairo and Mecca",
        ], scale=0.86, box=1)
        # --- Band 1: Mosques, Teachers and Students
        self.next_band(1)
        self.write_rows(1, "Mosques, Teachers and Students", [
            "Sankore, Djinguereber, Sidi Yahya",
            "Quranic school, then study with masters",
            "Ijaza: permission to teach a book",
            "Graduates spread learning across West Africa",
        ], scale=0.86, box=2)
        # --- Band 2: What Scholars Studied
        self.next_band(2)
        self.write_rows(2, "What Scholars Studied", [
            "Islam, law and advice to rulers",
            "Maths for trade and inheritance",
            "Astronomy for prayer times and calendars",
            "Medicine, history, geography, poetry",
        ], scale=0.86, box=1)
        # --- Band 3: Ahmad Baba and the Meaning of Timbuktu
        self.next_band(3)
        self.write_rows(3, "Ahmad Baba and the Meaning of Timbuktu", [
            "Ahmad Baba, born 1556: jurist and author",
            "1591: Moroccan army defeats Songhay",
            "Scholars deported to Marrakesh, 1593",
            "Manuscripts disprove 'Africa had no history'",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: A City of Books
        self.next_band(4)
        self.write_rows(4, "A City of Books", [
            "Rich families paid for books",
            "Kings respected scholars",
            "Over 150 schools",
        ], scale=0.86, box=0)
        # --- Band 5: How Students Learned
        self.next_band(5)
        self.write_rows(5, "How Students Learned", [
            "Wooden boards, then masters",
            "Ijaza: you may teach this book",
            "Law, maths, stars, medicine, history",
        ], scale=0.86, box=0)
        # --- Band 6: Ahmad Baba
        self.next_band(6)
        self.write_rows(6, "Ahmad Baba", [
            "Ahmad Baba, born 1556",
            "1591: Moroccan guns",
            "A library named after him today",
        ], scale=0.86, box=0)
        self.wait(4)
