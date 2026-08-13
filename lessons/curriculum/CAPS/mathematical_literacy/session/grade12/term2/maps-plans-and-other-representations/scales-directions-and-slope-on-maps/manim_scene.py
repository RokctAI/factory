from manim import *

# Band-layout whiteboard scene for Scales, Directions and Slope on Maps.
# One band per teaching beat; camera moves down, earlier work stays put.
# Exporter-supported mobjects only; every working line is a single-string
# Tex/MathTex revealed with Write. No transforms, no FadeOut.
#
# Subtopic time shares (subtopics.json, total 1525 s):
# 220/240/240/250/190/190/195 -> bands 0-1 / 2-3 / 4-5 / 6-8 / 9 / 10 / 11.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ScalesDirectionsSlopeOnMapsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the number scale, converted once
        title = Tex("Scales, Directions and Slope on Maps").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = MathTex(r"\text{Scale } 1 : 2\;000\;000").scale(1.2).shift(UP * 1.1)
        b0_l2 = MathTex(r"2\;000\;000 \text{ cm} = 20 \text{ km}").scale(1.1).shift(UP * 0.2)
        b0_l3 = Tex("Every centimetre is 20 kilometres").scale(1.1).shift(DOWN * 0.7)
        self.play(Write(b0_l1))
        self.wait(2)
        self.play(Write(b0_l2))
        self.wait(2)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(2.5)
        b0_l4 = Tex("Johannesburg to Durban: 28,5 cm on the map").scale(1.05).shift(DOWN * 1.7)
        b0_l5 = MathTex(r"28{,}5 \times 20 = 570 \text{ km (signs say 568)}").scale(1.05).shift(DOWN * 2.7)
        self.play(Write(b0_l4))
        self.wait(2)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the reverse trip and the unit chain
        self.next_band(1)
        b1_t = Tex("Ground to paper: shrink, so divide").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex("Bloemfontein to Pretoria: about 300 km").scale(1.05).shift(band_shift(1) + UP * 1.1)
        b1_l2 = MathTex(r"300 \div 20 = 15 \text{ cm}").scale(1.15).shift(band_shift(1) + UP * 0.2)
        self.play(Write(b1_l1))
        self.wait(2)
        self.play(Write(b1_l2))
        self.play(Create(SurroundingRectangle(b1_l2, color=GREEN)))
        self.wait(2)
        b1_l3 = MathTex(r"6\;000 \text{ cm on paper? Operations swapped}").scale(1.0).shift(band_shift(1) + DOWN * 0.8)
        self.play(Write(b1_l3))
        self.play(Create(strike(b1_l3)))
        self.wait(2)
        b1_l4 = Tex("Show the unit chain for the method mark:").scale(1.05).shift(band_shift(1) + DOWN * 1.7)
        b1_l5 = MathTex(r"28{,}5 \times 2\;000\;000 = 57\;000\;000 \text{ cm}").scale(1.0).shift(band_shift(1) + DOWN * 2.5)
        b1_l6 = MathTex(r"57\;000\;000 \div 100\;000 = 570 \text{ km}").scale(1.0).shift(band_shift(1) + DOWN * 3.1)
        self.play(Write(b1_l4))
        self.wait(2)
        self.play(Write(b1_l5))
        self.wait(2)
        self.play(Write(b1_l6))
        self.wait(3)

        # --- Band 2 (subtopic_2): the bar scale, drawn and priced
        self.next_band(2)
        b2_t = Tex("The bar scale: measure, then price 1 cm").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        bar1 = Rectangle(width=1.6, height=0.4).shift(band_shift(2) + LEFT * 2.0 + UP * 1.1)
        bar2 = Rectangle(width=1.6, height=0.4).shift(band_shift(2) + LEFT * 0.4 + UP * 1.1)
        bar_lab = Tex("one segment: 2 cm, labelled 50 km").scale(1.0).shift(band_shift(2) + RIGHT * 3.2 + UP * 1.1)
        self.play(Create(bar1), Create(bar2))
        self.play(Write(bar_lab))
        self.wait(2)
        b2_l1 = MathTex(r"1 \text{ cm} = 50 \div 2 = 25 \text{ km}").scale(1.1).shift(band_shift(2) + UP * 0.1)
        b2_l2 = MathTex(r"\text{Coastal road: } 7 \times 25 = 175 \text{ km}").scale(1.1).shift(band_shift(2) + DOWN * 0.8)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.play(Create(SurroundingRectangle(b2_l2, color=GREEN)))
        self.wait(2.5)
        b2_l3 = Tex("Photocopy or zoom: the ratio becomes a lie").scale(1.05).shift(band_shift(2) + DOWN * 1.8)
        b2_l4 = Tex("The bar resizes WITH the roads — still true").scale(1.05).shift(band_shift(2) + DOWN * 2.7)
        self.play(Write(b2_l3))
        self.wait(2)
        self.play(Write(b2_l4))
        self.wait(3)

        # --- Band 3 (subtopic_2): determining and choosing a scale
        self.next_band(3)
        b3_t = Tex("Scale = drawn length : real length").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex("Bakkie: real 4,5 m, drawing 9 cm").scale(1.05).shift(band_shift(3) + UP * 1.2)
        b3_l2 = MathTex(r"4{,}5 \text{ m} = 450 \text{ cm (same units first)}").scale(1.05).shift(band_shift(3) + UP * 0.3)
        b3_l3 = MathTex(r"9 : 450 = 1 : 50").scale(1.15).shift(band_shift(3) + DOWN * 0.6)
        self.play(Write(b3_l1))
        self.wait(2)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(b3_l3, color=GREEN)))
        self.wait(2.5)
        b3_l4 = MathTex(r"\text{Hall 30 m at } 1:50: \; 3\;000 \div 50 = 60 \text{ cm}").scale(1.0).shift(band_shift(3) + DOWN * 1.6)
        b3_l5 = Tex("1 : 20 gives 150 cm (off the board)").scale(1.0).shift(band_shift(3) + DOWN * 2.4)
        b3_l6 = Tex("1 : 200 gives 15 cm (hides detail)").scale(1.0).shift(band_shift(3) + DOWN * 3.1)
        self.play(Write(b3_l4))
        self.wait(2.5)
        self.play(Write(b3_l5))
        self.wait(2)
        self.play(Write(b3_l6))
        self.wait(3)

        # --- Band 4 (subtopic_3): the grid, drawn
        self.next_band(4)
        b4_t = Tex("Grid references: column first, then row").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        # 4 columns (A-D) x 3 rows grid, cells 1.4 x 1.0
        grid_left = -2.8
        grid_top = 1.2
        for i in range(4):
            self.play(Create(Line(
                band_shift(4) + RIGHT * grid_left + UP * (grid_top - 1.0 * i) + LEFT * 0,
                band_shift(4) + RIGHT * (grid_left + 5.6) + UP * (grid_top - 1.0 * i))),
                run_time=0.4)
        for j in range(5):
            self.play(Create(Line(
                band_shift(4) + RIGHT * (grid_left + 1.4 * j) + UP * grid_top,
                band_shift(4) + RIGHT * (grid_left + 1.4 * j) + UP * (grid_top - 3.0))),
                run_time=0.4)
        cols = VGroup(*[Tex(c).scale(1.0).shift(band_shift(4) + RIGHT * (grid_left + 0.7 + 1.4 * i) + UP * (grid_top + 0.4))
                        for i, c in enumerate(["A", "B", "C", "D"])])
        rows = VGroup(*[Tex(str(r + 1)).scale(1.0).shift(band_shift(4) + RIGHT * (grid_left - 0.4) + UP * (grid_top - 0.5 - 1.0 * r))
                        for r in range(3)])
        self.play(Write(cols))
        self.play(Write(rows))
        self.wait(2)
        town = Dot(band_shift(4) + RIGHT * (grid_left + 0.7 + 1.4 * 3) + UP * (grid_top - 2.5), color=RED)
        town_lab = Tex("Harrismith: D3").scale(1.05).shift(band_shift(4) + RIGHT * 4.6 + DOWN * 1.3)
        self.play(FadeIn(town))
        self.play(Write(town_lab))
        self.wait(2)
        b4_l1 = Tex("A reference names a BLOCK, not a point").scale(1.05).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(b4_l1))
        self.wait(3)

        # --- Band 5 (subtopic_3): compass directions and the distance table
        self.next_band(5)
        b5_t = Tex("Eight compass words, from the right viewpoint").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        centre = band_shift(5) + LEFT * 3.2 + DOWN * 0.4
        self.play(Create(Arrow(centre, centre + UP * 1.6, buff=0)),
                  Create(Arrow(centre, centre + DOWN * 1.6, buff=0)))
        self.play(Create(Arrow(centre, centre + RIGHT * 1.6, buff=0)),
                  Create(Arrow(centre, centre + LEFT * 1.6, buff=0)))
        n_lab = Tex("N").scale(1.0).shift(centre + UP * 2.0)
        s_lab = Tex("S").scale(1.0).shift(centre + DOWN * 2.0)
        e_lab = Tex("E").scale(1.0).shift(centre + RIGHT * 2.0)
        w_lab = Tex("W").scale(1.0).shift(centre + LEFT * 2.0)
        self.play(Write(n_lab), Write(s_lab), Write(e_lab), Write(w_lab))
        self.wait(2)
        b5_l1 = Tex("Durban from Johannesburg: SOUTH-EAST").scale(1.0).shift(band_shift(5) + RIGHT * 3.0 + UP * 1.0)
        b5_l2 = Tex("Johannesburg from Durban: NORTH-WEST").scale(1.0).shift(band_shift(5) + RIGHT * 3.0 + UP * 0.1)
        b5_l3 = Tex("Swap the towns, reverse the answer").scale(1.0).shift(band_shift(5) + RIGHT * 3.0 + DOWN * 0.8)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.wait(2)
        self.play(Write(b5_l3))
        self.wait(2)
        b5_l4 = Tex("Distance table: Jo'burg row, Durban column: 568").scale(1.05).shift(band_shift(5) + DOWN * 2.0)
        b5_l5 = Tex("Measured along ROADS, not the ruler's line").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l4))
        self.wait(2)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): contour lines and spacing
        self.next_band(6)
        b6_t = Tex("Contours: same line, same height").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        # crowded contours (steep) on the left, spread contours (gentle) right
        for i in range(5):
            self.play(Create(Line(band_shift(6) + LEFT * (4.6 - 0.35 * i) + UP * 1.2,
                                  band_shift(6) + LEFT * (4.6 - 0.35 * i) + DOWN * 0.6)),
                      run_time=0.35)
        steep_lab = Tex("close together: steep").scale(1.0).shift(band_shift(6) + LEFT * 3.8 + DOWN * 1.3)
        self.play(Write(steep_lab))
        for i in range(5):
            self.play(Create(Line(band_shift(6) + RIGHT * (0.8 + 1.0 * i) + UP * 1.2,
                                  band_shift(6) + RIGHT * (0.8 + 1.0 * i) + DOWN * 0.6)),
                      run_time=0.35)
        gentle_lab = Tex("far apart: gentle").scale(1.0).shift(band_shift(6) + RIGHT * 2.8 + DOWN * 1.3)
        self.play(Write(gentle_lab))
        self.wait(2)
        b6_l1 = Tex("Contour interval 20 m; cross five lines:").scale(1.05).shift(band_shift(6) + DOWN * 2.1)
        b6_l2 = MathTex(r"5 \times 20 = 100 \text{ m of climb}").scale(1.1).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l1))
        self.wait(2)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): gradient as 1 : n
        self.next_band(7)
        b7_t = Tex("Gradient = rise : horizontal distance").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex("Rise: 1 400 m contour up to 1 500 m = 100 m").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7_l2 = MathTex(r"\text{Map length } 4 \text{ cm}: \; 4 \times 50\;000 = 200\;000 \text{ cm}").scale(1.0).shift(band_shift(7) + UP * 0.3)
        b7_l3 = MathTex(r"200\;000 \text{ cm} = 2\;000 \text{ m}").scale(1.05).shift(band_shift(7) + DOWN * 0.6)
        b7_l4 = MathTex(r"\text{Gradient} = 100 : 2\;000 = 1 : 20").scale(1.1).shift(band_shift(7) + DOWN * 1.5)
        self.play(Write(b7_l1))
        self.wait(2)
        self.play(Write(b7_l2))
        self.wait(2)
        self.play(Write(b7_l3))
        self.wait(2)
        self.play(Write(b7_l4))
        self.play(Create(SurroundingRectangle(b7_l4, color=GREEN)))
        self.wait(2.5)
        b7_l5 = MathTex(r"\text{Second path: } 100 : 500 = 1 : 5 \; \text{ — STEEPER}").scale(1.0).shift(band_shift(7) + DOWN * 2.5)
        b7_l6 = Tex("Smaller second number = steeper slope").scale(1.05).shift(band_shift(7) + DOWN * 3.2)
        self.play(Write(b7_l5))
        self.wait(2)
        self.play(Write(b7_l6))
        self.wait(3)

        # --- Band 8 (subtopic_4): slope into time
        self.next_band(8)
        b8_t = Tex("From map to route card: time").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = Tex("Walking pace on flat ground: about 4 km/h").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l2 = MathTex(r"6 \text{ km} \div 4 \text{ km/h} = 1{,}5 \text{ h} = 90 \text{ min}").scale(1.1).shift(band_shift(8) + UP * 0.1)
        self.play(Write(b8_l1))
        self.wait(2)
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex("Add time where the contours crowd").scale(1.05).shift(band_shift(8) + DOWN * 0.9)
        b8_l4 = Tex("One map: distance, direction, slope, time").scale(1.05).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l3))
        self.wait(2)
        self.play(Write(b8_l4))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the kitchen-table map
        self.next_band(9)
        b9_t = Tex("Twenty kilometres in every centimetre").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(1.5)
        b9_l1 = Tex("One clever move first: 2 000 000 cm = 20 km").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = MathTex(r"\text{Ruler says } 28{,}5 \text{ cm}: \; 28{,}5 \times 20 = 570 \text{ km}").scale(1.0).shift(band_shift(9) + UP * 0.2)
        b9_l3 = MathTex(r"\text{Backwards shrinks: } 300 \div 20 = 15 \text{ cm}").scale(1.05).shift(band_shift(9) + DOWN * 0.8)
        self.play(Write(b9_l1))
        self.wait(2.5)
        self.play(Write(b9_l2))
        self.wait(2.5)
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(2.5)
        b9_l4 = Tex("Zoomed on a phone? The printed ratio lies").scale(1.05).shift(band_shift(9) + DOWN * 1.8)
        b9_l5 = Tex("Trust the striped bar — it grew with the roads").scale(1.05).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9_l4))
        self.wait(2)
        self.play(Write(b9_l5))
        self.wait(3)

        # --- Band 10 (subtopic_6): where it is and which way it lies
        self.next_band(10)
        b10_t = Tex("Where it is, and which way it lies").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(1.5)
        b10_l1 = Tex("Index says Harrismith D3: column D, row 3").scale(1.05).shift(band_shift(10) + UP * 1.1)
        b10_l2 = Tex("Compass language is fixed: north is up").scale(1.05).shift(band_shift(10) + UP * 0.2)
        b10_l3 = Tex("Body language travels: left becomes right").scale(1.05).shift(band_shift(10) + DOWN * 0.7)
        b10_l4 = Tex("Southbound: Midlands on your RIGHT (west)").scale(1.05).shift(band_shift(10) + DOWN * 1.6)
        b10_l5 = Tex("The triangle table knows the bends: 568 km").scale(1.05).shift(band_shift(10) + DOWN * 2.5)
        self.play(Write(b10_l1))
        self.wait(2.5)
        self.play(Write(b10_l2))
        self.wait(2)
        self.play(Write(b10_l3))
        self.wait(2)
        self.play(Write(b10_l4))
        self.wait(2)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): reading the hills without climbing them
        self.next_band(11)
        b11_t = Tex("Reading the hills without climbing them").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(1.5)
        b11_l1 = MathTex(r"\text{Cross 5 lines at 20 m each: } 5 \times 20 = 100 \text{ m}").scale(1.0).shift(band_shift(11) + UP * 1.1)
        b11_l2 = Tex("Lines crowd = ground rears up").scale(1.05).shift(band_shift(11) + UP * 0.2)
        b11_l3 = MathTex(r"100 : 2\;000 = 1:20 \quad 100 : 500 = 1:5").scale(1.05).shift(band_shift(11) + DOWN * 0.8)
        b11_l4 = Tex("One-to-five is STEEPER than one-to-twenty").scale(1.05).shift(band_shift(11) + DOWN * 1.7)
        b11_l5 = MathTex(r"6 \div 4 = 1{,}5 \text{ h} = 90 \text{ min, plus juice stops}").scale(1.0).shift(band_shift(11) + DOWN * 2.7)
        self.play(Write(b11_l1))
        self.wait(2.5)
        self.play(Write(b11_l2))
        self.wait(2)
        self.play(Write(b11_l3))
        self.wait(2.5)
        self.play(Write(b11_l4))
        self.play(Create(SurroundingRectangle(b11_l4, color=GREEN)))
        self.wait(2)
        self.play(Write(b11_l5))
        self.wait(4)
