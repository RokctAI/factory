# Copyright (c) 2026 ROKCT INTELLIGENCE (PTY) LTD
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from manim import *

# Band-layout whiteboard scene for "Tropical Cyclones: Formation, Structure
# and Impacts" (grade 12, term 1). All seven subtopics: Part 1 Expert (1-4),
# Part 2 Simplifier (5-7). Band time apportioned to subtopics.json
# (240/250/240/260/195/205/200 of 1590 s). Exporter-safe primitives only;
# the cross-section, the doughnut and the Idai track are hand-built from
# Circle/Line/Arrow/Dot/Tex, element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class TropicalCyclonesSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the four birth conditions
        title = Tex("Tropical Cyclones").scale(1.3).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        b0_l1 = Tex(r"1. Sea $\geq$ 26,5--27 $^\circ$C, warm 50 m deep —").scale(0.9).shift(UP * 1.3)
        b0_l2 = Tex(r"evaporation loads the fuel: latent heat").scale(0.9).shift(UP * 0.6)
        self.play(Write(b0_l1))
        self.play(Write(b0_l2))
        self.wait(2.5)
        b0_l3 = Tex(r"2. At least 5$^\circ$ from the equator:").scale(0.9).shift(DOWN * 0.2)
        b0_l4 = Tex(r"Coriolis is zero ON the equator — no spin").scale(0.9).shift(DOWN * 0.9)
        self.play(Write(b0_l3))
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2.5)
        b0_l5 = Tex(r"3. Converging trade winds start the inflow").scale(0.9).shift(DOWN * 1.8)
        b0_l6 = Tex(r"4. Weak shear: calm upper air lets the").scale(0.9).shift(DOWN * 2.5)
        b0_l7 = Tex(r"chimney build straight and tall").scale(0.9).shift(DOWN * 3.2)
        self.play(Write(b0_l5))
        self.play(Write(b0_l6))
        self.play(Write(b0_l7))
        self.wait(3)

        # --- Band 1 (subtopic_1): names, season, rotation
        self.next_band(1)
        b1_title = Tex("Passports and season").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"Hurricane: N Atlantic, E Pacific").scale(0.95).shift(band_shift(1) + UP * 1.2)
        b1_l2 = Tex(r"Typhoon: NW Pacific").scale(0.95).shift(band_shift(1) + UP * 0.5)
        b1_l3 = Tex(r"Cyclone: Indian Ocean, Australia").scale(0.95).shift(band_shift(1) + DOWN * 0.2)
        self.play(Write(b1_l1))
        self.play(Write(b1_l2))
        self.play(Write(b1_l3))
        self.wait(2.5)
        b1_l4 = Tex(r"Our nursery: SW Indian Ocean east of").scale(0.95).shift(band_shift(1) + DOWN * 1.1)
        b1_l5 = Tex(r"Madagascar, November--April").scale(0.95).shift(band_shift(1) + DOWN * 1.8)
        self.play(Write(b1_l4))
        self.play(Write(b1_l5))
        self.wait(2.5)
        b1_l6 = Tex(r"Named A--Z per season; clockwise spin;").scale(0.95).shift(band_shift(1) + DOWN * 2.7)
        b1_l7 = Tex(r"drift east $\to$ west, then curve poleward").scale(0.95).shift(band_shift(1) + DOWN * 3.4)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): four growth stages
        self.next_band(2)
        b2_title = Tex("Four stages by wind speed").scale(1.2).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"Disturbance: thunderstorm cluster").scale(0.95).shift(band_shift(2) + UP * 1.2)
        self.play(Write(b2_l1))
        self.wait(2)
        b2_l2 = Tex(r"Depression: closed low, $<$ 63 km/h").scale(0.95).shift(band_shift(2) + UP * 0.4)
        self.play(Write(b2_l2))
        self.wait(2)
        b2_l3 = Tex(r"Tropical storm: 63--118 km/h — NAMED now").scale(0.95).shift(band_shift(2) + DOWN * 0.4)
        self.play(Write(b2_l3))
        self.play(Create(SurroundingRectangle(b2_l3, color=GREEN)))
        self.wait(2.5)
        b2_l4 = Tex(r"Cyclone: $>$ 118 km/h, the eye appears;").scale(0.95).shift(band_shift(2) + DOWN * 1.3)
        b2_l5 = Tex(r"categories climb to five").scale(0.95).shift(band_shift(2) + DOWN * 2.0)
        self.play(Write(b2_l4))
        self.play(Write(b2_l5))
        self.wait(2.5)
        b2_l6 = Tex(r"Central pressure can fall below 960 hPa").scale(0.95).shift(band_shift(2) + DOWN * 2.9)
        self.play(Write(b2_l6))
        self.wait(3)

        # --- Band 3 (subtopic_2): cross-section anatomy
        self.next_band(3)
        b3_title = Tex("Anatomy, centre outward").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        # Plan view: eye, eye wall ring, two spiral arm lines.
        eye = Circle(radius=0.3, color=YELLOW).shift(band_shift(3) + DOWN * 0.6)
        eye_lab = Tex("eye: sinking air, calm, clear").scale(0.8).shift(band_shift(3) + UP * 0.5)
        self.play(Create(eye), Write(eye_lab))
        self.wait(2)
        wall = Circle(radius=0.8, color=RED).shift(band_shift(3) + DOWN * 0.6)
        wall_lab = Tex(r"eye wall: strongest wind ($>$200 km/h),\\ heaviest rain").scale(0.8).shift(band_shift(3) + DOWN * 0.6 + RIGHT * 3.9)
        self.play(Create(wall), Write(wall_lab))
        self.wait(2.5)
        arm1 = Line(band_shift(3) + DOWN * 0.1 + LEFT * 0.9, band_shift(3) + UP * 0.9 + LEFT * 2.9, color=BLUE)
        arm2 = Line(band_shift(3) + DOWN * 1.3 + LEFT * 0.7, band_shift(3) + DOWN * 2.5 + LEFT * 2.5, color=BLUE)
        arm_lab = Tex(r"spiral rain bands:\\ rain in pulses").scale(0.8).shift(band_shift(3) + DOWN * 1.6 + LEFT * 4.2)
        self.play(Create(arm1), Create(arm2), Write(arm_lab))
        self.wait(2.5)
        b3_l1 = Tex(r"Loop: evaporate $\to$ spiral in $\to$ rise $\to$").scale(0.9).shift(band_shift(3) + DOWN * 3.1)
        b3_l2 = Tex(r"latent heat $\to$ deeper low $\to$ faster inflow").scale(0.9).shift(band_shift(3) + DOWN * 3.8)
        self.play(Write(b3_l1))
        self.play(Write(b3_l2))
        self.play(Create(SurroundingRectangle(b3_l2, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): the weather sequence over a town
        self.next_band(4)
        b4_title = Tex("The sequence over Quelimane").scale(1.2).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        b4_l1 = Tex(r"Approach: long swells, thin cloud thickening,").scale(0.9).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"sliding barometer, squall--lull--squall").scale(0.9).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(2.5)
        b4_l3 = Tex(r"Front half: destructive wind, blinding rain,").scale(0.9).shift(band_shift(4) + DOWN * 0.4)
        b4_l4 = Tex(r"and the STORM SURGE — the great killer").scale(0.95).shift(band_shift(4) + DOWN * 1.1)
        self.play(Write(b4_l3))
        self.play(Write(b4_l4))
        self.play(Create(SurroundingRectangle(b4_l4, color=GREEN)))
        self.wait(2.5)
        b4_l5 = Tex(r"Eye: minutes of calm at minimum pressure").scale(0.9).shift(band_shift(4) + DOWN * 2.0)
        b4_l6 = Tex(r"Back half: full violence, wind REVERSED;").scale(0.9).shift(band_shift(4) + DOWN * 2.7)
        b4_l7 = Tex(r"then rivers rise inland for days").scale(0.9).shift(band_shift(4) + DOWN * 3.4)
        self.play(Write(b4_l5))
        self.play(Write(b4_l6))
        self.play(Write(b4_l7))
        self.wait(3)

        # --- Band 5 (subtopic_3): the eye trap and how the storm dies
        self.next_band(5)
        b5_title = Tex("The eye trap and the three deaths").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        trap = Tex(r"``The sky cleared — it must be over''").scale(0.95).shift(band_shift(5) + UP * 1.2)
        self.play(Write(trap))
        self.play(Create(strike(trap)))
        self.wait(2)
        b5_l1 = Tex(r"The eye passes in 20--60 minutes; the far").scale(0.9).shift(band_shift(5) + UP * 0.2)
        b5_l2 = Tex(r"wall returns with the wind reversed").scale(0.9).shift(band_shift(5) + DOWN * 0.5)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.wait(2.5)
        b5_l3 = Tex(r"Death one: landfall — fuel line cut,").scale(0.9).shift(band_shift(5) + DOWN * 1.4)
        b5_l4 = Tex(r"friction grinds the winds (rain remains!)").scale(0.9).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l3))
        self.play(Write(b5_l4))
        self.wait(2)
        b5_l5 = Tex(r"Death two: cold water past 30$^\circ$S").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        b5_l6 = Tex(r"Death three: shear tears the chimney apart").scale(0.9).shift(band_shift(5) + DOWN * 3.6)
        self.play(Write(b5_l5))
        self.play(Write(b5_l6))
        self.wait(3)

        # --- Band 6 (subtopic_4): case study — Cyclone Idai
        self.next_band(6)
        b6_title = Tex("Case study: Idai, March 2019").scale(1.2).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex(r"Depression soaks Mozambique and Malawi,").scale(0.9).shift(band_shift(6) + UP * 1.2)
        b6_l2 = Tex(r"loops BACK over the warm Channel — refuels").scale(0.9).shift(band_shift(6) + UP * 0.5)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.play(Create(SurroundingRectangle(b6_l2, color=GREEN)))
        self.wait(2.5)
        b6_l3 = Tex(r"Strikes Beira: eye wall $+$ multi-metre surge —").scale(0.9).shift(band_shift(6) + DOWN * 0.4)
        b6_l4 = Tex(r"most of the city damaged or destroyed").scale(0.9).shift(band_shift(6) + DOWN * 1.1)
        self.play(Write(b6_l3))
        self.play(Write(b6_l4))
        self.wait(2.5)
        b6_l5 = Tex(r"Stalls inland: floods across Mozambique,").scale(0.9).shift(band_shift(6) + DOWN * 2.0)
        b6_l6 = Tex(r"Chimanimani mudslides, 1 000$+$ deaths,").scale(0.9).shift(band_shift(6) + DOWN * 2.7)
        b6_l7 = Tex(r"cholera in the floodwater's wake").scale(0.9).shift(band_shift(6) + DOWN * 3.4)
        self.play(Write(b6_l5))
        self.play(Write(b6_l6))
        self.play(Write(b6_l7))
        self.wait(3)

        # --- Band 7 (subtopic_4): satellite ID and management
        self.next_band(7)
        b7_title = Tex("Identification and management").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Satellite: tight white circle with a dark").scale(0.9).shift(band_shift(7) + UP * 1.2)
        b7_l2 = Tex(r"eye-dot vs the mid-latitude open comma").scale(0.9).shift(band_shift(7) + UP * 0.5)
        self.play(Write(b7_l1))
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(2.5)
        b7_l3 = Tex(r"Before: warnings, strong codes, mangroves,").scale(0.9).shift(band_shift(7) + DOWN * 0.4)
        b7_l4 = Tex(r"drilled evacuation, emergency kits").scale(0.9).shift(band_shift(7) + DOWN * 1.1)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex(r"During: high-ground shelter, stay in").scale(0.9).shift(band_shift(7) + DOWN * 1.9)
        b7_l6 = Tex(r"through the eye, follow broadcasts").scale(0.9).shift(band_shift(7) + DOWN * 2.6)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2)
        b7_l7 = Tex(r"After: clean water first (cholera), clinics,").scale(0.9).shift(band_shift(7) + DOWN * 3.3)
        b7_l8 = Tex(r"power, rebuild stronger — hazard natural,").scale(0.9).shift(band_shift(7) + DOWN * 4.0)
        b7_l9 = Tex(r"disaster partly social").scale(0.9).shift(band_shift(7) + DOWN * 4.6)
        self.play(Write(b7_l7))
        self.play(Write(b7_l8))
        self.play(Write(b7_l9))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the pot and the spin
        self.next_band(8)
        b8_title = Tex("The pot, the skater, the rules").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Summer ocean $=$ boiling pot; condensing").scale(0.95).shift(band_shift(8) + UP * 1.2)
        b8_l2 = Tex(r"vapour repays LATENT HEAT — the fuel").scale(0.95).shift(band_shift(8) + UP * 0.5)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.play(Create(SurroundingRectangle(b8_l2, color=GREEN)))
        self.wait(2.5)
        b8_l3 = Tex(r"Skater pulls arms in $\to$ spins faster;").scale(0.95).shift(band_shift(8) + DOWN * 0.4)
        b8_l4 = Tex(r"Coriolis bends the inflow — zero at the").scale(0.95).shift(band_shift(8) + DOWN * 1.1)
        b8_l5 = Tex(r"equator: that dance floor is closed").scale(0.95).shift(band_shift(8) + DOWN * 1.8)
        self.play(Write(b8_l3))
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex(r"Gentle upper winds; a thunderstorm cluster").scale(0.9).shift(band_shift(8) + DOWN * 2.7)
        b8_l7 = Tex(r"as the seed; hurricane/typhoon/cyclone").scale(0.9).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): the doughnut with the hole
        self.next_band(9)
        b9_title = Tex("The doughnut with the hole").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        hole = Circle(radius=0.35, color=YELLOW).shift(band_shift(9) + UP * 0.4)
        ring = Circle(radius=0.9, color=RED).shift(band_shift(9) + UP * 0.4)
        arm_a = Line(band_shift(9) + UP * 0.9 + RIGHT * 0.8, band_shift(9) + UP * 1.7 + RIGHT * 2.6, color=BLUE)
        arm_b = Line(band_shift(9) + DOWN * 0.1 + LEFT * 0.9, band_shift(9) + DOWN * 0.9 + LEFT * 2.7, color=BLUE)
        self.play(Create(hole), Create(ring))
        self.play(Create(arm_a), Create(arm_b))
        lab = Tex(r"hole: calm eye; ring: the worst place\\ on Earth; arms: rain in pulses").scale(0.85).shift(band_shift(9) + DOWN * 1.9)
        self.play(Write(lab))
        self.wait(3)
        b9_l1 = Tex(r"Quiet middle $=$ hole, NOT the end —").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        b9_l2 = Tex(r"the ring returns, wind reversed").scale(0.95).shift(band_shift(9) + DOWN * 3.6)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.play(Create(SurroundingRectangle(b9_l2, color=GREEN)))
        self.wait(2.5)
        b9_l3 = Tex(r"Surge: sea climbs like liquid up a straw,").scale(0.9).shift(band_shift(9) + DOWN * 4.3)
        self.play(Write(b9_l3))
        self.wait(3.5)

        # --- Band 10 (subtopic_7): Idai, the fuel gauge, being ready
        self.next_band(10)
        b10_title = Tex("Idai and the fuel gauge").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Inland as a depression $\to$ back over the").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l2 = Tex(r"hot Channel $\to$ refuelled $\to$ Beira $\to$").scale(0.95).shift(band_shift(10) + UP * 0.5)
        b10_l3 = Tex(r"stalls: floods and mudslides inland").scale(0.95).shift(band_shift(10) + DOWN * 0.2)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Write(b10_l3))
        self.wait(2.5)
        b10_l4 = Tex(r"Warm water: gauge fills. Land or cold").scale(0.95).shift(band_shift(10) + DOWN * 1.1)
        b10_l5 = Tex(r"water: gauge drains — the whole physics").scale(0.95).shift(band_shift(10) + DOWN * 1.8)
        self.play(Write(b10_l4))
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(2.5)
        b10_l6 = Tex(r"Pinwheel with a dot vs comma with a tail;").scale(0.9).shift(band_shift(10) + DOWN * 2.7)
        b10_l7 = Tex(r"before--during--after, and NEVER step out").scale(0.9).shift(band_shift(10) + DOWN * 3.4)
        b10_l8 = Tex(r"into the quiet middle").scale(0.9).shift(band_shift(10) + DOWN * 4.0)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.play(Write(b10_l8))
        self.wait(4)
