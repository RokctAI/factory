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

# Band-layout whiteboard scene (see lessons/scripts/CAPS/manim_exporter.py): one
# band per teaching beat, camera moves down to fresh space, nothing is ever
# removed. Write-only reveals on single-string Tex/MathTex keep the export to
# the allowed primitive vocabulary. Bands cover all seven subtopics of the duo
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7), with
# dwell time proportional to subtopics.json (220/230/230/230/190/190/180 of
# 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ReproductiveSystemOverviewSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): Sexual Reproduction and Gametes
        title = Tex("Sexual reproduction and gametes").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Two parents; offspring show variation").scale(0.9).shift(UP * 1.30)
        b0_l2 = Tex("Gametes: sperm (male) and egg or ovum (female)").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Body cell: 46 chromosomes; gamete: 23").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("23 + 23 gives a zygote with 46").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): Components of the Male and Female Systems
        self.next_band(1)
        b1_title = Tex("Components: name and function").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Testes: sperm and testosterone; scrotum keeps them cooler").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Sperm ducts, prostate, seminal vesicles: semen; urethra and penis").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Ovaries: eggs, oestrogen, progesterone; oviduct: fertilisation").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Uterus: baby develops; cervix: neck; vagina: birth canal").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Processes: From Gametes to a Baby
        self.next_band(2)
        b2_title = Tex("The processes in order").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("1 Gamete production  2 Transfer of sperm").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("3 Fertilisation in the oviduct  4 Implantation in the uterus").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("5 Pregnancy, about 38 weeks  6 Birth").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("No implantation: lining breaks down, menstruation").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Health Issues of the Reproductive System and the Error Museum
        self.next_band(3)
        b3_title = Tex("Health issues").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("STIs: bacterial ones curable, viral ones (HIV, herpes) controlled").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Infertility: about 1 couple in 6; male or female cause").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Cervical cancer: HPV vaccine (Grade 5 girls), Pap smear").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Prostate and testicular cancer: check early").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Health Issues of the Reproductive System and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``Sperm are made in the penis''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Fertilisation happens in the uterus''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``Gametes have 46 chromosomes''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``Infertility is always the woman's problem''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): Half a Recipe From Each Parent
        self.next_band(5)
        b5_title = Tex("Half a recipe from each parent").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Recipe book: 46 chromosomes in 23 pairs").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Sperm: half a book, 23. Egg: half a book, 23.").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Together: a full book of 46, the zygote").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Every mix is new, so siblings differ").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): Two Factories and a Nursery
        self.next_band(6)
        b6_title = Tex("Two factories and a nursery").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Male factory: testes, millions of sperm a day").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Female warehouse: ovaries, one egg about every 28 days").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Meeting place: the oviduct").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Nursery: the uterus; door: cervix; birth canal: vagina").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): Looking After the System
        self.next_band(7)
        b7_title = Tex("Looking after the system").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Bacterial STIs cured; viral STIs controlled").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Infertility: either partner").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("HPV vaccine and Pap smear prevent cervical cancer").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("Monthly self-checks find lumps early").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l3, color=YELLOW)))
        self.wait(4)
