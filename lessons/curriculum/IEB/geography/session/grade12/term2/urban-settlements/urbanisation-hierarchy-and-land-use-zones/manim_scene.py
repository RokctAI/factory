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

# Band-layout whiteboard scene for the urbanisation, hierarchy and
# land-use zones duo lesson. Exporter-safe primitives only (Tex/Line/
# Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle; camera moves
# down one frame-height per band. The hierarchy pyramid and the zone
# journey are hand-built from Rectangles and Lines in script order.
#
# Subtopic shares (subtopics.json, total 1660 s):
# 225/215/260/280 expert, 210/230/240 simplifier. Bands 0-8 = Part 1
# (two per expert subtopic, three for subtopic_4), bands 9-11 = fresh
# Part 2 bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class UrbanisationLandUseSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): the birth of towns ---
        title = Tex("From first villages to an urban world").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        f1 = Tex(r"Surplus + specialisation + exchange = a town").scale(1.0).shift(UP * 1.3)
        self.play(Write(f1))
        self.play(Create(SurroundingRectangle(f1, color=GREEN)))
        self.wait(2.5)
        f2 = Tex(r"Extra food frees traders, craftsmen, rulers").scale(0.95).shift(UP * 0.3)
        self.play(Write(f2))
        self.wait(2)
        f3 = Tex(r"Cradles: Nile, Tigris-Euphrates, Indus valleys").scale(0.95).shift(DOWN * 0.6)
        self.play(Write(f3))
        self.wait(2)
        f4 = Tex(r"Irrigated floodplains = reliable surplus").scale(0.95).shift(DOWN * 1.5)
        self.play(Write(f4))
        self.wait(3)

        # --- Band 1 (subtopic_1): the industrial gradient + level vs rate ---
        self.next_band(1)
        b1_t = Tex("Factories, and the halfway line").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        g1 = Tex(r"Industrial revolution: factories gather workers").scale(0.9).shift(band_shift(1) + UP * 1.2)
        self.play(Write(g1))
        self.wait(2)
        g2 = Tex(r"Early 2000s: majority of humanity urban").scale(0.9).shift(band_shift(1) + UP * 0.4)
        self.play(Write(g2))
        self.wait(2)
        g3 = Tex(r"Developed: HIGH level, slow rate").scale(0.95).shift(band_shift(1) + DOWN * 0.5)
        g4 = Tex(r"Developing: lower level, RAPID rate").scale(0.95).shift(band_shift(1) + DOWN * 1.3)
        self.play(Write(g3))
        self.wait(2)
        self.play(Write(g4))
        self.play(Create(SurroundingRectangle(g4, color=GREEN)))
        self.wait(2)
        g5 = Tex(r"SA: about two thirds urban, Gauteng the magnet").scale(0.9).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(g5))
        self.wait(3)

        # --- Band 2 (subtopic_2): urbanisation vs growth, rate vs level ---
        self.next_band(2)
        b2_t = Tex("Percentage against number").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        v1 = Tex(r"URBANISATION: rising \% of population urban").scale(0.95).shift(band_shift(2) + UP * 1.2)
        v2 = Tex(r"URBAN GROWTH: rising NUMBER of urban people").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(v1))
        self.wait(2)
        self.play(Write(v2))
        self.wait(2)
        v3 = Tex(r"Equal growth everywhere = growth, no urbanisation").scale(0.9).shift(band_shift(2) + DOWN * 0.5)
        self.play(Write(v3))
        self.play(Create(SurroundingRectangle(v3, color=GREEN)))
        self.wait(2.5)
        v4 = Tex(r"RATE = speed of the climb; LEVEL = the snapshot").scale(0.9).shift(band_shift(2) + DOWN * 1.4)
        self.play(Write(v4))
        self.wait(3)

        # --- Band 3 (subtopic_2): expansion, sprawl, counter-urbanisation ---
        self.next_band(3)
        b3_t = Tex("Expansion, sprawl, and the reverse flow").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        e1 = Tex(r"EXPANSION: built-up area spreads outward").scale(0.95).shift(band_shift(3) + UP * 1.2)
        e2 = Tex(r"SPRAWL: low-density, poorly planned spread —").scale(0.95).shift(band_shift(3) + UP * 0.4)
        e2b = Tex(r"leapfrogging estates, farmland eaten").scale(0.95).shift(band_shift(3) + DOWN * 0.3)
        self.play(Write(e1))
        self.wait(2)
        self.play(Write(e2))
        self.play(Write(e2b))
        self.wait(2.5)
        e3 = Tex(r"All sprawl is expansion; not all expansion is sprawl").scale(0.9).shift(band_shift(3) + DOWN * 1.2)
        self.play(Write(e3))
        self.play(Create(SurroundingRectangle(e3, color=GREEN)))
        self.wait(2)
        e4 = Tex(r"COUNTER-urbanisation: city $\rightarrow$ small town").scale(0.9).shift(band_shift(3) + DOWN * 2.1)
        e4b = Tex(r"(Garden Route, Overberg — lifestyle, price, safety)").scale(0.85).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(e4))
        self.play(Write(e4b))
        self.wait(3)

        # --- Band 4 (subtopic_3): site vs situation — the great pair ---
        self.next_band(4)
        b4_t = Tex("Site, situation: the great pair").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        s1 = Tex(r"Cape Town: fine site (shelter, water, bay)").scale(0.95).shift(band_shift(4) + UP * 1.2)
        s1b = Tex(r"+ fine situation (sea-route resupply)").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        s2 = Tex(r"Johannesburg: poor site, no harbour, no river —").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        s2b = Tex(r"situation on the Witwatersrand gold overruled it").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(s2))
        self.play(Write(s2b))
        self.wait(2.5)
        s3 = Tex(r"Answer site first, then situation — name the winner").scale(0.9).shift(band_shift(4) + DOWN * 2.1)
        self.play(Write(s3))
        self.play(Create(SurroundingRectangle(s3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): functional classification ---
        self.next_band(5)
        b5_t = Tex("Towns classified by their work").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        c1 = Tex(r"Central place: serves its sphere of influence").scale(0.9).shift(band_shift(5) + UP * 1.3)
        c2 = Tex(r"Break-of-bulk: Richards Bay — train to ship").scale(0.9).shift(band_shift(5) + UP * 0.5)
        c3 = Tex(r"Junction: De Aar — where railways meet").scale(0.9).shift(band_shift(5) + DOWN * 0.3)
        c4 = Tex(r"Gateway: Komatipoort — the border door").scale(0.9).shift(band_shift(5) + DOWN * 1.1)
        c5 = Tex(r"Gap: Ceres, Tulbagh — mountain passages").scale(0.9).shift(band_shift(5) + DOWN * 1.9)
        c6 = Tex(r"Specialised: Welkom, Secunda, Hermanus,").scale(0.9).shift(band_shift(5) + DOWN * 2.7)
        c6b = Tex(r"Stellenbosch, Bhisho").scale(0.9).shift(band_shift(5) + DOWN * 3.4)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.wait(2)
        self.play(Write(c5))
        self.wait(2)
        self.play(Write(c6))
        self.play(Write(c6b))
        self.wait(3)

        # --- Band 6 (subtopic_4): the urban hierarchy see-saw ---
        self.next_band(6)
        b6_t = Tex("The hierarchy's see-saw rule").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        # Pyramid of rectangles: wide base, narrow top
        base = Rectangle(width=7.0, height=0.8, color=WHITE).shift(band_shift(6) + DOWN * 1.6)
        base_lab = Tex(r"many villages + small towns: low order").scale(0.8).shift(band_shift(6) + DOWN * 1.6)
        mid = Rectangle(width=4.4, height=0.8, color=WHITE).shift(band_shift(6) + DOWN * 0.7)
        mid_lab = Tex(r"regional towns: hospitals").scale(0.8).shift(band_shift(6) + DOWN * 0.7)
        top = Rectangle(width=2.0, height=0.8, color=WHITE).shift(band_shift(6) + UP * 0.2)
        top_lab = Tex(r"metros").scale(0.8).shift(band_shift(6) + UP * 0.2)
        self.play(Create(base), Write(base_lab))
        self.play(Create(mid), Write(mid_lab))
        self.play(Create(top), Write(top_lab))
        self.wait(2.5)
        h1 = Tex(r"Higher order $\Rightarrow$ larger sphere needed $\Rightarrow$ fewer places").scale(0.85).shift(band_shift(6) + DOWN * 2.6)
        self.play(Write(h1))
        self.play(Create(SurroundingRectangle(h1, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): CBD and transition zone ---
        self.next_band(7)
        b7_t = Tex("CBD and the transition zone").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        z1 = Tex(r"CBD trio: dearest land, tallest buildings,").scale(0.95).shift(band_shift(7) + UP * 1.2)
        z1b = Tex(r"greatest accessibility").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(z1))
        self.play(Write(z1b))
        self.play(Create(SurroundingRectangle(z1b, color=GREEN)))
        self.wait(2.5)
        z2 = Tex(r"Crowded by day, hollow by night").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(z2))
        self.wait(2)
        z3 = Tex(r"Transition ring: subdivided houses, light industry,").scale(0.9).shift(band_shift(7) + DOWN * 1.3)
        z3b = Tex(r"decay beside gentrification — the city rebuilding").scale(0.9).shift(band_shift(7) + DOWN * 2.0)
        self.play(Write(z3))
        self.play(Write(z3b))
        self.wait(3)

        # --- Band 8 (subtopic_4): residential gradient, industry, nodes ---
        self.next_band(8)
        b8_t = Tex("Residents, industry, and the nodes").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        r1 = Tex(r"Model: income rises outward — history deformed it:").scale(0.85).shift(band_shift(8) + UP * 1.3)
        r1b = Tex(r"townships pushed to the far edge, behind buffers").scale(0.85).shift(band_shift(8) + UP * 0.6)
        self.play(Write(r1))
        self.play(Write(r1b))
        self.wait(2.5)
        r2 = Tex(r"Longest, costliest commutes for the poorest").scale(0.9).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(r2))
        self.play(Create(SurroundingRectangle(r2, color=GREEN)))
        self.wait(2)
        r3 = Tex(r"Heavy industry: rail, highway, harbour, flat land").scale(0.85).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(r3))
        self.wait(2)
        r4 = Tex(r"Nodes: Menlyn, uMhlanga Ridge, Canal Walk —").scale(0.85).shift(band_shift(8) + DOWN * 2.0)
        r4b = Tex(r"CBD functions chasing highways and spenders").scale(0.85).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(r4))
        self.play(Write(r4b))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 9 (subtopic_5): why cities exist ---
        self.next_band(9)
        b9_t = Tex("Why cities exist").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        y1 = Tex(r"Extra food $\rightarrow$ divided jobs $\rightarrow$ a marketplace").scale(0.9).shift(band_shift(9) + UP * 1.2)
        self.play(Write(y1))
        self.play(Create(SurroundingRectangle(y1, color=GREEN)))
        self.wait(2.5)
        y2 = Tex(r"Factories: gathering machines at one gate").scale(0.9).shift(band_shift(9) + UP * 0.3)
        self.play(Write(y2))
        self.wait(2)
        y3 = Tex(r"Early 2000s: the world crossed the halfway line").scale(0.9).shift(band_shift(9) + DOWN * 0.6)
        self.play(Write(y3))
        self.wait(2)
        y4 = Tex(r"Parked car = developed; climbing car = developing").scale(0.9).shift(band_shift(9) + DOWN * 1.5)
        y4b = Tex(r"LEVEL = where you are; RATE = how fast you climb").scale(0.9).shift(band_shift(9) + DOWN * 2.3)
        self.play(Write(y4))
        self.play(Write(y4b))
        self.wait(3)

        # --- Band 10 (subtopic_6): the ladder of shops ---
        self.next_band(10)
        b10_t = Tex("The ladder of shops").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        x1 = Tex(r"Bread: the spaza. Shoes: town.").scale(0.95).shift(band_shift(10) + UP * 1.2)
        x2 = Tex(r"Specialist doctor: the city. Transplant: one place").scale(0.9).shift(band_shift(10) + UP * 0.4)
        self.play(Write(x1))
        self.wait(2)
        self.play(Write(x2))
        self.wait(2)
        x3 = Tex(r"Ordinary = near and common; special = far and few").scale(0.9).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(x3))
        self.play(Create(SurroundingRectangle(x3, color=GREEN)))
        self.wait(2.5)
        x4 = Tex(r"Jobs: shopkeeper, cargo-changer, junction,").scale(0.9).shift(band_shift(10) + DOWN * 1.4)
        x4b = Tex(r"border door, mountain doorway, one-trick towns").scale(0.9).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(x4))
        self.play(Write(x4b))
        self.wait(2)
        x5 = Tex(r"Joburg forgave its site — the gold was reason enough").scale(0.85).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(x5))
        self.wait(3)

        # --- Band 11 (subtopic_7): a taxi ride across the zones ---
        self.next_band(11)
        b11_t = Tex("A taxi ride across the zones").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        t1 = Tex(r"Downtown: tug-of-war land $\rightarrow$ stacked towers").scale(0.9).shift(band_shift(11) + UP * 1.2)
        self.play(Write(t1))
        self.wait(2)
        t2 = Tex(r"Next ring: half building site, half waiting room").scale(0.9).shift(band_shift(11) + UP * 0.4)
        self.play(Write(t2))
        self.wait(2)
        t3 = Tex(r"Then houses — with apartheid's rearranged seats:").scale(0.9).shift(band_shift(11) + DOWN * 0.5)
        t3b = Tex(r"townships far out, buffers and rail between").scale(0.9).shift(band_shift(11) + DOWN * 1.2)
        self.play(Write(t3))
        self.play(Write(t3b))
        self.play(Create(SurroundingRectangle(t3b, color=GREEN)))
        self.wait(2.5)
        t4 = Tex(r"Factory belts along rail and highway").scale(0.9).shift(band_shift(11) + DOWN * 2.1)
        self.play(Write(t4))
        self.wait(2)
        t5 = Tex(r"Last stop: the mall node that ate the CBD's lunch").scale(0.9).shift(band_shift(11) + DOWN * 2.9)
        self.play(Write(t5))
        self.wait(4)
