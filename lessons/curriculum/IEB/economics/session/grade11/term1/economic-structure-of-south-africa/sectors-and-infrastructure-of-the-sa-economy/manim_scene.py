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

# Band-layout whiteboard scene for "Sectors and Infrastructure of the SA
# Economy" (IEB). (Part 1 — Expert subtopics 1-4, Part 2 — Simplifier 5-7.)
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
        d0a = Tex("manganese, cane, rooibos, pilchards").scale(0.75).shift(UP * 0.9 + RIGHT * 1.7)
        self.play(Write(d0a))
        self.wait(2)
        r0b = Rectangle(width=3.6, height=1.4).shift(DOWN * 0.8 + LEFT * 4.6)
        t0b = Tex("Secondary").scale(0.85).move_to(r0b.get_center() + UP * 0.3)
        t0b2 = Tex("transform goods").scale(0.7).move_to(r0b.get_center() + DOWN * 0.35)
        a0a = Arrow(r0a.get_bottom(), r0b.get_top(), buff=0.1)
        self.play(Create(a0a), Create(r0b), Write(t0b), Write(t0b2))
        d0b = Tex("cars, sugar, cement, construction").scale(0.78).shift(DOWN * 0.8 + RIGHT * 1.7)
        self.play(Write(d0b))
        self.wait(2)
        r0c = Rectangle(width=3.6, height=1.4).shift(DOWN * 2.5 + LEFT * 4.6)
        t0c = Tex("Tertiary").scale(0.85).move_to(r0c.get_center() + UP * 0.3)
        t0c2 = Tex("services").scale(0.7).move_to(r0c.get_center() + DOWN * 0.35)
        a0b = Arrow(r0b.get_bottom(), r0c.get_top(), buff=0.1)
        self.play(Create(a0b), Create(r0c), Write(t0c), Write(t0c2))
        d0c = Tex("insurance, taxis, tour guides, teachers").scale(0.75).shift(DOWN * 2.5 + RIGHT * 1.9)
        self.play(Write(d0c))
        self.wait(3)

        # --- Band 1 (subtopic_1): the shares, and the jobs warning ---
        self.next_band(1)
        b1t = Tex("The South African shares of GDP").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("Services: roughly two thirds — the colossus").scale(1.05).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2)
        b1b = Tex("Secondary: about one fifth; manufacturing $\\approx$ 13\\%").scale(0.95).shift(band_shift(1) + UP * 0.3)
        self.play(Write(b1b))
        self.wait(2)
        b1c = Tex("Primary smallest: mining $\\approx$ 6\\%, agriculture $\\approx$ 3\\%").scale(0.84).shift(band_shift(1) + DOWN * 0.5)
        self.play(Write(b1c))
        self.wait(2)
        b1w = Tex("Small GDP share $=$ sector does not matter").scale(1.0).shift(band_shift(1) + DOWN * 1.5)
        self.play(Write(b1w))
        self.play(Create(strike(b1w)))
        self.wait(1.5)
        b1d = Tex("Rand scoreboard and jobs scoreboard differ").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(b1d))
        self.play(Create(SurroundingRectangle(b1d, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): one cup of tea through the chain ---
        self.next_band(2)
        b2t = Tex("One cup of rooibos, three sectors").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        s2a = Tex("Farmer cuts the bush").scale(0.85).shift(band_shift(2) + UP * 1.0 + LEFT * 4.5)
        s2b = Tex("Plant dries and packs").scale(0.85).shift(band_shift(2) + UP * 1.0)
        s2c = Tex("Truck, shop, bank sell").scale(0.85).shift(band_shift(2) + UP * 1.0 + RIGHT * 4.4)
        a2a = Arrow(s2a.get_right(), s2b.get_left(), buff=0.15)
        a2b = Arrow(s2b.get_right(), s2c.get_left(), buff=0.15)
        self.play(Write(s2a))
        self.play(Create(a2a), Write(s2b))
        self.play(Create(a2b), Write(s2c))
        self.wait(2)
        l2a = Tex("primary").scale(0.8).shift(band_shift(2) + UP * 0.3 + LEFT * 4.5)
        l2b = Tex("secondary").scale(0.8).shift(band_shift(2) + UP * 0.3)
        l2c = Tex("tertiary").scale(0.8).shift(band_shift(2) + UP * 0.3 + RIGHT * 4.4)
        self.play(Write(l2a), Write(l2b), Write(l2c))
        self.wait(2)
        b2a = Tex("Value added at every station — interdependence").scale(1.0).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2a))
        self.wait(2)
        b2b = Tex("A withered harvest idles the packing line").scale(1.0).shift(band_shift(2) + DOWN * 1.7)
        b2b2 = Tex("and thins out the shop's shelf").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2b))
        self.play(Write(b2b2))
        self.wait(3)

        # --- Band 3 (subtopic_2): structural transformation and its defect ---
        self.next_band(3)
        b3t = Tex("The structure rebuilt twice — with a defect").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3t))
        self.wait(2)
        s3a = Tex("Mines and farms").scale(0.85).shift(band_shift(3) + UP * 1.1 + LEFT * 4.5)
        s3b = Tex("Factory decades").scale(0.85).shift(band_shift(3) + UP * 1.1)
        s3c = Tex("Services era").scale(0.85).shift(band_shift(3) + UP * 1.1 + RIGHT * 4.3)
        a3a = Arrow(s3a.get_right(), s3b.get_left(), buff=0.15)
        a3b = Arrow(s3b.get_right(), s3c.get_left(), buff=0.15)
        self.play(Write(s3a))
        self.play(Create(a3a), Write(s3b))
        self.play(Create(a3b), Write(s3c))
        self.wait(2)
        b3a = Tex("Structural transformation: the maturing walk").scale(1.0).shift(band_shift(3) + UP * 0.2)
        self.play(Write(b3a))
        self.wait(2)
        b3b = Tex("SA defect: manufacturing above 20\\% (early 1990s)").scale(0.95).shift(band_shift(3) + DOWN * 0.7)
        b3b2 = Tex("$\\rightarrow$ roughly 13\\% today").scale(1.0).shift(band_shift(3) + DOWN * 1.4)
        self.play(Write(b3b))
        self.play(Write(b3b2))
        self.wait(2)
        b3c = Tex("Premature deindustrialisation: the factory era faded").scale(0.92).shift(band_shift(3) + DOWN * 2.3)
        b3c2 = Tex("before employing the semi-skilled workers who need it").scale(0.92).shift(band_shift(3) + DOWN * 3.0)
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
        t4a2 = Tex("grid, rail, roads,").scale(0.75).move_to(r4a.get_center())
        t4a3 = Tex("harbours, dams, fibre").scale(0.75).move_to(r4a.get_center() + DOWN * 0.7)
        self.play(Create(r4a), Write(t4a), Write(t4a2), Write(t4a3))
        self.wait(2)
        r4b = Rectangle(width=5.6, height=2.4).shift(band_shift(4) + UP * 0.2 + RIGHT * 3.4)
        t4b = Tex("Social:").scale(0.85).move_to(r4b.get_center() + UP * 0.7)
        t4b2 = Tex("schools, clinics,").scale(0.75).move_to(r4b.get_center())
        t4b3 = Tex("housing, sanitation").scale(0.75).move_to(r4b.get_center() + DOWN * 0.7)
        self.play(Create(r4b), Write(t4b), Write(t4b2), Write(t4b3))
        self.wait(2)
        b4a = Tex("Production served directly / people served directly").scale(0.95).shift(band_shift(4) + DOWN * 1.5)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex("The prize is competitiveness: one shared asset").scale(1.0).shift(band_shift(4) + DOWN * 2.4)
        b4b2 = Tex("cuts costs for every firm simultaneously").scale(1.0).shift(band_shift(4) + DOWN * 3.1)
        self.play(Write(b4b))
        self.play(Write(b4b2))
        self.wait(3)

        # --- Band 5 (subtopic_3): strain, and the tax-on-everyone logic ---
        self.next_band(5)
        b5t = Tex("The endowment under strain").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5t))
        self.wait(2)
        b5a = Tex("Load shedding, worst in 2023: generators and solar").scale(0.95).shift(band_shift(5) + UP * 1.1)
        b5a2 = Tex("bought, costs lifted, output cut").scale(1.0).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5a))
        self.play(Write(b5a2))
        self.wait(2.5)
        b5b = Tex("Freight: buyers lost, not for lack of ore, but because").scale(0.92).shift(band_shift(5) + DOWN * 0.5)
        b5b2 = Tex("locomotives and cranes could not shift the tonnage").scale(0.92).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5b))
        self.play(Write(b5b2))
        self.wait(2.5)
        b5c = Tex("Shared-infrastructure failure $=$ a tax on every").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        b5c2 = Tex("producer at once — restoring it is cheap growth").scale(1.0).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5c))
        self.play(Write(b5c2))
        self.play(Create(SurroundingRectangle(VGroup(b5c, b5c2), color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): access — achievement and gap ---
        self.next_band(6)
        b6t = Tex("Service delivery: achievement and gap").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(2)
        b6a = Tex("$\\approx$ 90\\% of households with an electricity connection;").scale(0.92).shift(band_shift(6) + UP * 1.1)
        b6a2 = Tex("$\\approx$ 90\\% with piped water in or near the home").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6a))
        self.play(Write(b6a2))
        self.wait(2.5)
        b6b = Tex("Gaps cluster where incomes are lowest: rural former").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6b2 = Tex("homelands and informal settlements").scale(1.0).shift(band_shift(6) + DOWN * 1.2)
        self.play(Write(b6b))
        self.play(Write(b6b2))
        self.wait(2.5)
        b6c = Tex("Digital divide: the smallest incomes pay the most,").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        b6c2 = Tex("per rand earned, for every hour online").scale(0.95).shift(band_shift(6) + DOWN * 2.8)
        self.play(Write(b6c))
        self.play(Write(b6c2))
        self.wait(3)

        # --- Band 7 (subtopic_4): access is opportunity ---
        self.next_band(7)
        b7t = Tex("Access to services is access to opportunity").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("No electricity: no overlocker, no revising after sunset").scale(0.9).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("No transport: the distant vacancy is fictional").scale(0.95).shift(band_shift(7) + UP * 0.3)
        self.play(Write(b7b))
        self.wait(2)
        b7c = Tex("No data: adverts, prices, banking out of sight").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("Weak access raises the price of participating —").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        b7d2 = Tex("steepest for the poor: inequality copied forward").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(b7d))
        self.play(Write(b7d2))
        self.play(Create(SurroundingRectangle(VGroup(b7d, b7d2), color=GREEN)))
        self.wait(2)
        b7e = Tex("Argument: achievement $+$ number, gap $+$ place, mechanism").scale(0.85).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(b7e))
        self.wait(3)

        # ===================== Part 2 — Simplifier =====================
        # --- Band 8 (subtopic_5): the cup of tea run backwards ---
        self.next_band(8)
        b8t = Tex("A cup of rooibos, run backwards").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Bush grown and cut on the farm — primary").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("Plant ferments, dries, packs — secondary").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Truck hauls, shop sells, card pays — tertiary").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("Of every R100: services $\\approx$ R65, factories $\\approx$ R20,").scale(0.88).shift(band_shift(8) + DOWN * 1.4)
        b8d2 = Tex("mines and farms less than R10 combined").scale(0.95).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8d))
        self.play(Write(b8d2))
        self.wait(2)
        b8e = Tex("A services economy that owns famous mines").scale(1.0).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8e))
        self.play(Create(SurroundingRectangle(b8e, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): one street, three sectors ---
        self.next_band(9)
        b9t = Tex("One market, all three sectors holding hands").scale(1.05).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("Boerewors roll: cattle (primary) $\\rightarrow$ abattoir,").scale(0.92).shift(band_shift(9) + UP * 1.1)
        b9a2 = Tex("bakery (secondary) $\\rightarrow$ stall, gas, app (tertiary)").scale(0.92).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9a))
        self.play(Write(b9a2))
        self.wait(2.5)
        b9b = Tex("Auctions close $\\rightarrow$ wors price climbs $\\rightarrow$ smaller roll").scale(0.9).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("Eras: mines and farms $\\rightarrow$ factory decades $\\rightarrow$ services").scale(0.9).shift(band_shift(9) + DOWN * 1.4)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("The bruise: factories emptied before enough").scale(1.0).shift(band_shift(9) + DOWN * 2.3)
        b9d2 = Tex("people had ever worked in them").scale(1.0).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9d))
        self.play(Write(b9d2))
        self.play(Create(SurroundingRectangle(b9d2, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the wires and pipes ---
        self.next_band(10)
        b10t = Tex("The wires and pipes decide who plays").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("One power cut: clippers die, fridges warm,").scale(1.0).shift(band_shift(10) + UP * 1.1)
        b10a2 = Tex("screens black — the whole corner taxed in a minute").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10a))
        self.play(Write(b10a2))
        self.wait(2.5)
        b10b = Tex("About 90 in 100 households have electricity and").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10b2 = Tex("water close by — but averages dissolve at the edges").scale(0.92).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10b))
        self.play(Write(b10b2))
        self.wait(2.5)
        b10c = Tex("Services are the ticket at the economy's gate:").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        b10c2 = Tex("a missing pipe becomes a missing chance").scale(1.0).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10c))
        self.play(Write(b10c2))
        self.play(Create(SurroundingRectangle(b10c2, color=GREEN)))
        self.wait(4)
