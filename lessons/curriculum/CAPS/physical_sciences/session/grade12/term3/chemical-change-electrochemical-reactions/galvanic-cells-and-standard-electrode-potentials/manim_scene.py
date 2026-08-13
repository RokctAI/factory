from manim import *

# Band-layout whiteboard scene for "Galvanic Cells and Standard Electrode
# Potentials" (Part 1 Expert subtopics 1-4, Part 2 Simplifier subtopics 5-7).
# Exporter-safe vocabulary only; the zinc-copper cell is hand-built from
# Lines (beakers, wires, salt bridge), Rectangles (electrodes), a Circle
# (voltmeter) and Tex labels. Write-only reveals.
# Subtopic durations 235/240/240/235/190/195/195 of 1530 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class GalvanicCellsPotentialsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): redox bookkeeping ---
        title = Tex("Galvanic Cells and Electrode Potentials").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex("OIL RIG: Oxidation Is Loss,").scale(1.05).shift(UP * 1.2)
        b0_l2 = Tex("Reduction Is Gain (of electrons)").scale(1.05).shift(UP * 0.4)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.play(Create(SurroundingRectangle(b0_l2, color=GREEN)))
        self.wait(2.5)
        b0_l3 = Tex("Oxidising agent: takes electrons, is REDUCED").scale(0.95).shift(DOWN * 0.5)
        b0_l4 = Tex("Reducing agent: donates, is OXIDISED").scale(0.95).shift(DOWN * 1.3)
        self.play(Write(b0_l3))
        self.wait(2.5)
        self.play(Write(b0_l4))
        self.wait(2.5)
        b0_l5 = Tex("Zn to $Zn^{2+}$: 0 to $+2$ — oxidation, confirmed").scale(0.95).shift(DOWN * 2.2)
        self.play(Write(b0_l5))
        self.wait(2)
        b0_l6 = Tex("Anode: oxidation. Cathode: reduction.").scale(1.0).shift(DOWN * 3.1)
        self.play(Write(b0_l6))
        self.wait(3)

        # --- Band 1 (subtopic_2): the zinc-copper cell, drawn ---
        self.next_band(1)
        b1_title = Tex("The zinc-copper cell").scale(1.2).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        c1 = band_shift(1) + DOWN * 0.8
        # Two beakers.
        beak_l = VGroup(
            Line(c1 + LEFT * 5.0 + UP * 0.8, c1 + LEFT * 5.0 + DOWN * 1.4),
            Line(c1 + LEFT * 5.0 + DOWN * 1.4, c1 + LEFT * 1.8 + DOWN * 1.4),
            Line(c1 + LEFT * 1.8 + DOWN * 1.4, c1 + LEFT * 1.8 + UP * 0.8),
        )
        beak_r = VGroup(
            Line(c1 + RIGHT * 1.8 + UP * 0.8, c1 + RIGHT * 1.8 + DOWN * 1.4),
            Line(c1 + RIGHT * 1.8 + DOWN * 1.4, c1 + RIGHT * 5.0 + DOWN * 1.4),
            Line(c1 + RIGHT * 5.0 + DOWN * 1.4, c1 + RIGHT * 5.0 + UP * 0.8),
        )
        self.play(Create(beak_l), Create(beak_r))
        el_zn = Rectangle(width=0.25, height=1.6).move_to(c1 + LEFT * 4.2 + DOWN * 0.1)
        el_cu = Rectangle(width=0.25, height=1.6).move_to(c1 + RIGHT * 4.2 + DOWN * 0.1)
        self.play(Create(el_zn), Create(el_cu))
        lab_zn = Tex("Zn $-$").scale(0.8).shift(c1 + LEFT * 4.2 + DOWN * 1.9)
        lab_cu = Tex("Cu $+$").scale(0.8).shift(c1 + RIGHT * 4.2 + DOWN * 1.9)
        self.play(Write(lab_zn), Write(lab_cu))
        self.wait(1.5)
        # External wire with voltmeter.
        volt = Circle(radius=0.4).move_to(c1 + UP * 2.2)
        lab_v = Tex("V").scale(0.8).shift(c1 + UP * 2.2)
        wire = VGroup(
            Line(c1 + LEFT * 4.2 + UP * 0.7, c1 + LEFT * 4.2 + UP * 2.2),
            Line(c1 + LEFT * 4.2 + UP * 2.2, c1 + LEFT * 0.4 + UP * 2.2),
            Line(c1 + RIGHT * 0.4 + UP * 2.2, c1 + RIGHT * 4.2 + UP * 2.2),
            Line(c1 + RIGHT * 4.2 + UP * 2.2, c1 + RIGHT * 4.2 + UP * 0.7),
        )
        self.play(Create(wire), Create(volt), Write(lab_v))
        arr_e = Arrow(c1 + LEFT * 3.4 + UP * 2.7, c1 + LEFT * 1.4 + UP * 2.7, buff=0, color=YELLOW)
        lab_e = Tex("$e^-$").scale(0.8).shift(c1 + LEFT * 2.4 + UP * 3.1)
        self.play(Create(arr_e), Write(lab_e))
        self.wait(1.5)
        # Salt bridge.
        bridge = VGroup(
            Line(c1 + LEFT * 2.6 + UP * 0.2, c1 + LEFT * 2.6 + UP * 1.3),
            Line(c1 + LEFT * 2.6 + UP * 1.3, c1 + RIGHT * 2.6 + UP * 1.3),
            Line(c1 + RIGHT * 2.6 + UP * 1.3, c1 + RIGHT * 2.6 + UP * 0.2),
        )
        lab_sb = Tex("salt bridge").scale(0.75).shift(c1 + UP * 0.85)
        self.play(Create(bridge))
        self.play(Write(lab_sb))
        self.wait(3)

        # --- Band 2 (subtopic_2): running the cell ---
        self.next_band(2)
        b2_title = Tex("Run the cell").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{anode: } Zn \rightarrow Zn^{2+} + 2e^-").scale(1.0).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{cathode: } Cu^{2+} + 2e^- \rightarrow Cu").scale(1.0).shift(band_shift(2) + UP * 0.2)
        self.play(Write(b2_l1))
        self.wait(2.5)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("Zn loses mass; Cu gains; the blue fades").scale(1.0).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l3))
        self.wait(2.5)
        b2_l4 = Tex("Salt bridge: completes the circuit and").scale(1.0).shift(band_shift(2) + DOWN * 1.6)
        b2_l5 = Tex("keeps both half-cells neutral").scale(1.0).shift(band_shift(2) + DOWN * 2.4)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex("Remove it: the voltmeter drops to zero").scale(1.0).shift(band_shift(2) + DOWN * 3.2)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_3): the table and its anchor ---
        self.next_band(3)
        b3_title = Tex("Standard electrode potentials").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Standard: 1 mol$\cdot$dm$^{-3}$, 25 $^\circ$C").scale(1.0).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex("Zero of the table: the hydrogen electrode").scale(1.0).shift(band_shift(3) + UP * 0.3)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = MathTex(r"Cu^{2+}/Cu: +0{,}34\ \text{V} \quad Zn^{2+}/Zn: -0{,}76\ \text{V}").scale(0.95).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l3))
        self.wait(2.5)
        b3_l4 = Tex("More positive: stronger oxidising agent").scale(1.0).shift(band_shift(3) + DOWN * 1.5)
        b3_l5 = Tex("More negative: stronger reducing agent").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(b3_l4))
        self.wait(2)
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex("HIGHER potential takes the cathode's job").scale(1.0).shift(band_shift(3) + DOWN * 3.2)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_4): cell notation + the emf calculation ---
        self.next_band(4)
        b4_title = MathTex(r"Zn(s) \,|\, Zn^{2+}(aq) \,||\, Cu^{2+}(aq) \,|\, Cu(s)").scale(1.0).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(2.5)
        b4_l1 = Tex("Anode left, cathode right; $||$ is the bridge").scale(0.95).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2.5)
        b4_eq = MathTex(r"E_{cell} = E_{cathode} - E_{anode}").scale(1.1).shift(band_shift(4) + UP * 0.2)
        self.play(Write(b4_eq))
        self.play(Create(SurroundingRectangle(b4_eq, color=GREEN)))
        self.wait(2.5)
        b4_wrong = MathTex(r"E_{cell} = 0{,}34 - 0{,}76 = -0{,}42").scale(1.0).shift(band_shift(4) + DOWN * 0.9)
        self.play(Write(b4_wrong))
        self.play(Create(strike(b4_wrong)))
        self.wait(2)
        b4_l2 = MathTex(r"E_{cell} = 0{,}34 - (-0{,}76) = 1{,}10\ \text{V}").scale(1.05).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(b4_l2))
        self.play(Create(SurroundingRectangle(b4_l2, color=GREEN)))
        self.wait(2)
        b4_l3 = Tex("Brackets on the negatives, every time").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(b4_l3))
        self.wait(3)

        # --- Band 5 (subtopic_4): Mg-Ag and the flat battery ---
        self.next_band(5)
        b5_title = Tex("Magnesium against silver").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"Ag: +0{,}80\ \text{V (higher: cathode)}").scale(1.0).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"Mg: -2{,}36\ \text{V (anode)}").scale(1.0).shift(band_shift(5) + UP * 0.2)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = MathTex(r"E_{cell} = 0{,}80 - (-2{,}36) = 3{,}16\ \text{V}").scale(1.05).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2.5)
        b5_l4 = Tex("Positive emf: spontaneous as written").scale(1.0).shift(band_shift(5) + DOWN * 1.8)
        b5_l5 = Tex("Flat battery $=$ equilibrium, not empty").scale(1.0).shift(band_shift(5) + DOWN * 2.7)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 6 (subtopic_5): chemistry that pays in electricity ---
        self.next_band(6)
        b6_title = Tex("Chemistry that pays in electricity").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(2)
        b6_l1 = Tex("Zinc: a giver. Copper ions: takers.").scale(1.05).shift(band_shift(6) + UP * 1.1)
        b6_l2 = Tex("Strip in beaker: the trade happens as HEAT").scale(1.0).shift(band_shift(6) + UP * 0.2)
        self.play(Write(b6_l1))
        self.wait(2.5)
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex("Separate them: electrons must commute").scale(1.0).shift(band_shift(6) + DOWN * 0.7)
        b6_l4 = Tex("through YOUR wire — that is the current").scale(1.0).shift(band_shift(6) + DOWN * 1.5)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(2.5)
        b6_l5 = Tex("The wanting is the voltage").scale(1.05).shift(band_shift(6) + DOWN * 2.5)
        self.play(Write(b6_l5))
        self.wait(3)

        # --- Band 7 (subtopic_6): the bridge that keeps the peace ---
        self.next_band(7)
        b7_title = Tex("The bridge that keeps the peace").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(2)
        b7_l1 = Tex("Anode beaker drifts positive,").scale(1.0).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex("cathode beaker drifts negative: seize-up").scale(1.0).shift(band_shift(7) + UP * 0.2)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex("The bridge is a corridor for IONS:").scale(1.0).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = Tex("it tops up whichever side runs short").scale(1.0).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex("Electrons upstairs, ions downstairs —").scale(1.0).shift(band_shift(7) + DOWN * 2.4)
        b7_l6 = Tex("neither storey works without the other").scale(1.0).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_7): the league table ---
        self.next_band(8)
        b8_title = Tex("The league table of electron grabbers").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Fluorine: champion grabber (big positive)").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex("Lithium: pushover (big negative)").scale(1.0).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.wait(2)
        b8_l3 = Tex("Stronger grabber grabs; weaker surrenders").scale(1.0).shift(band_shift(8) + DOWN * 0.7)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2.5)
        b8_l4 = Tex("The gap is the score: Zn-Cu gives 1,10 V;").scale(1.0).shift(band_shift(8) + DOWN * 1.7)
        b8_l5 = Tex("Mg-Ag, opposite ends, yawns to 3,16 V").scale(1.0).shift(band_shift(8) + DOWN * 2.5)
        self.play(Write(b8_l4))
        self.wait(2)
        self.play(Write(b8_l5))
        self.wait(2)
        b8_l6 = Tex("Read the rankings, quote the gap").scale(1.05).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8_l6))
        self.wait(4)
