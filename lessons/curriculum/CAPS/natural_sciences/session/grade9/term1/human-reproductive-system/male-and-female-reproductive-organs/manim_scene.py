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


class ReproductiveOrgansSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): The Male Reproductive Organs
        title = Tex("Male organs and functions").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(1.5)
        b0_l1 = Tex("Testis: sperm and testosterone; scrotum keeps it 2 to 3 degrees cooler").scale(0.75).shift(UP * 1.30)
        b0_l2 = Tex("Epididymis: stores and matures sperm").scale(0.9).shift(UP * 0.35)
        b0_l3 = Tex("Sperm duct: muscle contractions move sperm").scale(0.9).shift(DOWN * 0.60)
        b0_l4 = Tex("Seminal vesicles, prostate: fluid; semen out via urethra and penis").scale(0.9).shift(DOWN * 1.55)
        for m in (b0_l1, b0_l2, b0_l3, b0_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b0_l1, color=YELLOW)))
        self.wait(2)

        # --- Band 1 (subtopic_2): The Female Reproductive Organs
        self.next_band(1)
        b1_title = Tex("Female organs and functions").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex("Ovary: releases an egg at ovulation; oestrogen, progesterone").scale(0.9).shift(band_shift(1) + UP * 1.30)
        b1_l2 = Tex("Oviduct: cilia carry the egg; site of fertilisation").scale(0.9).shift(band_shift(1) + UP * 0.35)
        b1_l3 = Tex("Uterus: muscular wall and endometrium; the baby grows here").scale(0.9).shift(band_shift(1) + DOWN * 0.60)
        b1_l4 = Tex("Cervix: closes, then widens to 10 cm; vagina: birth canal").scale(0.9).shift(band_shift(1) + DOWN * 1.55)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b1_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 2 (subtopic_3): The Gametes: Sperm and Egg Compared
        self.next_band(2)
        b2_title = Tex("Sperm and egg compared").scale(1.2).shift(band_shift(2) + UP * 2.4)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex("Sperm: about 0,05 mm; head, middle piece, tail").scale(0.9).shift(band_shift(2) + UP * 1.30)
        b2_l2 = Tex("Acrosome enzymes; mitochondria power the tail").scale(0.9).shift(band_shift(2) + UP * 0.35)
        b2_l3 = Tex("Egg: about 0,1 mm; food store; cannot move").scale(0.9).shift(band_shift(2) + DOWN * 0.60)
        b2_l4 = Tex("Egg always X; sperm X or Y decides the sex").scale(0.9).shift(band_shift(2) + DOWN * 1.55)
        for m in (b2_l1, b2_l2, b2_l3, b2_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b2_l4, color=YELLOW)))
        self.wait(2)

        # --- Band 3 (subtopic_4): Labelling Diagrams and the Error Museum
        self.next_band(3)
        b3_title = Tex("Labelling diagrams").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Ruled lines, no crossings, end on the exact part").scale(0.9).shift(band_shift(3) + UP * 1.30)
        b3_l2 = Tex("Male side view: testis to urethra; bladder is urinary").scale(0.9).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex("Female front view: ovaries, oviducts, uterus, cervix, vagina").scale(0.9).shift(band_shift(3) + DOWN * 0.60)
        b3_l4 = Tex("Female side view: urethra, vagina, anus").scale(0.9).shift(band_shift(3) + DOWN * 1.55)
        for m in (b3_l1, b3_l2, b3_l3, b3_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2)

        # --- Band 4 (subtopic_4): Labelling Diagrams and the Error Museum
        self.next_band(4)
        b4_title = Tex("Error museum").scale(1.2).shift(band_shift(4) + UP * 2.4)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("``The bladder is a reproductive organ''").scale(0.9).shift(band_shift(4) + UP * 1.30)
        b4_l2 = Tex("``Sperm swim all the way from the testes''").scale(0.9).shift(band_shift(4) + UP * 0.35)
        b4_l3 = Tex("``The egg swims to the uterus''").scale(0.9).shift(band_shift(4) + DOWN * 0.60)
        b4_l4 = Tex("``The mother decides the sex of the baby''").scale(0.9).shift(band_shift(4) + DOWN * 1.55)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4):
            self.play(Write(m))
            self.play(Create(strike(m)))
            self.wait(1.8)
        self.wait(2)

        # ============ Part 2 — Simplifier ============
        # --- Band 5 (subtopic_5): The Sperm's Road
        self.next_band(5)
        b5_title = Tex("The sperm's road").scale(1.2).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Testis, epididymis, sperm duct, glands, urethra").scale(0.9).shift(band_shift(5) + UP * 1.30)
        b5_l2 = Tex("Make it, store it, move it, feed it, deliver it").scale(0.9).shift(band_shift(5) + UP * 0.35)
        b5_l3 = Tex("Scrotum: the cool section").scale(0.9).shift(band_shift(5) + DOWN * 0.60)
        b5_l4 = Tex("Prostate cancels the acid of the vagina").scale(0.9).shift(band_shift(5) + DOWN * 1.55)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b5_l2, color=YELLOW)))
        self.wait(2)

        # --- Band 6 (subtopic_6): The Egg's Road
        self.next_band(6)
        b6_title = Tex("The egg's road").scale(1.2).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Ovary: a follicle pops, ovulation").scale(0.9).shift(band_shift(6) + UP * 1.30)
        b6_l2 = Tex("Funnel fingers catch the egg").scale(0.9).shift(band_shift(6) + UP * 0.35)
        b6_l3 = Tex("Cilia carry it 3 to 4 days to the uterus").scale(0.9).shift(band_shift(6) + DOWN * 0.60)
        b6_l4 = Tex("Way out: cervix, then vagina").scale(0.9).shift(band_shift(6) + DOWN * 1.55)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b6_l3, color=YELLOW)))
        self.wait(2)

        # --- Band 7 (subtopic_7): A Tadpole and a Grain of Sand
        self.next_band(7)
        b7_title = Tex("A tadpole and a grain of sand").scale(1.2).shift(band_shift(7) + UP * 2.4)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Sperm: tiny, many, swims, no food store").scale(0.9).shift(band_shift(7) + UP * 1.30)
        b7_l2 = Tex("Egg: biggest cell, one, still, food store").scale(0.9).shift(band_shift(7) + UP * 0.35)
        b7_l3 = Tex("Both: 23 chromosomes").scale(0.9).shift(band_shift(7) + DOWN * 0.60)
        b7_l4 = Tex("X egg + X sperm: girl; X egg + Y sperm: boy").scale(0.9).shift(band_shift(7) + DOWN * 1.55)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(2.3)
        self.play(Create(SurroundingRectangle(b7_l4, color=YELLOW)))
        self.wait(4)
