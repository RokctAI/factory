### subtopic_1 — From Investigation to Brief: One Sentence That Names the Need
**Assistant:** Why can the brief not just say LED and float switch when the whole team already agrees on them?

**Tutor:** Because agreement in week 3 is not the same as being right, and a brief that names the circuit locks the team into it before the sketches have tested it. Suppose the float switch turns out to be unavailable in town, or the LED is invisible in the afternoon sun off the kitchen window. A brief that said LED float switch indicator has now failed, and the team either breaks its own brief or builds something it knows is wrong. A brief that says warn the household clearly when the tank is nearly empty is still true, and the team can move to probes and a flashing LED, or two LEDs, without rewriting anything. The circuit belongs in the sketches and the final circuit diagram, where it can be compared with alternatives. Keeping the brief about the need also earns the Design marks, because examiners look for exactly this separation of problem from solution.

***

### subtopic_2 — Specifications for an Electronic Device
**Assistant:** How do I turn battery life into something we can actually test in a school term?

**Tutor:** By testing the thing that determines it, the current, instead of waiting six months. Battery life is the battery's capacity divided by the current drawn. A 4.5 volt pack of three AA cells holds roughly 2000 milliampere-hours; to last six months, about 4400 hours, the average current must be under about 0.5 milliamperes. So the specification is written in two parts: the device must draw less than 0.5 milliamperes when the tank is full, measured with a multimeter on the milliamperes range in series with the battery, and the LED current when warning must be under 10 milliamperes. Both can be measured in a minute on the bench. If the standby current is close to zero, because the sensor is an open switch until the level drops, the test passes easily; if a transistor circuit is drawing a few milliamperes all the time, the test fails and the team knows to add a switch or redesign before building the model.

***

### subtopic_3 — Constraints, Evaluation Criteria and Team Agreement
**Assistant:** What happens if the team cannot agree on a specification?

**Tutor:** The investigation decides, and if the investigation is silent, the team goes back and asks. Most disagreements in a brief are really disagreements about the user: one member thinks a buzzer is essential, another thinks it is annoying. The interview says the grandmother wants a light and no sound at night, so the specification becomes a visible warning with any sound switchable off, which gives both members something and the user what she asked for. If the investigation genuinely has no answer, for instance on how large the indoor unit may be, the right move is a short extra question to the user or a measurement of the windowsill, recorded as an addition to the investigation, rather than a vote. A brief that rests on evidence is easy to defend in the presentation; a brief that rests on who argued loudest is not.
