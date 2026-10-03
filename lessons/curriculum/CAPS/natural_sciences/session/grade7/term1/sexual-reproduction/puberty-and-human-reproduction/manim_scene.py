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

# Band-layout whiteboard scene for puberty-and-human-reproduction (Part 1 Expert
# subtopics 1-3, Part 2 Simplifier subtopics 4-6). One band per teaching
# beat, camera moves down to fresh space, nothing is removed. Write-only
# reveals on single-string Tex keep the export inside the whiteboard
# primitive vocabulary. Dwell time proportional to subtopics.json
# (150/170/220/120/120/120 of 900 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PubertyAndHumanReproductionSession(MovingCameraScene):
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
        # --- Band 0 (subtopic_1): Puberty
        self.write_rows(0, "Puberty", [
            "Hormones: oestrogen (ovaries), testosterone (testes)",
            "Both: growth spurt, body hair, sweat, pimples",
            "Girls: breasts, hips, menstruation",
            "Boys: voice deepens, facial hair, sperm made",
        ], scale=0.82, box=3)

        # --- Band 1 (subtopic_2): The reproductive organs
        self.next_band(1)
        self.write_rows(1, "The reproductive organs", [
            "Male: testes, scrotum, sperm ducts, glands, urethra, penis",
            "Female: ovaries, oviducts, uterus, cervix, vagina",
            "Fertilisation normally in the oviduct",
            "Sperm: tiny, swims; egg: large, food store",
        ], scale=0.76, box=2)

        # --- Band 2 (subtopic_3): Cycle, fertilisation, pregnancy
        self.next_band(2)
        self.write_rows(2, "Cycle, fertilisation, pregnancy", [
            "Menstruation days 1 to 5; ovulation about day 14",
            "Not fertilised: lining shed; fertilised: implants",
            "Placenta and cord: food and oxygen in, wastes out",
            "About 40 weeks; no alcohol in pregnancy",
        ], scale=0.82, box=2)

        # --- Band 3 (subtopic_3): error museum
        self.next_band(3)
        em = Tex("Error museum").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(em))
        self.wait(1.5)
        errs = [
            "``The baby grows in the stomach''",
            "``Fertilisation happens in the uterus''",
            "``Menstruation is when the egg is released''",
            "``Pregnancy cannot happen the first time''",
        ]
        for i, e in enumerate(errs):
            t = Tex(e).scale(0.9).shift(band_shift(3) + UP * (1.3 - 1.0 * i))
            self.play(Write(t))
            self.play(Create(strike(t)))
            self.wait(1.8)
        self.wait(1.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 4 (subtopic_4): A body under construction
        self.next_band(4)
        self.write_rows(4, "A body under construction", [
            "Puberty: about 8 to 14, at different ages",
            "Hormones run it: oestrogen and testosterone",
            "Growth spurt, hair, sweat, pimples, feelings",
            "Different ages are normal",
        ], scale=0.88, box=3)

        # --- Band 5 (subtopic_5): Two teams of organs
        self.next_band(5)
        self.write_rows(5, "Two teams of organs", [
            "Male: testes make sperm; scrotum; penis",
            "Female: ovaries release eggs; oviducts",
            "Uterus: a pear-sized muscle where a baby grows",
            "Sperm swims; egg is big and still",
        ], scale=0.82, box=1)

        # --- Band 6 (subtopic_6): The monthly calendar
        self.next_band(6)
        self.write_rows(6, "The monthly calendar", [
            "Period: the old lining is shed",
            "Lining builds up; an egg is released mid-cycle",
            "Sperm meets egg: fertilisation; settles: pregnancy",
            "Placenta feeds the baby; about nine months",
        ], scale=0.82, box=1)

        last = Tex("Puberty prepares the body; fertilisation starts a new life.").scale(0.9).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(last))
        self.play(Create(SurroundingRectangle(last, color=YELLOW)))
        self.wait(4)
