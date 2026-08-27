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

# Band-layout whiteboard scene for "High-Pressure Cells and Travelling
# Disturbances" (grade 12, term 1). All seven subtopics: Part 1 Expert (1-4),
# Part 2 Simplifier (5-7). Band time apportioned to subtopics.json
# (235/255/255/245/195/205/210 of 1600 s). Exporter-safe primitives only; the
# three-highs map, the inversion ceiling and the berg-wind descent are built
# from Circle/Line/Arrow/Dot/Tex, element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SubtropicalAnticyclonesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the three highs on the map
        title = Tex("Subtropical Anticyclones").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"SA sits near 30$^\circ$S — inside the").scale(0.95).shift(UP * 1.5)
        b0_l2 = Tex(r"subtropical high-pressure belt").scale(0.95).shift(UP * 0.8)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        # Schematic map: country box with three H cells around it.
        country = Rectangle(width=2.6, height=1.8).shift(DOWN * 1.1)
        country_lab = Tex("SA").scale(0.8).shift(DOWN * 1.1)
        self.play(Create(country), Write(country_lab))
        h_w = Circle(radius=0.55, color=BLUE).shift(DOWN * 1.1 + LEFT * 3.6)
        h_w_lab = Tex("H").scale(0.9).shift(DOWN * 1.1 + LEFT * 3.6)
        h_e = Circle(radius=0.55, color=RED).shift(DOWN * 1.1 + RIGHT * 3.6)
        h_e_lab = Tex("H").scale(0.9).shift(DOWN * 1.1 + RIGHT * 3.6)
        h_k = Circle(radius=0.45, color=YELLOW).shift(DOWN * 0.9)
        self.play(Create(h_w), Write(h_w_lab))
        self.play(Create(h_e), Write(h_e_lab))
        self.play(Create(h_k))
        w_lab = Tex("South Atlantic High").scale(0.7).shift(DOWN * 2.2 + LEFT * 3.6)
        e_lab = Tex("South Indian High").scale(0.7).shift(DOWN * 2.2 + RIGHT * 3.6)
        k_lab = Tex("Kalahari High (seasonal)").scale(0.7).shift(DOWN * 2.5)
        self.play(Write(w_lab), Write(e_lab))
        self.play(Write(k_lab))
        self.wait(2.5)
        b0_l3 = Tex(r"Rule: highs turn ANTICLOCKWISE down here").scale(0.95).shift(DOWN * 3.3)
        self.play(Write(b0_l3))
        self.play(Create(SurroundingRectangle(b0_l3, color=GREEN)))
        self.wait(3)

        # --- Band 1 (subtopic_1): character of the three cells
        self.next_band(1)
        b1_title = Tex("Character of the cells").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Atlantic cell: cool air north, Benguela").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"upwelling — fog coast, Namib aridity").scale(0.95).shift(band_shift(1) + UP * 0.5)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.wait(2.5)
        b1_l3 = Tex(r"Indian cell: warm moist air onto the").scale(0.95).shift(band_shift(1) + DOWN * 0.4)
        b1_l4 = Tex(r"east coast — KZN's humid summers").scale(0.95).shift(band_shift(1) + DOWN * 1.1)
        self.play(Write(b1_l3))
        self.play(Write(b1_l4))
        self.wait(2.5)
        b1_l5 = Tex(r"Kalahari cell: strong at the surface in winter,").scale(0.9).shift(band_shift(1) + DOWN * 2.0)
        b1_l6 = Tex(r"weakened and lifted in summer").scale(0.9).shift(band_shift(1) + DOWN * 2.7)
        self.play(Write(b1_l5))
        self.play(Write(b1_l6))
        self.wait(2)
        b1_l7 = Tex(r"All three: sinking air $=$ dry, stable, clear").scale(0.95).shift(band_shift(1) + DOWN * 3.5)
        self.play(Write(b1_l7))
        self.play(Create(SurroundingRectangle(b1_l7, color=GREEN)))
        self.wait(3)

        # --- Band 2 (subtopic_2): the inversion ceiling, winter vs summer
        self.next_band(2)
        b2_title = Tex("The inversion ceiling").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        # Escarpment step with a movable ceiling line.
        floor = Line(band_shift(2) + DOWN * 2.6 + LEFT * 5.4, band_shift(2) + DOWN * 2.6 + LEFT * 1.4)
        step = Line(band_shift(2) + DOWN * 2.6 + LEFT * 1.4, band_shift(2) + DOWN * 1.2 + LEFT * 1.4)
        plateau = Line(band_shift(2) + DOWN * 1.2 + LEFT * 1.4, band_shift(2) + DOWN * 1.2 + RIGHT * 5.0)
        esc_lab = Tex("escarpment").scale(0.75).shift(band_shift(2) + DOWN * 2.0 + LEFT * 0.2)
        self.play(Create(floor), Create(step), Create(plateau), Write(esc_lab))
        self.wait(2)
        winter_ceiling = Line(band_shift(2) + DOWN * 1.7 + LEFT * 5.4,
                              band_shift(2) + DOWN * 1.7 + LEFT * 1.4, color=ORANGE)
        w_c_lab = Tex("winter: ceiling BELOW the step").scale(0.85).shift(band_shift(2) + DOWN * 0.5 + LEFT * 3.2)
        self.play(Create(winter_ceiling), Write(w_c_lab))
        self.wait(2.5)
        summer_ceiling = Line(band_shift(2) + UP * 0.6 + LEFT * 1.0,
                              band_shift(2) + UP * 0.6 + RIGHT * 5.0, color=RED)
        s_c_lab = Tex("summer: ceiling lifts high above it").scale(0.85).shift(band_shift(2) + UP * 1.3 + RIGHT * 1.8)
        self.play(Create(summer_ceiling), Write(s_c_lab))
        self.wait(2.5)
        b2_l1 = Tex(r"Winter: moisture locked out, frost and haze;").scale(0.9).shift(band_shift(2) + DOWN * 3.3)
        b2_l2 = Tex(r"summer: moist air pours in — afternoon storms").scale(0.9).shift(band_shift(2) + DOWN * 3.9)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(3)

        # --- Band 3 (subtopic_2): migration, currents, ridging
        self.next_band(3)
        b3_title = Tex("Migration, currents, ridging").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Belt follows the sun: north in winter").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l2 = Tex(r"(fronts reach the Cape), south in summer").scale(0.95).shift(band_shift(3) + UP * 0.5)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.wait(2.5)
        b3_l3 = Tex(r"Benguela: cold, foggy, desert west coast;").scale(0.95).shift(band_shift(3) + DOWN * 0.4)
        b3_l4 = Tex(r"Agulhas: warm, humid, green east coast").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l3))
        self.play(Write(b3_l4))
        self.wait(2.5)
        b3_l5 = Tex(r"Ridging: Atlantic High hooks around the").scale(0.95).shift(band_shift(3) + DOWN * 2.0)
        b3_l6 = Tex(r"south coast behind each front — onshore").scale(0.95).shift(band_shift(3) + DOWN * 2.7)
        b3_l7 = Tex(r"air, showers: rain in ALL seasons there").scale(0.95).shift(band_shift(3) + DOWN * 3.4)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.play(Write(b3_l7))
        self.play(Create(SurroundingRectangle(b3_l7, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the moisture front
        self.next_band(4)
        b4_title = Tex("The moisture front (dry line)").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Summer interior: humid NE air meets").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"hot dry western air along a boundary").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        dry_line = Line(band_shift(4) + DOWN * 0.3 + LEFT * 3.6,
                        band_shift(4) + DOWN * 2.1 + RIGHT * 2.8, color=YELLOW)
        dl_lab = Tex("NW--SE line of storms").scale(0.8).shift(band_shift(4) + DOWN * 0.9 + RIGHT * 3.3)
        self.play(Create(dry_line), Write(dl_lab))
        st1 = Dot(band_shift(4) + DOWN * 0.6 + LEFT * 2.6, color=RED)
        st2 = Dot(band_shift(4) + DOWN * 1.1 + LEFT * 1.0, color=RED)
        st3 = Dot(band_shift(4) + DOWN * 1.6 + RIGHT * 0.8, color=RED)
        self.play(Create(st1), Create(st2), Create(st3))
        self.wait(2.5)
        b4_l3 = Tex(r"Line thunderstorms: downpours, lightning,").scale(0.95).shift(band_shift(4) + DOWN * 2.9)
        b4_l4 = Tex(r"hail, flash floods — warnings and drains").scale(0.95).shift(band_shift(4) + DOWN * 3.6)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.wait(3)

        # --- Band 5 (subtopic_3): coastal low and berg wind
        self.next_band(5)
        b5_title = Tex("Coastal low and berg wind").scale(1.2).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex(r"Coastal low: shallow cell under the").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex(r"escarpment, sliding along the coast").scale(0.95).shift(band_shift(5) + UP * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2)
        b5_l3 = Tex(r"Ahead: hot dry offshore; behind: cool").scale(0.95).shift(band_shift(5) + DOWN * 0.3)
        b5_l4 = Tex(r"moist onshore — ten degrees in an hour").scale(0.95).shift(band_shift(5) + DOWN * 1.0)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2.5)
        b5_l5 = Tex(r"Berg wind: plateau air falls $\sim$1 500 m,").scale(0.95).shift(band_shift(5) + DOWN * 1.9)
        b5_l6 = Tex(r"warms $\approx$ 1 $^\circ$C per 100 m $\to$ $\sim$14 $^\circ$C hotter").scale(0.95).shift(band_shift(5) + DOWN * 2.6)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.play(Create(SurroundingRectangle(b5_l6, color=GREEN)))
        self.wait(2.5)
        b5_l7 = Tex(r"Peak fire danger: bans, breaks, standby crews").scale(0.9).shift(band_shift(5) + DOWN * 3.4)
        self.play(Write(b5_l7))
        self.wait(3)

        # --- Band 6 (subtopic_4): the chart drill — highs and season
        self.next_band(6)
        b6_title = Tex("Chart drill: highs and season").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Find the H cells: Atlantic west, Indian east,").scale(0.95).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"Kalahari inland (winter); 1020 hPa and up").scale(0.95).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(2.5)
        b6_l3 = Tex(r"Season clue 1: strong interior high $=$ winter;").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex(r"heat low with moist NE inflow $=$ summer").scale(0.9).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex(r"Clue 2: fronts at the Cape $=$ winter;").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        b6_l6 = Tex(r"clue 3: interior dew points — teens summer,").scale(0.9).shift(band_shift(6) + DOWN * 2.7)
        b6_l7 = Tex(r"near or below zero winter").scale(0.9).shift(band_shift(6) + DOWN * 3.4)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # --- Band 7 (subtopic_4): signatures and prediction
        self.next_band(7)
        b7_title = Tex("Signatures and prediction").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Ridging: isobars hook east around the south").scale(0.95).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"coast $\to$ onshore SW wind, cool, drizzle").scale(0.95).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.wait(2.5)
        b7_l3 = Tex(r"Coastal low $+$ berg wind: hot dry offshore").scale(0.95).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex(r"ahead, abrupt cool change behind").scale(0.95).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2.5)
        b7_l5 = Tex(r"Moisture front: interior trough, moist east").scale(0.95).shift(band_shift(7) + DOWN * 2.0)
        b7_l6 = Tex(r"flank, diagonal storm line on satellite").scale(0.95).shift(band_shift(7) + DOWN * 2.7)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2.5)
        b7_l7 = Tex(r"Predict: west $\to$ east; ridging follows fronts —").scale(0.9).shift(band_shift(7) + DOWN * 3.5)
        b7_l8 = Tex(r"always give the mechanism").scale(0.9).shift(band_shift(7) + DOWN * 4.1)
        self.play(Write(b7_l7))
        self.play(Write(b7_l8))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): three guards around the country
        self.next_band(8)
        b8_title = Tex("Three guards around the country").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"West guard: cold water, fog coast, desert").scale(0.95).shift(band_shift(8) + UP * 1.2)
        self.play(Write(b8_l1))
        self.wait(2)
        b8_l2 = Tex(r"East guard: warm wet air — bathwater sea,").scale(0.95).shift(band_shift(8) + UP * 0.4)
        b8_l3 = Tex(r"soupy February afternoons").scale(0.95).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8_l2))
        self.play(Write(b8_l3))
        self.wait(2.5)
        b8_l4 = Tex(r"Inside guard: heavy in winter, floats up").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex(r"in summer — the moody one").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex(r"Sinking air wipes cloud like a warm cloth").scale(0.95).shift(band_shift(8) + DOWN * 2.8)
        b8_l7 = Tex(r"on a mirror; highs go AGAINST the clock").scale(0.95).shift(band_shift(8) + DOWN * 3.5)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.play(Create(SurroundingRectangle(b8_l7, color=GREEN)))
        self.wait(3)

        # --- Band 9 (subtopic_6): the pot lid over Bloemfontein
        self.next_band(9)
        b9_title = Tex("The pot lid over Bloemfontein").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Pot $=$ plateau; lid $=$ inversion layer").scale(0.95).shift(band_shift(9) + UP * 1.3)
        self.play(Write(b9_l1))
        self.wait(2)
        b9_l2 = Tex(r"Winter: lid screwed down below the step —").scale(0.95).shift(band_shift(9) + UP * 0.5)
        b9_l3 = Tex(r"frost, blue sky, brown haze trapped under it").scale(0.95).shift(band_shift(9) + DOWN * 0.2)
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.wait(2.5)
        b9_l4 = Tex(r"Summer: lid floats high — wet air climbs the").scale(0.95).shift(band_shift(9) + DOWN * 1.1)
        b9_l5 = Tex(r"step, four-o'clock storms over hot ground").scale(0.95).shift(band_shift(9) + DOWN * 1.8)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex(r"Wet air meets desert air: storms queue on").scale(0.95).shift(band_shift(9) + DOWN * 2.7)
        b9_l7 = Tex(r"the moisture front like beads on a wire").scale(0.95).shift(band_shift(9) + DOWN * 3.4)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.play(Create(SurroundingRectangle(b9_l7, color=GREEN)))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): the hairdryer and the cool change
        self.next_band(10)
        b10_title = Tex("The hairdryer and the cool change").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        # Berg wind descent: escarpment edge with falling arrow.
        top = Line(band_shift(10) + UP * 0.9 + LEFT * 4.8, band_shift(10) + UP * 0.9 + LEFT * 2.4)
        drop = Arrow(band_shift(10) + UP * 0.9 + LEFT * 2.4, band_shift(10) + DOWN * 1.5 + RIGHT * 0.6, color=ORANGE)
        sea = Line(band_shift(10) + DOWN * 1.5 + RIGHT * 0.6, band_shift(10) + DOWN * 1.5 + RIGHT * 5.0, color=BLUE)
        drop_lab = Tex(r"falls 1 500 m, $+$14 $^\circ$C").scale(0.85).shift(band_shift(10) + DOWN * 0.1 + LEFT * 2.9)
        self.play(Create(top), Create(drop), Create(sea))
        self.play(Write(drop_lab))
        self.wait(2.5)
        b10_l1 = Tex(r"East London: mid-thirties in July —").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l2 = Tex(r"a hairdryer aimed at the coast; fire wind").scale(0.95).shift(band_shift(10) + DOWN * 2.9)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex(r"Coastal low $=$ bead on a wire: hairdryer ahead,").scale(0.9).shift(band_shift(10) + DOWN * 3.7)
        b10_l4 = Tex(r"cool change behind — jersey by supper").scale(0.9).shift(band_shift(10) + DOWN * 4.3)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(4)
