from manim import *

# Band-layout whiteboard scene for the CAPS Grade 11 Geography session duo
# "Unequal Heating and the Energy Balance". One band per teaching beat; the
# camera moves down to fresh space and nothing is ever removed. Diagrams are
# hand-built from Line/Arrow/Dot/Circle/Rectangle/Tex only (exporter-safe).
# Subtopic time shares follow subtopics.json:
# 215/230/230/220/180/190/205 of 1470 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class UnequalHeatingEnergyBalanceSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic held full screen while intro.md audio plays.
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): insolation and the angle of incidence
        title = Tex("Unequal Heating and the Energy Balance").scale(1.25).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex(r"Insolation: $1\,367$ W/m$^2$ at the top").scale(1.15).shift(UP * 1.0)
        self.play(Write(s0_l1))
        self.wait(2)
        s0_l2 = Tex("Same above Kalahari and Antarctica").scale(1.1).shift(UP * 0.1)
        self.play(Write(s0_l2))
        self.wait(2)
        s0_l3 = Tex("What differs: the ANGLE OF INCIDENCE").scale(1.15).shift(DOWN * 0.9)
        self.play(Write(s0_l3))
        self.play(Create(SurroundingRectangle(s0_l3, color=GREEN)))
        self.wait(2)
        s0_l4 = Tex("Curved earth $=$ same beam, more ground").scale(1.1).shift(DOWN * 2.0)
        self.play(Write(s0_l4))
        self.wait(3)

        # --- Band 1 (subtopic_1): beam-spread diagram + path length + albedo
        self.next_band(1)
        b1_title = Tex("Spread thin, then filtered hard").scale(1.2).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        # curved surface approximated as a 3-segment line chain
        surf = VGroup(
            Line(LEFT * 5.5 + DOWN * 1.6, LEFT * 2.0 + DOWN * 1.1, color=WHITE),
            Line(LEFT * 2.0 + DOWN * 1.1, RIGHT * 1.5 + DOWN * 1.3, color=WHITE),
            Line(RIGHT * 1.5 + DOWN * 1.3, RIGHT * 5.5 + DOWN * 2.2, color=WHITE),
        ).shift(band_shift(1))
        self.play(Create(surf[0]), Create(surf[1]), Create(surf[2]))
        # equator: vertical rays onto a small patch
        eq_rays = VGroup(
            Arrow(LEFT * 4.4 + UP * 1.4, LEFT * 4.4 + DOWN * 1.3, color=YELLOW, buff=0),
            Arrow(LEFT * 3.6 + UP * 1.4, LEFT * 3.6 + DOWN * 1.2, color=YELLOW, buff=0),
        ).shift(band_shift(1))
        eq_lab = Tex("Equator: steep, small patch").scale(0.9).shift(band_shift(1) + LEFT * 3.6 + DOWN * 2.3)
        self.play(Create(eq_rays[0]), Create(eq_rays[1]))
        self.play(Write(eq_lab))
        self.wait(2)
        # pole: oblique rays smeared over a wide patch
        po_rays = VGroup(
            Arrow(RIGHT * 0.6 + UP * 1.6, RIGHT * 2.6 + DOWN * 1.5, color=YELLOW, buff=0),
            Arrow(RIGHT * 1.6 + UP * 1.6, RIGHT * 3.8 + DOWN * 1.8, color=YELLOW, buff=0),
        ).shift(band_shift(1))
        po_lab = Tex("Pole: oblique, big patch").scale(0.9).shift(band_shift(1) + RIGHT * 3.4 + DOWN * 2.7)
        self.play(Create(po_rays[0]), Create(po_rays[1]))
        self.play(Write(po_lab))
        self.wait(2)
        b1_l1 = Tex("Path length: oblique ray crosses more air").scale(1.0).shift(band_shift(1) + UP * 1.9 + RIGHT * 0.2)
        self.play(Write(b1_l1))
        self.wait(2.5)
        b1_l2 = Tex(r"Albedo: snow $80$--$90\%$, ocean $<10\%$").scale(1.0).shift(band_shift(1) + UP * 1.0 + RIGHT * 0.2)
        self.play(Write(b1_l2))
        self.wait(3)

        # --- Band 2 (subtopic_1): the standard budget + lapse rate
        self.next_band(2)
        b2_title = Tex("The standard insolation budget").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"$\approx 30\%$ reflected back to space").scale(1.1).shift(band_shift(2) + UP * 1.1)
        b2_l2 = Tex(r"$\approx 20\%$ absorbed in the atmosphere").scale(1.1).shift(band_shift(2) + UP * 0.2)
        b2_l3 = Tex(r"$\approx 50\%$ absorbed at the surface").scale(1.1).shift(band_shift(2) + DOWN * 0.7)
        self.play(Write(b2_l1))
        self.wait(2)
        self.play(Write(b2_l2))
        self.wait(2)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2)
        b2_l4 = Tex("Air is heated from below, so it").scale(1.05).shift(band_shift(2) + DOWN * 1.7)
        b2_l5 = Tex(r"cools with height: $6{,}5\,^\circ$C per km").scale(1.1).shift(band_shift(2) + DOWN * 2.6)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(3)

        # --- Band 3 (subtopic_2): tilt, parallelism, the four dates
        self.next_band(3)
        b3_title = Tex("The axis, the revolution, the seasons").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Tilt $23{,}5^\circ$ — held fixed: PARALLELISM").scale(1.1).shift(band_shift(3) + UP * 1.1)
        self.play(Write(b3_l1))
        self.wait(2.5)
        b3_l2 = Tex(r"22 Dec: sun over Capricorn — our summer").scale(1.05).shift(band_shift(3) + UP * 0.2)
        b3_l3 = Tex(r"21 Jun: sun over Cancer — our winter").scale(1.05).shift(band_shift(3) + DOWN * 0.7)
        b3_l4 = Tex(r"21 Mar / 23 Sep: equinoxes, 12 h day").scale(1.05).shift(band_shift(3) + DOWN * 1.6)
        self.play(Write(b3_l2))
        self.wait(2)
        self.play(Write(b3_l3))
        self.wait(2)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex("Capricorn crosses Limpopo").scale(1.05).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.wait(3)

        # --- Band 4 (subtopic_2): the altitude calculation + distance trap
        self.next_band(4)
        b4_title = Tex(r"Midday altitude, Cape Town ($34^\circ$S)").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = MathTex(r"\text{altitude} = 90^\circ - \text{angular distance}").scale(1.05).shift(band_shift(4) + UP * 1.2)
        self.play(Write(b4_l1))
        self.wait(2)
        b4_l2 = MathTex(r"22\text{ Dec}: 34 - 23{,}5 = 10{,}5^\circ").scale(1.05).shift(band_shift(4) + UP * 0.3)
        b4_l3 = MathTex(r"90 - 10{,}5 = 79{,}5^\circ").scale(1.1).shift(band_shift(4) + DOWN * 0.5)
        self.play(Write(b4_l2))
        self.wait(2)
        self.play(Write(b4_l3))
        self.play(Create(SurroundingRectangle(b4_l3, color=GREEN)))
        self.wait(2)
        b4_l4 = MathTex(r"21\text{ Jun}: 34 + 23{,}5 = 57{,}5^\circ").scale(1.05).shift(band_shift(4) + DOWN * 1.4)
        b4_l5 = MathTex(r"90 - 57{,}5 = 32{,}5^\circ \;\; (47^\circ \text{ swing})").scale(1.05).shift(band_shift(4) + DOWN * 2.2)
        self.play(Write(b4_l4))
        self.wait(2)
        self.play(Write(b4_l5))
        self.play(Create(SurroundingRectangle(b4_l5, color=GREEN)))
        self.wait(2)
        b4_trap = Tex("Closest to sun in January — distance").scale(0.95).shift(band_shift(4) + DOWN * 3.0 + LEFT * 2.2)
        b4_trap2 = Tex("is NOT the cause").scale(0.95).shift(band_shift(4) + DOWN * 3.0 + RIGHT * 3.4)
        self.play(Write(b4_trap), Write(b4_trap2))
        self.wait(3)

        # --- Band 5 (subtopic_3): radiation, greenhouse, conduction
        self.next_band(5)
        b5_title = Tex("How energy moves: radiation, conduction").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        # shortwave in / longwave out arrows over a ground line
        ground5 = Line(LEFT * 5.0 + DOWN * 1.4, RIGHT * 5.0 + DOWN * 1.4, color=WHITE).shift(band_shift(5))
        sw = Arrow(LEFT * 3.5 + UP * 1.4, LEFT * 2.0 + DOWN * 1.3, color=YELLOW, buff=0).shift(band_shift(5))
        sw_lab = Tex("shortwave in").scale(0.9).shift(band_shift(5) + LEFT * 4.3 + UP * 0.4)
        lw = Arrow(RIGHT * 2.0 + DOWN * 1.3, RIGHT * 3.5 + UP * 1.4, color=RED, buff=0).shift(band_shift(5))
        lw_lab = Tex("longwave out").scale(0.9).shift(band_shift(5) + RIGHT * 4.3 + UP * 0.4)
        self.play(Create(ground5))
        self.play(Create(sw), Write(sw_lab))
        self.wait(2)
        self.play(Create(lw), Write(lw_lab))
        self.wait(2)
        b5_l1 = Tex(r"Greenhouse gases: $-18\,^\circ$C $\rightarrow$ $+15\,^\circ$C").scale(1.0).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l1))
        self.wait(2.5)
        b5_l2 = Tex("Conduction: contact only, lowest cm of air").scale(0.95).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l2))
        self.wait(3)

        # --- Band 6 (subtopic_3): convection, advection, latent heat
        self.next_band(6)
        b6_title = Tex("Convection, advection, latent heat").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        conv = Arrow(LEFT * 3.5 + DOWN * 0.6, LEFT * 3.5 + UP * 1.2, color=YELLOW, buff=0).shift(band_shift(6))
        conv_lab = Tex("convection: VERTICAL").scale(0.95).shift(band_shift(6) + LEFT * 3.3 + DOWN * 1.3)
        adv = Arrow(RIGHT * 1.2 + UP * 0.3, RIGHT * 4.6 + UP * 0.3, color=BLUE, buff=0).shift(band_shift(6))
        adv_lab = Tex("advection: HORIZONTAL").scale(0.95).shift(band_shift(6) + RIGHT * 2.9 + DOWN * 0.4)
        self.play(Create(conv), Write(conv_lab))
        self.wait(2)
        self.play(Create(adv), Write(adv_lab))
        self.wait(2)
        b6_l1 = Tex("Highveld cumulonimbus; Durban sea breeze").scale(0.95).shift(band_shift(6) + DOWN * 2.0)
        self.play(Write(b6_l1))
        self.wait(2)
        b6_l2 = Tex(r"Latent heat: $2{,}5$ MJ per kg evaporated").scale(1.05).shift(band_shift(6) + DOWN * 2.9)
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(3)

        # --- Band 7 (subtopic_4): surplus and deficit by latitude
        self.next_band(7)
        b7_title = Tex("Surplus and deficit").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        # latitude bar: pole - 40N - equator - 40S - pole
        lat_line = Line(LEFT * 5.0 + UP * 0.6, RIGHT * 5.0 + UP * 0.6, color=WHITE).shift(band_shift(7))
        d_40n = Dot(LEFT * 2.0 + UP * 0.6).shift(band_shift(7))
        d_40s = Dot(RIGHT * 2.0 + UP * 0.6).shift(band_shift(7))
        lab_40n = MathTex(r"40^\circ\text{N}").scale(0.9).shift(band_shift(7) + LEFT * 2.0 + UP * 1.2)
        lab_40s = MathTex(r"40^\circ\text{S}").scale(0.9).shift(band_shift(7) + RIGHT * 2.0 + UP * 1.2)
        self.play(Create(lat_line))
        self.play(Create(d_40n), Create(d_40s), Write(lab_40n), Write(lab_40s))
        self.wait(2)
        sur_lab = Tex("SURPLUS: absorbed $>$ lost").scale(1.0).shift(band_shift(7) + DOWN * 0.2)
        def_l = Tex("DEFICIT").scale(0.9).shift(band_shift(7) + LEFT * 4.2 + DOWN * 0.2)
        def_r = Tex("DEFICIT").scale(0.9).shift(band_shift(7) + RIGHT * 4.2 + DOWN * 0.2)
        self.play(Write(sur_lab))
        self.play(Write(def_l), Write(def_r))
        self.wait(2.5)
        b7_l1 = Tex("Gap stays stable, so heat MUST").scale(1.0).shift(band_shift(7) + DOWN * 1.3)
        b7_l2 = Tex("move poleward, continuously").scale(1.0).shift(band_shift(7) + DOWN * 2.1)
        tr_l = Arrow(LEFT * 0.8 + DOWN * 2.9, LEFT * 3.8 + DOWN * 2.9, color=YELLOW, buff=0).shift(band_shift(7))
        tr_r = Arrow(RIGHT * 0.8 + DOWN * 2.9, RIGHT * 3.8 + DOWN * 2.9, color=YELLOW, buff=0).shift(band_shift(7))
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(tr_l), Create(tr_r))
        self.wait(3)

        # --- Band 8 (subtopic_4): the two carriers + the balance identity
        self.next_band(8)
        b8_title = Tex("Who carries the heat?").scale(1.2).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(1.5)
        b8_l1 = Tex(r"Atmosphere: $\approx \tfrac{3}{4}$ — cells, westerlies,").scale(1.05).shift(band_shift(8) + UP * 1.1)
        b8_l1b = Tex("jet streams, latent heat").scale(1.05).shift(band_shift(8) + UP * 0.3)
        b8_l2 = Tex(r"Oceans: $\approx \tfrac{1}{4}$ — warm Agulhas south,").scale(1.05).shift(band_shift(8) + DOWN * 0.6)
        b8_l2b = Tex("cold Benguela north").scale(1.05).shift(band_shift(8) + DOWN * 1.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l1b))
        self.wait(2.5)
        self.play(Write(b8_l2))
        self.play(Write(b8_l2b))
        self.wait(2.5)
        b8_l3 = MathTex(r"\text{energy in} = \text{energy out}").scale(1.15).shift(band_shift(8) + DOWN * 2.4)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 9 (subtopic_5): a torch against a wall
        self.next_band(9)
        b9_title = Tex("A torch against a wall").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        wall9 = Line(LEFT * 5.0 + DOWN * 0.6, RIGHT * 5.0 + DOWN * 0.6, color=WHITE).shift(band_shift(9))
        self.play(Create(wall9))
        t_straight = Arrow(LEFT * 3.2 + UP * 1.4, LEFT * 3.2 + DOWN * 0.5, color=YELLOW, buff=0).shift(band_shift(9))
        c_small = Circle(radius=0.35, color=YELLOW).shift(band_shift(9) + LEFT * 3.2 + DOWN * 0.6)
        lab_small = Tex("small hot circle").scale(0.9).shift(band_shift(9) + LEFT * 3.2 + DOWN * 1.5)
        self.play(Create(t_straight), Create(c_small))
        self.play(Write(lab_small))
        self.wait(2)
        t_slant = Arrow(RIGHT * 0.8 + UP * 1.4, RIGHT * 3.0 + DOWN * 0.5, color=YELLOW, buff=0).shift(band_shift(9))
        oval = VGroup(
            Line(RIGHT * 1.8 + DOWN * 0.6, RIGHT * 4.4 + DOWN * 0.6, color=YELLOW),
        ).shift(band_shift(9))
        lab_oval = Tex("stretched dim oval").scale(0.9).shift(band_shift(9) + RIGHT * 3.1 + DOWN * 1.5)
        self.play(Create(t_slant), Create(oval[0]))
        self.play(Write(lab_oval))
        self.wait(2.5)
        b9_l1 = Tex("Slant also crosses more air — taxi rank").scale(0.95).shift(band_shift(9) + DOWN * 2.3)
        b9_l2 = Tex("White bakkie bounces light: albedo").scale(0.95).shift(band_shift(9) + DOWN * 3.0)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(3)

        # --- Band 10 (subtopic_6): the ball that never straightens up
        self.next_band(10)
        b10_title = Tex("The ball that never straightens up").scale(1.15).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        ball = Circle(radius=0.8, color=BLUE).shift(band_shift(10) + LEFT * 3.0 + UP * 0.4)
        axis = Line(LEFT * 3.5 + DOWN * 0.7, LEFT * 2.5 + UP * 1.5, color=WHITE).shift(band_shift(10))
        axis_lab = MathTex(r"23{,}5^\circ").scale(0.9).shift(band_shift(10) + LEFT * 1.4 + UP * 1.4)
        self.play(Create(ball), Create(axis))
        self.play(Write(axis_lab))
        self.wait(2)
        b10_l1 = Tex("Lean TOWARD the lamp: December").scale(1.0).shift(band_shift(10) + RIGHT * 2.3 + UP * 0.7)
        b10_l2 = Tex("Lean AWAY: June").scale(1.0).shift(band_shift(10) + RIGHT * 2.3 + DOWN * 0.1)
        self.play(Write(b10_l1))
        self.wait(2)
        self.play(Write(b10_l2))
        self.wait(2)
        b10_l3 = MathTex(r"\text{Cape Town: } 79{,}5^\circ \text{ vs } 32{,}5^\circ").scale(1.05).shift(band_shift(10) + DOWN * 1.2)
        self.play(Write(b10_l3))
        self.play(Create(SurroundingRectangle(b10_l3, color=GREEN)))
        self.wait(2)
        b10_myth = Tex("``Winter because further from the sun''").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        self.play(Write(b10_myth))
        self.play(Create(strike(b10_myth)))
        b10_l4 = Tex("Closest in January — it is the lean").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l4))
        self.wait(3)

        # --- Band 11 (subtopic_7): braai heat and the spaza budget
        self.next_band(11)
        b11_title = Tex("Kettle, braai and taxi — moving heat").scale(1.15).shift(band_shift(11) + UP * 2.2)
        self.play(Write(b11_title))
        self.wait(2)
        b11_l1 = Tex("Palms warm across the gap: RADIATION").scale(0.95).shift(band_shift(11) + UP * 1.2)
        b11_l2 = Tex("Hot grid handle: CONDUCTION").scale(0.95).shift(band_shift(11) + UP * 0.5)
        b11_l3 = Tex("Shimmer rising: CONVECTION").scale(0.95).shift(band_shift(11) + DOWN * 0.2)
        b11_l4 = Tex("Wind carries it sideways: ADVECTION").scale(0.95).shift(band_shift(11) + DOWN * 0.9)
        b11_l5 = Tex("Sweat steals heat: LATENT HEAT").scale(0.95).shift(band_shift(11) + DOWN * 1.6)
        self.play(Write(b11_l1))
        self.wait(2)
        self.play(Write(b11_l2))
        self.wait(2)
        self.play(Write(b11_l3))
        self.wait(2)
        self.play(Write(b11_l4))
        self.wait(2)
        self.play(Write(b11_l5))
        self.wait(2.5)
        b11_l6 = Tex(r"Spaza budget: winds carry $\tfrac{3}{4}$, currents $\tfrac{1}{4}$").scale(1.0).shift(band_shift(11) + DOWN * 2.6)
        self.play(Write(b11_l6))
        self.play(Create(SurroundingRectangle(b11_l6, color=GREEN)))
        self.wait(4)
