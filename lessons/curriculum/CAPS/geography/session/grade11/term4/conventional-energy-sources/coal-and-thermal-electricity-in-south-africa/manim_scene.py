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

# Band-layout whiteboard scene for "Coal and Thermal Electricity in South
# Africa" (grade 11, term 4). All seven subtopics of the duo: Part 1 Expert
# (subtopics 1-4), Part 2 Simplifier (subtopics 5-7). Band time apportioned
# to subtopics.json (230/235/235/235/190/195/200 of 1520 s). Exporter-safe
# primitives only; diagrams (energy mix bar, pumped storage, station energy
# chain) hand-built from Line/Arrow/Dot/Rectangle/Tex, element by element.

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
        # --- Band 0 (subtopic_1): coal country and the energy mix
        title = Tex("Coal and Thermal Electricity in SA").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"Coalfields: Mpumalanga, Waterberg, Free State").scale(1.0).shift(UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        # Energy mix as a horizontal bar: coal dominates, slivers beside it.
        coal_bar = Rectangle(width=5.6, height=0.7, color=GREY).shift(UP * 0.3 + LEFT * 0.9)
        coal_lab = Tex(r"coal $\approx 80\%$").scale(1.0).shift(UP * 0.3 + LEFT * 0.9)
        rest_bar = Rectangle(width=1.4, height=0.7, color=BLUE).shift(UP * 0.3 + RIGHT * 2.6)
        rest_lab = Tex(r"nuclear, hydro,\\ renewables").scale(0.8).shift(DOWN * 0.7 + RIGHT * 2.6)
        self.play(Create(coal_bar), Write(coal_lab))
        self.wait(2)
        self.play(Create(rest_bar), Write(rest_lab))
        self.wait(2)
        b0_l2 = Tex(r"Stations sit ON the coalfields:").scale(1.05).shift(DOWN * 1.5)
        b0_l3 = Tex(r"wire is cheaper than rail").scale(1.1).shift(DOWN * 2.3)
        self.play(Write(b0_l2))
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2)
        b0_l4 = Tex(r"Kendal, Matimba, Majuba, Medupi, Kusile").scale(0.95).shift(DOWN * 3.1)
        self.play(Write(b0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): hydro and pumped storage diagram
        self.next_band(1)
        b1_title = Tex("Hydro and pumped storage").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Dry country, variable rivers: hydro small").scale(1.0).shift(band_shift(1) + UP * 1.3)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex(r"Gariep, Vanderkloof; imports: Cahora Bassa").scale(0.95).shift(band_shift(1) + UP * 0.6)
        self.play(Write(b1_l2))
        self.wait(2)
        # Pumped storage: high and low reservoirs joined by a slope.
        hi_res = Rectangle(width=1.8, height=0.6, color=BLUE).shift(band_shift(1) + DOWN * 0.4 + LEFT * 3.4)
        hi_lab = Tex("high dam").scale(0.8).shift(band_shift(1) + UP * 0.2 + LEFT * 3.4)
        lo_res = Rectangle(width=1.8, height=0.6, color=BLUE).shift(band_shift(1) + DOWN * 2.4 + RIGHT * 3.4)
        lo_lab = Tex("low dam").scale(0.8).shift(band_shift(1) + DOWN * 3.0 + RIGHT * 3.4)
        slope = Line(band_shift(1) + DOWN * 0.7 + LEFT * 2.5,
                     band_shift(1) + DOWN * 2.1 + RIGHT * 2.5)
        self.play(Create(hi_res), Write(hi_lab))
        self.play(Create(lo_res), Write(lo_lab))
        self.play(Create(slope))
        self.wait(1.5)
        up_arrow = Arrow(band_shift(1) + DOWN * 2.2 + RIGHT * 1.6,
                         band_shift(1) + DOWN * 0.9 + LEFT * 1.6, color=YELLOW)
        up_lab = Tex("night: pump up (cheap)").scale(0.85).shift(band_shift(1) + DOWN * 0.9 + RIGHT * 1.2)
        self.play(Create(up_arrow), Write(up_lab))
        self.wait(2)
        dn_arrow = Arrow(band_shift(1) + DOWN * 1.3 + LEFT * 2.0,
                         band_shift(1) + DOWN * 2.6 + RIGHT * 1.2, color=GREEN)
        dn_lab = Tex("peak: release, generate").scale(0.85).shift(band_shift(1) + DOWN * 2.9 + LEFT * 2.4)
        self.play(Create(dn_arrow), Write(dn_lab))
        self.wait(2)
        b1_l3 = Tex(r"Not a source — a giant battery").scale(1.05).shift(band_shift(1) + DOWN * 0.05)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the energy chain, station diagram
        self.next_band(2)
        b2_title = Tex("Inside a coal-fired power station").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_chain = Tex(r"chemical $\to$ heat $\to$ kinetic $\to$ electrical").scale(1.0).shift(band_shift(2) + UP * 1.4)
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
        b2_f1 = Tex(r"burns: 1 400 $^\circ$C").scale(0.85).shift(band_shift(2) + DOWN * 0.9 + LEFT * 4.6)
        b2_f2 = Tex(r"steam spins 3 000 rpm").scale(0.85).shift(band_shift(2) + DOWN * 0.9 + LEFT * 1.55)
        b2_f3 = Tex(r"magnet in coils").scale(0.85).shift(band_shift(2) + DOWN * 0.9 + RIGHT * 1.55)
        b2_f4 = Tex(r"up to 400 kV").scale(0.85).shift(band_shift(2) + DOWN * 0.9 + RIGHT * 4.6)
        self.play(Write(b2_f1))
        self.wait(1.5)
        self.play(Write(b2_f2))
        self.wait(1.5)
        self.play(Write(b2_f3))
        self.wait(1.5)
        self.play(Write(b2_f4))
        self.wait(2)
        b2_l1 = Tex(r"High voltage cuts losses over distance").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"Pulverised coal burns fast and completely").scale(1.0).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l2))
        self.wait(3)

        # --- Band 3 (subtopic_2): cooling, ash and the efficiency check
        self.next_band(3)
        b3_title = Tex("Cooling, ash, and the efficiency check").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Cooling towers: plumes are water vapour,").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"not smoke — steam condensed to reuse").scale(1.0).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"Dry-cooled for scarce water: Kendal, Matimba").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex(r"Flue gas: CO$_2$, SO$_2$, NO$_x$; ash dumped").scale(1.0).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex(r"Only $\approx \tfrac{1}{3}$ of coal energy becomes").scale(1.05).shift(band_shift(3) + DOWN * 2.2)
        b3_l6 = Tex(r"electricity — the rest is waste heat").scale(1.05).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): coal's advantages
        self.next_band(4)
        b4_title = Tex("Weighing coal: the advantages").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Abundance: reserves for decades").scale(1.05).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"Cost: historically among world's cheapest").scale(1.0).shift(band_shift(4) + UP * 0.4)
        b4_l3 = Tex(r"Reliability: steady baseload, day and night").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"Jobs: $\approx$ 90 000 miners; Emalahleni,").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        b4_l5 = Tex(r"Middelburg, Secunda built on coal").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        b4_l6 = Tex(r"Exports earn forex via Richards Bay").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        for m in (b4_l1, b4_l2, b4_l3, b4_l4, b4_l5, b4_l6):
            self.play(Write(m))
            self.wait(1.8)
        self.wait(1.5)

        # --- Band 5 (subtopic_3): coal's disadvantages
        self.next_band(5)
        b5_title = Tex("Weighing coal: the disadvantages").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Climate: Africa's largest CO$_2$ emitter").scale(1.0).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"Air: Highveld SO$_2$/NO$_x$; lung disease").scale(1.0).shift(band_shift(5) + UP * 0.4)
        b5_l3 = Tex(r"Water: thirsty stations $+$ acid mine drainage").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        b5_l4 = Tex(r"Land: opencast strips maize farmland").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        b5_l5 = Tex(r"Ageing fleet gave us load-shedding").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4, b5_l5):
            self.play(Write(m))
            self.wait(1.8)
        b5_l6 = Tex(r"Coal built the economy — the bills are overdue").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): can conventional carry the future?
        self.next_band(6)
        b6_title = Tex("Can conventional carry the future?").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"For: decades of reserves, skills, rail;").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"Medupi and Kusile run to mid-century").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Against: old unreliable fleet; no new").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l4 = Tex(r"coal finance; water limits; carbon border").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        b6_l5 = Tex(r"taxes; Paris Agreement commitments").scale(1.0).shift(band_shift(6) + DOWN * 2.1)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.play(Write(b6_l5))
        self.wait(2.5)
        b6_l6 = Tex(r"Conventional-only is a countdown, not a plan").scale(1.0).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l6))
        self.play(Create(SurroundingRectangle(b6_l6, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): nuclear as case study — Koeberg
        self.next_band(7)
        b7_title = Tex("Nuclear case study: Koeberg").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Two reactors, $\approx$ 1 900 MW, since 1984").scale(1.0).shift(band_shift(7) + UP * 1.3)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex(r"Fission heat $\Rightarrow$ steam $\Rightarrow$ thermal plant").scale(0.94).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l2))
        self.wait(2)
        b7_l3 = Tex(r"1 fingertip pellet $\approx$ 1 tonne of coal").scale(1.05).shift(band_shift(7) + DOWN * 0.3)
        self.play(Write(b7_l3))
        self.play(Create(SurroundingRectangle(b7_l3, color=GREEN)))
        self.wait(2.5)
        b7_l4 = Tex(r"For: no CO$_2$ running, baseload, no ash").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        b7_l5 = Tex(r"Against: costliest, slowest builds; waste").scale(1.0).shift(band_shift(7) + DOWN * 2.0)
        b7_l6 = Tex(r"isolated for millennia (Vaalputs); rare").scale(1.0).shift(band_shift(7) + DOWN * 2.7)
        b7_l7 = Tex(r"but enormous accidents. Verdict: a MIX").scale(1.0).shift(band_shift(7) + DOWN * 3.4)
        self.play(Write(b7_l4))
        self.wait(2)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2)
        self.play(Write(b7_l7))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the kettle the size of a suburb
        self.next_band(8)
        b8_title = Tex("The kettle the size of a suburb").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"coal $\Rightarrow$ steam $\Rightarrow$ spin $\Rightarrow$ spark").scale(0.91).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.play(Create(SurroundingRectangle(b8_l1, color=GREEN)))
        self.wait(2.5)
        b8_l2 = Tex(r"Powder burns at 1 400 $^\circ$C; tube walls").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex(r"are the kettle; steam spins 3 000 rpm").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"Transformers push up to 400 000 V:").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex(r"high pressure, low loss, Gauteng is far").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex(r"Funnel towers: cooling; clouds are vapour").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        self.play(Write(b8_l6))
        self.wait(2)
        b8_l7 = Tex(r"Only 1 coal truck in 3 becomes electricity").scale(0.95).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): the drawer of unpaid bills
        self.next_band(9)
        b9_title = Tex("The drawer of unpaid bills").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_mid = Line(band_shift(9) + UP * 1.6, band_shift(9) + DOWN * 2.2)
        self.play(Create(b9_mid))
        b9_rh = Tex("Receipts", color=GREEN).scale(1.05).shift(band_shift(9) + UP * 1.3 + LEFT * 3.2)
        b9_bh = Tex("Bills", color=RED).scale(1.05).shift(band_shift(9) + UP * 1.3 + RIGHT * 3.2)
        self.play(Write(b9_rh), Write(b9_bh))
        self.wait(1.5)
        b9_r1 = Tex(r"cheap power built\\ industry").scale(0.9).shift(band_shift(9) + UP * 0.4 + LEFT * 3.2)
        b9_b1 = Tex(r"climate: biggest\\ emitter in Africa").scale(0.9).shift(band_shift(9) + UP * 0.4 + RIGHT * 3.2)
        self.play(Write(b9_r1))
        self.play(Write(b9_b1))
        self.wait(2)
        b9_r2 = Tex(r"baseload keeps\\ hospitals alive").scale(0.9).shift(band_shift(9) + DOWN * 0.7 + LEFT * 3.2)
        b9_b2 = Tex(r"dirty Highveld air;\\ acid mine drainage").scale(0.9).shift(band_shift(9) + DOWN * 0.7 + RIGHT * 3.2)
        self.play(Write(b9_r2))
        self.play(Write(b9_b2))
        self.wait(2)
        b9_r3 = Tex(r"90 000 jobs;\\ Richards Bay forex").scale(0.9).shift(band_shift(9) + DOWN * 1.8 + LEFT * 3.2)
        b9_b3 = Tex(r"strip-mined maize\\ land; load-shedding").scale(0.9).shift(band_shift(9) + DOWN * 1.8 + RIGHT * 3.2)
        self.play(Write(b9_r3))
        self.play(Write(b9_b3))
        self.wait(2.5)
        b9_l1 = Tex(r"Emalahleni sits in BOTH drawers").scale(1.05).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l1))
        self.play(Create(SurroundingRectangle(b9_l1, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the fork in the road
        self.next_band(10)
        b10_title = Tex("The fork in the road").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Tank not empty — but trucks are old,").scale(1.0).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"banks refuse new coal, border taxes loom").scale(1.0).shift(band_shift(10) + UP * 0.5)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.wait(2.5)
        b10_l3 = Tex(r"Coal-only $=$ a countdown").scale(1.05).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(b10_l3))
        self.play(Create(strike(b10_l3)))
        self.wait(2)
        b10_l4 = Tex(r"Detour: Koeberg — fingertip pellet").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        b10_l5 = Tex(r"$\approx$ 1 tonne of coal; clean but slow, dear").scale(1.0).shift(band_shift(10) + DOWN * 2.0)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.wait(2.5)
        b10_l6 = Tex(r"Verdict at the fork: a MIX of sources").scale(1.1).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l6))
        self.play(Create(SurroundingRectangle(b10_l6, color=GREEN)))
        self.wait(4)
