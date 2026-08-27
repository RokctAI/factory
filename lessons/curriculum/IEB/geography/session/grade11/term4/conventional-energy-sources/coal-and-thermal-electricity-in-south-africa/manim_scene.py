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

# Band-layout whiteboard scene for the IEB session "Coal and Thermal
# Electricity in South Africa" (grade 11, term 4). Seven subtopics of the duo:
# Part 1 Expert (subtopics 1-4), Part 2 Simplifier (subtopics 5-7). Band time
# apportioned to subtopics.json (230/235/235/235/190/195/200 of 1520 s).
# Exporter-safe primitives only; diagrams (mix bar, water battery, station
# energy chain) hand-built from Line/Arrow/Dot/Rectangle/Tex element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class CoalThermalElectricitySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): coalfield geography and the mix
        title = Tex("Coal and Thermal Electricity in SA").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Seams: Mpumalanga Highveld, Waterberg, Free State").scale(0.9).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        # The mix as a horizontal bar: coal dominates, one thin sliver beside it.
        coal_bar = Rectangle(width=5.6, height=0.7, color=GREY).shift(UP * 0.3 + LEFT * 0.9)
        coal_lab = Tex(r"coal: 8 units in 10").scale(0.95).shift(UP * 0.3 + LEFT * 0.9)
        rest_bar = Rectangle(width=1.4, height=0.7, color=BLUE).shift(UP * 0.3 + RIGHT * 2.6)
        rest_lab = Tex(r"Koeberg, hydro,\\ renewables").scale(0.8).shift(DOWN * 0.7 + RIGHT * 2.6)
        self.play(Create(coal_bar), Write(coal_lab))
        self.wait(2)
        self.play(Create(rest_bar), Write(rest_lab))
        self.wait(2)
        b0_l2 = Tex(r"Stations planted on the seams they burn:").scale(1.0).shift(DOWN * 1.5)
        b0_l3 = Tex(r"the coal stays put, the power travels").scale(1.05).shift(DOWN * 2.3)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex(r"Tutuka, Duvha, Kendal, Matimba, Medupi").scale(0.95).shift(DOWN * 3.1)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): hydro limits and the water battery
        self.next_band(1)
        b1_title = Tex("Hydro and the water battery").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Low rainfall, seasonal rivers: little true hydro").scale(0.95).shift(band_shift(1) + UP * 1.3)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Gariep, Vanderkloof; imports from Cahora Bassa").scale(0.9).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1_l2))
        self.wait(2)
        # Water battery: top dam and bottom dam joined by a penstock slope.
        top_dam = Rectangle(width=1.8, height=0.6, color=BLUE).shift(band_shift(1) + DOWN * 0.4 + LEFT * 3.4)
        top_lab = Tex("top dam").scale(0.8).shift(band_shift(1) + UP * 0.2 + LEFT * 3.4)
        bot_dam = Rectangle(width=1.8, height=0.6, color=BLUE).shift(band_shift(1) + DOWN * 2.4 + RIGHT * 3.4)
        bot_lab = Tex("bottom dam").scale(0.8).shift(band_shift(1) + DOWN * 3.0 + RIGHT * 3.4)
        penstock = Line(band_shift(1) + DOWN * 0.7 + LEFT * 2.5,
                        band_shift(1) + DOWN * 2.1 + RIGHT * 2.5)
        self.play(Create(top_dam), Write(top_lab))
        self.play(Create(bot_dam), Write(bot_lab))
        self.play(Create(penstock))
        self.wait(1.5)
        up_arrow = Arrow(band_shift(1) + DOWN * 2.2 + RIGHT * 1.6,
                         band_shift(1) + DOWN * 0.9 + LEFT * 1.6, color=YELLOW)
        up_lab = Tex("small hours: pump up cheap").scale(0.8).shift(band_shift(1) + DOWN * 0.9 + RIGHT * 1.4)
        self.play(Create(up_arrow), Write(up_lab))
        self.wait(2)
        dn_arrow = Arrow(band_shift(1) + DOWN * 1.3 + LEFT * 2.0,
                         band_shift(1) + DOWN * 2.6 + RIGHT * 1.2, color=GREEN)
        dn_lab = Tex("evening peak: release").scale(0.8).shift(band_shift(1) + DOWN * 2.9 + LEFT * 2.4)
        self.play(Create(dn_arrow), Write(dn_lab))
        self.wait(2)
        b1_l3 = Tex(r"Palmiet, Steenbras, Ingula: batteries, not sources").scale(0.9).shift(band_shift(1) + DOWN * 0.05)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the four energy costumes
        self.next_band(2)
        b2_title = Tex("Inside a coal-fired power station").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_chain = Tex(r"chemical $\to$ heat $\to$ movement $\to$ electricity").scale(0.95).shift(band_shift(2) + UP * 1.4)
        self.play(Write(b2_chain))
        self.wait(2.5)
        # Four-stage chain of boxes with arrows, built one element at a time.
        stages = [
            ("furnace + boiler", LEFT * 4.6),
            ("turbine", LEFT * 1.55),
            ("generator", RIGHT * 1.55),
            ("transformer", RIGHT * 4.6),
        ]
        boxes = []
        for name, pos in stages:
            box = Rectangle(width=2.5, height=1.0).shift(band_shift(2) + UP * 0.2 + pos)
            lab = Tex(name).scale(0.75).shift(band_shift(2) + UP * 0.2 + pos)
            self.play(Create(box), Write(lab))
            if boxes:
                ar = Arrow(boxes[-1].get_right(), box.get_left(), buff=0.05)
                self.play(Create(ar), run_time=0.5)
            boxes.append(box)
            self.wait(1.2)
        b2_f1 = Tex(r"1 400 $^\circ$C dust flame").scale(0.8).shift(band_shift(2) + DOWN * 0.9 + LEFT * 4.6)
        b2_f2 = Tex(r"3 000 turns a minute").scale(0.8).shift(band_shift(2) + DOWN * 0.9 + LEFT * 1.55)
        b2_f3 = Tex(r"magnet in copper coils").scale(0.8).shift(band_shift(2) + DOWN * 0.9 + RIGHT * 1.55)
        b2_f4 = Tex(r"up to 400 kV out").scale(0.8).shift(band_shift(2) + DOWN * 0.9 + RIGHT * 4.6)
        self.play(Write(b2_f1))
        self.wait(1.5)
        self.play(Write(b2_f2))
        self.wait(1.5)
        self.play(Write(b2_f3))
        self.wait(1.5)
        self.play(Write(b2_f4))
        self.wait(2)
        b2_l1 = Tex(r"High voltage slashes losses along the cables").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"Milled finer than flour: ignites and burns out fully").scale(0.9).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l2))
        self.wait(3)

        # --- Band 3 (subtopic_2): cooling, waste and the third
        self.next_band(3)
        b3_title = Tex("Cooling, waste, and the stubborn third").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Curved towers are coolers, not chimneys:").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"their white plumes are water vapour").scale(0.95).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"Dry cooling in the Waterberg: Matimba, Medupi").scale(0.9).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"Flue gas: CO$_2$, SO$_2$, NO$_x$; ash to dumps and cement").scale(0.9).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex(r"About $\tfrac{1}{3}$ of the coal's energy leaves as").scale(1.0).shift(band_shift(3) + DOWN * 2.2)
        b3_l6 = Tex(r"electricity — two thirds surrendered as heat").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the advantages column
        self.next_band(4)
        b4_title = Tex("Weighing coal: the advantages").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Security: reserves outlast every learner here").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"Cost: shallow seams, once world's cheapest power").scale(0.95).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex(r"Baseload: the constant floor, midnight and midday").scale(0.95).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"Livelihoods: $\approx$ 90 000 miners; Emalahleni,").scale(0.95).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex(r"Middelburg, Secunda stand on the seam").scale(0.95).shift(band_shift(4) + DOWN * 2.0)
        b4_l6 = Tex(r"Exports: Richards Bay earns foreign exchange").scale(0.95).shift(band_shift(4) + DOWN * 2.8)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4, b4_l5, b4_l6):
            self.play(Write(m))
            self.wait(1.8)
        self.wait(1.5)

        # --- Band 5 (subtopic_3): the disadvantages column
        self.next_band(5)
        b5_title = Tex("Weighing coal: the disadvantages").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Climate: heaviest CO$_2$ emitter on the continent").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Air: Highveld SO$_2$/NO$_x$ ring; clinic queues").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"Water: evaporation $+$ acid mine drainage").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex(r"Land: opencast pits in the maize fields").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex(r"Practice: tired fleet $=$ load-shedding").scale(0.95).shift(band_shift(5) + DOWN * 2.0)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4, b5_l5):
            self.play(Write(m))
            self.wait(1.8)
        b5_l6 = Tex(r"Coal financed the rise — the invoices arrive at once").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the running-down clock
        self.next_band(6)
        b6_title = Tex("Can conventional carry the future?").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"For: decades of coal, skills and rail exist;").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"Medupi and Kusile built for mid-century").scale(0.95).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Against: elderly fleet; lenders refuse new").scale(0.95).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex(r"coal; water deficit; carbon border charges;").scale(0.95).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex(r"climate commitments bend emissions down").scale(0.95).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex(r"Conventional-only: a clock running down").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the Koeberg case study
        self.next_band(7)
        b7_title = Tex("Nuclear case study: Koeberg").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Two reactors, $\approx$ 1 900 MW, coast north of").scale(0.95).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"Cape Town, anchoring the grid since 1984").scale(0.95).shift(band_shift(7) + UP * 0.6)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"Fission heat $\Rightarrow$ steam $\Rightarrow$ thermal station").scale(0.9).shift(band_shift(7) + DOWN * 0.1)
        self.play(Write(b7_l3))
        self.wait(2)
        b7_l4 = Tex(r"Thumbnail pellet $\approx$ 1 tonne of coal").scale(1.0).shift(band_shift(7) + DOWN * 0.9)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = Tex(r"For: no CO$_2$ running, baseload, no ash dumps").scale(0.9).shift(band_shift(7) + DOWN * 1.7)
        b7_l6 = Tex(r"Against: costliest, slowest builds; waste at").scale(0.9).shift(band_shift(7) + DOWN * 2.4)
        b7_l7 = Tex(r"Vaalputs for millennia; rare, vast accidents.").scale(0.9).shift(band_shift(7) + DOWN * 3.1)
        b7_l8 = Tex(r"Verdict: a diversified MIX").scale(1.0).shift(band_shift(7) + DOWN * 3.8)
        self.play(Write(b7_l5))
        self.wait(2)
        self.play(Write(b7_l6))
        self.play(Write(b7_l7))
        self.wait(2)
        self.play(Write(b7_l8))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the kettle the size of a suburb
        self.next_band(8)
        b8_title = Tex("The kettle the size of a suburb").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"chemical $\Rightarrow$ heat $\Rightarrow$ spin $\Rightarrow$ spark").scale(0.9).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.play(Create(SurroundingRectangle(b8_l1, color=GREEN)))
        self.wait(2.5)
        b8_l2 = Tex(r"Flour-fine coal at 1 400 $^\circ$C; tube walls").scale(0.95).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex(r"boil the water; steam spins 3 000 a minute").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"Magnet in copper coils $=$ the whole generator").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex(r"400 000 V out: long journeys leak less at pressure").scale(0.9).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex(r"Curved towers cool; their clouds are vapour").scale(0.9).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l6))
        self.wait(2)
        b8_l7 = Tex(r"Of 3 bags of coal, 1 becomes electricity").scale(0.9).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): the drawer of unpaid bills
        self.next_band(9)
        b9_title = Tex("The drawer of unpaid bills").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_mid = Line(band_shift(9) + UP * 1.6, band_shift(9) + DOWN * 2.2)
        self.play(Create(b9_mid))
        b9_ph = Tex("Paid us", color=GREEN).scale(1.05).shift(band_shift(9) + UP * 1.3 + LEFT * 3.2)
        b9_bh = Tex("Bills", color=RED).scale(1.05).shift(band_shift(9) + UP * 1.3 + RIGHT * 3.2)
        self.play(Write(b9_ph), Write(b9_bh))
        self.wait(1.5)
        b9_p1 = Tex(r"cheap power built\\ the economy").scale(0.9).shift(band_shift(9) + UP * 0.4 + LEFT * 3.2)
        b9_b1 = Tex(r"heaviest carbon\\ emitter in Africa").scale(0.9).shift(band_shift(9) + UP * 0.4 + RIGHT * 3.2)
        self.play(Write(b9_p1))
        self.play(Write(b9_b1))
        self.wait(2)
        b9_p2 = Tex(r"baseload at 3 am\\ and 6 pm alike").scale(0.9).shift(band_shift(9) + DOWN * 0.7 + LEFT * 3.2)
        b9_b2 = Tex(r"Highveld air;\\ acid mine drainage").scale(0.9).shift(band_shift(9) + DOWN * 0.7 + RIGHT * 3.2)
        self.play(Write(b9_p2))
        self.play(Write(b9_b2))
        self.wait(2)
        b9_p3 = Tex(r"90 000 pay cheques;\\ Richards Bay exports").scale(0.85).shift(band_shift(9) + DOWN * 1.8 + LEFT * 3.2)
        b9_b3 = Tex(r"pits in the maize;\\ load-shedding").scale(0.9).shift(band_shift(9) + DOWN * 1.8 + RIGHT * 3.2)
        self.play(Write(b9_p3))
        self.play(Write(b9_b3))
        self.wait(2.5)
        b9_l1 = Tex(r"Emalahleni files papers in BOTH drawers").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l1))
        self.play(Create(SurroundingRectangle(b9_l1, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the fork in the road
        self.next_band(10)
        b10_title = Tex("The fork in the road").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Fuel: plenty. Vehicle: elderly. Finance:").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"closed. Tolls: carbon charges at the border").scale(0.95).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Coal-only road $=$ a countdown").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l3))
        self.play(Create(strike(b10_l3)))
        self.wait(2)
        b10_l4 = Tex(r"Detour: Koeberg — thumbnail pellet $\approx$").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        b10_l5 = Tex(r"1 tonne of coal; clean, but slow and dear").scale(0.95).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex(r"Verdict: drive several roads — the MIX").scale(1.05).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
