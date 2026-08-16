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

# Band-layout whiteboard scene for the CAPS Grade 12 Geography session duo
# "Settlement, Economic Geography and Mapwork Essentials" (term 4 revision,
# week two). Bands cover all seven subtopics (Part 1 — Expert: subtopics 1-4;
# Part 2 — Simplifier: subtopics 5-7) with dwell time proportional to
# subtopics.json (250/260/260/260/200/200/210 of 1640 s). The South African
# city strip and the calculation recipes are hand-built from exporter-safe
# primitives only (Tex/MathTex/Line/Arrow/Dot/Rectangle/VGroup); add-only
# lifecycle, the camera moves down between bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SettlementEconomyMapworkEssentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(15)

        # --- Band 0 (subtopic_1): site, situation and the rural world ---
        title = Tex("Settlement, Economy and Mapwork Essentials").scale(1.1).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Site: the land the settlement stands on").scale(1.0).shift(UP * 0.9)
        b0_l2 = Tex(r"Situation: its position among rivers,").scale(1.0).shift(UP * 0.2)
        b0_l3 = Tex(r"routes, resources and other towns").scale(1.0).shift(DOWN * 0.5)
        for m in (b0_l1, b0_l2, b0_l3):
            self.play(Write(m))
            self.wait(1.7)
        b0_l4 = Tex(r"Site starts the town; situation grows it").scale(1.0).shift(DOWN * 1.4)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = Tex(r"Rural patterns: nucleated or dispersed;").scale(0.95).shift(DOWN * 2.3)
        b0_l6 = Tex(r"round, linear, T-shaped, crossroad").scale(0.95).shift(DOWN * 3.0)
        self.play(Write(b0_l5)); self.wait(1.5)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_1): depopulation chain and land reform ---
        self.next_band(1)
        b1_t = Tex("Rural issues: the chain and the repair").scale(1.1).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex(r"Push: drought, mechanisation, few services").scale(0.95).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex(r"Pull: jobs, schools, city lights (real or not)").scale(0.95).shift(band_shift(1) + UP * 0.4)
        self.play(Write(b1_l1)); self.wait(1.7)
        self.play(Write(b1_l2)); self.wait(1.8)
        b1_l3 = Tex(r"Depopulation: young leave first, schools").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex(r"close, shops lose their threshold").scale(0.95).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1_l3)); self.wait(1.6)
        self.play(Write(b1_l4)); self.wait(1.8)
        b1_l5 = Tex(r"Land reform's three legs: restitution,").scale(0.95).shift(band_shift(1) + DOWN * 2.0)
        b1_l6 = Tex(r"redistribution, tenure reform").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5)); self.wait(1.5)
        self.play(Write(b1_l6))
        self.play(Create(SurroundingRectangle(b1_l6, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): urban vocabulary and hierarchy ---
        self.next_band(2)
        b2_t = Tex("Urban vocabulary and the hierarchy").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        b2_l1 = Tex(r"Urbanisation $=$ rising percentage in towns;").scale(0.95).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"growth $=$ numbers; sprawl $=$ uncontrolled spread").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l1)); self.wait(1.7)
        self.play(Write(b2_l2)); self.wait(1.8)
        b2_l3 = Tex(r"Threshold: minimum customers to survive").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        b2_l4 = Tex(r"Range: furthest people travel for it").scale(0.95).shift(band_shift(2) + DOWN * 1.1)
        b2_l5 = Tex(r"Sphere of influence: the area served").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        for m in (b2_l3, b2_l4, b2_l5):
            self.play(Write(m))
            self.wait(1.7)
        b2_l6 = Tex(r"Low-order everywhere; high-order in metropoles").scale(0.9).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): the South African city, drawn as a strip ---
        self.next_band(3)
        b3_t = Tex("The South African city in one strip").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        sc3 = band_shift(3) + UP * 0.5
        zones = [
            ("CBD", 1.4, YELLOW),
            ("transition", 1.8, WHITE),
            ("suburbs", 2.0, WHITE),
            ("buffer", 1.2, RED),
            ("township", 2.2, WHITE),
        ]
        x = -4.3
        for name, w, col in zones:
            r = Rectangle(width=w, height=1.0, color=col).shift(sc3 + RIGHT * (x + w / 2))
            lab = Tex(name).scale(0.7).shift(sc3 + RIGHT * (x + w / 2))
            self.play(Create(r), Write(lab), run_time=0.8)
            self.wait(1.0)
            x += w
        b3_l1 = Tex(r"A colonial-apartheid skeleton: workers far").scale(0.95).shift(band_shift(3) + DOWN * 0.9)
        b3_l2 = Tex(r"from work --- long commutes ARE the model").scale(0.95).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l1)); self.wait(1.7)
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(2)
        b3_l3 = Tex(r"Issues want cause, impact, strategy: upgrade").scale(0.9).shift(band_shift(3) + DOWN * 2.4)
        b3_l4 = Tex(r"in situ, BRT transport, inner-city renewal").scale(0.9).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l3)); self.wait(1.5)
        self.play(Write(b3_l4))
        self.wait(3)

        # --- Band 4 (subtopic_3): sectors, farms, mines ---
        self.next_band(4)
        b4_t = Tex("Economy: sectors, farms, mines").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        b4_l1 = Tex(r"Extract, make, serve, know --- four sectors").scale(0.95).shift(band_shift(4) + UP * 1.1)
        self.play(Write(b4_l1)); self.wait(1.8)
        b4_l2 = Tex(r"Twist: agriculture small in GDP ($\pm$3\%),").scale(0.95).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex(r"huge in food security and rural jobs").scale(0.95).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(b4_l2)); self.wait(1.6)
        self.play(Write(b4_l3)); self.wait(1.8)
        b4_l4 = Tex(r"Farming: commercial vs subsistence;").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        b4_l5 = Tex(r"drought and scarce arable land hinder").scale(0.95).shift(band_shift(4) + DOWN * 1.8)
        self.play(Write(b4_l4)); self.wait(1.5)
        self.play(Write(b4_l5)); self.wait(1.7)
        b4_l6 = Tex(r"Mining: gold built it all; coal, platinum, iron").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        self.play(Write(b4_l6))
        self.wait(3)

        # --- Band 5 (subtopic_3): factories, zones, informal sector ---
        self.next_band(5)
        b5_t = Tex("Four regions, IDZ vs SDI, informal work").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex(r"Name the set: Gauteng (PWV), Durban--Pinetown,").scale(0.9).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"PE--Uitenhage, South-western Cape").scale(0.9).shift(band_shift(5) + UP * 0.4)
        self.play(Write(b5_l1)); self.wait(1.7)
        self.play(Write(b5_l2))
        self.play(Create(SurroundingRectangle(b5_l2, color=GREEN)))
        self.wait(2)
        b5_l3 = Tex(r"IDZ: export estate at a port (Coega)").scale(0.95).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex(r"SDI: investment corridor (Maputo)").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(b5_l3)); self.wait(1.7)
        self.play(Write(b5_l4)); self.wait(1.8)
        b5_l5 = Tex(r"Informal sector: uncounted survival net ---").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        b5_l6 = Tex(r"micro-finance, shelters, simpler rules help").scale(0.95).shift(band_shift(5) + DOWN * 2.8)
        self.play(Write(b5_l5)); self.wait(1.5)
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): the calculation recipes ---
        self.next_band(6)
        b6_t = Tex("Section B recipes (10 marks of them)").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = MathTex(r"\text{Distance: cm} \times 0{,}5\ \text{km on } 1{:}50\,000").scale(1.0).shift(band_shift(6) + UP * 1.1)
        b6_l2 = MathTex(r"\text{Gradient} = \frac{\text{VI}}{\text{HE}} \Rightarrow 1:\text{something}").scale(0.83).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"\text{VE} = \frac{\text{vertical scale}}{\text{horizontal scale}}").scale(0.9).shift(band_shift(6) + DOWN * 1.0)
        b6_l4 = MathTex(r"\text{Declination: change} \times \text{years, then apply}").scale(1.0).shift(band_shift(6) + DOWN * 2.0)
        b6_l5 = MathTex(r"\text{Area} = \text{real length} \times \text{real breadth (km}^2)").scale(1.0).shift(band_shift(6) + DOWN * 2.9)
        for m in (b6_l1, b6_l2, b6_l3, b6_l4, b6_l5):
            self.play(Write(m))
            self.wait(2)
        self.wait(1.5)

        # --- Band 7 (subtopic_4): the discipline + interpretation + GIS ---
        self.next_band(7)
        b7_t = Tex("Interpretation and GIS").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex(r"Formula, substitution, calculation,").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"answer with unit --- each step a mark").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(b7_l1)); self.wait(1.5)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2)
        b7_l3 = Tex(r"Read zones from street patterns: CBD grid,").scale(0.95).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex(r"suburb crescents, dense township blocks").scale(0.95).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(b7_l3)); self.wait(1.6)
        self.play(Write(b7_l4)); self.wait(1.8)
        b7_l5 = Tex(r"GIS: layers stack, buffers ring, queries ask;").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        b7_l6 = Tex(r"vector points-lines-polygons, raster pixels").scale(0.95).shift(band_shift(7) + DOWN * 2.8)
        self.play(Write(b7_l5)); self.wait(1.5)
        self.play(Write(b7_l6))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the village, the taxi and the city ---
        self.next_band(8)
        b8_t = Tex("The village, the taxi and the city").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        b8_l1 = Tex(r"Village: nucleated at the borehole (site);").scale(0.95).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"the tar road that reached it is situation").scale(0.95).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1)); self.wait(1.7)
        self.play(Write(b8_l2)); self.wait(1.8)
        b8_l3 = Tex(r"Sipho's taxi ride: mechanised farm pushes,").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex(r"Joburg wages pull --- repeat 10 000 times").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8_l3)); self.wait(1.7)
        self.play(Write(b8_l4)); self.wait(1.8)
        b8_l5 = Tex(r"He reads the city: CBD, blighted transition,").scale(0.95).shift(band_shift(8) + DOWN * 2.0)
        b8_l6 = Tex(r"decentralised malls, buffer, far township").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l5)); self.wait(1.5)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): how the country earns its keep ---
        self.next_band(9)
        b9_t = Tex("How the country earns its keep").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"One household: grandmother digs (primary),").scale(0.95).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"uncle makes, sister serves, cousin researches").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(b9_l1)); self.wait(1.7)
        self.play(Write(b9_l2)); self.wait(1.8)
        b9_l3 = Tex(r"Her work looks small in the money books,").scale(0.95).shift(band_shift(9) + DOWN * 0.4)
        b9_l4 = Tex(r"but the whole family eats because of her").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9_l3)); self.wait(1.6)
        self.play(Write(b9_l4)); self.wait(1.8)
        b9_l5 = Tex(r"Four corners of the yard hold the factories;").scale(0.95).shift(band_shift(9) + DOWN * 2.0)
        b9_l6 = Tex(r"IDZ $=$ ready yard, SDI $=$ extension cord").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l5)); self.wait(1.5)
        self.play(Write(b9_l6))
        self.play(Create(SurroundingRectangle(b9_l6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): five calculations that always pay ---
        self.next_band(10)
        b10_t = Tex("Five calculations that always pay").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        b10_l1 = Tex(r"1. Distance: cm $\times$ half a km, say the unit").scale(0.95).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex(r"2. Gradient: height over ground, 1 in 20").scale(0.95).shift(band_shift(10) + UP * 0.4)
        b10_l3 = Tex(r"3. VE: vertical over horizontal, TIMES").scale(0.95).shift(band_shift(10) + DOWN * 0.3)
        b10_l4 = Tex(r"4. Declination: years $\times$ change, add west").scale(0.95).shift(band_shift(10) + DOWN * 1.0)
        b10_l5 = Tex(r"5. Area: length $\times$ breadth, km$^2$").scale(0.95).shift(band_shift(10) + DOWN * 1.7)
        for m in (b10_l1, b10_l2, b10_l3, b10_l4, b10_l5):
            self.play(Write(m))
            self.wait(1.8)
        b10_l6 = Tex(r"Every claim points at map evidence").scale(1.0).shift(band_shift(10) + DOWN * 2.7)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
