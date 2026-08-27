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

# Band layout: one frame-tall bands down a long canvas, camera moves down,
# nothing removed. Exporter-safe mobjects only (Tex/MathTex/Line/Arrow/Dot/
# Circle/Rectangle/VGroup); write-only reveals, no Transform/FadeOut.
#
# Mirrors script.md across the seven subtopics
# (Expert 1-4: bands 0-7; Simplifier 5-7: bands 8-10), time apportioned to
# subtopics.json (220/240/250/240/190/190/190 of 1520 s).

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class BusinessCyclesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md plays (~4-5%).
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): definition, word by word ---
        title = Tex("Business Cycles: Features, Causes, Smoothing").scale(1.15).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        d1 = Tex(r"Successive expansion and contraction").scale(1.1).shift(UP * 1.1)
        d2 = Tex(r"in aggregate activity — real GDP —").scale(1.1).shift(UP * 0.3)
        d3 = Tex(r"around a long-term growth trend").scale(1.1).shift(DOWN * 0.5)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.wait(2)
        self.play(Write(d3))
        self.wait(2)
        kw = Tex(r"Examinable words: SUCCESSIVE, REAL, TREND").scale(1.05).shift(DOWN * 1.6)
        self.play(Write(kw))
        self.play(Create(SurroundingRectangle(kw, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): the labelled wave diagram ---
        self.next_band(1)
        b1_title = Tex("Anatomy of the cycle").scale(1.2).shift(band_shift(1) + UP * 2.9)
        self.play(Write(b1_title))
        self.wait(1.5)
        o = band_shift(1) + DOWN * 2.9 + LEFT * 5.8
        y_ax = Arrow(o, o + UP * 4.6, buff=0, stroke_width=3)
        x_ax = Arrow(o, o + RIGHT * 11.0, buff=0, stroke_width=3)
        y_lab = Tex("real output").scale(0.75).shift(o + UP * 4.6 + RIGHT * 1.2)
        x_lab = Tex("time").scale(0.8).shift(o + RIGHT * 11.0 + DOWN * 0.35)
        self.play(Create(y_ax), Create(x_ax))
        self.play(Write(y_lab), Write(x_lab))
        self.wait(1.5)
        trend = Line(o + RIGHT * 0.4 + UP * 1.5, o + RIGHT * 10.4 + UP * 3.3, color=GREY)
        t_lab = Tex("trend line", color=GREY).scale(0.8).shift(o + RIGHT * 9.6 + UP * 2.5)
        self.play(Create(trend), Write(t_lab))
        self.wait(2)
        # Wave as a chain of Lines: trough -> peak -> trough -> peak
        p0 = o + RIGHT * 0.8 + UP * 0.9
        p1 = o + RIGHT * 2.0 + UP * 2.4
        p2 = o + RIGHT * 3.1 + UP * 3.5
        p3 = o + RIGHT * 4.2 + UP * 2.6
        p4 = o + RIGHT * 5.3 + UP * 1.6
        p5 = o + RIGHT * 6.6 + UP * 3.0
        p6 = o + RIGHT * 7.8 + UP * 4.2
        p7 = o + RIGHT * 9.4 + UP * 2.9
        wave = VGroup(Line(p0, p1, color=BLUE), Line(p1, p2, color=BLUE),
                      Line(p2, p3, color=BLUE), Line(p3, p4, color=BLUE),
                      Line(p4, p5, color=BLUE), Line(p5, p6, color=BLUE),
                      Line(p6, p7, color=BLUE))
        self.play(Create(wave), run_time=2.5)
        self.wait(1.5)
        tr_dot = Dot(p0, color=YELLOW)
        tr_lab = Tex("trough").scale(0.75).shift(p0 + DOWN * 0.4)
        pk_dot = Dot(p2, color=YELLOW)
        pk_lab = Tex("peak").scale(0.75).shift(p2 + UP * 0.4)
        self.play(Create(tr_dot), Write(tr_lab))
        self.play(Create(pk_dot), Write(pk_lab))
        self.wait(1.5)
        up_lab = Tex("upswing").scale(0.75).shift(p1 + LEFT * 1.3)
        dn_lab = Tex("downswing").scale(0.75).shift(p3 + RIGHT * 1.5)
        self.play(Write(up_lab), Write(dn_lab))
        self.wait(1.5)
        tr2_dot = Dot(p4, color=YELLOW)
        pk2_dot = Dot(p6, color=YELLOW)
        self.play(Create(tr2_dot), Create(pk2_dot))
        turn = Tex("peak + trough = turning points").scale(0.8).shift(o + RIGHT * 8.0 + UP * 0.7)
        self.play(Write(turn))
        self.wait(1.5)
        # Amplitude: vertical line trend -> peak; length: peak to peak
        amp = Line(p6, p6 + DOWN * 1.3, color=RED, stroke_width=5)
        amp_lab = Tex("amplitude", color=RED).scale(0.75).shift(p6 + DOWN * 0.6 + RIGHT * 1.5)
        self.play(Create(amp), Write(amp_lab))
        self.wait(1.5)
        length = Line(o + RIGHT * 3.1 + UP * 4.6, o + RIGHT * 7.8 + UP * 4.6, color=GREEN, stroke_width=4)
        len_lab = Tex("length: peak to peak", color=GREEN).scale(0.75).shift(p2 + UP * 1.3 + RIGHT * 2.4)
        self.play(Create(length), Write(len_lab))
        self.wait(2)
        rec = Tex(r"Recession: 2 quarters of falling real GDP").scale(0.85).shift(o + RIGHT * 5.6 + DOWN * 0.4)
        self.play(Write(rec))
        self.wait(2.5)

        # --- Band 2 (subtopic_2): exogenous vs endogenous ---
        self.next_band(2)
        b2_title = Tex("Why cycles happen").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        ex1 = Tex(r"EXOGENOUS — cause OUTSIDE the market").scale(1.05).shift(band_shift(2) + UP * 1.2)
        ex2 = Tex(r"Monetarists: markets stable; blame shocks").scale(1.0).shift(band_shift(2) + UP * 0.4)
        ex3 = Tex(r"and government — cure: stable policy").scale(1.0).shift(band_shift(2) + DOWN * 0.3)
        self.play(Write(ex1))
        self.wait(2)
        self.play(Write(ex2))
        self.wait(2)
        self.play(Write(ex3))
        self.wait(2)
        en1 = Tex(r"ENDOGENOUS — cause INSIDE the market").scale(1.05).shift(band_shift(2) + DOWN * 1.2)
        en2 = Tex(r"Keynesians: confidence + multiplier +").scale(1.0).shift(band_shift(2) + DOWN * 2.0)
        en3 = Tex(r"accelerator — government must lean against").scale(1.0).shift(band_shift(2) + DOWN * 2.8)
        self.play(Write(en1))
        self.wait(2)
        self.play(Write(en2))
        self.wait(2)
        self.play(Write(en3))
        self.play(Create(SurroundingRectangle(en3, color=GREEN)))
        self.wait(3)

        # --- Band 3 (subtopic_2): the catalogue of cycle types ---
        self.next_band(3)
        b3_title = Tex("Cycle types, ordered by length").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        c1 = Tex(r"KITCHIN: 3--5 yrs — inventories").scale(1.05).shift(band_shift(3) + UP * 1.1)
        c2 = Tex(r"JUGLAR: 7--11 yrs — machinery").scale(1.05).shift(band_shift(3) + UP * 0.3)
        c3 = Tex(r"KUZNETS: 15--20 yrs — building").scale(1.05).shift(band_shift(3) + DOWN * 0.5)
        c4 = Tex(r"KONDRATIEFF: 45--60 yrs — technology").scale(1.05).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.wait(2)
        ride = Tex(r"Shorter cycles ride on longer ones").scale(1.0).shift(band_shift(3) + DOWN * 2.3)
        self.play(Write(ride))
        self.play(Create(SurroundingRectangle(ride, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): monetary policy against the wave ---
        self.next_band(4)
        b4_title = Tex("Monetary policy: the SARB leans in").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        i1 = Tex(r"Main lever: the REPO RATE").scale(1.05).shift(band_shift(4) + UP * 1.2)
        i2 = Tex(r"Also: open-market transactions,").scale(1.0).shift(band_shift(4) + UP * 0.4)
        i3 = Tex(r"cash reserve requirement, moral suasion").scale(1.0).shift(band_shift(4) + DOWN * 0.3)
        self.play(Write(i1))
        self.wait(2)
        self.play(Write(i2))
        self.play(Write(i3))
        self.wait(2)
        e1 = Tex(r"Downswing: EXPANSIONARY — repo cut").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        e2 = Tex(r"to a record 3,5\% in 2020").scale(1.0).shift(band_shift(4) + DOWN * 1.9)
        self.play(Write(e1))
        self.play(Write(e2))
        self.wait(2)
        e3 = Tex(r"Upswing: CONTRACTIONARY — 2022--23 hikes").scale(1.0).shift(band_shift(4) + DOWN * 2.8)
        self.play(Write(e3))
        self.play(Create(SurroundingRectangle(e3, color=GREEN)))
        self.wait(3)

        # --- Band 5 (subtopic_3): fiscal policy, stabilisers, limits ---
        self.next_band(5)
        b5_title = Tex("Fiscal policy and its limits").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        f1 = Tex(r"Downswing: spend more, tax less,").scale(1.0).shift(band_shift(5) + UP * 1.2)
        f2 = Tex(r"wider deficit — the multiplier magnifies").scale(1.0).shift(band_shift(5) + UP * 0.5)
        self.play(Write(f1))
        self.play(Write(f2))
        self.wait(2)
        f3 = Tex(r"Automatic stabilisers: progressive tax,").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        f4 = Tex(r"grants and UIF — no pen lifted").scale(1.0).shift(band_shift(5) + DOWN * 1.1)
        self.play(Write(f3))
        self.play(Write(f4))
        self.wait(2)
        l1 = Tex(r"Limits: LAGS, debt costs, crowding out").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(l1))
        self.wait(2)
        l2 = Tex(r"Cheaper credit builds no power stations").scale(1.0).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(l2))
        self.play(Create(SurroundingRectangle(l2, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): the new economic paradigm ---
        self.next_band(6)
        b6_title = Tex("The new economic paradigm").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        n1 = Tex(r"Demand side: inflation targeting,").scale(1.05).shift(band_shift(6) + UP * 1.2)
        n2 = Tex(r"disciplined budgets — anchor expectations").scale(1.0).shift(band_shift(6) + UP * 0.5)
        self.play(Write(n1))
        self.play(Write(n2))
        self.wait(2.5)
        n3 = Tex(r"Supply side: infrastructure, skills,").scale(1.05).shift(band_shift(6) + DOWN * 0.4)
        n4 = Tex(r"competition — the trend line climbs faster").scale(1.0).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(n3))
        self.play(Write(n4))
        self.wait(2.5)
        wrongp = Tex(r"Smoothing abolishes the cycle").scale(1.0).shift(band_shift(6) + DOWN * 2.0 + LEFT * 2.6)
        self.play(Write(wrongp))
        self.play(Create(strike(wrongp)))
        n5 = Tex(r"It narrows the AMPLITUDE").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(n5))
        self.play(Create(SurroundingRectangle(n5, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): indicators and forecasting tools ---
        self.next_band(7)
        b7_title = Tex("Reading the future: indicators").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        ld = Tex(r"LEADING — turn first: new orders,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        ld2 = Tex(r"building plans, shares, confidence").scale(1.0).shift(band_shift(7) + UP * 0.5)
        self.play(Write(ld))
        self.play(Write(ld2))
        self.wait(2)
        co = Tex(r"COINCIDENT — with: retail sales, production").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        self.play(Write(co))
        self.wait(2)
        lg = Tex(r"LAGGING — after: unemployment").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(lg))
        self.wait(2)
        tools = Tex(r"Tools: trend line, extrapolation,").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        tools2 = Tex(r"moving averages — plus length and amplitude").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(tools))
        self.play(Write(tools2))
        self.play(Create(SurroundingRectangle(tools2, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): a town that breathes ---
        self.next_band(8)
        b8_title = Tex("A town that breathes").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        t1 = Tex(r"Quiet bottom, nothing worse — TROUGH").scale(1.0).shift(band_shift(8) + UP * 1.2)
        t2 = Tex(r"Bookings, hiring, wages respent — UPSWING").scale(1.0).shift(band_shift(8) + UP * 0.4)
        t3 = Tex(r"Town FULL, prices creep — PEAK").scale(1.0).shift(band_shift(8) + DOWN * 0.4)
        t4 = Tex(r"Each loss causes the next — DOWNSWING").scale(1.0).shift(band_shift(8) + DOWN * 1.2)
        self.play(Write(t1))
        self.wait(2.5)
        self.play(Write(t2))
        self.wait(2.5)
        self.play(Write(t3))
        self.wait(2.5)
        self.play(Write(t4))
        self.wait(2.5)
        keep = Tex(r"Wave $=$ cycle; slope $=$ trend; swing $=$ amplitude").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(keep))
        self.play(Create(SurroundingRectangle(keep, color=GREEN)))
        self.wait(3.5)

        # --- Band 9 (subtopic_6): the thermostat and the budget ---
        self.next_band(9)
        b9_title = Tex("The thermostat and the budget").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        th1 = Tex(r"Repo rate $=$ thermostat for spending").scale(1.05).shift(band_shift(9) + UP * 1.2)
        th2 = Tex(r"Too cold: rate DOWN (2020, 3,5\%)").scale(1.0).shift(band_shift(9) + UP * 0.4)
        th3 = Tex(r"Too hot: rate UP (2022--23 hikes)").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        self.play(Write(th1))
        self.wait(2.5)
        self.play(Write(th2))
        self.wait(2)
        self.play(Write(th3))
        self.wait(2)
        bu1 = Tex(r"Budget: bad year spend, fat year save").scale(1.0).shift(band_shift(9) + DOWN * 1.3)
        bu2 = Tex(r"UIF + tax lean automatically — shock absorber").scale(0.95).shift(band_shift(9) + DOWN * 2.1)
        self.play(Write(bu1))
        self.wait(2.5)
        self.play(Write(bu2))
        self.wait(2)
        hon = Tex(r"Honest limits: slow, and no power stations").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(hon))
        self.play(Create(SurroundingRectangle(hon, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): reading the signs ---
        self.next_band(10)
        b10_title = Tex("Reading the signs before the turn").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        s1 = Tex(r"Signs FIRST: bookings, plans — LEADING").scale(1.0).shift(band_shift(10) + UP * 1.2)
        s2 = Tex(r"Signs WITH: the tills — COINCIDENT").scale(1.0).shift(band_shift(10) + UP * 0.4)
        s3 = Tex(r"Signs LATE: permanent hires — LAGGING").scale(1.0).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(s1))
        self.wait(2.5)
        self.play(Write(s2))
        self.wait(2.5)
        self.play(Write(s3))
        self.wait(2.5)
        ma = Tex(r"Moving average smooths; extrapolation").scale(1.0).shift(band_shift(10) + DOWN * 1.3)
        ma2 = Tex(r"extends — and fails at the turning point").scale(1.0).shift(band_shift(10) + DOWN * 2.1)
        self.play(Write(ma))
        self.play(Write(ma2))
        self.wait(2.5)
        final = Tex(r"Narrow the amplitude, raise the trend").scale(1.05).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(final))
        self.play(Create(SurroundingRectangle(final, color=GREEN)))
        self.wait(4)
