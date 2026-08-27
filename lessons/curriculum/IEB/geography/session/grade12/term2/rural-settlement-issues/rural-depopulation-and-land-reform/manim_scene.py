# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from manim import *

# Band-layout whiteboard scene for the rural depopulation and land
# reform duo lesson. Exporter-safe primitives only (Tex/Line/Arrow/
# Dot/Circle/Rectangle/VGroup); add-only lifecycle; camera moves down
# one frame-height per band. The push-pull diagram and pinched pyramid
# are hand-built from Arrows and Line chains in script order.
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
        title = Tex("Push and pull: the migration engine").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        person = Dot(ORIGIN, radius=0.14, color=WHITE)
        p_lab = Tex(r"one person, one decision").scale(0.85).shift(DOWN * 0.6)
        self.play(Create(person), Write(p_lab))
        self.wait(2)
        push = Arrow(LEFT * 4.2, LEFT * 0.5, buff=0, color=RED)
        push_lab = Tex(r"PUSH: no work, thin services,\\ drought, shrinking plots").scale(0.8).shift(LEFT * 3.2 + UP * 1.2)
        self.play(Create(push), Write(push_lab))
        self.wait(2.5)
        pull = Arrow(RIGHT * 0.5, RIGHT * 4.2, buff=0, color=GREEN)
        pull_lab = Tex(r"PULL: jobs, schools, hospitals,\\ the relative's open door").scale(0.8).shift(RIGHT * 3.2 + UP * 1.2)
        self.play(Create(pull), Write(pull_lab))
        self.wait(2.5)
        eq = Tex(r"Move when shove + tug $>$ comfort of home").scale(0.95).shift(DOWN * 1.8)
        self.play(Write(eq))
        self.play(Create(SurroundingRectangle(eq, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): perception + who moves ---
        self.next_band(1)
        b1_t = Tex("The rumour, and the chosen few").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        r1 = Tex(r"Pull is real OR believed — perception moves people").scale(0.9).shift(band_shift(1) + UP * 1.2)
        self.play(Write(r1))
        self.wait(2)
        r2 = Tex(r"Many arrive to no job + informal housing").scale(0.9).shift(band_shift(1) + UP * 0.4)
        self.play(Write(r2))
        self.wait(2)
        r3 = Tex(r"WHO moves: young, economically active adults").scale(0.9).shift(band_shift(1) + DOWN * 0.5)
        r4 = Tex(r"historically men first (migrant labour system)").scale(0.9).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(r3))
        self.wait(2)
        self.play(Write(r4))
        self.wait(2)
        r5 = Tex(r"Selectivity unbalances the village left behind").scale(0.9).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(r5))
        self.play(Create(SurroundingRectangle(r5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): depopulation — definition and causes ---
        self.next_band(2)
        b2_t = Tex("Rural depopulation: causes").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        d1 = Tex(r"Definition: rural population declines as").scale(0.95).shift(band_shift(2) + UP * 1.2)
        d1b = Tex(r"out-migration outruns natural increase").scale(0.95).shift(band_shift(2) + UP * 0.5)
        self.play(Write(d1))
        self.play(Write(d1b))
        self.wait(2.5)
        d2 = Tex(r"+ Mechanised, consolidated commercial farms").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        d3 = Tex(r"+ Service closures: school, bank, post office").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(d2))
        self.wait(2)
        self.play(Write(d3))
        self.wait(2)
        d4 = Tex(r"Each closure pushes the next family out: a spiral").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        self.play(Write(d4))
        self.play(Create(SurroundingRectangle(d4, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): consequences + the balanced account ---
        self.next_band(3)
        b3_t = Tex("Consequences, both columns").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        c1 = Tex(r"People: pinched pyramid, grants + remittances,").scale(0.9).shift(band_shift(3) + UP * 1.2)
        c1b = Tex(r"high dependency ratio, brain drain").scale(0.9).shift(band_shift(3) + UP * 0.5)
        self.play(Write(c1))
        self.play(Write(c1b))
        self.wait(2.5)
        c2 = Tex(r"Place: idle fields, empty homesteads,").scale(0.9).shift(band_shift(3) + DOWN * 0.4)
        c2b = Tex(r"closed shops (Free State platteland)").scale(0.9).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(c2))
        self.play(Write(c2b))
        self.wait(2.5)
        c3 = Tex(r"But: remittances build, land pressure eases,").scale(0.9).shift(band_shift(3) + DOWN * 2.0)
        c3b = Tex(r"returnees bring skills — balance the ledger").scale(0.9).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(c3))
        self.play(Write(c3b))
        self.play(Create(SurroundingRectangle(c3b, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): strategies matched to push factors ---
        self.next_band(4)
        b4_t = Tex("Strategies: aim at the push factor").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        s1 = Tex(r"Unemployment $\rightarrow$ agri-processing, public works,").scale(0.9).shift(band_shift(4) + UP * 1.2)
        s1b = Tex(r"small-farmer finance and markets").scale(0.9).shift(band_shift(4) + UP * 0.5)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        s2 = Tex(r"Weak services $\rightarrow$ schools, clinics, power, roads").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        self.play(Write(s2))
        self.wait(2)
        s3 = Tex(r"No opportunity $\rightarrow$ tourism: game, heritage, trails").scale(0.9).shift(band_shift(4) + DOWN * 1.2)
        self.play(Write(s3))
        self.wait(2)
        s4 = Tex(r"People rarely leave a home that offers a living").scale(0.9).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(s4))
        self.play(Create(SurroundingRectangle(s4, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): the social justice layer ---
        self.next_band(5)
        b5_t = Tex("Why poverty sits where it sits").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        j1 = Tex(r"1913 Land Act: ownership rationed by race").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(j1))
        self.wait(2)
        j2 = Tex(r"Homelands: many people, least productive land").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(j2))
        self.wait(2)
        j3 = Tex(r"Less investment: schools, clinics, roads, banks").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(j3))
        self.wait(2)
        j4 = Tex(r"Missing infrastructure IS a push factor").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        self.play(Write(j4))
        self.play(Create(SurroundingRectangle(j4, color=GREEN)))
        self.wait(2)
        j5 = Tex(r"Today's poverty map traces the lines apartheid drew").scale(0.9).shift(band_shift(5) + DOWN * 2.2)
        self.play(Write(j5))
        self.wait(3)

        # --- Band 6 (subtopic_4): the three legs of land reform ---
        self.next_band(6)
        b6_t = Tex("Land reform: three legs").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        l1 = Tex(r"TENURE: strengthen rights of those already there").scale(0.9).shift(band_shift(6) + UP * 1.2)
        l1b = Tex(r"no eviction by one letter; moves nobody").scale(0.85).shift(band_shift(6) + UP * 0.5)
        self.play(Write(l1))
        self.play(Write(l1b))
        self.wait(2.5)
        l2 = Tex(r"REDISTRIBUTION: transfer farmland going forward").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        l2b = Tex(r"assisted purchase, equity and livelihoods").scale(0.85).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(l2))
        self.play(Write(l2b))
        self.wait(2.5)
        l3 = Tex(r"RESTITUTION: return specific land taken").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        l3b = Tex(r"after 19 June 1913 — or compensate").scale(0.85).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(l3))
        self.play(Write(l3b))
        self.play(Create(SurroundingRectangle(l3, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the separator + the loop ---
        self.next_band(7)
        b7_t = Tex("Keep the legs apart, close the loop").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        v1 = Tex(r"Tenure = secure rights in place").scale(0.95).shift(band_shift(7) + UP * 1.2)
        v2 = Tex(r"Redistribution = transfer for equity").scale(0.95).shift(band_shift(7) + UP * 0.4)
        v3 = Tex(r"Restitution = named land, proven removal").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(v1))
        self.wait(2)
        self.play(Write(v2))
        self.wait(2)
        self.play(Write(v3))
        self.wait(2)
        v4 = Tex(r"Reform that works = a livelihood at home").scale(0.95).shift(band_shift(7) + DOWN * 1.4)
        v5 = Tex(r"= a depopulation strategy in itself").scale(0.95).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(v4))
        self.play(Write(v5))
        self.play(Create(SurroundingRectangle(v5, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the kitchen-table decision ---
        self.next_band(8)
        b8_t = Tex("The kitchen-table decision").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        k1 = Tex(r"19, matric done, plot too small, work seasonal").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(k1))
        self.wait(2)
        k2 = Tex(r"Durban: the aunt's room, the talk of jobs").scale(0.9).shift(band_shift(8) + UP * 0.4)
        self.play(Write(k2))
        self.wait(2)
        k3 = Tex(r"Shove (push) + tug (pull) vs the comfort of home").scale(0.9).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(k3))
        self.play(Create(SurroundingRectangle(k3, color=GREEN)))
        self.wait(2.5)
        k4 = Tex(r"The tug is partly a rumour — perception moves people").scale(0.85).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(k4))
        self.wait(2)
        k5 = Tex(r"Gran stays; the young and strong go").scale(0.9).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(k5))
        self.wait(3)

        # --- Band 9 (subtopic_6): the village after the taxi leaves ---
        self.next_band(9)
        b9_t = Tex("The village after the taxi leaves").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        # Pinched pyramid: wide base, narrow middle, wide top
        py1 = Line(band_shift(9) + LEFT * 2.6 + DOWN * 1.9, band_shift(9) + LEFT * 0.9 + DOWN * 0.7, color=WHITE, stroke_width=4)
        py2 = Line(band_shift(9) + LEFT * 0.9 + DOWN * 0.7, band_shift(9) + LEFT * 1.7 + UP * 0.4, color=WHITE, stroke_width=4)
        py3 = Line(band_shift(9) + RIGHT * 2.6 + DOWN * 1.9, band_shift(9) + RIGHT * 0.9 + DOWN * 0.7, color=WHITE, stroke_width=4)
        py4 = Line(band_shift(9) + RIGHT * 0.9 + DOWN * 0.7, band_shift(9) + RIGHT * 1.7 + UP * 0.4, color=WHITE, stroke_width=4)
        py_lab = Tex(r"pinched waist: the workers are gone").scale(0.85).shift(band_shift(9) + DOWN * 2.5)
        self.play(Create(py1), Create(py3))
        self.play(Create(py2), Create(py4))
        self.play(Write(py_lab))
        self.wait(2.5)
        q1 = Tex(r"School merges, bank closes, post office follows").scale(0.85).shift(band_shift(9) + UP * 1.3)
        q2 = Tex(r"A slow puncture — less every week").scale(0.9).shift(band_shift(9) + UP * 0.6)
        self.play(Write(q1))
        self.wait(2)
        self.play(Write(q2))
        self.play(Create(SurroundingRectangle(q2, color=GREEN)))
        self.wait(2)
        q3 = Tex(r"Remittances build brick rooms — but fields lie idle").scale(0.8).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(q3))
        self.wait(3)

        # --- Band 10 (subtopic_7): strengthen, share, return ---
        self.next_band(10)
        b10_t = Tex("Three repairs for one old injustice").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        z1 = Tex(r"1913: the law drew today's poverty map").scale(0.9).shift(band_shift(10) + UP * 1.2)
        self.play(Write(z1))
        self.wait(2)
        z2 = Tex(r"STRENGTHEN: tenure — firmer grip, same land").scale(0.9).shift(band_shift(10) + UP * 0.4)
        z3 = Tex(r"SHARE: redistribution — new owners, fair future").scale(0.9).shift(band_shift(10) + DOWN * 0.4)
        z4 = Tex(r"RETURN: restitution — named place, proven removal").scale(0.9).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(z2))
        self.wait(2)
        self.play(Write(z3))
        self.wait(2)
        self.play(Write(z4))
        self.play(Create(SurroundingRectangle(z4, color=GREEN)))
        self.wait(2)
        z5 = Tex(r"A living at home ends the kitchen-table decision").scale(0.9).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(z5))
        self.wait(4)
