# Copyright (c) 2026 RokctAI
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

# Band-layout whiteboard scene for "Population distribution and density"
# (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7). The
# same-density/different-distribution two-ward sketch and the SA east-west
# rainfall pattern are hand-built from Dot/Line/Rectangle/Tex; the density
# calculations run line by line with the script's numbers.
# Subtopic durations (s): 215/230/245/245/185/180/190 of 1490.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PopulationDistributionSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): two different ideas ---
        title = Tex("Population Distribution and Density").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"Distribution = the PATTERN, in words").scale(1.0).shift(UP * 1.3)
        d2 = Tex(r"Density = a NUMBER: people per km$^2$").scale(1.0).shift(UP * 0.6)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(2)
        # two wards, same density, different distribution
        boxA = Rectangle(width=3.4, height=2.2).shift(DOWN * 1.6 + LEFT * 2.9)
        for dx, dy in [(-1.0, 0.6), (0.0, 0.6), (1.0, 0.6), (-1.0, -0.5), (0.0, -0.5), (1.0, -0.5)]:
            boxA.add(Dot(DOWN * 1.6 + LEFT * 2.9 + RIGHT * dx + UP * dy, radius=0.06))
        self.play(Create(boxA))
        la = Tex("smallholdings: even").scale(0.8).shift(DOWN * 3.1 + LEFT * 2.9)
        self.play(Write(la))
        boxB = Rectangle(width=3.4, height=2.2).shift(DOWN * 1.6 + RIGHT * 2.9)
        for dx, dy in [(-1.35, 0.65), (-1.15, 0.65), (-1.35, 0.85), (-1.15, 0.85), (-1.25, 0.75), (-1.05, 0.75)]:
            boxB.add(Dot(DOWN * 1.6 + RIGHT * 2.9 + RIGHT * dx + UP * dy, radius=0.06))
        self.play(Create(boxB))
        lb = Tex("one fishing town: clustered").scale(0.8).shift(DOWN * 3.1 + RIGHT * 2.9)
        self.play(Write(lb))
        self.wait(2)
        eq = Tex(r"Same density (60/km$^2$), opposite patterns").scale(0.95).shift(DOWN * 0.3)
        self.play(Write(eq))
        self.play(Create(SurroundingRectangle(eq, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the vocabulary ---
        self.next_band(1)
        b1t = Tex("Words for describing a pattern").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        v1 = Tex(r"Dense, sparse, uninhabited").scale(1.0).shift(band_shift(1) + UP * 1.1)
        v2 = Tex(r"Clustered: bunched around a point").scale(1.0).shift(band_shift(1) + UP * 0.3)
        v3 = Tex(r"Linear: strung along road, river, shore").scale(1.0).shift(band_shift(1) + DOWN * 0.5)
        v4 = Tex(r"Dispersed: homesteads standing apart").scale(1.0).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(v1))
        self.wait(2)
        self.play(Write(v2))
        self.wait(1.5)
        self.play(Write(v3))
        self.wait(1.5)
        self.play(Write(v4))
        self.wait(2)
        v5 = Tex(r"How many = density; where = distribution").scale(0.95).shift(band_shift(1) + DOWN * 2.3)
        self.play(Write(v5))
        self.play(Create(SurroundingRectangle(v5, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the calculation ---
        self.next_band(2)
        b2t = Tex("Calculating density").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        f1 = MathTex(r"\text{density} = \frac{\text{total population}}{\text{total area}}").scale(1.01).shift(band_shift(2) + UP * 1.0)
        self.play(Write(f1))
        self.wait(2)
        f2 = MathTex(r"\frac{189\,000}{1\,400 \text{ km}^2} = 135 \text{ people/km}^2").scale(0.97).shift(band_shift(2) + DOWN * 0.2)
        self.play(Write(f2))
        self.play(Create(SurroundingRectangle(f2, color=GREEN)))
        self.wait(2)
        f3 = Tex(r"135").scale(1.0).shift(band_shift(2) + DOWN * 1.2 + LEFT * 2.4)
        self.play(Write(f3))
        self.play(Create(strike(f3)))
        f3b = Tex(r"— an unfinished answer:").scale(0.95).shift(band_shift(2) + DOWN * 1.2 + RIGHT * 1.0)
        f3c = Tex(r"always write people per km$^2$").scale(0.95).shift(band_shift(2) + DOWN * 1.9)
        self.play(Write(f3b))
        self.play(Write(f3c))
        self.wait(2)
        f4 = Tex(r"SA: 63 million $\div$ 1,22 million km$^2$").scale(0.95).shift(band_shift(2) + DOWN * 2.7)
        f4b = Tex(r"$\approx$ just over 50 people/km$^2$").scale(0.95).shift(band_shift(2) + DOWN * 3.3)
        self.play(Write(f4))
        self.play(Write(f4b))
        self.wait(3)

        # --- Band 3 (subtopic_2): what the average hides ---
        self.next_band(3)
        b3t = Tex("What the average hides").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(1.5)
        g1 = Tex(r"KwaZulu-Natal: a fifth of the nation,").scale(0.95).shift(band_shift(3) + UP * 1.2)
        g1b = Tex(r"$\approx$ 130 people/km$^2$").scale(0.95).shift(band_shift(3) + UP * 0.6)
        g2 = Tex(r"Northern Cape: a third of the land,").scale(0.95).shift(band_shift(3) + DOWN * 0.2)
        g2b = Tex(r"under 4 people/km$^2$").scale(0.95).shift(band_shift(3) + DOWN * 0.8)
        self.play(Write(g1))
        self.play(Write(g1b))
        self.wait(2)
        self.play(Write(g2))
        self.play(Write(g2b))
        self.wait(2)
        g3 = Tex(r"50/km$^2$ describes nowhere: silent").scale(0.9).shift(band_shift(3) + DOWN * 1.7)
        g3b = Tex(r"Bushmanland and packed Umlazi blended").scale(0.9).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(g3))
        self.play(Write(g3b))
        self.wait(2)
        g4 = Tex(r"Better: people per ARABLE km$^2$").scale(0.95).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(g4))
        self.wait(3)

        # --- Band 4 (subtopic_3): physical factors ---
        self.next_band(4)
        b4t = Tex("Physical factors").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(1.5)
        p1 = Tex(r"Relief: level fills, steep empties").scale(0.95).shift(band_shift(4) + UP * 1.2)
        p2 = Tex(r"Climate: the strongest control —").scale(0.95).shift(band_shift(4) + UP * 0.5)
        p2b = Tex(r"Namib, Siberia, Congo forest repel").scale(0.95).shift(band_shift(4) + DOWN * 0.1)
        p3 = Tex(r"Water: no settlement without it").scale(0.95).shift(band_shift(4) + DOWN * 0.8)
        p4 = Tex(r"Soils: Java + Bangladesh = dense farms").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(p1))
        self.wait(1.5)
        self.play(Write(p2))
        self.play(Write(p2b))
        self.wait(2)
        self.play(Write(p3))
        self.wait(1.5)
        self.play(Write(p4))
        self.wait(1.5)
        p5 = Tex(r"Minerals fix people to the deposit;").scale(0.95).shift(band_shift(4) + DOWN * 2.3)
        p5b = Tex(r"harbours and passes funnel trade").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(p5))
        self.play(Write(p5b))
        self.wait(3)

        # --- Band 5 (subtopic_4): human factors and the SA map ---
        self.next_band(5)
        b5t = Tex("Human factors and South Africa").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(1.5)
        h1 = Tex(r"Work, transport corridors, services,").scale(0.95).shift(band_shift(5) + UP * 1.2)
        h1b = Tex(r"government and history, social bonds").scale(0.95).shift(band_shift(5) + UP * 0.6)
        self.play(Write(h1))
        self.play(Write(h1b))
        self.wait(2.5)
        # east-west divide sketch
        box = Rectangle(width=4.2, height=2.4).shift(band_shift(5) + LEFT * 2.7 + DOWN * 1.2)
        div = Line(band_shift(5) + LEFT * 2.7 + UP * 0.0, band_shift(5) + LEFT * 2.7 + DOWN * 2.4, color=BLUE)
        self.play(Create(box))
        self.play(Create(div))
        wl = Tex("dry west: sparse").scale(0.75).shift(band_shift(5) + LEFT * 3.8 + DOWN * 2.8)
        el = Tex("wet east: settled").scale(0.75).shift(band_shift(5) + LEFT * 1.5 + DOWN * 2.8)
        self.play(Write(wl), Write(el))
        self.wait(2)
        h2 = Tex(r"Moisture line: about 500 mm a year").scale(0.9).shift(band_shift(5) + RIGHT * 2.6 + DOWN * 0.8)
        self.play(Write(h2))
        h3 = Tex(r"Four clusters: Gauteng, Durban,").scale(0.9).shift(band_shift(5) + RIGHT * 2.7 + DOWN * 1.6)
        h3b = Tex(r"Cape Town, Gqeberha–East London").scale(0.9).shift(band_shift(5) + RIGHT * 2.7 + DOWN * 2.2)
        self.play(Write(h3))
        self.play(Write(h3b))
        self.wait(3)

        # --- Band 6 (subtopic_4): Gauteng and the homelands ---
        self.next_band(6)
        b6t = Tex("The puzzle and the inheritance").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        a1 = Tex(r"Gauteng: no harbour, no river — gold").scale(0.95).shift(band_shift(6) + UP * 1.2)
        a1b = Tex(r"1880s Witwatersrand: workers, factories,").scale(0.95).shift(band_shift(6) + UP * 0.5)
        a1c = Tex(r"banks — the structure outlived the gold").scale(0.95).shift(band_shift(6) + DOWN * 0.1)
        self.play(Write(a1))
        self.wait(2)
        self.play(Write(a1b))
        self.play(Write(a1c))
        self.wait(2)
        a2 = Tex(r"Crowded rural districts in the former").scale(0.95).shift(band_shift(6) + DOWN * 1.0)
        a2b = Tex(r"homelands — QwaQwa, Venda, Gazankulu:").scale(0.95).shift(band_shift(6) + DOWN * 1.6)
        a2c = Tex(r"densities written by law, not land").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        self.play(Write(a2))
        self.play(Write(a2b))
        self.play(Write(a2c))
        self.play(Create(SurroundingRectangle(a2c, color=GREEN)))
        a3 = Tex(r"Sparse: Karoo, Bushmanland, Namaqualand").scale(0.9).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(a3))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 7 (subtopic_5): the bus and the beach ---
        self.next_band(7)
        b7t = Tex("The bus and the beach").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        c1 = Tex(r"60 passengers in one bus: squeezed").scale(1.0).shift(band_shift(7) + UP * 1.2)
        c2 = Tex(r"Same 60 on a beach: lost — DENSITY").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        c3 = Tex(r"Along the waterline or round the pool:").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        c3b = Tex(r"same density, new map — DISTRIBUTION").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(c3))
        self.play(Write(c3b))
        self.wait(2)
        c4 = Tex(r"Number answers how crowded;").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        c4b = Tex(r"picture answers where").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(c4))
        self.play(Write(c4b))
        self.play(Create(SurroundingRectangle(VGroup(c4, c4b), color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_6): why the Richtersveld stays empty ---
        self.next_band(8)
        b8t = Tex("Why the Richtersveld stays empty").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        k1 = Tex(r"Water first: villages bead the Orange").scale(0.95).shift(band_shift(8) + UP * 1.2)
        k2 = Tex(r"Flat ground: ploughs, buildings, roads").scale(0.95).shift(band_shift(8) + UP * 0.4)
        k3 = Tex(r"Bearable weather + good soil feed people").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(k1))
        self.wait(2)
        self.play(Write(k2))
        self.wait(2)
        self.play(Write(k3))
        self.wait(2)
        k4 = Tex(r"Two wildcards: Kathu's iron ore,").scale(0.95).shift(band_shift(8) + DOWN * 1.3)
        k4b = Tex(r"Saldanha's deep natural harbour").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(k4))
        self.play(Write(k4b))
        self.wait(2)
        k5 = Tex(r"People follow the rain eastward —").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        k5b = Tex(r"the land drew most of the map").scale(0.95).shift(band_shift(8) + DOWN * 3.3)
        self.play(Write(k5))
        self.play(Write(k5b))
        self.play(Create(SurroundingRectangle(k5b, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_7): follow the jobs ---
        self.next_band(9)
        b9t = Tex("Follow the jobs").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        j1 = Tex(r"Gauteng: quarter of SA on 2\% of land —").scale(0.95).shift(band_shift(9) + UP * 1.2)
        j1b = Tex(r"1880s gold: miners, towns, engineering,").scale(0.95).shift(band_shift(9) + UP * 0.6)
        j1c = Tex(r"banks, railways, holding each other").scale(0.95).shift(band_shift(9) + UP * 0.0)
        self.play(Write(j1))
        self.play(Write(j1b))
        self.play(Write(j1c))
        self.wait(2.5)
        j2 = Tex(r"Richards Bay: harbour, exports, smelters").scale(0.95).shift(band_shift(9) + DOWN * 0.9)
        self.play(Write(j2))
        self.wait(2)
        j3 = Tex(r"Crowded rural east: homeland history,").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        j3b = Tex(r"the engine of migration to the cities").scale(0.95).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(j3))
        self.play(Write(j3b))
        self.wait(2)
        j4 = Tex(r"Rain, gold and harbours, history").scale(1.0).shift(band_shift(9) + DOWN * 3.1)
        self.play(Write(j4))
        self.play(Create(SurroundingRectangle(j4, color=GREEN)))
        self.wait(4)
