# Onboarding slide imagery

One JSON per onboarding slide, per branch. Hand the `prompt` field to an image
model; `negative_prompt` and `framing` apply to every slide in the folder.

    students/   the learner is setting up their own account
    partner/    a parent or guardian is setting it up for a learner

## Where the slides come from

The shipped flow, not invented:
`Users/onboarding/dart/lib/src/common/presentation/pages/intro/intro_page.dart`
- welcome carousel: "Live classes, every day", "Know where you stand",
  "Your library stays yours"
- role choice: "Who is setting this up?"
- grade capture: student branch only (a host-supplied slide)
- done: "You're all set!"

`headline_in_app` and `caption_in_app` are the copy that sits ON the image.
That is why every prompt leaves the top third quiet and forbids text in the
image itself.

## Two branches, same three promises

A learner is being told what their week will look like; a parent is being told
what they will be able to see and what they are paying for. Same platform,
different reader - so the same headline gets a different photograph.

## Rules every prompt follows

Carried over from the tutor appearance work, because the same model makes the
same mistakes:

- **No text, numbers, UI or logos in the image.** Models cannot write, and the
  slide's own copy sits on top. Every phone screen in these prompts is angled
  away or face-down for that reason.
- **No held props unless named singly.** Hands are where image models fail.
- **Name real places and objects** - a South African kitchen, a school jersey,
  a minibus taxi - never generic "African" scenery. Specificity is what keeps
  it from becoming pastiche.
- **No two slides in a branch may photograph the same moment.** Differ on at
  least two of: setting, time of day, camera position, and how many people are
  in frame. Slides 01 and 03 first came back as the same picture - same boy,
  same table, same window - because the prompts differed only in lighting and
  in an idea ("going back over an earlier lesson"). A model cannot render
  "earlier". Make the difference photographable, or it will not exist.
- **A device rests on something named.** "Propped-up" describes the result,
  not the support, and the model answers it with a phone standing upright on
  nothing. Say what it leans against - a stack of exercise books, a small
  folding stand - and say it is touching them. Same reason every screen is
  angled away: state the physical fact, not the intention.
- **Nobody lounging.** Learners are shown upright and purposeful - at a
  table, book open, pen in hand. No lying on beds, no slouching, no
  night-time bedrooms, no idle scrolling. This is a study product: the
  posture in the picture is the habit being taught, and slide three is
  reached before the student has watched a single lesson.
- **Photograph, not film still**: no cinematic grade, no motion blur, no flare.

## One thing to fix elsewhere

`intro_page.dart`'s first slide caption still reads "Follow Grandmaster and Big
John" - names the roster no longer uses. The `caption_in_app` fields here carry
the corrected wording ("the subject's expert and simplifier"); the app copy
needs the same edit.
