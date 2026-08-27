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

# Band-layout whiteboard scene for the CAPS Grade 12 Geography session duo
# "Agriculture, Maize and Food Security". Bands cover all seven subtopics
# (Part 1 — Expert: subtopics 1-4; Part 2 — Simplifier: subtopics 5-7) with
# dwell time proportional to subtopics.json (225/225/240/240/230/220/240 of
# 1620 s). Exporter-safe mobjects only (Tex/MathTex/Line/Arrow/Dot/Circle/
# Rectangle/SurroundingRectangle/VGroup); add-only lifecycle — no FadeOut,
# no Transform — the camera moves down to a fresh band instead.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class AgricultureMaizeFoodSecuritySession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md audio plays.
        self.wait(14)

        # --- Band 0 (subtopic_1): the small-percentage paradox ---
        title = Tex("Agriculture, Maize and Food Security").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"GDP share: only 2--3 per cent").scale(1.15).shift(UP * 0.9)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"Only about 12\% of land is arable").scale(1.15).shift(DOWN * 0.1)
        self.play(Write(b0_l2))
        self.wait(2)
        b0_wrong = Tex(r"Small percentage $=$ unimportant?").scale(1.1).shift(DOWN * 1.2)
        self.play(Write(b0_wrong))
        self.play(Create(strike(b0_wrong)))
        self.wait(2)
        b0_l3 = Tex(r"The memo expects five counter-arguments").scale(1.1).shift(DOWN * 2.3)
        self.play(Write(b0_l3))
        self.wait(3)

        # --- Band 1 (subtopic_1): the five hammers + two markets ---
        self.next_band(1)
        b1_t = Tex("Five hammers against ``unimportant''").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        b1_l1 = Tex(r"1. Food supply --- feeds 60+ million").scale(1.1).shift(band_shift(1) + UP * 1.1)
        b1_l2 = Tex(r"2. Employment --- $\pm$5\% formal + seasonal").scale(1.1).shift(band_shift(1) + UP * 0.2)
        b1_l3 = Tex(r"3. Linkages --- feeds agro-processing").scale(1.1).shift(band_shift(1) + DOWN * 0.7)
        b1_l4 = Tex(r"4. Exports --- citrus, wine, wool, maize").scale(1.1).shift(band_shift(1) + DOWN * 1.6)
        b1_l5 = Tex(r"5. Rural stability --- anchors small towns").scale(1.1).shift(band_shift(1) + DOWN * 2.5)
        for m in (b1_l1, b1_l2, b1_l3, b1_l4, b1_l5):
            self.play(Write(m))
            self.wait(1.8)
        self.wait(2)

        # --- Band 2 (subtopic_2): two farming worlds, five comparison lines ---
        self.next_band(2)
        b2_t = Tex("Two farming worlds --- compare on 5 lines").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        rail = Line(band_shift(2) + UP * 1.6, band_shift(2) + DOWN * 2.4, stroke_width=3)
        h_l = Tex("Large-scale").scale(1.05).shift(band_shift(2) + UP * 1.3 + LEFT * 3.0)
        h_r = Tex("Small-scale").scale(1.05).shift(band_shift(2) + UP * 1.3 + RIGHT * 3.0)
        self.play(Create(rail), Write(h_l), Write(h_r))
        self.wait(1.5)
        rows = [
            (r"Size: 1000s of ha", r"a few hectares", 0.4),
            (r"Capital: machines", r"hand tools", -0.3),
            (r"Labour: hired", r"the family", -1.0),
            (r"Market: nation, export", r"the household", -1.7),
            (r"Tenure: title deed", r"communal land", -2.4),
        ]
        for left_txt, right_txt, dy in rows:
            lm = Tex(left_txt).scale(0.95).shift(band_shift(2) + UP * dy + LEFT * 3.0)
            rm = Tex(right_txt).scale(0.95).shift(band_shift(2) + UP * dy + RIGHT * 3.0)
            self.play(Write(lm), Write(rm))
            self.wait(1.6)
        self.wait(2)

        # --- Band 3 (subtopic_2): balanced evaluation + the policy bridge ---
        self.next_band(3)
        b3_t = Tex("Evaluate with balance, then bridge").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        b3_l1 = Tex(r"Large: national food + exports,").scale(1.05).shift(band_shift(3) + UP * 1.1)
        b3_l2 = Tex(r"but fewer jobs per hectare").scale(1.05).shift(band_shift(3) + UP * 0.35)
        b3_l3 = Tex(r"Small: millions of livelihoods,").scale(1.05).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex(r"but low yields expose households").scale(1.05).shift(band_shift(3) + DOWN * 1.15)
        self.play(Write(b3_l1)); self.wait(1.5)
        self.play(Write(b3_l2)); self.wait(1.5)
        self.play(Write(b3_l3)); self.wait(1.5)
        self.play(Write(b3_l4)); self.wait(2)
        b3_l5 = Tex(r"Communal land cannot back a loan").scale(1.05).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(b3_l5))
        self.wait(2)
        b3_l6 = Tex(r"Bridge: finance, extension, tenure, markets").scale(1.0).shift(band_shift(3) + DOWN * 2.8)
        self.play(Write(b3_l6))
        self.play(Create(SurroundingRectangle(b3_l6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the Maize Triangle, drawn corner by corner ---
        self.next_band(4)
        b4_t = Tex("The Maize Triangle").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        c_fs = band_shift(4) + DOWN * 1.4 + LEFT * 3.2
        c_nw = band_shift(4) + UP * 1.0 + LEFT * 0.2
        c_mp = band_shift(4) + DOWN * 1.4 + RIGHT * 3.2
        d_fs = Dot(c_fs, color=YELLOW)
        l_fs = Tex("Free State (biggest)").scale(0.9).shift(c_fs + DOWN * 0.5)
        d_nw = Dot(c_nw, color=YELLOW)
        l_nw = Tex("North West -- Lichtenburg").scale(0.9).shift(c_nw + UP * 0.5)
        d_mp = Dot(c_mp, color=YELLOW)
        l_mp = Tex("Mpumalanga -- Ermelo").scale(0.9).shift(c_mp + DOWN * 0.5)
        self.play(Create(d_fs), Write(l_fs))
        self.wait(1.5)
        self.play(Create(d_nw), Write(l_nw))
        self.wait(1.5)
        self.play(Create(d_mp), Write(l_mp))
        self.wait(1.5)
        self.play(Create(Line(c_fs, c_nw, color=YELLOW)))
        self.play(Create(Line(c_nw, c_mp, color=YELLOW)))
        self.play(Create(Line(c_mp, c_fs, color=YELLOW)))
        self.wait(2)
        b4_l1 = Tex("Summer-rainfall grain country of the plateau").scale(1.0).shift(band_shift(4) + DOWN * 2.6)
        self.play(Write(b4_l1))
        self.wait(3)

        # --- Band 5 (subtopic_3): favouring factors and their shadows ---
        self.next_band(5)
        b5_t = Tex("Why there --- and what hinders").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        b5_l1 = Tex(r"Summer rain 500--800 mm in season").scale(1.05).shift(band_shift(5) + UP * 1.1)
        b5_l2 = Tex(r"Long, hot, frost-free growing period").scale(1.05).shift(band_shift(5) + UP * 0.3)
        b5_l3 = Tex(r"Deep soils on flat, machine-friendly land").scale(1.05).shift(band_shift(5) + DOWN * 0.5)
        b5_l4 = Tex(r"Silos, rail, mills, futures markets").scale(1.05).shift(band_shift(5) + DOWN * 1.3)
        for m in (b5_l1, b5_l2, b5_l3, b5_l4):
            self.play(Write(m))
            self.wait(1.6)
        b5_l5 = Tex(r"Shadows: drought, hail, frost, costs,").scale(1.05).shift(band_shift(5) + DOWN * 2.2)
        b5_l6 = Tex(r"and a climate shifting the rain westward").scale(1.05).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5)); self.wait(1.5)
        self.play(Write(b5_l6)); self.wait(3)

        # --- Band 6 (subtopic_3): maize feeds the nation twice ---
        self.next_band(6)
        b6_t = Tex("Maize feeds the nation twice").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        b6_l1 = Tex(r"White maize $\rightarrow$ mealie meal, the staple").scale(1.1).shift(band_shift(6) + UP * 1.0)
        b6_l2 = Tex(r"Yellow maize $\rightarrow$ poultry, dairy, beef feed").scale(1.1).shift(band_shift(6) + UP * 0.1)
        self.play(Write(b6_l1)); self.wait(2)
        self.play(Write(b6_l2)); self.wait(2)
        b6_l3 = Tex(r"Supports milling, feeds, grain-belt towns").scale(1.05).shift(band_shift(6) + DOWN * 0.9)
        b6_l4 = Tex(r"Surplus years: the subcontinent's maize barn").scale(1.05).shift(band_shift(6) + DOWN * 1.8)
        self.play(Write(b6_l3)); self.wait(2)
        self.play(Write(b6_l4))
        self.play(Create(SurroundingRectangle(b6_l4, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): the definition, clause by clause ---
        self.next_band(7)
        b7_t = Tex("Food security --- every clause load-bearing").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        b7_l1 = Tex(r"ALL people --- not the national average").scale(1.05).shift(band_shift(7) + UP * 1.1)
        b7_l2 = Tex(r"AT ALL times --- not only good harvests").scale(1.05).shift(band_shift(7) + UP * 0.3)
        b7_l3 = Tex(r"PHYSICAL and ECONOMIC access").scale(1.05).shift(band_shift(7) + DOWN * 0.5)
        b7_l4 = Tex(r"SUFFICIENT, SAFE, NUTRITIOUS food").scale(1.05).shift(band_shift(7) + DOWN * 1.3)
        for m in (b7_l1, b7_l2, b7_l3, b7_l4):
            self.play(Write(m))
            self.wait(1.8)
        b7_l5 = Tex(r"Nation secure, households insecure:").scale(1.05).shift(band_shift(7) + DOWN * 2.2)
        b7_l6 = Tex(r"access, not production, is the problem").scale(1.05).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(b7_l5)); self.wait(1.5)
        self.play(Write(b7_l6))
        self.play(Create(SurroundingRectangle(b7_l6, color=GREEN)))
        self.wait(3)

        # --- Band 8 (subtopic_4): factor triads and matched fixes ---
        self.next_band(8)
        b8_t = Tex("Factors in threes, fixes matched to failures").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(1.5)
        b8_l1 = Tex(r"Environmental: drought, climate, soil, water").scale(1.0).shift(band_shift(8) + UP * 1.1)
        b8_l2 = Tex(r"Economic: unemployment, prices, inputs").scale(1.0).shift(band_shift(8) + UP * 0.3)
        b8_l3 = Tex(r"Social: population, HIV/AIDS, land, conflict").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        for m in (b8_l1, b8_l2, b8_l3):
            self.play(Write(m))
            self.wait(1.8)
        b8_l4 = Tex(r"Fixes: farmer support, grants, food gardens,").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        b8_l5 = Tex(r"storage, drought-tolerant cultivars").scale(1.0).shift(band_shift(8) + DOWN * 2.1)
        self.play(Write(b8_l4)); self.wait(1.5)
        self.play(Write(b8_l5)); self.wait(1.5)
        b8_l6 = Tex(r"NSNP feeds $\pm$9 million learners daily").scale(1.05).shift(band_shift(8) + DOWN * 2.9)
        self.play(Write(b8_l6))
        self.play(Create(SurroundingRectangle(b8_l6, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): the country that runs on pap ---
        self.next_band(9)
        b9_t = Tex("The country that runs on pap").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        b9_l1 = Tex(r"Trace the plate: pap $=$ white maize").scale(1.05).shift(band_shift(9) + UP * 1.1)
        b9_l2 = Tex(r"Chicken $=$ yellow maize, hiding inside").scale(1.05).shift(band_shift(9) + UP * 0.3)
        b9_l3 = Tex(r"Maize is on your plate twice").scale(1.1).shift(band_shift(9) + DOWN * 0.5)
        self.play(Write(b9_l1)); self.wait(2)
        self.play(Write(b9_l2)); self.wait(2)
        self.play(Write(b9_l3)); self.wait(2)
        b9_l4 = Tex(r"Sweep a finger: Free State $\rightarrow$ North West").scale(1.0).shift(band_shift(9) + DOWN * 1.4)
        b9_l5 = Tex(r"$\rightarrow$ Mpumalanga highveld $=$ the Triangle").scale(1.0).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(b9_l4)); self.wait(1.8)
        self.play(Write(b9_l5)); self.wait(1.8)
        b9_l6 = Tex(r"Thunderstorm rain is a gambler: drought risk").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l6))
        self.wait(3)

        # --- Band 10 (subtopic_6): two farmers, one fence ---
        self.next_band(10)
        b10_t = Tex("Two farmers, one fence").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        fence = Line(band_shift(10) + UP * 1.5, band_shift(10) + DOWN * 1.6, color=YELLOW, stroke_width=4)
        self.play(Create(fence))
        b10_l = Tex(r"3000 ha, tractors,\\ bank loan").scale(0.85).shift(band_shift(10) + UP * 0.7 + LEFT * 3.0)
        b10_r = Tex(r"2 ha communal plot,\\family pot, no loan").scale(0.95).shift(band_shift(10) + UP * 0.7 + RIGHT * 3.0)
        self.play(Write(b10_l)); self.wait(2)
        self.play(Write(b10_r)); self.wait(2)
        b10_l2 = Tex(r"Five fingers: size, capital, labour,").scale(1.05).shift(band_shift(10) + DOWN * 1.0)
        b10_l3 = Tex(r"market, tenure $=$ five marks").scale(1.05).shift(band_shift(10) + DOWN * 1.7)
        self.play(Write(b10_l2)); self.wait(1.8)
        self.play(Write(b10_l3)); self.wait(1.8)
        b10_l4 = Tex(r"Neither is the villain --- build the bridge").scale(1.05).shift(band_shift(10) + DOWN * 2.6)
        self.play(Write(b10_l4))
        self.play(Create(SurroundingRectangle(b10_l4, color=GREEN)))
        self.wait(3)

        # --- Band 11 (subtopic_7): full silos, empty plates ---
        self.next_band(11)
        b11_t = Tex("Full silos, empty plates").scale(1.2).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_t))
        self.wait(2)
        b11_l1 = Tex(r"Riddle: full silos, hungry children?").scale(1.1).shift(band_shift(11) + UP * 1.1)
        self.play(Write(b11_l1)); self.wait(2)
        b11_l2 = Tex(r"Country secure, households insecure:").scale(1.05).shift(band_shift(11) + UP * 0.3)
        b11_l3 = Tex(r"the food is there, the money is not").scale(1.05).shift(band_shift(11) + DOWN * 0.4)
        self.play(Write(b11_l2)); self.wait(1.8)
        self.play(Write(b11_l3))
        self.play(Create(SurroundingRectangle(b11_l3, color=GREEN)))
        self.wait(2)
        b11_l4 = Tex(r"Three bags: nature, money, people").scale(1.05).shift(band_shift(11) + DOWN * 1.3)
        self.play(Write(b11_l4)); self.wait(2)
        b11_l5 = Tex(r"Fix aimed at each bag: school feeding,").scale(1.0).shift(band_shift(11) + DOWN * 2.1)
        b11_l6 = Tex(r"gardens, farmer support, better seed").scale(1.0).shift(band_shift(11) + DOWN * 2.8)
        self.play(Write(b11_l5)); self.wait(1.8)
        self.play(Write(b11_l6))
        self.wait(4)
