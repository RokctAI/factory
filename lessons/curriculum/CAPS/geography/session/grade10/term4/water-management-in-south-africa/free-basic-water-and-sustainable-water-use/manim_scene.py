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

# Band-layout whiteboard scene for "Free Basic Water and Sustainable Water
# Use" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7).
# Exporter-safe primitives only: the Lesotho Highlands transfer is a
# hand-built cross-section of Line segments with Dots and Arrows (gravity
# downhill vs pumping uphill), and the purification plant is a chain of
# Rectangles and Arrows. Add-only lifecycle; camera moves down band by band.
# Band time apportioned to subtopics.json (235/245/250/230/190/185/165
# of 1500 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


class FreeBasicWaterSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the legal foundation ---
        title = Tex("Free Basic Water and Sustainability").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        l1 = Tex("Section 27: everyone has the right of").scale(1.0).shift(UP * 1.0)
        l2 = Tex("access to sufficient water").scale(1.05).shift(UP * 0.2)
        self.play(Write(l1))
        self.play(Write(l2))
        self.play(Create(SurroundingRectangle(l2, color=GREEN)))
        self.wait(2.5)
        l3 = Tex("National Water Act 1998: water belongs").scale(0.95).shift(DOWN * 0.8)
        l4 = Tex("to the nation; a RESERVE set aside first —").scale(0.95).shift(DOWN * 1.6)
        l5 = Tex("for basic needs and for the rivers themselves").scale(0.95).shift(DOWN * 2.4)
        self.play(Write(l3))
        self.play(Write(l4))
        self.play(Write(l5))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): the six kilolitres and the tariff ---
        self.next_band(1)
        b1_title = Tex("The promise as a number (2001)").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        c1 = MathTex(r"25 \text{ L} \times 8 \text{ people} \times 30 \text{ days}").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(c1))
        self.wait(2)
        c2 = MathTex(r"= 6\,000 \text{ litres free per month}").scale(1.1).shift(band_shift(1) + UP * 0.1)
        self.play(Write(c2))
        self.play(Create(SurroundingRectangle(c2, color=GREEN)))
        self.wait(2)
        c3 = Tex("Within 200 m of the home; basic vs the").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        c4 = Tex("suburban 150 litres per person per day").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(c3))
        self.play(Write(c4))
        self.wait(2)
        c5 = Tex("Rising block tariff: first block cheap, each").scale(0.9).shift(band_shift(1) + DOWN * 2.6)
        c6 = Tex("block dearer — the pool subsidises the standpipe").scale(0.9).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(c5))
        self.play(Write(c6))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): rural challenges ---
        self.next_band(2)
        b2_title = Tex("Why delivery is hard: rural").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        r1 = Tex("Dispersed homes over huge areas:").scale(0.95).shift(band_shift(2) + UP * 1.2)
        r2 = Tex("piping costs many times more per household").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(r1))
        self.play(Write(r2))
        self.wait(2.5)
        r3 = Tex("Dry-interior sources fail in drought;").scale(0.95).shift(band_shift(2) + DOWN * 0.5)
        r4 = Tex("pumps and pipes break, no engineers to fix").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(r3))
        self.play(Write(r4))
        self.wait(2.5)
        r5 = Tex("The burden falls on women and children;").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        r6 = Tex("shared streams bring cholera").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(r5))
        self.play(Write(r6))
        self.wait(2.5)

        # --- Band 3 (subtopic_2): urban challenges ---
        self.next_band(3)
        b3_title = Tex("Why delivery is hard: urban").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        u1 = Tex("Cities grow faster than pipes; informal").scale(0.95).shift(band_shift(3) + UP * 1.2)
        u2 = Tex("settlements on unplanned, unplumbed land").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(u1))
        self.play(Write(u2))
        self.wait(2.5)
        u3 = Tex("Poverty and non-payment strain the revenue").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        self.play(Write(u3))
        self.wait(2)
        u4 = Tex("NON-REVENUE WATER: a third or more leaked,").scale(0.95).shift(band_shift(3) + DOWN * 1.4)
        u5 = Tex("unmetered or unbilled").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(u4))
        self.play(Write(u5))
        self.play(Create(SurroundingRectangle(u5, color=GREEN)))
        self.wait(2)
        u6 = Tex("Shared weakness: municipalities without money,").scale(0.9).shift(band_shift(3) + DOWN * 3.0)
        u7 = Tex("skills or maintenance discipline").scale(0.9).shift(band_shift(3) + DOWN * 3.7)
        self.play(Write(u6))
        self.play(Write(u7))
        self.wait(2.5)

        # --- Band 4 (subtopic_3): transfers — gravity vs pumping ---
        self.next_band(4)
        b4_title = Tex("Inter-basin transfers").scale(1.15).shift(band_shift(4) + UP * 2.5)
        self.play(Write(b4_title))
        self.wait(1.5)
        # cross-section: Lesotho highlands (high, right) down to Gauteng (left)
        p_gau = band_shift(4) + LEFT * 5.0 + DOWN * 0.6
        p_mid = band_shift(4) + LEFT * 0.6 + UP * 0.4
        p_les = band_shift(4) + RIGHT * 3.4 + UP * 1.8
        prof1 = Line(p_gau, p_mid, stroke_width=5)
        prof2 = Line(p_mid, p_les, stroke_width=5)
        self.play(Create(prof1), Create(prof2))
        dam = Dot(p_les, color=BLUE)
        dam_lab = Tex("Katse, Mohale (Lesotho)").scale(0.75).shift(p_les + UP * 0.6 + LEFT * 0.4)
        gau_lab = Tex("Gauteng / Vaal").scale(0.75).shift(p_gau + UP * 0.6 + RIGHT * 0.4)
        self.play(FadeIn(dam), Write(dam_lab), Write(gau_lab))
        flow = Arrow(p_les + DOWN * 0.15 + LEFT * 0.3, p_gau + UP * 0.25 + RIGHT * 0.5,
                     buff=0, color=BLUE, stroke_width=5)
        flow_lab = Tex("gravity — no pumping").scale(0.8).shift(band_shift(4) + LEFT * 0.6 + DOWN * 1.1)
        self.play(Create(flow), Write(flow_lab))
        self.wait(2.5)
        t1 = Tex("Lesotho earns royalties and power; Gauteng drinks").scale(0.85).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(t1))
        self.wait(2)
        t2 = Tex("Tugela-Vaal PUMPS up the escarpment —").scale(0.85).shift(band_shift(4) + DOWN * 2.7)
        t3 = Tex("costly, so Sterkfontein is the drought reserve;").scale(0.85).shift(band_shift(4) + DOWN * 3.4)
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(2.5)

        # --- Band 5 (subtopic_3): dams and the five purification steps ---
        self.next_band(5)
        b5_title = Tex("Dams, and cleaning the water").scale(1.15).shift(band_shift(5) + UP * 2.4)
        self.play(Write(b5_title))
        self.wait(1.5)
        d1 = Tex("Gariep, Vanderkloof, Vaal Dam: store summer").scale(0.9).shift(band_shift(5) + UP * 1.5)
        d2 = Tex("flood for winter need (at evaporation cost)").scale(0.9).shift(band_shift(5) + UP * 0.8)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(2)
        steps = ["1 screen", "2 coagulate", "3 settle", "4 filter", "5 chlorinate"]
        xs = [-5.0, -2.5, 0.0, 2.5, 5.0]
        prev = None
        for x, s in zip(xs, steps):
            box = Rectangle(width=2.2, height=0.9).shift(band_shift(5) + RIGHT * x + DOWN * 0.4)
            lab = Tex(s).scale(0.7).shift(band_shift(5) + RIGHT * x + DOWN * 0.4)
            self.play(Create(box), Write(lab), run_time=0.7)
            if prev is not None:
                ar = Arrow(band_shift(5) + RIGHT * (prev + 1.1) + DOWN * 0.4,
                           band_shift(5) + RIGHT * (x - 1.1) + DOWN * 0.4,
                           buff=0, stroke_width=4, color=BLUE)
                self.play(Create(ar), run_time=0.4)
            prev = x
        self.wait(2)
        d3 = Tex("Aluminium sulphate clumps the fine dirt;").scale(0.9).shift(band_shift(5) + DOWN * 1.7)
        d4 = Tex("chlorine (or ozone, UV) disinfects").scale(0.9).shift(band_shift(5) + DOWN * 2.5)
        self.play(Write(d3))
        self.play(Write(d4))
        self.wait(2)
        d5 = Tex("Blue Drop audits taps; Green Drop audits sewage").scale(0.85).shift(band_shift(5) + DOWN * 3.3)
        self.play(Write(d5))
        self.wait(2.5)

        # --- Band 6 (subtopic_4): government's list ---
        self.next_band(6)
        b6_title = Tex("Sustainability: government's half").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        g1 = Tex("War on leaks: repair, meter, manage pressure").scale(0.9).shift(band_shift(6) + UP * 1.2)
        g2 = Tex("Protect: enforce the Act, fix sewage works").scale(0.9).shift(band_shift(6) + UP * 0.4)
        g3 = Tex("Working for Water: clear thirsty alien plants").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        g4 = Tex("Price wisely: rising blocks, drought restrictions").scale(0.9).shift(band_shift(6) + DOWN * 1.2)
        g5 = Tex("Diversify: desalination, reuse, aquifers").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(g1))
        self.wait(1.5)
        self.play(Write(g2))
        self.wait(1.5)
        self.play(Write(g3))
        self.wait(1.5)
        self.play(Write(g4))
        self.wait(1.5)
        self.play(Write(g5))
        self.wait(2)
        g6 = Tex("...and educate until saving is normal").scale(0.9).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(g6))
        self.wait(2.5)

        # --- Band 7 (subtopic_4): individuals, and the Cape Town proof ---
        self.next_band(7)
        b7_title = Tex("The individual's half").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        i1 = Tex("Fix drips, shower briefly, close the tap,").scale(0.95).shift(band_shift(7) + UP * 1.2)
        i2 = Tex("harvest rain, reuse greywater, plant indigenous").scale(0.95).shift(band_shift(7) + UP * 0.4)
        self.play(Write(i1))
        self.play(Write(i2))
        self.wait(2.5)
        i3 = Tex("Cape Town 2018: use cut roughly in half —").scale(0.95).shift(band_shift(7) + DOWN * 0.6)
        i4 = MathTex(r"\approx 1\,000 \to 500 \text{ million litres a day}").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(i3))
        self.play(Write(i4))
        self.play(Create(SurroundingRectangle(i4, color=GREEN)))
        self.wait(2.5)
        i5 = Tex("Millions of small decisions, plus a state").scale(0.95).shift(band_shift(7) + DOWN * 2.5)
        i6 = Tex("that keeps its pipes whole").scale(0.95).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(i5))
        self.play(Write(i6))
        self.wait(2.5)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the first six thousand litres ---
        self.next_band(8)
        b8_title = Tex("The first six thousand litres").scale(1.15).shift(band_shift(8) + UP * 2.3)
        self.play(Write(b8_title))
        self.wait(2)
        s1 = MathTex(r"25 \times 8 \times 30 = 6\,000 \text{ L free}").scale(1.05).shift(band_shift(8) + UP * 1.2)
        self.play(Write(s1))
        self.play(Create(SurroundingRectangle(s1, color=GREEN)))
        self.wait(2.5)
        s2 = Tex("25 L = five big cooldrink bottles;").scale(0.95).shift(band_shift(8) + UP * 0.1)
        s3 = Tex("one shower uses more. A floor, not comfort").scale(0.95).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(s2))
        self.play(Write(s3))
        self.wait(2.5)
        s4 = Tex("Rising blocks: careful homes stay cheap,").scale(0.95).shift(band_shift(8) + DOWN * 1.6)
        s5 = Tex("the pool's litres pay for the free ones").scale(0.95).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(s4))
        self.play(Write(s5))
        self.wait(2.5)
        s6 = Tex("Paper access is not water in the bucket").scale(0.95).shift(band_shift(8) + DOWN * 3.2)
        self.play(Write(s6))
        self.wait(2.5)

        # --- Band 9 (subtopic_6): moving a river over a mountain ---
        self.next_band(9)
        b9_title = Tex("Moving a river over a mountain").scale(1.15).shift(band_shift(9) + UP * 2.3)
        self.play(Write(b9_title))
        self.wait(2)
        m1 = Tex("Lesotho: the region's heaviest rain,").scale(0.95).shift(band_shift(9) + UP * 1.3)
        m2 = Tex("standing HIGHER than Johannesburg —").scale(0.95).shift(band_shift(9) + UP * 0.5)
        m3 = Tex("those two facts are the whole scheme").scale(0.95).shift(band_shift(9) + DOWN * 0.3)
        self.play(Write(m1))
        self.play(Write(m2))
        self.play(Write(m3))
        self.wait(2.5)
        m4 = Tex("Dam it high, tunnel it through, let gravity").scale(0.95).shift(band_shift(9) + DOWN * 1.2)
        m5 = Tex("run it to the Vaal; Polihali will add more").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(m4))
        self.play(Write(m5))
        self.wait(2.5)
        m6 = Tex("Tugela-Vaal fights gravity uphill = expensive;").scale(0.9).shift(band_shift(9) + DOWN * 2.9)
        m7 = Tex("sieve, clump, settle, filter, chlorinate").scale(0.9).shift(band_shift(9) + DOWN * 3.6)
        self.play(Write(m6))
        self.play(Write(m7))
        self.play(Create(SurroundingRectangle(m7, color=GREEN)))
        self.wait(2.5)

        # --- Band 10 (subtopic_7): the city that counted its days ---
        self.next_band(10)
        b10_title = Tex("The city that counted its days").scale(1.15).shift(band_shift(10) + UP * 2.3)
        self.play(Write(b10_title))
        self.wait(2)
        z1 = Tex("2018: Cape Town names Day Zero —").scale(0.95).shift(band_shift(10) + UP * 1.3)
        z2 = Tex("taps off, 25 L rations in queues").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(z1))
        self.play(Write(z2))
        self.wait(2.5)
        z3 = Tex("It never came: use halved by a million").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        z4 = Tex("small decisions — buckets, grey water, tanks").scale(0.95).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(z3))
        self.play(Write(z4))
        self.wait(2.5)
        z5 = Tex("The cheapest new dam is the water").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        z6 = Tex("a city stops wasting").scale(1.0).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(z5))
        self.play(Write(z6))
        self.play(Create(SurroundingRectangle(z6, color=GREEN)))
        self.wait(2)
        z7 = Tex("Two halves: state pipes + citizen habits").scale(0.95).shift(band_shift(10) + DOWN * 3.6)
        self.play(Write(z7))
        self.wait(3)
