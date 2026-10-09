# Part 1 — Expert

This session covers drawing circuits: an LED with a 470 ohm resistor, a switch and a 4.5 volt battery, and an LDR with a buzzer on a 3 volt battery. The anchor is a pair of breadboards on a bench in Mahikeng, the first holding the LED circuit lit by a push of its switch, the second holding an LDR, a transistor and a small buzzer that falls silent when a torch is shone on the LDR and sounds again under a cupped hand. The governing idea is that a correctly drawn circuit diagram, with standard symbols, every value written and polarity shown, is a prediction of what the built circuit will do, and that building to the diagram and testing against it closes the loop between design and making. Drawing these two circuits correctly, explaining their operation and building and testing them are examinable and are the core skills of the PAT Make stage.

## Subtopic: Drawing the LED Circuit: 470 Ohm Resistor, Switch and 4.5 Volt Battery

The LED circuit is drawn as a single loop. Battery on the left, three cells drawn as a battery symbol and labelled 4.5 V, positive at the top. A wire from positive to a switch, labelled with its type, a push-to-make or an SPST. From the switch to a resistor, a rectangle labelled 470 ohms. From the resistor to the LED, the diode symbol with its two arrows, triangle pointing away from the resistor toward the battery's negative side, labelled red LED or with its colour. From the LED's cathode back to the battery's negative terminal. Four components, one loop, straight lines, right-angle corners, no junction dots because nothing branches.

Tracing the loop predicts the behaviour. With the switch open there is a gap; no current, LED off. With the switch closed, conventional current leaves the positive terminal, passes the switch, drops about 2.5 volts across the resistor, passes through the LED from anode to cathode dropping about 2 volts and lighting it, and returns to negative. The current is 2.5 over 470, about 5.3 milliamperes, safe and visible. If the LED were drawn reversed, the trace would predict no light, and the diagram would be wrong before anything was built.

Variations examiners ask for: the same circuit with a second LED in series needs the two LEDs to share 4 volts, leaving 0.5 across the resistor, marginal on 4.5 volts; two LEDs in parallel need a resistor each; a 6 volt battery needs a 390 ohm resistor for the same current, or the 470 can stay for a slightly brighter 8.5 milliamperes, still safe. Each variation is drawn and traced before being built, which is the design habit the course teaches.

The questions for this section are with you now: drawing the LED circuit component by component, tracing it to predict the current and behaviour, and the variations.

## Subtopic: Drawing the LDR and Buzzer Circuit on a 3 Volt Battery

The LDR and buzzer circuit on 3 volts needs a transistor, because the LDR cannot drive a buzzer directly. Battery on the left, two cells labelled 3 V. From positive, two paths. The first path is the sensing divider: a fixed resistor, 10 kilohms or a variable resistor for adjustment, from positive down to a junction, then the LDR from the junction to negative. The second path is the load: the buzzer from positive to the transistor's collector, the emitter to negative. The junction of the divider connects through a base resistor, 10 kilohms, to the base. The buzzer is labelled with its voltage and polarity, since most small electronic buzzers have a positive lead.

Tracing it predicts the behaviour. In bright light the LDR's resistance is low, a few kilohms or less, so the junction is pulled close to negative; the base voltage is below 0.6 volts, the transistor is off, and the buzzer is silent. When the light falls, the LDR's resistance rises to hundreds of kilohms, the junction is pulled up toward positive by the fixed resistor, the base passes 0.6 volts, the transistor turns on and the buzzer sounds. Light falls, buzzer sounds: a drawer alarm, a cupboard alarm or a dusk reminder. Swapping the LDR and the fixed resistor gives the opposite, a buzzer that sounds when light arrives, a fridge-door or jewellery-box alarm.

On 3 volts the margins are tight: the base needs 0.6 volts, the buzzer wants most of the rest, and a fresh pair of cells is needed. This is why the LED circuit uses 4.5 volts and why many transistor circuits are happier on 4.5 or 6. The variable resistor in the divider lets the user set the light level at which the alarm trips, turned until the buzzer just stops in the light the device will live in. The circuit is drawn with every value, the transistor labelled with its type and its three legs marked C, B, E.

The questions for this section are with you now: drawing the LDR, divider, transistor and buzzer circuit, tracing it to predict when the buzzer sounds, and the inverted version and setting the threshold.

## Subtopic: Building Both on a Breadboard and Testing Against the Diagram

The breadboard is the tool for building without soldering. Its holes are connected in short rows of five across the middle and in long rails down the sides for the supply. Components push into the holes; wires link rows. The LED circuit is placed first: battery clip to the rails, red to positive, black to negative; the switch across two rows; the resistor from the switch's row to a new row; the LED from that row, long leg in, to a row linked to the negative rail. Before the battery is connected, the build is checked against the diagram, component by component and connection by connection, by reading the diagram and touching each part.

Testing is done against the prediction. Connect the battery, press the switch: the LED should light at a moderate brightness. If it does not, fault-find in the order learnt: battery and clip, LED polarity, which is the usual culprit, resistor in place, switch rows. A multimeter across the resistor should read about 2.5 volts with the switch closed and across the LED about 2 volts, matching the trace. Record the readings beside the diagram; measured values that match predicted values are the evidence that the diagram was right.

The LDR and buzzer circuit follows the same method, with extra care over the transistor's legs and the buzzer's polarity. Test by covering the LDR: the buzzer should sound; uncover it in good light: silence. Adjust the variable resistor to set the threshold. If the buzzer sounds continuously, the fixed resistor may be too small or the light too dim; if it never sounds, the LDR may be in the wrong position or the transistor reversed. Each test and its result is recorded. The error museum, four exhibits. One: LED in backwards, the most common fault on any bench. Two: rows miscounted so two components are not actually joined. Three: transistor legs in the wrong order. Four: building before checking the build against the diagram, so a wiring slip is blamed on the design.

The questions for this section are with you now: breadboard layout and building the LED circuit, testing against predicted readings, and building and testing the LDR buzzer circuit.

# Part 2 — Simplifier

Now the same lesson again with the two breadboards on the bench in Mahikeng — plain words, same facts.

## Subtopic: Battery, Switch, Resistor, LED, in a Loop

LED circuit, one loop. Battery, 4.5 volts, plus at the top. Wire to a switch. Switch to a 470 ohm resistor. Resistor to the LED, triangle pointing toward minus. LED back to minus. Straight lines, corners, no dots.

Trace it. Switch open: gap, dark. Switch closed: 2.5 volts on the resistor, 2 on the LED, about 5 milliamps, lit. Drawn backwards, the trace says dark before you build.

Variations: two LEDs in series is tight on 4.5 volts; two in parallel need a resistor each; 6 volts wants 390 ohms or the 470 for a bit brighter.

Keep battery, switch, resistor, LED, in a loop in mind and try the questions for this part: the LED circuit.

## Subtopic: Light Falls, Buzzer Sounds

LDR buzzer on 3 volts. Battery, plus at the top. Two paths. Path one: a 10 kilohm resistor from plus to a junction, LDR from the junction to minus. Path two: buzzer from plus to the collector, emitter to minus. Junction through 10 kilohms to the base.

Trace it. Bright: LDR low, junction near minus, base under 0.6, transistor off, quiet. Dark: LDR high, junction pulled up, base over 0.6, transistor on, buzzer sounds. Light falls, buzzer sounds. Swap the LDR and the resistor to get the opposite.

3 volts is tight: fresh cells. A variable resistor sets the light level. Label the transistor type and its legs.

Hold light falls, buzzer sounds in mind and try this part's questions: the LDR buzzer circuit.

## Subtopic: Build What You Drew, Then Check It

Breadboard: rows of five joined across the middle, rails down the sides. Battery clip to the rails. Switch, resistor, LED row by row, long leg toward plus. Before the battery goes on, check every part against the diagram.

Test: press the switch, LED lights. No? Battery, LED backwards, resistor, switch rows. Meter: about 2.5 across the resistor, about 2 across the LED. Write them down next to the diagram.

LDR circuit the same way, careful with transistor legs and buzzer plus. Cover the LDR: sound. Uncover: quiet. Set the variable resistor. Always on? Resistor too small or room too dark. Never on? LDR in the wrong place or transistor backwards.

Pocket summary of the lesson. The LED circuit is a 4.5 volt battery, a switch, a 470 ohm resistor and an LED in one loop, drawn with values and polarity and traced to predict about 5 milliamperes. The LDR buzzer circuit on 3 volts uses a resistor and LDR divider feeding a transistor base through a resistor, with the buzzer in the collector circuit, so the buzzer sounds when light falls. Both are built on a breadboard to the diagram, checked before power, tested against the predicted readings and fault-found in order.

Hold build what you drew, then check it, and take the final questions of the lesson: building and testing.
