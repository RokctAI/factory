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

# Band-layout whiteboard scene for improved-healthcare (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/170/150/160/90/90/90 of 900 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class ImprovedHealthcareSession(MovingCameraScene):
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
        # --- Band 0: What Healthcare Includes
        self.write_rows(0, "What Healthcare Includes", [
            "Primary: clinics and community health workers",
            "Secondary: district and regional hospitals",
            "Tertiary: large specialist hospitals",
            "Public health protects whole populations",
        ], scale=0.8, box=1)
        # --- Band 1: Mothers, Babies and Young Children
        self.next_band(1)
        self.write_rows(1, "Mothers, Babies and Young Children", [
            "Antenatal care during pregnancy",
            "Skilled birth with a midwife or nurse",
            "Free immunisation: measles, polio, rotavirus",
            "Road to Health booklet tracks growth",
        ], scale=0.86, box=3)
        # --- Band 2: Family Planning and Healthcare's Effect on Births
        self.next_band(2)
        self.write_rows(2, "Family Planning and Healthcare's Effect on Births", [
            "Family planning: choose if and when",
            "Free contraception at public clinics",
            "Child survival leads to smaller families",
            "SA fertility: about 6 then, 2.3 now",
        ], scale=0.86, box=3)
        # --- Band 3: Healthcare in South Africa: Progress and Challenges
        self.next_band(3)
        self.write_rows(3, "Healthcare in South Africa: Progress and Challenges", [
            "1994: free care for pregnant women, under-6s",
            "1996: free primary healthcare at clinics",
            "About 80 percent use public health",
            "Challenges: staff, queues, lifestyle disease",
        ], scale=0.86, box=3)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: Clinics and Hospitals
        self.next_band(4)
        self.write_rows(4, "Clinics and Hospitals", [
            "Clinic: first stop",
            "Hospital: operations and very sick people",
            "Special hospitals: complicated care",
        ], scale=0.86, box=0)
        # --- Band 5: Mothers and Babies
        self.next_band(5)
        self.write_rows(5, "Mothers and Babies", [
            "Check-ups and safe births",
            "Free vaccines for children",
            "Free family planning",
        ], scale=0.86, box=0)
        # --- Band 6: Healthcare in South Africa
        self.next_band(6)
        self.write_rows(6, "Healthcare in South Africa", [
            "1996: free clinic care for all",
            "ARVs raised life expectancy",
            "Still: queues, few staff, diabetes",
        ], scale=0.86, box=0)
        self.wait(4)
