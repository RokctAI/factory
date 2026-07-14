<!-- CARD RULES
     This card is the source of truth for this job.
     Status field controls pipeline progression.
     All status changes must go through update_status.py.
     Direct edits to status field will be rejected by the state machine.

     LESSON CARDS (type: lesson.<subject>)
     Input fields mirror the Prompt Template in
     agent/replay/docs/supacharge-tech.md §4 "Content Production Pipeline":
     Subject, Grade, Topic, Subtopic, Example problem, Tutor, Prior knowledge.
     theme is kept for mechanism compatibility (ledger/dedup) and holds the
     human-readable "Subject Grade N: Topic — Subtopic" string.
     Content path fields are filled by Level 2 (Jules) when the seven §4
     content items land under lessons/drafts/<id>/.
     The pipeline for lessons stops at status: evaluated (Level 4 approved).
     Level 6 production (Manim/VibeVoice) is a separate future brief.
-->
---
id:
theme:
type:
subject:
grade:
term:
topic:
subtopic:
tutor:
example_problem:
prior_knowledge:
metarules:
guardrail:
idea:
idea_status:
concept:
concept_status:
rules_status:
lesson_name:
lesson_path:
script_path:
manim_path:
subtopics_path:
mcq_data_path:
comprehension_check_path:
reel_brief_path:
mandy_transcript_path:
mandy_nervous_script_path:
status:
created:
last_updated:
session_id:
session_started:
attempts: 0
last_error:
expansion_requested:
crosscheck_status:
crosscheck_notes:
loop_iterations: 0
max_iterations: 10
---
