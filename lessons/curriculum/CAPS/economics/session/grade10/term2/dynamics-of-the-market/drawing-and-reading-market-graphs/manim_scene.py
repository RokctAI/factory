from manim import *

# Band-layout whiteboard scene for "Drawing and Reading Market Graphs"
# (grade 10, term 2). One band per teaching beat; camera moves down, earlier
# work stays. The schedule table is a Line grid + Tex cells; graphs are
# hand-built (Arrow axes, Dot points, Line curves, DashedLine readings) —
# exporter-safe primitives only, write-only reveals.
#
# Subtopic shares (subtopics.json, total 1450 s):
# 190/230/190/270/190/190/190 — subtopics 2 and 4 are the heavyweights.
#
# Graph scale used throughout: price R2-R10 -> 0.4 units per rand up;
# quantity 20-100 -> 0.07 units per unit across. So (R6, 60) = (4.2, 2.4).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DrawingReadingMarketGraphsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the schedule ---
        title = Tex("Drawing and Reading Market Graphs").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # Table: header + 5 rows, 3 columns, drawn as a Line grid.
        top, left = UP * 1.7, LEFT * 3.9
        col_w, row_h = 2.6, 0.62
        rows, cols = 6, 3
        grid = VGroup()
        for r in range(rows + 1):
            grid.add(Line(left + top + DOWN * row_h * r,
                          left + top + RIGHT * col_w * cols + DOWN * row_h * r,
                          stroke_width=2))
        for c in range(cols + 1):
            grid.add(Line(left + top + RIGHT * col_w * c,
                          left + top + RIGHT * col_w * c + DOWN * row_h * rows,
                          stroke_width=2))
        self.play(Create(grid), run_time=1.5)
        headers = ["Price (R)", "Qty demanded", "Qty supplied"]
        data = [["2", "100", "20"], ["4", "80", "40"], ["6", "60", "60"],
                ["8", "40", "80"], ["10", "20", "100"]]
        head_tex = VGroup(*[Tex(h).scale(0.7).move_to(
            left + top + RIGHT * (col_w * (c + 0.5)) + DOWN * (row_h * 0.5))
            for c, h in enumerate(headers)])
        self.play(Write(head_tex))
        for r, row in enumerate(data):
            row_tex = VGroup(*[Tex(v).scale(0.75).move_to(
                left + top + RIGHT * (col_w * (c + 0.5)) + DOWN * (row_h * (r + 1.5)))
                for c, v in enumerate(row)])
            self.play(Write(row_tex), run_time=0.7)
        self.wait(2)
        note = Tex(r"A schedule: two quantities at each price").scale(0.95).shift(DOWN * 2.7)
        self.play(Write(note))
        self.wait(3)

        # --- Band 1 (subtopic_1): interrogate the table ---
        self.next_band(1)
        b1t = Tex("Read the table before you draw").scale(1.15).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1t))
        self.wait(1.5)
        b1a = Tex(r"Demand column: 100, 80, 60, 40, 20 —").scale(1.0).shift(band_shift(1) + UP * 1.2)
        b1b = Tex(r"falls as price rises: slopes DOWN").scale(1.0).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1a))
        self.play(Write(b1b))
        self.wait(2.5)
        b1c = Tex(r"Supply column: 20, 40, 60, 80, 100 —").scale(1.0).shift(band_shift(1) + DOWN * 0.4)
        b1d = Tex(r"rises with price: slopes UP").scale(1.0).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1c))
        self.play(Write(b1d))
        self.wait(2.5)
        b1e = Tex(r"At R6 both columns say 60 —").scale(1.05).shift(band_shift(1) + DOWN * 2.0)
        b1f = Tex(r"remember that row").scale(1.05).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1e))
        self.play(Write(b1f))
        self.play(Create(SurroundingRectangle(VGroup(b1e, b1f), color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the three setup rules ---
        self.next_band(2)
        b2t = Tex("Three rules of setup").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2t))
        self.wait(1.5)
        b2a = Tex(r"1. Price VERTICAL, quantity HORIZONTAL").scale(1.0).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2a))
        self.wait(2)
        b2b = Tex(r"2. Even scales: R2-steps up,").scale(1.0).shift(band_shift(2) + UP * 0.3)
        b2c = Tex(r"20-unit steps across — never squashed").scale(1.0).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2b))
        self.play(Write(b2c))
        self.wait(2)
        b2d = Tex(r"3. Label everything: axes, title, D, S").scale(1.0).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(b2d))
        self.play(Create(SurroundingRectangle(b2d, color=GREEN)))
        self.wait(2)
        b2e = Tex(r"An uneven scale bends curves and").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        b2f = Tex(r"destroys every reading afterwards").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2e))
        self.play(Write(b2f))
        self.wait(3)

        # --- Band 3 (subtopic_2): plotting both curves ---
        self.next_band(3)
        o3 = band_shift(3) + LEFT * 4.6 + DOWN * 3.1
        x_axis = Arrow(o3, o3 + RIGHT * 8.4, buff=0, stroke_width=4)
        y_axis = Arrow(o3, o3 + UP * 5.0, buff=0, stroke_width=4)
        self.play(Create(x_axis), Create(y_axis))
        pl = Tex("Price (R)").scale(0.75).next_to(y_axis.get_end(), RIGHT, buff=0.15)
        ql = Tex("Quantity").scale(0.75).next_to(x_axis.get_end(), UP, buff=0.15)
        self.play(Write(pl), Write(ql))
        # Even tick labels.
        yticks = VGroup(*[Tex(str(p)).scale(0.6).move_to(o3 + UP * (0.4 * p) + LEFT * 0.35)
                          for p in (2, 4, 6, 8, 10)])
        xticks = VGroup(*[Tex(str(q)).scale(0.6).move_to(o3 + RIGHT * (0.07 * q) + DOWN * 0.35)
                          for q in (20, 40, 60, 80, 100)])
        self.play(Write(yticks), Write(xticks))
        self.wait(2)
        # Demand points, then line.
        d_xy = [(100, 2), (80, 4), (60, 6), (40, 8), (20, 10)]
        d_dots = VGroup(*[Dot(o3 + RIGHT * (0.07 * q) + UP * (0.4 * p), color=BLUE)
                          for q, p in d_xy])
        for dot in d_dots:
            self.play(Create(dot), run_time=0.4)
        d_line = Line(o3 + RIGHT * 7.0 + UP * 0.8, o3 + RIGHT * 1.4 + UP * 4.0,
                      color=BLUE, stroke_width=5)
        self.play(Create(d_line))
        d_lab = Tex("D", color=BLUE).scale(0.9).move_to(o3 + RIGHT * 7.3 + UP * 1.3)
        self.play(Write(d_lab))
        self.wait(2)
        # Supply points, then line.
        s_xy = [(20, 2), (40, 4), (60, 6), (80, 8), (100, 10)]
        s_dots = VGroup(*[Dot(o3 + RIGHT * (0.07 * q) + UP * (0.4 * p), color=YELLOW)
                          for q, p in s_xy])
        for dot in s_dots:
            self.play(Create(dot), run_time=0.4)
        s_line = Line(o3 + RIGHT * 1.4 + UP * 0.8, o3 + RIGHT * 7.0 + UP * 4.0,
                      color=YELLOW, stroke_width=5)
        self.play(Create(s_line))
        s_lab = Tex("S", color=YELLOW).scale(0.9).move_to(o3 + RIGHT * 7.3 + UP * 3.7)
        self.play(Write(s_lab))
        self.wait(3)

        # --- Band 4 (subtopic_3): equilibrium read off ---
        self.next_band(4)
        b4t = Tex("Finding equilibrium").scale(1.15).shift(band_shift(4) + UP * 2.8)
        self.play(Write(b4t))
        self.wait(1.5)
        o4 = band_shift(4) + LEFT * 4.6 + DOWN * 3.1
        xa4 = Arrow(o4, o4 + RIGHT * 8.4, buff=0, stroke_width=4)
        ya4 = Arrow(o4, o4 + UP * 5.0, buff=0, stroke_width=4)
        self.play(Create(xa4), Create(ya4))
        d4 = Line(o4 + RIGHT * 7.0 + UP * 0.8, o4 + RIGHT * 1.4 + UP * 4.0,
                  color=BLUE, stroke_width=5)
        s4 = Line(o4 + RIGHT * 1.4 + UP * 0.8, o4 + RIGHT * 7.0 + UP * 4.0,
                  color=YELLOW, stroke_width=5)
        self.play(Create(d4), Create(s4))
        self.wait(1.5)
        e = o4 + RIGHT * 4.2 + UP * 2.4
        e_dot = Dot(e, color=GREEN)
        self.play(Create(e_dot))
        e_lab = Tex("E").scale(0.9).next_to(e_dot, UR, buff=0.1)
        self.play(Write(e_lab))
        dash_p = DashedLine(e, o4 + UP * 2.4, color=GREEN, stroke_width=3)
        dash_q = DashedLine(e, o4 + RIGHT * 4.2, color=GREEN, stroke_width=3)
        self.play(Create(dash_p), Create(dash_q))
        p6 = Tex("R6").scale(0.75).next_to(o4 + UP * 2.4, LEFT, buff=0.12)
        q60 = Tex("60").scale(0.75).next_to(o4 + RIGHT * 4.2, DOWN, buff=0.12)
        self.play(Write(p6), Write(q60))
        self.wait(2)
        b4a = Tex(r"Matches the table's 60 = 60 row").scale(0.9).shift(band_shift(4) + RIGHT * 3.1 + UP * 1.2)
        self.play(Write(b4a))
        self.play(Create(SurroundingRectangle(b4a, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_4): excess supply at R8 ---
        self.next_band(5)
        b5t = Tex("Excess supply at R8").scale(1.15).shift(band_shift(5) + UP * 2.8)
        self.play(Write(b5t))
        self.wait(1.5)
        o5 = band_shift(5) + LEFT * 4.6 + DOWN * 3.1
        xa5 = Arrow(o5, o5 + RIGHT * 8.4, buff=0, stroke_width=4)
        ya5 = Arrow(o5, o5 + UP * 5.0, buff=0, stroke_width=4)
        self.play(Create(xa5), Create(ya5))
        d5 = Line(o5 + RIGHT * 7.0 + UP * 0.8, o5 + RIGHT * 1.4 + UP * 4.0,
                  color=BLUE, stroke_width=5)
        s5 = Line(o5 + RIGHT * 1.4 + UP * 0.8, o5 + RIGHT * 7.0 + UP * 4.0,
                  color=YELLOW, stroke_width=5)
        self.play(Create(d5), Create(s5))
        self.wait(1)
        # Level flight at R8: y = 3.2.
        flight = DashedLine(o5 + UP * 3.2, o5 + UP * 3.2 + RIGHT * 5.6,
                            color=RED, stroke_width=3)
        r8 = Tex("R8").scale(0.75).next_to(o5 + UP * 3.2, LEFT, buff=0.12)
        self.play(Write(r8), Create(flight))
        dd = Dot(o5 + RIGHT * 2.8 + UP * 3.2, color=BLUE)
        sd = Dot(o5 + RIGHT * 5.6 + UP * 3.2, color=YELLOW)
        self.play(Create(dd), Create(sd))
        drop1 = DashedLine(o5 + RIGHT * 2.8 + UP * 3.2, o5 + RIGHT * 2.8,
                           color=RED, stroke_width=3)
        drop2 = DashedLine(o5 + RIGHT * 5.6 + UP * 3.2, o5 + RIGHT * 5.6,
                           color=RED, stroke_width=3)
        self.play(Create(drop1), Create(drop2))
        q40 = Tex("40").scale(0.75).next_to(o5 + RIGHT * 2.8, DOWN, buff=0.12)
        q80 = Tex("80").scale(0.75).next_to(o5 + RIGHT * 5.6, DOWN, buff=0.12)
        self.play(Write(q40), Write(q80))
        self.wait(2)
        gap = MathTex(r"80 - 40 = 40 \text{ units}").scale(0.95).shift(band_shift(5) + RIGHT * 2.9 + UP * 1.4)
        self.play(Write(gap))
        exl = Tex(r"excess supply $=$ 40 units").scale(0.95).shift(band_shift(5) + RIGHT * 2.9 + UP * 0.6)
        self.play(Write(exl))
        self.play(Create(SurroundingRectangle(exl, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the mirror skill + verification ---
        self.next_band(6)
        b6t = Tex("The mirror — and the checks").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6t))
        self.wait(1.5)
        b6a = Tex(r"At R4: demand 80, supply 40 —").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6b = Tex(r"excess DEMAND of 40 units").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6a))
        self.play(Write(b6b))
        self.wait(2.5)
        b6w = Tex(r"Reading the two curves at different prices").scale(0.95).shift(band_shift(6) + DOWN * 0.4)
        self.play(Write(b6w))
        self.play(Create(strike(b6w)))
        self.wait(2)
        b6c = Tex(r"Both readings at ONE price, then subtract").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6c))
        self.play(Create(SurroundingRectangle(b6c, color=GREEN)))
        self.wait(2)
        b6d = Tex(r"Checks: points match rows; D down, S up;").scale(0.9).shift(band_shift(6) + DOWN * 2.2)
        b6e = Tex(r"crossing agrees with the equal row").scale(0.9).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6d))
        self.play(Write(b6e))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 7 (subtopic_5): the table is the boss ---
        self.next_band(7)
        b7t = Tex("The table is the boss").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7t))
        self.wait(2)
        b7a = Tex(r"The graph invents NOTHING — it is").scale(1.0).shift(band_shift(7) + UP * 1.2)
        b7b = Tex(r"the table's portrait").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7a))
        self.play(Write(b7b))
        self.play(Create(SurroundingRectangle(b7b, color=GREEN)))
        self.wait(2.5)
        b7c = Tex(r"Demand shrinks: downhill line coming.").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        b7d = Tex(r"Supply grows: uphill line coming.").scale(1.0).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7c))
        self.play(Write(b7d))
        self.wait(2.5)
        b7e = Tex(r"Circle the agreeing row (R6: 60 and 60) —").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        b7f = Tex(r"the lines MUST cross there").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7e))
        self.play(Write(b7f))
        self.wait(3)

        # --- Band 8 (subtopic_6): building the picture frame ---
        self.next_band(8)
        b8t = Tex("Building the picture frame").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8t))
        self.wait(2)
        b8a = Tex(r"Habit 1: price UP the side,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8b = Tex(r"quantity ALONG the bottom").scale(1.0).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8a))
        self.play(Write(b8b))
        self.wait(2)
        b8c = Tex(r"Habit 2: even steps — a squashed ruler").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        b8d = Tex(r"measures nothing").scale(1.0).shift(band_shift(8) + DOWN * 1.1)
        self.play(Write(b8c))
        self.play(Write(b8d))
        self.wait(2)
        b8e = Tex(r"Habit 3: name everything — free marks").scale(1.0).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8e))
        self.play(Create(SurroundingRectangle(b8e, color=GREEN)))
        self.wait(2)
        b8f = Tex(r"Then dots to their addresses: up to 2,").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        b8g = Tex(r"across to 100, drop the dot").scale(0.95).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8f))
        self.play(Write(b8g))
        self.wait(3)

        # --- Band 9 (subtopic_7): the answer machine ---
        self.next_band(9)
        b9t = Tex("The answer machine").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9t))
        self.wait(2)
        b9a = Tex(r"Crossing: R6 across, 60 down —").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9b = Tex(r"dotted landing gear to both axes").scale(1.0).shift(band_shift(9) + UP * 0.5)
        self.play(Write(b9a))
        self.play(Write(b9b))
        self.wait(2.5)
        b9c = Tex(r"Feed it R8: level flight — demand 40,").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9d = Tex(r"supply 80, gap 40 $=$ excess supply").scale(1.0).shift(band_shift(9) + DOWN * 1.1)
        self.play(Write(b9c))
        self.play(Write(b9d))
        self.play(Create(SurroundingRectangle(b9d, color=GREEN)))
        self.wait(2.5)
        b9e = Tex(r"One flying rule: BOTH readings on ONE").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        b9f = Tex(r"height — level flight, two touchdowns").scale(1.0).shift(band_shift(9) + DOWN * 2.7)
        self.play(Write(b9e))
        self.play(Write(b9f))
        self.wait(4)
