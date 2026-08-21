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

# Band-layout whiteboard scene for the catchment-and-river-management duo
# (drainage basins, human impact and catchment management). Exporter-safe
# primitives only (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup);
# add-only lifecycle; camera moves down one frame-height per band.
# The superimposed/antecedent gorge diagrams are hand-built from Line
# chains and Arrows, assembled element by element in script order.
#
# Subtopic shares (subtopics.json, total 1635 s):
# 240/250/255/255 expert, 210/210/215 simplifier. Bands 0-7 = Part 1
# (two per expert subtopic), bands 8-10 = fresh Part 2 bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class DrainageBasinsManagementSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): superimposed drainage ---
        title = Tex("Rivers That Ignore the Rock").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0 = Tex(r"Structure writes the pattern: dendritic,").scale(1.0).shift(UP * 1.3)
        s0b = Tex(r"trellis, radial — until history interferes").scale(1.0).shift(UP * 0.6)
        self.play(Write(s0))
        self.play(Write(s0b))
        self.wait(2.5)
        # Superimposed: young flat cover over an old folded structure
        cover = Rectangle(width=7.0, height=0.8, color=GREY).shift(DOWN * 0.6)
        cover_lab = Tex(r"young flat cover").scale(0.85).shift(DOWN * 0.6 + RIGHT * 4.9)
        fold1 = Line(LEFT * 3.5 + DOWN * 2.6, LEFT * 1.8 + DOWN * 1.4, color=WHITE, stroke_width=4)
        fold2 = Line(LEFT * 1.8 + DOWN * 1.4, DOWN * 2.6, color=WHITE, stroke_width=4)
        fold3 = Line(DOWN * 2.6, RIGHT * 1.8 + DOWN * 1.4, color=WHITE, stroke_width=4)
        fold4 = Line(RIGHT * 1.8 + DOWN * 1.4, RIGHT * 3.5 + DOWN * 2.6, color=WHITE, stroke_width=4)
        fold_lab = Tex(r"buried folded structure").scale(0.85).shift(DOWN * 3.2)
        self.play(Create(cover), Write(cover_lab))
        self.play(Create(fold1), Create(fold2), Create(fold3), Create(fold4))
        self.play(Write(fold_lab))
        self.wait(2)
        river = Arrow(UP * 0.1, DOWN * 2.4, buff=0, color=BLUE)
        riv_lab = Tex(r"river keeps\\ its course").scale(0.85).shift(DOWN * 0.1 + LEFT * 4.2)
        self.play(Create(river), Write(riv_lab))
        self.wait(2)
        sup = Tex(r"SUPERIMPOSED: lowered onto old folds (Meiringspoort)").scale(0.9).shift(UP * 2.0)
        self.play(Write(sup))
        self.play(Create(SurroundingRectangle(sup, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): antecedent + the age test ---
        self.next_band(1)
        b1_t = Tex("Antecedent: the river came first").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        # Land rising into a downcutting river (steady blade picture)
        riv2 = Arrow(band_shift(1) + LEFT * 4.6 + UP * 0.6, band_shift(1) + RIGHT * 4.6 + UP * 0.6,
                     buff=0, color=BLUE)
        riv2_lab = Tex(r"river, already flowing").scale(0.85).shift(band_shift(1) + UP * 1.2 + LEFT * 2.6)
        self.play(Create(riv2), Write(riv2_lab))
        self.wait(1.5)
        rise1 = Arrow(band_shift(1) + LEFT * 1.2 + DOWN * 2.2, band_shift(1) + LEFT * 1.2 + DOWN * 0.4,
                      buff=0, color=RED)
        rise2 = Arrow(band_shift(1) + RIGHT * 1.2 + DOWN * 2.2, band_shift(1) + RIGHT * 1.2 + DOWN * 0.4,
                      buff=0, color=RED)
        rise_lab = Tex(r"uplift rises; downcutting keeps pace (Brahmaputra)").scale(0.85).shift(band_shift(1) + DOWN * 2.7)
        self.play(Create(rise1), Create(rise2))
        self.play(Write(rise_lab))
        self.wait(2)
        d1 = Tex(r"Superimposed: structure older, river let down").scale(0.95).shift(band_shift(1) + DOWN * 0.9)
        d2 = Tex(r"Antecedent: river older than the uplift").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(d1))
        self.wait(2)
        self.play(Write(d2))
        self.play(Create(SurroundingRectangle(d2, color=GREEN)))
        self.wait(2)
        d3 = Tex(r"Both: transverse gorges = dam sites, corridors").scale(0.95).shift(band_shift(1) + DOWN * 3.3)
        self.play(Write(d3))
        self.wait(3)

        # --- Band 2 (subtopic_2): vocabulary + why catchments matter ---
        self.next_band(2)
        b2_t = Tex("Basin, catchment, watershed").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        v1 = Tex(r"Basin: all land drained by river + tributaries").scale(0.95).shift(band_shift(2) + UP * 1.2)
        v2 = Tex(r"Catchment: the same land as a rain-collector").scale(0.95).shift(band_shift(2) + UP * 0.4)
        v3 = Tex(r"Watershed: the ridge between basins").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(v1))
        self.wait(2)
        self.play(Write(v2))
        self.wait(2)
        self.play(Write(v3))
        self.wait(2)
        v4 = Tex(r"A river is the summary of its whole catchment").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        self.play(Write(v4))
        self.play(Create(SurroundingRectangle(v4, color=GREEN)))
        self.wait(2)
        v5 = Tex(r"Matters: supply (Durban $\leftarrow$ uMngeni dams),").scale(0.95).shift(band_shift(2) + DOWN * 2.2)
        v6 = Tex(r"flood sponge, ecology — SA rain 465 vs 860 mm").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(v5))
        self.wait(2)
        self.play(Write(v6))
        self.wait(3)

        # --- Band 3 (subtopic_2): why management fails ---
        self.next_band(3)
        b3_t = Tex("Why catchments are poorly managed").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        m1 = Tex(r"1. Fragmented control: nobody owns the basin").scale(1.0).shift(band_shift(3) + UP * 1.2)
        m2 = Tex(r"2. Weak enforcement of admired water law").scale(1.0).shift(band_shift(3) + UP * 0.4)
        m3 = Tex(r"3. Failing sewage works (the uMsunduzi)").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        m4 = Tex(r"4. Competing users; ecological share last").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        m5 = Tex(r"5. Short-term choices: wetlands drained").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(m1))
        self.wait(2)
        self.play(Write(m2))
        self.wait(2)
        self.play(Write(m3))
        self.wait(2)
        self.play(Write(m4))
        self.wait(2)
        self.play(Write(m5))
        self.wait(3)

        # --- Band 4 (subtopic_3): the eutrophication chain ---
        self.next_band(4)
        b4_t = Tex("Impact 1 — eutrophication, in order").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        e1 = Tex(r"1. Nitrates + phosphates enter the water").scale(1.0).shift(band_shift(4) + UP * 1.2)
        e2 = Tex(r"2. Runaway algal bloom (blue-green)").scale(1.0).shift(band_shift(4) + UP * 0.4)
        e3 = Tex(r"3. Sunlight shut out; deep plants die").scale(1.0).shift(band_shift(4) + DOWN * 0.4)
        e4 = Tex(r"4. Bloom dies; bacteria decompose it").scale(1.0).shift(band_shift(4) + DOWN * 1.2)
        e5 = Tex(r"5. Oxygen collapses; life suffocates").scale(1.0).shift(band_shift(4) + DOWN * 2.0)
        self.play(Write(e1))
        self.wait(2)
        self.play(Write(e2))
        self.wait(2)
        self.play(Write(e3))
        self.wait(2)
        self.play(Write(e4))
        self.wait(2)
        self.play(Write(e5))
        self.play(Create(SurroundingRectangle(e5, color=GREEN)))
        self.wait(2)
        e6 = Tex(r"Example: Roodeplaat Dam, blooms + hyacinth").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        self.play(Write(e6))
        self.wait(3)

        # --- Band 5 (subtopic_3): the other three impacts ---
        self.next_band(5)
        b5_t = Tex("Impacts 2--4 on the catchment").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        i1 = Tex(r"Overgrazing: crusted soil $\rightarrow$ fast runoff,").scale(0.95).shift(band_shift(5) + UP * 1.2)
        i1b = Tex(r"silted dams, dongas").scale(0.95).shift(band_shift(5) + UP * 0.4)
        self.play(Write(i1))
        self.play(Write(i1b))
        self.wait(2.5)
        i2 = Tex(r"Vegetation loss: roots gone, muddy floods;").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        i2b = Tex(r"alien wattle + pine SHRINK streamflow").scale(0.95).shift(band_shift(5) + DOWN * 1.2)
        self.play(Write(i2))
        self.play(Write(i2b))
        self.wait(2.5)
        i3 = Tex(r"Settlement: sealed ground = flashier floods,").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        i3b = Tex(r"housing on floodplains, wetlands paved over").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(i3))
        self.play(Write(i3b))
        self.wait(3)

        # --- Band 6 (subtopic_4): strategies, rim to mouth ---
        self.next_band(6)
        b6_t = Tex("Strategies from rim to mouth").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        g1 = Tex(r"Govern by basin: catchment agencies").scale(0.95).shift(band_shift(6) + UP * 1.2)
        g2 = Tex(r"Guard water factories: Hottentots-Holland,").scale(0.95).shift(band_shift(6) + UP * 0.4)
        g2b = Tex(r"Maloti-Drakensberg").scale(0.95).shift(band_shift(6) + DOWN * 0.3)
        g3 = Tex(r"Repair wetlands; buffer strips on rivers").scale(0.95).shift(band_shift(6) + DOWN * 1.1)
        g4 = Tex(r"Fix sewage, treat mine acid, licence discharge").scale(0.95).shift(band_shift(6) + DOWN * 1.9)
        g5 = Tex(r"Farm gently; fix leaks; keep ecological flow").scale(0.95).shift(band_shift(6) + DOWN * 2.7)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.play(Write(g2b))
        self.wait(2)
        self.play(Write(g3))
        self.wait(2)
        self.play(Write(g4))
        self.wait(2)
        self.play(Write(g5))
        self.wait(3)

        # --- Band 7 (subtopic_4): Working for Wetlands case study ---
        self.next_band(7)
        b7_t = Tex("Case study: Working for Wetlands").scale(1.15).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        w1 = Tex(r"Problem: wetlands drained, gullied,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        w2 = Tex(r"built over — the basin's sponges lost").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(w1))
        self.play(Write(w2))
        self.wait(2.5)
        w3 = Tex(r"Method: plug drains, gabion the gullies, replant").scale(1.0).shift(band_shift(7) + DOWN * 0.5)
        self.play(Write(w3))
        self.wait(2.5)
        w4 = Tex(r"Dividend 1: sponge services restored").scale(1.0).shift(band_shift(7) + DOWN * 1.4)
        w5 = Tex(r"Dividend 2: rural jobs and training").scale(1.0).shift(band_shift(7) + DOWN * 2.2)
        self.play(Write(w4))
        self.wait(2)
        self.play(Write(w5))
        self.wait(2)
        w6 = Tex(r"Water services + livelihoods, one budget").scale(1.0).shift(band_shift(7) + DOWN * 3.1)
        self.play(Write(w6))
        self.play(Create(SurroundingRectangle(w6, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the funnel everyone lives in ---
        self.next_band(8)
        b8_t = Tex("The funnel everyone lives in").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        # Funnel: two slanted lines meeting at the river mouth
        fn_l = Line(band_shift(8) + LEFT * 3.6 + UP * 1.4, band_shift(8) + LEFT * 0.6 + DOWN * 0.6,
                    color=WHITE, stroke_width=5)
        fn_r = Line(band_shift(8) + RIGHT * 3.6 + UP * 1.4, band_shift(8) + RIGHT * 0.6 + DOWN * 0.6,
                    color=WHITE, stroke_width=5)
        fn_spout = Arrow(band_shift(8) + DOWN * 0.6, band_shift(8) + DOWN * 1.8, buff=0, color=BLUE)
        fn_lab = Tex(r"rim = watershed; spout = the river").scale(0.9).shift(band_shift(8) + UP * 1.9 + RIGHT * 0.2)
        self.play(Create(fn_l), Create(fn_r))
        self.play(Create(fn_spout))
        self.play(Write(fn_lab))
        self.wait(2)
        f1 = Tex(r"Whatever happens in the funnel ends in the river").scale(0.95).shift(band_shift(8) + DOWN * 2.3)
        self.play(Write(f1))
        self.play(Create(SurroundingRectangle(f1, color=GREEN)))
        self.wait(2.5)
        f2 = Tex(r"Dry country: Durban drinks the uMngeni funnel").scale(0.95).shift(band_shift(8) + DOWN * 3.1)
        self.play(Write(f2))
        self.wait(2.5)
        f3 = Tex(r"Gorges: lowered from above, or older than uplift").scale(0.9).shift(band_shift(8) + UP * 2.9 + RIGHT * 0.1)
        self.play(Write(f3))
        self.wait(3)

        # --- Band 9 (subtopic_6): the fish tank that turned green ---
        self.next_band(9)
        b9_t = Tex("The fish tank that turned green").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        t1 = Tex(r"Double the feeding $\rightarrow$ the water turns rich").scale(1.0).shift(band_shift(9) + UP * 1.2)
        self.play(Write(t1))
        self.wait(2)
        t2 = Tex(r"Six beats: feed, bloom, dark, die, rot, suffocate").scale(0.95).shift(band_shift(9) + UP * 0.4)
        self.play(Write(t2))
        self.play(Create(SurroundingRectangle(t2, color=GREEN)))
        self.wait(2.5)
        t3 = Tex(r"= EUTROPHICATION (over-nourishment); SA's").scale(0.95).shift(band_shift(9) + DOWN * 0.5)
        t3b = Tex(r"green tank is Roodeplaat Dam").scale(0.95).shift(band_shift(9) + DOWN * 1.3)
        self.play(Write(t3))
        self.play(Write(t3b))
        self.wait(2.5)
        t4 = Tex(r"Also: factory toxins, mine acid, plastic drains").scale(0.9).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(t4))
        self.wait(2)
        t5 = Tex(r"Crusted veld sheds silt; alien trees drink flow;").scale(0.9).shift(band_shift(9) + DOWN * 2.6)
        t5b = Tex(r"sealed tar turns storms into brown torrents").scale(0.9).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(t5))
        self.play(Write(t5b))
        self.wait(3)

        # --- Band 10 (subtopic_7): spades, sponges and the water factories ---
        self.next_band(10)
        b10_t = Tex("Spades, sponges and the water factories").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        x1 = Tex(r"Guard the mountain water factories").scale(1.0).shift(band_shift(10) + UP * 1.2)
        x2 = Tex(r"Rebuild the sponges; police the pipes").scale(0.95).shift(band_shift(10) + UP * 0.4)
        x3 = Tex(r"Farm softly; waste less; one team per funnel").scale(0.95).shift(band_shift(10) + DOWN * 0.4)
        self.play(Write(x1))
        self.wait(2)
        self.play(Write(x2))
        self.wait(2)
        self.play(Write(x3))
        self.wait(2)
        x4 = Tex(r"Working for Wetlands: plug, gabion, replant").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(x4))
        self.wait(2)
        x5 = Tex(r"Pays twice: sponge services back + rural").scale(0.95).shift(band_shift(10) + DOWN * 2.1)
        x5b = Tex(r"jobs and training — the model answer").scale(0.95).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(x5))
        self.play(Write(x5b))
        self.play(Create(SurroundingRectangle(x5b, color=GREEN)))
        self.wait(4)
