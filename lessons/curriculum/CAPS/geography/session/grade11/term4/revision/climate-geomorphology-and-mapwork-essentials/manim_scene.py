from manim import *

# Band-layout whiteboard scene for the revision duo "Climate, Geomorphology
# and Mapwork Essentials" (grade 11, term 4). All seven subtopics: Part 1
# Expert (1-4), Part 2 Simplifier (5-7). Band time apportioned to
# subtopics.json (250/260/255/255/190/195/195 of 1600 s). Exporter-safe
# primitives only; every profile (Karoo sequence, cuesta, slope elements)
# is a hand-built Line chain with Dot/Tex labels, drawn element by element.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class ClimateGeomorphologyMapworkSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        # Intro beat: topic full-screen while intro.md audio plays.
        self.wait(15)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): unequal heating and the pressure chain
        title = Tex("Climate, Geomorphology and Mapwork").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        # Globe with concentrated vs smeared rays.
        globe = Circle(radius=1.1, color=BLUE).shift(LEFT * 3.4 + UP * 0.3)
        self.play(Create(globe))
        ray1 = Arrow(LEFT * 0.6 + UP * 0.3, LEFT * 2.2 + UP * 0.3, color=YELLOW)
        ray2 = Arrow(LEFT * 0.6 + UP * 1.7, LEFT * 2.6 + UP * 1.15, color=YELLOW)
        self.play(Create(ray1), Create(ray2))
        g_lab1 = Tex(r"tropics: vertical rays,\\ concentrated").scale(0.8).shift(LEFT * 3.4 + DOWN * 1.5)
        g_lab2 = Tex(r"poles: low angle,\\ smeared wide").scale(0.8).shift(LEFT * 3.4 + UP * 2.1)
        self.play(Write(g_lab1), Write(g_lab2))
        self.wait(2.5)
        b0_l1 = Tex(r"Surplus equator--40$^\circ$; deficit poleward").scale(0.95).shift(RIGHT * 2.9 + UP * 1.3)
        self.play(Write(b0_l1))
        self.wait(2)
        b0_l2 = Tex(r"Heated air rises $\Rightarrow$ LOW;").scale(0.95).shift(RIGHT * 2.9 + UP * 0.4)
        b0_l3 = Tex(r"cooled air sinks $\Rightarrow$ HIGH;").scale(0.95).shift(RIGHT * 2.9 + DOWN * 0.3)
        b0_l4 = Tex(r"wind flows high $\to$ low").scale(0.95).shift(RIGHT * 2.9 + DOWN * 1.0)
        self.play(Write(b0_l2))
        self.wait(1.5)
        self.play(Write(b0_l3))
        self.wait(1.5)
        self.play(Write(b0_l4))
        self.play(Create(SurroundingRectangle(b0_l4, color=GREEN)))
        self.wait(2)
        b0_l5 = Tex(r"Circulation hauls surplus energy poleward").scale(0.95).shift(DOWN * 2.6)
        self.play(Write(b0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): belts, cells, Coriolis
        self.next_band(1)
        b1_title = Tex("Belts, cells and the bend").scale(1.2).shift(band_shift(1) + UP * 2.2)
        self.play(Write(b1_title))
        self.wait(1.5)
        b1_l1 = Tex(r"0$^\circ$ equatorial LOW — rising, rain").scale(0.95).shift(band_shift(1) + UP * 1.3)
        b1_l2 = Tex(r"30$^\circ$ subtropical HIGHS — subsiding, dry").scale(0.95).shift(band_shift(1) + UP * 0.6)
        b1_l3 = Tex(r"60$^\circ$ subpolar LOWS; poles: polar HIGHS").scale(0.95).shift(band_shift(1) + DOWN * 0.1)
        self.play(Write(b1_l1))
        self.wait(1.8)
        self.play(Write(b1_l2))
        self.wait(1.8)
        self.play(Write(b1_l3))
        self.wait(2)
        b1_l4 = Tex(r"Belts migrate with the overhead sun").scale(1.0).shift(band_shift(1) + DOWN * 0.9)
        self.play(Write(b1_l4))
        self.wait(2)
        b1_l5 = Tex(r"Hadley (trades), Ferrel (westerlies), Polar").scale(0.95).shift(band_shift(1) + DOWN * 1.7)
        self.play(Write(b1_l5))
        self.wait(2)
        b1_l6 = Tex(r"Coriolis: winds bend LEFT in the south —").scale(0.95).shift(band_shift(1) + DOWN * 2.5)
        b1_l7 = Tex(r"SE trades at Durban, SW gales at the Cape").scale(0.95).shift(band_shift(1) + DOWN * 3.2)
        self.play(Write(b1_l6))
        self.play(Write(b1_l7))
        self.wait(3)

        # --- Band 2 (subtopic_2): Africa's rain switch
        self.next_band(2)
        b2_title = Tex("Africa: convergence vs subsidence").scale(1.15).shift(band_shift(2) + UP * 2.2)
        self.play(Write(b2_title))
        self.wait(1.5)
        b2_l1 = Tex(r"ITCZ: thundery seam where trades meet —").scale(0.95).shift(band_shift(2) + UP * 1.3)
        b2_l2 = Tex(r"migrates south in summer: our wet season").scale(0.95).shift(band_shift(2) + UP * 0.6)
        self.play(Write(b2_l1))
        self.play(Write(b2_l2))
        self.wait(2.5)
        b2_l3 = Tex(r"Three highs around southern Africa:").scale(0.95).shift(band_shift(2) + DOWN * 0.3)
        b2_l4 = Tex(r"South Atlantic, South Indian, Kalahari").scale(0.95).shift(band_shift(2) + DOWN * 1.0)
        self.play(Write(b2_l3))
        self.play(Write(b2_l4))
        self.wait(2.5)
        b2_l5 = Tex(r"Winter Kalahari High: dry frosty Highveld").scale(0.95).shift(band_shift(2) + DOWN * 1.8)
        self.play(Write(b2_l5))
        self.wait(2)
        b2_l6 = Tex(r"East coast wet: warm Agulhas feeds air;").scale(0.95).shift(band_shift(2) + DOWN * 2.6)
        b2_l7 = Tex(r"west coast dry: cold Benguela $+$ subsidence").scale(0.95).shift(band_shift(2) + DOWN * 3.3)
        self.play(Write(b2_l6))
        self.play(Write(b2_l7))
        self.wait(3)

        # --- Band 3 (subtopic_2): drought ladder and desertification
        self.next_band(3)
        b3_title = Tex("Drought is not desertification").scale(1.2).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex(r"Drought: rainfall below the EXPECTED").scale(1.0).shift(band_shift(3) + UP * 1.3)
        self.play(Write(b3_l1))
        self.wait(2)
        b3_l2 = Tex(r"Ladder: meteorological $\to$ hydrological").scale(0.95).shift(band_shift(3) + UP * 0.5)
        b3_l3 = Tex(r"$\to$ agricultural $\to$ socio-economic").scale(0.95).shift(band_shift(3) + DOWN * 0.2)
        self.play(Write(b3_l2))
        self.play(Write(b3_l3))
        self.play(Create(SurroundingRectangle(VGroup(b3_l2, b3_l3), color=GREEN)))
        self.wait(2.5)
        b3_l4 = Tex(r"El Ni\~no dries our summers; La Ni\~na wets").scale(0.95).shift(band_shift(3) + DOWN * 1.1)
        self.play(Write(b3_l4))
        self.wait(2)
        b3_l5 = Tex(r"Desertification: long-term land degradation —").scale(0.95).shift(band_shift(3) + DOWN * 1.9)
        b3_l6 = Tex(r"overgrazing, overcultivation, deforestation").scale(0.95).shift(band_shift(3) + DOWN * 2.6)
        self.play(Write(b3_l5))
        self.play(Write(b3_l6))
        self.wait(2.5)
        b3_l7 = Tex(r"Manage: carrying capacity, rotation, Green Wall").scale(0.9).shift(band_shift(3) + DOWN * 3.3)
        self.play(Write(b3_l7))
        self.wait(3)

        # --- Band 4 (subtopic_3): horizontal strata — the Karoo sequence
        self.next_band(4)
        b4_title = Tex("Flat strata: plateau to conical hill").scale(1.15).shift(band_shift(4) + UP * 2.2)
        self.play(Write(b4_title))
        self.wait(1.5)
        base_y = DOWN * 1.6
        ground = Line(band_shift(4) + base_y + LEFT * 6.0, band_shift(4) + base_y + RIGHT * 6.0)
        self.play(Create(ground))
        # Mesa: wide flat cap, steep sides.
        mesa = VGroup(
            Line(band_shift(4) + base_y + LEFT * 5.2, band_shift(4) + base_y + UP * 1.4 + LEFT * 4.8),
            Line(band_shift(4) + base_y + UP * 1.4 + LEFT * 4.8, band_shift(4) + base_y + UP * 1.4 + LEFT * 2.6),
            Line(band_shift(4) + base_y + UP * 1.4 + LEFT * 2.6, band_shift(4) + base_y + LEFT * 2.2),
        )
        mesa_lab = Tex("mesa: top wider than height").scale(0.8).shift(band_shift(4) + base_y + DOWN * 0.6 + LEFT * 3.7)
        self.play(Create(mesa), Write(mesa_lab))
        self.wait(2)
        # Butte: narrow, taller than wide.
        butte = VGroup(
            Line(band_shift(4) + base_y + LEFT * 0.7, band_shift(4) + base_y + UP * 1.5 + LEFT * 0.45),
            Line(band_shift(4) + base_y + UP * 1.5 + LEFT * 0.45, band_shift(4) + base_y + UP * 1.5 + RIGHT * 0.45),
            Line(band_shift(4) + base_y + UP * 1.5 + RIGHT * 0.45, band_shift(4) + base_y + RIGHT * 0.7),
        )
        butte_lab = Tex("butte").scale(0.8).shift(band_shift(4) + base_y + DOWN * 0.6)
        self.play(Create(butte), Write(butte_lab))
        self.wait(2)
        # Conical hill: cap stripped, soft cone.
        cone = VGroup(
            Line(band_shift(4) + base_y + RIGHT * 2.4, band_shift(4) + base_y + UP * 1.1 + RIGHT * 3.5),
            Line(band_shift(4) + base_y + UP * 1.1 + RIGHT * 3.5, band_shift(4) + base_y + RIGHT * 4.6),
        )
        cone_lab = Tex("conical hill: cap gone").scale(0.8).shift(band_shift(4) + base_y + DOWN * 0.6 + RIGHT * 3.5)
        self.play(Create(cone), Write(cone_lab))
        self.wait(2)
        b4_l1 = Tex(r"Hard dolerite cap protects soft shale;").scale(0.95).shift(band_shift(4) + UP * 1.2)
        b4_l2 = Tex(r"differential erosion, slopes retreat sideways").scale(0.95).shift(band_shift(4) + UP * 0.5)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(3)

        # --- Band 5 (subtopic_3): inclined and massive rock
        self.next_band(5)
        b5_title = Tex("Tilted books and granite domes").scale(1.15).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        # Cuesta profile: long gentle dip slope, short steep scarp.
        c_base = band_shift(5) + UP * 0.2
        dip = Line(c_base + LEFT * 5.4, c_base + UP * 1.1 + LEFT * 1.6, color=BLUE)
        scarp = Line(c_base + UP * 1.1 + LEFT * 1.6, c_base + LEFT * 0.9, color=RED)
        dip_lab = Tex("dip slope: gentle").scale(0.8).shift(c_base + UP * 1.2 + LEFT * 4.4)
        scarp_lab = Tex("scarp: steep").scale(0.8).shift(c_base + UP * 0.9 + RIGHT * 0.6)
        self.play(Create(dip), Write(dip_lab))
        self.play(Create(scarp), Write(scarp_lab))
        self.wait(2)
        b5_l1 = Tex(r"Dip $<25^\circ$: cuesta; moderate: homoclinal;").scale(0.9).shift(band_shift(5) + DOWN * 0.7)
        b5_l2 = Tex(r"near-vertical: hogsback — steeper tilt,").scale(0.9).shift(band_shift(5) + DOWN * 1.4)
        b5_l3 = Tex(r"more equal slopes").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l1))
        self.wait(2)
        self.play(Write(b5_l2))
        self.play(Write(b5_l3))
        self.play(Create(SurroundingRectangle(b5_l3, color=GREEN)))
        self.wait(2)
        # Granite dome: shallow polyline arc.
        d_base = band_shift(5) + DOWN * 3.2
        dome = VGroup(
            Line(d_base + RIGHT * 1.0, d_base + UP * 0.5 + RIGHT * 1.9),
            Line(d_base + UP * 0.5 + RIGHT * 1.9, d_base + UP * 0.7 + RIGHT * 3.0),
            Line(d_base + UP * 0.7 + RIGHT * 3.0, d_base + UP * 0.5 + RIGHT * 4.1),
            Line(d_base + UP * 0.5 + RIGHT * 4.1, d_base + RIGHT * 5.0),
        )
        dome_lab = Tex(r"batholith dome:\\ exfoliation (Paarl)").scale(0.8).shift(d_base + UP * 0.5 + LEFT * 1.4)
        self.play(Create(dome), Write(dome_lab))
        self.wait(2)
        b5_l4 = Tex(r"Jointed blocks rot at corners $\to$ tors").scale(0.9).shift(d_base + DOWN * 0.5 + RIGHT * 1.6)
        self.play(Write(b5_l4))
        self.wait(3)

        # --- Band 6 (subtopic_4): the four slope elements
        self.next_band(6)
        b6_title = Tex("The slope: crest, cliff, talus, pediment").scale(1.1).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        # Slope cross-section as a labelled polyline, drawn top-down.
        p0 = band_shift(6) + UP * 1.3 + LEFT * 5.6
        p1 = band_shift(6) + UP * 1.2 + LEFT * 4.6
        p2 = band_shift(6) + UP * 0.9 + LEFT * 4.0
        p3 = band_shift(6) + DOWN * 0.6 + LEFT * 3.6
        p4 = band_shift(6) + DOWN * 1.6 + LEFT * 1.4
        p5 = band_shift(6) + DOWN * 2.1 + RIGHT * 1.6
        p6 = band_shift(6) + DOWN * 2.3 + RIGHT * 5.4
        crest = VGroup(Line(p0, p1), Line(p1, p2))
        crest_lab = Tex("crest: convex").scale(0.8).shift(band_shift(6) + UP * 1.8 + LEFT * 3.9)
        self.play(Create(crest), Write(crest_lab))
        self.wait(1.8)
        cliff = Line(p2, p3, color=RED)
        cliff_lab = Tex("cliff / free face").scale(0.8).shift(band_shift(6) + UP * 0.2 + LEFT * 5.1)
        self.play(Create(cliff), Write(cliff_lab))
        self.wait(1.8)
        talus = Line(p3, p4, color=ORANGE)
        talus_lab = Tex(r"talus: straight,\\ angle of rest").scale(0.8).shift(band_shift(6) + DOWN * 0.5 + LEFT * 1.6)
        self.play(Create(talus), Write(talus_lab))
        self.wait(1.8)
        pediment = VGroup(Line(p4, p5), Line(p5, p6))
        ped_lab = Tex("pediment: concave run-out").scale(0.8).shift(band_shift(6) + DOWN * 1.4 + RIGHT * 3.0)
        self.play(Create(pediment), Write(ped_lab))
        self.wait(2)
        b6_l1 = Tex(r"Parallel retreat: cliff eats back, pediment").scale(0.9).shift(band_shift(6) + DOWN * 3.0 + LEFT * 1.4)
        b6_l2 = Tex(r"widens — mesa $\to$ butte $\to$ cone").scale(0.9).shift(band_shift(6) + DOWN * 3.6 + LEFT * 1.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l2))
        self.wait(3)

        # --- Band 7 (subtopic_4): mass movement and contour signatures
        self.next_band(7)
        b7_title = Tex("Mass movement and the map").scale(1.2).shift(band_shift(7) + UP * 2.2)
        self.play(Write(b7_title))
        self.wait(1.5)
        b7_l1 = Tex(r"Slow, dry: soil creep — leaning fence posts").scale(0.95).shift(band_shift(7) + UP * 1.3)
        b7_l2 = Tex(r"Wet flows: earthflow, racing mudflow").scale(0.95).shift(band_shift(7) + UP * 0.6)
        b7_l3 = Tex(r"Slides: landslide (plane), slump (curved,").scale(0.95).shift(band_shift(7) + DOWN * 0.1)
        b7_l4 = Tex(r"crescent scar); rockfall feeds the talus").scale(0.95).shift(band_shift(7) + DOWN * 0.8)
        self.play(Write(b7_l1))
        self.wait(1.8)
        self.play(Write(b7_l2))
        self.wait(1.8)
        self.play(Write(b7_l3))
        self.play(Write(b7_l4))
        self.wait(2)
        b7_l5 = Tex(r"Triggers: steepness, WATER, cut feet,").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        b7_l6 = Tex(r"stripped vegetation, shaking").scale(0.95).shift(band_shift(7) + DOWN * 2.3)
        self.play(Write(b7_l5))
        self.play(Write(b7_l6))
        self.wait(2)
        b7_l7 = Tex(r"Contours: mesa = crowded ring, empty top;").scale(0.9).shift(band_shift(7) + DOWN * 3.0)
        b7_l8 = Tex(r"cuesta = one-sided crowding; dome = smooth rings").scale(0.85).shift(band_shift(7) + DOWN * 3.6)
        self.play(Write(b7_l7))
        self.play(Write(b7_l8))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): conveyor belts and the merry-go-round
        self.next_band(8)
        b8_title = Tex("Conveyor belts and a merry-go-round").scale(1.15).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex(r"Braai loop: hot air rises at the equator,").scale(0.95).shift(band_shift(8) + UP * 1.3)
        b8_l2 = Tex(r"sinks dry at 30$^\circ$ — where deserts sit").scale(0.95).shift(band_shift(8) + UP * 0.6)
        self.play(Write(b8_l1))
        self.play(Write(b8_l2))
        self.wait(2.5)
        b8_l3 = Tex(r"One loop explains jungle AND desert").scale(1.0).shift(band_shift(8) + DOWN * 0.3)
        self.play(Write(b8_l3))
        self.play(Create(SurroundingRectangle(b8_l3, color=GREEN)))
        self.wait(2)
        b8_l4 = Tex(r"Merry-go-round: paths curve — LEFT in").scale(0.95).shift(band_shift(8) + DOWN * 1.2)
        b8_l5 = Tex(r"the south. SE trades, SW Cape storms").scale(0.95).shift(band_shift(8) + DOWN * 1.9)
        self.play(Write(b8_l4))
        self.play(Write(b8_l5))
        self.wait(2.5)
        b8_l6 = Tex(r"Summer: ITCZ soaks us. Winter: Kalahari").scale(0.95).shift(band_shift(8) + DOWN * 2.7)
        b8_l7 = Tex(r"lid on the Highveld, fronts reach the Cape").scale(0.95).shift(band_shift(8) + DOWN * 3.4)
        self.play(Write(b8_l6))
        self.play(Write(b8_l7))
        self.wait(3)

        # --- Band 9 (subtopic_6): cake, books, loaf
        self.next_band(9)
        b9_title = Tex("The cake, the books, the loaf").scale(1.2).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex(r"Rained-on layer cake: chocolate cap guards").scale(0.95).shift(band_shift(9) + UP * 1.3)
        b9_l2 = Tex(r"the sponge — wide table, small table,").scale(0.95).shift(band_shift(9) + UP * 0.6)
        b9_l3 = Tex(r"tall stump, cone: plateau, mesa, butte, hill").scale(0.95).shift(band_shift(9) + DOWN * 0.1)
        self.play(Write(b9_l1))
        self.play(Write(b9_l2))
        self.play(Write(b9_l3))
        self.play(Create(SurroundingRectangle(b9_l3, color=GREEN)))
        self.wait(3)
        b9_l4 = Tex(r"Leaning books: gentle tilt = cuesta;").scale(0.95).shift(band_shift(9) + DOWN * 1.0)
        b9_l5 = Tex(r"steeper = homoclinal; upright = hogsback").scale(0.95).shift(band_shift(9) + DOWN * 1.7)
        self.play(Write(b9_l4))
        self.play(Write(b9_l5))
        self.wait(2.5)
        b9_l6 = Tex(r"Fresh loaf: granite peels in curved crusts —").scale(0.95).shift(band_shift(9) + DOWN * 2.5)
        b9_l7 = Tex(r"exfoliation domes; sugar-cube corners $\to$ tors").scale(0.9).shift(band_shift(9) + DOWN * 3.2)
        self.play(Write(b9_l6))
        self.play(Write(b9_l7))
        self.wait(3)

        # --- Band 10 (subtopic_7): one walk down the hillside
        self.next_band(10)
        b10_title = Tex("One walk down the hillside").scale(1.2).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex(r"Crest (rounded) $\to$ cliff (bare rock) $\to$").scale(0.95).shift(band_shift(10) + UP * 1.3)
        b10_l2 = Tex(r"talus (angle of rest) $\to$ pediment (run-out)").scale(0.95).shift(band_shift(10) + UP * 0.6)
        self.play(Write(b10_l1))
        self.play(Write(b10_l2))
        self.play(Create(SurroundingRectangle(b10_l2, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex(r"Creep (fence posts) $\to$ flows (porridge soil)").scale(0.9).shift(band_shift(10) + DOWN * 0.3)
        b10_l4 = Tex(r"$\to$ slides and slumps $\to$ rockfall").scale(0.9).shift(band_shift(10) + DOWN * 1.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l4))
        self.wait(2.5)
        b10_l5 = Tex(r"The trigger is nearly always WATER or US").scale(1.0).shift(band_shift(10) + DOWN * 1.9)
        self.play(Write(b10_l5))
        self.play(Create(SurroundingRectangle(b10_l5, color=GREEN)))
        self.wait(2)
        b10_l6 = Tex(r"On the map: crowded rings at the cliff,").scale(0.95).shift(band_shift(10) + DOWN * 2.7)
        b10_l7 = Tex(r"widening down the pediment; gradient 1 in $n$").scale(0.9).shift(band_shift(10) + DOWN * 3.4)
        self.play(Write(b10_l6))
        self.play(Write(b10_l7))
        self.wait(4)
