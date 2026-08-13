from manim import *

# Band-layout whiteboard scene for the CAPS Grade 11 Geography session duo
# "Slope Elements and Slope Development". One band per teaching beat; the
# camera moves down, nothing is removed. Diagrams hand-built from
# Line/Arrow/Dot/Circle/Rectangle/Tex only (exporter-safe primitives).
# Subtopic shares follow subtopics.json: 220/230/235/240/185/190/210 of 1510 s.

BAND = config.frame_height


def band_shift(k):
    return DOWN * BAND * k


def strike(m):
    return Line(m.get_corner(DL) + 0.08 * DL, m.get_corner(UR) + 0.08 * UR,
                color=RED, stroke_width=6)


class SlopeElementsSession(MovingCameraScene):
    def next_band(self, k):
        self.play(self.camera.frame.animate.move_to(band_shift(k)), run_time=0.8)

    def construct(self):
        self.wait(14)

        # ============ Part 1 — Expert ============
        # --- Band 0 (subtopic_1): the three-part stage
        title = Tex("Slope Elements and Slope Development").scale(1.2).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
        s0_l1 = Tex(r"Interior plateau: $1\,200$--$1\,800$ m, flat").scale(1.05).shift(UP * 1.0)
        self.play(Write(s0_l1))
        self.wait(2)
        s0_l2 = Tex(r"Great Escarpment: the rim — Drakensberg").scale(1.05).shift(UP * 0.1)
        s0_l3 = Tex(r"climax above $3\,000$ m").scale(1.05).shift(DOWN * 0.7)
        self.play(Write(s0_l2))
        self.play(Write(s0_l3))
        self.wait(2.5)
        s0_l4 = Tex("Marginal zone: Cape folds, terraces,").scale(1.05).shift(DOWN * 1.6)
        s0_l5 = Tex("east-coast lowlands").scale(1.05).shift(DOWN * 2.4)
        self.play(Write(s0_l4))
        self.play(Write(s0_l5))
        self.wait(3)

        # --- Band 1 (subtopic_1): the staircase + slope shapes
        self.next_band(1)
        b1_title = Tex("Three steps, four slope shapes").scale(1.15).shift(band_shift(1) + UP * 2.6)
        self.play(Write(b1_title))
        self.wait(1.5)
        # staircase cross-section: plateau, escarpment drop, coastal belt, sea
        stair = VGroup(
            Line(LEFT * 6.0 + UP * 1.2, LEFT * 2.0 + UP * 1.2, color=WHITE),
            Line(LEFT * 2.0 + UP * 1.2, LEFT * 0.8 + DOWN * 0.8, color=RED),
            Line(LEFT * 0.8 + DOWN * 0.8, RIGHT * 3.6 + DOWN * 1.4, color=WHITE),
            Line(RIGHT * 3.6 + DOWN * 1.4, RIGHT * 6.0 + DOWN * 1.6, color=BLUE),
        ).shift(band_shift(1))
        self.play(Create(stair[0]))
        p_lab = Tex("plateau").scale(0.8).shift(band_shift(1) + LEFT * 4.4 + UP * 1.8)
        self.play(Write(p_lab))
        self.play(Create(stair[1]))
        e_lab = Tex("escarpment").scale(0.8).shift(band_shift(1) + LEFT * 2.6 + UP * 0.1)
        self.play(Write(e_lab))
        self.play(Create(stair[2]), Create(stair[3]))
        m_lab = Tex("marginal zone").scale(0.8).shift(band_shift(1) + RIGHT * 1.6 + DOWN * 0.6)
        sea_lab = Tex("sea").scale(0.8).shift(band_shift(1) + RIGHT * 5.4 + DOWN * 1.0)
        self.play(Write(m_lab), Write(sea_lab))
        self.wait(2)
        b1_l1 = Tex("Tugela leaps $\\approx 950$ m off the rim").scale(0.95).shift(band_shift(1) + DOWN * 2.2)
        self.play(Write(b1_l1))
        self.wait(2)
        b1_l2 = Tex("Shapes: convex, concave, rectilinear,").scale(0.95).shift(band_shift(1) + DOWN * 3.0 + LEFT * 1.2)
        b1_l2b = Tex("compound").scale(0.95).shift(band_shift(1) + DOWN * 3.0 + RIGHT * 4.4)
        self.play(Write(b1_l2), Write(b1_l2b))
        self.wait(3)

        # --- Band 2 (subtopic_2): the four elements drawn
        self.next_band(2)
        b2_title = Tex("The four slope elements").scale(1.15).shift(band_shift(2) + UP * 2.6)
        self.play(Write(b2_title))
        self.wait(1.5)
        # profile: crest (convex 2-chain), cliff (steep), talus (straight), pediment (gentle concave 2-chain)
        crest = VGroup(
            Line(LEFT * 6.0 + UP * 1.5, LEFT * 4.6 + UP * 1.3, color=YELLOW),
            Line(LEFT * 4.6 + UP * 1.3, LEFT * 3.8 + UP * 0.8, color=YELLOW),
        ).shift(band_shift(2))
        cliff = Line(LEFT * 3.8 + UP * 0.8, LEFT * 3.4 + DOWN * 0.8, color=RED).shift(band_shift(2))
        talus = Line(LEFT * 3.4 + DOWN * 0.8, LEFT * 0.6 + DOWN * 1.8, color=BLUE).shift(band_shift(2))
        ped = VGroup(
            Line(LEFT * 0.6 + DOWN * 1.8, RIGHT * 2.6 + DOWN * 2.2, color=GREEN),
            Line(RIGHT * 2.6 + DOWN * 2.2, RIGHT * 6.0 + DOWN * 2.3, color=GREEN),
        ).shift(band_shift(2))
        self.play(Create(crest[0]), Create(crest[1]))
        c_lab = Tex("CREST: convex").scale(0.85).shift(band_shift(2) + LEFT * 4.8 + UP * 2.0)
        self.play(Write(c_lab))
        self.wait(1.5)
        self.play(Create(cliff))
        cl_lab = Tex("CLIFF: free face").scale(0.85).shift(band_shift(2) + LEFT * 1.6 + UP * 0.6)
        self.play(Write(cl_lab))
        self.wait(1.5)
        self.play(Create(talus))
        t_lab = Tex("TALUS: straight").scale(0.85).shift(band_shift(2) + LEFT * 1.4 + DOWN * 0.7)
        self.play(Write(t_lab))
        self.wait(1.5)
        self.play(Create(ped[0]), Create(ped[1]))
        pd_lab = Tex("PEDIMENT: concave").scale(0.85).shift(band_shift(2) + RIGHT * 3.6 + DOWN * 1.5)
        self.play(Write(pd_lab))
        self.wait(2)
        b2_l1 = Tex("Fixed order, summit to plain").scale(0.95).shift(band_shift(2) + DOWN * 3.0)
        self.play(Write(b2_l1))
        self.wait(3)

        # --- Band 3 (subtopic_2): each element's numbers
        self.next_band(3)
        b3_title = Tex("Each element's character").scale(1.15).shift(band_shift(3) + UP * 2.2)
        self.play(Write(b3_title))
        self.wait(1.5)
        b3_l1 = Tex("Cliff: bare bedrock; freed rock falls").scale(0.95).shift(band_shift(3) + UP * 1.2)
        b3_l1b = Tex("at once — the debris supplier").scale(0.95).shift(band_shift(3) + UP * 0.4)
        self.play(Write(b3_l1))
        self.play(Write(b3_l1b))
        self.wait(2.5)
        b3_l2 = Tex(r"Talus: angle of repose $25^\circ$--$35^\circ$;").scale(0.95).shift(band_shift(3) + DOWN * 0.5)
        b3_l2b = Tex("coarse high, fine low — transport slope").scale(0.95).shift(band_shift(3) + DOWN * 1.3)
        self.play(Write(b3_l2))
        self.play(Write(b3_l2b))
        self.wait(2.5)
        b3_l3 = Tex(r"Pediment: $<5^\circ$, rock floor, sheetwash").scale(0.95).shift(band_shift(3) + DOWN * 2.2)
        self.play(Write(b3_l3))
        self.wait(2)
        b3_l4 = Tex("Convex, vertical, straight, concave").scale(1.0).shift(band_shift(3) + DOWN * 3.0)
        self.play(Write(b3_l4))
        self.play(Create(SurroundingRectangle(b3_l4, color=GREEN)))
        self.wait(3)

        # --- Band 4 (subtopic_3): slope retreat — the machine
        self.next_band(4)
        b4_title = Tex("Slope retreat: the profile relocates").scale(1.1).shift(band_shift(4) + UP * 2.6)
        self.play(Write(b4_title))
        self.wait(1.5)
        base4 = Line(LEFT * 6.0 + DOWN * 1.8, RIGHT * 6.0 + DOWN * 1.8, color=WHITE).shift(band_shift(4))
        self.play(Create(base4))
        # two profile positions, same shape
        prof1 = VGroup(
            Line(LEFT * 4.8 + UP * 1.0, LEFT * 4.4 + DOWN * 0.4, color=BLUE),
            Line(LEFT * 4.4 + DOWN * 0.4, LEFT * 2.6 + DOWN * 1.8, color=BLUE),
        ).shift(band_shift(4))
        prof2 = VGroup(
            Line(LEFT * 1.8 + UP * 1.0, LEFT * 1.4 + DOWN * 0.4, color=RED),
            Line(LEFT * 1.4 + DOWN * 0.4, RIGHT * 0.4 + DOWN * 1.8, color=RED),
        ).shift(band_shift(4))
        self.play(Create(prof1[0]), Create(prof1[1]))
        self.play(Create(prof2[0]), Create(prof2[1]))
        ret = Arrow(LEFT * 0.6 + UP * 1.4, LEFT * 3.8 + UP * 1.4, color=RED, buff=0).shift(band_shift(4))
        ret_lab = Tex("same proportions, further back").scale(0.85).shift(band_shift(4) + RIGHT * 3.4 + UP * 1.4)
        self.play(Create(ret), Write(ret_lab))
        self.wait(2.5)
        b4_l1 = Tex("Cliff sheds and retreats; talus follows;").scale(0.95).shift(band_shift(4) + DOWN * 2.5)
        b4_l2 = Tex("pediment widens — King's parallel retreat").scale(0.95).shift(band_shift(4) + DOWN * 3.2 + RIGHT * 0.2)
        self.play(Write(b4_l1))
        self.play(Write(b4_l2))
        self.wait(3)

        # --- Band 5 (subtopic_3): retreat vs decline; people
        self.next_band(5)
        b5_title = Tex("Retreat or decline — and why here").scale(1.1).shift(band_shift(5) + UP * 2.2)
        self.play(Write(b5_title))
        self.wait(1.5)
        b5_l1 = Tex("Opposing slopes retreat: pediments merge").scale(0.95).shift(band_shift(5) + UP * 1.2)
        b5_l2 = Tex("into a PEDIPLAIN; survivors stand as").scale(0.95).shift(band_shift(5) + UP * 0.4)
        b5_l2b = Tex("koppies and inselbergs").scale(0.95).shift(band_shift(5) + DOWN * 0.4)
        self.play(Write(b5_l1))
        self.play(Write(b5_l2))
        self.play(Write(b5_l2b))
        self.wait(2.5)
        b5_l3 = Tex("Humid, deep-soil regions: slopes DECLINE").scale(0.95).shift(band_shift(5) + DOWN * 1.3)
        b5_l4 = Tex("Semi-arid SA, hard caps: parallel retreat").scale(0.95).shift(band_shift(5) + DOWN * 2.1)
        self.play(Write(b5_l3))
        self.wait(2)
        self.play(Write(b5_l4))
        self.play(Create(SurroundingRectangle(b5_l4, color=GREEN)))
        self.wait(2)
        b5_l5 = Tex("People: build on crest and pediment,").scale(0.9).shift(band_shift(5) + DOWN * 2.9)
        self.play(Write(b5_l5))
        self.wait(3)

        # --- Band 6 (subtopic_4): resolution, two kinds
        self.next_band(6)
        b6_title = Tex("GIS toolkit: resolution").scale(1.15).shift(band_shift(6) + UP * 2.2)
        self.play(Write(b6_title))
        self.wait(1.5)
        b6_l1 = Tex("SPATIAL: ground size of one pixel —").scale(1.0).shift(band_shift(6) + UP * 1.2)
        b6_l1b = Tex("10 m sees fields and roads, not cars").scale(1.0).shift(band_shift(6) + UP * 0.4)
        self.play(Write(b6_l1))
        self.play(Write(b6_l1b))
        self.wait(2.5)
        b6_l2 = Tex("SPECTRAL: number and narrowness of").scale(1.0).shift(band_shift(6) + DOWN * 0.5)
        b6_l2b = Tex("wavelength bands the sensor records").scale(1.0).shift(band_shift(6) + DOWN * 1.3)
        self.play(Write(b6_l2))
        self.play(Write(b6_l2b))
        self.wait(2.5)
        b6_l3 = Tex("More bands: veld, stressed crops, soil").scale(0.95).shift(band_shift(6) + DOWN * 2.2)
        b6_l3b = Tex("and water told apart by reflectance").scale(0.95).shift(band_shift(6) + DOWN * 3.0)
        self.play(Write(b6_l3))
        self.play(Write(b6_l3b))
        self.wait(3)

        # --- Band 7 (subtopic_4): vector and raster
        self.next_band(7)
        b7_title = Tex("Vector and raster").scale(1.15).shift(band_shift(7) + UP * 2.6)
        self.play(Write(b7_title))
        self.wait(1.5)
        # vector: point, line, area
        v_pt = Dot(LEFT * 4.6 + UP * 1.4).shift(band_shift(7))
        v_ln = Line(LEFT * 5.4 + UP * 0.4, LEFT * 3.4 + UP * 0.8, color=BLUE).shift(band_shift(7))
        v_ar = Rectangle(width=1.6, height=1.0, color=GREEN).shift(band_shift(7) + LEFT * 4.4 + DOWN * 0.8)
        v_lab = Tex("vector: point, line, area").scale(0.85).shift(band_shift(7) + LEFT * 4.2 + DOWN * 1.9)
        self.play(Create(v_pt), Create(v_ln), Create(v_ar))
        self.play(Write(v_lab))
        self.wait(2)
        # raster: grid of cells
        cells = VGroup(
            Rectangle(width=0.8, height=0.8, color=GREY).shift(RIGHT * 2.6 + UP * 1.0),
            Rectangle(width=0.8, height=0.8, color=GREY).shift(RIGHT * 3.4 + UP * 1.0),
            Rectangle(width=0.8, height=0.8, color=GREY).shift(RIGHT * 2.6 + UP * 0.2),
            Rectangle(width=0.8, height=0.8, color=GREY).shift(RIGHT * 3.4 + UP * 0.2),
        ).shift(band_shift(7))
        r_lab = Tex("raster: grid, one value per cell").scale(0.85).shift(band_shift(7) + RIGHT * 3.2 + DOWN * 0.7)
        self.play(Create(cells[0]), Create(cells[1]), Create(cells[2]), Create(cells[3]))
        self.play(Write(r_lab))
        self.wait(2)
        b7_l1 = Tex("Attributes: the table of facts attached").scale(0.95).shift(band_shift(7) + DOWN * 1.6)
        self.play(Write(b7_l1))
        self.wait(2)
        b7_l2 = Tex("DEM (raster) $\\rightarrow$ slope map in seconds").scale(0.95).shift(band_shift(7) + DOWN * 2.4)
        self.play(Write(b7_l2))
        self.play(Create(SurroundingRectangle(b7_l2, color=GREEN)))
        self.wait(3)

        # ============ Part 2 — Simplifier ============
        # --- Band 8 (subtopic_5): the book on the table
        self.next_band(8)
        b8_title = Tex("The country is a three-step staircase").scale(1.1).shift(band_shift(8) + UP * 2.2)
        self.play(Write(b8_title))
        self.wait(2)
        b8_l1 = Tex("Thick book flat on the table: plateau,").scale(1.0).shift(band_shift(8) + UP * 1.2)
        b8_l1b = Tex(r"Johannesburg on top at $1\,700$ m").scale(1.0).shift(band_shift(8) + UP * 0.4)
        self.play(Write(b8_l1))
        self.play(Write(b8_l1b))
        self.wait(2.5)
        b8_l2 = Tex("Book edges: the Escarpment — sharpest").scale(1.0).shift(band_shift(8) + DOWN * 0.5)
        b8_l2b = Tex("drop is the Drakensberg; Tugela jumps it").scale(1.0).shift(band_shift(8) + DOWN * 1.3)
        self.play(Write(b8_l2))
        self.play(Write(b8_l2b))
        self.wait(2.5)
        b8_l3 = Tex("Shapes by feel: shoulder (convex), spoon").scale(0.95).shift(band_shift(8) + DOWN * 2.2)
        b8_l3b = Tex("(concave), plank (straight), stacked hills").scale(0.95).shift(band_shift(8) + DOWN * 3.0)
        self.play(Write(b8_l3))
        self.play(Write(b8_l3b))
        self.wait(3)

        # --- Band 9 (subtopic_6): crest, cliff, chute, apron
        self.next_band(9)
        b9_title = Tex("Crest, cliff, chute and apron").scale(1.15).shift(band_shift(9) + UP * 2.2)
        self.play(Write(b9_title))
        self.wait(2)
        b9_l1 = Tex("Crest: the hill's rounded scalp").scale(1.0).shift(band_shift(9) + UP * 1.2)
        b9_l2 = Tex("Cliff: the factory — drops fresh rock").scale(1.0).shift(band_shift(9) + UP * 0.4)
        b9_l3 = Tex(r"Talus: rubble chute at $25^\circ$--$35^\circ$,").scale(1.0).shift(band_shift(9) + DOWN * 0.4)
        b9_l3b = Tex("the builder's-sand resting angle").scale(1.0).shift(band_shift(9) + DOWN * 1.2)
        b9_l4 = Tex("Pediment: the apron out to the plain").scale(1.0).shift(band_shift(9) + DOWN * 2.0)
        self.play(Write(b9_l1))
        self.wait(2)
        self.play(Write(b9_l2))
        self.wait(2)
        self.play(Write(b9_l3))
        self.play(Write(b9_l3b))
        self.wait(2)
        self.play(Write(b9_l4))
        self.wait(2)
        b9_l5 = Tex("No hard band: no cliff, no chute").scale(0.95).shift(band_shift(9) + DOWN * 2.9)
        self.play(Write(b9_l5))
        self.play(Create(SurroundingRectangle(b9_l5, color=GREEN)))
        self.wait(3)

        # --- Band 10 (subtopic_7): the walking hill and the Lego map
        self.next_band(10)
        b10_title = Tex("The hill that walks; the map of Lego").scale(1.1).shift(band_shift(10) + UP * 2.2)
        self.play(Write(b10_title))
        self.wait(2)
        b10_l1 = Tex("Cliff drops rock and steps back; chute").scale(0.95).shift(band_shift(10) + UP * 1.2)
        b10_l1b = Tex("follows; apron extends — shape held").scale(0.95).shift(band_shift(10) + UP * 0.4)
        self.play(Write(b10_l1))
        self.play(Write(b10_l1b))
        self.wait(2.5)
        b10_l2 = Tex("Fifty million years: aprons merge into").scale(0.95).shift(band_shift(10) + DOWN * 0.5)
        b10_l2b = Tex("the pediplain; koppies still walking").scale(0.95).shift(band_shift(10) + DOWN * 1.3)
        self.play(Write(b10_l2))
        self.play(Write(b10_l2b))
        self.play(Create(SurroundingRectangle(b10_l2b, color=GREEN)))
        self.wait(2.5)
        b10_l3 = Tex("Vector $=$ Lego objects with fact tables;").scale(0.95).shift(band_shift(10) + DOWN * 2.2)
        b10_l3b = Tex("raster $=$ graph paper, one value per square").scale(0.95).shift(band_shift(10) + DOWN * 3.0)
        self.play(Write(b10_l3))
        self.play(Write(b10_l3b))
        self.play(Create(SurroundingRectangle(b10_l3b, color=GREEN)))
        self.wait(4)
