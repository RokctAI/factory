### subtopic_1 — Switches in Series: AND Logic
**Assistant:** If electrons really move from negative to positive, why do we draw it the wrong way?

**Tutor:** Because the convention was fixed before electrons were discovered, and when the discovery came it turned out not to matter for designing circuits. Every rule about series and parallel, every calculation with voltage, current and resistance, and the behaviour of every component works out identically whether you imagine positive charge moving one way or negative charge moving the other; only the arrow flips. Changing the convention would have meant redrawing every diagram, remarking every diode and rewriting every textbook on the planet for no practical gain, so engineers kept conventional current and physicists note the electron direction when it matters, for example inside a television tube. For this course and the PAT, draw current from positive to negative, and when you meet the diode and LED next week, remember that the arrowhead of the symbol points the way conventional current is allowed to go.

***

### subtopic_2 — Switches in Parallel: OR Logic
**Assistant:** Can I get AND and OR without switches, from a sensor?

**Tutor:** Yes, and that is exactly what happens in the PAT device, because a sensor is just a switch that something other than a hand operates. A float switch is closed by water, a reed switch by a magnet, a pressure mat by a foot, and later in the term a transistor driven by a light-dependent resistor or a thermistor acts as a switch closed by darkness or heat. Each one can sit in series or in parallel with other switches exactly like a toggle. So a night light that comes on when it is dark and the enable switch is on is an LDR-transistor switch in series with a manual switch, which is AND; a tank alarm that sounds when the level is low or the test button is pressed is a float switch in parallel with a push button, which is OR. The logic is the arrangement; what closes each switch is up to the designer.

***

### subtopic_3 — Conventional Current From Positive to Negative and Reading Logic in Devices
**Assistant:** How do I handle a rule with three conditions in the exam?

**Tutor:** Translate it word by word into series and parallel, building up in pieces. Take the buzzer sounds when the tank is low and the silence switch is on, or when the test button is pressed. First, low and silence-on is two conditions that must both hold, so the float switch and the silence switch go in series as a pair. Second, that whole pair or the test button is enough, so the pair is placed in parallel with the test button. Finally the combined switch network sits in series with the buzzer and the battery. Draw it in that order and label each switch with its condition. The truth table for three switches has eight rows; fill it by asking, for each row, whether there is a complete path. Checking two or three rows against the words in the question, such as all open gives off and test button alone gives on, catches most mistakes.
