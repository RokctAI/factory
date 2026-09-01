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

# Band-layout whiteboard scene for the rural-settlement-issues duo
# (rural depopulation and land reform). Exporter-safe primitives only
# (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle;
# camera moves down one frame-height per band. The push/pull engine is a
# hand-built diagram (village and city rectangles, a migrant Dot, push and
# pull Arrows); the rest of the topic is staged line by line in script order.
#
# Subtopic shares (subtopics.json, total 1610 s):
# 230/240/230/250 expert, 210/220/230 simplifier. Bands 0-7 = Part 1
# (two per expert subtopic), bands 8-10 = fresh Part 2 bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class RuralDepopulationLandReformSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the push-pull engine ---
        title = Tex("Push and Pull: The Migration Engine").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        village = Rectangle(width=2.6, height=1.2, color=GREY).shift(LEFT * 4.2 + UP * 0.6)
        v_lab = Tex(r"village").scale(0.9).shift(LEFT * 4.2 + UP * 0.6)
        city = Rectangle(width=2.6, height=1.2, color=GREY).shift(RIGHT * 4.2 + UP * 0.6)
        c_lab = Tex(r"city").scale(0.9).shift(RIGHT * 4.2 + UP * 0.6)
        self.play(Create(village), Write(v_lab))
        self.play(Create(city), Write(c_lab))
        self.wait(1.5)
        migrant = Dot(UP * 0.6, color=YELLOW)
        push_a = Arrow(LEFT * 2.6 + UP * 0.6, LEFT * 0.6 + UP * 0.6, buff=0, color=RED)
        pull_a = Arrow(RIGHT * 0.6 + UP * 0.6, RIGHT * 2.6 + UP * 0.6, buff=0, color=GREEN)
        push_lab = Tex(r"PUSH shoves").scale(0.85).shift(LEFT * 1.7 + UP * 1.3)
        pull_lab = Tex(r"PULL tugs").scale(0.85).shift(RIGHT * 1.7 + UP * 1.3)
        self.play(Create(migrant))
        self.play(Create(push_a), Write(push_lab))
        self.play(Create(pull_a), Write(pull_lab))
        self.wait(2)
        p1 = Tex(r"Push: no jobs, thin services, drought,").scale(0.95).shift(DOWN * 0.7)
        p1b = Tex(r"plots too small to split again").scale(0.95).shift(DOWN * 1.4)
        p2 = Tex(r"Pull: wages, schools, hospitals, the cousin's").scale(0.95).shift(DOWN * 2.2)
        p2b = Tex(r"open door — real OR believed").scale(0.95).shift(DOWN * 2.9)
        self.play(Write(p1))
        self.play(Write(p1b))
        self.wait(2.5)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.wait(3)

        # --- Band 1 (subtopic_1): perception + who moves ---
        self.next_band(1)
        b1_t = Tex("Perception, and who boards the taxi").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        s1 = Tex(r"Migrants move on the PERCEPTION of").scale(1.0).shift(band_shift(1) + UP * 1.2)
        s1b = Tex(r"opportunity — the city does not always deliver").scale(1.0).shift(band_shift(1) + UP * 0.4)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        s2 = Tex(r"Many arrive to unemployment and informal").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        s2b = Tex(r"settlements on the urban edge").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(s2))
        self.play(Write(s2b))
        self.wait(2.5)
        s3 = Tex(r"Selectivity: young, economically active adults;").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        s3b = Tex(r"historically men first (migrant labour system)").scale(0.95).shift(band_shift(1) + DOWN * 3.0)
        self.play(Write(s3))
        self.play(Write(s3b))
        self.play(Create(SurroundingRectangle(s3b, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): depopulation — definition and causes ---
        self.next_band(2)
        b2_t = Tex("Rural depopulation: the spiral").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        d1 = Tex(r"Decline of rural population: out-migration").scale(1.0).shift(band_shift(2) + UP * 1.2)
        d1b = Tex(r"outrunning natural increase").scale(1.0).shift(band_shift(2) + UP * 0.4)
        self.play(Write(d1))
        self.play(Write(d1b))
        self.wait(2.5)
        d2 = Tex(r"+ mechanised, consolidated commercial farms").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(d2))
        self.wait(2)
        d3 = Tex(r"+ service closures: school shuts $\rightarrow$ families").scale(0.95).shift(band_shift(2) + DOWN * 1.4)
        d3b = Tex(r"leave $\rightarrow$ next service shuts — a spiral").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(d3))
        self.play(Write(d3b))
        self.play(Create(SurroundingRectangle(d3b, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): consequences + the balanced account ---
        self.next_band(3)
        b3_t = Tex("Consequences: the people, the place").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        q1 = Tex(r"People: hollowed-out pyramid — children,").scale(0.95).shift(band_shift(3) + UP * 1.2)
        q1b = Tex(r"elderly, women remain; middle missing").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(q1))
        self.play(Write(q1b))
        self.wait(2.5)
        q2 = Tex(r"Grants + remittances; dependency ratio climbs;").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        q2b = Tex(r"brain drain — teachers and nurses leave first").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(q2))
        self.play(Write(q2b))
        self.wait(2.5)
        q3 = Tex(r"Place: idle fields, empty buildings, closed").scale(0.95).shift(band_shift(3) + DOWN * 2.1)
        q3b = Tex(r"shopfronts (Karoo, Eastern Cape end state)").scale(0.95).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(q3))
        self.play(Write(q3b))
        self.wait(2)
        q4 = Tex(r"Balance: remittances build; land pressure eases").scale(0.9).shift(band_shift(3) + DOWN * 3.5)
        self.play(Write(q4))
        self.wait(3)

        # --- Band 4 (subtopic_3): strategies matched to push factors ---
        self.next_band(4)
        b4_t = Tex("Strategies: attack the push factors").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        g1 = Tex(r"Unemployment: agri-processing, public works,").scale(0.95).shift(band_shift(4) + UP * 1.2)
        g1b = Tex(r"small-farmer finance and markets").scale(0.95).shift(band_shift(4) + UP * 0.4)
        self.play(Write(g1))
        self.play(Write(g1b))
        self.wait(2.5)
        g2 = Tex(r"Services: schools, clinics, electrification,").scale(0.95).shift(band_shift(4) + DOWN * 0.5)
        g2b = Tex(r"water, roads — each removes a reason to leave").scale(0.95).shift(band_shift(4) + DOWN * 1.3)
        self.play(Write(g2))
        self.play(Write(g2b))
        self.wait(2.5)
        g3 = Tex(r"Opportunity: tourism turns landscape into income").scale(0.9).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(g3))
        self.wait(2)
        g4 = Tex(r"People rarely leave home when home offers a living").scale(0.9).shift(band_shift(4) + DOWN * 3.0)
        self.play(Write(g4))
        self.play(Create(SurroundingRectangle(g4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the social justice layer ---
        self.next_band(5)
        b5_t = Tex("Social justice: history drew this map").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        j1 = Tex(r"Natives Land Act 1913: black ownership").scale(1.0).shift(band_shift(5) + UP * 1.2)
        j1b = Tex(r"confined to a small fraction of the country").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(j1))
        self.play(Write(j1b))
        self.wait(2.5)
        j2 = Tex(r"Homelands: many people, least productive land").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        j3 = Tex(r"Less investment: schools, clinics, roads, finance").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(j2))
        self.wait(2)
        self.play(Write(j3))
        self.wait(2)
        j4 = Tex(r"Today's poorest rural districts trace, to a").scale(0.95).shift(band_shift(5) + DOWN * 2.2)
        j4b = Tex(r"large degree, the map apartheid drew").scale(0.95).shift(band_shift(5) + DOWN * 3.0)
        self.play(Write(j4))
        self.play(Write(j4b))
        self.play(Create(SurroundingRectangle(j4b, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three legs of land reform ---
        self.next_band(6)
        b6_t = Tex("Land reform: three distinct legs").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        l1 = Tex(r"1. TENURE: strengthens rights of people").scale(0.95).shift(band_shift(6) + UP * 1.2)
        l1b = Tex(r"already on the land — moves no one").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(l1))
        self.play(Write(l1b))
        self.wait(2.5)
        l2 = Tex(r"2. REDISTRIBUTION: transfers farmland for").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        l2b = Tex(r"equity now — forward-looking, willing buyer/seller").scale(0.9).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(l2))
        self.play(Write(l2b))
        self.wait(2.5)
        l3 = Tex(r"3. RESTITUTION: returns specific land taken by").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        l3b = Tex(r"racial laws after 19 June 1913 — or compensates").scale(0.9).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(l3))
        self.play(Write(l3b))
        self.wait(3)

        # --- Band 7 (subtopic_4): the separator + the loop ---
        self.next_band(7)
        b7_t = Tex("Keep the legs apart — then close the loop").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        x1 = Tex(r"Tenure: secures those ON the land").scale(1.0).shift(band_shift(7) + UP * 1.2)
        x2 = Tex(r"Redistribution: redresses unequal ownership").scale(1.0).shift(band_shift(7) + UP * 0.4)
        x3 = Tex(r"Restitution: named land, proven removal").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(x1))
        self.wait(2)
        self.play(Write(x2))
        self.wait(2)
        self.play(Write(x3))
        self.play(Create(SurroundingRectangle(x3, color=GREEN)))
        self.wait(2.5)
        x4 = Tex(r"Loop: land reform IS a depopulation strategy —").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        x4b = Tex(r"secure rights + productive land = a livelihood").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        x4c = Tex(r"without leaving home").scale(0.95).shift(band_shift(7) + DOWN * 3.0)
        self.play(Write(x4))
        self.play(Write(x4b))
        self.play(Write(x4c))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the kitchen-table decision ---
        self.next_band(8)
        b8_t = Tex("The kitchen-table decision").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        k1 = Tex(r"22, matric done; small plot, seasonal work,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        k1b = Tex(r"far clinic — vs a cousin's bed in Gauteng").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(k1))
        self.play(Write(k1b))
        self.wait(2.5)
        k2 = Tex(r"The shove (push) + the tug (pull) vs the").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        k2b = Tex(r"comfort of staying home").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(k2))
        self.play(Write(k2b))
        self.wait(2.5)
        k3 = Tex(r"The tug is partly a story: the city promises").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        k3b = Tex(r"more than it pays — perception moves people").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(k3))
        self.play(Write(k3b))
        self.play(Create(SurroundingRectangle(k3b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the village after the taxi leaves ---
        self.next_band(9)
        b9_t = Tex("The village after the taxi leaves").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        v1 = Tex(r"Left behind: children, pensioners, women —").scale(1.0).shift(band_shift(9) + UP * 1.2)
        v1b = Tex(r"a pyramid with its waist pinched in").scale(1.0).shift(band_shift(9) + UP * 0.4)
        self.play(Write(v1))
        self.play(Write(v1b))
        self.wait(2.5)
        v2 = Tex(r"School merges, bank closes, post office follows:").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        v2b = Tex(r"a slow leak, the way a football goes soft").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(v2))
        self.play(Write(v2b))
        self.wait(2.5)
        v3 = Tex(r"Remittances build brick rooms — but a village").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        v3b = Tex(r"cannot live on sent money forever").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(v3))
        self.play(Write(v3b))
        self.wait(2)
        v4 = Tex(r"Every fix must answer: which push factor is off?").scale(0.9).shift(band_shift(9) + DOWN * 3.5)
        self.play(Write(v4))
        self.wait(3)

        # --- Band 10 (subtopic_7): grip, share, give back ---
        self.next_band(10)
        b10_t = Tex("Three repairs for one old injustice").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        z1 = Tex(r"1913 squeezed ownership; homelands got the").scale(0.95).shift(band_shift(10) + UP * 1.2)
        z1b = Tex(r"worst land — today's poverty map traces it").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(z1))
        self.play(Write(z1b))
        self.wait(2.5)
        z2 = Tex(r"GRIP: tenure — handshake becomes signed lease").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        z3 = Tex(r"SHARE: redistribution — new owners, fairness").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        z4 = Tex(r"GIVE BACK: restitution — named place, proven").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        z4b = Tex(r"removal, land returned or paid out").scale(0.95).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(z2))
        self.wait(2)
        self.play(Write(z3))
        self.wait(2)
        self.play(Write(z4))
        self.play(Write(z4b))
        self.play(Create(SurroundingRectangle(z4b, color=GREEN)))
        self.wait(2.5)
        z5 = Tex(r"Done well, it answers the kitchen table: a living, at home").scale(0.85).shift(band_shift(10) + DOWN * 3.5)
        self.play(Write(z5))
        self.wait(4)
