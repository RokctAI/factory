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

# Band-layout whiteboard scene for "Magnets and Magnetic Fields" (Part 1 —
# Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7). Exporter-safe
# mobjects only; the domain sketches, bar-magnet field pattern and two-magnet
# pictures are hand-built from Rectangles, Lines and Arrows (field arcs are
# short line-segment chains). Add-only lifecycle. Band time apportioned to
# subtopics.json (230/240/240/250/180/190/190 of 1520 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class MagnetsAndMagneticFieldsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays (~4-5%).
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): force without touching ---
        title = Tex("Magnets and Magnetic Fields").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex("The clip jumps the gap — nothing crosses it").scale(1.05).shift(UP * 0.9)
        self.play(Write(d1))
        self.wait(2.5)
        d2 = Tex("Magnetic field: a region in space where").scale(1.05).shift(DOWN * 0.2)
        d3 = Tex("a magnet or ferromagnetic material feels a force").scale(1.0).shift(DOWN * 1.1)
        self.play(Write(d2))
        self.play(Write(d3))
        self.play(Create(SurroundingRectangle(VGroup(d2, d3), color=GREEN)))
        self.wait(3)
        d4 = Tex("A volume of influence — invisible and real").scale(1.0).shift(DOWN * 2.4)
        self.play(Write(d4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the family of fields ---
        self.next_band(1)
        b1t = Tex("Three fields, one pattern").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(2)
        b1a = Tex("Gravitational: acts on mass, only attracts").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1a))
        self.wait(2)
        b1b = Tex("Electric: acts on charge — attracts or repels").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1b))
        self.wait(2)
        b1c = Tex("Magnetic: poles — but the pair never separates").scale(1.0).shift(band_shift(1) + DOWN * 0.7)
        self.play(Write(b1c))
        self.wait(2.5)
        b1d = Tex("Ferromagnetic: iron, steel, cobalt, nickel").scale(1.0).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1d))
        self.play(Create(SurroundingRectangle(b1d, color=GREEN)))
        self.wait(2)
        b1e = Tex("Copper, aluminium, glass, paper: indifferent").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1e))
        self.wait(3)

        # --- Band 2 (subtopic_2): poles and the interaction rule ---
        self.next_band(2)
        b2t = Tex("Poles come in pairs").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(2)
        b2a = Tex("Hung from a thread, the north-seeking end $=$ N").scale(0.95).shift(band_shift(2) + UP * 1.1)
        self.play(Write(b2a))
        self.wait(2.5)
        b2b = Tex("Like poles repel").scale(1.1).shift(band_shift(2) + UP * 0.1)
        self.play(Write(b2b))
        self.wait(2)
        b2c = Tex("Opposite poles attract").scale(1.1).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2c))
        self.play(Create(SurroundingRectangle(VGroup(b2b, b2c), color=GREEN)))
        self.wait(2.5)
        b2d = Tex("A lone pole — a monopole — has never been found").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2d))
        self.wait(3)

        # --- Band 3 (subtopic_2): cutting, and the domain picture ---
        self.next_band(3)
        b3t = Tex("Cut it in half — and fail").scale(1.2).shift(band_shift(3) + UP * 2.4)
        self.play(Write(b3t))
        self.wait(2)
        b3a = Tex("Every piece, down to dust, has BOTH poles").scale(1.0).shift(band_shift(3) + UP * 1.4)
        self.play(Write(b3a))
        self.wait(2.5)
        # domain sketches: unmagnetised (random arrows) vs magnetised (aligned)
        n1 = Rectangle(width=3.6, height=1.6).shift(band_shift(3) + LEFT * 2.6 + DOWN * 0.4)
        n1l = Tex("unmagnetised").scale(0.8).move_to(band_shift(3) + LEFT * 2.6 + DOWN * 1.6)
        r1 = Arrow(n1.get_center() + LEFT * 1.3 + DOWN * 0.3, n1.get_center() + LEFT * 0.7 + UP * 0.3, buff=0, stroke_width=4)
        r2 = Arrow(n1.get_center() + UP * 0.4, n1.get_center() + LEFT * 0.1 + DOWN * 0.3, buff=0, stroke_width=4)
        r3 = Arrow(n1.get_center() + RIGHT * 0.5 + DOWN * 0.4, n1.get_center() + RIGHT * 1.2 + DOWN * 0.1, buff=0, stroke_width=4)
        r4 = Arrow(n1.get_center() + RIGHT * 1.3 + UP * 0.4, n1.get_center() + RIGHT * 0.6 + UP * 0.2, buff=0, stroke_width=4)
        self.play(Create(n1), Write(n1l))
        self.play(Create(r1), Create(r2), Create(r3), Create(r4))
        self.wait(2)
        n2 = Rectangle(width=3.6, height=1.6).shift(band_shift(3) + RIGHT * 2.6 + DOWN * 0.4)
        n2l = Tex("magnetised: domains aligned").scale(0.8).move_to(band_shift(3) + RIGHT * 2.6 + DOWN * 1.6)
        a1 = Arrow(n2.get_center() + LEFT * 1.4 + UP * 0.4, n2.get_center() + LEFT * 0.4 + UP * 0.4, buff=0, stroke_width=4, color=YELLOW)
        a2 = Arrow(n2.get_center() + LEFT * 1.4 + DOWN * 0.4, n2.get_center() + LEFT * 0.4 + DOWN * 0.4, buff=0, stroke_width=4, color=YELLOW)
        a3 = Arrow(n2.get_center() + RIGHT * 0.2 + UP * 0.4, n2.get_center() + RIGHT * 1.2 + UP * 0.4, buff=0, stroke_width=4, color=YELLOW)
        a4 = Arrow(n2.get_center() + RIGHT * 0.2 + DOWN * 0.4, n2.get_center() + RIGHT * 1.2 + DOWN * 0.4, buff=0, stroke_width=4, color=YELLOW)
        self.play(Create(n2), Write(n2l))
        self.play(Create(a1), Create(a2), Create(a3), Create(a4))
        self.wait(2.5)
        b3b = Tex("One pattern runs through the whole metal").scale(1.0).shift(band_shift(3) + DOWN * 2.7)
        self.play(Write(b3b))
        self.wait(3)

        # --- Band 4 (subtopic_3): the four field-line rules ---
        self.next_band(4)
        b4t = Tex("Field lines: the four rules").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4t))
        self.wait(2)
        b4a = Tex("1. Run N $\\to$ S outside the magnet, arrowed").scale(1.0).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4a))
        self.wait(2)
        b4b = Tex("2. Close together $=$ strong; spread $=$ weak").scale(1.0).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4b))
        self.wait(2)
        b4c = Tex("3. Field lines never cross").scale(1.0).shift(band_shift(4) + DOWN * 0.7)
        self.play(Write(b4c))
        self.wait(2)
        b4d = Tex("4. The field is 3-D; the page flattens it").scale(1.0).shift(band_shift(4) + DOWN * 1.6)
        self.play(Write(b4d))
        self.wait(2)
        b4e = Tex("Filings show shape; compasses show direction").scale(0.95).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4e))
        self.wait(3)

        # --- Band 5 (subtopic_3): the bar-magnet pattern, drawn ---
        self.next_band(5)
        b5t = Tex("The bar magnet's fountain").scale(1.2).shift(band_shift(5) + UP * 2.6)
        self.play(Write(b5t))
        self.wait(2)
        c5 = band_shift(5) + DOWN * 0.4
        bar = Rectangle(width=2.6, height=0.8).move_to(c5)
        ln = MathTex(r"\text{N}").scale(0.9).move_to(c5 + RIGHT * 0.9)
        ls = MathTex(r"\text{S}").scale(0.9).move_to(c5 + LEFT * 0.9)
        self.play(Create(bar), Write(ln), Write(ls))
        self.wait(2)
        top = VGroup(
            Line(c5 + RIGHT * 1.5 + UP * 0.3, c5 + RIGHT * 2.6 + UP * 1.3, stroke_width=4, color=YELLOW),
            Line(c5 + RIGHT * 2.6 + UP * 1.3, c5 + UP * 2.2, stroke_width=4, color=YELLOW),
            Arrow(c5 + UP * 2.2, c5 + LEFT * 2.6 + UP * 1.3, buff=0, stroke_width=4, color=YELLOW),
            Line(c5 + LEFT * 2.6 + UP * 1.3, c5 + LEFT * 1.5 + UP * 0.3, stroke_width=4, color=YELLOW),
        )
        self.play(Create(top), run_time=2)
        self.wait(1.5)
        bot = VGroup(
            Line(c5 + RIGHT * 1.5 + DOWN * 0.3, c5 + RIGHT * 2.6 + DOWN * 1.3, stroke_width=4, color=YELLOW),
            Line(c5 + RIGHT * 2.6 + DOWN * 1.3, c5 + DOWN * 2.2, stroke_width=4, color=YELLOW),
            Arrow(c5 + DOWN * 2.2, c5 + LEFT * 2.6 + DOWN * 1.3, buff=0, stroke_width=4, color=YELLOW),
            Line(c5 + LEFT * 2.6 + DOWN * 1.3, c5 + LEFT * 1.5 + DOWN * 0.3, stroke_width=4, color=YELLOW),
        )
        self.play(Create(bot), run_time=2)
        self.wait(2)
        b5a = Tex("Dense at the poles, spreading with distance").scale(0.95).move_to(band_shift(5) + DOWN * 3.0)
        self.play(Write(b5a))
        self.wait(3)

        # --- Band 6 (subtopic_3): two magnets together ---
        self.next_band(6)
        b6t = Tex("Two magnets: the exam's favourite pictures").scale(1.05).shift(band_shift(6) + UP * 2.4)
        self.play(Write(b6t))
        self.wait(2)
        # attraction: N facing S, lines bridge the gap
        mA = Rectangle(width=2.0, height=0.7).shift(band_shift(6) + LEFT * 2.6 + UP * 1.0)
        mAl = MathTex(r"\text{N}").scale(0.8).move_to(band_shift(6) + LEFT * 1.85 + UP * 1.0)
        mB = Rectangle(width=2.0, height=0.7).shift(band_shift(6) + RIGHT * 2.6 + UP * 1.0)
        mBl = MathTex(r"\text{S}").scale(0.8).move_to(band_shift(6) + RIGHT * 1.85 + UP * 1.0)
        g1 = Arrow(band_shift(6) + LEFT * 1.5 + UP * 1.0, band_shift(6) + RIGHT * 1.5 + UP * 1.0, buff=0, stroke_width=4, color=YELLOW)
        g2 = Line(band_shift(6) + LEFT * 1.5 + UP * 1.3, band_shift(6) + RIGHT * 1.5 + UP * 1.3, stroke_width=3, color=YELLOW)
        g3 = Line(band_shift(6) + LEFT * 1.5 + UP * 0.7, band_shift(6) + RIGHT * 1.5 + UP * 0.7, stroke_width=3, color=YELLOW)
        atl = Tex("lines bridge the gap: attraction").scale(0.9).move_to(band_shift(6) + UP * 0.1)
        self.play(Create(mA), Write(mAl), Create(mB), Write(mBl))
        self.play(Create(g1), Create(g2), Create(g3))
        self.play(Write(atl))
        self.wait(2.5)
        # repulsion: N facing N, lines bend away, neutral point between
        mC = Rectangle(width=2.0, height=0.7).shift(band_shift(6) + LEFT * 2.6 + DOWN * 1.6)
        mCl = MathTex(r"\text{N}").scale(0.8).move_to(band_shift(6) + LEFT * 1.85 + DOWN * 1.6)
        mD = Rectangle(width=2.0, height=0.7).shift(band_shift(6) + RIGHT * 2.6 + DOWN * 1.6)
        mDl = MathTex(r"\text{N}").scale(0.8).move_to(band_shift(6) + RIGHT * 1.85 + DOWN * 1.6)
        h1 = Line(band_shift(6) + LEFT * 1.5 + DOWN * 1.5, band_shift(6) + LEFT * 0.9 + DOWN * 0.9, stroke_width=3, color=YELLOW)
        h2 = Line(band_shift(6) + LEFT * 1.5 + DOWN * 1.7, band_shift(6) + LEFT * 0.9 + DOWN * 2.3, stroke_width=3, color=YELLOW)
        h3 = Line(band_shift(6) + RIGHT * 1.5 + DOWN * 1.5, band_shift(6) + RIGHT * 0.9 + DOWN * 0.9, stroke_width=3, color=YELLOW)
        h4 = Line(band_shift(6) + RIGHT * 1.5 + DOWN * 1.7, band_shift(6) + RIGHT * 0.9 + DOWN * 2.3, stroke_width=3, color=YELLOW)
        np_dot = Dot(band_shift(6) + DOWN * 1.6, radius=0.07)
        npl = Tex("neutral point").scale(0.8).move_to(band_shift(6) + DOWN * 2.7)
        self.play(Create(mC), Write(mCl), Create(mD), Write(mDl))
        self.play(Create(h1), Create(h2), Create(h3), Create(h4))
        self.play(Create(np_dot), Write(npl))
        self.wait(3)

        # --- Band 7 (subtopic_4): the Earth is a magnet ---
        self.next_band(7)
        b7t = Tex("The Earth is a magnet").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex("A compass: a small magnet on a pivot").scale(1.05).shift(band_shift(7) + UP * 1.1)
        self.play(Write(b7a))
        self.wait(2)
        b7b = Tex("It aligns with the planet's field lines").scale(1.05).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7b))
        self.wait(2.5)
        b7c = Tex("Needle's north points north; opposites attract...").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7c))
        self.wait(2)
        b7d = Tex("...so `magnetic north' is magnetically a SOUTH").scale(0.95).shift(band_shift(7) + DOWN * 1.7)
        self.play(Write(b7d))
        self.play(Create(SurroundingRectangle(b7d, color=GREEN)))
        self.wait(2.5)
        b7e = Tex("Two norths: the map's and the needle's — drifting").scale(0.9).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7e))
        self.wait(3)

        # --- Band 8 (subtopic_4): the shield in the sky ---
        self.next_band(8)
        b8t = Tex("The field as a shield").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex("Solar wind: charged particles streaming out").scale(1.0).shift(band_shift(8) + UP * 1.1)
        self.play(Write(b8a))
        self.wait(2)
        b8b = Tex("The field deflects it around the planet").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex("Funnelled to the poles: AURORAS glow").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8c))
        self.wait(2)
        b8d = Tex("Solar eruptions $\\to$ magnetic storms:").scale(1.0).shift(band_shift(8) + DOWN * 1.6)
        b8e = Tex("radio, satellites and power grids stumble").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8d))
        self.play(Write(b8e))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): the invisible bubble ---
        self.next_band(9)
        b9t = Tex("The invisible bubble").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex("The fridge grabs the magnet BEFORE they touch").scale(1.0).shift(band_shift(9) + UP * 1.1)
        self.play(Write(b9a))
        self.wait(2.5)
        b9b = Tex("A bubble of influence — strongest up close").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9b))
        self.wait(2)
        b9c = Tex("You know two others: gravity and the balloon").scale(1.0).shift(band_shift(9) + DOWN * 0.7)
        self.play(Write(b9c))
        self.wait(2)
        b9d = Tex("Guest list: iron, steel, cobalt, nickel").scale(1.0).shift(band_shift(9) + DOWN * 1.6)
        self.play(Write(b9d))
        self.play(Create(SurroundingRectangle(b9d, color=GREEN)))
        self.wait(2)
        b9e = Tex("Paper is invisible; the steel does the work").scale(1.0).shift(band_shift(9) + DOWN * 2.6)
        self.play(Write(b9e))
        self.wait(3)

        # --- Band 10 (subtopic_6): the pin you cannot divorce ---
        self.next_band(10)
        b10t = Tex("The pin you cannot divorce").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10t))
        self.wait(2)
        b10a = Tex("Snip the pin: a new south appears at the cut").scale(1.0).shift(band_shift(10) + UP * 1.1)
        self.play(Write(b10a))
        self.wait(2.5)
        b10b = Tex("Grind to powder: every speck has both poles").scale(1.0).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10b))
        self.wait(2.5)
        b10c = Tex("Domains: a stadium crowd doing the same wave").scale(1.0).shift(band_shift(10) + DOWN * 0.8)
        self.play(Write(b10c))
        self.play(Create(SurroundingRectangle(b10c, color=GREEN)))
        self.wait(2.5)
        b10d = Tex("Dropping shakes domains loose — weaker magnet").scale(0.95).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10d))
        self.wait(2)
        b10e = Tex("Stroking talks them into line — magnetised").scale(0.95).shift(band_shift(10) + DOWN * 2.8)
        self.play(Write(b10e))
        self.wait(3)

        # --- Band 11 (subtopic_7): the needle that knows north ---
        self.next_band(11)
        b11t = Tex("The needle that knows north").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11t))
        self.wait(2)
        b11a = Tex("Float it on still water: it settles north-south").scale(1.0).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11a))
        self.wait(2)
        b11b = Tex("Who turns it? The planet's own field").scale(1.0).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11b))
        self.wait(2.5)
        b11c = Tex("The Arctic spot it seeks acts as a SOUTH pole").scale(1.0).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11c))
        self.play(Create(SurroundingRectangle(b11c, color=GREEN)))
        self.wait(2.5)
        b11d = Tex("The field: windscreen against the solar hail").scale(1.0).shift(band_shift(11) + DOWN * 1.8)
        self.play(Write(b11d))
        self.wait(2)
        b11e = Tex("Auroras: the shield made visible").scale(1.0).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11e))
        self.wait(4)
