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

# Band-layout whiteboard scene for harmful-micro-organisms-and-disease (Part 1
# Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). One band per
# teaching beat, camera moves down to fresh space, nothing is removed.
# Write-only reveals on single-string Tex keep the export inside the
# whiteboard primitive vocabulary. Dwell time proportional to subtopics.json
# (230/250/250/210/170/190/170 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class HarmfulMicroOrganismsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def write_rows(self, k, title, rows, scale=0.8, box=None, box_color=YELLOW):
        t = Tex(title).scale(1.15).shift(band_shift(k) + UP * 2.4)
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
        # --- Band 0 (subtopic_1): routes of transmission
        self.write_rows(0, "Pathogen: a micro-organism that causes disease", [
            "Air: TB, flu \\quad Water and food: cholera",
            "Blood and body fluids: HIV \\quad Vector bite: malaria",
            "Barriers: skin, mucus, stomach acid",
            "White blood cells, antibodies, memory; vaccines",
        ], scale=0.82, box=1)

        # --- Band 1 (subtopic_2): TB and cholera
        self.next_band(1)
        self.write_rows(1, "TB and cholera: two bacteria", [
            "TB: lungs, airborne; cough over 2 weeks, night sweats",
            "Cure: daily antibiotics for about 6 months, finish them",
            "Cholera: dirty water and food; toxin, watery diarrhoea",
            "Rehydrate: 1 L clean water, 6 tsp sugar, half tsp salt",
        ], scale=0.8, box=3)

        # --- Band 2 (subtopic_3): HIV/AIDS and malaria
        self.next_band(2)
        self.write_rows(2, "HIV and AIDS; malaria", [
            "HIV: virus in blood, semen, vaginal fluid, breast milk",
            "AIDS: late stage of untreated HIV; ART keeps it undetectable",
            "Malaria: Plasmodium, a protist; female Anopheles at night",
            "SA: low north-east; nets, repellent, spraying, no standing water",
        ], scale=0.78, box=1)

        # --- Band 3 (subtopic_4): break the chain
        self.next_band(3)
        self.write_rows(3, "Prevention breaks a link", [
            "Handwashing, safe water, sanitation: water and food route",
            "Cover coughs, ventilate: air route",
            "Condoms, no shared needles, gloves: blood route",
            "Vaccines and herd immunity; treatment stops spread",
        ], scale=0.8, box=3)

        # --- Band 4 (subtopic_4): error museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        errs = [
            "``AIDS is a virus''",
            "``Mosquitoes spread HIV''",
            "``The mosquito causes malaria''",
            "``Stop the TB tablets when the cough clears''",
        ]
        for i, e in enumerate(errs):
            m = Tex(e).scale(0.9).shift(band_shift(4) + UP * (1.3 - 1.0 * i))
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): four doors
        self.next_band(5)
        self.write_rows(5, "Germs need a way in", [
            "Door 1: the air", "Door 2: dirty water and food",
            "Door 3: blood and body fluids", "Door 4: a bite",
        ], scale=0.9)

        # --- Band 6 (subtopic_6): four diseases
        self.next_band(6)
        self.write_rows(6, "Four diseases at a glance", [
            "TB: bacterium, air, six months of tablets",
            "Cholera: bacterium, water, sugar and salt drink",
            "HIV: virus, blood; AIDS is the late stage",
            "Malaria: protist, mosquito bite, waves of fever",
        ], scale=0.85, box=2)

        # --- Band 7 (subtopic_7): locks
        self.next_band(7)
        self.write_rows(7, "Locking the doors", [
            "Elbow and open windows \\quad Soap and boiled water",
            "No shared needles \\quad Nets and repellent",
            "Vaccines keep the guards ready",
        ], scale=0.85)
        last = Tex("Know the door, use the lock.").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
