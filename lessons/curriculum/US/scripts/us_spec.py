"""Structural spec for the US curriculum tree.

Single source of truth for what the four US subtrees contain, imported by
build_us_tree.py (which writes the generated layers) and audit_tree.py (which
validates both the generated and the hand-owned halves).

Why four subtrees and not one "US curriculum": the frameworks are genuinely
different KINDS of thing.

  COMMON_CORE / NGSS  are content standards - published statements of what a
                      student should know by a grade. They have no examining
                      body, set no papers and award no certificate, so
                      `past_papers/` is deliberately absent rather than empty.
  AP / SAT            are examination programmes run by a commercial exam
                      board (College Board), closer to Cambridge/IEB than to
                      a standards document. They DO have past papers, and
                      those papers are rights-gated.

The grade axis differs per framework and is taken from the framework itself
rather than forced into CAPS's grade10-12 shape:

  COMMON_CORE math   K-8 by grade, then one high-school file - CCSS high
                     school maths is organised by conceptual category, not by
                     grade, and inventing grade9/10/11/12 splits would
                     fabricate a distinction the standards do not make.
  COMMON_CORE ela    K-8 by grade, then the two grade BANDS the standards
                     themselves use (9-10, 11-12).
  NGSS               K-5 by grade, then the MS (6-8) and HS (9-12) bands the
                     standards themselves use.
  SAT                the three grade bands the SAT Suite is built around
                     (PSAT 8/9, PSAT 10 + PSAT/NMSQT, SAT).
  AP                 no grade axis at all. An AP course is a course; the
                     College Board prescribes no grade for it. So the
                     syllabus layer is partitioned by course, one file, and
                     the deviation is recorded in the subtree README - the
                     same reasoning that omits past_papers from the standards
                     frameworks.
"""

FRAMEWORKS = ["COMMON_CORE", "NGSS", "AP", "SAT"]

# --------------------------------------------------------------------------
# Common Core
# --------------------------------------------------------------------------

# Domain codes per grade. CCSS domains vary by grade by design (a spiral that
# opens and closes domains), which is why this is a per-grade table and not one
# list. Verified against the published domain progressions; the standards
# themselves are transcribed only after a real fetch.
CCSS_MATH_DOMAINS = {
    "K": [("CC", "Counting and Cardinality"),
          ("OA", "Operations and Algebraic Thinking"),
          ("NBT", "Number and Operations in Base Ten"),
          ("MD", "Measurement and Data"),
          ("G", "Geometry")],
    "1": [("OA", "Operations and Algebraic Thinking"),
          ("NBT", "Number and Operations in Base Ten"),
          ("MD", "Measurement and Data"),
          ("G", "Geometry")],
    "2": [("OA", "Operations and Algebraic Thinking"),
          ("NBT", "Number and Operations in Base Ten"),
          ("MD", "Measurement and Data"),
          ("G", "Geometry")],
    "3": [("OA", "Operations and Algebraic Thinking"),
          ("NBT", "Number and Operations in Base Ten"),
          ("NF", "Number and Operations - Fractions"),
          ("MD", "Measurement and Data"),
          ("G", "Geometry")],
    "4": [("OA", "Operations and Algebraic Thinking"),
          ("NBT", "Number and Operations in Base Ten"),
          ("NF", "Number and Operations - Fractions"),
          ("MD", "Measurement and Data"),
          ("G", "Geometry")],
    "5": [("OA", "Operations and Algebraic Thinking"),
          ("NBT", "Number and Operations in Base Ten"),
          ("NF", "Number and Operations - Fractions"),
          ("MD", "Measurement and Data"),
          ("G", "Geometry")],
    "6": [("RP", "Ratios and Proportional Relationships"),
          ("NS", "The Number System"),
          ("EE", "Expressions and Equations"),
          ("G", "Geometry"),
          ("SP", "Statistics and Probability")],
    "7": [("RP", "Ratios and Proportional Relationships"),
          ("NS", "The Number System"),
          ("EE", "Expressions and Equations"),
          ("G", "Geometry"),
          ("SP", "Statistics and Probability")],
    "8": [("NS", "The Number System"),
          ("EE", "Expressions and Equations"),
          ("F", "Functions"),
          ("G", "Geometry"),
          ("SP", "Statistics and Probability")],
    "9-12": [("N", "Number and Quantity"),
             ("A", "Algebra"),
             ("F", "Functions"),
             ("G", "Geometry"),
             ("S", "Statistics and Probability"),
             ("M", "Modelling (a Modeling category marked by a star on standards in other categories, with no standards of its own)")],
}

CCSS_MATH_GRADES = ["K", "1", "2", "3", "4", "5", "6", "7", "8", "9-12"]
CCSS_ELA_GRADES = ["K", "1", "2", "3", "4", "5", "6", "7", "8", "9-10", "11-12"]

# ELA strands. RF (Reading: Foundational Skills) is K-5 only; the
# history/social-studies and science/technical literacy strands are 6-12 only.
CCSS_ELA_STRANDS_K5 = [
    ("RL", "Reading: Literature"),
    ("RI", "Reading: Informational Text"),
    ("RF", "Reading: Foundational Skills"),
    ("W", "Writing"),
    ("SL", "Speaking and Listening"),
    ("L", "Language"),
]
CCSS_ELA_STRANDS_612 = [
    ("RL", "Reading: Literature"),
    ("RI", "Reading: Informational Text"),
    ("W", "Writing"),
    ("SL", "Speaking and Listening"),
    ("L", "Language"),
    ("RH", "Reading in History/Social Studies (literacy strand)"),
    ("RST", "Reading in Science and Technical Subjects (literacy strand)"),
    ("WHST", "Writing in History/Social Studies, Science and Technical Subjects (literacy strand)"),
]

# The eight Standards for Mathematical Practice. These are stated identically
# at every grade K-12, which is exactly why they are modelled as cross-grade
# skills rather than duplicated into each grade's skills folder.
CCSS_MATH_PRACTICES = [
    ("MP1", "Make sense of problems and persevere in solving them"),
    ("MP2", "Reason abstractly and quantitatively"),
    ("MP3", "Construct viable arguments and critique the reasoning of others"),
    ("MP4", "Model with mathematics"),
    ("MP5", "Use appropriate tools strategically"),
    ("MP6", "Attend to precision"),
    ("MP7", "Look for and make use of structure"),
    ("MP8", "Look for and express regularity in repeated reasoning"),
]

# College and Career Readiness anchor standards - the cross-grade backbone the
# grade-specific ELA standards are derived from.
CCSS_ELA_ANCHORS = [
    ("reading", "College and Career Readiness Anchor Standards for Reading", 10),
    ("writing", "College and Career Readiness Anchor Standards for Writing", 10),
    ("speaking_listening", "College and Career Readiness Anchor Standards for Speaking and Listening", 6),
    ("language", "College and Career Readiness Anchor Standards for Language", 6),
]

# --------------------------------------------------------------------------
# NGSS
# --------------------------------------------------------------------------

NGSS_GRADES = ["K", "1", "2", "3", "4", "5", "6-8", "9-12"]

NGSS_DCI_DOMAINS = [
    ("PS", "Physical Science"),
    ("LS", "Life Science"),
    ("ESS", "Earth and Space Science"),
    ("ETS", "Engineering, Technology, and Applications of Science"),
]

NGSS_PRACTICES = [
    ("SEP1", "Asking questions (for science) and defining problems (for engineering)"),
    ("SEP2", "Developing and using models"),
    ("SEP3", "Planning and carrying out investigations"),
    ("SEP4", "Analyzing and interpreting data"),
    ("SEP5", "Using mathematics and computational thinking"),
    ("SEP6", "Constructing explanations (for science) and designing solutions (for engineering)"),
    ("SEP7", "Engaging in argument from evidence"),
    ("SEP8", "Obtaining, evaluating, and communicating information"),
]

NGSS_CROSSCUTTING = [
    ("CCC1", "Patterns"),
    ("CCC2", "Cause and effect: Mechanism and explanation"),
    ("CCC3", "Scale, proportion, and quantity"),
    ("CCC4", "Systems and system models"),
    ("CCC5", "Energy and matter: Flows, cycles, and conservation"),
    ("CCC6", "Structure and function"),
    ("CCC7", "Stability and change"),
]

# --------------------------------------------------------------------------
# SAT Suite
# --------------------------------------------------------------------------

# Content domains published by College Board for the digital SAT Suite. These
# are the names of the domains (facts about the test's reporting structure),
# not test content.
SAT_SECTIONS = {
    "reading_writing": {
        "title": "Reading and Writing",
        "domains": [
            "Information and Ideas",
            "Craft and Structure",
            "Expression of Ideas",
            "Standard English Conventions",
        ],
    },
    "math": {
        "title": "Math",
        "domains": [
            "Algebra",
            "Advanced Math",
            "Problem-Solving and Data Analysis",
            "Geometry and Trigonometry",
        ],
    },
}

# The SAT Suite's own grade axis.
SAT_GRADE_BANDS = [
    ("8-9", "PSAT 8/9"),
    ("10", "PSAT 10 and PSAT/NMSQT (PSAT/NMSQT is also taken in grade 11)"),
    ("11-12", "SAT"),
]

# Published digital-SAT format. Recorded as reported fact with its corroboration
# status, never as reproduced content.
SAT_FORMAT = {
    "delivery": "digital, section-adaptive",
    "sections": 2,
    "adaptive_design": "Each section is split into two separately timed modules; performance on module 1 determines the difficulty mix of module 2.",
    "reading_writing": {"questions": 54, "minutes": 64, "modules": 2,
                        "per_module": {"questions": 27, "minutes": 32}},
    "math": {"questions": 44, "minutes": 70, "modules": 2,
             "per_module": {"questions": 22, "minutes": 35},
             "calculator": "permitted throughout"},
    "totals": {"questions": 98, "minutes": 134},
    "confidence": "corroborated across multiple secondary sources in August 2026; NOT yet confirmed against College Board's own published specification, which this environment could not reach. Verify at satsuite.collegeboard.org before any student-facing use.",
}

# --------------------------------------------------------------------------
# AP
# --------------------------------------------------------------------------

# Courses scaffolded now: chosen to line up with the subject spine this
# repository already teaches (maths, physical sciences, economics, geography)
# plus the ELA pair that matches Common Core ELA. Everything else in the
# official course list is registered in AP/courses.json as not_yet_scaffolded -
# adding one is a spec edit plus a regenerate, not new code.
AP_SCAFFOLDED_COURSES = [
    ("ap_precalculus", "AP Precalculus", "Math and Computer Science"),
    ("ap_calculus_ab", "AP Calculus AB", "Math and Computer Science"),
    ("ap_calculus_bc", "AP Calculus BC", "Math and Computer Science"),
    ("ap_statistics", "AP Statistics", "Math and Computer Science"),
    ("ap_physics_1", "AP Physics 1: Algebra-Based", "Sciences"),
    ("ap_physics_2", "AP Physics 2: Algebra-Based", "Sciences"),
    ("ap_physics_c_mechanics", "AP Physics C: Mechanics", "Sciences"),
    ("ap_physics_c_electricity_and_magnetism", "AP Physics C: Electricity and Magnetism", "Sciences"),
    ("ap_chemistry", "AP Chemistry", "Sciences"),
    ("ap_biology", "AP Biology", "Sciences"),
    ("ap_environmental_science", "AP Environmental Science", "Sciences"),
    ("ap_macroeconomics", "AP Macroeconomics", "History and Social Sciences"),
    ("ap_microeconomics", "AP Microeconomics", "History and Social Sciences"),
    ("ap_human_geography", "AP Human Geography", "History and Social Sciences"),
    ("ap_english_language_and_composition", "AP English Language and Composition", "English"),
    ("ap_english_literature_and_composition", "AP English Literature and Composition", "English"),
]

# The wider official course list, for the registry. Names only - a name is a
# fact, and naming a course is not reproducing College Board content.
AP_OTHER_COURSES = [
    ("ap_art_history", "AP Art History", "Arts"),
    ("ap_music_theory", "AP Music Theory", "Arts"),
    ("ap_2d_art_and_design", "AP 2-D Art and Design", "Arts"),
    ("ap_3d_art_and_design", "AP 3-D Art and Design", "Arts"),
    ("ap_drawing", "AP Drawing", "Arts"),
    ("ap_computer_science_a", "AP Computer Science A", "Math and Computer Science"),
    ("ap_computer_science_principles", "AP Computer Science Principles", "Math and Computer Science"),
    ("ap_psychology", "AP Psychology", "History and Social Sciences"),
    ("ap_united_states_history", "AP United States History", "History and Social Sciences"),
    ("ap_world_history_modern", "AP World History: Modern", "History and Social Sciences"),
    ("ap_european_history", "AP European History", "History and Social Sciences"),
    ("ap_united_states_government_and_politics", "AP United States Government and Politics", "History and Social Sciences"),
    ("ap_comparative_government_and_politics", "AP Comparative Government and Politics", "History and Social Sciences"),
    ("ap_african_american_studies", "AP African American Studies", "History and Social Sciences"),
    ("ap_chinese_language_and_culture", "AP Chinese Language and Culture", "World Languages and Cultures"),
    ("ap_french_language_and_culture", "AP French Language and Culture", "World Languages and Cultures"),
    ("ap_german_language_and_culture", "AP German Language and Culture", "World Languages and Cultures"),
    ("ap_italian_language_and_culture", "AP Italian Language and Culture", "World Languages and Cultures"),
    ("ap_japanese_language_and_culture", "AP Japanese Language and Culture", "World Languages and Cultures"),
    ("ap_latin", "AP Latin", "World Languages and Cultures"),
    ("ap_spanish_language_and_culture", "AP Spanish Language and Culture", "World Languages and Cultures"),
    ("ap_spanish_literature_and_culture", "AP Spanish Literature and Culture", "World Languages and Cultures"),
    ("ap_seminar", "AP Seminar", "AP Capstone Diploma Program"),
    ("ap_research", "AP Research", "AP Capstone Diploma Program"),
]


def subtree_layout():
    """Return {framework: {subject: {"grades": [...], "past_papers": bool}}}."""
    return {
        "COMMON_CORE": {
            "math": {"grades": CCSS_MATH_GRADES, "past_papers": False},
            "ela": {"grades": CCSS_ELA_GRADES, "past_papers": False},
        },
        "NGSS": {
            "science": {"grades": NGSS_GRADES, "past_papers": False},
        },
        "AP": {
            slug: {"grades": ["course"], "past_papers": True}
            for slug, _title, _cat in AP_SCAFFOLDED_COURSES
        },
        "SAT": {
            "reading_writing": {"grades": [g for g, _ in SAT_GRADE_BANDS], "past_papers": True},
            "math": {"grades": [g for g, _ in SAT_GRADE_BANDS], "past_papers": True},
        },
    }


def grade_filename(grade):
    """'K' -> 'gradeK.json', '9-12' -> 'grade9-12.json', 'course' -> 'course.json'."""
    if grade == "course":
        return "course.json"
    return "grade{}.json".format(grade)
