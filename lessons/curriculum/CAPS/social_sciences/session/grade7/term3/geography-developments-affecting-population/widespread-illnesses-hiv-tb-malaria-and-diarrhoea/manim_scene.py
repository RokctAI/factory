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

# Band-layout whiteboard scene for widespread-illnesses-hiv-tb-malaria-and-diarrhoea (Part 1 Expert
# subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (170/170/180/190/90/90/90 of 980 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class WidespreadIllnessesHivTbMalariaAndDiarrhoeaSession(MovingCameraScene):
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
        # --- Band 0: HIV and AIDS
        self.write_rows(0, "HIV and AIDS", [
            "HIV attacks the immune system",
            "Spread: unprotected sex, mother to baby, blood",
            "ARVs control the virus; no cure yet",
            "SA life expectancy fell, then recovered",
        ], scale=0.8, box=1)
        # --- Band 1: Tuberculosis
        self.next_band(1)
        self.write_rows(1, "Tuberculosis", [
            "TB: bacterium, usually in the lungs",
            "Spreads through the air by coughing",
            "Cured with 6 months of daily medicine",
            "HIV makes active TB more likely",
        ], scale=0.86, box=2)
        # --- Band 2: Malaria
        self.next_band(2)
        self.write_rows(2, "Malaria", [
            "Parasite carried by Anopheles mosquitoes",
            "Mostly in Africa; children under 5 at risk",
            "SA: north-east KZN, Mpumalanga, Limpopo",
            "Nets, spraying, removing standing water",
        ], scale=0.86, box=4)
        # --- Band 3: Diarrhoea and the Overall Effect
        self.next_band(3)
        self.write_rows(3, "Diarrhoea and the Overall Effect", [
            "Diarrhoea: germs in water, food, dirty hands",
            "Danger: dehydration in young children",
            "Prevent: clean water, toilets, handwashing",
            "Treat: oral rehydration solution and zinc",
        ], scale=0.86, box=4)

        # ============ Part 2 — Simplifier ============
        # --- Band 4: HIV and TB
        self.next_band(4)
        self.write_rows(4, "HIV and TB", [
            "HIV: weakens the body; ARVs keep people well",
            "TB: spread by coughing",
            "TB is curable: 6 months of pills",
        ], scale=0.86, box=0)
        # --- Band 5: Malaria
        self.next_band(5)
        self.write_rows(5, "Malaria", [
            "Spread by mosquito bites",
            "Hot, low north-east of SA",
            "Nets, spraying, no standing water",
        ], scale=0.86, box=0)
        # --- Band 6: Diarrhoea
        self.next_band(6)
        self.write_rows(6, "Diarrhoea", [
            "Germs in water, food, hands",
            "Danger: dehydration",
            "Clean water, soap, ORS",
        ], scale=0.86, box=0)
        self.wait(4)
