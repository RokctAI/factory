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

# Band-layout whiteboard scene for "Sectors and Infrastructure of the SA
# Economy" (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7).
# Exporter-safe primitives only; add-only lifecycle.
# Subtopic durations: 225/230/225/230/190/190/190 of 1480 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SectorsInfrastructureSASession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ===================== Part 1 — Expert =====================
        # --- Band 0 (subtopic_1): the three sectors ---
        title = Tex("Sectors and Infrastructure of the SA Economy").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        r0a = Rectangle(width=3.6, height=1.4).shift(UP * 0.9 + LEFT * 4.6)
        t0a = Tex("Primary").scale(0.85).move_to(r0a.get_center() + UP * 0.3)
        t0a2 = Tex("from nature").scale(0.7).move_to(r0a.get_center() + DOWN * 0.35)
        self.play(Create(r0a), Write(t0a), Write(t0a2))
        d0a = Tex("mining, maize, hake, timber").scale(0.8).shift(UP * 0.9 + RIGHT * 1.4)
        self.play(Write(d0a))
        self.wait(2)
        r0b = Rectangle(width=3.6, height=1.4).shift(DOWN * 0.8 + LEFT * 4.6)
        t0b = Tex("Secondary").scale(0.85).move_to(r0b.get_center() + UP * 0.3)
        t0b2 = Tex("transform goods").scale(0.7).move_to(r0b.get_center() + DOWN * 0.35)
        a0a = Arrow(r0a.get_bottom(), r0b.get_top(), buff=0.1)
        self.play(Create(a0a), Create(r0b), Write(t0b), Write(t0b2))
        d0b = Tex("bakkies, flour, steel, construction").scale(0.8).shift(DOWN * 0.8 + RIGHT * 1.7)
        self.play(Write(d0b))
        self.wait(2)
        r0c = Rectangle(width=3.6, height=1.4).shift(DOWN * 2.5 + LEFT * 4.6)
        t0c = Tex("Tertiary").scale(0.85).move_to(r0c.get_center() + UP * 0.3)
        t0c2 = Tex("services").scale(0.7).move_to(r0c.get_center() + DOWN * 0.35)
        a0b = Arrow(r0b.get_bottom(), r0c.get_top(), buff=0.1)
        self.play(Create(a0b), Create(r0c), Write(t0c), Write(t0c2))
        d0c = Tex("banking, taxis, teaching, call centres").scale(0.8).shift(DOWN * 2.5 + RIGHT * 1.9)
        self.play(Write(d0c))
        self.wait(3)

        # --- Band 1 (subtopic_1): the shares, and the jobs warning ---
        self.next_band(1)
        b1t = Tex("The South African shares of GDP").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("Tertiary: roughly two thirds — the giant").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2)
        b1b = Tex("Secondary: about a fifth; manufacturing $\\approx$ 13\\%").scale(1.0).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1b))
        self.wait(2)
        b1c = Tex("Primary smallest: mining $\\approx$ 6\\%, agriculture $\\approx$ 3\\%").scale(0.84).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1c))
        self.wait(2)
        b1w = Tex("Small share of GDP $=$ unimportant sector").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1w))
        self.play(Create(strike(b1w)))
        self.wait(1.5)
        b1d = Tex("GDP share and jobs share are different questions").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1d))
        self.play(Create(SurroundingRectangle(b1d, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): one orange through the chain ---
        self.next_band(2)
        b2t = Tex("One orange, three sectors").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        s2a = Tex("Farmer grows it").scale(0.9).shift(band_shift(2) + UP * 1.0 + LEFT * 4.4)
        s2b = Tex("Factory makes juice").scale(0.9).shift(band_shift(2) + UP * 1.0)
        s2c = Tex("Shop, bank, truck sell it").scale(0.9).shift(band_shift(2) + UP * 1.0 + RIGHT * 4.3)
        a2a = Arrow(s2a.get_right(), s2b.get_left(), buff=0.15)
        a2b = Arrow(s2b.get_right(), s2c.get_left(), buff=0.15)
        self.play(Write(s2a))
        self.play(Create(a2a), Write(s2b))
        self.play(Create(a2b), Write(s2c))
        self.wait(2)
        l2a = Tex("primary").scale(0.8).shift(band_shift(2) + UP * 0.3 + LEFT * 4.4)
        l2b = Tex("secondary").scale(0.8).shift(band_shift(2) + UP * 0.3)
        l2c = Tex("tertiary").scale(0.8).shift(band_shift(2) + UP * 0.3 + RIGHT * 4.3)
        self.play(Write(l2a), Write(l2b), Write(l2c))
        self.wait(2)
        b2a = Tex("Value gathers at every link — interdependence").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2a))
        self.wait(2)
        b2b = Tex("A drought empties the factory shift").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        b2b2 = Tex("and quietens the till").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2b))
        self.play(Write(b2b2))
        self.wait(3)

        # --- Band 3 (subtopic_2): structural transformation and its complication ---
        self.next_band(3)
        b3t = Tex("The structure has shifted — with a warning").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        s3a = Tex("Primary era").scale(0.9).shift(band_shift(3) + UP * 1.1 + LEFT * 4.4)
        s3b = Tex("Secondary era").scale(0.9).shift(band_shift(3) + UP * 1.1)
        s3c = Tex("Tertiary era").scale(0.9).shift(band_shift(3) + UP * 1.1 + RIGHT * 4.2)
        a3a = Arrow(s3a.get_right(), s3b.get_left(), buff=0.15)
        a3b = Arrow(s3b.get_right(), s3c.get_left(), buff=0.15)
        self.play(Write(s3a))
        self.play(Create(a3a), Write(s3b))
        self.play(Create(a3b), Write(s3c))
        self.wait(2)
        b3a = Tex("Structural transformation: most economies walk it").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3a))
        self.wait(2)
        b3b = Tex("SA complication: manufacturing 20\\%+ (1990s)").scale(1.0).shift(band_shift(3) + DOWN * 0.7)
        b3b2 = Tex("$\\rightarrow$ about 13\\% today").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3b))
        self.play(Write(b3b2))
        self.wait(2)
        b3c = Tex("Premature deindustrialisation: factories faded before").scale(0.95).shift(band_shift(3) + DOWN * 2.3)
        b3c2 = Tex("absorbing the semi-skilled workers who need them").scale(0.95).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3c))
        self.play(Write(b3c2))
        self.play(Create(SurroundingRectangle(b3c2, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): infrastructure split in two ---
        self.next_band(4)
        b4t = Tex("Infrastructure — the economy's skeleton").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        r4a = Rectangle(width=5.6, height=2.4).shift(band_shift(4) + UP * 0.2 + LEFT * 3.4)
        t4a = Tex("Economic:").scale(0.85).move_to(r4a.get_center() + UP * 0.7)
        t4a2 = Tex("power, rail, roads,").scale(0.75).move_to(r4a.get_center())
        t4a3 = Tex("ports, dams, telecoms").scale(0.75).move_to(r4a.get_center() + DOWN * 0.7)
        self.play(Create(r4a), Write(t4a), Write(t4a2), Write(t4a3))
        self.wait(2)
        r4b = Rectangle(width=5.6, height=2.4).shift(band_shift(4) + UP * 0.2 + RIGHT * 3.4)
        t4b = Tex("Social:").scale(0.85).move_to(r4b.get_center() + UP * 0.7)
        t4b2 = Tex("schools, hospitals,").scale(0.75).move_to(r4b.get_center())
        t4b3 = Tex("housing, sanitation").scale(0.75).move_to(r4b.get_center() + DOWN * 0.7)
        self.play(Create(r4b), Write(t4b), Write(t4b2), Write(t4b3))
        self.wait(2)
        b4a = Tex("Serves production directly / people directly").scale(1.0).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex("Good infrastructure $=$ competitiveness:").scale(1.0).shift(band_shift(4) + DOWN * 2.4)
        b4b2 = Tex("it lowers every firm's costs at once").scale(1.0).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4b))
        self.play(Write(b4b2))
        self.wait(3)

        # --- Band 5 (subtopic_3): strain, and the tax-on-everyone logic ---
        self.next_band(5)
        b5t = Tex("The recent story is strain").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Load shedding, peaking 2023: generators bought,").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5a2 = Tex("costs raised, output cut").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5a))
        self.play(Write(b5a2))
        self.wait(2.5)
        b5b = Tex("Freight rail and ports: exports lost because").scale(1.0).shift(band_shift(5) + DOWN * 0.5)
        b5b2 = Tex("trains and cranes could not move the volumes").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5b))
        self.play(Write(b5b2))
        self.wait(2.5)
        b5c = Tex("Infrastructure failure $=$ a tax on every").scale(1.05).shift(band_shift(5) + DOWN * 2.1)
        b5c2 = Tex("producer at once — fixing it is cheap growth").scale(1.05).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5c))
        self.play(Write(b5c2))
        self.play(Create(SurroundingRectangle(VGroup(b5c, b5c2), color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): access — achievement and gap ---
        self.next_band(6)
        b6t = Tex("Service delivery: achievement and gap").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("$\\approx$ 90\\% of households connected to electricity;").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6a2 = Tex("$\\approx$ 90\\% with piped water near the dwelling").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6a))
        self.play(Write(b6a2))
        self.wait(2.5)
        b6b = Tex("Weakest where poverty is deepest: rural former").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6b2 = Tex("homelands and informal settlements").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6b))
        self.play(Write(b6b2))
        self.wait(2.5)
        b6c = Tex("Digital divide: the poor pay most per rand").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        b6c2 = Tex("of income to be online").scale(1.0).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6c))
        self.play(Write(b6c2))
        self.wait(3)

        # --- Band 7 (subtopic_4): access is opportunity ---
        self.next_band(7)
        b7t = Tex("Access to services is access to opportunity").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("No electricity: no machine, no studying after dark").scale(0.95).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("No transport: the far job does not pay").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("No connectivity: adverts, prices, banking missed").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("Poor access raises the cost of participating —").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        b7d2 = Tex("most for the poor: inequality reproduced").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7d))
        self.play(Write(b7d2))
        self.play(Create(SurroundingRectangle(VGroup(b7d, b7d2), color=GREEN)))
        self.wait(2)
        b7e = Tex("Essay: achievement $+$ number, gap $+$ place, mechanism").scale(0.9).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7e))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 8 (subtopic_5): the plate of chicken and pap ---
        self.next_band(8)
        b8t = Tex("Chicken and pap, run backwards").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Mealies and chicken from farms — primary").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("Mill grinds, plant processes — secondary").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Shop fries, truck delivers, app pays — tertiary").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("Of every R100: services $\\approx$ R65, factories $\\approx$ R20,").scale(0.88).shift(band_shift(8) + DOWN * 1.4)
        b8d2 = Tex("mines and farms under R10 together").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8d))
        self.play(Write(b8d2))
        self.wait(2)
        b8e = Tex("A services economy with famous mines").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8e))
        self.play(Create(SurroundingRectangle(b8e, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): one street, three sectors ---
        self.next_band(9)
        b9t = Tex("One street, all three sectors holding hands").scale(1.1).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Vetkoek: wheat (primary) $\\rightarrow$ mill (secondary)").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9a2 = Tex("$\\rightarrow$ frying, taxi, wholesaler (tertiary)").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9a))
        self.play(Write(b9a2))
        self.wait(2.5)
        b9b = Tex("Harvest fails $\\rightarrow$ flour jumps $\\rightarrow$ smaller vetkoek").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("Eras: mines and farms $\\rightarrow$ factory years $\\rightarrow$ services").scale(0.95).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("Sore point: factories faded before enough").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        b9d2 = Tex("workers found work in them").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9d))
        self.play(Write(b9d2))
        self.play(Create(SurroundingRectangle(b9d2, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the wires and pipes ---
        self.next_band(10)
        b10t = Tex("The wires and pipes decide who plays").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("One blackout: fryers stop, stock spoils,").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10a2 = Tex("card machine dies — every business taxed at once").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10a))
        self.play(Write(b10a2))
        self.wait(2.5)
        b10b = Tex("About 90 in 100 households have electricity").scale(1.0).shift(band_shift(10) + DOWN * 0.5)
        b10b2 = Tex("and water close by — but averages hide the edges").scale(0.95).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10b))
        self.play(Write(b10b2))
        self.wait(2.5)
        b10c = Tex("Services are the entry ticket to the economy:").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        b10c2 = Tex("a missing pipe becomes a missing opportunity").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10c))
        self.play(Write(b10c2))
        self.play(Create(SurroundingRectangle(b10c2, color=GREEN)))
        self.wait(4)
