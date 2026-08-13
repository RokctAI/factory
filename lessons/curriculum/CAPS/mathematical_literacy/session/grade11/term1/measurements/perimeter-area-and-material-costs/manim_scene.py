from manim import *

# Band layout: one frame-height band per teaching beat; the camera moves down,
# nothing is removed. Exporter-supported mobjects only (Tex/MathTex/Line/
# Rectangle/SurroundingRectangle); single-string Write reveals throughout.
#
# Covers all seven subtopics (Part 1 — Expert: 1-4; Part 2 — Simplifier: 5-7),
# band time roughly proportional to subtopics.json
# (210/225/225/230/190/195/195 of 1470 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class PerimeterAreaCostsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full screen while intro.md plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): perimeter of the yard ---
        title = Tex("Perimeter, Area and Material Costs").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        yard = Rectangle(width=6.0, height=3.2).shift(DOWN * 0.4)
        self.play(Create(yard))
        lab_l = Tex("12,5 m").scale(0.9).shift(UP * 1.5)
        lab_b = Tex("8 m").scale(0.9).shift(LEFT * 3.7 + DOWN * 0.4)
        self.play(Write(lab_l), Write(lab_b))
        self.wait(2)
        p1 = MathTex(r"P = 2 \times (l + b)").scale(1.1).shift(DOWN * 2.5 + LEFT * 3.0)
        p2 = MathTex(r"P = 2 \times (12{,}5 + 8) = 41\text{ m}").scale(1.1).shift(DOWN * 2.5 + RIGHT * 2.6)
        self.play(Write(p1)); self.wait(2)
        self.play(Write(p2))
        self.play(Create(SurroundingRectangle(p2, color=GREEN)))
        self.wait(2.5)

        # --- Band 1 (subtopic_1): circumference, and the gate ---
        self.next_band(1)
        b1_title = Tex("Edging, and what is NOT fence").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = MathTex(r"C = 2 \times \pi \times r = 2 \times 3{,}14 \times 1{,}5 = 9{,}42\text{ m}").scale(1.0).shift(band_shift(1) + UP * 1.1)
        self.play(Write(b1_l1)); self.wait(2.5)
        b1_wrong = MathTex(r"41 \times 289 \quad \text{(fenced over the gate!)}").scale(1.0).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_wrong))
        self.play(Create(strike(b1_wrong)))
        self.wait(2)
        b1_l2 = MathTex(r"\text{Fencing} = 41 - 3 = 38\text{ m}").scale(1.1).shift(band_shift(1) + DOWN * 0.8)
        b1_l3 = MathTex(r"38 \times 289 = R10\,982").scale(1.1).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l2)); self.wait(2)
        self.play(Write(b1_l3))
        self.play(Create(SurroundingRectangle(b1_l3, color=GREEN)))
        self.wait(2)
        b1_l4 = Tex("Read the context for gates and gaps first").scale(1.0).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l4)); self.wait(2.5)

        # --- Band 2 (subtopic_2): the three area formulae ---
        self.next_band(2)
        b2_title = Tex("Area: the three formulae").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = MathTex(r"\text{Yard: } A = 12{,}5 \times 8 = 100\text{ m}^2").scale(1.05).shift(band_shift(2) + UP * 1.1)
        b2_l2 = MathTex(r"\text{Circle: } A = 3{,}14 \times 1{,}5^2 = 7{,}07\text{ m}^2").scale(1.05).shift(band_shift(2) + UP * 0.2)
        b2_l3 = MathTex(r"\text{Triangle: } A = \tfrac{1}{2} \times 4 \times 2{,}5 = 5\text{ m}^2").scale(1.05).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1)); self.wait(2.5)
        self.play(Write(b2_l2)); self.wait(2.5)
        self.play(Write(b2_l3)); self.wait(2.5)
        b2_l4 = Tex("Height means the PERPENDICULAR drop, not the slant").scale(0.95).shift(band_shift(2) + DOWN * 1.7)
        self.play(Write(b2_l4)); self.wait(2.5)

        # --- Band 3 (subtopic_2): composite areas and unit care ---
        self.next_band(3)
        b3_title = Tex("Composite shapes: add or subtract areas").scale(1.1).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = MathTex(r"\text{Paved area} = 100 - 7{,}07 = 92{,}93\text{ m}^2").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.play(Create(SurroundingRectangle(b3_l1, color=GREEN)))
        self.wait(2.5)
        b3_l2 = Tex("An L or a T: cut into rectangles, label, add").scale(1.0).shift(band_shift(3) + UP * 0.1)
        self.play(Write(b3_l2)); self.wait(2.5)
        b3_wrong = MathTex(r"\text{cm}^2 \div 100 \quad \text{(lengths rule, not areas!)}").scale(1.0).shift(band_shift(3) + DOWN * 0.9)
        self.play(Write(b3_wrong))
        self.play(Create(strike(b3_wrong)))
        self.wait(2)
        b3_l3 = MathTex(r"1\text{ m}^2 = 100 \times 100 = 10\,000\text{ cm}^2").scale(1.05).shift(band_shift(3) + DOWN * 1.9)
        self.play(Write(b3_l3)); self.wait(2.5)

        # --- Band 4 (subtopic_3): the wall-area shortcut ---
        self.next_band(4)
        b4_title = Tex("Walls: perimeter times height").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex("Unroll the four walls into one long rectangle").scale(1.0).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1)); self.wait(2)
        b4_l2 = MathTex(r"P = 2 \times (4{,}2 + 3{,}6) = 15{,}6\text{ m}").scale(1.1).shift(band_shift(4) + UP * 0.2)
        b4_l3 = MathTex(r"\text{Wall area} = 15{,}6 \times 2{,}5 = 39\text{ m}^2").scale(1.1).shift(band_shift(4) + DOWN * 0.8)
        self.play(Write(b4_l2)); self.wait(2.5)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): subtract the openings, apply the coats ---
        self.next_band(5)
        b5_title = Tex("Doors, windows and coats").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = MathTex(r"\text{Door } 0{,}9 \times 2 = 1{,}8; \; \text{window } 1{,}5 \times 1{,}2 = 1{,}8\text{ m}^2").scale(0.85).shift(band_shift(5) + UP * 1.1)
        b5_l2 = MathTex(r"39 - 3{,}6 = 35{,}4\text{ m}^2 \text{ paintable}").scale(1.1).shift(band_shift(5) + UP * 0.2)
        b5_l3 = MathTex(r"\text{Two coats: } 35{,}4 \times 2 = 70{,}8\text{ m}^2").scale(1.1).shift(band_shift(5) + DOWN * 0.8)
        self.play(Write(b5_l1)); self.wait(2.5)
        self.play(Write(b5_l2)); self.wait(2.5)
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        b5_l4 = Tex(r"Prism: SA $= 2lb + 2lh + 2bh$; leave out a missing face").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        self.play(Write(b5_l4)); self.wait(2.5)

        # --- Band 6 (subtopic_4): paint into tins ---
        self.next_band(6)
        b6_title = Tex("From square metres to rands: paint").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = MathTex(r"70{,}8 \div 8 = 8{,}85\ \ell").scale(1.1).shift(band_shift(6) + UP * 1.0)
        b6_l2 = Tex(r"The shop sells 5 $\ell$ tins at R525 — buy two").scale(1.0).shift(band_shift(6) + UP * 0.1)
        b6_l3 = MathTex(r"2 \times 525 = R1\,050").scale(1.1).shift(band_shift(6) + DOWN * 0.9)
        self.play(Write(b6_l1)); self.wait(2.5)
        self.play(Write(b6_l2)); self.wait(2)
        self.play(Write(b6_l3))
        self.play(Create(SurroundingRectangle(b6_l3, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): tiles with wastage ---
        self.next_band(7)
        b7_title = Tex(r"Tiles: add 10\% wastage, round UP").scale(1.1).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = MathTex(r"\text{Floor: } 4{,}2 \times 3{,}6 = 15{,}12\text{ m}^2").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = MathTex(r"15{,}12 \times 1{,}10 = 16{,}63\text{ m}^2").scale(1.05).shift(band_shift(7) + UP * 0.2)
        b7_l3 = MathTex(r"16{,}63 \div 1{,}44 = 11{,}55 \Rightarrow 12\text{ boxes}").scale(1.05).shift(band_shift(7) + DOWN * 0.7)
        b7_l4 = MathTex(r"12 \times 289 = R3\,468").scale(1.1).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l1)); self.wait(2)
        self.play(Write(b7_l2)); self.wait(2)
        self.play(Write(b7_l3)); self.wait(2.5)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2)
        b7_l5 = Tex("11 boxes leaves bare floor — always round up").scale(1.0).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5)); self.wait(2)

        # --- Band 8 (subtopic_4): paving and the honest total ---
        self.next_band(8)
        b8_title = Tex("Paving, then the project total").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = MathTex(r"92{,}93 \times 1{,}10 = 102{,}22 \Rightarrow \text{order } 103\text{ m}^2").scale(0.92).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"103 \times 145 = R14\,935").scale(1.1).shift(band_shift(8) + UP * 0.2)
        self.play(Write(b8_l1)); self.wait(2.5)
        self.play(Write(b8_l2)); self.wait(2.5)
        b8_l3 = Tex(r"Fence 10\,982 $+$ paving 14\,935 $+$ tiles 3\,468 $+$ paint 1\,050").scale(0.9).shift(band_shift(8) + DOWN * 0.8)
        b8_l4 = MathTex(r"\text{Materials total} = R30\,435").scale(1.15).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l3)); self.wait(2.5)
        self.play(Write(b8_l4))
        self.play(Create(SurroundingRectangle(b8_l4, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): walking the fence ---
        self.next_band(9)
        b9_title = Tex("Perimeter is the walk around the edge").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2.5)
        b9_l1 = MathTex(r"12{,}5 + 8 + 12{,}5 + 8 = 41\text{ m}").scale(1.1).shift(band_shift(9) + UP * 1.2)
        self.play(Write(b9_l1)); self.wait(3)
        b9_l2 = Tex(r"Flower bed: 3 m across, so $3{,}14 \times 3 = 9{,}42$ m").scale(1.0).shift(band_shift(9) + UP * 0.2)
        self.play(Write(b9_l2)); self.wait(3)
        b9_l3 = MathTex(r"\text{Fence} = 41 - 3 = 38\text{ m}; \quad 38 \times 289 = R10\,982").scale(0.94).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)
        b9_l4 = Tex("Ask what is NOT fence before you multiply by a price").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4)); self.wait(3.5)

        # --- Band 10 (subtopic_6): covering floor and walls ---
        self.next_band(10)
        b10_title = Tex("Walk around vs cover over").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2.5)
        b10_l1 = Tex("Fencing is perimeter; tiles, paint and paving are area").scale(0.95).shift(band_shift(10) + UP * 1.2)
        self.play(Write(b10_l1)); self.wait(3)
        b10_l2 = MathTex(r"\text{Paving: } 100 - 7{,}07 = 92{,}93\text{ m}^2").scale(1.05).shift(band_shift(10) + UP * 0.2)
        self.play(Write(b10_l2)); self.wait(3)
        b10_l3 = MathTex(r"\text{Walls: } 15{,}6 \times 2{,}5 = 39\text{ m}^2").scale(1.05).shift(band_shift(10) + DOWN * 0.8)
        b10_l4 = MathTex(r"39 - 3{,}6 = 35{,}4; \quad \times 2 \text{ coats} = 70{,}8\text{ m}^2").scale(1.05).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l3)); self.wait(3)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(3.5)

        # --- Band 11 (subtopic_7): the shop does not sell half a box ---
        self.next_band(11)
        b11_title = Tex("The shop does not sell half a box").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2.5)
        b11_l1 = MathTex(r"8{,}85\ \ell \Rightarrow \text{two } 5\ \ell \text{ tins} = R1\,050").scale(0.96).shift(band_shift(11) + UP * 1.2)
        self.play(Write(b11_l1)); self.wait(3)
        b11_l2 = MathTex(r"11{,}55 \Rightarrow 12\text{ boxes} = R3\,468").scale(1.05).shift(band_shift(11) + UP * 0.2)
        self.play(Write(b11_l2)); self.wait(3)
        b11_l3 = MathTex(r"102{,}22 \Rightarrow 103\text{ m}^2 = R14\,935").scale(1.05).shift(band_shift(11) + DOWN * 0.8)
        self.play(Write(b11_l3)); self.wait(3)
        b11_l4 = MathTex(r"\text{Whole job: } R30\,435 \text{ before labour}").scale(1.1).shift(band_shift(11) + DOWN * 1.8)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(3)
        b11_l5 = Tex("Round UP when running short stops the job").scale(1.0).shift(band_shift(11) + DOWN * 2.8)
        self.play(Write(b11_l5)); self.wait(4)
