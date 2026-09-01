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

# Band-layout whiteboard scene for the session duo "World Population Growth
# and Overpopulation" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier
# subtopics 5-7). Exporter-safe mobjects only (Tex/MathTex/Line/Arrow/Dot/
# Circle/Rectangle/VGroup); the J-curve is a chained-Line polyline built on
# hand-made Arrow axes. Add-only lifecycle: the camera moves down band by
# band, nothing is ever removed or transformed.
# Band time is apportioned to subtopics.json (235/230/240/240/190/185/180
# of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class WorldPopulationGrowthSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): two chapters of population history ---
        title = Tex("World Population Growth").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        ch1 = Tex("Chapter 1: a ten-millennium crawl").scale(1.1).shift(UP * 1.0)
        self.play(Write(ch1))
        self.wait(2)
        ch1b = Tex("Plentiful births clawed back by deaths").scale(1.1).shift(UP * 0.1)
        self.play(Write(ch1b))
        self.wait(2)
        ch2 = Tex("Chapter 2: 1 billion around 1804...").scale(1.1).shift(DOWN * 0.9)
        self.play(Write(ch2))
        self.wait(2)
        ch2b = Tex("...8 billion by 2022").scale(1.1).shift(DOWN * 1.8)
        self.play(Write(ch2b))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the J-curve, built element by element ---
        self.next_band(1)
        b1_title = Tex("The J-curve").scale(1.2).shift(band_shift(1) + UP * 2.4)
        self.play(Write(b1_title))
        self.wait(1.5)
        origin = band_shift(1) + LEFT * 4.6 + DOWN * 2.4
        x_axis = Arrow(origin, origin + RIGHT * 9.0, buff=0, stroke_width=4)
        y_axis = Arrow(origin, origin + UP * 4.4, buff=0, stroke_width=4)
        x_lab = Tex("Time").scale(0.9).shift(band_shift(1) + RIGHT * 4.4 + DOWN * 2.9)
        y_lab = Tex("People").scale(0.9).shift(band_shift(1) + LEFT * 3.6 + UP * 2.0)
        self.play(Create(x_axis), Create(y_axis))
        self.play(Write(x_lab), Write(y_lab))
        self.wait(1.5)
        # flat tail, the elbow, the near-vertical climb
        seg1 = Line(origin + UP * 0.2, origin + RIGHT * 5.2 + UP * 0.4, color=YELLOW, stroke_width=5)
        seg2 = Line(origin + RIGHT * 5.2 + UP * 0.4, origin + RIGHT * 6.6 + UP * 1.2, color=YELLOW, stroke_width=5)
        seg3 = Line(origin + RIGHT * 6.6 + UP * 1.2, origin + RIGHT * 7.6 + UP * 2.8, color=YELLOW, stroke_width=5)
        seg4 = Line(origin + RIGHT * 7.6 + UP * 2.8, origin + RIGHT * 8.2 + UP * 4.0, color=YELLOW, stroke_width=5)
        self.play(Create(seg1))
        self.wait(1.5)
        self.play(Create(seg2))
        self.play(Create(seg3))
        self.play(Create(seg4))
        self.wait(1.5)
        d1804 = Dot(origin + RIGHT * 5.2 + UP * 0.4, color=RED)
        l1804 = Tex("1804: 1 bn").scale(0.85).shift(band_shift(1) + RIGHT * 0.6 + DOWN * 2.4)
        d1927 = Dot(origin + RIGHT * 6.6 + UP * 1.2, color=RED)
        l1927 = Tex("1927: 2 bn").scale(0.85).shift(band_shift(1) + RIGHT * 3.4 + DOWN * 1.4)
        d2022 = Dot(origin + RIGHT * 8.2 + UP * 4.0, color=RED)
        l2022 = Tex("2022: 8 bn").scale(0.85).shift(band_shift(1) + RIGHT * 2.4 + UP * 1.7)
        self.play(FadeIn(d1804), Write(l1804))
        self.wait(1.5)
        self.play(FadeIn(d1927), Write(l1927))
        self.wait(1.5)
        self.play(FadeIn(d2022), Write(l2022))
        self.wait(2.5)

        # --- Band 2 (subtopic_1): what bent the curve ---
        self.next_band(2)
        b2_title = Tex("What bent the curve?").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_wrong = Tex("Bigger families?").scale(1.1).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2_wrong))
        self.play(Create(strike(b2_wrong)))
        self.wait(2)
        b2_l1 = Tex("Dying became rarer:").scale(1.1).shift(band_shift(2) + UP * 0.2)
        b2_l2 = Tex("food, sanitation, vaccines, antibiotics").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1))
        self.wait(1.5)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"Rate crested $\approx 2\%$ (late 1960s)").scale(1.05).shift(band_shift(2) + DOWN * 1.7)
        b2_l4 = Tex(r"now under $1\%$: the J turning into an S").scale(1.05).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.play(Create(SurroundingRectangle(b2_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): natural increase, worked ---
        self.next_band(3)
        b3_title = Tex("Measuring growth: natural increase").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{NI} = \text{births} - \text{deaths}").scale(1.15).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = MathTex(r"34 - 9 = 25 \text{ per thousand}").scale(1.15).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2))
        self.wait(2)
        b3_l3 = MathTex(r"25 \div 10 = 2{,}5\% \text{ per year}").scale(1.15).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2)
        b3_l4 = Tex("Natural = migration left out").scale(1.05).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l4))
        self.wait(2.5)

        # --- Band 4 (subtopic_2): rule of 70 and country cases ---
        self.next_band(4)
        b4_title = Tex("Doubling time: the rule of 70").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{doubling time} = 70 \div \text{growth \%}").scale(1.1).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"70 \div 2{,}5 = 28 \text{ years}").scale(1.1).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = MathTex(r"3{,}5\%: 20 \text{ yrs} \quad 1\%: 70 \text{ yrs}").scale(1.05).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l3))
        self.wait(2)
        b4_l4 = Tex(r"Angola $\approx 3\%$: doubles in $\approx$ 23 yrs").scale(1.0).shift(band_shift(4) + DOWN * 1.7)
        b4_l5 = Tex(r"Italy: negative NI. SA $\approx 1\%$: 70 yrs").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): overpopulation is a relationship ---
        self.next_band(5)
        b5_title = Tex("Overpopulation: people vs resources").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_wrong = Tex("Overpopulated = crowded?").scale(1.05).shift(band_shift(5) + UP * 1.1)
        self.play(Write(b5_wrong))
        self.play(Create(strike(b5_wrong)))
        self.wait(2)
        b5_l1 = Tex("Overpopulated: people outnumber the").scale(1.1).shift(band_shift(5) + UP * 0.2)
        b5_l2 = Tex("CARRYING CAPACITY of the region").scale(1.1).shift(band_shift(5) + DOWN * 0.7)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2.5)
        b5_l3 = Tex("Density is a headcount;").scale(1.05).shift(band_shift(5) + DOWN * 1.7)
        b5_l4 = Tex("overpopulation is a relationship").scale(1.05).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)

        # --- Band 6 (subtopic_3): Singapore vs southern Madagascar ---
        self.next_band(6)
        b6_title = Tex("Singapore vs southern Madagascar").scale(1.1).shift(band_shift(6) + UP * 2.3)
        self.play(Write(b6_title))
        self.wait(1.5)
        sg_box = Rectangle(width=5.4, height=2.6).shift(band_shift(6) + LEFT * 3.2 + UP * 0.5)
        sg_1 = Tex(r"$>8\,000$ per km$^2$").scale(0.9).shift(band_shift(6) + LEFT * 3.2 + UP * 1.1)
        sg_2 = Tex("NOT overpopulated:").scale(0.85).shift(band_shift(6) + LEFT * 3.2 + UP * 0.4)
        sg_3 = Tex("wealth, trade, technology").scale(0.85).shift(band_shift(6) + LEFT * 3.2 + DOWN * 0.3)
        self.play(Create(sg_box))
        self.play(Write(sg_1))
        self.play(Write(sg_2))
        self.play(Write(sg_3))
        self.wait(2)
        md_box = Rectangle(width=5.4, height=2.6).shift(band_shift(6) + RIGHT * 3.2 + UP * 0.5)
        md_1 = Tex("sparse drylands").scale(0.9).shift(band_shift(6) + RIGHT * 3.2 + UP * 1.1)
        md_2 = Tex("CAN be overpopulated:").scale(0.85).shift(band_shift(6) + RIGHT * 3.2 + UP * 0.4)
        md_3 = Tex("meagre rain, spent soils").scale(0.85).shift(band_shift(6) + RIGHT * 3.2 + DOWN * 0.3)
        self.play(Create(md_box))
        self.play(Write(md_1))
        self.play(Write(md_2))
        self.play(Write(md_3))
        self.wait(2)
        b6_l1 = Tex("Signs: shrinking plots, erosion, joblessness,").scale(0.95).shift(band_shift(6) + DOWN * 1.4)
        b6_l2 = Tex("oversubscribed services, hunger, leaving").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2)
        b6_l3 = Tex("The ceiling moves: tech lifts it, abuse sinks it").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l3))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): the four levers ---
        self.next_band(7)
        b7_title = Tex("Managing growth: what works").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex("1. Educate girls and women").scale(1.1).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7_l1))
        self.play(Create(SurroundingRectangle(b7_l1, color=GREEN)))
        self.wait(2)
        b7_l2 = Tex("2. Cut infant mortality").scale(1.1).shift(band_shift(7) + UP * 0.1)
        self.play(Write(b7_l2))
        self.wait(1.5)
        b7_l3 = Tex("(surviving babies end insurance babies)").scale(0.95).shift(band_shift(7) + DOWN * 0.7)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex("3. Family planning within reach").scale(1.1).shift(band_shift(7) + DOWN * 1.6)
        b7_l5 = Tex("4. Less poverty, pensions for old age").scale(1.1).shift(band_shift(7) + DOWN * 2.5)
        self.play(Write(b7_l4))
        self.wait(1.5)
        self.play(Write(b7_l5))
        self.wait(2.5)

        # --- Band 8 (subtopic_4): China vs Bangladesh and Botswana, SA ---
        self.next_band(8)
        b8_title = Tex("Force vs choice").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex("China one-child (1979--2015):").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("old before rich, fewer workers, skewed sexes").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex("Bangladesh and Botswana: same fall,").scale(1.05).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = Tex("by schooling and clinics, no scars").scale(1.05).shift(band_shift(8) + DOWN * 1.7)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.wait(2)
        b8_l5 = Tex(r"SA: 6 children per woman $\to$ 2,3 by choice").scale(1.0).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5))
        self.play(Create(SurroundingRectangle(b8_l5, color=GREEN)))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the festival that fills in the final week ---
        self.next_band(9)
        b9_title = Tex("The festival fills in the final week").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        # year-long timeline
        t0 = band_shift(9) + LEFT * 5.2 + UP * 1.0
        t1 = band_shift(9) + RIGHT * 5.2 + UP * 1.0
        tline = Line(t0, t1, stroke_width=5)
        self.play(Create(tline))
        m0 = Tex("1 Jan").scale(0.8).shift(band_shift(9) + LEFT * 5.2 + UP * 1.6)
        m1 = Tex("25 Dec").scale(0.8).shift(band_shift(9) + RIGHT * 3.6 + UP * 1.6)
        m2 = Tex("31 Dec").scale(0.8).shift(band_shift(9) + RIGHT * 5.2 + UP * 1.6)
        d1 = Dot(band_shift(9) + RIGHT * 3.6 + UP * 1.0, color=RED)
        d2 = Dot(band_shift(9) + RIGHT * 5.2 + UP * 1.0, color=RED)
        self.play(Write(m0))
        self.play(Write(m1), FadeIn(d1))
        self.play(Write(m2), FadeIn(d2))
        self.wait(2)
        b9_l1 = Tex("Eleven and a half months: 1 billion inside").scale(1.0).shift(band_shift(9) + UP * 0.1)
        self.play(Write(b9_l1))
        self.wait(2.5)
        b9_l2 = Tex("Final week: the other 7 billion pour in").scale(1.0).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l2))
        self.wait(2.5)
        b9_l3 = Tex("Why? Death lost its grip —").scale(1.0).shift(band_shift(9) + DOWN * 1.7)
        b9_l4 = Tex("not more births, fewer funerals").scale(1.0).shift(band_shift(9) + DOWN * 2.5)
        self.play(Write(b9_l3))
        self.play(Write(b9_l4))
        self.play(Create(SurroundingRectangle(b9_l4, color=GREEN)))
        self.wait(2.5)
        b9_l5 = Tex("The queue outside shrinks every year").scale(1.0).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l5))
        self.wait(2.5)

        # --- Band 10 (subtopic_6): the overloaded taxi ---
        self.next_band(10)
        b10_title = Tex("Too many for what? The taxi").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        # simple taxi: body rectangle plus two wheel circles, licence label
        body = Rectangle(width=5.2, height=1.6).shift(band_shift(10) + UP * 0.8)
        w1 = Circle(radius=0.35).shift(band_shift(10) + LEFT * 1.6 + UP * 0.0)
        w2 = Circle(radius=0.35).shift(band_shift(10) + RIGHT * 1.6 + UP * 0.0)
        cap = Tex("licensed for 15 = carrying capacity").scale(0.95).shift(band_shift(10) + UP * 2.0)
        self.play(Create(body), Create(w1), Create(w2))
        self.play(Write(cap))
        self.wait(2.5)
        b10_l1 = Tex("11 aboard: fine. 23 aboard: overloaded").scale(1.0).shift(band_shift(10) + DOWN * 0.7)
        self.play(Write(b10_l1))
        self.wait(2.5)
        b10_l2 = Tex("Singapore: packed luxury coach, rides fine").scale(1.0).shift(band_shift(10) + DOWN * 1.5)
        b10_l3 = Tex("Dry Madagascar south: tiny taxi, overloaded").scale(1.0).shift(band_shift(10) + DOWN * 2.3)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex("The licence can change: drought downgrades it").scale(0.95).shift(band_shift(10) + DOWN * 3.1)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(2.5)

        # --- Band 11 (subtopic_7): the school gate ---
        self.next_band(11)
        b11_title = Tex("What slows growth: the school gate").scale(1.15).shift(band_shift(11) + UP * 2.3)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex(r"Girl finishes school $\to$ marries later").scale(1.0).shift(band_shift(11) + UP * 1.2)
        b11_l2 = Tex(r"$\to$ earns $\to$ invests in fewer children").scale(1.0).shift(band_shift(11) + UP * 0.3)
        self.play(Write(b11_l1))
        self.wait(2)
        self.play(Write(b11_l2))
        self.wait(2.5)
        b11_l3 = Tex("Surviving babies end insurance babies:").scale(1.0).shift(band_shift(11) + DOWN * 0.7)
        b11_l4 = Tex("families shrink within a generation").scale(1.0).shift(band_shift(11) + DOWN * 1.5)
        self.play(Write(b11_l3))
        self.play(Write(b11_l4))
        self.wait(2.5)
        b11_l5 = Tex("China forced it and pays; Bangladesh chose it").scale(1.0).shift(band_shift(11) + DOWN * 2.4)
        self.play(Write(b11_l5))
        self.wait(2)
        b11_l6 = Tex(r"SA: 6 $\to$ 2,3 children — choice worked").scale(1.0).shift(band_shift(11) + DOWN * 3.2)
        self.play(Write(b11_l6))
        self.play(Create(SurroundingRectangle(b11_l6, color=GREEN)))
        self.wait(3)
