# Session Assistants (Mandy & Bianca)

Host / timekeeper / support-assistant content for the live session chrome —
the identity framing that is NOT part of a lesson script (tutors own their
greetings/signoffs under `lessons/tutors/<slug>/`; the lesson script is pure
teaching content).

**Bianca is not a distinct personality** (supacharge-characters.md §3): she is
a second rendered identity for the exact same role Mandy fills, so no single
host is ever live in two concurrent sessions at once. Each live session is
assigned ONE host from the pool (Mandy or Bianca). The two directories hold
functional equivalents — same script formulas, second name.

## Categories
- `intro/` — session opening (`new`, `returning` student variants)
- `handover/` — the break bridge (`into_break`, `out_of_break` toward the
  second tutor)
- `signoff/` — session end + office hours (`session_end`,
  `office_hours_open`, `office_hours_close`)
- `timekeeping/` — time-check callouts (`halfway`, `five_min_warning`,
  `wrap_up`)

## Placeholder tokens
Filled with the session's actual tutors by the pipeline (the §3 scripts
likewise name "Grandmaster"):
- `{first_tutor}` — the tutor leading part one
- `{second_tutor}` — the tutor taking over after the break
