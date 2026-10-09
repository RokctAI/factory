# Part 1 — Expert

This session covers the circuit diagram and 3D sketch of the device and the team's choice of a final solution. The anchor is the Rustenburg team's desk with three A4 sheets, each holding a circuit diagram above a pencil sketch of a small box by a window and a sensor on a tank, and the brief pinned beside them so that each idea can be ticked against the numbered specifications. The governing idea is that an electronic device idea is communicated by two complementary drawings, the circuit diagram giving the connections in standard symbols with every component valued and polarised, and the 3D sketch giving the enclosure, the user's view and the placement of components, and that the final choice is made by comparing each idea against the brief's specifications and constraints rather than by preference. Producing a correct circuit diagram and a labelled 3D sketch for a design idea and justifying a team choice are examinable.

## Subtopic: Drawing the Circuit Diagram for Each Idea

A circuit diagram for a design idea is drawn to the standards revised earlier in the term: standard symbols, straight wires with right-angle corners, junction dots where wires join, the supply on the left with positive at the top, and the signal flowing left to right from sensor to output. Every component carries its value or type: the battery as 4.5 V, each resistor with its ohms, the LED with its colour, the transistor with its type number if one is used, the switch with its kind. Polarised components, the battery, the LED, any diode, the capacitor if electrolytic, are drawn the right way round, with the LED's triangle pointing from positive toward negative.

Idea A: a 4.5 volt battery, a float switch that closes when the level falls, a 470 ohm resistor and a high-brightness red LED in series, with a push-button test switch in parallel with the float switch. Idea B: a 4.5 volt battery, two probes in the tank acting as a switch that opens when the water drops below them, a transistor arranged so that an open probe pair turns it on, a 470 ohm resistor and a flashing LED, and a slide switch to silence an optional buzzer in parallel with the LED. Idea C: like A but with a reed switch on the tank wall closed by a magnet on a float, sealed from the water.

Each diagram is checked by tracing the loop: from positive, through the sensor, through the resistor and LED, back to negative, and asking what happens when the sensor changes state. If the LED is lit when the tank is full and dark when it is low, the logic is inverted and the diagram is wrong, not the idea. Checking the diagram on paper, before any building, is the habit that saves components and time, and it is a skill examiners test directly by asking what a given circuit does when a switch is closed.

The questions for this section are with you now: diagram standards with values and polarity, the three ideas as circuits, and checking the logic by tracing.

## Subtopic: The 3D Sketch: What the Device Looks Like and Where the Circuit Lives

The 3D sketch shows the device as an object: the indoor indicator unit as a small box on the windowsill with the LED on its front face and the test button beside it, the battery holder inside shown with a cut-away or a dotted outline, the wire leaving the back; the outdoor sensor unit on the tank, the float switch or probes through the lid or wall, its small housing and the wire running down the stand. A figure or a hand gives scale. The sketch is freehand, in pencil, with the main parts labelled, and it shows the user's view, which for the indicator is from the kitchen side of the window.

The sketch must agree with the circuit diagram. Every component on the diagram appears somewhere in the sketch, placed where it will actually go: the LED on the face, the resistor and any transistor on a small board inside, the battery in its holder, the switches reachable, the sensor at the tank. A sketch that shows a tiny sleek box while the diagram calls for a three-cell battery holder has a problem that is better found now than when the box will not close. Dimensions are approximate but written: box about 90 by 60 by 30 millimetres, wire 12 metres, sensor housing about 50 by 50.

Two more sketches may help: an artistic impression of the device in place, the box on the sill with the tank seen through the window, for the presentation; and a note on materials, a plastic project box or a recycled container for the indoor unit, a sealed film canister or pipe fitting for the sensor housing, cable ties and a conduit for the wire. Costs are estimated beside the sketch from the kit list and the shop's prices.

The questions for this section are with you now: the content of the 3D sketch for both units, agreement between sketch and circuit, and the artistic impression and materials note.

## Subtopic: Comparing Ideas Against the Brief and Choosing as a Team

Choosing is done against the brief. The team draws a table: specifications down the side, ideas across the top, and fills each cell with a tick, a cross or a note. Detect below one fifth: A, yes, float at that height; B, yes, probes at that height; C, yes, magnet float. No opening of the tank: A needs the lid drilled; B needs two holes; C needs none, the reed switch is outside. Visible at ten metres: A standard red LED, borderline; B flashing high-brightness, yes; C as A. Standby current under 0.5 milliamperes: A and C, zero, the switch is open; B, a transistor circuit draws a small current all the time, needs checking. Survives rain: A's float switch is inside the tank, fine; B's probes corrode over months; C is sealed. Cost: A cheapest; B dearest; C in between.

The table makes the strengths plain. C's sealed reed switch and zero standby current are the best sensor; B's flashing high-brightness LED is the best output; A is the simplest to build. The team's final solution combines them: the reed switch and magnet float from C, the flashing high-brightness LED and silenceable buzzer from B, with the simple series circuit of A and no transistor, because the reed switch can carry the LED current directly. The choice is written as a paragraph with the reasons pointing to specification numbers.

The final circuit diagram and 3D sketch are then redrawn clean for the portfolio, and a parts list with costs is attached. The error museum, four exhibits. One: a circuit diagram without values, so nobody knows which resistor. Two: a sketch that cannot hold the battery the diagram requires. Three: choosing the idea whose author argued hardest, without the table. Four: an LED drawn the wrong way round, which is caught only when the model stays dark.

The questions for this section are with you now: the comparison table against specifications, combining ideas into a final solution with reasons, and the clean final drawings.

# Part 2 — Simplifier

Now the same lesson again with the three A4 sheets and the pinned brief on the desk in Rustenburg — plain words, same facts.

## Subtopic: Symbols for the Insides

Circuit diagram rules: standard symbols, straight wires, dots at joins, battery on the left with plus at the top, sensor to output left to right. Every part gets its value. LED and battery the right way round.

Idea A: battery, float switch, 470 ohms, bright red LED, test button in parallel with the float. Idea B: probes, a transistor, 470 ohms, a flashing LED, a buzzer with a silence switch. Idea C: like A but a reed switch and a magnet on a float, all sealed.

Trace the loop. When the level drops, does the LED light? If it lights when full, the logic is backwards. Fix it on paper.

Keep symbols for the insides in mind and try the questions for this part: the circuit diagrams.

## Subtopic: A Picture of the Outside

3D sketch: the box on the sill with the LED and test button on the front, battery shown inside, wire out the back; the sensor on the tank with its wire down the stand. A hand for scale. Pencil, labelled, from the user's side.

Everything on the diagram must appear in the sketch, where it really goes. A box too small for three cells is a problem; find it now. Write rough sizes.

Extra: a picture of it in place for the presentation, and a note on materials and costs.

Hold a picture of the outside in mind and try this part's questions: the sketch.

## Subtopic: Tick the List, Pick One

Table: specifications down, ideas across. Tick, cross, note. Opening the tank: C wins, reed switch outside. Visible at ten metres: B wins, flashing bright LED. Standby current: A and C zero, B draws a little. Rain: C sealed, B's probes corrode. Cost: A cheapest.

Combine: C's sealed reed switch, B's flashing LED and silenceable buzzer, A's simple series circuit. Write the choice with the specification numbers.

Redraw the final diagram and sketch clean, add the parts list and costs.

Pocket summary of the lesson. Each design idea is shown by a circuit diagram in standard symbols with every value and polarity, and by a labelled 3D sketch of the device as the user sees it with the components placed inside; the two must agree. Ideas are compared in a table against every specification and constraint of the brief, and the final solution, often a combination, is chosen with reasons pointing to the brief and then drawn clean for the portfolio.

Hold tick the list, pick one, and take the final questions of the lesson: the choice.
