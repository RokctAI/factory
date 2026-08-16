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

# Band-layout whiteboard scene for the urban-climates session duo
# (urban heat islands and pollution domes). Exporter-safe primitives only
# (Tex/MathTex/Line/Arrow/Dot/Circle/Rectangle/VGroup); add-only lifecycle;
# camera moves down one frame-height per band. Diagrams (heat-island
# temperature profile, pollution dome and plume under the inversion lid)
# are hand-built element by element in script order.
#
# Subtopic shares (subtopics.json, total 1585 s):
# 235/245/245/250 expert, 200/200/210 simplifier. Bands 0-7 = Part 1
# (two bands per expert subtopic), bands 8-10 = fresh Part 2 bands.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class UrbanHeatIslandsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full-screen while intro.md plays.
        self.wait(14)

        # ===== Part 1 — Expert =====
        # --- Band 0 (subtopic_1): city vs farm, element by element ---
        title = Tex("Why City Air Differs from Farm Air").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        e1 = Tex(r"Temperature: city warmer, 2--6$^\circ$C at night").scale(1.05).shift(UP * 1.1)
        e2 = Tex(r"Surfaces: tar + concrete = low albedo,").scale(1.05).shift(UP * 0.2)
        e2b = Tex(r"absorb by day, release slowly by night").scale(1.05).shift(DOWN * 0.6)
        e3 = Tex(r"Moisture: rural ground breathes; the city").scale(1.05).shift(DOWN * 1.5)
        e3b = Tex(r"is sealed — rain races into the drains").scale(1.05).shift(DOWN * 2.3)
        self.play(Write(e1))
        self.wait(2.5)
        self.play(Write(e2))
        self.play(Write(e2b))
        self.wait(2.5)
        self.play(Write(e3))
        self.play(Write(e3b))
        self.wait(3)

        # --- Band 1 (subtopic_1): wind, rain, sunshine ---
        self.next_band(1)
        b1_t = Tex("Wind, rain and sunshine in town").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_t))
        self.wait(1.5)
        w1 = Tex(r"Wind: slower overall, but gusty canyons").scale(1.05).shift(band_shift(1) + UP * 1.1)
        w2 = Tex(r"Cloud + rain: a few \% more, on/downwind").scale(1.05).shift(band_shift(1) + UP * 0.2)
        w3 = Tex(r"Why: heat-island convection + smoke, dust").scale(1.05).shift(band_shift(1) + DOWN * 0.7)
        w4 = Tex(r"= condensation nuclei (thicker fog too)").scale(1.05).shift(band_shift(1) + DOWN * 1.5)
        w5 = Tex(r"Sunshine: haze filters it — less direct sun").scale(1.05).shift(band_shift(1) + DOWN * 2.5)
        self.play(Write(w1))
        self.wait(2.5)
        self.play(Write(w2))
        self.wait(2)
        self.play(Write(w3))
        self.play(Write(w4))
        self.wait(2.5)
        self.play(Write(w5))
        self.wait(3)

        # --- Band 2 (subtopic_2): UHI definition + temperature profile ---
        self.next_band(2)
        b2_t = Tex("The Urban Heat Island profile").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_t))
        self.wait(1.5)
        d1 = Tex(r"Dome of warmer air over the city —").scale(1.0).shift(band_shift(2) + UP * 1.3)
        d2 = Tex(r"strongest at night and in winter").scale(1.0).shift(band_shift(2) + UP * 0.6)
        self.play(Write(d1))
        self.play(Write(d2))
        self.wait(2.5)
        # Hand-built temperature profile: rural -> suburbs -> park dip -> CBD peak
        ax_x = Arrow(band_shift(2) + DOWN * 2.6 + LEFT * 5.2,
                     band_shift(2) + DOWN * 2.6 + RIGHT * 5.2, buff=0, color=WHITE)
        ax_y = Arrow(band_shift(2) + DOWN * 2.6 + LEFT * 5.0,
                     band_shift(2) + UP * 0.1 + LEFT * 5.0, buff=0, color=WHITE)
        ax_lab = Tex(r"temp").scale(0.8).shift(band_shift(2) + UP * 0.1 + LEFT * 4.3)
        self.play(Create(ax_x), Create(ax_y), Write(ax_lab))
        self.wait(1)
        p1 = Line(band_shift(2) + DOWN * 2.2 + LEFT * 4.8,
                  band_shift(2) + DOWN * 1.4 + LEFT * 2.6, color=YELLOW, stroke_width=5)
        p2 = Line(band_shift(2) + DOWN * 1.4 + LEFT * 2.6,
                  band_shift(2) + DOWN * 1.8 + LEFT * 1.2, color=YELLOW, stroke_width=5)
        p3 = Line(band_shift(2) + DOWN * 1.8 + LEFT * 1.2,
                  band_shift(2) + DOWN * 0.6 + RIGHT * 1.2, color=YELLOW, stroke_width=5)
        p4 = Line(band_shift(2) + DOWN * 0.6 + RIGHT * 1.2,
                  band_shift(2) + DOWN * 2.2 + RIGHT * 4.8, color=YELLOW, stroke_width=5)
        self.play(Create(p1))
        self.play(Create(p2))
        self.play(Create(p3))
        self.play(Create(p4))
        self.wait(1.5)
        dip_dot = Dot(band_shift(2) + DOWN * 1.8 + LEFT * 1.2, color=GREEN)
        dip_lab = Tex(r"park dip").scale(0.85).shift(band_shift(2) + DOWN * 1.2 + LEFT * 2.4)
        peak_dot = Dot(band_shift(2) + DOWN * 0.6 + RIGHT * 1.2, color=RED)
        peak_lab = Tex(r"CBD peak").scale(0.85).shift(band_shift(2) + DOWN * 0.1 + RIGHT * 2.4)
        rur_lab = Tex(r"rural").scale(0.8).shift(band_shift(2) + DOWN * 3.1 + LEFT * 4.4)
        self.play(Create(dip_dot), Write(dip_lab))
        self.play(Create(peak_dot), Write(peak_lab), Write(rur_lab))
        self.wait(3)

        # --- Band 3 (subtopic_2): the five causes ---
        self.next_band(3)
        b3_t = Tex("Five causes, five mechanisms").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_t))
        self.wait(1.5)
        c1 = Tex(r"1. Dark surfaces store heat (storage heater)").scale(1.0).shift(band_shift(3) + UP * 1.2)
        c2 = Tex(r"2. Anthropogenic heat: engines, aircons, fires").scale(1.0).shift(band_shift(3) + UP * 0.4)
        c3 = Tex(r"3. No evaporation — the city cannot sweat").scale(1.0).shift(band_shift(3) + DOWN * 0.4)
        c4 = Tex(r"4. Urban canyons trap radiation, slow cooling").scale(1.0).shift(band_shift(3) + DOWN * 1.2)
        c5 = Tex(r"5. Pollution blanket re-radiates heat down").scale(1.0).shift(band_shift(3) + DOWN * 2.0)
        self.play(Write(c1))
        self.wait(2)
        self.play(Write(c2))
        self.wait(2)
        self.play(Write(c3))
        self.wait(2)
        self.play(Write(c4))
        self.wait(2)
        self.play(Write(c5))
        self.wait(2)
        c6 = Tex(r"Night discharge $\Rightarrow$ island peaks at night").scale(1.0).shift(band_shift(3) + DOWN * 2.9)
        self.play(Write(c6))
        self.play(Create(SurroundingRectangle(c6, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): effects, grouped for the essay ---
        self.next_band(4)
        b4_t = Tex("Heat island effects, grouped").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_t))
        self.wait(1.5)
        f1 = Tex(r"Health: hot nights kill in heat waves —").scale(1.0).shift(band_shift(4) + UP * 1.2)
        f1b = Tex(r"elderly, infants, zinc-roofed housing worst").scale(1.0).shift(band_shift(4) + UP * 0.4)
        f2 = Tex(r"Energy: aircon load peaks on Eskom's grid").scale(1.0).shift(band_shift(4) + DOWN * 0.5)
        f3 = Tex(r"Weather: stronger storms over/downwind (hail)").scale(1.0).shift(band_shift(4) + DOWN * 1.4)
        f4 = Tex(r"Ecology: early budding, pests overwinter").scale(1.0).shift(band_shift(4) + DOWN * 2.3)
        self.play(Write(f1))
        self.play(Write(f1b))
        self.wait(2.5)
        self.play(Write(f2))
        self.wait(2)
        self.play(Write(f3))
        self.wait(2)
        self.play(Write(f4))
        self.wait(3)

        # --- Band 5 (subtopic_3): strategies matched to causes ---
        self.next_band(5)
        b5_t = Tex("Each strategy attacks one cause").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_t))
        self.wait(1.5)
        g1 = Tex(r"Albedo: white roofs, light paving").scale(1.0).shift(band_shift(5) + UP * 1.2)
        g2 = Tex(r"Vegetation: street trees, parks, green roofs").scale(1.0).shift(band_shift(5) + UP * 0.4)
        g3 = Tex(r"Sealed ground: permeable paving, wetlands").scale(1.0).shift(band_shift(5) + DOWN * 0.4)
        g4 = Tex(r"Waste heat: insulation, public transport").scale(1.0).shift(band_shift(5) + DOWN * 1.2)
        g5 = Tex(r"Geometry: ventilated streets, wind corridors").scale(1.0).shift(band_shift(5) + DOWN * 2.0)
        self.play(Write(g1))
        self.wait(2)
        self.play(Write(g2))
        self.wait(2)
        self.play(Write(g3))
        self.wait(2)
        self.play(Write(g4))
        self.wait(2)
        self.play(Write(g5))
        self.wait(2)
        g6 = Tex(r"Proof trees work: the park dips (Joburg greening)").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(g6))
        self.play(Create(SurroundingRectangle(g6, color=GREEN)))
        self.wait(3)

        # --- Band 6 (subtopic_4): dome vs plume + the inversion seal ---
        self.next_band(6)
        b6_t = Tex("Pollution dome and pollution plume").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_t))
        self.wait(1.5)
        ground = Line(band_shift(6) + DOWN * 2.6 + LEFT * 5.5,
                      band_shift(6) + DOWN * 2.6 + RIGHT * 5.5, color=WHITE, stroke_width=5)
        c_b1 = Rectangle(width=0.5, height=0.9, color=GREY).shift(band_shift(6) + DOWN * 2.15 + LEFT * 3.4)
        c_b2 = Rectangle(width=0.5, height=1.3, color=GREY).shift(band_shift(6) + DOWN * 1.95 + LEFT * 2.7)
        c_b3 = Rectangle(width=0.5, height=0.7, color=GREY).shift(band_shift(6) + DOWN * 2.25 + LEFT * 2.0)
        self.play(Create(ground))
        self.play(Create(c_b1), Create(c_b2), Create(c_b3))
        self.wait(1.5)
        # Dome: three chained lines over the city
        dm1 = Line(band_shift(6) + DOWN * 2.6 + LEFT * 4.6,
                   band_shift(6) + DOWN * 1.0 + LEFT * 3.8, color=YELLOW, stroke_width=5)
        dm2 = Line(band_shift(6) + DOWN * 1.0 + LEFT * 3.8,
                   band_shift(6) + DOWN * 1.0 + LEFT * 1.6, color=YELLOW, stroke_width=5)
        dm3 = Line(band_shift(6) + DOWN * 1.0 + LEFT * 1.6,
                   band_shift(6) + DOWN * 2.6 + LEFT * 0.8, color=YELLOW, stroke_width=5)
        dome_lab = Tex(r"calm: DOME").scale(0.9).shift(band_shift(6) + DOWN * 0.5 + LEFT * 2.7)
        self.play(Create(dm1), Create(dm2), Create(dm3))
        self.play(Write(dome_lab))
        self.wait(2)
        # Plume: wind arrow stretches it downwind
        wind = Arrow(band_shift(6) + DOWN * 0.9 + RIGHT * 0.2,
                     band_shift(6) + DOWN * 0.9 + RIGHT * 2.0, buff=0, color=BLUE)
        pl1 = Line(band_shift(6) + DOWN * 1.6 + RIGHT * 0.6,
                   band_shift(6) + DOWN * 1.3 + RIGHT * 4.8, color=YELLOW, stroke_width=5)
        pl2 = Line(band_shift(6) + DOWN * 2.2 + RIGHT * 0.6,
                   band_shift(6) + DOWN * 1.9 + RIGHT * 4.8, color=YELLOW, stroke_width=5)
        plume_lab = Tex(r"wind: PLUME").scale(0.9).shift(band_shift(6) + DOWN * 0.5 + RIGHT * 3.4)
        self.play(Create(wind))
        self.play(Create(pl1), Create(pl2))
        self.play(Write(plume_lab))
        self.wait(2)
        seal = Tex(r"Inversion = the seal; Kalahari High deepens it").scale(1.0).shift(band_shift(6) + DOWN * 3.3)
        self.play(Write(seal))
        self.wait(3)

        # --- Band 7 (subtopic_4): sources, effects, strategies ---
        self.next_band(7)
        b7_t = Tex("Fill it, feel it, fix it").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_t))
        self.wait(1.5)
        s1 = Tex(r"Sources: exhausts, stacks, coal + wood fires,").scale(1.0).shift(band_shift(7) + UP * 1.2)
        s1b = Tex(r"dust from mines, veld fires").scale(1.0).shift(band_shift(7) + UP * 0.4)
        self.play(Write(s1))
        self.play(Write(s1b))
        self.wait(2.5)
        s2 = Tex(r"Effects: asthma + bronchitis where burning").scale(1.0).shift(band_shift(7) + DOWN * 0.4)
        s2b = Tex(r"meets inversion; smog; acid deposition").scale(1.0).shift(band_shift(7) + DOWN * 1.2)
        self.play(Write(s2))
        self.play(Write(s2b))
        self.wait(2.5)
        s3 = Tex(r"Fix: electrification, scrubbers (Air Quality Act),").scale(0.95).shift(band_shift(7) + DOWN * 2.1)
        s3b = Tex(r"no burning on stable days, zone downwind").scale(0.95).shift(band_shift(7) + DOWN * 2.9)
        self.play(Write(s3))
        self.wait(2)
        self.play(Write(s3b))
        self.play(Create(SurroundingRectangle(s3b, color=GREEN)))
        self.wait(3)

        # ===== Part 2 — Simplifier =====
        # --- Band 8 (subtopic_5): the city is a storage heater ---
        self.next_band(8)
        b8_t = Tex("The city is a storage heater").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_t))
        self.wait(2)
        h1 = Tex(r"Evening tar still burns your feet; grass is cool").scale(1.0).shift(band_shift(8) + UP * 1.1)
        h2 = Tex(r"Tar drinks sun all day, breathes it out all night").scale(1.0).shift(band_shift(8) + UP * 0.3)
        self.play(Write(h1))
        self.wait(2.5)
        self.play(Write(h2))
        self.wait(2.5)
        h3 = Tex(r"The field sweats (evaporation cools);").scale(1.0).shift(band_shift(8) + DOWN * 0.6)
        h3b = Tex(r"the city cannot — rain runs to the drains").scale(1.0).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(h3))
        self.play(Write(h3b))
        self.wait(2.5)
        h4 = Tex(r"+ engines, canyons, haze blanket").scale(1.0).shift(band_shift(8) + DOWN * 2.2)
        self.play(Write(h4))
        self.wait(2)
        h5 = Tex(r"= URBAN HEAT ISLAND, park dips prove trees cool").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(h5))
        self.play(Create(SurroundingRectangle(h5, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): undo each sin ---
        self.next_band(9)
        b9_t = Tex("Cooling the island: undo each sin").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_t))
        self.wait(2)
        u1 = Tex(r"Dark surfaces $\rightarrow$ paint the town light").scale(1.0).shift(band_shift(9) + UP * 1.2)
        u2 = Tex(r"Cannot sweat $\rightarrow$ trees, parks, green roofs").scale(1.0).shift(band_shift(9) + UP * 0.4)
        u3 = Tex(r"Sealed ground $\rightarrow$ let the rain soak in").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        u4 = Tex(r"Little heaters $\rightarrow$ insulate, share transport").scale(1.0).shift(band_shift(9) + DOWN * 1.2)
        u5 = Tex(r"Canyon pocket $\rightarrow$ build for breeze").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(u1))
        self.wait(2)
        self.play(Write(u2))
        self.wait(2)
        self.play(Write(u3))
        self.wait(2)
        self.play(Write(u4))
        self.wait(2)
        self.play(Write(u5))
        self.wait(2)
        u6 = Tex(r"A tree cools twice: shade + transpiration").scale(1.0).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(u6))
        self.play(Create(SurroundingRectangle(u6, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the pot lid of smoke ---
        self.next_band(10)
        b10_t = Tex("The pot lid of smoke").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_t))
        self.wait(2)
        l1 = Tex(r"Still winter night: cold air below, warm above").scale(1.0).shift(band_shift(10) + UP * 1.2)
        l2 = Tex(r"Smoke climbs, hits the warm layer, flattens out").scale(1.0).shift(band_shift(10) + UP * 0.4)
        self.play(Write(l1))
        self.wait(2.5)
        self.play(Write(l2))
        self.wait(2.5)
        l3 = Tex(r"Calm makes a DOME, wind makes a PLUME").scale(1.05).shift(band_shift(10) + DOWN * 0.5)
        self.play(Write(l3))
        self.play(Create(SurroundingRectangle(l3, color=GREEN)))
        self.wait(2.5)
        l4 = Tex(r"Thickest where coal fires warm the poorest homes").scale(0.95).shift(band_shift(10) + DOWN * 1.5)
        self.play(Write(l4))
        self.wait(2.5)
        l5 = Tex(r"Fix: electrify homes, filter stacks, no burning").scale(0.95).shift(band_shift(10) + DOWN * 2.4)
        l6 = Tex(r"on still days, industry downwind of townships").scale(0.95).shift(band_shift(10) + DOWN * 3.2)
        self.play(Write(l5))
        self.play(Write(l6))
        self.wait(4)
