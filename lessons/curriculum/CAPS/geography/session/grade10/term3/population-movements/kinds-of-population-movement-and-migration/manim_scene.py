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

# Band-layout whiteboard scene for "Kinds of Population Movement and
# Migration" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7).
# Exporter-safe primitives only; the push-pull machine and the tug-of-war
# rope are hand-built from Lines/Arrows/Rectangles/Tex. Add-only lifecycle,
# camera moves down band by band. Band time apportioned to subtopics.json
# (240/230/245/240/190/185/170 of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PopulationMovementsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): migration vs circulation ---
        title = Tex("Population Movement and Migration").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("Migration: a permanent or semi-permanent").scale(1.05).shift(UP * 1.0)
        d2 = Tex("change of RESIDENCE").scale(1.1).shift(UP * 0.2)
        self.play(Write(d1))
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(d2, color=GREEN)))
        self.wait(2.5)
        d3 = Tex("Circulation: repeated temporary moves").scale(1.05).shift(DOWN * 0.9)
        d4 = Tex("that return home (commuting, seasonal work)").scale(1.0).shift(DOWN * 1.7)
        self.play(Write(d3))
        self.play(Write(d4))
        self.wait(2.5)
        d5 = Tex("Shopper, tourist, commuter: NOT migrants").scale(1.0).shift(DOWN * 2.7)
        self.play(Write(d5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the three sorting axes ---
        self.next_band(1)
        b1_title = Tex("Three axes of classification").scale(1.2).shift(band_shift(1) + UP * 2.3)
        self.play(Write(b1_title))
        self.wait(1.5)
        a1 = Tex("1. WHERE: internal vs international").scale(1.05).shift(band_shift(1) + UP * 1.3)
        self.play(Write(a1))
        self.wait(1.5)
        a1b = Tex("emigrate OUT of, immigrate INTO").scale(1.0).shift(band_shift(1) + UP * 0.5)
        self.play(Write(a1b))
        self.wait(2)
        a2 = Tex("2. WHY: voluntary vs forced").scale(1.05).shift(band_shift(1) + DOWN * 0.4)
        self.play(Write(a2))
        self.wait(1.5)
        a2b = Tex("refugee / asylum seeker / IDP").scale(1.0).shift(band_shift(1) + DOWN * 1.2)
        self.play(Write(a2b))
        self.wait(2)
        a3 = Tex("3. HOW LONG: permanent vs temporary").scale(1.05).shift(band_shift(1) + DOWN * 2.1)
        a3b = Tex("mine contracts: oscillating migration").scale(1.0).shift(band_shift(1) + DOWN * 2.9)
        self.play(Write(a3))
        self.wait(1.5)
        self.play(Write(a3b))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): the push-pull machine ---
        self.next_band(2)
        b2_title = Tex("Push and pull").scale(1.2).shift(band_shift(2) + UP * 2.3)
        self.play(Write(b2_title))
        self.wait(1.5)
        o_box = Rectangle(width=4.2, height=1.5).shift(band_shift(2) + LEFT * 3.8 + UP * 1.0)
        o_lab = Tex("ORIGIN: push out").scale(0.9).shift(band_shift(2) + LEFT * 3.8 + UP * 1.0)
        d_box = Rectangle(width=4.2, height=1.5).shift(band_shift(2) + RIGHT * 3.8 + UP * 1.0)
        d_lab = Tex("DESTINATION: pull in").scale(0.85).shift(band_shift(2) + RIGHT * 3.8 + UP * 1.0)
        arrow = Arrow(band_shift(2) + LEFT * 1.5 + UP * 1.0, band_shift(2) + RIGHT * 1.5 + UP * 1.0,
                      buff=0, color=YELLOW, stroke_width=6)
        self.play(Create(o_box), Write(o_lab))
        self.play(Create(d_box), Write(d_lab))
        self.play(Create(arrow))
        self.wait(2)
        f1 = Tex("Economic: no work $\\to$ jobs, wages").scale(1.0).shift(band_shift(2) + DOWN * 0.2)
        f2 = Tex("Social: poor services $\\to$ schools, family").scale(1.0).shift(band_shift(2) + DOWN * 1.0)
        f3 = Tex("Political: war $\\to$ peace and rights").scale(1.0).shift(band_shift(2) + DOWN * 1.8)
        f4 = Tex("Environmental: drought $\\to$ reliable rain").scale(1.0).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(f1))
        self.wait(1.5)
        self.play(Write(f2))
        self.wait(1.5)
        self.play(Write(f3))
        self.wait(1.5)
        self.play(Write(f4))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): obstacles and perception ---
        self.next_band(3)
        b3_title = Tex("Obstacles and perception").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("In between: cost, distance,").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex("borders and permits, leaving family").scale(1.05).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex("Move when perceived gain $>$ perceived cost").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex("PERCEIVED: the picture in the head").scale(1.0).shift(band_shift(3) + DOWN * 1.7)
        b3_l5 = Tex("is often brighter than the real city").scale(1.0).shift(band_shift(3) + DOWN * 2.5)
        self.play(Write(b3_l4))
        self.play(Write(b3_l5))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): Eastern Cape to Gauteng — roots and factors ---
        self.next_band(4)
        b4_title = Tex("Case study: Eastern Cape $\\to$ Gauteng").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Roots: homelands, migrant labour,").scale(1.0).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex("pass laws — released in the 1990s").scale(1.0).shift(band_shift(4) + UP * 0.4)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex("Push: rural unemployment, tiny plots,").scale(1.0).shift(band_shift(4) + DOWN * 0.6)
        b4_l4 = Tex("thin services, few prospects").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(2)
        b4_l5 = Tex("Pull: jobs, schools, hospitals,").scale(1.0).shift(band_shift(4) + DOWN * 2.2)
        b4_l6 = Tex("family networks already there").scale(1.0).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): consequences for both ends ---
        self.next_band(5)
        b5_title = Tex("Consequences: both places, both signs").scale(1.1).shift(band_shift(5) + UP * 2.3)
        self.play(Write(b5_title))
        self.wait(1.5)
        ec = Tex("Eastern Cape origin").scale(0.95).shift(band_shift(5) + LEFT * 3.4 + UP * 1.4)
        self.play(Write(ec))
        ec1 = Tex("$+$ remittances, returning skills").scale(0.9).shift(band_shift(5) + LEFT * 3.4 + UP * 0.6)
        ec2 = Tex("$-$ loses working-age adults").scale(0.9).shift(band_shift(5) + LEFT * 3.4 + DOWN * 0.2)
        self.play(Write(ec1))
        self.play(Write(ec2))
        self.wait(2)
        gp = Tex("Gauteng destination").scale(0.95).shift(band_shift(5) + RIGHT * 3.4 + UP * 1.4)
        self.play(Write(gp))
        gp1 = Tex("$+$ young workforce, spending").scale(0.9).shift(band_shift(5) + RIGHT * 3.4 + UP * 0.6)
        gp2 = Tex("$-$ housing and service strain").scale(0.9).shift(band_shift(5) + RIGHT * 3.4 + DOWN * 0.2)
        self.play(Write(gp1))
        self.play(Write(gp2))
        self.wait(2)
        b5_l1 = Tex("Still circular: money home monthly,").scale(1.0).shift(band_shift(5) + DOWN * 1.3)
        b5_l2 = Tex("December return, retire back home").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): the Zimbabwean stream ---
        self.next_band(6)
        b6_title = Tex("Case study: crossing into South Africa").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("Zimbabwe from 2000: hyperinflation,").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex("unemployment, crumbling services").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Pull: strongest regional economy,").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex("shared border, family networks").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2)
        b6_l5 = Tex("Over a million; MIXED migration:").scale(1.0).shift(band_shift(6) + DOWN * 2.2)
        b6_l6 = Tex("economic migrants + refugees together").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): consequences and xenophobia ---
        self.next_band(7)
        b7_title = Tex("The honest balance").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("Origin: remittances a lifeline,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex("but brain drain of nurses, teachers").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("SA: labour, business, scarce skills;").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex("but competition at the bottom, strain").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Xenophobic violence: 2008 and 2015 —").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        b7_l6 = Tex("name it and count its cost honestly").scale(1.0).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the taxi rank and two questions ---
        self.next_band(8)
        b8_title = Tex("Every move answers two questions").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Back by dark: circulation, the daily loop").scale(1.0).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex("Everything you own, not returning: migration").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Q1: crossed a border?").scale(1.05).shift(band_shift(8) + DOWN * 0.5)
        b8_l4 = Tex("emigrant leaving, immigrant arriving").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2.5)
        b8_l5 = Tex("Q2: did they choose?").scale(1.05).shift(band_shift(8) + DOWN * 2.1)
        b8_l6 = Tex("Oscillating: 11 months mine, December home").scale(0.95).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l5))
        self.wait(2)
        self.play(Write(b8_l6))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): the tug-of-war rope ---
        self.next_band(9)
        b9_title = Tex("The tug-of-war decision").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        rope = Line(band_shift(9) + LEFT * 4.8 + UP * 1.0, band_shift(9) + RIGHT * 4.8 + UP * 1.0, stroke_width=6)
        mig = Dot(band_shift(9) + UP * 1.0, color=YELLOW, radius=0.14)
        self.play(Create(rope), FadeIn(mig))
        push_a = Arrow(band_shift(9) + LEFT * 4.6 + UP * 1.7, band_shift(9) + LEFT * 2.4 + UP * 1.7,
                       buff=0, color=RED, stroke_width=5)
        push_l = Tex("home pushes").scale(0.85).shift(band_shift(9) + LEFT * 3.5 + UP * 2.2)
        pull_a = Arrow(band_shift(9) + RIGHT * 2.4 + UP * 1.7, band_shift(9) + RIGHT * 4.6 + UP * 1.7,
                       buff=0, color=GREEN, stroke_width=5)
        pull_l = Tex("city pulls").scale(0.85).shift(band_shift(9) + RIGHT * 3.5 + UP * 2.2)
        self.play(Create(push_a), Write(push_l))
        self.play(Create(pull_a), Write(pull_l))
        self.wait(2.5)
        b9_l1 = Tex("Four players: money, people, safety, land").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex("Every cousin ahead pulls the rope harder").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l2))
        self.wait(2)
        b9_l3 = Tex("Knots in the rope: fares, distance, permits").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l3))
        self.wait(2)
        b9_l4 = Tex("People answer the picture, not the statistics").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): the letter home — four boxes ---
        self.next_band(10)
        b10_title = Tex("The letter home: four boxes").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        # 2x2 grid of consequence boxes
        box_or_g = Rectangle(width=5.6, height=1.6).shift(band_shift(10) + LEFT * 3.1 + UP * 0.9)
        t_or_g = Tex("Origin gains: remittances,").scale(0.8).shift(band_shift(10) + LEFT * 3.1 + UP * 1.15)
        t_or_g2 = Tex("returning skills").scale(0.8).shift(band_shift(10) + LEFT * 3.1 + UP * 0.6)
        self.play(Create(box_or_g), Write(t_or_g), Write(t_or_g2))
        self.wait(2)
        box_or_l = Rectangle(width=5.6, height=1.6).shift(band_shift(10) + LEFT * 3.1 + DOWN * 1.0)
        t_or_l = Tex("Origin loses: workers,").scale(0.8).shift(band_shift(10) + LEFT * 3.1 + DOWN * 0.75)
        t_or_l2 = Tex("whole age groups").scale(0.8).shift(band_shift(10) + LEFT * 3.1 + DOWN * 1.3)
        self.play(Create(box_or_l), Write(t_or_l), Write(t_or_l2))
        self.wait(2)
        box_de_g = Rectangle(width=5.6, height=1.6).shift(band_shift(10) + RIGHT * 3.1 + UP * 0.9)
        t_de_g = Tex("City gains: labour,").scale(0.8).shift(band_shift(10) + RIGHT * 3.1 + UP * 1.15)
        t_de_g2 = Tex("energy, businesses").scale(0.8).shift(band_shift(10) + RIGHT * 3.1 + UP * 0.6)
        self.play(Create(box_de_g), Write(t_de_g), Write(t_de_g2))
        self.wait(2)
        box_de_l = Rectangle(width=5.6, height=1.6).shift(band_shift(10) + RIGHT * 3.1 + DOWN * 1.0)
        t_de_l = Tex("City strains: housing,").scale(0.8).shift(band_shift(10) + RIGHT * 3.1 + DOWN * 0.75)
        t_de_l2 = Tex("services, social peace").scale(0.8).shift(band_shift(10) + RIGHT * 3.1 + DOWN * 1.3)
        self.play(Create(box_de_l), Write(t_de_l), Write(t_de_l2))
        self.wait(2.5)
        b10_l1 = Tex("Fill all four boxes, attach your example").scale(1.0).shift(band_shift(10) + DOWN * 2.4)
        self.play(Write(b10_l1))
        self.play(Create(SurroundingRectangle(b10_l1, color=GREEN)))
        self.wait(3)
